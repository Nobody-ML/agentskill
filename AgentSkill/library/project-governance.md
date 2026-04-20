# Project Governance（大任务治理）检查表

适用：Level = L3，或风险/依赖复杂度触发治理层。

---

## 触发条件（任一即启用 L3 治理）

- 多里程碑、跨模块、外部依赖多
- 验收链条长（需要多轮验证/复现/评审）
- 风险高（安全/合规/不可逆）

---

## A. 里程碑计划（Milestone Plan）

最小要求：
- [ ] 里程碑数量控制在可管理范围（通常 2–6）
- [ ] 每个里程碑都写：产出物 + 验证方式 + 通过标准
- [ ] 里程碑完成必须触发 Review（打分+整改）

来源：
- SWEBOK v4.0a — Chapter 09 *Software Engineering Management*, §2 *Software Project Planning*
- `Reference/Modern Software Engineering/Modern Software Engineering.md` — Ch.4/5（迭代与反馈）

---

## B. 依赖管理（Dependency Map / Matrix）

依赖类型：
- 外部依赖：账号/权限/数据/第三方服务
- 内部依赖：模块、接口、数据结构、工具链

最小要求：
- [ ] 依赖表（每条含 owner/获取方式/阻塞程度）
- [ ] 依赖未满足时：明确阻塞并返回用户，不“硬推”实现

---

## C. 验收契约（Acceptance Contract）

最小要求：
- [ ] 每条契约有 ID（AC-XXX）
- [ ] 每条契约有证据要求（测试/实验/截图/引用）
- [ ] 每条契约至少被一个 Task 引用

来源：
- SWEBOK v4.0a — Chapter 01 §4.3（验收标准驱动规格）

---

## D. 风险矩阵（Risk Matrix）

最小要求：
- [ ] 风险表落盘到 State.md（影响×概率×缓解×证据/监控）
- [ ] 风险变化要即时更新（不是收尾才写）

来源：
- SWEBOK v4.0a — Chapter 09（范围与可行性、需求修订流程）

---

## E. 变更控制（Scope Change）

规则：
- 新需求/范围变化 → 回到 Plan 更新验收契约与 Task，再进入 Execute
- 任何“跳过验证”的决定 → 必须记录在 State.md Decision Log

来源：
- SWEBOK v4.0a — Chapter 09 §1.3 *Process for the Review and Revision of Requirements*

---

## E.1 执行会话与多轮迭代（长任务防失忆）

规则：
- 用户授权 `开始执行` 后形成一次 Execution Session：在该会话内按 Task 一次性推进到完成（允许跨多轮继续，但不改方向、不跳门禁）。
- 每轮必须维护 State.md 的 Next Action（可续跑指针），下一轮先读再续跑。
- 出现“上下文压缩/交接摘要/总结”请求：把它视为治理动作；摘要输出必须包含当前任务组/检查点/Next Action/阻塞点/未完成项入口，并保持会话不中断，摘要后默认继续推进（除非用户明确要求暂停或仅输出摘要）。
- 用户反馈不满意/新想法：结束当前会话（或标记为 interrupted），回到 Plan 更新验收与 Task，再重新走授权门禁。

---

## F. 复现协议（Repro Protocol）

规则：
- Research：强制
- Software/Writing：当含代码/命令/指标对比时强制

落盘：State.md Evidence Index + templates/ 复现协议。
