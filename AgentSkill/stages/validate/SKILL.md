---
name: validate
description: 证据门禁：把“应该没问题”变成可复现/可观察的验证证据，并写入 State 的 Evidence Index
---

# Validate（验证与证据）

## 铁律

> 没有新鲜证据，不得宣称“完成/通过/修复/正确”。

验证的目标不是“让人放心”，而是**让结论可复查、可复现**。

---

## Stage Contract（阶段契约）

### 输入（Inputs）
- 需要验证的交付物（代码/实验结果/文档）
- `Plan.md` 的 Validation Plan
- （L3）Acceptance Contract（AC-XXX）与验证矩阵

### 输出（Outputs）
- 验证结论：passed / failed / missing
- 证据入口：命令输出/日志/截图/引用条目/实验记录
- 验证数据声明：data_type（real / sanitized-real / synthetic）+ 来源入口
- 验证范围声明：scope（checkpoint / milestone / final）+ 覆盖面摘要

### 工件更新（Artifacts Updated）
- `State.md`：Evidence Index（必须更新）
- （L3）Acceptance Contract：可选更新 AC 状态（passed/blocked），并写入验证矩阵入口

### 退出条件（Exit Criteria）
- 每个关键结论都有证据入口，且能进入 Review

### 返工条件（Rework）
- 任一关键验证失败 → 回到 Execute 修复，再 Validate

---

## library 索引（按触发条件查）

- 测试策略与证据门禁：`library/testing-verification.md`
- 复现协议：`library/reproducibility.md`
- 风险与安全（验证缺失时的提示与决策）：`library/risk-security.md`

---

## 输出

（L2/L3 强制）每轮对外回复开头必须带：

```text
【Mode】Validate | scope=<checkpoint/milestone/final> | data_type=<real/sanitized-real/synthetic>
```

- 运行了哪些验证（命令/步骤）
- 结果是什么（成功/失败/缺失）
- 验证使用的数据（real / sanitized-real / synthetic）与来源入口
- 验证范围（checkpoint / milestone / final）与覆盖面摘要
- 覆盖维度（Dimensions）：本次覆盖了哪些（Correctness/Spec/Failure/Performance/Docs/...），哪些未覆盖与原因
- 真实数据获取尝试（当 data_type!=real/sanitized-real 时必须写）：尝试入口 + 不可用原因
- 证据入口在哪里（日志/截图/链接/实验记录）
- State.md：Evidence Index 必须更新

结果枚举建议：
- `passed`：验证通过，有证据入口
- `failed`：验证失败（必须返工）
- `missing`：验证缺失/不可运行（必须提醒风险；是否返工由用户决定，L3 默认建议补齐）

---

## 验证节奏（Cadence）：Checkpoint → Milestone → Final

> 目的：在“不把流程做重”的前提下维持可验证性：组内小步推进，组间检查点验证，里程碑再做宽验证，最后做总验证与总评审。

### scope 定义（必须标注）

- `checkpoint`：任务组级验证（覆盖“本组改动影响的关键路径/失败模式/边界”，目标是快速回归）
- `milestone`：里程碑级验证（更宽的回归 + 性能/资源 smoke check + 规范与文档一致性）
- `final`：全局总验证（全套验收断言/关键路径/复现要素/交付文档与 Runbook）

### 选择规则（从上到下命中即采用更高强度）

1) 这是最终交付前 → `final`
2) 完成一个里程碑（Plan 中定义的 M1/M2/...）→ `milestone`
3) 完成一个任务组（Task.md 的一个大标题）→ `checkpoint`

### scope 与“快慢”平衡

- checkpoint 追求快：只要能证明“这一组没把系统搞坏”，并能让下一组安心推进。
- milestone 追求稳：要能支撑一次阶段性交付与回滚决策。
- final 追求完整：要能支撑最终 PASS（Review）的证据链。

---

## 验证覆盖维度（Dimensions，不止正确性）

> 目的：解决“跑了测试但完全不符合用户需求/不符合规范/性能不可用”的问题。验证不是单一维度，至少要覆盖对用户最敏感的那几项。

建议把验证拆成可打勾的维度（按 Track/WorkType 取最相关的子集）：

1) **Correctness（正确性）**：对照验收标准/关键路径是否成立
2) **Spec & Consistency（规范与一致性）**：接口/错误语义/边界/日志/配置是否符合 Plan 的 Spec
3) **Failure Modes（失败模式）**：错误输入、缺资源、权限不足、网络异常等是否按预期失败
4) **Performance & Resource（性能与资源）**：至少一次 smoke check（耗时/内存/吞吐/峰值），高风险时做基准对比
5) **Maintainability（可维护性信号）**：复杂度、重复、可读性（作为 Review 的证据输入）
6) **Security & Compliance（安全与合规）**：敏感信息、权限边界、危险操作门禁
7) **Docs & Operability（文档与可运行性）**：Runbook/运行说明/验证说明是否能支撑复查与复跑
8) **Visual/UX（视觉/可视化验证，按需）**：截图/渲染/图示可读性（Writing/UI 相关任务）

对外输出时无需把每一项都展开成大段文字，但必须明确：
- 本次 scope 覆盖了哪些维度
- 哪些维度未覆盖，以及为什么（阻塞点/成本/数据缺失）

---

## 验证数据门禁（真实数据优先）

> 目的：避免“在假数据上跑通”带来的虚假安全感。默认先用真实数据（可脱敏），确认没有真实样本后才允许模拟。

### 数据类型（必须标注）

- `real`：真实系统/真实数据源的样本（可能含敏感信息，需遵循边界与合规）
- `sanitized-real`：真实样本的脱敏版本（允许裁剪、打码、去标识）
- `synthetic`：为验证临时生成的模拟数据（必须明确标注，不能当作真实覆盖）

### 优先级（从上到下找，命中即停）

1) 用户提供的真实样本（可脱敏）
2) 仓库内样本数据/fixture/示例输入（若确为真实或来自真实分布）
3) 可采集的最小真实日志/请求样本（只读、脱敏、最小化）
4) 权威公开数据集（研究任务常用）
5) `synthetic`（仅当用户明确确认“没有可用真实样本/脱敏样本”后）

### 硬规则

- Level≥L2：默认必须使用 `real` 或 `sanitized-real` 做至少一次关键路径验证。
- 只有在用户明确确认“确实没有可用真实样本（含脱敏样本）”后，才允许 `synthetic`。
- 使用 `synthetic` 时必须额外记录：
  - 为什么缺少真实样本
  - synthetic 与真实分布的差距（可能遗漏哪些失败模式）
  - 下一步如何补真实样本验证（写入 Plan/State）

---

## 工作步骤

### Step 0：确定验证范围与验证数据（并标注）

- scope：checkpoint / milestone / final
- 选择数据类型：real / sanitized-real / synthetic
- 记录数据来源入口（文件/链接/采集命令/数据集版本）
- 若选择 `synthetic`：必须在 Plan/State 中能找到用户已确认“无可用真实样本（含脱敏样本）”的记录；否则本轮 Validate 结论只能是 `missing`（并返回 Plan 解决数据门禁）。
- （建议强制）记录“真实数据获取尝试”（Data Acquisition Log）：
  - 尝试了哪些入口（用户样本/仓库样本/最小日志采集/公开数据集）
  - 为什么不可用（权限/脱敏成本/不可获得）

### Step 1：选择验证集合（按 scope 选“最小但够用”的集合）

优先验证：
- 关键路径（主流程）
- 失败模式（错误输入、缺资源、权限不足）
- 边界条件（空/极值/并发/大数据量）

（按 scope 补充）
- checkpoint：优先“本任务组改到的那条路径”
- milestone：加上跨模块交互路径与关键回归
- final：对照验收标准/验收契约逐条覆盖（尤其 L3）

（按维度补充，避免只测正确性）
- milestone：至少覆盖 Correctness + Failure Modes + Performance/Resource + Docs/Operability
- final：在 milestone 的基础上，补齐 Spec/Consistency + Security/Compliance（按风险触发）+ Writing/UI 的 Visual/UX（如适用）

### Step 2：执行验证并记录结果

记录字段建议：
- command / action
- exit code（如有）
- 观察到的关键输出摘要
- 证据文件/截图/链接路径

### Step 3：把证据写入 State.md

更新 `Evidence Index`，确保后续评审与复盘能直接定位证据。

---

## 按 Track 的最小验证建议

### Software

按项目实际选择（至少一个）：
- 单元/集成测试
- typecheck/lint
- 手动走通（包含失败分支）
-（建议）关键路径的性能/资源 smoke check（至少记录一次运行耗时/内存/失败模式）

> 若项目缺少测试/无法运行：必须提示用户“验证缺失”的风险，并在 State.md 记录。

### Research

至少包含：
- 最小可行实验（MVE）或 sanity check
- 指标可计算且解释清楚
- 基线或对照（哪怕是弱基线）
- 复现要素齐全（环境/seed/数据版本/脚本）

### Writing

至少包含：
- 来源与引用可追溯（关键结论能定位出处）
- 示例/代码可运行（给出运行方式与输出摘要）
- 图示可读（图注说明用途；能解释关键关系）

---

## 失败时怎么做

- 验证失败：回到 Execute 修复，再重新 Validate。
- 验证缺失：回到 Plan 补齐验证方案，或请求用户提供环境/权限。
