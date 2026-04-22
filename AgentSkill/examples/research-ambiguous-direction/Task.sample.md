# Task（节选）— research-ambiguous-direction

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

任务状态：`[ ]` 待执行 / `[x]` 已完成 / `[~]` 进行中 / `[!]` 阻塞

---

## 1. 规划

- [x] T-01 定义 RQ/Hypothesis/Metrics/Baselines
  - 关联验收契约：AC-001
  - 产出物：Plan.md#1 与 #8
  - 验收方式：Review 时检查定义与引用

- [~] T-02 实现并跑通 MVE（EXP-001）
  - 关联验收契约：AC-002
  - 产出物：experiments/mve.py + logs/exp-001/
  - 验收方式：可重复运行命令 + 指标输出

---

## 2. 验证与证据

- [ ] T-03 记录复现协议（Research）
  - 使用模板：`templates/ReproProtocol-Research.template.md`
  - 验收方式：State.md Evidence Index 能定位命令与日志
