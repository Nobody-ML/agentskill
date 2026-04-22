# 03-execution-preflight：执行预检协议（Preflight）

适用范围：
- Track：Research / Software / Writing
- Level：L2 / L3（强制）

目标：
把“开干”变成可控行为：执行前先确认授权、边界、数据、环境、风险与回滚点；避免执行中才发现缺依赖/缺数据导致大返工。

相关门禁：
- `protocols/00-hard-gates.md`：G6（Execution Preflight）
- `protocols/07-fallback-and-boundaries.md`：执行期禁止擅自兜底

---

## 1) Plan Mode 下允许的非变更探测（Non-mutating probes）

Plan Mode 允许做“只读探测”，用于获得必要证据：
- 文件与目录勘测：`ls`、`find`、`rg`
- 读取文件：`sed`、`cat`
- 静态分析：格式检查、类型检查（不改文件）
- 轻量复现：只要不改业务文件、不跑破坏性命令、不进入长任务

硬规则：
- 只读探测必须记录到 Plan/State（读了哪些文件/跑了哪些命令/得到什么结论）。

---

## 2) Execution Preflight 最低清单（执行批次开始前）

执行批次 = 按 Task.md 的一个 Task Group 或一个 checkpoint 节奏推进的批量执行。

执行前必须确认并落盘：

1) **授权与范围**
   - Execution Authorization=received（否则停下回 Plan）
   - Allowed/Forbidden 路径范围明确
2) **目标与验收**
   - 本批次对应哪些 AC/哪些 Task
   - 本批次结束要跑哪一层验证（micro-check/checkpoint/milestone/final）
3) **数据就绪**
   - 本批次验证用的数据来源与类型（real/sanitized-real/synthetic）
   - 缺数据时的阻塞点（不得擅自用 synthetic 代替）
4) **环境与依赖**
   - 运行时版本、依赖、GPU/驱动（若需要）
   - 安装/启动命令
5) **风险与回滚**
   - 破坏性操作的备份点
   - 失败时回滚路径
6) **观测点**
   - 日志、指标、关键产物路径

模板参考：
- `templates/ExecutionPreflight.template.md`

---

## 3) Preflight 失败处理

Preflight 不通过时，不得进入执行：
- 缺授权：回 Plan，等待用户授权
- 缺数据：回 Plan，补数据策略与最小输入
- 缺依赖：回 Plan，补依赖安装与验证步骤
- 风险不可控：回 Plan，补边界/回滚/兜底登记（如需）

