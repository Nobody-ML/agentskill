# PDF Layout Translation Playbook（保排版翻译 / 功能保持）

适用：
- Track：Software
- Level：L3（强制）

目标：
把“翻译 PDF”做成 **PDF 版式外科系统**：
- 保留背景与页面对象结构
- 删除原文字（不白底覆盖）
- 在原 block bbox 内重排译文（不溢出、不重叠）
- 尽可能保留或重建交互功能（链接/目录/书签/命名目标/注释/表单）

这是一个 playbook：用于指导 Plan 写到足够深、足够可执行，不是默认实现方案，也不是输出下限。

对应门禁：
- `protocols/00-hard-gates.md`：G2/G3/G4/G6/G7/G8
- `protocols/04-validation-real-data-first.md`：视觉/几何/功能验证
- `library/format-surgery-systems.md`：通用外科模式

---

## 0) Plan Mode 研究起步包（必须联网检索并落盘）

这类任务的 Plan 失败，通常不是因为“实现写得不够多”，而是因为 **关键外部事实没查清**：
- 库的边界行为（redaction 是否影响 annotation）
- 坐标系与旋转页
- MinerU 不同 backend/版本的 JSON 差异
- 字体与中文排版可行性
- 数字签名、加密与线性化等 PDF 工程约束
- 渲染 QA 在不同引擎/阅读器的差异

因此，进入 Plan 前先按下面主题做高质量检索，并把来源写进 Plan 的 Research Log（每条来源必须写 Extracted facts + Impact）：

1) **MinerU**
   - middle.json/schema 的字段含义、坐标系、不同 backend（例如 VLM vs pipeline）的 bbox 表示差异
   - 版本升级的 breaking changes（至少记录版本/日期）
2) **PyMuPDF（fitz）**
   - text extraction 结构（block/line/span）与 style 字段
   - redaction / text 删除的行为与副作用（尤其 annotation/link）
   - 写入文本盒（insert_textbox / HTML 文本盒）与字体/换行控制
   - outline/toc 与 link annotations 的读取与写回
3) **pikepdf / qpdf（低层 PDF）**
   - 加密/权限/修复、线性化（linearization）、对象树检查
   - named destinations、page labels、attachments、metadata 等对象的读写入口
4) **渲染与 QA 引擎**
   - pdfium / poppler（或同级渲染器）用于渲染对比与兼容性抽检
5) **数字签名与不可修改约束**
   - 预期：修改正文往往会导致签名失效；Plan 必须把这件事当作“必须告知”的交付事实

硬规则：
- 未做上述研究就写 Plan，视为 Research Gate（G3）不通过。
- 任何“据说/一般/应该”都必须在 Research Log 里找到可追溯来源，否则只能写成假设（Assumption）并在 Validate 中安排验证。

## 1) 推荐端到端流水线（必须写入 Plan）

```text
输入 PDF / 文件夹
  ↓
预检：类型、权限、签名、页面盒、字体、链接、目录、扫描页比例
  ↓
MinerU 解析：layout middle.json / spans / blocks / bbox
  ↓
PyMuPDF 二次抽取：真实文本样式、字体、字号、颜色、旋转、链接与目录对象
  ↓
构建 Layout DOM：Page → Column → Block → Line → Span → Unit
  ↓
保护 token：公式、引用、URL/DOI、代码、链接锚点
  ↓
翻译：结构化输出（JSON schema）+ 缓存 + 批处理 + 术语表
  ↓
排版适配：字体选择、字号搜索、换行、fit solver、必要时二次压缩改写
  ↓
删除原文字：透明 redaction / 内容流处理（不白底）
  ↓
写入译文：文本盒写入（HTML/CSS 或 shaping 引擎）
  ↓
恢复功能：链接/目录/书签/命名目标/注释/元数据
  ↓
QA：渲染对比、溢出/重叠检测、旧文字残留、链接可点击、目录可跳转
  ↓
输出 translated PDF + sidecars + 报告（支持断点续跑）
```

Plan 的硬要求：
- 不能只写“用 PyMuPDF 写回”这种一句话。必须写出每阶段候选技术、推荐技术、风险与验证。

### 1.1 阶段→技术→验证映射（PDF 任务的最小基线）

Plan 中必须出现“阶段→技术→验证”的表；下面给出一个可直接改写/扩展的基线（不是固定实现）：

| Stage | Goal | Inputs → Outputs | Candidate tech | Recommended baseline | Key risks | Validation & evidence |
|---|---|---|---|---|---|---|
| Preflight | 分类与路由 | pdf → preflight.json | PyMuPDF / pikepdf | PyMuPDF +（按需）pikepdf | 加密/签名/权限导致不可写 | preflight.json + 统计 |
| Layout parse | 语义与几何 | pdf → middle.json | MinerU / 其它 parser | MinerU | 版本/backends 差异 | schema 记录 + 样例页对齐 |
| Ground truth | 对象真相 | pdf → rawdict/links/toc | PyMuPDF | PyMuPDF | 坐标/旋转不一致 | bbox 可视化抽检 |
| Functional snapshot | 功能快照 | pdf → func_snapshot.json | PyMuPDF / pikepdf | PyMuPDF | redaction 误伤 annotations | snapshot 完整性检查 |
| Layout DOM (IR) | 中间表示 | middle/raw → dom.json | 自定义 schema | 自定义 schema | ID 不稳定导致不可续跑 | schema 校验 + diff |
| Token protect | 保护不改写片段 | dom → protected_dom | 规则/正则/分类器 | 规则优先 | token 丢失导致链接/引用断裂 | token QA |
| Translate | 结构化翻译 | units → translated | OpenAI-compatible / 其它 | OpenAI-compatible + cache | 解析脆弱/重复翻译 | JSON schema + cache 命中率 |
| Typeset/Fit | 装入 bbox | translated → fitted | PyMuPDF textbox / Pango/HarfBuzz | textbox →（升级）shaping | 溢出/重叠/不可读 | overflow/overlap 报告 + 截图 |
| Erase text | 删除原文字 | pdf → redacted pdf | transparent redaction / 内容流编辑 | transparent redaction | 背景破坏/链接丢失 | 渲染对比 + links 计数 |
| Write text | 写入译文 | redacted → translated pdf | insert_textbox / HTML textbox | insert_textbox/HTML | 字体缺字/渲染差异 | 多页抽样渲染 |
| Restore function | 恢复功能层 | snapshot → restored | PyMuPDF insert_link / pikepdf | PyMuPDF | 跳转失效/热区偏移 | 统计+抽样点击证据 |
| QA | 渲染/几何/功能 | pdf → report | PyMuPDF render / pdfium/poppler | 至少 2 渲染器抽检 | 单一渲染器误判 | report + screenshots |
| Batch/Resume | 批处理与恢复 | dir → outputs | workdir + markers | workdir + markers | 单页失败拖垮全局 | pages_done + summary |

说明：
- Candidate tech 与推荐基线必须写“为什么”，不能只列名词。
- 任何阶段的“推荐=省略验证”都属于违规：推荐路线只改变优先级，不改变证据门禁。

---

## 2) 阶段一：PDF 预检（Domain Preflight）

目的：
- 决定文件是否适合高质量替换
- 决定 pipeline 路由（born-digital / 扫描页 / 混合）
- 提前暴露“不可实现/需要人工/需要降级”的页或文件

建议输出工件：
- `preflight.json`（或等价报告）

预检最小字段（示例）：
- page_count / page_size / rotation
- is_encrypted / can_modify / has_digital_signature
- has_outline / has_links / has_forms
- has_named_destinations
- has_page_labels / has_attachments / has_metadata_changes_risk（按需）
- born_digital_ratio / scan_page_ratio
- route_decision（recommended pipeline）
- blockers（缺权限/签名/加密等）

建议把 `preflight.json` 写成“可机器读取的路由决策”，不要只写一段文字。最小示例：

```json
{
  "input_path": "paper.pdf",
  "output_path": "paper.zh-CN.pdf",
  "page_count": 12,
  "page_boxes": {
    "0": {"mediabox": [0, 0, 595.28, 841.89], "cropbox": [0, 0, 595.28, 841.89], "rotation": 0}
  },
  "is_encrypted": false,
  "can_modify": true,
  "has_digital_signature": false,
  "has_outline": true,
  "has_links": true,
  "has_forms": false,
  "has_named_destinations": true,
  "has_page_labels": false,
  "has_attachments": false,
  "born_digital_ratio": 0.96,
  "scan_like_pages": [7],
  "route_decision": "born-digital",
  "blockers": []
}
```

`route_decision` 建议枚举（写进 Plan 的 Constraints/Boundaries 与 Roadmap）：
- `born-digital`：允许“透明删除文字 + 重排写回 + 功能快照/恢复”
- `mixed`：born-digital 为主，但包含 scan-like 页；必须把 scan-like 页的路线写进 Fallback Register
- `scan-like`：默认进入“图像路线（inpainting/贴片/人工审校）”；不得静默假装能无损删除文字
- `blocked`：加密/权限/签名/损坏导致不可修改；必须停线并把阻塞点回给用户

门禁：
- 预检报告缺失 → 不进入后续实现（否则后续验证不可控）。

数字签名处理（必须在 Plan 写清并进入交付说明）：
- 一般情况下，只要改动正文内容，原签名就会失效（即便增量保存）。
- 系统必须保留原文件，并在输出报告中显式标记：译文版不保持原签名有效性。

工具建议（写入 Plan 的 Candidate tech）：
- PyMuPDF：快速检查 page box、links/toc、抽样渲染、后续写回
- pikepdf/qpdf：低层对象检查、修复、线性化、命名目标、页面标签、附件/元数据（按需）

---

## 3) 阶段二：MinerU 做版面语义，PyMuPDF 做对象真相

MinerU（版面语义）负责：
- 阅读顺序、多栏结构、块级分类（title/text/list/caption/footnote/reference）
- span/line/block 的 bbox
- 公式/表格/图片及其关联（用于保护 token 与后续策略）

PyMuPDF（对象真相）补充：
- 字体名、字号、颜色、flags（粗斜体等）、旋转、字符 bbox
- page box、crop box、rotation
- 链接、注释、目录对象

关键门禁：坐标统一
- 内部 DOM 统一采用：origin=top-left、unit=pt、y_down_positive=true
- MinerU bbox 若为归一化，需要乘 page_size 转 pt

建议在 Plan 的 Specification 里把坐标约定写成显式字段（避免实现期“猜坐标”）：

```yaml
coordinate_system:
  origin: "top-left"
  unit: "pt"
  x_right_positive: true
  y_down_positive: true
  rotation_handling: "normalize_to_upright" # 或 "preserve_page_rotation"
```

归一化 bbox（0..1）→ pt（示例）：

```python
x0_pt = x0_norm * page_width_pt
y0_pt = y0_norm * page_height_pt
x1_pt = x1_norm * page_width_pt
y1_pt = y1_norm * page_height_pt
```

旋转页（rotation != 0）的处理必须在 Plan 写清并在 QA 抽检验证：
- 方案 A：在 IR 层把 bbox 先归一化到“正向页面”，后续所有写回都在统一坐标系处理
- 方案 B：保留 page rotation，但每次 bbox/写回都走同一个变换函数（更容易出错）

验证方式（最低要求）：
- 抽样 1–3 页输出 `bbox_overlay.png` 或等价渲染证据：在渲染图上把 block/line bbox 画出来，确认对齐

MinerU 版本/后端适配（必须写入 Plan）：
- 必须记录 MinerU 的版本与 backend 类型，并在 IR 层做兼容适配（不要把某一种 middle.json 结构硬编码成唯一结构）。
- Plan 的 Research Log 必须包含：middle.json 字段含义、bbox 表示与已知 breaking changes。

---

## 4) 阶段三：抽取并保护 PDF 功能层

必须在任何 redaction/内容写回之前快照：
- TOC / outlines（目录/书签）
- page links（链接热区、目标）
- annotations / widgets（注释/表单）
- named destinations（命名目标）
- page labels（页面标签）
- metadata / attachments（元数据/附件）

建议把功能层快照落成 `func_snapshot.json`（最小示例；可扩展）：

```json
{
  "toc": [],
  "page_links": {
    "0": [
      {"kind": "LINK_GOTO", "from": [120.1, 300.2, 140.5, 312.8], "page": 10, "to": [72, 100], "xref": 123}
    ]
  },
  "annotations": {},
  "widgets": {},
  "page_labels": {},
  "named_destinations": {},
  "metadata": {},
  "attachments": []
}
```

风险点：
- redaction 可能删除重叠 links（先 snapshot，再删除文字，再重建）

进阶（生产级）建议：
- 链接锚点映射：把链接覆盖的文本保护成 token，翻译后用 token 在新文本中的 bbox 重建热区

“链接锚点映射（Link Anchor Mapping）”的最小算法（建议写进 Plan 的 Restore/QA 小节）：
1) 在原 PDF 中读取每个 link rect 覆盖的可见文本（例如 `[12]`、`Figure 3`、目录条目）。
2) 在 IR 层把该文本替换为占位符 token（例如 `<LINK_42>`），并把 token 写入 protected_tokens。
3) 翻译时要求严格保留 token（结构化输出 + schema 校验）。
4) typeset 时记录 token 在新文本中的 glyph bbox（或近似 bbox），得到 `token_bbox_map`。
5) 写回译文后，用 `token_bbox_map` 重建 link 热区（`insert_link/update_link`），并把证据写入 QA 报告。

注意：
- “只做 links count 对比”属于 MVP 级风险控制：能发现明显丢失，但无法解决“热区偏移”的问题。
- 生产级方案必须把 “token→bbox→重建” 写成可执行路线，并在 Roadmap 里排期。

---

## 5) 阶段四：构建 Layout DOM（中间表示）

最小数据结构（示意）：
- DocumentLayout：pages、toc、metadata、named_destinations
- PageLayout：page_index、width/height/rotation、blocks
- Block：id、block_type、bbox、reading_order、lines、original_text、protected_text、translated_text、style、links

建议在 Plan 的 Specification → Data Model 中给出更具体的字段（示例，不是固定实现）：

```python
@dataclass
class TextStyle:
    font_family_source: str
    font_size_pt: float
    color_rgb: tuple[int, int, int]
    bold: bool
    italic: bool
    align: str
    line_height: float
    writing_mode: str

@dataclass
class LinkAnchor:
    link_id: str
    kind: str
    target: dict
    original_rect: list[float]  # [x0,y0,x1,y1]
    token: str                  # "<LINK_42>"

@dataclass
class Block:
    id: str
    page_index: int
    block_type: str  # title/text/list/caption/footnote/reference/header/footer/page_number/...
    bbox: list[float]
    reading_order: int
    original_text: str
    protected_text: str
    translated_text: str | None
    style: TextStyle
    link_anchors: list[LinkAnchor]
    fit_result: dict | None
```

要求：
- Block/Unit 的 ID 必须稳定（用于缓存、断点续跑、QA 报告与 link rebuild）
- 保留原文与译文 sidecar（便于复查与二次迭代）

---

## 6) 阶段五：翻译引擎（结构化、可恢复、可缓存）

Plan 必须写清：
- 翻译单元粒度（block/line/span）
- JSON schema（结构化输出，避免解析脆弱）
- 缓存策略（SQLite/JSONL，key=doc_hash+unit_id+lang+model）
- 术语表与专有名词策略
- 批处理与失败重试策略
- token 保护策略（公式/引用/URL/链接锚点必须保持）

建议把“翻译请求/翻译结果”写成稳定 schema（以便断点续跑、缓存、重试、抽检与审校）。

### 6.1 翻译请求 schema（示例）

```json
{
  "target_language": "zh-CN",
  "domain": "physics",
  "units": [
    {
      "id": "p003_b012",
      "type": "body",
      "text": "For the N-particle system, we choose our unperturbed Hamiltonian...",
      "context_before": "and perturbation theory.",
      "context_after": "using the formalism presented in Chapter 6.",
      "protected_tokens": [
        {"token": "<EQ_1>", "value": "N E_0^{(0+1+2)}"},
        {"token": "<CITE_1>", "value": "(7.70)"},
        {"token": "<LINK_42>", "value": "[12]"}
      ]
    }
  ]
}
```

### 6.2 翻译结果 schema（示例）

```json
{
  "units": [
    {
      "id": "p003_b012",
      "translation": "对于 N 粒子体系，我们选择未扰动哈密顿量……",
      "preserved_tokens": ["<EQ_1>", "<CITE_1>", "<LINK_42>"],
      "needs_review": false,
      "length_risk": "medium"
    }
  ]
}
```

### 6.3 缓存 key 与 SQLite 表（示例）

缓存 key 建议包含：
- normalized_source_text（去掉可变空白/规范化换行）
- target_language / glossary_version / prompt_version / model_name

```sql
CREATE TABLE IF NOT EXISTS translation_cache (
  cache_key TEXT PRIMARY KEY,
  unit_id TEXT,
  source_text TEXT,
  translated_text TEXT,
  source_lang TEXT,
  target_lang TEXT,
  model TEXT,
  glossary_version TEXT,
  prompt_version TEXT,
  created_at TEXT,
  quality_flags TEXT
);
```

### 6.4 批处理与失败重试

Plan 至少要写清：
- 批处理单位（按页/按 block/按文件）
- 可恢复点（哪些产物落盘后算完成）
- 失败重试策略（重试次数、退避、失败隔离到 report）

### 6.5 fit 失败时的二次“压缩译文/改写”

外科任务常见失败不是“翻译错”，而是“译文塞不进 bbox”。Plan 必须定义二次改写策略：
- 当 fit solver 判定 `failed`：触发 rewrite request（压缩译文、保持 token、不丢核心含义）
- rewrite 仍失败：进入 Fallback Register 预定义的路线（标记人工审校/允许小范围扩张/跳过块）

门禁：
- 结构化输出与缓存未定义 → 视为不可续跑，不进入执行。

---

## 7) 阶段六：字体与排版引擎（fit solver）

Plan 必须明确“三档排版能力”，并给推荐路线：

1) **MVP：文本盒引擎（快速落地）**
   - 典型：PyMuPDF 文本盒/HTML 文本盒
   - 风险：精细排版不足，但适合作为 MVP 打通关键门槛

2) **Production：shaping/测量增强**
   - 典型：Pango/HarfBuzz 做文本 shaping 与测量，确保 CJK 与混排质量

3) **Publisher-grade：段落排版系统**
   - 典型：更强断行、禁则、惩罚模型、局部重排与避让

### 7.1 A/B/C 三档更细的技术落点（写进 Plan 的 Candidate Solutions）

**A 档（MVP）**：PyMuPDF `insert_textbox` / `insert_htmlbox`
- 适合：多数 born-digital 论文正文与简单标题/图注
- 优点：实现快；原地写回；易于与 redaction/链接恢复集成
- 风险：极致微排版控制有限；部分字体/混排测量不够精细
- Plan 要写清：`insert_textbox` 与 `insert_htmlbox` 何时用哪个；CSS 怎么控制字体/行距/颜色；溢出判据怎么判断

**B 档（Production）**：Pango + HarfBuzz + Cairo（自研 foreground layer）
- 适合：追求“像 LaTeX 一样优雅”的最终质量；需要更精确 glyph bbox（用于链接热区重建）
- 关键能力：HarfBuzz shaping（字形与定位）+ PangoLayout 段落断行/对齐 + Cairo 绘制
- 风险：工程复杂度更高；需要把排版结果映射回 PDF（overlay 或 content stream）
- Plan 要写清：输出形态（PDF overlay / PDF text operators）、字体嵌入策略、测量一致性验证（多渲染器）

**C 档（备选/重建型）**：HTML/CSS 全页重排（例如 WeasyPrint 等）
- 优点：排版能力强、可得到漂亮 PDF
- 核心问题：通常会“生成新 PDF”，而不是原地修改；功能层对象迁移成本高（目录/命名目标/注释/表单/页面标签/附件等）
- 结论：更适合作为“当原地外科不可控时的备选路线”，不是默认路线

### 7.2 Fit Solver：不要只做“字号缩小”

fit solver 的输出不仅是“是否 fit”，还应落盘为 `fit_result`（用于 QA 与返工）：
- chosen_font / chosen_size / line_height / align
- overflow_area / clipped_glyph_count / rewrite_used
- failure_reason（若失败）

候选参数（示例；Plan 里应按你的目标质量/页面类型给出范围）：

```python
font_size_scale = [1.00, 0.97, 0.94, 0.91, 0.88, 0.85, 0.82, 0.78]
line_height = [1.05, 1.10, 1.15, 1.20]
tracking = [0.0, -0.01, -0.02]  # 中文慎用
rewrite = [False, True]         # fit 失败后触发“压缩译文”
```

评分函数（示例；用于在候选配置中选“最不难看”的那一个）：

```python
penalty = (
    100000 * overflow_area
  + 10000  * collision_area
  + 5000   * clipped_glyph_count
  + 400    * abs(font_size_scale - 1.0)
  + 100    * bad_line_break_count
  + 80     * orphan_punctuation_count
  + 50     * line_count_deviation
  + 20     * raggedness_score
)
```

硬门禁（写进 Plan 的失败判据）：
- 正文不得无限缩小字号；必须设定下限（例如：不低于原字号的 82%，或绝对不低于 6.5pt）
- 触发 rewrite 的条件必须明确（例如：overflow_area>0 且 font_size_scale 已到下限）
- rewrite 仍失败：进入 Fallback Register 预定义路径（人工审校/跳过块/允许小范围扩张），不得执行期临时兜底

### 7.3 中文与混排排版规则（Plan 必须明确）

要接近论文/书籍观感，中文不能“只是换行”。Plan 应至少覆盖：
- 标点避头尾：逗号/句号/分号/冒号/右括号/右引号不在行首；左括号/左引号不在行尾
- 不可拆 token：引用编号 `[12]`、`(7.70)`、单位/变量（`m/s`、`GPU`）、URL/DOI、公式 token 不跨行断裂
- 两栏论文：默认左对齐或轻微两端对齐，避免大字距
- 标题/图注：允许轻微改写以变短，但不得改变编号与 token

fit solver 必须定义：
- 目标：把译文装进 bbox（不溢出、不重叠、字号可读）
- 策略顺序：换行→字号搜索→行距→必要时二次压缩改写
- 失败判据：无法 fit 的块如何处理（必须走 Plan 的 fallback policy，不得执行期擅自兜底）

---

## 8) 阶段七：删除原文字（禁止白底覆盖）

原则：
- born-digital：优先透明 redaction 删除文字对象
- 扫描页：需要单独路线（背景修复/采样贴片/人工审校），必须在 Plan 阶段明确

### 8.1 born-digital：只用 redaction 删除原文字（不填充背景）

推荐策略：
1) 先完成 `func_snapshot.json`（功能层快照），尤其是 links/toc/named destinations。
2) 只用 redaction “删除文字”，不使用 redaction 的 replacement text（排版能力有限且容易难看）。
3) redaction 填充保持透明（不要画白底）。
4) 避免误伤图片/线条/背景块（按需关闭 images/graphics 的处理）。
5) redaction 后再用独立 typeset 引擎写入译文（textbox/htmlbox/shaping）。

要点（写进 Plan 的 Erase 阶段风险与验证）：
- redaction 是按“文字 glyph bbox 与矩形是否重叠”删除文字对象；矩形选取过大容易误删相邻对象
- redaction 可能移除与矩形重叠的链接热区（因此必须快照并重建）

### 8.2 redaction 矩形粒度：不要粗暴用整段 bbox

更稳的策略是“按行/按 span union 生成多个窄矩形”，并排除敏感 span：
- 含公式的行：公式 span 不进入 redaction rect
- 含链接的行：先保护为 `<LINK_*>` token，并在重建阶段恢复
- 表格单元格：矩形不要碰到表格线

示意（伪代码）：

```python
for line in block.lines:
    text_spans = [s for s in line.spans if s.type == "text" and not s.is_equation]
    rect = union([s.bbox for s in text_spans])
    rect = rect.inflate(x=0.5, y=0.2)  # pt 级微扩张
    redaction_rects.append(rect)
```

扫描页/图片型 PDF 的路线（必须在 Plan 预先定义，不得执行期临时兜底）：
1) 图像修复/inpainting：尽量恢复背景后再写译文（复杂背景风险高）
2) 采样贴片：按局部纹理/底色生成贴片（比纯白更接近原背景，但仍是覆盖）
3) 标记为低可信页：进入人工审校流程（把不可控性显式化）

门禁：
- 出现白底覆盖即违反 must_avoid；验证必须 fail。

---

## 9) 阶段八：写入译文（保持背景与质感）

写入要求：
- 不改变页数/页面尺寸
- 译文在原 bbox 内排版
- 字体策略必须覆盖 CJK（缺字要提前处理）

建议在 Plan 中按 block_type 明确写入规则（否则实现期会随手写导致质量漂移）：

**正文（text/body）**
- 使用原 block bbox；优先目标语言正文衬线字体（更接近论文/书籍观感）
- 字号初始值接近原字号；行距建议 1.08–1.18
- 不画背景（overlay=True），避免遮罩底色

**标题（title/heading）**
- 中文标题视觉密度更高：允许轻微缩字号或分两行，但不得压到作者/摘要区域
- 保持对齐方式与粗细（bold/semibold）

**图注/表注（caption）**
- 不移动图/表对象；图注必须在原区域内 fit
- 编号 token（Figure 2 / Table 1）必须保护并回填

**页眉页脚（header/footer/page_number）**
- 默认不翻译页码；期刊页眉可配置翻译或保持
- DOI/版权声明默认不翻译（或仅翻译固定前缀）

**参考文献（references/ref_text）**
- 常见策略：不全文翻译条目，仅翻译“References/参考文献”标题；条目可配置翻译题名

字体策略（Plan 必须写清）：
- 不要依赖源 PDF 的 subset 字体写中文：常见缺字
- 建议准备目标语言字体并做 fallback（生产级需要明确字体许可证）

---

## 10) 阶段九：恢复链接/目录/跳转

保守策略：
- 尽量保持原 links/toc 不变（复制或恢复）

生产级策略：
- token_bbox：根据 token 在新文本中的 bbox 重建链接热区
- toc/bookmarks：保持目标页与坐标语义一致（必要时补底层对象处理）

Plan 的 Restore 阶段至少要覆盖（按快照字段逐项写清“如何恢复 + 如何验证”）：
- `toc`（outline/bookmarks）：数量、层级、目标页与坐标语义保持
- `page_links`：LINK_GOTO / LINK_URI 等类型；支持多矩形（换行 URL）
- `named_destinations`：命名目标的保留/迁移策略（必要时用低层库处理）
- `page_labels`：页面标签（罗马数字/章节编号）是否保留
- `annotations/widgets/forms`：注释与表单的保留策略（MVP 可先声明 non-goal，但必须显式）
- `metadata/attachments`：元数据与附件的迁移/保留策略（按需）

验证建议（写入 QA Plan）：
- 统计对比：toc 项数、links 项数（按页）、named destinations 数量
- 抽样点击证据：目录页、引用跳转、外链 URL 至少各抽检 1–3 个（截图/录屏/日志）

---

## 11) QA（决定能不能生产使用）

必须写入 Plan 的 QA 最小集合：
- 渲染 QA：逐页截图（抽样或全量）+ 可视化对比
- 几何 QA：溢出/重叠/越界检测
- token QA：受保护 token 未丢失
- 功能 QA：links/toc 可点击（至少统计 + 抽样点击 + 证据）
- 多渲染器抽检（按需强制）：至少 2 个渲染引擎（例如 MuPDF + pdfium/poppler）抽样对比，避免单一阅读器偏差
- 报告产物：HTML 或等价报告（含失败页与原因）

建议把 QA 产物结构化（便于复跑与回归），并写入 Plan 的 Evidence Index 约定：

```text
.work/<job_id>/
  qa/
    report.json
    report.html
    screenshots/
      page_0001.mupdf.png
      page_0001.pdfium.png
    diffs/
      page_0001.pixel_diff.png
```

多渲染器抽检的最低策略（写进 Plan）：
- 渲染器 A：MuPDF（PyMuPDF）
- 渲染器 B：pdfium 或 poppler（任选其一即可；目标是“不同实现”）
- 抽样：目录页/引用跳转页/含图片与底色页/含两栏正文页
- 对比：像素 diff（允许小阈值）+ 人工目检（记录证据）

几何 QA 的最低策略（写进 Plan）：
- `overflow`: textbox/htmlbox 返回值或测量值判定
- `collision`: 以 block bbox 为约束，检查相邻 block 是否明显重叠（可先做近似）
- `out_of_box`: 任何 glyph bbox 超出 block bbox 的统计与失败页列表

旧文字残留检查（按需）：
- 若 redaction/写回后仍能选中原文或搜索到原文：判定 fail（必须回溯 erase 阶段）

Fail Criteria 示例：
- PDF 打不开 / 页数变化 / 页面尺寸变化
- links/toc 数量显著减少或功能失效
- 出现白底覆盖或背景被破坏
- 大量溢出/重叠不可接受

---

## 12) 文件夹批处理与断点续跑

必须在 Plan 中定义：
- 输出策略（同级输出、后缀、是否覆盖）
- workdir 结构（preflight/mineru/dom/cache/fitted/qa/pages_done）
- 单页失败策略（隔离失败页，最终报告列出原因）

---

## 13) 推荐工程架构（用于写 Plan 的模块拆分参考）

把系统按职责拆成模块，有助于把 Plan 写深、写清、写可验证：

```text
pdf_translator/
  cli.py
  config.py

  preflight/
  mineru_adapter/
  pdf_extract/
  layout_dom/
  translate/
  typeset/
  function_restore/
  render/
  qa/
```

要求：
- Plan 必须明确每个模块的输入/输出工件与验证点。

建议在 Plan 的 “Architecture / Specification / Workdir” 三处建立一致的 I/O 约定（示例）：
- `preflight/`：`pdf -> preflight.json`（route_decision + blockers）
- `mineru_adapter/`：`pdf -> middle.json`（记录 mineru_version/backend）
- `pdf_extract/`：`pdf -> rawdict.json + links.json + toc.json`（ground truth）
- `layout_dom/`：`middle+raw -> dom.json`（stable ids + styles + anchors）
- `translate/`：`units.json -> translations.json + cache.sqlite`（schema + retry + rewrite）
- `typeset/`：`dom+translations -> fitted_dom.json + fit_report.json`
- `function_restore/`：`func_snapshot.json + token_bbox_map -> restored_objects.json`
- `render/`：`pdf -> page_*.png`（mupdf/pdfium 双渲染）
- `qa/`：聚合 `fit_report + diffs + func checks -> report.html/json`

---

## 14) MVP → Production 路线图（避免一上来无限工程）

建议路线（写入 Plan 的 Milestones）：
- MVP：born-digital 论文跑通（透明删除 + block fit + links/toc 基本保持 + 最小 QA）
- Beta：批处理 + 缓存 + token 保护 + QA 报告 + 失败恢复
- Production：shaping 引擎 + 多渲染器 QA + 扫描页路线 + 合规与许可证
- Publisher-grade：段落排版系统与更强中文排版规则

---

## 15) 最容易踩的坑（把坑写进 Plan 的风险与验证）

Plan 里建议显式列出并逐条给“预防 + 验证证据”：

- 坐标/旋转没统一：表现为写回位置整体偏移（必须做 bbox overlay 抽检）
- MinerU schema/版本变更：表现为 bbox 缺失或归一化解释错误（必须记录版本 + 适配层）
- redaction 矩形过大：误删背景线条/表格边框/相邻文字（必须按行生成矩形 + 抽检）
- redaction 误伤 links：表现为链接热区消失（必须 func_snapshot + rebuild 策略）
- 字体缺字/替换：表现为方框/乱码/渲染差异（必须字体策略 + 多渲染器抽检）
- 只靠缩字号 fit：表现为可读性崩溃（必须 rewrite 路线 + font size 下限门禁）
- QA 只用单一阅读器：表现为换一个阅读器就出错（必须至少 2 渲染器抽检）
- 批处理不可恢复：表现为失败后只能重跑全本（必须 workdir + cache + pages_done）
