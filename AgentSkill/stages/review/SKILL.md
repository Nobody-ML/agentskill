---
name: review
description: 评审与打分：按 Track 选择评分表，绑定证据给出分数与整改清单，并依据门禁决定是否返工复评
---

# Review（评审与打分）

## 目标

把“看起来不错/差不多”变成：
- 有维度、有证据的评分
- 有优先级、可执行的整改清单
- 明确的结论（PASS / NEEDS_USER_DECISION / BLOCKED）

---

## Stage Contract（阶段契约）

### 输入（Inputs）
- 交付物 + Validate 证据
- `Plan.md`（验收标准/验证方案）
- （L3）Acceptance Contract（AC-XXX）与验证矩阵

### 输出（Outputs）
- 总分（0–10）+ 维度证据
- P0/P1/P2 整改清单
- 结论：PASS / NEEDS_USER_DECISION / BLOCKED
- Delivery Report（固定格式交付回执）

### 工件更新（Artifacts Updated）
- `State.md`：Evidence Index + Progress
- （L3 可选）Acceptance Contract：更新 AC 状态/备注

### 退出条件（Exit Criteria）
- 给出结论与下一步（交付 / 返工 / 回到 Plan）

### 返工条件（Rework）
- Validate 不通过 → 必须返工复评（BLOCKED）

---

## 必读协议（L2/L3 强制加载）

- 交付与评审协议：`protocols/06-delivery-and-review.md`
- 门禁状态机：`protocols/00-hard-gates.md`（G8）

常用模板：
- 交付回执：`templates/DeliveryReport.template.md`
- 评分表：`templates/ReviewRubric-*.template.md`
- 评审报告（可选）：`templates/ReviewReport.template.md`

---

## library 索引（按触发条件查）

- 深计划质量标准（用于判定“Plan/Task 是否敷衍”）：`library/plan-quality-standard.md`
- 验收标准/验收契约：`library/requirements-acceptance.md`
- 测试与证据门禁：`library/testing-verification.md`
- 大任务治理（返工与变更控制）：`library/project-governance.md`
- 质量/运维/维护（质量整改打法）：`library/quality-operations-maintenance.md`

---

## 输入

- 交付物（代码/文档/实验结果/计划）
- Validate 阶段的证据（命令输出、实验记录、引用清单、截图等）
- State.md（风险、约束、验收标准）

---

## 输出（必须包含）

（L2/L3 强制）每轮对外回复开头必须带：

```text
【Mode】Review | 结论=<PASS/NEEDS_USER_DECISION/BLOCKED> | 总分=<0-10>
```

1) 总分（0–10，允许小数）
2) 每个评分维度的证据/理由
3) 整改清单（P0/P1/P2）
4) 结论：PASS / NEEDS_USER_DECISION / BLOCKED
5) 过程与对齐审计摘要（Execution Authorization 入口 + Task 映射入口 + Non-negotiables 检查结论）
6) State.md 更新：Evidence Index + Progress

---

## 评分模板选择

- Research → `templates/ReviewRubric-Research.template.md`
- Software → `templates/ReviewRubric-Software.template.md`
- Writing → `templates/ReviewRubric-Writing.template.md`
- 交付回执（固定格式）→ `templates/DeliveryReport.template.md`

---

## 门禁规则（用户偏好，必须执行）

### -1) 硬门禁：过程合规违规（Stop-the-line）

> 目的：解决“未授权就写代码/脱离 Plan/Task 推进/跑几轮忘记 skill”这类过程事故。过程失控会让任何分数都失去意义，因此必须先停线。

当 Level≥L2，命中任一项：
- 执行阶段发生了改动/运行，但 `Execution Authorization != received`
- 交付物的关键改动无法映射到 `Task.md` 的具体条目（找不到任务组/任务 ID）
- Validate/Review 使用了 `synthetic` 数据，但 Plan/State 没有用户确认“无可用真实样本（含脱敏样本）”的记录

处理规则：
- 结论必须为 `BLOCKED`
- 动作：执行 `SKILL.md` 的 Recovery Protocol（回到 Plan 补齐 Plan/Task/State 与证据门禁，再重新走授权门禁）

### -0) 硬门禁：Plan/Task 契约缺失或敷衍（L2/L3）

> 目的：解决“Plan/Task 写得很敷衍，导致执行与验证无从对照”的问题。没有可执行契约，就无法评审交付是否符合需求。

当 Level≥L2，命中任一项：
- 不存在 `Plan.md` 或 `Task.md`
- Plan 未包含关键门禁项（验收标准、边界、Spec、验证数据声明、Cadence 映射到 Task）
- Task 未按任务组组织，或缺少 `Validate Checkpoint` / `Milestone Validate` / `Final Validate`
- Plan/Task 残留大量占位符且未标注为阻塞点（例如 `<...>`、`TODO`、`path/to/file`）

处理规则：
- 结论必须为 `BLOCKED`
- 动作：回到 Plan 重写/补齐 Plan/Task（先把契约变得可执行，再谈交付质量）

### 0) 硬门禁：真实数据门禁违规（数据类型不合规）

若 Validate 使用了 `synthetic` 数据，但 Plan/State 中**没有**用户已确认“无可用真实样本（含脱敏样本）”的记录：
- 结论必须为 `BLOCKED`
- 动作：回到 Plan 解决数据门禁（补真实样本/脱敏样本、或由用户更新验收与范围），再 Execute/Validate/Review

### 1) 硬门禁：验证不通过

若 Validate = `failed`（测试失败/实验跑不通/引用缺失/示例不可运行）：
- 结论必须为 `BLOCKED`
- **必须返工并复评**（回到 Execute → Validate → Review）

### 1.1) 验证缺失（missing）

若 Validate = `missing`（没有测试/环境不可运行/证据入口缺失）：
- 必须明确提示风险（哪些断言/哪些路径无法被证据支撑）
- 结论默认：`NEEDS_USER_DECISION`
- 是否返工并复评：由用户决定（默认建议补齐最小验证或在 Plan 中降低/调整验收）

### 2) 软门禁：总分阈值

- 若总分 ≥ 7.0/10 且验证通过 → `PASS`
- 若总分 < 7.0/10 且验证通过：
  - 必须提醒用户当前质量风险与可能后果
  - 结论为 `NEEDS_USER_DECISION`
  - 是否返工并复评：由用户反馈决定（默认建议返工）

> 解释：分数是“质量信号”，验证是“可用性证据”。二者都重要，但验证优先。

---

## 工作步骤

### Step 0：过程与对齐审计（先停线再打分）

在打分前先确认三件事（任一不满足直接 BLOCKED）：
1) 执行授权与范围：Execution Authorization 已落盘（time+scope），且执行行为在 scope 内
2) 任务追溯：关键改动/关键结论能映射到 Task 条目（任务组/任务 ID）
3) 用户意图一致：交付物没有违反 Plan 的 Non-goals/Non-negotiables（例如擅自兜底/擅自降级/跳过真数据门禁）

### Step 1：对照验收标准

- 把 Plan 中的验收标准逐条映射到交付物与证据。
- 缺证据的项先标为 P0 或直接 BLOCKED（视影响）。

### Step 2：逐维度打分（必须写证据）

- 只允许两类依据：
  1) 可指向的证据（输出/实验/引用/截图）
  2) 可复述的约束（来自用户/Plan/State）

### Step 3：产出整改清单（P0/P1/P2）

- P0：阻断验证/明显错误/安全与合规
- P1：强烈建议，显著改善质量与可维护性
- P2：可选优化

### Step 4：给出结论并更新 State

- 写清结论与理由
- 把证据入口写进 State.md（Evidence Index）
- 更新 Progress（是否回到 Plan/Execute、或进入交付）

### Step 5：生成 Delivery Report（交付回执）

按模板 `templates/DeliveryReport.template.md` 输出交付报告，必须包含：
- 做了什么（对照 Task/验收标准）
- 过程合规（Execution Authorization 记录入口 + 关键改动→Task 映射摘要）
- 怎么验证（命令/数据类型/结果摘要）
- 证据入口（State Evidence Index）
- 风险与限制（缺失验证/使用 synthetic 数据等必须明示）

（交付后的反馈回路）
- 用户检验不满意/提出新想法：视为新一轮迭代，回到 Plan 更新验收与 Task，再重新走授权门禁；不要在交付后“悄悄补改”。

---

## 建议的对外输出格式（简洁）

```text
【Review】总分: X.X/10 | 结论: PASS/NEEDS_USER_DECISION/BLOCKED
P0: ...
P1: ...
P2: ...
证据: (指向 State.md 的 Evidence Index 条目)
```

交付时追加：

```text
【Delivery】按 templates/DeliveryReport.template.md 输出交付报告
```
