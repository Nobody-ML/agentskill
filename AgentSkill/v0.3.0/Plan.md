# AgentSkill v0.3.0 — Plan Mode 强化 + 多范式协同 + 真数据优先验证 + Ops 能力（规划）

版本：`v0.3.0`  
位置：`droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/`  
语言：简体中文（术语保留英文）

---

## 1. 现状与缺口（v0.2.0 仍不满足的点）

对照你的 0.3.0 诉求，v0.2.0 的主要缺口集中在“**大任务的交互式对齐**”与“**执行/验证的强门禁**”两条主线上：

1) **Plan Mode 不够硬**
   - v0.2.0 有 Plan/Task 与阶段契约，但“Plan 写完就可能直接 Execute”的门禁仍然偏软。
   - 你要求：面对大任务（工程/科研）必须先充分理解（读材料/读代码/高质量检索/深度交互），在用户**单独回复**授权口令 `开始执行` 之前不能进入真实执行。

2) **交互方式仍可能发散**
   - v0.2.0 的 Brainstorm/Router 允许用“多选题”快速收敛，但没有把“提问强约束”写得足够硬：需要避免无休止让用户做选择的句式与分叉。

3) **开发范式存在“单点绑定”风险**
   - v0.2.0 在 Execute 更偏向把“测试先行/最小回归”作为默认路径，但你明确指出：只依赖一种范式危险且不准确。
   - 需要把“规范驱动、行为锁定、验收先行、原型验证、契约先行、可观测性排障”等放回工具箱，并给出多范式协同的选择依据（greenfield / legacy / research prototype / ops/debug）。

4) **验证缺少“真数据优先”的硬规则**
   - v0.2.0 Validate 强调证据门禁，但没有把“真实数据优先、无则用户确认后才模拟”写成硬门禁与决策树。
   - 你要求：测试不仅是正确性，还必须覆盖规范、性能、可读性等（至少作为验证/评审输入）。

5) **Ops/Debug/Monitoring 不是一等公民**
   - v0.2.0 的 Operations/maintenance 在 library 有提及，但没有把“替用户跑 debug/训练监控/长任务运行”写成可执行的工件协议与流程（Runbook、观察点、告警阈值、日志证据）。

6) **交付回执格式未统一为“可复查的交付报告”**
   - Review 有简洁输出格式，但你希望完成任务后要明确“做了什么”、输出格式固定、信息足够可复查，并且开发过程中配套文档必须非常详细。

7) **路径与边界引用存在不一致**
   - 部分 Plan/Task/State 仍引用旧输出路径（与当前输出目录不一致），导致跳转与引用混乱。
   - v0.3.0 统一为本目录路径，并把边界约束落到全局硬约束与 State 的 Memory。

8) **上下文压缩后可能“停机”**
   - 任务进行中出现“交接摘要/压缩总结”之类请求时，智能体容易把摘要当作收尾，导致未完成任务无法继续推进。
   - 需要把“摘要不是结束”写成协议：摘要必须带可续跑指针（Resumption Block），并默认继续推进未完成 Task（遵守执行授权门禁）。

---

## 2. v0.3.0 目标（你要的能力，写成可验收目标）

本版本目标是把 v0.2.0 的“作战手册”升级为可控的两相系统：

### 2.1 两相系统：Plan Mode → Execution Mode

**Plan Mode（对齐阶段）**
- L2/L3 大任务强制进入 Plan Mode：深读材料/代码 + 高质量检索 + 少而关键的交互提问。
- 在 Plan Mode 内只允许做三类动作：
  1) 阅读/整理材料（含仓库代码与用户文档）
  2) Research（必要时联网检索，来源可追溯）
  3) 产出/更新规划工件（Plan/Task/必要模板）
- **硬门禁**：用户未**单独回复**授权口令 `开始执行` 前，不得进入 Execute（不得修改目标代码、不得跑破坏性命令、不得进入长时间训练/监控）。

**Execution Mode（执行阶段）**
- 一旦用户授权执行：按 Task 列表持续推进，直到把 Plan/Task 中约定的内容完整跑完（除非阻塞或用户中断提出新需求）。
- 执行过程中持续落盘证据与进度（State），验证不通过必须回溯返工并复评。

### 2.2 多范式协同（从“唯一正确”变成“选择依据清晰”）

- 形成“开发范式工具箱”，并在 Execute/Plan 中给出选择规则：
  - SDD（Spec-Driven：先把需求写成可执行规范，再实现）
  - Characterization tests（接手/遗留代码先锁行为再改）
  - BDD（验收断言驱动，面向用户行为）
  - Prototype-first / Spike（科研与高不确定任务，先做最小验证）
  - Contract/Interface-first（边界清晰、多人协作/可替换实现）
  - Observability-driven debugging（先补可观测性，再定位问题）

### 2.3 验证策略升级：真数据优先 + 全维度质量验证

- Validate 引入硬规则：**真实数据优先**。
- 真数据不可得时：必须先向用户确认“确实没有可用真实数据/样本/日志”，才允许进入模拟数据验证，并在证据中明确标注“模拟”。
- 验证的覆盖面升级：
  - Correctness（对照验收标准）
  - Engineering compliance（开发规范/一致性/错误信息/边界）
  - Performance / resource（至少 smoke check，必要时基准）
  - Readability / maintainability（至少作为 Review 的评分输入）

### 2.4 Ops 能力：替用户跑、替用户盯、替用户排障

把“运行与诊断”写成工件协议与闭环：
- 明确 Runbook（启动/停止/参数/健康检查/常见失败模式）
- 明确观察点（logs/metrics/关键产物文件）
- 明确阈值与告警条件（例如训练 loss 不下降、OOM、性能退化）
- 明确证据落盘格式（State Evidence Index）

### 2.5 文档必须配套（工程交付的可读性保障）

- 对 Software/Research 交付也强制配套文档（按规模增减）：
  - 变更说明（What/Why/How）
  - 运行说明（Runbook）
  - 验证说明（命令/数据/结果摘要）

---

## 3. 范围（Scope）

### 3.1 必做（v0.3.0 必须落盘）

1) **引入“执行授权门禁”**
   - 新增全局概念：`Execution Authorization`（执行授权）
   - 默认：L2/L3 = 未授权（Plan Mode）
   - 授权后：进入 Execution Mode，并把授权记录落盘（Plan + State）

2) **更新 Router / Plan / Execute：写清 Plan Mode 的交互规则**
   - 明确：大任务必须先读材料/检索/交互对齐
   - 明确：提问必须少而关键，不得发散；每轮提问必须推动 Plan 收敛

3) **更新 Execute：多范式协同**
   - 把“单一默认路径”改为“优先规范驱动（Spec）+ 按场景选范式组合”
   - 给出选择表：新功能/修 bug/遗留系统/科研 spike/ops debug

4) **更新 Validate：真数据优先决策树**
   - 真数据来源顺序（用户提供 > 仓库样本 > 可采集日志 > 公开数据）
   - 无真数据必须用户确认后才能模拟
   - 证据中标注数据类型：real / sanitized-real / synthetic

5) **引入 Ops/Monitoring 工件与检查表**
   - 新增模板（至少一个）与 library 检查表
   - 在 Plan/Execute/Validate/Review 挂接触发条件

6) **统一交付回执格式**
   - 定义“交付报告（Delivery Report）”输出格式，覆盖：做了什么、改了哪些文件、如何验证、证据入口、风险与限制

7) **修正路径/禁区引用**
   - 全部文档统一为本目录路径（不再引用禁区目录）
   - 全局硬约束补齐禁区与输出位置

8) **上下文压缩/交接摘要续跑协议**
   - 摘要不是结束点：摘要输出必须携带 Resumption Block（任务组/检查点/Next Action/阻塞点/未完成项入口）
   - 默认摘要后继续推进未完成 Task（遵守执行授权门禁与 Plan/Task 契约）

### 3.2 不做（防止无限膨胀）

- 不把每个学科（CUDA/物理/语言学）写成手册：仍以“研究/验证/复现/工程治理”通用框架为主。
- 不引入复杂自动化脚手架：仍以 Markdown 工件协议为核心，必要时只补最小脚本/命令范式。

---

## 4. 交付物（Deliverables）

### 4.1 核心文件更新（必改）

- `AgentSkill/SKILL.md`：补齐 Plan Mode/Execution Mode 双相门禁 + 总览图更新
- `AgentSkill/State.md`：补齐执行授权记录字段、路径修正、v0.3.0 决策落盘
- `AgentSkill/stages/router/SKILL.md`：路由输出增加“是否需要执行授权确认”
- `AgentSkill/stages/plan/SKILL.md`：Plan Mode 交互规则 + 执行授权 gate
- `AgentSkill/stages/execute/SKILL.md`：多范式协同 + 一次性执行约束 + Ops 运行规则
- `AgentSkill/stages/validate/SKILL.md`：真数据优先 + 数据类型标注 + 性能/规范验证挂点
- `AgentSkill/stages/review/SKILL.md`：交付报告格式 + 返工规则更硬（验证失败必回溯重写/复评）

### 4.2 模板更新/新增（建议）

- 更新：`AgentSkill/templates/Plan.template.md`（增加执行授权段落、真数据声明、Ops/Runbook 段落）
- 更新：`AgentSkill/templates/Task.template.md`（增加执行授权任务、真数据验证任务、文档配套任务）
- 更新：`AgentSkill/templates/State.template.md`（增加 Execution Authorization、Ops 运行信息索引）
- 新增：`AgentSkill/templates/DeliveryReport.template.md`（统一交付回执）
- 新增（可选但建议）：`AgentSkill/templates/Ops-Runbook.template.md`（运行/监控/排障说明）

### 4.3 library 加厚（新增主题清单）

- 新增：`library/plan-mode-interaction.md`（少而关键的交互、问题收敛、避免发散）
- 新增：`library/development-paradigms.md`（多范式协同：选择表与适用条件）
- 更新：`library/testing-verification.md`（真数据优先 + 数据类型标注 + 性能/规范验证）
- 更新/新增：`library/quality-operations-maintenance.md`（扩展“监控/排障/长任务运行”的检查项）

### 4.4 图示（补齐 v0.3.0 差异点）

- 更新现有主流程图：增加 “Execution Authorization Gate（用户确认后才 Execute）”
- 新增 1 张图：Plan Mode ↔ Execution Mode 的门禁与回路（包含阻塞/返工路径）
- 新增 1 张图：Ops/Monitoring 闭环（Observe → Diagnose → Mitigate → Verify → Record）

---

## 5. 验收标准（Definition of Done）

1) **Plan Mode 门禁可执行**
   - [ ] 文档明确：L2/L3 默认停在 Plan Mode，必须等待用户单独回复授权口令 `开始执行`
   - [ ] 授权记录有落盘位置（Plan/State），可追溯时间与范围

2) **多范式协同明确且可落盘**
   - [ ] Execute 不再单点绑定单一范式；提供选择依据表与最小操作步骤

3) **真数据优先验证变成硬规则**
   - [ ] Validate 有决策树：优先真数据；无则用户确认后才模拟
   - [ ] 证据中明确标注数据类型（real/sanitized-real/synthetic）

4) **Ops/Monitoring 成为一等公民**
   - [ ] 至少 1 个 Runbook/Monitoring 模板或等价工件
   - [ ] Plan/Execute/Validate/Review 里有触发条件与落盘方式

5) **交付报告格式统一**
   - [ ] Review/交付阶段输出能稳定复查：做了什么、怎么验证、证据入口在哪里

6) **路径与边界一致**
   - [ ] 全部文档引用统一为本目录（不再出现禁区目录路径）

7) **上下文压缩可续跑**
   - [ ] 文档明确：交接摘要/压缩总结属于维护动作，不是任务完成
   - [ ] 摘要输出包含 Resumption Block（任务组/检查点/Next Action/阻塞点/未完成项入口），摘要后默认继续推进未完成任务（遵守执行授权门禁）

---

## 6. 实施步骤（Milestones）

1) 写清并落盘“执行授权门禁”（SKILL + Router + Plan + templates）
2) Execute 改为多范式协同（Execute + library）
3) Validate 真数据优先 + 全维度验证（Validate + library + templates）
4) Ops/Monitoring 工件与闭环（templates + library + diagrams）
5) 统一交付报告格式（Review + templates）
6) 路径修正 + v0.3.0 自检（对照 DoD 补齐缺口）
7) 上下文压缩/交接摘要续跑协议补齐（SKILL + library + templates + State）

---

## 7. 已决策事项（本版本默认锁定）

1) **执行授权口令/判定**
   - 规则：L2/L3 默认不执行；为避免误判，仅当用户**单独回复**授权口令 `开始执行`（建议独立消息或独立一行）才进入 Execution Mode。
   - 边界：不接受任何“同义句/近义句/上下文推断”的授权（例如“确认/继续/好的/收到”等均不视为授权）。

2) **“真实数据”的定义边界**
   - 建议定义：真实数据 = 来自真实系统/真实用户/真实数据源的样本（可脱敏）；合成数据 = 为测试临时编造/随机生成。
   - 规则：在 Software 任务中，“脱敏日志/真实请求样本”归类为 `sanitized-real`，属于真实数据验证范畴；`synthetic` 仅在用户明确确认“无可用真实样本（含脱敏样本）”且 Plan/State 已落盘时允许使用。

3) **Ops/Monitoring 的定位**
   - 建议：不新增 Track，仍归入 Software，但新增字段 `WorkType = Build | Debug | Ops`（写入 Router 回执与 State/Plan）。
   - 规则：采用 `WorkType` 作为次级分类，避免扩展 Track 导致分流复杂与文档膨胀。
