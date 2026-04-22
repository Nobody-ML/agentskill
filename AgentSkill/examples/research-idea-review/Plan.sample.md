# Plan（节选）— research-idea-review

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

Track：Research  
Level：L2

---

## 1. 目标（Goal）

一句话目标：对用户提供的 research idea 给出证据驱动的评分与可执行修改建议。

### 成功标准（验收）
- [ ] 输出 Review：总分 + 每维度证据/理由 + P0/P1/P2 整改清单
- [ ] 明确指出“哪些地方缺证据导致 BLOCKED/降分”，并给出最小补证据方案

---

## 5. 约束与边界

- 当前没有代码/数据/实验记录：只能做“方案层评审”，无法宣称效果

---

## 8. 验证方案（Validation Plan）

- 若 idea 的关键主张无法提出最小实验/对照/指标 → Review 结论应为 BLOCKED

（可选：补证据的落盘工件）
- Literature Review Matrix：`templates/Literature-Review-Matrix.template.md`
- Paper Outline：`templates/Paper-Outline.template.md`（若目标是论文/报告）
