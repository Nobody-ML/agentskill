> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Delivery Report：<任务/项目名称>

版本：`vX.Y.Z`（或日期）  
Track：Research / Software / Writing / Simple  
WorkType（仅 Software）：Build / Debug / Ops  
Level：L0 / L1 / L2 / L3  
结论：PASS / NEEDS_USER_DECISION / BLOCKED  
日期：YYYY-MM-DD

---

## 1. What Was Done（做了什么）

用 3–8 条描述“做了什么”，每条都应能映射到 Task 或验收标准：
- 

---

## 2. Files Changed（改了哪些文件）

> 只列关键文件与关键改动点；避免堆所有细节。

- `path/to/file`：一句话变化

（可选）新增/更新文档：
- `path/to/doc`：一句话变化

---

## 3. Acceptance Criteria Result（验收条目结果）

> 对照 Acceptance Contract / Plan 的验收标准逐条给结论。

- AC-001: pass/fail/blocked/partial/missing（证据入口）

---

## 4. Validation Summary（验证摘要）

### 4.0 过程合规（Process Compliance）

> 目的：让“按 skill 执行”变成可复查事实，而不是对话承诺。

- Execution Authorization 记录入口（Plan/State 的路径或段落锚点）：
- 授权时间与 scope（允许执行的目录/环境/边界）：
- Task 覆盖摘要（本次完成了哪些任务组/任务 ID；或指向 Task.md 勾选结果）：
- 关键变更 → Task 映射（至少列 3–10 条关键改动与对应任务 ID）：

### 4.1 验证数据声明（真实数据优先）

- data_type：real / sanitized-real / synthetic
- 数据来源入口：
- synthetic（如使用）差距说明：

### 4.2 运行的验证（命令与摘要）

- command：
  - exit_code：
  - summary：
  - artifact（日志/截图/链接）：

### 4.3 Evidence Index 入口

- `State.md#Evidence Index`：条目名称/关键索引

## 5. Review Score（评审打分）

- 总分：X.X/10
- 维度分：<按 rubric 列出>

---

## 6. Residual Risks（剩余风险）

> 只写事实与后果，不写情绪化措辞。

- 

---

## 7. Limits（限制）

- 

---

## 8. Resumption Block（可续跑块）

（建议贴入 YAML；格式参考：`templates/ResumptionBlock.template.md`）

---

## 9. Final Statement（最终结论）

- 结论：PASS / NEEDS_USER_DECISION / BLOCKED
- 下一步（最多 1–3 条，按优先级）：

- P0：
- P1：
- P2：
