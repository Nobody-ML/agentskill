# Delivery Report：<任务/项目名称>

> 注意：本模板仅提供参考结构，不是执行规范；实际输出必须遵循本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md`。模板与规则冲突时，以规则为准。

版本：`vX.Y.Z`（或日期）  
Track：Research / Software / Writing / Simple  
WorkType（仅 Software）：Build / Debug / Ops  
Level：L0 / L1 / L2 / L3  
结论：PASS / NEEDS_USER_DECISION / BLOCKED  
日期：YYYY-MM-DD

---

## 1. 摘要（What changed）

用 3–8 条描述“做了什么”，每条都应能映射到 Task 或验收标准：
- 

---

## 2. 交付物清单（Deliverables）

- 文件/目录：
- 文档：
- 运行/实验产物（如有）：

---

## 3. 变更清单（Key Changes）

> 只列关键文件与关键改动点；避免堆所有细节。

- `path/to/file`：变化一句话
- `path/to/doc`：变化一句话

---

## 4. 验证与证据（Validation & Evidence）

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

---

## 5. 风险、限制与未完成项（Risks & Limits）

> 只写事实与后果，不写情绪化措辞。

- 

---

## 6. 返工/后续（Next）

> 不发散；最多 1–3 条，按优先级给出可执行动作。

- P0：
- P1：
- P2：
