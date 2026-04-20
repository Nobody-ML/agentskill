# AgentSkill v0.1.0 — 任务清单（最小执行单元）

目录：`droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/`

任务状态：
- `[ ]` 待执行
- `[x]` 已完成
- `[~]` 进行中
- `[!]` 阻塞/需要用户决策

---

## 0. 需求对齐与准备

- [x] 0.1 明确输出语言与风格：简体中文（术语保留英文）
- [x] 0.2 明确目录组织：模块化 `SKILL.md + stages/* + templates/*`
- [x] 0.3 明确版本化方式：语义版本目录 `v0.1.0/Plan.md`、`v0.1.0/Task.md`
- [x] 0.4 明确记忆落盘：统一 `State.md`
- [x] 0.5 产出 `v0.1.0/Plan.md`（本版本规划）

---

## 1. 建立目录骨架（不填内容也要先落盘）

- [x] 1.1 创建 `AgentSkill/SKILL.md`（先写 YAML 头 + 目录树占位）
- [x] 1.2 创建 `AgentSkill/State.md`（从 `templates/State.template.md` 初始化）
- [x] 1.3 创建 `AgentSkill/stages/router/SKILL.md`
- [x] 1.4 创建 `AgentSkill/stages/brainstorm/SKILL.md`
- [x] 1.5 创建 `AgentSkill/stages/research/SKILL.md`
- [x] 1.6 创建 `AgentSkill/stages/plan/SKILL.md`
- [x] 1.7 创建 `AgentSkill/stages/execute/SKILL.md`
- [x] 1.8 创建 `AgentSkill/stages/validate/SKILL.md`
- [x] 1.9 创建 `AgentSkill/stages/review/SKILL.md`
- [x] 1.10 创建 `AgentSkill/stages/write/SKILL.md`
- [x] 1.11 创建 `AgentSkill/templates/Plan.template.md`
- [x] 1.12 创建 `AgentSkill/templates/Task.template.md`
- [x] 1.13 创建 `AgentSkill/templates/State.template.md`
- [x] 1.14 创建 `AgentSkill/templates/ReviewRubric-Research.template.md`
- [x] 1.15 创建 `AgentSkill/templates/ReviewRubric-Software.template.md`
- [x] 1.16 创建 `AgentSkill/templates/ReviewRubric-Writing.template.md`

验收：`AgentSkill/` 目录树与 `v0.1.0/Plan.md` 约定一致。

---

## 2. 先定模板（让流程有“落点”）

- [x] 2.1 完成 `State.template.md`：包含 Memory / Decision Log / Progress / Risks & Assumptions / Evidence Index
- [x] 2.2 完成 `Plan.template.md`：目标/非目标/输入材料/产出物/验收标准/里程碑/风险/验证方案
- [x] 2.3 完成 `Task.template.md`：分组任务 + 方框 + 每条任务的产出物/验收方式/依赖
- [x] 2.4 完成 Research 评分表模板（维度、评分标度、证据点、整改清单）
- [x] 2.5 完成 Software 评分表模板（含“兜底代码/无意义函数”检查项）
- [x] 2.6 完成 Writing 评分表模板（含“图示质量/风格贴合/引用来源”检查项）

验收：模板可直接复制填空；所有“完成/通过”字段都要求证据。

---

## 3. Router（渐进式披露的核心）

- [x] 3.1 在 `stages/router/SKILL.md` 定义 Track（Research/Software/Writing/Simple）判定表
- [x] 3.2 定义 Level（L0–L3）判定表 + 升级/降级规则（不确定时保守）
- [x] 3.3 定义风险门禁（敏感数据/破坏性操作/生产环境/学术诚信等）与“必须停下询问”的条件
- [x] 3.4 定义路由后的“下一步加载规则”（明确：只读哪个 stage 文档）
- [x] 3.5 定义写入策略：Simple/L1 可不写 Plan/Task；L2/L3 必须写 Plan/Task/更新 State

验收：给 4 个示例输入，Router 能唯一决定下一阶段。

---

## 4. Brainstorm（想法生成与需求对齐）

- [x] 4.1 定义进入条件：方向模糊/方案未定/需要选型与对比
- [x] 4.2 定义输出物：候选方案 2–3 个 + 取舍 + 推荐 + 需要补的关键信息
- [x] 4.3 定义“无AI味”的表达规则：少空话、用证据与约束说话
- [x] 4.4 定义与 Plan 衔接：Brainstorm 必须产出可写入 Plan 的结构化结论

---

## 5. Research（资料检索与证据管理）

- [x] 5.1 定义检索策略：关键词扩展、时间窗、可靠来源优先级
- [x] 5.2 定义引用规范：来源列表 + 关键结论对应来源 + 不确定标注
- [x] 5.3 定义“复现要素”检查表（实验环境/seed/数据版本/指标/基线/消融）
- [x] 5.4 定义 Evidence Index 写入规则（落到 State.md）

---

## 6. Plan（把复杂任务变成可执行）

- [x] 6.1 定义 Plan 的最小必填项与可选扩展项（分层）
- [x] 6.2 定义 Task 拆分粒度标准（最小执行单元、依赖、验收方式）
- [x] 6.3 定义“先计划后执行”的硬门禁（L2/L3）

---

## 7. Execute（按 Task 推进的执行规范）

- [x] 7.1 定义软件开发执行规范：深读现有代码→改动→最小回归→记录证据
- [x] 7.2 定义科研执行规范：最小可行实验→记录参数→保存结果→可复现脚本
- [x] 7.3 定义写作执行规范：先搭结构→逐段填充→插图→例子/代码可运行
- [x] 7.4 定义每轮迭代的 State 更新点（进度、阻塞、风险变化）

---

## 8. Validate（证据门禁）

- [x] 8.1 定义“完成声明”门禁：没有证据不得宣称完成
- [x] 8.2 定义软件验证最小集合（测试/类型检查/静态检查/手动走通）与如何选
- [x] 8.3 定义科研验证最小集合（重复实验/对照/ sanity check / 指标解释）
- [x] 8.4 定义写作验证最小集合（引用一致性、示例可运行、术语一致、图示可读）

---

## 9. Review（打分与整改）

- [x] 9.1 定义 Research/Software/Writing 三类评审入口与输出格式（绑定模板）
- [x] 9.2 定义整改清单优先级（P0/P1/P2）与返工规则（低于阈值必须回到 Plan）

---

## 10. Write（写作交付与图示规范）

- [x] 10.1 定义写作风格对齐步骤（受众/语气/长度/结构/必须图示）
- [x] 10.2 定义图示规范：Mermaid 为主；何时用表格/ASCII
- [x] 10.3 定义“无AI味”写作检查表（禁用口吻、去模板化套话）

---

## 11. 主 SKILL.md（总装与图示）

- [x] 11.1 写入总目录树与按需加载规则（只读必要 stage）
- [x] 11.2 补齐 4+ 张 Mermaid 图（总流程/路由/阶段门禁/工件关系）
- [x] 11.3 写入全局硬门禁（证据优先、风险停下、简单任务直达但最小验证）

---

## 12. 演练与自检（用例驱动）

- [x] 12.1 用例 A（科研模糊方向）：从 Router 跑到“可验证 idea”输出清单
- [x] 12.2 用例 B（科研 idea 审查）：给出评分与可执行修改建议
- [x] 12.3 用例 C（软件从零）：产出 Plan/Task，并给出最小验证与评审输出样例
- [x] 12.4 用例 D（写教程）：产出结构+图示要求+引用要求
- [x] 12.5 用例 E（简单脚本）：直达执行路径的最小输出规范

验收：每个用例都能明确落到“下一阶段要读哪个 stage + 需要哪些工件/证据”。
