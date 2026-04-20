# AgentSkill v0.2.0 — 项目级作战手册（规划）

版本：`v0.2.0`  
位置：`droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/`

---

## 1. 这次要解决什么问题（来自 v0.1.0 反馈）

你指出的三件事都成立：

1) **显得简略**：v0.1.0 更像“行军框架”，把阶段与工件搭出来，但缺少“工程门禁密度”与“可执行细则”。
2) **看不到软件工程参考资料**：v0.1.0 没有把 `Reference/` 里的材料提炼成可复用检查表，也没有在流程中挂接“何时查哪本”。
3) **逻辑没串起来**：缺少“阶段契约（输入/输出/退出）+ 状态机 + 工件流转规则”的硬连接，导致读起来像模块堆叠。

v0.2.0 的目标：把它从“框架”加厚成**项目级作战手册**，做到：
- 逻辑闭环：每一步都知道下一步是什么、要写什么工件、如何验收、何时返工。
- 参考资料可见：每条关键门禁/检查表都能指向 `Reference/.../*.md` 的章节或目录定位。
- 支撑大任务：提供里程碑/依赖/风险矩阵/验收契约/复现协议，并保持“渐进式披露”。

同时，把**软件工程的思想/意识/方法/架构**融入整体 skill：
- 思想（Engineering mindset）：用反馈与证据驱动，而不是“写完再看”。
- 意识（Complexity awareness）：复杂度是核心敌人；长期维护成本优先。
- 方法（Process & gates）：需求→验收→实现→验证→评审→迭代；每步都有门禁与返工规则。
- 架构（Architecture as decisions）：用 stakeholders/concerns/质量属性与 ADR 把取舍显式化。

---

## 2. 范围（Scope）

### 2.1 必做

0) **软件工程内化（贯穿全流程）**
   - 主 `SKILL.md` 增加：软件工程“工程观”总纲（学习/反馈/经验主义/复杂度管理/架构取舍/验证与复现）。
   - stages 中把工程方法写成可执行门禁：需求评分、Stakeholders & Concerns、质量属性、ADR、开发范式工具箱/验证矩阵、变更控制。
   - library 负责把 `Reference/` 提炼成可复用检查表（每条带来源定位），stages 只放索引与触发条件。

   本轮继续加厚（仍在 v0.2.0 内）：
   - 补齐 SWEBOK 设计/构建/质量/运维/维护的可执行清单并挂接到 stages
   - 加入论文写作工件（Literature Matrix / Paper Outline）并挂接到 research/write
   - 强化 State.template 的治理索引字段，保证 SSOT 不断链

1) **串联逻辑加厚（最高优先级）**
   - 在 `SKILL.md` 增加：全局状态机、阶段契约总表、工件流转不变量。
   - 在每个 `stages/*/SKILL.md` 增加：Stage Contract（输入/输出/工件更新/进入条件/退出条件/返工条件/返回用户条件）。

2) **引入 Reference → library（两层挂接）**
   - 新增 `AgentSkill/library/`（平铺结构）：把 `Reference/` 中的要点提炼成“可执行检查表”，每条都标注来源路径与章节。
   - stages 中只放“触发条件 + 索引”，不把长清单堆在 stages 里。

3) **大任务治理（仅 L3 或触发条件启用）**
   - 里程碑计划（Milestone Plan）
   - 依赖管理（Dependency Map / Matrix）
   - 风险矩阵（Risk Matrix）
   - 验收契约（Acceptance Contract：可测试断言 + 证据要求）
   - 复现协议（Repro Protocol：Research/Software/Writing 三类）

4) **新增 examples/ 四个端到端演练包**
   - 科研-模糊方向（从方向到可验证 idea）
   - 科研-idea 审查（打分+整改+证据）
   - 软件从零（架构→Plan/Task→实现→验证→评审）
   - 写教程（受众/结构/图示/引用→写作→验证→评审）

### 2.2 不做（避免无限膨胀）

- 不把所有学科知识（CUDA/物理/语言学）写成手册；只提供“研究/验证/复现”的通用治理框架。
- 不引入复杂自动化脚手架；以 Markdown 工件协议为核心。

---

## 3. 交付物（Deliverables）

### 3.1 目录目标态

```text
AgentSkill/
├── SKILL.md                      # 总架构 + 状态机 + 契约总表 + 索引
├── State.md                      # SSOT（记忆/决策/进度/风险/证据）
├── stages/*/SKILL.md             # 每阶段：契约 + 门禁 + 索引
├── templates/*                   # Plan/Task/State + Rubrics + 契约/复现模板
├── library/*                     # 从 Reference 提炼的检查表（带来源定位）
├── examples/*                    # 4 个演练包
└── v0.2.0/
    ├── Plan.md
    └── Task.md
```

### 3.2 新增/更新文件清单

- 新增：`AgentSkill/library/`（若干 md）
- 新增：`AgentSkill/examples/`（四个包）
- 新增：`templates/AcceptanceContract.template.md`（或等价嵌入 Plan 模板）
- 新增：`templates/ReproProtocol-*.template.md`（Research/Software/Writing）
- 更新：`SKILL.md`、`State.md`、所有 `stages/*/SKILL.md`、若干 templates

---

## 4. 关键设计：渐进式披露 + 大任务治理层

### 4.1 渐进式披露不变，但“契约更硬”

- Router 仍然只做最小判定（Track×Level×风险）
- 但从 v0.2.0 起：每个 stage 都必须写清“输入/输出/退出/返工”

### 4.2 大任务治理只在 L3 启用

触发条件（任一即可）：
- Level = L3
- 风险较高（不可逆/合规/生产/学术诚信）
- 依赖项多（外部资料/多模块/多验证面）

启用后强制要求：
- 进入 Execute 前：必须有验收契约（Acceptance Contract）
- 进入 Validate 前：必须能定位证据入口（Evidence Index）

---

## 5. 验收标准（Definition of Done）

### 5.1 串联逻辑
- [ ] 主 `SKILL.md` 含：状态机图 + 阶段契约总表 + 工件流转规则
- [ ] 每个 stage 文件都包含统一的 Stage Contract 段落

### 5.1.1 软件工程内化

- [ ] 主 `SKILL.md` 有“软件工程工程观”总纲，并与 stages/library/examples 有明确挂接
- [ ] 每个 stage 能回答：这一阶段在软件工程方法论中的角色是什么（需求/架构/设计/构建/测试/评审/写作/复现）

### 5.2 参考资料可见
- [ ] `library/*` 每条检查项都带来源定位（`Reference/.../*.md` + 章节/目录）
- [ ] stages 中有清晰索引：何时查 library 哪个文件

### 5.3 大任务治理
- [ ] templates 中有验收契约与复现协议模板
- [ ] stages/plan 明确：缺验收契约不得进入 Execute（L3）

### 5.4 examples
- [ ] 4 个演练包都包含：State/Plan/Task/Review/Evidence 示例片段
- [ ] 演练包能让读者“只看示例也能理解流程如何串起来”

---

## 6. 实施步骤（Milestones）

1) 串联逻辑：状态机 + 契约总表 + 每 stage 契约
2) library：从 `Reference/` 提炼检查表并挂接到 stages
3) 大任务治理：验收契约 + 复现协议模板 + 触发与门禁
4) examples：4 个演练包落盘
5) 自检：对照 DoD 做缺口扫描并补齐
