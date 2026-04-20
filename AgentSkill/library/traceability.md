# Traceability（需求追溯表）

目的：把用户诉求写成可追溯的条目，并标注它在本 AgentSkill 的落点（stage / template / State / version plan）。

说明：
- 本文件是“地图”，不替代规则本身；以 `AgentSkill/SKILL.md` 与 `AgentSkill/stages/*/SKILL.md` 的硬约束为准。
- 追溯采用“主约束在主 SKILL，细则在 stage，清单在 library，落盘在 templates/State”的组织方式，避免重复粘贴导致不一致。

---

## RQ-001：覆盖多场景（Research / Software / Writing / Simple）

定义：
- 同一套渐进式披露工作流覆盖科研、工程、写作与简单任务；入口统一路由，后续按需加载规则。

落点：
- 总览与场景枚举：`AgentSkill/SKILL.md`（“这一套解决什么问题”与“典型场景”）
- 入口路由与 Track 判定：`AgentSkill/stages/router/SKILL.md`

---

## RQ-002：渐进式披露（只读下一步）

定义：
- Router 只做分流与门禁；不要一次性读完所有规则；下一步只加载一个 stage 的 SKILL。

落点：
- 目录结构 + “只读下一步”规则：`AgentSkill/SKILL.md`
- 路由输出与“下一阶段只选一个”：`AgentSkill/stages/router/SKILL.md`

---

## RQ-003：大任务先对齐后执行（Plan Mode 硬门禁）

定义：
- Level≥L2 默认处于 Plan Mode：深读/检索/对齐/落盘 Plan+Task；用户未授权前不得进入执行（改代码/跑长任务/训练/监控等）。

落点：
- 两相系统 + 授权口令：`AgentSkill/SKILL.md`
- 路由优先级（未授权/Plan 未就绪 → 强制 Plan）：`AgentSkill/stages/router/SKILL.md`
- Plan Mode 允许/禁止动作：`AgentSkill/stages/plan/SKILL.md`
- 对齐与提问收敛清单：`AgentSkill/library/plan-mode-interaction.md`
- 防敷衍门禁（Read/Research 最低计数、占位符清零、Ready-to-Execute Gate）：`AgentSkill/stages/plan/SKILL.md`、`AgentSkill/templates/Plan.template.md`

---

## RQ-004：执行授权口令唯一且不可推断

定义：
- 进入 Execute/Write 的唯一授权口令为用户“单独回复” `开始执行`；不接受同义句、近义句、上下文推断。

落点：
- 全局硬约束：`AgentSkill/SKILL.md`
- Router 补充规则：`AgentSkill/stages/router/SKILL.md`
- Plan 的硬门禁与“请求授权”出口：`AgentSkill/stages/plan/SKILL.md`
- Execution Authorization 落盘字段：`AgentSkill/templates/Plan.template.md`、`AgentSkill/templates/State.template.md`
- 长期记忆与边界：`AgentSkill/State.md`

---

## RQ-005：规划阶段必须“深读 + 检索 + 方案对比 + 架构/选型”

定义：
- 大任务必须先深读用户材料/仓库代码；按需做高质量检索；至少给候选路线与默认推荐；再把结论内化到 Plan/Task。

落点：
- Brainstorm 输出契约（候选+推荐+MVP/MVE）：`AgentSkill/stages/brainstorm/SKILL.md`
- Research 输出契约（来源清单+Brief+证据索引）：`AgentSkill/stages/research/SKILL.md`
- Plan 深读要求/外部检索要求/候选方案与推荐：`AgentSkill/stages/plan/SKILL.md`
- Read Log / Research Log 模板：`AgentSkill/templates/Plan.template.md`

---

## RQ-006：Plan.md 与 Task.md 必须详细、可执行、可验收

定义：
- Plan 负责：验收标准、边界、架构/Spec、验证数据与节奏、风险与依赖。
- Task 负责：把 Plan 拆成可勾选、可执行、可验证的最小单元，并按任务组组织。

落点：
- Plan/Task 最低内容门禁与退出条件：`AgentSkill/stages/plan/SKILL.md`
- Plan 模板（Read Log / Spec / Validation Data / Cadence / Ready-to-Execute Gate）：`AgentSkill/templates/Plan.template.md`
- Task 模板（Task Group + Checkpoint/Milestone/Final 验证项）：`AgentSkill/templates/Task.template.md`
- Router 的就绪判定包含“占位符清零”门禁：`AgentSkill/stages/router/SKILL.md`

---

## RQ-007：执行必须按 Task 推进，且授权后持续推进到完成

定义：
- 执行阶段不得脱离 Task 写代码/写文档/跑命令；授权后按 Task 一次性推进到完成，只有阻塞/风险授权/范围变化才停。

落点：
- Execute 的 Task 绑定与“任务组推进”：`AgentSkill/stages/execute/SKILL.md`
- 项目治理（Execution Session + 多轮继续）：`AgentSkill/library/project-governance.md`
- 迭代与反馈（Resume Protocol）：`AgentSkill/library/iteration-feedback.md`

---

## RQ-008：验证节奏要平衡效率与可验证性（组末检查点 + 里程碑 + 最终）

定义：
- Task 组内允许批量推进；到组末 Validate Checkpoint 再统一验证；里程碑与最终交付再做更宽/全量验证。

落点：
- Plan 定义 Cadence 并映射到 Task：`AgentSkill/stages/plan/SKILL.md`
- Execute 的“任务组→检查点→里程碑→最终”节奏：`AgentSkill/stages/execute/SKILL.md`
- Validate 的 scope=checkpoint/milestone/final：`AgentSkill/stages/validate/SKILL.md`
- Task 模板的 Checkpoint/Milestone/Final 条目：`AgentSkill/templates/Task.template.md`
- Validate 的验证维度（Dimensions）与数据获取尝试：`AgentSkill/stages/validate/SKILL.md`

---

## RQ-009：禁止擅自兜底/降级；兜底只能在 Plan 阶段经确认后落盘

定义：
- 默认禁止兜底/降级逻辑掩盖错误或偷换验收；确需兜底必须在 Plan 写清策略并由用户确认；执行阶段不得擅自新增。

落点：
- 全局硬约束（兜底/降级 + 需求偷换）：`AgentSkill/SKILL.md`
- Plan 的兜底/降级策略门禁：`AgentSkill/stages/plan/SKILL.md`
- Execute 的实现约束：`AgentSkill/stages/execute/SKILL.md`
- Plan 模板 Non-negotiables 与边界段落：`AgentSkill/templates/Plan.template.md`

---

## RQ-010：验证必须优先真实数据；无真实样本需用户确认后才允许 synthetic

定义：
- Level≥L2 默认至少一次关键路径使用 real/sanitized-real；synthetic 只有在用户确认无真实样本（含脱敏样本）且 Plan/State 有记录时才允许。

落点：
- Validate 数据门禁与决策树：`AgentSkill/stages/validate/SKILL.md`
- Review 的硬门禁（synthetic 未经确认 → BLOCKED）：`AgentSkill/stages/review/SKILL.md`
- 验证数据门禁清单：`AgentSkill/library/testing-verification.md`
- Plan 模板 Validation Data 段落：`AgentSkill/templates/Plan.template.md`

---

## RQ-011：验证/评审覆盖面不仅是正确性（含规范/性能/可读性等）

定义：
- Validate/Review 必须把正确性以外的质量属性纳入：规范一致性、性能/资源 smoke check、可读性/可维护性等，作为门禁或评分依据。

落点：
- Validate 的范围定义与输出字段：`AgentSkill/stages/validate/SKILL.md`
- Review 的维度证据与整改清单：`AgentSkill/stages/review/SKILL.md`
- 质量与运维清单：`AgentSkill/library/quality-operations-maintenance.md`

---

## RQ-012：多范式协同（SDD 为骨架，按场景组合工具箱）

定义：
- 不绑定单一开发方式；按 greenfield/legacy/research/ops-debug 选择并组合（规范驱动、行为锁定、探索性原型、契约先行、可观测性排障等）。

落点：
- Execute 的范式工具箱与选择规则：`AgentSkill/stages/execute/SKILL.md`
- 范式选择表：`AgentSkill/library/development-paradigms.md`
- Plan 模板的 Development Strategy：`AgentSkill/templates/Plan.template.md`

---

## RQ-013：替用户跑 Debug / 训练监控 / Ops（Runbook + 证据）

定义：
- 支持 Build/Debug/Ops 三种形态；Ops/长任务需要 Runbook、观察点、阈值、证据落盘。

落点：
- Router 的 WorkType 判定：`AgentSkill/stages/router/SKILL.md`
- Execute 的 WorkType=Ops 建议顺序：`AgentSkill/stages/execute/SKILL.md`
- 运维/监控清单：`AgentSkill/library/quality-operations-maintenance.md`
- Runbook 模板：`AgentSkill/templates/Ops-Runbook.template.md`
- State 模板的治理索引与 Evidence Index：`AgentSkill/templates/State.template.md`

---

## RQ-014：文档/教程交付（无“AI味” + 图示丰富 + 可运行示例 + 引用可追溯）

定义：
- 写作先对齐受众/结构；至少一张总览图；关键结论要来源；示例要可运行；最后进 Validate 与 Review。

落点：
- Write 阶段约束与流程：`AgentSkill/stages/write/SKILL.md`
- 写作清单：`AgentSkill/library/documentation-writing.md`
- 写作验证（引用/示例可运行）：`AgentSkill/stages/validate/SKILL.md`

---

## RQ-015：交付后必须说明“做了什么/怎么验证/证据入口/风险限制”（固定格式）

定义：
- 交付必须输出可复查回执，列关键变更、验证方式、证据入口与限制。

落点：
- Review 阶段强制 Delivery Report：`AgentSkill/stages/review/SKILL.md`
- 回执模板：`AgentSkill/templates/DeliveryReport.template.md`
- Delivery Report 的过程合规段落（授权记录入口 + 关键改动→Task 映射）：`AgentSkill/templates/DeliveryReport.template.md`

---

## RQ-016：进度与记忆必须落盘（State 为单一真相）

定义：
- 长期事实、约束、决策、风险、证据索引与 Next Action 都要写入 State；不要只依赖对话。

落点：
- 全局硬约束：`AgentSkill/SKILL.md`
- State 模板结构：`AgentSkill/templates/State.template.md`
- 长期状态文件：`AgentSkill/State.md`

---

## RQ-017：长任务防漂移 + 违规恢复（Recovery Protocol）

定义：
- 每轮启动先读 State/路由/标注 Mode；发现越权执行/偏离 Plan/跳过真数据门禁等，必须立即停止并回 Plan 修复。

落点：
- Boot + Recovery Protocol：`AgentSkill/SKILL.md`
- Router 的 Step 0 重锚定：`AgentSkill/stages/router/SKILL.md`

---

## RQ-018：上下文压缩/交接摘要后必须可续跑（不停机）

定义：
- 摘要属于维护动作；摘要输出必须携带 Resumption Block；默认摘要后继续推进未完成任务（仍受执行授权门禁约束）。

落点：
- 全局硬约束：`AgentSkill/SKILL.md`
- Resume Protocol：`AgentSkill/library/iteration-feedback.md`
- 治理规则：`AgentSkill/library/project-governance.md`
- Next Action 交接约定：`AgentSkill/templates/State.template.md`
- 决策落盘：`AgentSkill/State.md`

---

## RQ-019：模板与示例仅供参考，规则优先

定义：
- template/example 只展示格式与证据链；实际输出以规则为准，避免示例干扰任务执行。

落点：
- templates 顶部声明：`AgentSkill/templates/*.template.md`
- examples 索引声明：`AgentSkill/examples/_index.md`

---

## RQ-020：目录边界（禁区不可访问 + 输出目录固定）

定义：
- 禁止访问指定禁区目录；所有输出固定到指定输出目录树。

落点：
- 全局边界：`AgentSkill/SKILL.md`
- 长期记忆边界：`AgentSkill/State.md`
