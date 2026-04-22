# Plan（节选）— software-pdf-layout-translation

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

Version：v2026-04-20  
Track：Software  
WorkType：Build  
Level：L3  
Current Mode：Plan  
Execution Authorization：required  

---

## 1) User Intent Lock（节选）

```yaml
primary_goal: "把输入 PDF 翻译成目标语言，并生成新的 translated PDF；尽量保持排版与交互功能"
must_preserve:
  - "页数/页面尺寸/背景/底色/插图/公式对象尽量不动"
  - "links/toc/bookmarks/named destinations/annotations/forms 尽量保留或可重建"
must_avoid:
  - "白底覆盖"
  - "执行期擅自兜底/降级"
quality_bar: "译文像重新排过版，且不溢出、不重叠；功能可用"
scope_boundary: "仅在目标项目目录内开发；fixture 只读；输出不覆盖原 PDF"
```

---

## 2) Problem Frame（节选）

这不是“替换字符串”，而是一个 **PDF 版式外科系统**：  
先预检可行性 → 理解版面 → 构建 IR/DOM → 结构化翻译 → fit 排版 → 删除原文字（透明）→ 写入译文 → 恢复功能层 → 多维 QA。

---

## 3) Inputs and Materials Read（节选）

| Material | Type | Scope | Key takeaways | Impact |
|---|---|---|---|---|
| 用户需求描述 | doc | must_preserve/must_avoid | 禁止白底覆盖；保留链接/目录跳转 | 决定走“原地外科”而非 overlay 方案 |
| fixture PDFs | data | 论文/书籍 | 多栏/目录/引用跳转存在 | QA 需覆盖功能层 |

---

## 4) Research Log（示例结构，节选）

> 说明：示例中列出“来源类型与主题”，实际 Plan 必须写 Extracted facts 与 Impact，并记录版本/日期。

| Query | Source (link) | Source type | Extracted facts | Impact on plan | Open questions |
|---|---|---|---|---|---|
| PyMuPDF redaction annotations link | PyMuPDF docs | official | redaction 可能影响 annotation；需快照/恢复 | 先 snapshot 再 erase | 哪些 annotation 类型会被影响 |
| MinerU middle.json schema bbox | MinerU docs | official | bbox 表示与 backend/版本相关 | IR 需适配层 | VLM bbox 是否归一化 |
| pikepdf named destinations page labels | pikepdf docs | official | 能读写低层对象（命名目标/页面标签） | preflight 覆盖更多对象 | 是否需要 qpdf repair |
| pdfium rendering | pdfium docs | official | 渲染差异与字体替换风险 | QA 多引擎抽检 | 哪些 PDF 需要强制多引擎 |
| qpdf linearization | qpdf docs | official | 可检测/修复/线性化 | 发布前可选修复步骤 | 线性化是否改变对象偏移 |
| PDF coordinate systems | PDF spec / notes | standard | 原生 PDF 坐标=左下；工具可能抽象为左上 | 坐标统一门禁 | 旋转页如何统一 |
| HarfBuzz/Pango shaping | docs | official | CJK 测量/断行需要 shaping | Production 目标路线 | MVP 是否先用 textbox |
| Digital signature invalidation | docs | official | 改正文通常会使签名失效 | 交付说明必须写明 | 是否存在不破坏签名的改动集 |

---

## 5) Candidate Solutions（节选）

### Option A（推荐基线）：PyMuPDF 原地外科（MVP → Beta）

- Pros：保留对象结构概率更高；可控；易于做断点续跑与证据
- Cons：中文排版与高级断行能力有限；需要 fit solver 与 QA

### Option B：Overlay PDF（reportlab 等）再合并

- Pros：排版能力强
- Cons：功能层（toc/links/annotations/forms）更易丢；删除原文字仍困难

### Option C：低层内容流编辑（pikepdf/qpdf）+ 高级排版引擎

- Pros：更接近 publisher-grade
- Cons：工程复杂，需更强测试与工具链

---

## 6) Pipeline Stages（阶段→技术→验证映射，节选）

| Stage | Goal | Inputs → Outputs | Candidate tech | Recommended | Key risks | Validation & evidence |
|---|---|---|---|---|---|---|
| Preflight | 分类/路由/风险 | pdf → preflight.json | PyMuPDF / pikepdf | PyMuPDF | 加密/签名/权限阻塞 | 预检报告 + 统计 |
| Parse | 语义+几何 | pdf → middle.json | MinerU | MinerU | backend/版本差异 | schema 记录 + 样例页对齐 |
| Enrich | 对象真相 | pdf → rawdict/links/toc | PyMuPDF | PyMuPDF | 坐标/旋转错误 | bbox 可视化抽检 |
| IR/DOM | 可追踪中间表示 | middle/raw → dom.json | schema v1/v2 | v2 | ID 不稳定 | schema 校验 + diff |
| Translate | 结构化翻译 | units → translated | OpenAI-compatible | OpenAI-compatible + cache | 解析脆弱 | JSON schema + cache |
| Fit | 装入 bbox | translated → fitted | textbox / shaping | textbox→shaping | 溢出/不可读 | overflow/overlap + 截图 |
| Erase | 删除原文 | pdf → redacted | transparent redaction / stream edit | transparent redaction | 误伤功能层 | links 计数 + 渲染 diff |
| Rewrite | 写入译文 | redacted → translated | insert_textbox/HTML | insert_textbox/HTML | 缺字/字体替换 | 抽样渲染 |
| Restore | 恢复功能层 | snapshot → restored | insert_link / low-level | insert_link | 热区偏移 | 抽样点击证据 |
| QA | 渲染/几何/功能 | pdf → report | MuPDF + pdfium/poppler | 2 引擎抽检 | 单一阅读器误判 | report + screenshots |

### 6.1 外科专项规格（节选：把“关键坑点”提前写死）

**Domain Preflight：`preflight.json`（字段示例）**

```json
{
  "page_count": 12,
  "is_encrypted": false,
  "can_modify": true,
  "has_digital_signature": false,
  "has_outline": true,
  "has_links": true,
  "has_forms": false,
  "has_named_destinations": true,
  "born_digital_ratio": 0.96,
  "scan_like_pages": [7],
  "route_decision": "born-digital",
  "blockers": []
}
```

**Functional snapshot：`func_snapshot.json`（字段示例）**

```json
{
  "toc": [],
  "page_links": {"0": [{"kind": "LINK_GOTO", "from": [0, 0, 1, 1], "page": 10, "to": [72, 100]}]},
  "named_destinations": {},
  "page_labels": {},
  "annotations": {},
  "widgets": {},
  "metadata": {},
  "attachments": []
}
```

**链接锚点映射（生产级路线）**
1) link rect 覆盖文本 → 保护成 `<LINK_42>` token  
2) 翻译输出必须保留 token（JSON schema 校验）  
3) typeset 记录 token 的 glyph bbox → `token_bbox_map`  
4) `insert_link()` 用新 bbox 重建热区

**Layout DOM（节选字段）**
- `dom.json` 结构建议覆盖：Page → Block → Line/Span → Unit，并包含 `TextStyle`、`LinkAnchor`、`fit_result`
- 单元 ID 必须稳定（用于 cache 与断点续跑）

**翻译结构化输出与缓存（节选）**
- 翻译结果 JSON schema：`{units:[{id,translation,preserved_tokens,needs_review,length_risk}]}`  
- 缓存：`cache.sqlite`（table=`translation_cache`；key 包含 prompt_version/model/glossary_version）

**Typeset/Fit（节选）**
- A 档：`insert_textbox` / `insert_htmlbox`（MVP）
- B 档：Pango + HarfBuzz + Cairo（更强的 CJK 测量与断行）
- C 档：WeasyPrint 等全页重排（备选；功能层迁移成本高）
- Fit Solver：参数搜索 + penalty 评分；中文禁则（标点避头尾、引用编号/单位/URL 不可拆）

**Erase（节选）**
- 只用 redaction 删除原文字，不使用 replacement text
- redaction 矩形按行/按 span 生成；避免整段 bbox 误删背景/链接
- 注意：redaction 可能移除重叠 links → 必须 `func_snapshot` + rebuild

**QA（节选）**
- multi-renderer：MuPDF + pdfium/poppler 抽检渲染
- 产物：`qa/report.json`、`qa/report.html`、`qa/screenshots/page_*.png`、`qa/diffs/page_*.png`

---

## 7) Acceptance Contract（节选）

| AC-ID | Assertion | Evidence | Owner task |
|---|---|---|---|
| AC-001 | 输出 PDF 可打开、页数/页面尺寸一致 | `pdfinfo`/渲染截图 | TG-5 |
| AC-002 | 禁止白底覆盖（背景不被破坏） | 页级渲染对比 | TG-5 |
| AC-003 | links/toc/bookmarks 不显著丢失且可点击（抽样） | links 统计 + 抽样点击录屏/截图 | TG-5 |
| AC-004 | 译文不溢出/不重叠（抽样或全量） | overlap/overflow 报告 + 截图 | TG-4 |

---

## 8) Real Data Strategy（节选）

优先级：
1) 用户真实 PDF（可脱敏/裁剪）
2) 仓库 fixture（若分布接近真实）
3) 公开 born-digital 样本（记录来源/许可证）
4) synthetic（仅当用户确认无真实/脱敏样本）

---

## 9) Workdir & Resume Strategy（节选）

```text
.work/job_id/
  preflight.json
  extract/dom.json
  translate/cache.sqlite
  typeset/fitted.json
  restore/func_snapshot.json
  qa/report.html
  qa/screenshots/
  pages_done/
```

---

## 10) Ready-to-Execute Gate（节选）

- [ ] Research Log ≥ 8 来源（含官方/标准/源码证据）
- [ ] Pipeline Stages 表完整（覆盖 Preflight→QA）
- [ ] AC + Validation Matrix 完整且可执行
- [ ] Fallback Register（默认空；若非空则已获得确认）
- [ ] 执行授权门禁：等待用户单独回复 `开始执行`
