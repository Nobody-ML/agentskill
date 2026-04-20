# Task（节选）— research-ambiguous-direction

> 注意：本文件为演练包节选，仅用于展示工件格式与证据链，不是执行规范；实际任务必须以本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md` 为准。示例内容可改写、扩展或替换。

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
