# plan-comparison_3 审查与差距分析（用于反推 Skill 加固点）

目标：
- 逐段对照 `improvement/plan-comparison_3.md` 中 **Skill 得出的 Plan/Task** 与 **我所希望的 Plan**
- 把差距转写成“可落盘的 Skill 改动清单”（协议/模板/校验脚本/playbook/示例）

说明：
- 本文是诊断与修复路线图，不是对某一次 Plan 的打分。
- 输出的改动必须保持“通用任务可用”，但对 **外科手术型任务（PDF/排版/交互保持）** 要显著更强。

---

## 0) 核心结论（一句话）

Skill 产出的 Plan 已经具备“外科任务意识”（Preflight/Units/Fit/Erase/Writeback/Links Count），但与目标 Plan 相比仍停留在 **MVP 级“能跑通”密度**，缺少生产级必须写清的：**外部调研证据包、功能层快照与重建、坐标与版本适配、结构化翻译与缓存、排版引擎分档与中文排版规则、redaction 副作用与细粒度矩形策略、多渲染器 QA 与证据结构、模块化工程架构与接口规格**。

这类差距无法靠“执行阶段补补丁”弥补，必须在 Plan Mode 通过门禁把 Plan 写深（并由脚本/清单校验），否则执行会稳定失控。

---

## 1) Research 深度与“必须联网检索”未落地

### 目标 Plan 的关键点
- 外科任务在 Plan 阶段必须做高质量联网检索，且要落盘来源、关键事实、影响面。
- 关键事实涉及：MinerU 版本差异、PyMuPDF redaction 副作用、pikepdf/qpdf 低层对象、渲染器差异、数字签名等。

### Skill Plan 的差距
- Research Log 主要是“本地实验/帮助文档/仓库样例”，并出现“未做外网检索（用户未要求）”的论证方式。
- 这会直接导致：关键边界行为靠猜（例如 redaction 是否会移除 link），Plan 的风险缓释不足。

### Skill 必须改动点
- **协议层**：明确“用户没要求联网”不是跳过 Research Gate 的理由；L3 默认必须联网（用户明确禁止除外）。
- **校验脚本**：L3 Plan 必须出现可追溯的外部来源（至少一定数量的 URL/来源条目），否则 Plan Quality Gate 判定 `blocked`，不得请求执行授权。

---

## 2) Domain Preflight 不够“工程化”（字段/路由/阻塞标准不足）

### 目标 Plan 的关键点
- 每个 PDF 先生成 `preflight.json`：加密/权限/签名、outline、links、forms、named destinations、page labels、attachments/metadata 等，并计算 born-digital vs scan-like 比例，决定后续路线。

### Skill Plan 的差距
- 有 Preflight 概念，但缺少明确的 `preflight.json` 字段清单与“路由结论”结构；没有把签名/权限风险作为交付事实写进 Plan。

### Skill 必须改动点
- **PDF playbook**：补齐 `preflight.json` 最小字段与 route 决策枚举。
- **Plan Quality Gate（外科加固）**：增加字段级检查项（命中则强制）。

---

## 3) MinerU 版本/后端适配与坐标统一需要更显式的规格

### 目标 Plan 的关键点
- MinerU 的 bbox 表达与 backend（VLM/pipeline）可能不同；Plan 要写“适配层”，不能硬编码某一种结构。
- 坐标统一要写清：内部统一坐标系（origin/unit/rotation），并给出转换公式与验证方式。

### Skill Plan 的差距
- 提到 schema 差异与“schema 校验”，但缺少：
  - 版本/后端识别方式与兼容策略
  - 坐标统一的明确约定 + 旋转页处理 + 抽检可视化证据

### Skill 必须改动点
- **PDF playbook**：加入“坐标统一 Gate”与最小公式/抽检方法。
- **Plan.deep 模板**：外科任务必须在 Specification 或 QA Plan 内写出坐标约定与验证证据。

---

## 4) 功能层（links/toc/bookmarks/annotations/…）需要“快照→删除→重建”的完整闭环

### 目标 Plan 的关键点
- 先保存功能快照：toc、page_links、annotations/widgets、page labels、named destinations、metadata、attachments。
- redaction 可能移除与矩形重叠的 links，因此不能只做“links count 对比”；要有重建策略。
- 生产级要做 **链接锚点映射**：保护 token → 翻译保留 → typeset 记录 glyph bbox → 重新 insert_link。

### Skill Plan 的差距
- 功能层只做到“links count 前后对比”，没有快照结构与重建策略，也没有锚点映射算法。

### Skill 必须改动点
- **PDF playbook**：增加功能快照 schema、重建策略（保守/生产级）、锚点映射算法步骤。
- **外科门禁清单**：把“只做 links count”明确标注为 MVP，且必须在 Plan 的 Roadmap 里写出升级路径。

---

## 5) IR/DOM（Layout DOM）与稳定 ID 的规格需要更具体

### 目标 Plan 的关键点
- Layout DOM：Page→Column→Block→Line→Span→Unit，包含 style、links、fit_result 等；ID 必须稳定以支撑缓存与断点续跑。

### Skill Plan 的差距
- 有 units + stable ID 的概念，但没有把 DOM 作为“一等规格”写清（字段、层级、与功能层绑定方式）。

### Skill 必须改动点
- **PDF playbook**：加入推荐数据结构（示例 dataclass）与最小字段约束。
- **Plan.deep 模板**：Data Model 小节对外科任务应给出更强的结构化要求（至少：DOM schema + ID 策略 + cache key）。

---

## 6) 翻译引擎：缺少结构化输出、缓存与二次改写的完整设计

### 目标 Plan 的关键点
- 翻译单位不能整页；必须结构化（JSON schema），并有缓存（SQLite/JSONL）。
- fit 失败需要二次“压缩译文”的改写请求，而不是无限缩小字号。
- 批处理（Batch）与术语表/占位符保护是工程必须项。

### Skill Plan 的差距
- 只有“翻译 + cache（概念）”，缺少 schema/caching 表结构/键设计/改写策略/批处理策略。

### Skill 必须改动点
- **PDF playbook**：补齐结构化 schema、cache key、SQLite 表结构示例、二次改写策略与门禁。
- **Plan Quality Gate（外科加固）**：要求 Plan 至少写清翻译 schema + 缓存策略。

---

## 7) 排版：需要“分档能力 + Fit Solver 评分函数 + 中文排版规则”

### 目标 Plan 的关键点
- 排版引擎分三档：PyMuPDF textbox/htmlbox（MVP）、Pango+HarfBuzz+Cairo（生产级）、全页重排（备选）。
- Fit Solver 不仅是字号缩小；需要参数搜索 + penalty 函数 + CJK 禁则/标点避头尾等规则。

### Skill Plan 的差距
- 只写 `insert_textbox` 字号搜索；未定义 penalty、中文禁则、以及升级到 shaping 引擎的路径。

### Skill 必须改动点
- **PDF playbook**：补齐三档排版能力、Fit Solver 评分函数、中文排版规则与“失败判据→回到 Fallback Register”的约束。
- **Task 分解标准**：把“排版分档与升级路线”作为外科任务里程碑之一（MVP→Beta→Production）。

---

## 8) 删除原文字：redaction 的副作用与矩形策略缺失

### 目标 Plan 的关键点
- 只用 redaction 删除原文字；不使用 replacement text。
- redaction 矩形应按行/字符 union 生成，避免粗暴用整段 bbox；并排除公式/链接等敏感区域。
- 明确 redaction 会移除重叠 links → 必须先快照并重建。

### Skill Plan 的差距
- 使用“unit bbox 直接 redaction”，风险较高；且没有把“links 会被移除”的风险写入 Plan。

### Skill 必须改动点
- **PDF playbook**：加入“按行矩形”策略与排除规则；把“links 会被移除”写成硬风险与必做快照/重建步骤。
- **Plan Quality Gate（外科加固）**：要求 Plan 写明 redaction 粒度策略与副作用验证。

---

## 9) QA：缺少多渲染器、几何自动化、功能可点击证据的结构化设计

### 目标 Plan 的关键点
- QA 需要：渲染对比、溢出/重叠检测、旧文字残留、链接可点击、目录可跳转。
- 多渲染器抽检（MuPDF + pdfium/poppler）避免单一引擎误判。
- QA 产物必须结构化：report + screenshots + failure pages list。

### Skill Plan 的差距
- QA 偏“人工抽检 + links count”；缺少 multi-renderer 与更强的证据结构。

### Skill 必须改动点
- **PDF playbook**：给出 QA 工件清单与最小字段（report schema）。
- **Validate 协议/模板**：对外科任务强化“多渲染器证据入口”。

---

## 10) 工程架构与接口规格：需要从 Task 清单升级为“模块化系统设计”

### 目标 Plan 的关键点
- 明确模块边界：preflight / mineru_adapter / pdf_extract / layout_dom / translate / typeset / render / qa / function_restore。
- 每个模块定义输入/输出工件与验证点。

### Skill Plan 的差距
- Task Group 命名有分段，但缺少模块接口与 I/O 工件的“稳定规格”（会导致实现阶段随手写）。

### Skill 必须改动点
- **PDF playbook**：补齐推荐模块与 I/O 工件清单。
- **Plan.deep 模板**：在 Interfaces/State/Workdir 部分要求写清模块 I/O 与落盘工件。

---

## 11) 需要落盘的 Skill 改动清单（可直接执行）

1) **加固校验脚本**：
   - `scripts/validate_plan_task_quality.py`：增加 L3 的 Research Log 计数/URL 检查；并对“外科/PDF” Plan 增加关键词门禁（Functional snapshot/Link rebuild/Layout DOM/Typesetting tiers/Redaction strategy/Multi-renderer QA）。
2) **扩写 PDF playbook**：
   - 把目标 Plan 的 Stage 1–17 的关键要求合并进 `library/pdf-layout-translation-playbook.md`。
3) **改 Router/Plan 的硬路由**：
   - 外科任务默认 `Research → Plan`（不能直接 Plan），且 Research 阶段必须产生 ≥8 外部来源（除非用户明确禁止联网）。
4) **把“跳过联网”写进 gotchas**：
   - 在 `protocols/10-gotchas.md` 增加“L3 不做联网检索=门禁失败”的提醒。
5) **升级 PDF 示例**：
   - `examples/software-pdf-layout-translation/Plan.sample.md` 补齐：preflight schema、functional snapshot schema、DOM 数据结构、translation schema+cache、typesetting tiers、fit penalty、redaction line-rect 策略、multi-renderer QA、模块架构。

