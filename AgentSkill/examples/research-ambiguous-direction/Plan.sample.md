# Plan（节选）— research-ambiguous-direction

> 注意：本文件为演练包节选，仅用于展示工件格式与证据链，不是执行规范；实际任务必须以本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md` 为准。示例内容可改写、扩展或替换。

版本：`example`  
Track：Research  
Level：L3

---

## 1. 目标（Goal）

一句话目标：把“提升 Agent 长任务可靠性”的模糊方向收敛为可验证/可复现的最小实验（MVE），并产出可执行下一步路线。

### 1.1 成功标准（验收）
- [ ] 给出 Research Question / Hypothesis / Metrics / Baselines
- [ ] MVE 可运行，且能输出指标与日志（可复现）

### 1.2 非目标（Non-goals）
- 不追求 SOTA
- 不做大规模分布式训练

---

## 2. 输入材料（Inputs）

- 用户方向描述（自然语言）
- 外部资料（允许联网）：近两年相关工作、常用评测设置

---

## 3. 产出物（Deliverables）

- 研究方案摘要（1–2 页）
- MVE 实验脚本与复现命令
- 证据索引（State.md Evidence Index）

（可选：论文/报告方向）
- Literature Review Matrix（相关工作矩阵）
- Paper Outline（论文结构）

---

## 7. 里程碑（Milestones）

- M1：问题定义与评测定义
  - 产出物：RQ/Hypothesis/Metrics/Baselines
  - 验证方式：可复述、可落盘到验收契约
- M2：MVE 跑通
  - 产出物：EXP-001 结果与日志
  - 验证方式：一键命令可重复运行

---

## 7.1 依赖与前置条件（Dependency Map）

| 依赖 | 类型 | Owner/来源 | 获取方式 | 阻塞等级 | 备注 |
|---|---|---|---|---|---|
| toy dataset | 内部 | 本项目 | 脚本生成 | P1 | 降低外部依赖 |
| GPU 资源 | 外部 | 用户环境 | 单卡即可 | P0 | 无 GPU 视为阻塞；替代路径（CPU/小模型）需用户确认并更新验收/成本（写入 Decision Log） |

---

## 7.2 验收契约（Acceptance Contract）

| ID | 标题 | 行为断言（Pass/Fail） | 证据要求 | 负责任务 | 状态 |
|---|---|---|---|---|---|
| AC-001 | RQ/指标/基线明确 | 文档中给出 RQ/Hypothesis/Metrics/Baselines，且各自定义清晰 | 文档片段 + 引用条目 | T-01 | pending |
| AC-002 | MVE 可复现 | `python experiments/mve.py ...` 可运行并生成日志与指标 | 命令输出摘要 + 日志路径 | T-02 | pending |

---

## 8. 验证方案（Validation Plan）

- 最小实验（MVE）：EXP-001
- 指标：accuracy / calibration error
- 失败判据：如果 MVE 无法稳定跑通或指标无定义，则结论 BLOCKED

---

## 8.4 复现协议（Repro Protocol）

使用模板：`templates/ReproProtocol-Research.template.md`
