# Task：<任务/项目名称>

> 注意：本模板仅提供参考结构，不是执行规范；实际输出必须遵循本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md`。模板与规则冲突时，以规则为准。

目录：`<建议放置目录>`

任务状态：
- `[ ]` 待执行
- `[x]` 已完成
- `[~]` 进行中
- `[!]` 阻塞/需要用户输入

拆分原则：
- 一条任务 = 一个最小可执行动作（能在一次迭代内完成并验收）
- 每条任务必须写清：**产出物** 与 **验收方式**
- 有依赖就写依赖；不确定就先拆“澄清/调查”任务
- 兜底/降级不得在 Execute 阶段临时决定；需要兜底/降级必须在 Plan 中写清并经用户确认，再落到 Task

验证节奏（Cadence）：
- Task.md 必须按“大标题/任务组（Task Group）”组织（一个组里可以有多个小任务）
- **每个任务组末尾必须有一个 `Validate Checkpoint`**（scope=checkpoint）
- 每个里程碑末尾必须有一个 `Milestone Validate`（scope=milestone）
- 全部任务完成后必须有 `Final Validate`（scope=final）与总评审/交付回执

勾选规则（避免“没证据就勾完”）：
- 小任务实现中用 `[~]`
- 到达该组的 Validate Checkpoint 并验证通过后，再把本组相关任务统一改为 `[x]`
- 任务组内允许随手做“微检查”（快、便宜、用来提前暴雷），但不把它当作正式 Validate

---

## 1. 路由与上下文

- [ ] 1.1 记录 Track/Level 判定（写入 State.md）
- [ ] 1.1.1 （Software）记录 WorkType=Build/Debug/Ops（写入 State.md）
- [ ] 1.1.2 记录 Execution Authorization=required/received/not_required（写入 Plan/State）
- [ ] 1.2 列出输入材料清单（文件/链接/数据）
- [ ] 1.3 明确验收标准（至少 2 条）

---

## 2. 调研/阅读（按需）

- [ ] 2.1 阅读：`path/to/file`（目标：提炼约束/接口/现状）
- [ ] 2.2 搜索外部资料（如允许）：记录来源与关键结论到 State.md

---

## 3. 规划（L2/L3 必选）

- [ ] 3.1 产出/更新 Plan.md（使用 `templates/Plan.template.md`）
- [ ] 3.2 细化本 Task.md（拆到最小可执行单元）

### 3.3 执行授权门禁（L2/L3 强制）

- [ ] 3.3.1 Plan Mode 对齐完成（验收/边界/验证方案已明确）
- [ ] 3.3.2 为避免误判：等待用户**单独回复**授权口令 `开始执行`（建议独立消息或独立一行），并把 time+scope 落盘到 Plan/State

### 3.4 验收契约挂接（L3 强制）

- [ ] 3.4.1 生成/更新验收契约（`templates/AcceptanceContract.template.md`）
- [ ] 3.4.2 确认每条 AC-XXX 都至少被一个 Task 覆盖（任务负责让它“可验收”）

---

## 4. 实施（按任务组拆分：组内执行，组末检查点验证）

### 4.A Task Group（Software）：<组名/组件/功能>
- 目标：
- In-scope：
- Out-of-scope：
- 依赖/前置（数据/权限/环境）：
- 产出物（文件/接口/命令）：
- 关键风险（失败模式/回滚策略）：
- 检查点通过标准（本组什么算通过）：

- [ ] 4.A.1 修改/新增：`path/to/file`
  - 产出：可运行代码
  - 验收：最小测试/手动路径
  - 关联验收契约：AC-XXX（如适用）
  - 证据入口：写入 State.md Evidence Index

- [ ] 4.A.9 Validate Checkpoint（scope=checkpoint）
  - data_type：real / sanitized-real / synthetic
  - 覆盖面：本组改动的关键路径/失败模式/边界
  - 覆盖维度（Dimensions）：Correctness / Spec / Failure / Performance / Docs / ...
  - 通过标准：失败判据是什么（失败即回滚/返工）
  - 命令/步骤：写清可复现入口（command/action + 预期输出摘要）
  - 证据入口：写入 State.md Evidence Index

### 4.B Task Group（Research）：<组名/问题/实验>
- 目标：
- 研究假设/要验证的点：
- 指标与基线：
- 依赖/前置（数据/算力/权限）：
- 产出物（脚本/表格/图/记录）：
- 检查点通过标准（失败判据）：

- [ ] 4.B.1 定义指标/基线（产出：对比表；验收：可复述可复现）
- [ ] 4.B.2 跑最小实验（产出：结果 + 参数；验收：可重复运行）
  - 关联验收契约：AC-XXX（如适用）
  - 证据入口：写入 State.md Evidence Index

（论文/综述可选）
- [ ] 4.B.3 维护相关工作矩阵（Literature Review Matrix）
  - 使用模板：`templates/Literature-Review-Matrix.template.md`
  - 验收：结论能映射到来源条目（写入 State.md Evidence Index）

- [ ] 4.B.9 Validate Checkpoint（scope=checkpoint）
  - data_type：real / sanitized-real / synthetic
  - 覆盖面：本组假设/指标计算/基线对照的最小证据
  - 覆盖维度（Dimensions）：Correctness / Failure / Performance（如适用）/ Repro / ...
  - 通过标准：失败判据是什么（失败即回到 Plan/Execute 调整）
  - 命令/步骤：一键复现入口（脚本/参数/seed/环境）
  - 证据入口：写入 State.md Evidence Index

### 4.C Task Group（Writing）：<组名/章节/交付物>
- 目标读者与预期用途：
- 范围边界（不写什么）：
- 产出物（文件/格式/图示清单）：
- 检查点通过标准（什么算“可交付”）：

- [ ] 4.C.1 写大纲（产出：章节结构；验收：覆盖验收标准）
- [ ] 4.C.2 补图示（产出：Mermaid/表格；验收：能解释关键关系）
  - 关联验收契约：AC-XXX（如适用）
  - 证据入口：写入 State.md Evidence Index

（论文/技术报告可选）
- [ ] 4.C.3 写 Paper Outline（先结构后填充）
  - 使用模板：`templates/Paper-Outline.template.md`
  - 验收：结构覆盖目标读者路径 + 实验/复现章节齐全（如适用）

- [ ] 4.C.9 Validate Checkpoint（scope=checkpoint）
  - data_type：real / sanitized-real / synthetic（写作通常对应来源与示例）
  - 覆盖面：引用可追溯/示例可运行/术语一致/图示可读
  - 覆盖维度（Dimensions）：Sources / Examples / Consistency / Visual / ...
  - 通过标准：引用/示例/术语一致性均可复查
  - 命令/步骤：示例运行方式（如有）+ 输出摘要
  - 证据入口：写入 State.md Evidence Index

---

## 5. 验证（里程碑验证 + 总验证，必须绑定证据）

- [ ] 5.1 Milestone Validate（scope=milestone）
  - data_type：real / sanitized-real / synthetic
  - 覆盖面：更宽回归 + 性能/资源 smoke check + 规范/文档一致性
  - 覆盖维度（Dimensions）：Correctness + Failure + Performance/Resource + Docs/Operability（按需补 Spec/Security）
  - 证据入口：写入 State.md Evidence Index

- [ ] 5.2 Final Validate（scope=final）
  - data_type：real / sanitized-real / synthetic
  - 覆盖面：对照验收标准/验收契约逐条覆盖（尤其 L3）
  - 覆盖维度（Dimensions）：里程碑维度 + Spec/Consistency +（按风险）Security/Compliance +（Writing/UI）Visual/UX
  - 证据入口：写入 State.md Evidence Index

### 5.3 复现协议（按 Track）

- [ ] 5.3.1 Research：补齐 `templates/ReproProtocol-Research.template.md`
- [ ] 5.3.2 Software：补齐 `templates/ReproProtocol-Software.template.md`
- [ ] 5.3.3 Writing：补齐 `templates/ReproProtocol-Writing.template.md`

---

## 6. 评审与交付

- [ ] 6.1 按评分模板输出评分与整改清单
- [ ] 6.2 若总分 < 7.0/10：结论置为 NEEDS_USER_DECISION，给出“默认建议返工复评”的推荐路径，并把用户最终决定写入 State.md Decision Log
- [ ] 6.3 生成 Delivery Report（使用 `templates/DeliveryReport.template.md`）
- [ ] 6.4 （WorkType=Ops）补齐 Ops Runbook（使用 `templates/Ops-Runbook.template.md`）
- [ ] 6.5 交付物清单 + 影响范围说明
