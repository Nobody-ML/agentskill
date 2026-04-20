# AgentSkill v0.3.0 — 任务清单（最小执行单元）

目录：`droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/`

任务状态：
- `[ ]` 待执行
- `[x]` 已完成
- `[~]` 进行中
- `[!]` 阻塞/需要用户输入

---

## 0. 版本准备

- [x] 0.1 生成 `v0.3.0/Plan.md`
- [x] 0.2 生成 `v0.3.0/Task.md`

---

## 1. Plan Mode / Execution Mode（双相门禁）

- [x] 1.1 在主 `SKILL.md` 增加“双相系统”段落：Plan Mode → Execution Mode
- [x] 1.2 在主 `SKILL.md` 主流程图中加入 **Execution Authorization Gate**（用户明确授权才可 Execute）
- [x] 1.3 更新 `stages/router/SKILL.md`：
  - 路由输出加入：`ExecutionAuth = required/received`
  - 建议默认：L2/L3 = required（Plan Mode）
- [x] 1.4 更新 `stages/plan/SKILL.md`：
  - 写清 Plan Mode 的允许动作（读材料/检索/落盘工件）
  - 写清“提问收敛规则”（少而关键、每轮推动 Plan 收敛）
  - 写清执行授权记录如何落盘（State/Plan）
- [x] 1.5 更新 `stages/execute/SKILL.md`：
  - 增加门禁：未授权不得执行（L2/L3）
  - 增加规则：授权后按 Task 一次性推进到完成（除非阻塞或用户中断）

验收：大任务在用户未授权前，流程停留在 Plan Mode；授权后进入 Execution Mode 且任务持续推进至完成。

---

## 2. 多范式协同（SDD + 工具箱组合）

- [x] 2.1 更新 `library/`：新增 `library/development-paradigms.md`
  - 工具箱：SDD（Spec-Driven）/ Characterization / BDD（验收断言）/ Spike / Contract-first / Observability-driven debugging
  - 选择表：按 greenfield / legacy / research / ops debug
- [x] 2.2 更新 `stages/execute/SKILL.md`：
  - 从“单一默认路径”改为“优先规范驱动 + 按场景选范式组合”
  - 对遗留系统强调：先 characterization tests 锁行为再改
- [x] 2.3 更新 `templates/Plan.template.md`：
  - 增加 “Development Strategy（范式组合）”段落（L2 建议，L3 强制）

验收：Execute 能明确说明“这次为什么用哪种范式”，并能写入 Plan/Review。

---

## 3. 验证升级：真实数据优先 + 全维度质量验证

- [x] 3.1 更新 `stages/validate/SKILL.md`：
  - 加入“真实数据优先”硬门禁与决策树
  - 证据需标注数据类型：real / sanitized-real / synthetic
  - 增加验证覆盖面：正确性/规范/性能/可读性（作为 Review 输入）
- [x] 3.2 更新 `library/testing-verification.md`：
  - 加入真实数据优先规则与数据类型标注
  - 明确“只有用户确认没有真实样本才允许 synthetic”
- [x] 3.3 更新 `templates/Plan.template.md`：
  - 增加 “Validation Data（验证数据声明）”段落（数据来源与类型）

验收：Validate 输出里能看到“用的是什么数据（real/sanitized-real/synthetic）+ 证据入口”。

---

## 4. Ops / Debug / Monitoring（替用户跑与盯）

- [x] 4.1 在 Router/State/Plan 引入 `WorkType = Build | Debug | Ops`（不新增 Track）
- [x] 4.2 新增模板：`templates/Ops-Runbook.template.md`
- [x] 4.3 更新 `library/quality-operations-maintenance.md`：
  - 加入监控/排障闭环（观察点、阈值、告警、回滚）
- [x] 4.4 更新 `stages/plan/SKILL.md` 与 `stages/execute/SKILL.md`：
  - 触发条件：debug/训练监控/长任务运行
  - 输出要求：Runbook + 观察点 + 证据落盘

验收：Ops 类任务能产出 Runbook，并把日志/监控证据写入 State Evidence Index。

---

## 5. 交付报告（固定格式）+ 文档配套

- [x] 5.1 新增模板：`templates/DeliveryReport.template.md`
- [x] 5.2 更新 `stages/review/SKILL.md`：
  - 交付时必须输出 Delivery Report（做了什么/改了哪些/如何验证/证据入口/风险限制）
  - 强化返工规则：验证失败必须回溯返工并复评
- [x] 5.3 更新 `templates/Task.template.md`：
  - 增加“文档配套任务”（变更说明/运行说明/验证说明）

验收：交付回执稳定可复查，且配套文档成为默认交付物之一。

---

## 6. 路径修正 + 禁止发散表达审计

- [x] 6.1 全仓（仅本 AgentSkill 范围）扫描并修正路径：
  - 不再出现旧输出路径引用（与当前输出目录不一致的路径）
- [x] 6.2 扫描并修正表达：
  - 删除/改写发散式多选句式（强制收敛为确认式提问）
- [x] 6.3 更新 `State.md`：
  - 落盘 v0.3.0 关键决策（Execution Authorization、真实数据、WorkType）
  - 修正 Evidence Index 中的路径引用

验收：文档一致、路径一致、表达不发散。

---

## 7. 上下文压缩/交接摘要续跑协议（长任务不停机）

- [x] 7.1 更新主 `SKILL.md`：
  - 加入“上下文压缩/交接摘要不是停机信号”
  - 定义 Resumption Block（任务组/检查点/Next Action/阻塞点/未完成项入口）
  - 默认摘要后继续推进未完成任务（遵守执行授权门禁）
- [x] 7.2 更新 `library/iteration-feedback.md`：
  - 在 Resume Protocol 增加“摘要不是结束”的检查项
- [x] 7.3 更新 `library/project-governance.md`：
  - 在执行会话治理中加入“摘要不中断会话”的规则
- [x] 7.4 更新 `templates/State.template.md`：
  - 在 Next Action 段落补充“Resumption Block 由此生成”的交接约定
- [x] 7.5 更新 `State.md`：
  - 落盘 DEC-008（长任务防漂移 + 上下文压缩续跑）
  - 补齐禁区边界（含 `droid_gpt-5.2-xhigh/AgentSkill/**`）

验收：出现“交接摘要/压缩总结”请求时，摘要输出不视为结束；Resumption Block 可从 State.md 的 Next Action 直接生成，并能无缝续跑未完成任务。
