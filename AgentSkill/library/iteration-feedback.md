# Iteration & Feedback（迭代与反馈回路）检查表

适用：Research / Software / Writing（任何需要多步推进的任务）。

---

## 触发条件

- 任务不确定性高（方向/方案/影响范围不清）
- 容易“先做一大坨，最后一起验证”的倾向
- 需要在早期暴露风险

---

## A. 迭代不是形式，是防御性设计

检查项：
- [ ] 把工作拆成短回路：每回路都有产出与验证
- [ ] 避免“先把大计划写完再做”（计划只能服务于下一步验证）

来源：
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Part II, Ch.4 *Working Iteratively*（Iteration as a defensive design strategy / The lure of the plan）

---

## B. 反馈回路越短越好（Prefer early feedback）

反馈层级（从快到慢）：
1) 静态检查/局部单测/最小实验
2) 集成验证/端到端路径
3) 用户测试/论文评审/生产观察

检查项：
- [ ] 先跑最短反馈回路，把方向钉住
- [ ] 每个里程碑边界都要有验证（不是到最后）

来源：
- Farley — Ch.5 *Feedback*（Feedback in coding/integration/design/architecture；Prefer early feedback）

---

## C. 增量主义（Incrementalism）

检查项：
- [ ] 每次改动尽量小（减少回滚成本）
- [ ] 把变化影响限制在模块边界内
- [ ] 把“大重构”拆成可验证的小步（保持系统可运行）

来源：
- Farley — Ch.6 *Incrementalism*（Tools of incrementalism / Limiting the impact of change）

---

## D. 经验主义（Empiricism）：用数据而不是自信

检查项：
- [ ] 重要结论必须有证据（命令输出/实验结果/引用）
- [ ] 避免自我欺骗：在 Plan 里写失败判据

来源：
- Farley — Ch.7 *Empiricism*（Avoiding self-deception）
- `superpowers/skills/verification-before-completion/SKILL.md`（Evidence before claims）

---

## E. 最小可行验证（MVP/MVE）

Research：先做最小可行实验（MVE）验证假设。  
Software：先做 walking skeleton 验证架构路径。  
Writing：先写目录 + 总览图 + 关键示例，验证读者路径。

来源：
- Farley — Ch.4/5（迭代与反馈）

---

## F. 可续跑协议（Resume Protocol，长任务必用）

> 目的：解决“跑几轮就失忆/忘规则/忘计划”的常见崩溃模式，让任务能跨多轮稳定推进。

检查项：
- [ ] 每轮结束都更新 `State.md` 的 Next Action（当前任务组 + 下一步 1–3 个动作 + 阻塞点）
- [ ] 每轮开始先读 State/Plan/Task，再继续同一任务组（不跳组、不改方向）
- [ ] 授权后形成一个执行会话（Execution Session）：直到 Final Validate + Review + Delivery 完成才结束
- [ ] 出现“上下文压缩/交接摘要/总结”请求时：摘要不等于结束；摘要输出必须包含 Resumption Block（当前任务组/检查点/Next Action/阻塞点/未完成项入口），并默认继续推进未完成任务（除非用户明确要求暂停或仅输出摘要）
- [ ] 用户反馈不满意/新想法 → 回到 Plan 更新验收与 Task，再重新走授权门禁（不要在 Execute 里硬改）
