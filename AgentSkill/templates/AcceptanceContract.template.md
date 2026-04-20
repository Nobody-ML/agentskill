# Acceptance Contract（验收契约）模板

> 注意：本模板仅提供参考结构，不是执行规范；实际输出必须遵循本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md`。模板与规则冲突时，以规则为准。
>
> 用途：把“验收标准”写成可追踪、可测试的断言集合（Assertions）。
>
> 启用条件：Level = L3 或风险/依赖复杂度触发治理层。

---

## 1. 断言清单（Assertions）

断言格式要求：
- 必须可测试/可观察/可复现
- 必须写明证据要求（Evidence Requirements）
- 必须能映射到 Task（至少一个任务负责让它“可验收”）

| ID | 标题 | 行为断言（Pass/Fail） | 证据要求 | 负责任务 | 状态 |
|---|---|---|---|---|---|
| AC-001 |  |  |  |  | pending |
| AC-002 |  |  |  |  | pending |

状态枚举：`pending / passed / blocked / deferred`

---

## 2. 验证矩阵（Assertion → Evidence）

| AC | 验证方式（测试/实验/手动/引用） | 证据入口（State.md Evidence Index） | 备注 |
|---|---|---|---|
| AC-001 |  |  |  |

---

## 3. 变更规则

- 新增/修改断言：必须同时更新 Plan/Task 与 Evidence Index 入口约定
- 断言通过：必须在 Evidence Index 能定位证据
- 断言 deferred：必须写明原因与后续计划（Decision Log）
