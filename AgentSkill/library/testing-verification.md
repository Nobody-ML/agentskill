# Testing & Verification（测试与验证）检查表

适用：Software / Research / Writing（验证逻辑相同：结论必须有证据）。

---

## 触发条件

- 任何“完成/通过/修复/正确/可复现”的声明
- Level ≥ L2
- 风险较高（安全/合规/不可逆）

---

## A. 证据门禁（铁律）

- [ ] 未运行验证命令/未观察到结果 → 不得宣称通过
- [ ] 证据必须可复查：命令、退出码、关键输出摘要、日志/截图/链接路径
- [ ] 证据入口必须写入 `State.md` 的 Evidence Index

来源：
- `superpowers/skills/verification-before-completion/SKILL.md`（Evidence before claims）

---

## A.1 验证数据门禁（真实数据优先）

> 目的：把“真实世界会不会炸”的风险前置，而不是在 synthetic 数据上获得虚假安全感。

数据类型（必须在证据中标注）：
- `real`：真实系统/真实数据源样本
- `sanitized-real`：真实样本脱敏版（裁剪/打码/去标识）
- `synthetic`：临时生成的模拟数据

检查项：
- [ ] Level ≥ L2：关键路径至少一次使用 `real` 或 `sanitized-real` 验证
- [ ] 只有在用户明确确认“没有可用真实样本（含脱敏样本）”后，才允许 `synthetic`
- [ ] 使用 `synthetic` 时记录差距：哪些失败模式可能被遗漏（写入 Plan/State）

---

## B. 软件测试：从“故障”到“失败”

检查项：
- [ ] 明确：要防的是 Fault（缺陷）还是 Failure（运行失败）
- [ ] 覆盖关键路径 + 失败路径 + 边界条件

来源：
- SWEBOK v4.0a — Chapter 05 *Software Testing*, §1.1 *Faults vs. Failures*

---

## C. 测试层级（最小集合）

最小集合按任务实际选，但必须覆盖“最危险的那条路径”：

- 单元测试（最快反馈）
- 集成测试（模块交互）
- 端到端/手动走通（关键用户路径）

来源：
- SWEBOK v4.0a — Chapter 05 *Software Testing*, §1 *Fundamentals*（Key issues / test case creation）
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Ch.5 *Feedback*（Prefer early feedback）

---

## C.1 多维度验证（不止正确性）

> 目的：把“跑了测试但不符合用户需求/规范/性能不可用”的风险前置。正确性只是最低门槛。

检查项（按任务选最相关的子集，至少覆盖 Top 2–4 风险）：
- [ ] Correctness：对照验收标准/关键路径
- [ ] Spec & Consistency：接口/错误语义/边界/日志/配置符合 Plan 的 Spec
- [ ] Failure Modes：错误输入/缺资源/权限不足/网络异常等失败判据清楚且可复查
- [ ] Performance & Resource：至少一次 smoke check（耗时/内存/吞吐/峰值）；高风险时做基准对比
- [ ] Maintainability 信号：复杂度、重复、可读性（作为 Review 的证据输入）
- [ ] Security & Compliance：敏感信息、危险操作、权限边界门禁
- [ ] Docs & Operability：运行说明/验证说明/Runbook 能支撑复查与复跑
- [ ] Visual/UX（按需）：截图/渲染/图示可读性（Writing/UI 任务）

---

## C.2 验证手段工具箱（把“能想到的方法”显式化）

> 目的：当用户要求“多种测试/多种证据”，把手段枚举出来，避免只跑一条命令就宣称通过。

常用手段（按 Track/WorkType 选择）：
- 自动化：单测/集成/E2E、静态检查（lint/typecheck）、契约/断言
- 手工路径：关键用户路径 + 失败路径 + 边界输入
- 数据验证：真实样本/脱敏样本回放、日志回放、公开数据集对照
- 性能验证：profile、基准对比、资源峰值观测（CPU/GPU/内存/IO）
- 工具验证：diff、grep/rg 搜索、格式化器、依赖分析、许可证/安全扫描（按环境可用性）
- 文档验证：逐步照着 Runbook 走一遍、示例可运行、引用可追溯
- 视觉验证（按需）：截图、渲染结果比对、图示可读性检查
- 来源验证（Research/Writing）：关键结论映射到来源条目（State Evidence Index）

---

## D. 验证矩阵（L3 建议强制）

把“验收契约（AC-XXX）”逐条映射到证据：

| AC | 验证方式 | 证据入口 | 状态 |
|---|---|---|---|
| AC-001 | 单测/命令/截图 | State.md#EvidenceIndex/... | pending/passed/blocked |

来源：
- SWEBOK v4.0a — Chapter 01 *Software Requirements*, §4.3（验收标准驱动）

---

## E. Research 验证（最小实验）

检查项：
- [ ] 最小可行实验（MVE）可运行
- [ ] 指标可计算，定义清晰
- [ ] 至少一个基线/对照
- [ ] 失败判据写清（什么情况下结论不成立）

来源：
- Farley — Ch.7 *Empiricism*（避免自我欺骗）

---

## F. Writing 验证（可操作性与一致性）

检查项：
- [ ] 关键结论有来源（可追溯）
- [ ] 示例可运行（给出运行方式与输出摘要）
- [ ] 术语一致、图示可读（图注解释用途）

来源：
- Ousterhout — Ch.13/15（注释/文档作为设计工具）
