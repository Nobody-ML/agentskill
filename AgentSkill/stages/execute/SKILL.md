---
name: execute
description: 按 Task 推进实施：按任务组小批量推进，组末检查点验证，并更新证据与状态
---

# Execute（实施）

## 进入条件

- Simple/L1：Router 判定可直接执行
- L2/L3：已具备 Plan/Task，且用户已明确授权执行（Execution Authorization = received；为避免误判，用户需单独回复口令：`开始执行`）

---

## Stage Contract（阶段契约）

### 输入（Inputs）
- `Task.md`（L2/L3 必须）
- `Plan.md`（验收/验证/依赖/风险）
- （L3）Acceptance Contract（AC-XXX）
- Execution Authorization（必须已 received）
- `State.md`（边界、Decision Log、Evidence Index 入口）

### 输出（Outputs）
- Task 勾选状态更新（[x]/[!]/[~]）
- 工件产出（代码/文档/脚本/实验结果）
- 最小验证结果与证据入口

### 工件更新（Artifacts Updated）
- `Task.md`：更新状态
- `State.md`：Progress/Risks/Evidence Index

### 退出条件（Exit Criteria）
- 本轮最小任务完成并能给出证据入口；或明确阻塞并返回用户

### 返工条件（Rework）
- Validate 失败 → 回到 Execute 修复（再 Validate）

---

## library 索引（按触发条件查）

- 迭代与反馈（短回路）：`library/iteration-feedback.md`
- 复杂度/模块化（避免浅封装与泄漏）：`library/complexity-modularity.md`
- 设计与构建（设计原则/构建实践）：`library/design-construction.md`
- 开发范式协同（SDD/Characterization/Spike/BDD...）：`library/development-paradigms.md`
- 质量/运维/维护（长期可用性）：`library/quality-operations-maintenance.md`
- 测试与证据门禁：`library/testing-verification.md`
- 复现协议：`library/reproducibility.md`

---

## 输出（每轮迭代必须有）

（L2/L3 强制）每轮对外回复开头必须带：

```text
【Mode】Execute | Level=<L?> | ExecutionAuth=received
```

- 本轮推进了哪个任务组（Task Group，大标题）
- 执行前预检摘要（Plan/Task/State 指针 + 本轮 Task Group/检查点 + data_type 计划）
- 勾选了哪些小任务（或标记为进行中）
- 产生了哪些工件（代码/文档/脚本/实验结果）
- 到达验证检查点时做了哪些验证（并写入 Evidence Index）
- State.md：更新 Progress / Risks / Evidence

---

## 执行原则（强约束）

0) **执行授权门禁（L2/L3）**：
   - Execution Authorization 未 received → 不进入执行；回到 Plan（等待用户回复 `开始执行` 并落盘授权记录）。

0.1) **执行前预检（Pre-flight，先过门禁再动手）**：
   - 目的：避免“还没授权就写代码/脱离 Plan/Task 推进/跑几轮忘记 skill”的事故。
   - 在做任何改动/运行命令前，必须同时满足：
     - `Plan.md` 与 `Task.md` 已存在且属于当前迭代（版本/Iteration ID 对齐）
     - `State.md` 中 `Execution Authorization=received` 已落盘（含 time+scope）
     - 本轮要推进的 Task Group 已明确，且下一步检查点是哪个（checkpoint/milestone/final）
     - 关键改动点能映射到 Task 的具体条目（任务 ID）
     - 验证数据入口已明确（real/sanitized-real 优先；synthetic 需满足门禁）
   - 任一不满足：停止推进并回到 Plan 补齐（不要在 Execute 里边写边补规范）。

1) **一次只推进一个任务组（Task Group）**：
   - Task.md 必须按“大标题/任务组”组织（例如按组件/里程碑/论文章节）。
   - 在同一任务组内允许连续完成多个小任务；到达该组的 **Validate Checkpoint** 时再统一验证。
   - 不允许在多个任务组之间来回跳（除非为了修复验证失败）。
1.1) **Task 绑定（不允许“脱离 Task 写代码”）**：
   - 每一次改动必须能指向 Task.md 里的某一条小任务（否则先回到 Plan 更新 Plan/Task，再继续）。
   - 发现 Plan/Task 不足以约束实现时：先补 Plan/Task（写清验收/边界/验证/风险），不要在代码里“边写边猜”。
2) **先读再改**：涉及已有材料/代码时，先定位并阅读相关部分，写入“读过的清单”。
3) **避免兜底与无意义拆分**（Software）：
   - 默认禁止引入兜底/降级逻辑来掩盖错误或偷换验收。
   - 需要兜底/降级时：只能按 Plan 中已落盘且用户已确认的策略实现（触发条件/成本/对验收影响/验证方式）；执行阶段不得擅自新增。
   - 小函数拆分必须带来可读性/复用性/测试性收益，否则不要拆。
4) **证据驱动**：任何“完成/通过/正确/可复现”的结论都要绑定证据入口（命令、截图、实验记录、引用）。
5) **遇阻塞就停**：缺权限/缺数据/边界不清/风险项 → 返回用户确认。

（Software 的 SWE 强化）
6) **按场景选择开发范式（组合使用）**：
   - **SDD（Spec-Driven）优先**：先把需求写成可执行规范（Plan/验收断言/示例/错误语义/数据约束），再实现。
   - 新增/新逻辑：先写可失败的自动化检查/断言（单测/属性/契约）→ 最小实现 → 重构
   - 遗留系统/不敢改：先 characterization / regression 把现有行为锁住，再改实现
   - 高不确定任务（科研/新库接入）：先 spike/prototype（可丢弃）证伪关键假设，再工程化
   - 需求以用户行为为中心：验收断言先行（BDD / Given-When-Then）
   - Debug/Ops：先补可观测性（logs/metrics/artifacts）再定位（避免盲改）

7) **一次性推进到完成（Execution Mode）**：
   - 授权后，按 Task.md 从上到下持续推进：
     - 任务组内：Execute →（到检查点）Validate Checkpoint
     - 里程碑级：Milestone Validate（更宽的回归/性能/规范）
     - 全局：Final Validate → Review → Delivery Report
   - 不在执行过程中反复要求用户做选择；需要决策时给出推荐默认值并请求确认。

8) **验证节奏上限（避免“堆一坨再测”）**：
   - 同一任务组内允许批量执行，但不得在以下情况下继续堆未验证改动：
     - 关键路径/高风险模块被改动（安全/数据一致性/并发/部署）
     - 已经连续变更超过 60–90 分钟仍未到达检查点
     - 本地 smoke check 已出现不稳定信号（报错/性能异常/日志异常）

---

## 通用步骤（每轮循环）

### Step 0：重锚定（本轮只做已约定的事）

- 打开并刷新：`Plan.md`（验收/边界/验证/兜底策略）与 `Task.md`（本轮要推进的任务组到检查点）。
- 复读并锁定：Plan.md 的“用户意图锁定/Non-goals/Non-negotiables”（执行阶段不得改方向、不得偷换验收）。
- 把本轮要做的任务组与检查点范围写清；任何超出范围的想法先记入 Decision Log/Risks，回 Plan 再决策。

### Step 1：选一个任务组（到下一个 Validate Checkpoint 为止）

- 选择 Task.md 中最靠前的未完成任务组（一个大标题）。
- 明确该组的退出条件：到达该组的 `Validate Checkpoint`。
- 如果没有 Task（Simple/L1）：把动作写成 1–3 条临时任务，并在完成后补回 State.md。

### Step 2：在任务组内执行（小批量）

- 按小任务逐条推进，但不跨任务组跳转。
- 改动面保持可控：避免一次性铺开大量文件与抽象层级。

### Step 3：微检查（快、便宜、随手做）

> 微检查不是“正式 Validate”，它的作用是避免把错误带到检查点后才爆炸。

- Software：能快速跑就快速跑（lint/typecheck/单测子集/最小运行）
- Research：sanity check / 指标可计算性确认
- Writing：章节结构一致性、引用占位、图示可读性自检

### Step 4：到达检查点 → 进入 Validate

- 执行到任务组的 `Validate Checkpoint` 时，必须进入 `stages/validate/SKILL.md`：
  - 使用真实/脱敏真实数据优先
  - 记录 data_type 与证据入口
  - 验证失败则回到本任务组内返工

### Step 5：落盘

- Task：组内小任务可先标记为 `[~]`；检查点验证通过后再统一改为 `[x]`
- State：更新 Progress（完成了什么/下一步是什么）
- Evidence Index：记录本轮验证证据入口
- 若本轮因时间/资源中断而未完成到检查点：必须在 `State.md` 的 Next Action 写清“当前任务组 + 下一步 1–3 个动作 + 阻塞点”，并在下一轮继续同一任务组（不跳组）
- 若已完成 Final Validate + Review 并交付：将 State 元信息中的 `Execution Session` 标记为 `completed`（并记录结束时间/交付入口）

---

## 按 Track 的执行补充

### Software
- 优先写最小可验证实现（避免“先搭大框架再补细节”）。
- 对于复杂改动：先用测试/脚手架把边界钉住，再实现。

#### WorkType=Build（开发建设）建议顺序（能做就做）
1) 写失败测试（或最小可观测验证）
2) 写最小实现
3) 运行验证并记录证据
4) 再做下一条 Task

#### WorkType=Debug（诊断修复）建议顺序
1) 复现问题（最小输入/最小场景），记录证据入口（日志/命令/截图）
2) 加 characterization / regression test（把 bug 固定成“会失败的证据”）
3) 修复（改动面尽量小，避免“顺手重构”引入二次风险）
4) Validate：跑测试 + 关键路径回归 +（必要时）性能/资源 smoke check
5) 落盘：原因、修复点、证据、影响面（写入 Delivery Report/State）

#### WorkType=Ops（运行维护/监控）建议顺序
1) 先写 Runbook（启动/停止/健康检查/常见失败模式）（建议用 `templates/Ops-Runbook.template.md`）
2) 明确观察点（logs/metrics/关键产物文件）与阈值（异常判据）
3) 执行/监控：按阈值判断是否介入（例如：loss 不下降、OOM、吞吐退化）
4) Validate：把“看到了什么”写成可复查证据（State Evidence Index）

### Research
- 先做最小可行实验（MVE），尽早发现假设不成立。
- 实验记录必须包含：环境、seed、数据版本、参数、指标、结果。

### Writing
- 先搭结构，再逐段填充；不要一上来写长段落。
- 图示优先服务“理解关键关系/流程”，不是装饰。
