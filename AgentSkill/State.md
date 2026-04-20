# State（统一记忆与进度）

> 说明：这是该 AgentSkill 的长期状态文件。用于保存偏好、边界、关键决策、进度、风险与证据索引。

---

## 0. 元信息

- **当前任务/项目名**：AgentSkill（渐进式披露工作流）
- **Track**：Software
- **WorkType**：Build
- **Level**：L3
- **当前阶段**：Review（v0.3.0 收尾：门禁一致性审计 + 长任务续跑协议）
- **创建时间**：2026-03-19
- **最后更新**：2026-04-19

---

## 1. Memory（稳定事实）

### 1.1 用户偏好
- 输出语言：简体中文（术语保留英文）
- 文件结构：模块化（`SKILL.md + stages/*/SKILL.md + templates/*`）
- 版本管理：语义版本目录（`v0.1.0/Plan.md`、`v0.1.0/Task.md`）
- 记忆落盘：统一 `State.md`
- 打分标度：0–10（允许小数）
- 执行授权门禁：Level≥L2 默认停在 Plan Mode；仅当用户明确回复 `开始执行` 才进入 Execute/Write
- 执行授权口令：唯一口令为 `开始执行`；不接受同义句、近义句、上下文推断授权
- 验证数据：真实数据优先；脱敏样本计为 `sanitized-real`；缺真实样本需用户确认后才可用 synthetic
- Software 次级分类：WorkType=Build/Debug/Ops（不新增 Track）
- 返工门禁（偏好）：
  - 验证/测试不通过 → 必须复评
  - 总分 < 7.0/10 且验证不通过 → 必须返工并复评
  - 总分 < 7.0/10 但验证通过/或无验证可做 → 必须提醒用户，是否返工由用户反馈决定
- 图示：允许混用（Mermaid/PlantUML/ASCII），按场景选

### 1.2 约束与边界（不可违反）
- 禁止访问：`codex_gpt-5.2-xhigh/**`
- 禁止访问：`codex_gpt-5.4-xhigh/AgentSkill/**`
- 禁止访问：`droid_gpt-5.2-xhigh/AgentSkill/**`
- 上下文压缩/交接摘要：不等于任务结束；摘要后必须继续按 Plan/Task 与 State 的 Next Action 续跑（除非用户明确要求暂停或仅输出摘要）

---

## 2. Decision Log（关键决策记录）

### DEC-001：采用模块化渐进披露结构
- 时间：2026-03-19
- 决策：主 `SKILL.md` 只放总架构与路由入口；细则下沉到 `stages/*`；工件模板放 `templates/*`。
- 备选：单文件；helloagents 风格扩展
- 理由：可按需加载，避免一次性读完；便于后续迭代扩展。

### DEC-002：引入 library 与 examples，形成“作战手册 + 证据闭环”
- 时间：2026-03-19
- 决策：新增 `library/`（从 `Reference/` 提炼可执行检查表并标注来源定位）与 `examples/`（4 个端到端演练包），并在主 SKILL.md 加入状态机与阶段契约总表。
- 理由：解决“单薄/不串联/看不到参考资料影子”的问题，同时保持渐进式披露。

### DEC-003：L3 引入大任务治理层（验收契约 + 复现协议 + 依赖/风险）
- 时间：2026-03-19
- 决策：当 Level=L3 或风险触发时，Plan 必须包含依赖表与验收契约（AC-XXX），并要求复现协议模板可执行；Review 以“验证×评分”门禁决策返工。
- 理由：让大任务可验收、可复查、可复现。

### DEC-004：引入 Plan Mode 与执行授权门禁（Execution Authorization）
- 时间：2026-04-17
- 决策：Level≥L2 默认处于 Plan Mode；为避免误判，用户需**单独回复** `开始执行`（建议独立消息或独立一行）后才进入 Execute/Write，并要求授权记录落盘（time + scope）。
- 理由：把“先充分理解再执行”变成硬门禁，减少方向性返工与风险操作。

### DEC-005：Software 引入 WorkType=Build/Debug/Ops（不新增 Track）
- 时间：2026-04-17
- 决策：Track 保持 Software；额外以 WorkType 区分开发建设/诊断修复/运行维护（包含训练监控与长任务运行）。
- 理由：不同工作形态的验证点与交付物不同，用同一套套路硬套会导致遗漏。

### DEC-006：验证升级为真实数据优先（含 sanitized-real）
- 时间：2026-04-17
- 决策：Validate 强制标注 data_type（real/sanitized-real/synthetic）；Level≥L2 默认至少一次关键路径使用真实或脱敏真实样本；缺失真实样本时需用户确认后才可用 synthetic。
- 理由：避免在模拟数据上获得虚假安全感，把真实世界失败模式前置。

### DEC-007：交付报告与 Ops Runbook 成为一等工件
- 时间：2026-04-17
- 决策：交付阶段必须输出 Delivery Report；WorkType=Ops 时必须提供 Runbook（启动/停止/健康检查/观测点/阈值/排障），并将证据入口写入 Evidence Index。
- 理由：交付可复查、可运行、可维护；支持替用户执行/监控/排障的工作形态。

### DEC-008：长任务防漂移与上下文压缩续跑
- 时间：2026-04-19
- 决策：引入每轮启动协议（Anti-drift Boot）+ Mode 头回执 + Recovery Protocol；并增加“上下文压缩/交接摘要不等于结束”的续跑规则：摘要输出必须同时维护 Next Action 指针，且默认继续推进未完成任务（除非用户明确要求暂停或仅输出摘要）。
- 理由：解决长任务中“跑几轮忘规则/压缩后停机”的常见失控模式，保证可持续推进与可交接复跑。

---

## 3. Progress（进度与阻塞）

### 3.1 当前目标
- v0.3.0：Plan Mode 强化 + 多范式协同 + 真数据优先验证 + Ops/Monitoring + 交付报告格式统一。

### 3.2 里程碑
- M1：v0.1.0 规划与任务清单（done）
- M2：模板落盘（done）
- M3：stages 文档落盘（done）
- M4：主 SKILL.md（done）
- M5：用例演练与自检（done）

- v0.2.0：
  - M1：阶段契约 + 状态机（done）
  - M2：library（done）
  - M3：L3 治理模板（done）
  - M4：examples 四包（done）

---

## 4. Risks & Assumptions（风险与假设）

| ID | 类型 | 描述 | 影响 | 缓解措施 | 状态 |
|---|---|---|---|---|---|
| R-001 | 风险 | 需求覆盖面过大导致文档臃肿 | 可用性下降 | 通过 Track×Level 路由 + 渐进披露控制展开 | open |
| R-002 | 风险 | 返工门禁不清导致争议 | 迭代成本 | 把“验证门禁”与“评分门禁”分开写清 | open |

---

## 5. Evidence Index（证据索引）

### 5.1 已生成文件
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/SKILL.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/State.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/*/SKILL.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/*.template.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/library/*.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/diagrams/*.svg`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/examples/*`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.1.0/Plan.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.1.0/Task.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.2.0/Plan.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.2.0/Task.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.3.0/Plan.md`
- `droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.3.0/Task.md`
