# examples（端到端演练包）索引

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

目的：把“阶段模块”串成可直观看懂的闭环：State → Plan/Task → Execute/Write → Validate(证据) → Review(打分与返工)。

每个演练包都包含：
- State（节选）
- Plan（节选）
- Task（节选）
- Review 输出示例（总分 + P0/P1/P2 + 结论）
- Evidence Index 示例（证据入口）

---

## A) research-ambiguous-direction

科研方向模糊：从“方向”收敛到“可验证/可复现的最小研究方案（MVE）”。

- `research-ambiguous-direction/State.sample.md`
- `research-ambiguous-direction/Plan.sample.md`
- `research-ambiguous-direction/Task.sample.md`
- `research-ambiguous-direction/Review.sample.md`

---

## B) research-idea-review

科研 idea 审查：按评分模板给出证据、分数与整改清单；验证缺失则 BLOCKED。

- `research-idea-review/State.sample.md`
- `research-idea-review/Plan.sample.md`
- `research-idea-review/Task.sample.md`
- `research-idea-review/Review.sample.md`

---

## C) software-greenfield

软件从零：架构取舍 → 验收契约 → Task 拆分 → 实现 → 测试证据 → 评审。

- `software-greenfield/State.sample.md`
- `software-greenfield/Plan.sample.md`
- `software-greenfield/Task.sample.md`
- `software-greenfield/Review.sample.md`

---

## D) writing-tutorial

写教程：受众/结构/图示/引用 → 写作 → 可运行示例与引用验证 → 评审。

- `writing-tutorial/State.sample.md`
- `writing-tutorial/Plan.sample.md`
- `writing-tutorial/Task.sample.md`
- `writing-tutorial/Review.sample.md`

---

## E) software-pdf-layout-translation

PDF 保排版翻译（外科手术型任务）：预检 → 版面理解 → IR/DOM → 结构化翻译 → fit 排版 → 删除原文（透明）→ 写回译文 → 恢复功能层 → 多维 QA。

- `software-pdf-layout-translation/State.sample.md`
- `software-pdf-layout-translation/Plan.sample.md`
- `software-pdf-layout-translation/Task.sample.md`
- `software-pdf-layout-translation/Review.sample.md`
