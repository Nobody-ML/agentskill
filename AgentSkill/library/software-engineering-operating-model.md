# Software Engineering Operating Model（通用工程作战模型）

适用：
- Track：Software
- Level：L2 / L3（强制建议）

目的：
把工程任务从“写代码”升级为“端到端可交付系统”：
- 需求可验收（Acceptance）
- 方案可论证（Architecture / trade-offs）
- 实现可维护（Modularity / readability）
- 验证可复查（Evidence）
- 运行可操作（Ops/Runbook）

本文件是通用模型：不绑定某一种开发教条，而是按任务形态组合工具箱。

相关资料入口：
- `library/development-paradigms.md`（范式工具箱）
- `library/requirements-acceptance.md`（验收与契约）
- `library/testing-verification.md`（验证与证据）
- `library/quality-operations-maintenance.md`（质量与运维）

---

## 1) 统一链路：从需求到交付（必须能画出来）

建议写进 Plan 的 Tech Chain（示意）：

```mermaid
flowchart LR
  Req[需求/约束] --> Spec[Spec/AC/接口]
  Spec --> Arch[架构/模块/ADR]
  Arch --> Impl[实现/集成]
  Impl --> Val[验证/证据]
  Val --> Rev[评审/打分]
  Rev --> Del[交付/回执]
  Del --> Ops[运行/维护/监控]
  Ops -->|反馈| Req
```

核心原则：
- 任何“实现动作”必须能回指 Spec/Task
- 任何“完成宣称”必须绑定证据

---

## 2) 三种工作形态（WorkType）与默认策略

### 2.1 Build（开发建设）

目标：把新能力做出来并可验证。

默认策略组合：
- SDD（Spec-Driven）：先把接口/错误语义/验收断言写清
- 风险驱动验证：先覆盖高风险路径
- 小步集成：每个 Task Group 出一个可验证产物

### 2.2 Debug（诊断修复）

目标：把问题变成可复现的证据，再修复并回归。

默认策略组合：
- 复现优先（最小输入、最小场景）
- 行为锁定（characterization / regression）
- 观测增强（logs/metrics/artifacts）
- 小改动修复 + 关键路径回归

### 2.3 Ops（运行维护 / 训练监控）

目标：跑得稳、看得见、能复盘、能恢复。

默认策略组合：
- Runbook 先行（启动/停止/健康检查/阈值/排障）
- 观测点与阈值明确（而不是“盯屏幕”）
- Checkpoint 与恢复协议（断点续跑）

参考：
- `protocols/08-long-running-ops.md`
- `library/long-run-agent-operations.md`

---

## 3) Plan 的“工程密度”最小要求（L3 强制）

Plan 至少要写清：
- 质量属性 Top 3–7（性能/可靠性/安全/可维护性/可诊断性…）
- 候选方案对比（至少 2 条路线 + 推荐）
- Pipeline Stages 表（阶段→技术→验证）
- 真实数据策略 + 验证矩阵
- 断点续跑与失败隔离（当任务可能跨多轮/长时间）

若写不出来：
- 不要进入 Execute
- 先回 Brainstorm/Research 补齐证据与取舍

---

## 4) 规格（Spec）写什么（避免“写一堆实现细节”）

Spec 的最小集合：
- Data model（关键结构与不变量）
- Interfaces（输入/输出/参数/返回码/错误语义）
- State（状态机/缓存/持久化/一致性约束）
- Observability（日志/指标/关键产物）
- Performance targets（至少 smoke target）
- Security/Privacy boundaries（按风险触发）

---

## 5) 验证与证据（不止正确性）

验证维度建议（按任务取子集）：
- Correctness（对照 AC）
- Failure modes（错误输入/缺资源）
- Performance/resource smoke（耗时/内存/吞吐）
- Docs/operability（文档可用、Runbook 可执行）
- Maintainability signals（复杂度、可读性、重复）

证据必须可定位：
- 命令 + exit code
- 产物路径（日志/报告/截图）
- 数据类型（real/sanitized-real/synthetic）与来源入口

---

## 6) 禁止项（边界与兜底）

默认禁止：
- 执行期擅自兜底/降级
- 用 synthetic 冒充真实验证覆盖
- 未授权进入执行（Level≥L2）
- 为了“看起来完成”偷换验收标准

需要兜底只能：
- Plan 阶段登记到 Fallback Register
- 写清触发条件/行为/代价/验证方式
- 获得用户确认后才允许落到实现

