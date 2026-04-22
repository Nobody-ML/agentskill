Q: 我现在有以下需求，最终效果是达到我发给你的图片那样的效果，为我详细搜索探讨我应该在哪些阶段使用哪些技术，要求非常非常非常详细，不吝啬篇幅和字数：我现在需要一个新的功能,目的很简单,对pdf中的文本进行翻译并且不改变原来pdf中的排版和功能(比如跳转,超链接等等),所以输入一个pdf(或者文件夹),输出也是一个pdf,与输入pdf在同级目录(或者在提供的文件夹下).本质上是使用mineru输出的layout json文件来看文本和对应的位置,要求其他语言的文本写入后仍要好看,不超格,不重叠等等.翻译引擎使用openai api这样的,一并翻译保存文本并写入pdf,同时我希望原pdf文件保留,相当于新生成了一个新的翻译版pdf。我希望达到的效果是像原来pdf 使用latex渲染出来一样优雅好看,排版,字体等等都非常讲究,同时也不要使用白底进行覆盖了,因为有些页面底色不是白色。源pdf中比如论文/书籍是有跳转的,比如引用论文会跳转到Refernce,还有书籍的目录,点击会跳转到对应的标题行等等

# Skill 得出的 Plan and Task 


```markdown
# Plan：PDF 原排版翻译写回（original-style-translate3）

Version: v0.1
Track: Software
WorkType: Build
Level: L3
Current Mode: Plan
Execution Authorization: not_received（需要用户单独回复“开始执行”）
Plan Owner: Codex (GPT-5.2)
Last Updated: 2026-04-21 (UTC)

---

## 0) Protocol State（门禁状态）

- 本任务属于“PDF 保排版/保交互的外科手术型任务”，按 AgentSkill 规则强制 L3。
- 在未收到执行授权口令 `开始执行` 前：
  - 仅允许在 `original-style-translate3/` 下写入治理工件（Plan/Task/State/AC）
  - 禁止修改任何交付实现代码（含脚本/包/配置），直到用户授权

---

## 1) User Intent Lock

```yaml
primary_goal: "将 PDF 中可抽取文字翻译为目标语言（默认简体中文），并写回生成新的译文 PDF。"
secondary_goals:
  - "批量处理：支持输入单个 PDF 或目录递归"
  - "提供 sidecar（原文→译文映射）便于复查与断点续跑"
must_preserve:
  - "源 PDF 文件不被覆盖（保留原文件）"
  - "页面尺寸/旋转/页数不变"
  - "不改变原有排版结构（列布局、标题/段落位置等）"
  - "保持交互功能：链接、跳转（目录/引用）等尽量不丢失"
  - "背景/色块/图片不被白底覆盖（禁止白底遮罩）"
must_avoid:
  - "整页栅格化（会丢失链接/矢量/可搜索性）"
  - "用白色矩形覆盖旧文字（页面底色可能非白）"
  - "译文越界、重叠、明显难看"
non_goals:
  - "对扫描页（文字在图片里）做完全无损替换（MVP 先检测并提示）"
  - "对表格 body 做精排翻译（若 MinerU 仅输出 table HTML/图片，MVP 先翻译 caption）"
style_preferences: "尽量接近 LaTeX 论文的克制、统一与可读性；必要时缩小字号以 fit。"
quality_bar: "译文写入后不超格、不重叠、不出现白底遮罩；链接/跳转仍可用。"
latest_user_feedback: "目标效果参考 pdf_with-layout_test/reference 中截图；保留跳转/超链接；不要白底覆盖。"
scope_boundary: "仅修改 original-style-translate3/ 目录内文件；pdf_with-layout_test 只读用于验证。"
```

---

## 2) Problem Frame

### 2.1 一句话目标

对 born-digital PDF：基于 MinerU 输出的 layout/middle JSON 获取文本与 bbox；调用 OpenAI-compatible 翻译；使用 PyMuPDF 透明删除原文字并在原 bbox 内重排写入译文，生成新的译文版 PDF，同时尽量保留链接/跳转等交互功能。

### 2.2 背景

- 传统“覆盖译文”方案常用白底矩形遮盖旧文字，会破坏非白底页面与色块背景。
- 栅格化（渲染成图片再写回）会破坏交互功能（链接/目录/书签）、可搜索与矢量质量。
- 目标是“对象级别外科”：删除原文字对象、写入新文字对象、保持功能层与几何约束。

---

## 3) Current State / Gap Analysis

- 仓库已有：MinerU 解析与 Markdown 翻译链路（`scripts/parse_pdf.py`、`scripts/translate_md.py`、`pdf_parse_translate/*`）。
- 仓库缺失：将译文“写回 PDF 并保留交互”的实现。
- 关键难点：
  - 透明删除旧文字（不白底遮罩）
  - bbox 内排版 fit（不溢出、不重叠）
  - 功能层（links/jumps）不丢失或可验证

---

## 4) Inputs and Materials Read（深读清单）

| Material | Type | Scope | Key takeaways | Impact on plan |
|---|---|---|---|---|
| `pdf_parse_translate/mineru_cli.py` | code | MinerU CLI wrapper | 支持 keep 输出 middle/model/content_list 等；middle.json 即 layout 的关键来源 | 可在必要时复用 run_mineru_parse 获取 JSON |
| `scripts/parse_pdf.py` | code | I/O 规范化脚本 | 支持 `--pdf/--dir`、输出目录、keep 额外产物；生成 `*_middle.json` 等 | 新功能 CLI 可复用相同输入遍历逻辑 |
| `scripts/translate_md.py` | code | OpenAI-compatible 翻译 | `OpenAICompatClient` + 并发翻译 | 译文引擎复用 openai_compat 与配置习惯 |
| `pdf_parse_translate/openai_compat.py` | code | OpenAI-compatible client | `/v1/chat/completions` 接口封装 | 新功能直接复用该 client |
| `pdf_with-layout_test/*/*_middle.json` | data | MinerU middle schema | `pdf_info` 按页列表；block 类型包含 text/title/list/code/table/image/equation | DOM 以 page→block 为主，table caption 单独处理 |
| PyMuPDF runtime help | runtime-doc | `add_redact_annot` / `apply_redactions` / `insert_textbox` | `apply_redactions(text=0)` 会删除文字；fill=None 不产生白底遮罩；insert_textbox 可 fit 检测 | 推荐路线：透明 redaction + textbox 排版 |

---

## 5) Research Log（最小研究包：以本地一手事实为主）

> 说明：当前阶段未做外网检索（用户未要求“必须联网”，且实现可用本地一手事实闭环）。如后续出现行为不确定（例如某类 PDF 的 annotation 被 redaction 误伤），将补充外网官方文档来源并更新本表。

| Query | Source | Source type | Extracted facts | Impact on plan | Open questions |
|---|---|---|---|---|---|
| PyMuPDF redaction 会否影响 links | `help(fitz.Page.apply_redactions)` + 本地实验 | source-code/runtime-doc | `apply_redactions(text=0)` 删除文字；links(annotations) 在实验中保持不变 | 功能保持 MVP 先做“链接计数前后对比” | 更复杂注释/表单是否受影响需抽检 |
| fill=None 是否会产生白底 | 本地实验（在图片区域放 redaction） | experiment | fill=None 不产生遮罩；fill=(1,1,1) 会产生白块 | 满足“不要白底覆盖”硬约束 | 不同 PDF 背景叠加模式是否存在边界 bug |
| MinerU middle.json schema | `pdf_with-layout_test/*_middle.json` | data | `pdf_info` 按页；table body 可能只有 html/image_path；equation blocks 可识别并保护 | typeset 单元以 block 为主；equation 不翻译不改写 | 不同 MinerU 版本字段差异需适配 |

---

## 6) Requirements

### 6.1 Functional Requirements

1) 输入：单个 PDF 或目录（递归）。
2) 输出：译文 PDF：
   - 默认输出到源 PDF 同级目录
   - 可用 `--output-dir` 指定输出目录
3) 翻译：使用 OpenAI-compatible API（用户指定 base_url/endpoint）。
4) 布局：使用 MinerU `*_middle.json` 提供 bbox；译文在 bbox 内排版。
5) 保留：链接/跳转/超链接等交互尽量不丢。
6) 保留：源 PDF 不覆盖（新文件输出）。
7) sidecar：保存翻译文本映射（便于复查/断点续跑）。

### 6.2 Non-functional Requirements（质量属性）

- 排版质量：不溢出、不重叠；尽量与原字号/行距一致；必要时缩小字号保证 fit。
- 视觉要求：不使用白底遮罩；背景/色块/图片保持原样。
- 可靠性：单页失败不应导致整本不可输出（MVP：失败块标记并继续；在报告里可追溯）。
- 可维护性：中间结构（DOM/sidecar）有稳定 ID；便于调参迭代。

---

## 7) Non-goals（MVP 明确不做）

- 扫描页（文字在图片中）做无损替换（MVP 仅检测并提示）。
- 将 LaTeX 公式（interline_equation）重新排版渲染为新字体（MVP：保护，不翻译不删除）。
- 对 table body 做单元格级排版翻译（当 MinerU 仅给 HTML/图片时）。

---

## 8) Constraints and Boundaries

### 8.1 Files / Areas Allowed to Modify

- `original-style-translate3/**`

### 8.2 Forbidden

- 修改 `original-style-translate3/` 之外任何文件/目录

### 8.3 Tech Stack / Versions / License Notes

- PDF 编辑：PyMuPDF（MuPDF）
- 布局 JSON：MinerU `*_middle.json`
- 翻译接口：OpenAI-compatible `/v1/chat/completions`
- 许可证：不新增第三方字体文件（MVP 优先用 PyMuPDF builtin CJK font `china-s`）；如需更优雅衬线字体，后续作为可选增强并明确字体许可

### 8.4 Fallback Policy

- 默认不兜底/不降级。
- 允许显式测试模式（非兜底）：`--mock-translate` 用于在翻译服务不可用时验证几何/写回链路（仅用于开发验证）。

---

## 9) Candidate Solutions

### Option A：Rasterize + Overlay（保守但不符合需求）

- 做法：渲染每页为图片，在图片上绘制译文再生成 PDF。
- 优点：实现简单，视觉可控。
- 缺点：丢失链接/跳转/可搜索/矢量质量；不满足 must_preserve。

### Option B：PyMuPDF 透明删除文字 + bbox 排版写回（推荐）

- 做法：
  - 使用 MinerU middle.json 获取 translatable blocks 与 bbox
  - 使用 PyMuPDF `add_redact_annot(fill=None)` + `apply_redactions(text=0, images=0, graphics=0)` 删除旧文字（不白底）
  - 使用 `insert_textbox` 将译文写入相同 bbox，字号搜索保证 fit
  - 不改动 annotations，验证 links 计数前后对比
- 优点：保留交互对象概率高；满足“无白底遮罩”；实现可控。
- 风险：文本排版精细度有限（CJK 禁则/字距）；超长译文需缩小字号。

### Option C：内容流级别替换（长期/高级）

- 做法：解析 content stream，定位文本绘制指令并替换，尽量复用原字体/布局。
- 缺点：工程复杂度极高，易破坏 PDF；不适合作为 MVP。

**推荐路线：Option B**（先打通端到端与门禁，再迭代排版质量）。

---

## 10) Architecture Decision（关键决策）

- 采用 PyMuPDF 作为 PDF 读写与 redaction/写回引擎。
- “删除旧文字”使用透明 redaction（fill=None），禁止白底遮罩。
- 排版引擎 MVP 使用 `insert_textbox` + 字号/行距搜索 fit solver。
- 公式（`interline_equation`）默认保护：不翻译、不删除、不覆盖。

---

## 11) Technical Chain / Method Chain

### 11.1 端到端链路图

```mermaid
flowchart TD
  In[Input: PDF / Dir] --> Pre[Preflight: PDF metadata + links snapshot]
  Pre --> Layout[MinerU middle.json: blocks + bbox]
  Layout --> Units[Build Units: translatable blocks]
  Units --> Tr[Translate via OpenAI-compatible + cache]
  Tr --> Fit[Fit/Typeset: font size search in bbox]
  Fit --> Erase[Erase old text: transparent redaction]
  Erase --> Write[Write translated text: insert_textbox]
  Write --> QA[QA: overflow/overlap + links count + render sample]
  QA --> Out[Output: translated PDF + sidecars + report]
```

### 11.2 Pipeline Stages（阶段→技术→验证）

| Stage | Goal | Inputs → Outputs | Candidate tech | Recommended tech | Key risks | Validation & evidence |
|---|---|---|---|---|---|---|
| Preflight | 可写性/风险识别 | pdf → preflight.json | PyMuPDF / pikepdf | PyMuPDF | 加密/签名导致不可写 | preflight.json（页数/links/加密） |
| Layout Parse | 获取 bbox/块类型 | pdf or existing json → middle.json | MinerU / existing | 优先复用 existing middle.json；否则 MinerU | schema 差异 | schema 校验 + 页尺寸一致性 |
| Units Build | 构建可翻译单元 | middle.json → units.json | custom | custom | table/equation 处理不当 | units 统计（type/len） |
| Protect | 保护不改写对象 | units → protected text | rules | rules | 公式/URL/引用被翻译破坏 | token QA（regex 扫描） |
| Translate | 结构化翻译 + 缓存 | protected → translated | OpenAI-compatible | OpenAICompatClient | API 失败/输出跑偏 | cache + 错误列表 |
| Fit/Typeset | 装入 bbox | translated → fitted | textbox/HTML textbox | insert_textbox | 溢出/字号过小 | overflow 统计 + failed blocks |
| Erase | 删除旧文字 | pdf → redacted pdf | redaction/content-edit | transparent redaction | 误伤图形/links | links count 对比 + 抽检渲染 |
| Writeback | 写入译文 | redacted → translated pdf | insert_textbox | insert_textbox | 缺字/编码问题 | 渲染抽检 + missing glyph 统计 |
| QA | 可感知+功能 | pdf → report.json | render + geometry | PyMuPDF render | 单渲染器误判 | 抽检页截图 + 指标 |
| Deliver | 输出与总结 | artifacts | - | - | 用户不易复查 | sidecar + report + 路径摘要 |

### 11.3 Workdir & Resume Strategy

- 对每个输入 PDF 生成 sidecars：
  - `*.ost3.units.json`（抽取到的 blocks）
  - `*.ost3.translations.json`（原文→译文映射 + 状态）
  - `*.ost3.report.json`（QA 报告）
- 断点续跑：若输出 PDF 已存在且 sidecar 完整，默认跳过；可 `--overwrite` 强制重跑。

### 11.4 QA Plan

- render QA：渲染抽检 1–3 页（含带图片/色块/目录页），人工目检“无白底遮罩、无明显重叠、可读性 OK”
- geometry QA：基于 `insert_textbox` 返回值判断 fit；记录未 fit blocks
- function QA：统计每页 `get_links()` 数量前后对比；抽样点击目录跳转（人工）

---

## 12) Specification（对外接口草案）

### 12.1 CLI（拟）

- `python original-style-translate3/translate_pdf.py --pdf <path> [--output-dir <dir>] [--to zh] [--base-url ...] [--model ...]`
- `python original-style-translate3/translate_pdf.py --dir <path> --output-dir <dir> [--recursive true]`

关键参数：
- `--use-existing-middle-json`：优先使用与 PDF 同目录的 `*_middle.json`（默认 true）
- `--mineru-backend/--mineru-method/...`：当需要现场跑 MinerU 时使用（MVP 可先不暴露）
- `--mock-translate`：跳过 API，用确定性假翻译测试排版/写回

### 12.2 Error Handling

- API 失败：记录到 sidecar + 报告；块级失败不阻塞整本输出（MVP 行为需在报告中可追溯）。
- Fit 失败（译文塞不进 bbox）：标记 failed block；可选策略（需用户确认后才能启用）：二次压缩改写/更小字号下限。

---

## 13) Acceptance Contract / Validation Matrix

- 见 `original-style-translate3/AcceptanceContract.md`

---

## 14) Ready-to-Execute Gate（请求执行授权前自检）

在请求用户发送 `开始执行` 前必须满足：
- Plan/Task/AC 已落盘且不含占位符
- 明确 Allowed/Forbidden 边界
- 明确 MVP 能做到的范围（non-goals 已声明）
- 明确验证方法与证据产物（report/sidecar/渲染抽检）

---

## 15) Resumption Block（可续跑块）

见 `original-style-translate3/State.md` 中 `RESUMPTION_BLOCK_v0.3`。



```

```markdown
# Task：PDF 原排版翻译写回（original-style-translate3）

Version: v0.1
Track: Software
WorkType: Build
Level: L3
Execution Authorization: not_received（需要用户单独回复“开始执行”）
Last Updated: 2026-04-21 (UTC)

---

## Task Status Legend

- `[ ]` pending
- `[~]` in progress
- `[x]` done
- `[!]` blocked (needs input)

---

## Execution Rules（硬门禁摘要）

1) 未收到 `开始执行` 前不得修改实现代码（仅可改 Plan/Task/State/AC）。
2) 执行必须映射到 Task；不在 Task 中的改动不得发生。
3) 每个 Task Group 结束必须做 Checkpoint Validation，并把证据入口写入 `original-style-translate3/State.md` Evidence Index。

---

## 0) Preflight（执行前置门禁）

- [ ] 确认 Execution Authorization=received（已落盘到 `State.md`/`Plan.md`）
- [ ] 再确认 Allowed/Forbidden 边界（仅 `original-style-translate3/**` 可改）
- [ ] 确认翻译服务可用（base_url/model 可用）或决定使用 `--mock-translate` 做几何链路验证
- [ ] 确认测试数据：`pdf_with-layout_test/`（只读）

### Checkpoint Validation

- data_type: real（仓库内样例）
- evidence:
  - 记录将使用的 base_url/model
  - 记录将跑的命令与输出路径

---

## 1) Task Group：TG-CLI（脚本入口与 I/O）

### Tasks

- [ ] 在 `original-style-translate3/` 新增可运行入口脚本 `translate_pdf.py`
- [ ] 支持 `--pdf` / `--dir`（递归）输入
- [ ] 支持 `--output-dir`（默认同级目录）与 `--overwrite`
- [ ] 输出命名规则：默认 `*_translated.pdf`（或 `*_zh.pdf`），同时写 sidecar（units/translations/report）

### Checkpoint Validation

- commands:
  - 运行 `--help` 可显示参数
  - 对 `pdf_with-layout_test/2509.14476/2509.14476_origin.pdf` 做一次 `--mock-translate`，确认输出文件生成
- pass criteria:
  - 输出文件路径正确、源文件未覆盖

---

## 2) Task Group：TG-Layout（解析 middle.json → translatable units）

### Tasks

- [ ] 实现 middle.json schema 解析（page→block→spans）
- [ ] 过滤/分类：保护 `interline_equation`；table 仅翻译 caption；discarded_blocks 默认不翻译（可配置）
- [ ] 为每个 unit 生成稳定 ID（page_idx + block_index + bbox hash）
- [ ] units sidecar：`*.ost3.units.json`

### Checkpoint Validation

- commands:
  - 对 `pdf_with-layout_test/*/*_middle.json` 运行 units 抽取
- pass criteria:
  - units 统计合理（含 page_idx/type/bbox/text_len）
  - interline_equation 未进入可翻译列表

---

## 3) Task Group：TG-Translate（OpenAI-compatible 翻译 + 缓存）

### Tasks

- [ ] 复用 `pdf_parse_translate.openai_compat.OpenAICompatClient`
- [ ] 定义翻译 prompt：只输出译文；保留数字/URL/引用编号；不翻译公式 token
- [ ] 支持并发翻译（线程池），并将结果写入 `*.ost3.translations.json`
- [ ] 支持 `--mock-translate`（确定性输出）用于无服务环境的几何验证

### Checkpoint Validation

- data_type:
  - real（若服务可用）/ synthetic（mock-translate）
- pass criteria:
  - sidecar 内含每个 unit 的状态（ok/failed/skipped）与译文

---

## 4) Task Group：TG-Typeset（bbox 内排版 fit solver）

### Tasks

- [ ] 使用 PyMuPDF `insert_textbox` 写入译文
- [ ] 实现字体/字号搜索：从原文字估计字号起步，下降到 fit（以 `insert_textbox` 返回值判定）
- [ ] 对齐策略：title/heading 左对齐；正文默认左对齐（必要时可选 justify）
- [ ] 记录每个 unit 的最终字号、是否 fit

### Checkpoint Validation

- commands:
  - `--mock-translate` 跑一份样例 PDF，生成 report 并渲染抽检页
- pass criteria:
  - report 中 overflow=0（或极少且可解释）
  - 输出 PDF 可正常打开

---

## 5) Task Group：TG-Writeback（透明删除旧文字 + 写回 PDF）

### Tasks

- [ ] 旧文字删除：对 unit 的原文字 bbox 调用 `add_redact_annot(fill=None, cross_out=False)`，随后 `apply_redactions(images=0, graphics=0, text=0)`
- [ ] 确保不产生白底遮罩
- [ ] 输出新 PDF（不覆盖源文件）

### Checkpoint Validation

- evidence:
  - 渲染对比截图：至少 1 页含图片/色块，确认无白底矩形
- pass criteria:
  - AC-002 通过（无白底覆盖）

---

## 6) Task Group：TG-Functional（链接/跳转保持与验证）

### Tasks

- [ ] 保存功能快照：每页 links count（MVP）
- [ ] 输出后再次统计 links count；将差异写入 report
- [ ] （如发现丢失）阻塞并回到 Plan 决定是否需要“重建 links”增强

### Checkpoint Validation

- pass criteria:
  - links count 不显著减少；或报告清晰解释差异

---

## 7) Task Group：TG-QA（报告与证据产物）

### Tasks

- [ ] 生成 `*.ost3.report.json`：
  - pages summary
  - overflow/failed blocks
  - links count delta
  - timing / config
- [ ] 可选：渲染抽检页到 `*.ost3.render/`（不进入 repo 其它目录）

### Checkpoint Validation

- pass criteria:
  - report 可定位问题页/块

---

## Milestone Validation（里程碑：对样例集端到端）

- scope: `pdf_with-layout_test/` 目录内 2–3 个样例 PDF
- expected evidence:
  - 输出 PDF（译文版）
  - sidecars（units/translations/report）
  - 渲染抽检图（可选）

---

## Final Validation

- acceptance contract coverage: AC-001～AC-006 全覆盖
- evidence index updated: `original-style-translate3/State.md` 更新证据入口
- residual risks: 扫描页/表格 body/复杂 inline math 的质量差异


```


# 我所希望的 Plan

```markdown
下面这件事，准确地说不是“把 PDF 里的英文换成中文”这么简单，而是一个 **PDF 版式外科手术系统**：先识别原 PDF 的文字、图像、公式、链接、目录、注释、页面坐标和字体风格，再把可翻译文本变成结构化翻译任务，最后在不破坏原页面对象和交互对象的前提下，删除原文字并重新排版写入译文。目标效果接近你图里那种：图片、公式、页眉、页码、栏宽、链接、目录跳转都保留，译文像重新排过版，而不是白色矩形遮盖。

---

## 1. 总体技术路线：不要“覆盖 PDF”，而要“保留背景、移除文字、重绘译文、恢复功能”

你的目标效果建议采用这个主流程：

```text
输入 PDF / 文件夹
  ↓
预检：PDF 类型、权限、字体、页面盒、链接、目录、扫描页、损坏页
  ↓
MinerU 解析：layout / middle.json / span / block / line / bbox
  ↓
PyMuPDF 二次抽取：原始文字样式、字体大小、颜色、旋转、链接、目录、注释
  ↓
构建 Layout DOM：页面 → 栏 → 块 → 行 → span → 可翻译单元
  ↓
保护公式、引用、URL、DOI、代码、页码、图表编号
  ↓
OpenAI API 翻译：结构化 JSON 输出 + 缓存 + 批处理 + 术语表
  ↓
排版适配：字体选择、字号搜索、行距、换行、避让、压缩/改写
  ↓
删除原文字：透明 redaction / 内容流处理，不使用白底覆盖
  ↓
写入译文：HTML/CSS 文本盒或 Pango/HarfBuzz/Cairo 高级文字引擎
  ↓
恢复链接、目录、书签、注释、页面标签、元数据
  ↓
渲染 QA：溢出、重叠、旧文字残留、链接可点击、目录可跳转
  ↓
输出同级 translated PDF，原 PDF 保留
```

核心原则是：**原 PDF 页面本身尽量原地修改，不重新生成整份 PDF**。重新生成整页虽然容易把版面做漂亮，但目录、内部跳转、注释、表单、页面标签、附件、元数据、命名目标等很容易丢。你的需求更像“保留原 PDF 的对象结构，只替换可见文本层”。

---

## 2. 先确认边界：哪些 PDF 可以做到很像 LaTeX，哪些需要降级

### 2.1 最适合的 PDF 类型

最适合的是 **born-digital PDF**，也就是由 LaTeX、Word、InDesign、出版社系统、网页打印等生成的 PDF。特点是：文字仍然是 PDF 文字对象，图像和背景是独立对象，链接是注释对象。这种文件可以做到：

* 原背景、插图、公式、线条、页眉页脚基本不动。
* 原文字被物理移除，而不是白底盖住。
* 新译文是可选中、可复制、可搜索的文本。
* 内部跳转、URL、目录、书签可以保留或重建。

### 2.2 最麻烦的 PDF 类型

扫描 PDF、图片型 PDF、旧 OCR PDF、或出版社把整页压成图片的 PDF最麻烦。因为文字已经变成图片像素，你无法“删除文字后自然露出原背景”。这时只有三种选择：

1. **图像修复 / inpainting**：把原文字区域像图像修复一样补背景，再写译文。复杂背景、纸张纹理、图片上文字会很难。
2. **半透明贴片**：不使用纯白，而是采样区域背景色或生成纹理贴片。效果比白底好，但严格来说仍是覆盖。
3. **标记为低可信页，人工审校**：对学术扫描书籍尤其重要。

MinerU 本身支持 PDF、图片、Office 文件输入，并能输出 Markdown、JSON 等结构化结果，适合做后续处理；它还会输出 layout.pdf、span.pdf、model.json、middle.json、content_list.json 等文件用于调试和二次开发。MinerU 官方文档也提醒，VLM backend 在 2.5 版本的输出结构有重大变化，并且与 pipeline backend 不兼容，所以你的系统必须做版本适配层，而不能硬编码某一种 JSON 结构。([OpenDataLab][1])

---

## 3. 阶段一：PDF 预检，决定后续走哪条处理路线

这一阶段建议不要直接跑翻译，而是为每个 PDF 生成一个 `preflight.json`。它决定该文件能不能做高质量替换、是否需要 OCR、是否要 inpaint、是否存在数字签名、是否有链接/目录/表单需要恢复。

### 3.1 要检查的内容

每个 PDF 至少检查这些字段：

```json
{
  "input_path": ".../paper.pdf",
  "output_path": ".../paper.zh-CN.pdf",
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
  "page_boxes": {
    "0": {
      "mediabox": [0, 0, 595.28, 841.89],
      "cropbox": [0, 0, 595.28, 841.89],
      "rotation": 0
    }
  },
  "risk_level": "medium"
}
```

### 3.2 推荐技术

**PyMuPDF** 用于快速打开、抽取页面文字、页面盒、页面旋转、链接、目录、渲染预览、后续删除和写入文本。PyMuPDF 文档说明它能抽取页面文本、图片并向 PDF 页面添加文本、图片等对象。([PyMuPDF][2])

**pikepdf / qpdf** 用于低层 PDF 对象检查、修复、线性化、元数据、命名目标、页面标签、附件、对象树等。pikepdf 是 qpdf 的 Python 封装，适合低层 PDF 操作、修复、线性化、处理加密 PDF，但它不是渲染器，不能把页面渲染成图片。([pikepdf 文档][3])

**pdfium / poppler** 用于渲染 QA。不要只用一个渲染器判断效果，因为不同 PDF 阅读器对字体、透明度、注释、裁剪的处理可能略有差异。

### 3.3 数字签名的特殊处理

如果 PDF 带数字签名，只要你改动正文内容，签名通常会失效；即便使用增量保存，也只有某些允许的改动类型可能不破坏签名。你的系统应该保留原文件，并在译文文件中标记“翻译版已修改原始内容，不保持原签名有效性”。([Nutrient][4])

---

## 4. 阶段二：用 MinerU 做版面理解，但不要只依赖 MinerU

MinerU 是很好的 layout parser，但你的目标不是只拿 Markdown 翻译，而是要把译文写回原 PDF 坐标。因此要把 MinerU 当成 **版面语义识别器**，再用 PyMuPDF 当成 **PDF 真实对象校验器**。

### 4.1 MinerU 负责什么

MinerU 的 `middle.json` 很关键。它包含每页 `pdf_info`，每页有 `page_idx`、`page_size`、`images`、`tables`、`interline_equations`、`para_blocks` 等；块结构可以到 block → line → span，span 含 `bbox`、`type`、`content` 或 `image_path`。这些字段正好适合构造你的翻译单元。([OpenDataLab][5])

你应该使用 MinerU 做：

* 页面阅读顺序识别。
* 标题、正文、列表、脚注、页眉页脚、图注、表注、参考文献的分类。
* 公式识别，尤其是 `inline_equation`、`interline_equation`。
* 图像、表格、图注、表注的关联。
* 多栏论文的阅读顺序和块级 bbox。
* 复杂页面的 layout debug，可用 MinerU 输出的 layout.pdf 和 span.pdf 做人工对照。

### 4.2 PyMuPDF 负责什么

PyMuPDF 的 `rawdict` / `dict` 文字抽取可以得到更接近 PDF 真实文本绘制的信息：block、line、span、字体、字号、颜色、flags、字符 bbox 等。PyMuPDF 文档说明，一个 text page 由 block、line、span 构成，span 是具有相同字体属性的一组相邻字符，包含字体名、字号、flags、颜色等。([PyMuPDF][6])

你应该用 PyMuPDF 补充：

* 原字体名、字号、颜色、粗体/斜体特征。
* 每行 baseline、行高、字符 bbox。
* 旋转文字、页边竖排文字、倾斜文字。
* 链接热区和链接目标。
* PDF 真实 page box、cropbox、rotation。
* 原文字是否真的存在于文本层，而不是图片层。

### 4.3 坐标统一非常重要

MinerU VLM backend 的 bbox 是 `[x0, y0, x1, y1]`，原点在页面左上角，坐标是 0 到 1 的归一化百分比；pipeline backend 中则会出现 `page_size` 和具体 bbox。PyMuPDF / MuPDF 也采用左上角为原点、y 轴向下的坐标系，单位通常是 PDF point，1 point = 1/72 inch。原生 PDF 坐标是左下角原点，所以如果你用 pikepdf 直接写内容流，需要做坐标转换。([OpenDataLab][5])

建议所有内部 layout DOM 统一使用：

```python
# 统一坐标系
origin = "top-left"
unit = "pt"
x_right_positive = True
y_down_positive = True
```

MinerU VLM bbox 转 PyMuPDF bbox：

```python
x0_pt = x0_norm * page_width_pt
y0_pt = y0_norm * page_height_pt
x1_pt = x1_norm * page_width_pt
y1_pt = y1_norm * page_height_pt
```

如果 MinerU 输出是像素坐标：

```python
x0_pt = x0_px / image_width_px * page_width_pt
y0_pt = y0_px / image_height_px * page_height_pt
x1_pt = x1_px / image_width_px * page_width_pt
y1_pt = y1_px / image_height_px * page_height_pt
```

---

## 5. 阶段三：抽取并保护 PDF 功能层

你提到论文引用跳转到 Reference，书籍目录跳转到标题行，这些功能在 PDF 里通常不是正文文本的一部分，而是注释、链接、目录 outline、命名目标、页面标签等对象。

### 5.1 需要保存的功能对象

在修改任何页面前，先把这些对象完整快照：

```json
{
  "toc": [],
  "page_links": {
    "0": [
      {
        "kind": "LINK_GOTO",
        "from": [120.1, 300.2, 140.5, 312.8],
        "page": 10,
        "to": [72, 100],
        "xref": 123
      }
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

PyMuPDF 的 Link 对象代表指向文档内部、外部文档或互联网的指针，并且链接存在于每一页上。目录/书签可以通过 `Document.get_toc()` 从 outline chain 中读取，`set_toc(get_toc())` 也能在同坐标语义下保持目标位置。([PyMuPDF][7])

pikepdf 适合处理更底层的 outline 和 destination。pikepdf 文档说明，outlines 也就是书签，用于 PDF 查看器侧边栏导航；destination 决定点击书签后跳转到哪里，既可以指向页，也可以使用 named destination。([pikepdf 文档][8])

### 5.2 链接不是简单“保留原矩形”就够

如果你只是把原链接矩形原样复制回去，某些场景能用，但不是完美：

* 目录页：每一行仍在原位置，原链接矩形大概率可复用。
* 论文引用 `[12]`：翻译后行内位置可能变化，原链接矩形可能不再盖住 `[12]`。
* 图表引用 “Figure 3”：译成“图 3”后文字变短，原链接矩形可能偏移。
* URL：换行后链接区域应重新按新文字位置生成多个矩形。

所以生产级方案应当做 **链接锚点映射**：

1. 在原 PDF 中读取 link rectangle 覆盖的文本，例如 `[7]`、`Section 2.1`、`Figure 3`。
2. 在翻译前把该文本保护成占位符，例如 `<LINK_42>[7]</LINK_42>`。
3. 翻译后要求模型保留占位符。
4. 排版时记录占位符在新文本中的 glyph bbox。
5. 写入译文后，用新 bbox 重新 `insert_link()`。

PyMuPDF 页面 API 支持 `insert_link`、`update_link`、`Page.links`、`Page.load_links` 等方法。([GitHub][9])

---

## 6. 阶段四：构建 Layout DOM，而不是直接翻译字符串

你要达到论文/书籍那种优雅效果，必须把 PDF 结构抽象成自己的中间表示。

### 6.1 推荐数据结构

```python
@dataclass
class DocumentLayout:
    path: str
    pages: list["PageLayout"]
    toc: list
    metadata: dict
    named_destinations: dict

@dataclass
class PageLayout:
    page_index: int
    width: float
    height: float
    rotation: int
    blocks: list["Block"]

@dataclass
class Block:
    id: str
    page_index: int
    block_type: str  # title, text, list, caption, footnote, table_cell, reference...
    bbox: Rect
    reading_order: int
    lines: list["Line"]
    original_text: str
    protected_text: str
    translated_text: str | None
    style: "TextStyle"
    links: list["LinkAnchor"]
    fit_result: "FitResult | None"

@dataclass
class TextStyle:
    font_family_source: str
    target_font_family: str
    font_size: float
    color: tuple[float, float, float]
    bold: bool
    italic: bool
    align: str
    line_height: float
    writing_mode: str
```

### 6.2 块级分类策略

不同块不能用同一种翻译和排版规则：

* `doc_title` / `title`：允许略微改写，使标题紧凑、正式。
* `text`：忠实翻译，保持段落语义。
* `list`：保留编号、缩进、项目符号。
* `image_caption` / `table_caption`：短句优先，不能挤压图表。
* `footnote`：字号小，但不能低于可读阈值。
* `header` / `footer` / `page_number`：通常不翻译，或只翻译固定页眉。
* `ref_text` / references：学术参考文献建议默认不全文翻译，只翻译 “References” 标题或按配置翻译题名。
* `inline_equation` / `interline_equation`：不翻译，只保护和回填。
* `code` / `algorithm`：默认不翻译代码，只翻译注释或标题。

MinerU 的输出类型里包含 text、title、equation、image、caption、table、ref_text、header、footer、page_number 等，正好可用于这一步。([OpenDataLab][5])

---

## 7. 阶段五：翻译引擎设计，重点是“结构化、可恢复、可缓存”

### 7.1 不要整页翻译

整页翻译会破坏：

* 块 ID。
* 链接锚点。
* 公式占位符。
* 图表编号。
* 脚注编号。
* 列表编号。
* 缓存复用。
* 失败重试粒度。

推荐按“段落块”翻译，但提供上下文：

```json
{
  "target_language": "zh-CN",
  "domain": "quantum chemistry",
  "units": [
    {
      "id": "p003_b012",
      "type": "body",
      "text": "For the N-particle system, we choose our unperturbed Hamiltonian...",
      "context_before": "and perturbation theory.",
      "context_after": "using the formalism presented in Chapter 6.",
      "protected_tokens": [
        {"token": "<EQ_1>", "value": "N E_0^{(0+1+2)}"},
        {"token": "<CITE_1>", "value": "(7.70)"}
      ],
      "style_hint": {
        "max_chars_preferred": 120,
        "formal": true,
        "preserve_equations": true
      }
    }
  ]
}
```

### 7.2 OpenAI API 用法

建议使用 OpenAI Responses API 做在线翻译请求，因为它是当前 OpenAI 用于生成模型响应的统一接口，支持文本/图像输入和文本输出，也支持函数调用等能力。对于输出格式，使用 Structured Outputs，让模型返回严格符合 JSON Schema 的结果，避免漏 ID、乱改占位符、返回散文式答案。([OpenAI开发者][10])

对于文件夹批量处理，使用 Batch API。官方文档给出的 Batch API 限制是单个 batch 最多 50,000 个请求，输入 JSONL 文件最大 200 MB，并且 batch rate limits 与普通 per-model rate limits 分开。([OpenAI开发者][11])

### 7.3 翻译结果 schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["units"],
  "properties": {
    "units": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "translation",
          "preserved_tokens",
          "needs_review",
          "length_risk"
        ],
        "properties": {
          "id": {"type": "string"},
          "translation": {"type": "string"},
          "preserved_tokens": {
            "type": "array",
            "items": {"type": "string"}
          },
          "needs_review": {"type": "boolean"},
          "length_risk": {
            "type": "string",
            "enum": ["low", "medium", "high"]
          }
        }
      }
    }
  }
}
```

### 7.4 翻译缓存

必须有缓存，否则大文件迭代排版会非常贵、非常慢。

缓存 key：

```text
sha256(
  normalized_source_text
  + target_language
  + glossary_version
  + prompt_version
  + model_name
  + translation_policy
)
```

缓存内容：

```sql
CREATE TABLE translation_cache (
  key TEXT PRIMARY KEY,
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

### 7.5 二次改写请求

排版时如果译文塞不进原 bbox，不要一味缩小字体。应该有第二轮“压缩译文”请求：

```json
{
  "id": "p003_b012",
  "current_translation": "...",
  "max_visual_lines": 4,
  "max_width_pt": 235.0,
  "font_size_pt": 8.8,
  "instruction": "在不丢失核心含义、不删除公式占位符的前提下，压缩为更适合窄栏论文排版的中文。"
}
```

这一步比把字号缩到 5pt 更重要。学术论文尤其如此：中文翻译常常可以通过术语压缩、从句合并、删除冗余连接词来变短。

---

## 8. 阶段六：字体与排版引擎，决定最终是否“像 LaTeX”

### 8.1 字体选择策略

不要直接复用原 PDF 里的嵌入字体来写译文。很多 PDF 嵌入的是子集字体，可能只包含原文用到的字形；英文字体也不包含中文。你应该用完整的目标语言字体，并在输出 PDF 中嵌入子集。

推荐：

* 英文、数字、公式附近：优先保持原 PDF 的拉丁字体观感。
* 中文正文：`Source Han Serif SC` / `Noto Serif CJK SC` 一类宋体/明朝风格，更像论文和书籍。
* 中文标题：可用同一字体的 Semibold/Bold。
* 图注、表注、脚注：同一字体小字号，不要混太多字体。
* UI 或说明类 PDF：可以用 `Source Han Sans` / `Noto Sans CJK`。
* 多语言：使用 Noto/Source Han 作为 fallback。

Source Han Serif 是 Adobe 的开源 Pan-CJK OpenType 字体项目；Noto CJK 字体也提供 Sans 和 Serif CJK 系列。([GitHub][12])

PyMuPDF FAQ 也提醒，内置 Base-14 字体只支持有限字符，扩展字符和 CJK 应使用合适的 Unicode 字体或 CJK fallback。([PyMuPDF][13])

### 8.2 排版引擎分三档

#### A 档：PyMuPDF `insert_htmlbox()` 快速实现

适合 MVP 和多数论文正文。PyMuPDF 的 `insert_textbox()` 可以把文本写入矩形并自动换行；`insert_htmlbox()` 可以使用 HTML/CSS，支持更丰富的文字效果和溢出缩放。PyMuPDF 文档说明，插入文本盒时会按盒宽自动换行，文本可包含 Latin、Greek、Cyrillic、Chinese、Japanese、Korean，richtext/HTML 可以提供更丰富效果。([PyMuPDF][14])

优点：

* 开发快。
* 直接写回原 PDF 页面。
* 支持透明叠加。
* 支持 HTML/CSS 风格。
* 与 PyMuPDF 删除、链接恢复流程整合简单。

缺点：

* 对极致微排版控制有限。
* 对复杂脚本、精确字距、断行惩罚、避头尾标点等控制不如完整排版引擎。
* 有些情况下需要反复试字号。

#### B 档：Pango + HarfBuzz + Cairo，自研 foreground layer

适合你追求“像 LaTeX 一样优雅”的生产级方案。HarfBuzz 负责 text shaping，也就是把 Unicode 字符映射成字体 glyph 并正确定位；PangoLayout 提供段落级排版，包括换行、对齐、两端对齐、省略等。([HarfBuzz 手册][15])

优点：

* 对复杂脚本、双向文本、连字、字形定位更可靠。
* 可拿到每个 glyph 的位置，方便重建链接热区。
* 可实现更复杂的 fit solver。
* 可输出更精确的视觉效果。

缺点：

* 工程量明显更大。
* 需要把 Pango/Cairo 的输出变成 PDF overlay，或把 glyph positions 转成 PDF text operators。
* 字体嵌入、ToUnicode、子集化要更认真处理。

#### C 档：HTML/CSS 全页重排，例如 WeasyPrint

WeasyPrint 是 HTML/CSS 到 PDF 的分页渲染引擎，适合从 HTML 生成漂亮 PDF。([Court Bouillon][16])
但对于你的任务，它更适合作为“重建型”备选方案，而不是默认方案。原因是：它会生成一份新 PDF，而不是原地修改原 PDF；原始内部跳转、注释、命名目标等需要额外迁移，难度更高。

### 8.3 Fit Solver：不要只做“字号缩小”

每个文本块需要一个排版求解器。目标是译文放进原 bbox，且美观、不重叠、不明显变小。

候选参数：

```python
font_size_scale = [1.00, 0.97, 0.94, 0.91, 0.88, 0.85, 0.82, 0.78]
line_height = [1.05, 1.10, 1.15, 1.20]
tracking = [0, -0.01, -0.02]  # 中文慎用
font_variant = ["regular", "condensed_if_available"]
paragraph_rewrite = [False, True]
```

评分函数：

```python
penalty =
    100000 * overflow_area
  + 10000  * collision_area
  + 5000   * clipped_glyph_count
  + 400    * abs(font_size_scale - 1.0)
  + 100    * bad_line_break_count
  + 80     * orphan_punctuation_count
  + 50     * line_count_deviation
  + 20     * raggedness_score
```

通过顺序：

1. 原字号尝试。
2. 轻微调行距。
3. 轻微缩字号。
4. 改用更紧凑翻译。
5. 最多缩到阈值，例如正文不低于原字号的 82% 或绝对 6.5pt。
6. 仍失败则标记人工审校或允许扩大到相邻空白区域。

### 8.4 中文排版细节

要像书籍/论文，中文不能只是换行：

* 标点避头尾：逗号、句号、分号、冒号、右括号、右引号不能出现在行首。
* 左括号、左引号不能出现在行尾。
* 英文缩写、变量、单位不能拆开。
* 公式占位符不要跨行断裂。
* 引文编号 `[12]`、`(7.70)` 不要拆开。
* 图表编号“图 2”、“表 1”不要拆开。
* 两栏论文建议左对齐或轻微两端对齐，不要产生过大字距。
* 页脚脚注不要为了塞进去把字号降得过小，宁可压缩译文。

---

## 9. 阶段七：删除原文字，不使用白底覆盖

这是你需求里最关键的一点。

### 9.1 正确思路

对 born-digital PDF，推荐用 **redaction 删除文字内容，但不填充背景**：

1. 对每个要翻译的文字区域生成 redaction 矩形。
2. `fill=False`，让 redaction 应用后不画白色填充。
3. `images=PDF_REDACT_IMAGE_NONE`，避免把图片区域打白。
4. `graphics=PDF_REDACT_LINE_ART_NONE`，避免删掉线条、表格边框、背景块。
5. 应用 redaction 后，原文字从内容流中物理删除。
6. 再写入译文。

PyMuPDF 的 redaction 文档说明，`fill=False` 可以抑制填充色，使矩形保持透明；`apply_redactions` 可以控制图片和矢量图形如何处理；文本删除是按字符 bbox 与 redaction 矩形是否重叠执行的。文档也明确提醒，所有与 redaction 矩形重叠的 links 会被移除，所以必须提前快照并在后面重建链接。([GitHub][9])

### 9.2 不建议直接用 redaction 的 replacement text

PyMuPDF 的 redaction 支持传入替换文字，但不适合你的高质量排版目标。文档说明 replacement text 字体支持有限，并且如果替换文字更长，可能出现难看的外观、换行或根本插不进去。([GitHub][9])

因此建议：

```python
# 只用 redaction 删除原文字
page.add_redact_annot(rect, fill=False, cross_out=False)
page.apply_redactions(
    images=fitz.PDF_REDACT_IMAGE_NONE,
    graphics=fitz.PDF_REDACT_LINE_ART_NONE,
    text=fitz.PDF_REDACT_TEXT_REMOVE
)

# 然后用独立排版引擎写译文
page.insert_htmlbox(rect, html, css=css, overlay=True, ...)
```

### 9.3 redaction 矩形不能粗暴等于整段 bbox

如果整段 bbox 包含行间背景、图形、链接、边框，风险会变高。更好的策略：

* 按行或字符 union 生成多个窄矩形。
* 对每行 bbox 左右略微扩展 0.3–0.8 pt。
* 上下不要扩太多，避免误删上下行。
* 对含公式的行，把公式 span 从 redaction 区域排除。
* 对链接区域先记录，redaction 后重建。
* 对表格单元格，矩形不要碰到表格线。

示意：

```python
for line in block.lines:
    text_spans = [s for s in line.spans if s.type == "text"]
    rect = union([s.bbox for s in text_spans])
    rect = rect.inflate(x=0.5, y=0.2)
    redaction_rects.append(rect)
```

### 9.4 扫描页的降级策略

如果页面是图片型文字，redaction 删除不了图像里的文字。此时你可以做：

```text
检测文字区域
  ↓
裁剪文字区域 + 周边背景
  ↓
背景复杂度判断
  ↓
简单背景：颜色/纹理采样补洞
复杂背景：图像修复模型 / OpenCV inpainting / LaMa 类模型
  ↓
写入译文
  ↓
QA 标记该页为 raster-inpainted
```

但是要诚实记录：这类页面无法保证“像原生 LaTeX 重新排版”，因为你没有原始背景，只能猜。

---

## 10. 阶段八：写入译文，保持透明背景和原排版质感

### 10.1 每类文本的写入规则

**正文块**

* 使用原 block bbox。
* 字体选择目标语言正文衬线字体。
* 字号初始值接近原字号。
* 行距 1.08–1.18。
* 多栏论文中尽量不跨栏。
* 默认不画背景。

**标题块**

* 字号可比原字号略小一点，因为中文标题视觉密度更高。
* 保留居中、加粗、颜色。
* 长标题可分两行，但不能压到作者信息。

**图注/表注**

* 小字号。
* 保留 “Figure 2.” → “图 2.” 或按配置保留英文。
* 不移动图片和表格。
* 图注不能压进图片。

**页眉页脚**

* 多数情况下不翻译页码。
* 期刊页眉、章节页眉可翻译，也可配置跳过。
* 页脚 DOI、版权声明默认不翻译。

**公式**

* 行间公式不翻译、不删除、不重绘。
* 行内公式作为占位符参与文本排版，或保持原公式 span 不删除。
* 如果公式嵌在英文句子中，最好将公式作为不可断 token 回填。

### 10.2 使用 PyMuPDF 写入的 MVP 方式

```python
css = f"""
body {{
  font-family: "{font_name}";
  font-size: {font_size}pt;
  line-height: {line_height};
  color: rgb({r},{g},{b});
  text-align: {align};
}}
"""

page.insert_htmlbox(
    rect,
    html_text,
    css=css,
    overlay=True,
    scale_low=0.85
)
```

PyMuPDF 文档说明 `insert_htmlbox` 在内容无法放入矩形时，可以选择只报告放不下，或者通过 `scale_low=0` 等策略缩放到适配。([GitHub][9])

### 10.3 高级方式：先生成透明 foreground PDF，再合成

对排版要求很高时，可以用 Pango/HarfBuzz/Cairo 生成一层只含译文的透明 PDF，再把它叠加到已删除原文字的 PDF 上。

```text
original.pdf
  ├─ remove original text → background_without_text.pdf
  └─ layout translated text → translated_text_layer.pdf
           ↓
      merge as foreground
           ↓
      translated.pdf
```

好处是文字排版完全受你控制。坏处是链接热区、字体嵌入、ToUnicode、层叠顺序、透明度都要自己管。

---

## 11. 阶段九：链接、目录、跳转的恢复策略

### 11.1 页面顺序和页数不要变

你的目标是保留原目录和引用跳转，所以默认应保持：

* page count 不变。
* 每页 mediabox/cropbox 不变。
* 页面顺序不变。
* 原图像和公式位置不变。
* 章节标题所在页不变。

这样，很多 outline/bookmark 目标仍然有效。

### 11.2 redaction 后必须重建重叠 links

因为 redaction 会删除重叠链接，处理顺序应是：

```python
links_snapshot = [page.get_links() for page in doc]
toc_snapshot = doc.get_toc(simple=False)

# 删除文字
apply_redactions()

# 写译文
insert_translated_text()

# 重建链接
for page_no, links in links_snapshot:
    for link in rebuild_link_rects(links):
        page.insert_link(link)

# 恢复 / 修正目录
doc.set_toc(toc_snapshot)
```

### 11.3 链接重建分三种

**第一种：整行级链接**

目录页、书籍目录、参考文献目录，链接通常覆盖整行。翻译后行位置基本不变，可以复用原 link rectangle。

**第二种：行内引用链接**

如 `[12]`、`(Smith, 2020)`、“Section 3”。这类应该通过占位符追踪新位置。最好让排版引擎返回占位符 bbox，再创建新的 link rectangle。

**第三种：URL 链接**

URL 如果不翻译，可以在写入后搜索 URL 文本并生成 link。若 URL 换行，需要多个矩形。PyMuPDF 的 `search_for` 可以返回命中文本的矩形，但重复 URL 时要用上下文 disambiguation。

---

## 12. 阶段十：表格、公式、图片、参考文献的特殊处理

### 12.1 表格

表格是翻译 PDF 中最容易翻车的部分。策略建议：

1. **优先保留表格线和背景**。
2. 删除单元格里的文字，不碰线条。
3. 每个单元格单独翻译和 fit。
4. 单元格文字不够放时，优先压缩译文，而不是缩到不可读。
5. 表头可适当改写。
6. 数字、单位、显著性标记、p 值、±、括号不要翻译。
7. 跨行跨列表格要识别 cell 合并。

如果 MinerU 只给 table bbox 和 HTML，不给每个 cell 的精确 PDF 坐标，可以用 PyMuPDF 的 table finder、Camelot、pdfplumber 或自研线条检测补充。复杂表格建议先跳过或输出人工审校标记。

### 12.2 公式

公式的最佳策略是 **不重画**：

* 行间公式：保留原 PDF 公式对象，不 redaction。
* 公式编号：如果是文字对象，可以翻译周边文本但保留编号。
* 行内公式：把公式区域从删除矩形中排除，或在译文中留出占位空间。
* MinerU 可以识别公式并转 LaTeX，但你不一定要用 LaTeX 重绘；重绘会产生字体和基线不一致的问题。

### 12.3 图片和图中文字

* 图片本体默认不翻译。
* 图注翻译。
* 图内标注如果是 PDF 文本对象，可以翻译；如果是图片像素，走 inpainting 或跳过。
* 坐标轴标签如果是文本对象，翻译时要考虑旋转。
* 图例、色条、legend 文字很短，适合单独处理。

### 12.4 参考文献

参考文献建议配置化：

```yaml
references:
  translate_section_title: true
  translate_article_titles: false
  translate_journal_names: false
  preserve_author_names: true
  preserve_doi: true
  preserve_url: true
```

学术 PDF 中 Reference 的链接目标很多，如果你翻译参考文献条目导致行数变化，可能影响引用跳转视觉位置。默认保留参考文献原文更稳。

---

## 13. 阶段十一：QA，决定系统能不能生产使用

你需要的不只是生成 PDF，而是自动判断它是否“好看、没坏、功能还在”。

### 13.1 渲染级 QA

每次输出后，渲染成图片：

```text
before/page_001.png
after/page_001.png
diff/page_001.png
```

检查：

* 是否有旧文字残留。
* 是否有译文超出 bbox。
* 是否文字重叠图片/公式/边框。
* 是否出现黑框、乱码、缺字。
* 是否透明背景正常。
* 是否某页变成空白或图像丢失。

### 13.2 几何级 QA

对每个译文 block：

```python
assert translated_text_bbox <= allowed_bbox
assert not intersects(translated_text_bbox, protected_formula_bboxes)
assert not intersects(translated_text_bbox, image_body_bbox)
assert font_size >= min_font_size
```

还要检查相邻块：

```python
for a, b in nearby_blocks:
    if overlap(a.translated_bbox, b.translated_bbox) > threshold:
        mark_error("overlap")
```

### 13.3 文本级 QA

* 翻译后不能漏掉 block ID。
* 保护 token 必须全部出现。
* 公式占位符数量一致。
* 引用编号数量一致。
* URL / DOI / email 不被改写。
* 页码不被错误翻译。
* 章节编号不丢失。
* 译文不能为空。
* 不出现模型解释性废话，如“以下是翻译”。

Structured Outputs 能显著降低结构化输出错误，因为它要求模型响应符合指定 JSON Schema。([OpenAI开发者][17])

### 13.4 功能级 QA

自动点击/检查：

* TOC entries 是否仍指向合法页。
* 内部 GoTo links 的 page index 是否存在。
* URL links 是否仍是 URI。
* 引用链接是否仍跳到 Reference。
* 书签数量是否与原 PDF 一致。
* 表单字段是否还存在。
* 注释是否还存在。
* 附件是否还存在。

### 13.5 生成 QA 报告

输出一个 HTML 或 JSON 报告：

```json
{
  "status": "needs_review",
  "pages": {
    "3": {
      "overflow_blocks": ["p003_b012"],
      "missing_tokens": [],
      "link_warnings": ["link_42 rectangle approximated"],
      "visual_diff_score": 0.18
    },
    "7": {
      "scan_page": true,
      "inpainting_used": true,
      "quality": "low"
    }
  }
}
```

---

## 14. 阶段十二：文件夹批处理、同级输出、原文件保留

你的 CLI 可以设计成：

```bash
pdf-translator input.pdf --to zh-CN
pdf-translator /books --to zh-CN --recursive
pdf-translator /papers --to zh-CN --workers 4 --engine openai-batch
```

### 14.1 输出规则

单 PDF：

```text
/path/a/book.pdf
/path/a/book.zh-CN.pdf
/path/a/book.zh-CN.translation.json
/path/a/book.zh-CN.report.html
```

文件夹：

```text
/input/A.pdf
/input/A.zh-CN.pdf

/input/sub/B.pdf
/input/sub/B.zh-CN.pdf
```

默认不覆盖：

```text
A.zh-CN.pdf
A.zh-CN.2.pdf
A.zh-CN.3.pdf
```

或者提供：

```bash
--overwrite
--output-dir /translated
--suffix ".translated.zh-CN"
```

### 14.2 任务恢复

对大 PDF 和文件夹必须支持断点续跑：

```text
.work/
  doc_hash/
    preflight.json
    mineru/
    layout_dom.json
    translation_cache.sqlite
    fitted_layout.json
    links_snapshot.json
    pages_done/
      0001.done
      0002.done
```

一页失败不能导致整本书全失败。最终报告里列出失败页和原因。

---

## 15. 推荐工程架构

### 15.1 模块划分

```text
pdf_translator/
  cli.py
  config.py

  preflight/
    inspect_pdf.py
    detect_scan.py
    detect_permissions.py

  mineru_adapter/
    run_mineru.py
    parse_pipeline_middle.py
    parse_vlm_model.py
    normalize_layout.py

  pdf_extract/
    pymupdf_styles.py
    links.py
    outlines.py
    annotations.py
    named_destinations.py

  layout_dom/
    model.py
    merge_spans.py
    reading_order.py
    protect_tokens.py

  translate/
    openai_client.py
    batch_builder.py
    schema.py
    cache.py
    glossary.py

  typeset/
    font_manager.py
    measure_pymupdf.py
    measure_pango.py
    fit_solver.py
    line_break.py

  render/
    erase_text.py
    draw_text_pymupdf.py
    draw_text_cairo.py
    restore_links.py
    save_pdf.py

  qa/
    render_pages.py
    visual_diff.py
    overlap_check.py
    link_check.py
    text_check.py
    report.py
```

### 15.2 配置文件示例

```yaml
target_language: zh-CN

output:
  mode: sibling
  suffix: ".zh-CN"
  overwrite: false
  keep_sidecars: true

mineru:
  backend: pipeline
  use_gpu: true
  fallback_to_ocr: true

translation:
  provider: openai
  mode: batch
  model: configurable
  structured_output: true
  glossary_path: ./glossary.yml
  cache_path: ~/.cache/pdf-translator/translations.sqlite

layout:
  preserve_page_count: true
  preserve_images: true
  preserve_equations: true
  translate_headers: false
  translate_footers: false
  translate_references: false
  min_body_font_size_pt: 6.5
  max_font_shrink: 0.82
  allow_rewrite_to_fit: true

fonts:
  zh-CN:
    serif: "Source Han Serif SC"
    sans: "Source Han Sans SC"
    fallback: "Noto Serif CJK SC"

links:
  restore_original_links: true
  rebuild_inline_links: true
  link_anchor_strategy: token_bbox

qa:
  render_dpi: 180
  fail_on_overlap: true
  fail_on_missing_tokens: true
  generate_html_report: true
```

---

## 16. MVP 到生产级路线图

### 16.1 MVP：先把 born-digital 论文跑通

目标：

* 支持英文论文 PDF → 中文 PDF。
* 保留图片、公式、页数。
* 原文物理删除，不用白底。
* 写入译文不溢出。
* URL 和目录大体保留。

技术：

* MinerU pipeline `middle.json`。
* PyMuPDF 抽取 style、link、toc。
* OpenAI Responses API + Structured Outputs。
* PyMuPDF redaction `fill=False` 删除文字。
* PyMuPDF `insert_htmlbox()` 写译文。
* 简单字号二分 fit。
* 简单 render QA。

先不要做：

* 扫描 PDF。
* 表格复杂翻译。
* 行内链接精确重建。
* 多语言复杂脚本。
* 全量命名目标修复。

### 16.2 Beta：解决论文/书籍常见问题

增加：

* 文件夹批处理。
* Batch API。
* 翻译缓存。
* 图注、表注、脚注分类排版。
* 公式 token 保护。
* 引用 token 保护。
* 链接快照和重建。
* TOC 精确保留。
* 表格 cell-level 翻译。
* QA HTML 报告。
* 失败页跳过和恢复。

### 16.3 Production：追求稳定、可审校、可回归

增加：

* Pango/HarfBuzz 测量引擎。
* glyph-level link bbox。
* 多渲染器 QA。
* OCR/扫描页降级路线。
* 人工审校界面。
* 术语库和项目级翻译记忆。
* 页面级并发。
* 安全日志脱敏。
* 许可证合规检查。
* PDF/A、元数据、附件、表单处理。

PyMuPDF 和 MuPDF 当前采用 AGPL 或商业许可双授权；如果做商业闭源产品，应提前确认许可证路径。([PyMuPDF][18])

### 16.4 Publisher-grade：接近你图里“像重新排版”的效果

增加：

* 自研段落排版器。
* 中文标点禁则。
* 断行惩罚模型。
* 自动压缩译文。
* 局部重排相邻块。
* 图文避让。
* 字重匹配。
* 字距和行距微调。
* 标题层级视觉系统。
* 页面整体视觉评分。

---

## 17. 最容易踩的坑

### 坑一：直接在 PDF 内容流里替换字符串

不要把 PDF 当 HTML 或 TXT。PDF 里的文字经常不是 Unicode 字符串，而是字体编码、glyph id、子集字体、CMap、ToUnicode 映射和定位指令的组合。直接查找替换内容流很容易乱码、漏字、破坏字距、破坏字体资源。更稳的是：抽取文字 → 删除原文字 → 用新字体重绘译文。

### 坑二：用白色矩形覆盖

这正是你明确不想要的。白底覆盖在非白页面、渐变背景、图片、彩色框、扫描纸张上会立刻露馅。正确方式是透明 redaction 删除文本对象；扫描页才考虑背景修复。

### 坑三：只用 MinerU，不看 PDF 原对象

MinerU 给你 layout 语义，但不一定知道 PDF 的链接、目录、命名目标、注释、字体资源、真实页面盒。必须结合 PyMuPDF/pikepdf。

### 坑四：链接提前没保存

redaction 会删除重叠链接。你必须先 snapshot，再删除文字，再重建链接。

### 坑五：翻译太忠实，排版太难看

“忠实”不等于“逐词冗长”。论文窄栏需要紧凑译文。建议允许二次压缩，尤其标题、图注、表注、脚注。

### 坑六：字体没有 CJK 字形

如果使用原英文字体写中文，必然缺字或 fallback 混乱。应使用完整 CJK 字体，并嵌入子集。

### 坑七：只看生成 PDF，不做渲染对比

PDF 在一个阅读器里看着没问题，不代表另一个阅读器没问题。至少用一个稳定渲染器自动渲染；生产环境建议用两个。

---

## 18. 我建议你的最终技术选型

最实用、可落地、效果好的组合是：

```text
版面识别：
  MinerU pipeline backend 为主，VLM/OCR 作为扫描页 fallback

PDF 操作：
  PyMuPDF 负责文本抽取、redaction、写入译文、链接/目录基本处理、渲染
  pikepdf/qpdf 负责低层对象、命名目标、元数据、附件、修复、线性化

翻译：
  OpenAI Responses API + Structured Outputs
  大批量用 Batch API
  SQLite translation memory

排版：
  第一版用 PyMuPDF insert_htmlbox
  生产版加入 Pango/HarfBuzz 测量
  更高要求用 Pango/Cairo foreground PDF layer

字体：
  Source Han Serif / Noto Serif CJK 作为中文论文书籍正文
  Source Han Sans / Noto Sans CJK 作为无衬线 fallback
  fontTools/pyftsubset 做字体子集化

QA：
  pdfium/poppler 渲染对比
  几何 overlap 检测
  token preservation 检测
  link/toc 自动检查
  HTML 报告
```

---

## 19. 最小可行伪代码

```python
def translate_pdf(input_pdf: Path, target_lang: str) -> Path:
    output_pdf = make_sibling_output_path(input_pdf, target_lang)

    # 1. 原文件不动，复制到临时工作文件
    work_pdf = copy_to_workdir(input_pdf)

    # 2. 预检
    preflight = inspect_pdf(work_pdf)

    # 3. MinerU layout
    mineru_result = run_mineru(work_pdf)
    layout = parse_mineru_to_layout_dom(mineru_result)

    # 4. PyMuPDF 补充 PDF 真实信息
    doc = fitz.open(work_pdf)
    style_info = extract_styles_with_pymupdf(doc)
    links_snapshot = snapshot_links(doc)
    toc_snapshot = doc.get_toc(simple=False)

    # 5. 合并样式和 layout
    layout = enrich_layout(layout, style_info, links_snapshot)

    # 6. 保护公式、引用、链接锚点
    units = build_translation_units(layout)

    # 7. 翻译
    translations = translate_units_with_cache(units, target_lang)

    # 8. fit solver
    fitted_blocks = []
    for block in layout.translatable_blocks:
        result = fit_translation_into_box(
            block=block,
            translation=translations[block.id],
            font_manager=font_manager,
        )
        fitted_blocks.append(result)

    # 9. 删除原文字，不填白底
    for page_index, page in enumerate(doc):
        redaction_rects = build_redaction_rects(layout.pages[page_index])
        for rect in redaction_rects:
            page.add_redact_annot(rect, fill=False, cross_out=False)

        page.apply_redactions(
            images=fitz.PDF_REDACT_IMAGE_NONE,
            graphics=fitz.PDF_REDACT_LINE_ART_NONE,
            text=fitz.PDF_REDACT_TEXT_REMOVE,
        )

    # 10. 写入译文
    for fitted in fitted_blocks:
        page = doc[fitted.page_index]
        page.insert_htmlbox(
            fitted.rect,
            fitted.html,
            css=fitted.css,
            overlay=True,
            scale_low=fitted.scale_low,
        )

    # 11. 重建 links / toc
    rebuild_links(doc, links_snapshot, fitted_blocks)
    doc.set_toc(toc_snapshot)

    # 12. 保存
    doc.save(
        output_pdf,
        garbage=4,
        deflate=True,
        clean=True,
    )
    doc.close()

    # 13. QA
    report = run_qa(input_pdf, output_pdf, layout, fitted_blocks)
    write_report(report, output_pdf.with_suffix(".report.html"))

    return output_pdf
```

---

## 20. 最终建议

你的功能可以做成两个模式：

**默认模式：Faithful PDF Translation**

* 保持页数、页面尺寸、图像、公式、目录、链接。
* 每个文本块在原位置内重排。
* 不白底覆盖。
* 最适合论文、教材、技术文档。

**高级模式：Beautiful Re-typeset Translation**

* 允许局部移动块、压缩/扩展段落、重排脚注。
* 效果更像真正翻译排版书。
* 链接和目录需要更复杂的重建。
* 适合高价值书籍或出版级处理。

从工程落地看，先做默认模式，核心攻克 **透明删除原文字 + block 级 fit + 链接恢复 + QA**。等这个稳定后，再上 Pango/HarfBuzz 和更高级的中文排版规则。这样最接近你图里的效果，也不会一开始就陷入“重新实现 InDesign/LaTeX”的巨大工程。

[1]: https://opendatalab.github.io/MinerU/ "MinerU - MinerU"
[2]: https://pymupdf.readthedocs.io/en/latest/tutorial.html?utm_source=chatgpt.com "Tutorial - PyMuPDF documentation"
[3]: https://pikepdf.readthedocs.io/en/latest/index.html "pikepdf Documentation — pikepdf 10.5.1 documentation"
[4]: https://www.nutrient.io/guides/web/signatures/digital-signatures/troubleshooting/document-modified-since-signature/?utm_source=chatgpt.com "Modify PDF after digital signing"
[5]: https://opendatalab.github.io/MinerU/reference/output_files/ "Output File Format - MinerU"
[6]: https://pymupdf.readthedocs.io/en/latest/app1.html "Appendix 1: Details on Text Extraction - PyMuPDF documentation"
[7]: https://pymupdf.readthedocs.io/en/latest/link.html "Link - PyMuPDF documentation"
[8]: https://pikepdf.readthedocs.io/en/latest/topics/outlines.html "Outlines — pikepdf 10.5.1 documentation"
[9]: https://github.com/pymupdf/PyMuPDF/blob/main/docs/page.rst "PyMuPDF/docs/page.rst at main · pymupdf/PyMuPDF · GitHub"
[10]: https://developers.openai.com/api/reference/responses/overview/ "Responses Overview | OpenAI API Reference"
[11]: https://developers.openai.com/api/docs/guides/batch "Batch API | OpenAI API"
[12]: https://github.com/adobe-fonts/source-han-serif?utm_source=chatgpt.com "adobe-fonts/source-han-serif - 思源宋體香港"
[13]: https://pymupdf.readthedocs.io/en/latest/faq/index.html "FAQ - PyMuPDF documentation"
[14]: https://pymupdf.readthedocs.io/en/latest/page.html "Page - PyMuPDF documentation"
[15]: https://harfbuzz.github.io/why-do-i-need-a-shaping-engine.html "Why do I need a shaping engine?: HarfBuzz Manual"
[16]: https://doc.courtbouillon.org/weasyprint/stable/ "WeasyPrint 68.1 documentation"
[17]: https://developers.openai.com/api/docs/guides/structured-outputs "Structured model outputs | OpenAI API"
[18]: https://pymupdf.readthedocs.io/en/latest/about.html?utm_source=chatgpt.com "Features Comparison - PyMuPDF documentation"

```