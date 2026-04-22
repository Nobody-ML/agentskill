> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Stakeholders & Concerns 模板

用途：把“谁关心什么”落盘，避免架构与实现只围绕开发者视角。

启用建议：Level=L3 或任何架构/选型/性能/安全/可维护性是关键的任务。

---

## 1. Stakeholders（利益相关方）

列出至少 3 类：

| Stakeholder | 角色说明 | 关键目标 |
|---|---|---|
| 用户/使用者 |  |  |
| 维护者/开发者 |  |  |
| 运行/运维/部署者 |  |  |
| 安全/合规（如适用） |  |  |

---

## 2. Concerns（关注点）

把关注点写成“可讨论、可验证”的条目：

| Stakeholder | Concern（关注点） | 如何验证/证据 | 优先级 |
|---|---|---|---|
|  |  |  | P0/P1/P2 |

---

## 3. 影响到的决策（Decision Hooks）

把 concerns 映射到需要做的决策点（DEC/ADR）：

| Concern | 影响的决策点（DEC-XXX/ADR-XXX） | 备注 |
|---|---|---|
|  |  |  |
