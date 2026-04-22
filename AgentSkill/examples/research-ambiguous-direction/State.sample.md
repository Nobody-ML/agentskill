# State（节选）— research-ambiguous-direction

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

## 0. 元信息

- 当前任务：把“方向模糊的研究想法”收敛为可验证/可复现的最小研究方案（MVE）
- Track：Research
- Level：L3
- 当前阶段：Plan → Execute → Validate

---

## 1. Memory（稳定事实）

- 允许联网检索：是
- 资源约束：单卡/可接受 2 小时内跑完最小实验
- 输出语言：简体中文（术语保留英文）

---

## 2. Decision Log（关键决策）

### DEC-001：先做最小可行实验（MVE），不直接追求 SOTA
- 决策：先验证核心假设是否成立，再扩展复杂实验。
- 证据：计划中的 AC-001/AC-002（见 Plan）

---

## 3. Progress（进度）

- 里程碑：
  - M1：明确 Research Question + Metrics + Baselines（done）
  - M2：实现并跑通 MVE（in_progress）

---

## 4. Risks & Assumptions

| ID | 类型 | 描述 | 影响 | 缓解措施 | 状态 |
|---|---|---|---|---|---|
| A-001 | 假设 | 核心改动能在小数据上体现趋势 | 方向可能不成立 | 先做 MVE + 明确失败判据 | open |

---

## 5. Evidence Index（证据索引）

### Research

- 实验ID：EXP-001 (MVE)
  - 环境：Ubuntu 22.04 / 1×GPU / Python 3.11
  - 数据：toy dataset v0.1（脚本生成）
  - 参数：seed=42, steps=500
  - 指标：accuracy / calibration error
  - 结果：待补
  - 复现方式：`python experiments/mve.py --seed 42 --steps 500`
