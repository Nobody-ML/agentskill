# State（统一记忆与进度）模板

> 注意：本模板仅提供参考结构，不是执行规范；实际输出必须遵循本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md`。模板与规则冲突时，以规则为准。
>
> 目的：把“任务的长期事实”从对话里抽出来，成为可持续维护的单一真相来源（SSOT）。
>
> 使用方式：每次完成一个阶段、发现新约束、验证产出、做出关键决策，都要更新本文件。

---

## 0. 元信息

- **当前任务/项目名**：
- **Track**：Research / Software / Writing / Simple
- **WorkType（仅 Software）**：Build / Debug / Ops
- **Level**：L0 / L1 / L2 / L3
- **当前阶段**：Router / Brainstorm / Research / Plan / Execute / Validate / Review / Write
- **Execution Authorization**：required / received / not_required
- **迭代标识（Iteration ID）**：v1 / v2 / YYYYMMDD-HHMM（用于多轮反馈→再规划→再执行）
- **Execution Session（执行会话）**：none / active / completed
  - session_id：
  - started_at：
  - scope：（允许执行的目录/环境/边界）
- **创建时间**：YYYY-MM-DD
- **最后更新**：YYYY-MM-DD HH:MM

---

## 1. Memory（稳定事实）

### 1.1 用户偏好
- 输出语言：简体中文（术语保留英文）
- 写作风格：
- 详细程度偏好：
- 是否允许联网搜索：
- 是否允许改动文件/代码：
- 执行授权口令（默认）：`开始执行`

### 1.2 约束与边界（不可违反）
- 禁止访问/操作：
- 安全与合规：敏感信息、生产环境、破坏性操作等
- 资源限制：CPU/内存/时间/预算
- 工具限制：可用工具列表、不可用工具列表
- 兜底/降级策略：默认禁止；如允许，必须列出已确认策略（触发条件/成本/对验收影响/验证方式）与对应 Decision Log 条目

### 1.3 术语表（Glossary）
- 术语A：定义
- 术语B：定义

### 1.4 架构/治理索引（L3 / 高风险触发）

- Stakeholders & Concerns（路径）：
- Quality Attributes（路径）：
- ADR 索引（路径或列表）：
- Architecture Blueprint/Description（路径）：
- Acceptance Contract（路径）：
- Validation Matrix（入口）：
- Repro Protocol（路径）：
- Ops Runbook（路径，如适用）：
- Literature Matrix / Paper Outline（如适用）：

---

## 2. Decision Log（关键决策记录）

> 只记录“会改变后续路径/成本/风险”的决策，避免流水账。

### DEC-001：标题
- **时间**：YYYY-MM-DD
- **问题**：要解决什么？
- **决策**：最终选择是什么？
- **备选**：A / B / C
- **拒绝理由**：为什么不选其它？
- **影响**：对架构/验证/写作/复现的影响
- **证据**：链接/命令输出摘要/引用条目

（继续追加 DEC-002、DEC-003…）

---

## 3. Progress（进度与阻塞）

### 3.1 当前目标
- 目标一句话：

### 3.2 里程碑
- M1：
  - 状态：pending / in_progress / done
  - 产出物：
- M2：

### 3.3 当前阻塞（如有）
- 阻塞点：
- 需要用户提供：
- 备选方案：

### 3.4 治理信息（L3 / 高风险触发）

- 验收契约（Acceptance Contract）位置：
- 复现协议（Repro Protocol）位置：
- 依赖表位置（如单独维护）：
- Execution Authorization（time + scope + 记录位置）：

### 3.5 Next Action（可续跑指针，必须维护）

> 目的：防止跨轮失忆。下一轮 Router/Execute 必须先读这一段再继续。
>
> 交接约定：当需要输出“上下文压缩/交接摘要”时，Resumption Block 必须直接从这一段生成（当前任务组/检查点/Next Action/阻塞点/未完成项入口），摘要不是结束点。

- 当前正在推进的任务组（Task Group）：
- 已完成到哪个检查点（checkpoint/milestone/final）：
- 下一步要做的 1–3 个动作（按顺序）：
- 若下一步需要真实数据/权限/账号：写清阻塞点与最小输入：

---

## 4. Risks & Assumptions（风险与假设）

| ID | 类型 | 描述 | 影响 | 缓解措施 | 状态 |
|---|---|---|---|---|---|
| R-001 | 风险 |  |  |  | open |
| A-001 | 假设 |  |  |  | open |

---

## 5. Evidence Index（证据索引）

> 所有“完成/通过/正确/可复现”的结论都必须能在这里找到证据入口。

（L3 建议）验收契约验证矩阵入口：
- `AcceptanceContract:`
  - `path:`
  - `notes:`

### 5.1 软件工程（命令与输出摘要）
- `command:`
  - `exit_code:`
  - `summary:`
  - `artifact:`（日志/截图/链接）

### 5.2 科研/算法（实验记录）
- 实验ID：
  - 环境：OS/CPU/GPU/依赖版本
  - 数据：版本/切分/预处理
  - 参数：seed/超参
  - 指标：
  - 结果：
  - 复现方式：脚本/命令

### 5.3 写作（来源与一致性）
- 引用条目：作者/标题/年份/链接/关键结论
- 图示清单：图名→文件或代码块位置→用途
- 示例可运行性：示例路径/运行命令/输出摘要
