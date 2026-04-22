# Format Surgery Systems（格式外科 / 保结构改写）作战手册

适用：
- Track：Software / Writing / Research（混合）
- Level：L3（默认）；L2 命中“外科手术型任务”信号时同样适用

典型任务：
- PDF 翻译但保持排版与交互功能（链接/目录/书签/注释/表单）
- “不改变行为”地重写/迁移复杂产物（富文本、Office、渲染产物、可交互文档）
- 任何“看起来是改文本，实质是改一个对象系统”的工作

核心结论：
这类任务不是字符串替换，而是 **对象级别的版式/功能外科系统**。Plan 必须以“阶段流水线 + 阶段→技术→验证”方式落盘，否则必然敷衍、必然漂移、必然在 Validate 才爆炸。

对应门禁：
- `protocols/00-hard-gates.md`：G2/G3/G4/G6/G7/G8/G9
- `protocols/01-plan-mode-and-deep-plan.md`：Deep Plan 最低结构（含阶段→技术→验证映射）
- `protocols/04-validation-real-data-first.md`：真实数据优先 + 分层验证节奏

---

## 1) 系统思维：先定义“必须保留的性质”

这类任务的第一件事不是选库，而是写清 “must_preserve / must_avoid”：
- must_preserve：交互功能、视觉结构、页数/页面尺寸、可搜索性、可复制性、元数据等
- must_avoid：白底覆盖、静默降级、未经确认兜底、重排导致跳转失效等

这些内容必须写进 Plan 的 User Intent Lock，并在执行中作为硬约束复读。

---

## 2) 通用阶段流水线（模板）

```text
Inputs
  ↓
Domain Preflight（分类/路由/风险/可行性）
  ↓
Parse / Extract（抽取语义与几何）
  ↓
Enrich with Ground Truth（补真实对象信息：样式/坐标/功能对象）
  ↓
Build IR / DOM（中间表示：结构化、可追踪、可恢复）
  ↓
Protect Invariants（保护不应被改写的 token）
  ↓
Transform（翻译/改写/结构化输出 + 缓存 + 批处理）
  ↓
Fit / Typeset（把新内容适配到原几何约束内）
  ↓
Erase / Rewrite（删除原内容，不改变背景）
  ↓
Restore Functional Layer（链接/目录/书签/注释/表单等）
  ↓
QA & Evidence（渲染/几何/功能/多渲染器）
  ↓
Batch / Resume（文件夹处理、断点续跑、失败隔离）
  ↓
Deliver（交付回执 + 证据索引 + 残余风险）
```

要求：
- Plan 不能只写“做这些步骤”；必须写 **每个阶段用什么技术、输出什么工件、怎么验证**。

---

## 3) 阶段→技术→验证映射（最小表）

Plan 必须至少包含一张这样的表（可扩展）：

| Stage | Goal | Inputs → Outputs | Candidate tech | Recommended tech | Key risks | Validation & evidence |
|---|---|---|---|---|---|---|
| Preflight | 分类与路由 | input → preflight.json | parser A/B | A | 误判导致后续全错 | 预检报告 + 统计 |
| IR/DOM | 结构化中间表示 | extracted → dom.json | schema v1/v2 | v2 | ID 不稳定 | schema 校验 + diff |
| Typeset | 适配与排版 | translation → fitted layout | engine A/B | A | 溢出/重叠 | overlap check + render |
| Restore | 功能恢复 | snapshots → restored | tool A/B | A | 跳转失效 | link/toc check |

---

## 4) Domain Preflight（领域预检）必备内容

预检的作用：
- 决定能不能做高质量替换
- 决定走哪条 pipeline（保守 / 推荐 / 高级）
- 把“不可实现/高风险”提前暴露并落盘

预检报告建议最小字段：
- 输入基本信息：页数/尺寸/旋转/加密/权限/签名
- 功能对象：是否有链接/目录/命名目标/注释/表单/附件/元数据
- 内容类型：born-digital 比例、扫描页比例、混合页比例
- 风险与路由结论：推荐走哪条路线、禁止做什么、需要什么额外输入

预检失败处理：
- 不得静默降级；必须回到 Plan 更新验收或登记 fallback 并获得确认。

---

## 5) IR / DOM（中间表示）必须满足的性质

DOM/IR 必须支持：
- 可追踪：每个可改写单元有稳定 ID，能映射回原对象
- 可恢复：能从落盘文件恢复继续（断点续跑）
- 可验证：能做几何检查（bbox/overflow/overlap）
- 可扩展：允许后续加入样式、链接锚点、token 保护等字段

建议字段（抽象层级）：
- Document → Page → Column/Region → Block → Line → Span → Unit

---

## 6) Protect Invariants（保护不应被改写的 token）

常见保护对象：
- 公式、代码、URL、DOI、引用编号、图表编号、页码、链接锚点

策略：
1) 在 IR 层把这些片段标记出来
2) 在 transform 前把它们替换成占位符 token
3) 要求 transform 输出保留 token
4) typeset/restore 时用 token 位置重建功能对象（例如链接热区）

---

## 7) QA & Evidence（验证必须覆盖“可感知 + 功能”）

对外科任务，Validate 的最低集合：
- 渲染证据：页级截图、可视化 diff（抽样或全量）
- 几何检查：溢出/重叠/越界/旧内容残留
- 功能检查：链接/目录/跳转可点击、热区矩形合理
- 多渲染器一致性（需要时）：至少两种渲染引擎抽样对比

Fail Criteria（建议写入 Plan）：
- 产物打不开、页数/页面尺寸变化
- 功能对象显著丢失
- 大面积遮罩/背景破坏
- 溢出/重叠不可接受

---

## 8) Batch & Resume（长任务的可控性）

长任务必须支持：
- 断点续跑（按页/按文件）
- 失败隔离（单页失败不拖垮整本）
- 工作目录结构可复查（可清理、可复跑）

推荐工作目录结构（示例）：

```text
.work/
  job_id/
    preflight.json
    extract/
      raw.json
      dom.json
    translate/
      cache.sqlite
      units.json
    typeset/
      fitted.json
    restore/
      functional_snapshot.json
    qa/
      report.html
      screenshots/
    pages_done/
      0001.done
```

---

## 9) Plan 输出要求（把“深思熟虑”写出来）

Plan 至少要能回答这些问题：
- 为什么这个任务是 L3（风险/复杂度在哪里）
- 每个阶段用什么技术，为什么不用备选方案
- 每个阶段怎么验证、证据是什么、失败判据是什么
- 哪些情况必须停线回 Plan（数据缺失/权限/格式不可控/链接丢失等）
- MVP→Production 的路线图（先打通关键门槛，再堆质量）

