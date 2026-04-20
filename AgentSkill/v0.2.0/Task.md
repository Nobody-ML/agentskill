# AgentSkill v0.2.0 — 任务清单（最小执行单元）

目录：`droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/`

任务状态：
- `[ ]` 待执行
- `[x]` 已完成
- `[~]` 进行中
- `[!]` 阻塞/需要用户输入

---

## 0. 版本准备

- [x] 0.1 生成 `v0.2.0/Plan.md`
- [x] 0.2 生成 `v0.2.0/Task.md`

---

## 1. 串联逻辑（最高优先级）

- [x] 1.1 在主 `SKILL.md` 增加“状态机（stateDiagram）”
- [x] 1.2 在主 `SKILL.md` 增加“阶段契约总表”（Router/Brainstorm/Research/Plan/Execute/Write/Validate/Review）
- [x] 1.3 在主 `SKILL.md` 增加“工件流转不变量”（State/Plan/Task/Evidence/Review 的约束）
- [x] 1.4 给每个 `stages/*/SKILL.md` 添加统一 Stage Contract 段落：
  - 输入 / 输出
  - 更新哪些工件（State/Plan/Task）
  - 进入条件 / 退出条件
  - 返工条件（BLOCKED/NEEDS_USER_DECISION）
  - 返回用户条件

验收：只读主 SKILL + 任意一个 stage，就能明确下一步和要产出的工件。

补强（软件工程内化）：
- [x] 1.5 在主 `SKILL.md` 增加“软件工程工程观（思想/意识/方法/架构）”与工程闭环图
- [x] 1.6 在主 `SKILL.md` 增加 SWEBOK 视角映射表（知识域 → stage → 工件）
- [x] 1.7 在 Router 增加“需求完整性快评”（<7 默认走 Brainstorm）
- [x] 1.8 在 Plan 增加 Stakeholders&Concerns、质量属性、架构描述、验证矩阵等 L3 方法门禁
- [x] 1.9 在 Execute 增加 开发范式工具箱/最小回归建议顺序
- [x] 1.10 在 Validate/Review 明确 `failed` vs `missing` 的门禁与用户决策路径
 - [x] 1.11 扩展 SWEBOK 映射：Design/Construction/Quality/Operations/Maintenance 的落点

---

## 2. 引入软件工程参考资料（library）

- [x] 2.1 新增目录 `AgentSkill/library/`
- [x] 2.2 生成 `library/00-index.md`（目录与使用方式：按触发条件检索）
- [x] 2.3 生成主题清单（每条含来源定位）：
  - requirements & acceptance（SWEBOK Requirements）
  - architecture & tradeoffs（Head First SA、SWEBOK）
  - complexity & modularity（Ousterhout、Farley）
  - iteration & feedback loops（Farley）
  - testing & verification（SWEBOK Testing、Farley）
  - documentation & writing（Ousterhout comments、Guidebook）
  - reproducibility（Research/Software/Writing 协议）
  - risk & security（SWEBOK Security + 通用风险门禁）

验收：每条检查项都能指到 `Reference/.../*.md` 的章节/目录。

继续加厚（SWE 覆盖面扩展）：
- [x] 2.4 新增 `library/design-construction.md`（Design/Construction 门禁）
- [x] 2.5 新增 `library/quality-operations-maintenance.md`（Quality/Operations/Maintenance 门禁）

---

## 3. 大任务治理层（L3）

- [x] 3.1 在 templates 新增 `AcceptanceContract.template.md`
- [x] 3.2 在 templates 新增 `ReproProtocol-Research.template.md`
- [x] 3.3 在 templates 新增 `ReproProtocol-Software.template.md`
- [x] 3.4 在 templates 新增 `ReproProtocol-Writing.template.md`
- [x] 3.5 更新 `templates/Plan.template.md`：加入里程碑/依赖/风险矩阵/验收契约/复现协议（分层：L2 可选，L3 强制）
- [x] 3.6 更新 `stages/plan/SKILL.md`：明确 L3 门禁（无验收契约不得进入 Execute）
- [x] 3.7 更新 `stages/review/SKILL.md`：把“验证×评分”门禁写成 if/then，并与模板一致

返工门禁细化：
- [x] 3.8 更新 Review Rubrics：把 `failed` 与 `missing` 分开（missing 需提醒并由用户决定）

架构与方法工件：
- [x] 3.9 新增 templates：Stakeholders&Concerns / Quality Attributes / ADR
- [x] 3.10 更新 Plan.template：加入 Stakeholders/质量属性/ADR 与架构描述入口
- [x] 3.11 更新 architecture-tradeoffs library：挂接新模板

---

## 4. examples（四个端到端演练包）

- [x] 4.1 新增 `AgentSkill/examples/_index.md`
- [x] 4.2 演练包 A：`research-ambiguous-direction/`
- [x] 4.3 演练包 B：`research-idea-review/`
- [x] 4.4 演练包 C：`software-greenfield/`
- [x] 4.5 演练包 D：`writing-tutorial/`

每包必须包含：
- State（节选）
- Plan（节选）
- Task（节选）
- Review 输出示例（总分+P0/P1/P2）
- Evidence Index 示例

继续加厚（Research/Writing 论文工件、Software 质量链路）：
- [x] 4.6 新增论文工件模板：Literature Review Matrix / Paper Outline
- [x] 4.7 在 research/write stages 挂接论文写作触发与门禁

---

## 5. 自检与收尾

- [x] 5.1 用 v0.2.0 DoD 清单逐条对照，补齐缺口
- [x] 5.2 更新 `State.md`：记录 v0.2.0 的关键决策与证据索引
