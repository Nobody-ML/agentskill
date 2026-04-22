> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Quality Attributes（质量属性）模板

用途：把“架构好不好”的讨论从偏好变成可取舍的质量属性集合。

启用建议：Level=L3 或存在明显 trade-off（性能/可靠性/安全/可维护性/成本/复现性）。

---

## 1. Top Quality Attributes（排序）

选 3–7 个最重要质量属性，并排序。

| Rank | Attribute | 为什么重要（1–2 句） | 如何验证/证据 |
|---:|---|---|---|
| 1 |  |  |  |

---

## 2. Quality Attribute Scenarios（场景化，推荐）

把质量属性写成“场景”，避免抽象口号。

模板：
- 当【刺激 Stimulus】发生在【环境 Environment】中，系统应在【响应 Response】上达到【度量 Measure】。

| Attribute | Scenario | 验证方式 | 通过标准 |
|---|---|---|---|
|  |  |  |  |

---

## 3. Trade-offs（取舍显式化）

| 决策点 | 获得什么 | 牺牲什么 | 受影响的 AC-XXX | 备注 |
|---|---|---|---|---|
|  |  |  |  |  |
