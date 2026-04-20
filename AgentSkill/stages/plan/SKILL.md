---
name: plan
description: 把复杂任务写成可执行 Plan/Task：明确验收、里程碑、验证、风险，并把任务拆到可勾选的最小单元
---

# Plan（计划与任务拆分）

## 进入条件

满足任一：
- Level ≥ L2
- 需要多步骤推进、跨文件/跨模块/跨资料
- 需要复现与验证闭环（测试/实验/引用）

---

## Stage Contract（阶段契约）

### 输入（Inputs）
- Router 的路由结果（Track/Level/风险）
- Research/Brainstorm 的输出（如有）
- 现有工件：`State.md`（偏好/边界/证据索引入口）

### 输出（Outputs）
- `Plan.md`（验收/里程碑/验证/风险/依赖）
- `Task.md`（最小执行单元 + 验收方式 + 依赖 + 证据入口）
- （L3）验收契约：Acceptance Contract（AC-XXX）
- 执行授权记录（Execution Authorization）：required / received / not_required（默认 L2/L3=required）
- 验证节奏（Cadence）：checkpoint / milestone / final（写入 Plan，并映射到 Task 的检查点任务）

### 工件更新（Artifacts Updated）
- `State.md`：Track/WorkType/Level、Execution Authorization、Decision Log、Progress、Risks、Evidence Index 入口

### 退出条件（Exit Criteria）
- L2：Plan/Task 已落盘且可执行（进入“等待执行授权”门禁）
- L3：额外满足“验收契约已落盘，且 Task 已挂接 AC-XXX”

### 返回用户条件（Return to User）
- 验收标准无法确定
- 外部依赖未明确（账号/权限/数据）
- 风险项需要授权

---

## 输出（必须产出）

（L2/L3 强制）每轮对外回复开头必须带：

```text
【Mode】Plan | Level=<L?> | ExecutionAuth=<required/received/not_required>
```

1) `Plan.md`（使用 `templates/Plan.template.md`）
2) `Task.md`（使用 `templates/Task.template.md`，带方框）
3) 更新 `State.md`：写入 Track/Level、关键约束、Decision Log、Progress、Evidence 入口

（L2/L3 的 Plan 最低内容门禁）
- 必须包含 Read Log（读过什么、提炼了什么约束/坑点）
- 必须包含（按需）Research Log（外部来源/基线/结论如何影响方案）
- 必须包含候选方案与推荐（至少 2 个候选 + 1 个默认推荐）
- 必须包含可执行规范（Spec：接口/错误语义/示例/不变量）
- 必须包含验证数据与节奏映射（real/sanitized-real 优先；checkpoint/milestone/final）
- 必须包含“用户意图锁定”（Goal/Non-goals/Non-negotiables + 已确认决策快照），并同步到 State.md（防止执行阶段跑偏）

（防敷衍的最低计数门槛，除非明确标注 N/A 与原因）
- L2：Read Log ≥ 5 条；Research Log ≥ 5 条（当存在选型/用库/对标/“最新”需求时强制）
- L3：Read Log ≥ 10 条；Research Log ≥ 8 条（至少包含 2 条官方文档/标准/论文；来源需可追溯）

---

## 硬门禁

- L2/L3：**没有 Plan/Task 不进入 Execute**。
- L2/L3：**没有执行授权（`开始执行`）不进入 Execute/Write**。（默认停留在 Plan Mode）
- Plan 必须包含：验收标准 + 验证方案（否则无法判断完成）。
- **兜底/降级策略门禁**：Plan 中未明确且用户未确认的兜底/降级，一律不得在 Execute 阶段引入；需要兜底/降级属于需求/验收变更，必须回 Plan 落盘并写入 Decision Log。

（L3 门禁）
- **没有验收契约（Acceptance Contract）不进入 Execute**。
- 验收契约必须可追踪（AC-XXX），并能映射到 Task。

---

## 工作步骤

### Plan Mode 交互协议（强约束）

Plan 阶段默认处于 Plan Mode：目标是把需求与方法对齐到“可执行、可验收、可验证”的状态。

规则：
1) **先读材料再提问**：能从材料推断的，不反问。
2) **问题少而关键**：每轮最多 3–6 个；每个问题都必须“会改变方案/验收/边界”。
3) **给推荐默认值**：不让用户在分叉里迷路；需要确认时，用“确认/不确认”的问法收敛。
4) **不进入执行**：用户未明确回复 `开始执行` 前，不修改目标代码/不进入长任务运行。
5) **仅允许写规划工件**：Plan Mode 只允许改动 `Plan.md`/`Task.md`/`State.md` 与治理模板；不得修改任何交付物（代码/脚本/配置/文档/实验产物）。

当需要更详细的提问与收敛规则：查 `library/plan-mode-interaction.md`。

### Step 1：归档输入材料

- 列出“读过的材料清单”（文件路径/链接/数据）。
- 把关键约束写进 Plan 的“约束与边界”，同步到 State.md。
- 默认禁止兜底/降级；确需兜底/降级时，必须在 Plan 中列出清单（触发条件→行为→成本/副作用→对验收影响→验证方式），写入 Decision Log，并在执行授权前与用户确认。

深读要求（不要敷衍）：
- 对用户提供的材料：至少提炼出“约束/验收/接口/数据/失败判据”这五类信息。
- 对仓库代码：至少定位并读到“关键入口 + 关键数据流 + 关键失败路径”，并把读到的事实写进 Plan 的 Read Log。

深读覆盖面建议（Software，L2/L3 默认执行）：
- 入口：主入口/CLI/服务启动点/核心 API
- 数据：关键数据结构/序列化格式/数据库模型（如有）
- 配置：环境变量/配置文件/启动参数
- 失败路径：错误处理、边界条件、异常信息、回滚路径
- 性能路径：热路径、资源瓶颈、并发/IO（如适用）
- 验证：现有测试/样例输入/fixture（如有）

（按需）外部检索要求：
- 需要选型/用库/对标/实验基线时：必须做高质量检索，并把结论写入 Plan 的 Research Log（来源可追溯 + 对方案的影响）。

检索最小质量门槛（避免“搜了但没用”）：
- 每条来源必须写清：可信度理由 + 与任务的关联点 + 对方案的影响（决策/约束/验证）
- 出现“最新/主流/最佳实践/官方推荐”字样时：必须以官方/标准/同行评审材料为主，且写入来源年份/版本

### Step 2：写验收标准（先于方案细节）

规则：
- 至少 2 条
- 必须可观察/可测试/可复现
- 避免“更好/更快/更优”这类不可验收描述

（SWE 门禁）如果验收标准写不出来：优先回到 Brainstorm 补齐需求与取舍，而不是硬写实现细节。

### Step 2.2：候选方案与推荐（内置 Brainstorm）

> 目的：即使用户给了“看起来明确”的想法，也要做一次工程化 sanity check：给出更稳的技术链路与取舍。

硬要求：
- 至少 2 个候选路线（A/B）
- 必须给 1 个默认推荐（含取舍理由）
- 方案必须能落盘到 Plan（并能映射到 Task 的里程碑与检查点验证）

（建议强制）技术链路图（Architecture/Tech Chain）：
- 至少 1 张图（Mermaid/PlantUML/ASCII 均可），把“从输入材料/数据 → 核心处理 → 产出物/证据”画出来
- 目的：让后续执行可对照，不走偏、不丢验证入口

### Step 2.1：需求完整性评分（建议）

- 用 Router 的“需求完整性快评”口径评分（0–10）。
- < 7 分：在 Plan 中列出缺口问题，并返回用户/Brainstorm 补齐。

### Step 3：写方案概览（不求长，求可执行）

至少包含：
- 推荐路线
- 关键假设
- 关键决策点（写入 State 的 Decision Log）

（L3 建议强制）补充两个“架构层输入”：
- Stakeholders & Concerns：谁关心什么（至少 3 类 stakeholder）
- 质量属性 Top 3–7：排序并写清 trade-offs

落盘建议（对应模板）：
- `templates/Stakeholders-Concerns.template.md`
- `templates/Quality-Attributes.template.md`

（重大决策）可选使用 `templates/ADR.template.md`，或写入 State.md 的 Decision Log。

### Step 4：拆里程碑

- L2：可拆 1–3 个里程碑
- L3：必须拆里程碑；每个里程碑都要写“产出物 + 验证方式”

（SWE 建议）里程碑的第一优先级是“缩短反馈回路”，不是“按模块列清单”。

### Step 4.1：架构描述（L3 建议强制）

- 至少提供：组件边界 + 依赖方向 + 关键交互路径
- 图示优先：Mermaid（组件/流程）或 PlantUML（时序/类图）
- 目的：让架构决策可复查、可讨论

### Step 5：写验证方案（绑定证据）

- Software：测试/静态检查/手动路径（WorkType=Ops 时额外包含：健康检查/观测点/阈值/Runbook）
- Research：最小实验、基线、指标、消融、复现要素
- Writing：引用与来源、示例可运行、图示清单

### Step 5.0：定义验证节奏（Cadence）（建议强制）

> 目标：在保证可验证性的前提下，避免“每个微任务都跑一遍大测试”。

要求：
- 为每个 **任务组（Task Group）** 定义一个 `Validate Checkpoint`（快速回归）
- 为每个 **里程碑（Milestone）** 定义一个 `Milestone Validate`（更宽回归 + 性能/规范/文档）
- 最终交付前定义 `Final Validate`（总验证）与 `Final Review`（总评审 + Delivery Report）

落盘方式：
- Plan.md：写清每个 checkpoint/milestone/final 的覆盖面与证据入口预期
- Task.md：为每个任务组追加一个 `Validate Checkpoint` 勾选项；为每个里程碑追加 `Milestone Validate` 勾选项；最后追加 `Final Validate`

### Step 5.1：验证矩阵（L3 建议强制）

- 把 AC-XXX 逐条映射到验证方式与证据入口（State.md Evidence Index）。
- 验证矩阵是 Review 的输入：没有矩阵就很难做证据驱动评审。

### Step 6：拆 Task（最小执行单元）

拆分规则：
- 一条任务要能独立完成并验收
- 每条任务写清：产出物、验收方式、依赖
- 不确定就先拆“调查/澄清”任务，不要在实现阶段才发现缺口

### Step 6.0：Task.md 的“组级结构”（必须）

Task.md 不只是“散点清单”，它是 Plan.md 的可执行拆解，必须满足：
- 任务按“大标题/任务组”组织（例如 `## 4.A 用户登录（组）`）
- 每个任务组末尾都有一个 `Validate Checkpoint`（scope=checkpoint）
- 每个里程碑末尾都有一个 `Milestone Validate`（scope=milestone）
- 全部任务末尾都有 `Final Validate`（scope=final）与交付回执（Delivery Report）

### Step 6.1：挂接验收契约（L3）

- 生成/更新：`templates/AcceptanceContract.template.md`
- 每条 AC-XXX 至少被一个 Task 覆盖（任务负责让其可验收）

### Step 7：落盘与同步

- Plan/Task 落盘后，更新 State.md 的 Progress（当前阶段切到 “AuthGate/等待执行授权”）
- 把“验证入口”（命令/脚本/实验ID/引用列表）预先写进 Evidence Index

（L3）同时预留：
- 验收契约文件位置（AcceptanceContract）
- 复现协议模板位置（ReproProtocol-*）

### Step 7.0：Plan 质量自检（防止 Plan/Task “写了但不可用”）

> 目的：把“计划写完了”变成“计划可执行、可验收、可验证”。这一步是阻止敷衍 Plan 的最后门禁。

要求：
- 对照 `templates/Plan.template.md` 的 `Ready-to-Execute Gate` 逐项自检
- 任一关键项缺失：继续停留 Plan Mode 补齐，不要请求执行授权
- Plan/Task 中不得残留明显占位符（例如 `<...>`、`TODO`、`path/to/file` 等）；若需要占位，必须标注为阻塞点并写清“最小输入”
- 对于 L3：必须能在 Plan/State 中指向以下入口（路径或段落锚点）：
  - 验收标准（≥2 条）
  - Spec（接口/错误语义/示例/不变量）
  - 验证数据与 Cadence（checkpoint/milestone/final）
  - 关键风险与依赖（阻塞点不能“假装不存在”）
  - Task 的任务组结构与检查点任务

### Step 7.1：请求执行授权（固定门禁）

当 Plan/Task 就绪：
- 明确告知：接下来进入 Execution Mode 会改动代码/运行命令/产生产物。
- 为避免误判：只有当 Ready-to-Execute Gate（Plan.md 内的退出门禁）已满足时，才允许请求用户授权；否则继续停留 Plan Mode 补齐缺口。
- 授权口令固定：要求用户用明确指令授权（建议独立消息或独立一行）：**请单独回复 `开始执行`**。
- 授权后把授权记录写入 Plan/State（time + scope），并在 State 元信息标记 `Execution Session=active`（session_id/started_at/scope）。

---

## 何时必须返回用户

- 验收标准无法确定（用户自己也不清楚）
- 需要外部账号/数据权限/预算
- 任务边界涉及风险（生产/敏感信息/不可逆操作）需要授权

---

## library 索引（按触发条件查）

- 需求/验收/验收契约：`library/requirements-acceptance.md`
- 大任务治理（里程碑/依赖/变更控制）：`library/project-governance.md`
- 验证矩阵与证据门禁：`library/testing-verification.md`
- 开发范式协同（Software：SDD/Characterization/Spike/BDD...）：`library/development-paradigms.md`
- 复现协议：`library/reproducibility.md`
