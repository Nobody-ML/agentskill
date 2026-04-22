# Changelog（AgentSkill）

本文件记录 AgentSkill 的版本演进摘要，便于长期维护与回溯。

格式：遵循“Added / Changed / Fixed / Notes”四段，尽量只写对使用者有影响的变化。

---

## v0.3.0 (2026-04-21)

### Added

- `improvement/plan-comparison_3-review.md`：对照 plan-comparison_3 的差距审查，并把差距落成可执行的 Skill 改动清单

### Changed

- `scripts/validate_plan_task_quality.py`：L3 强制 Research Log 条数与 URL 数，并对 PDF/外科任务追加关键概念门禁
- `templates/PlanQualityGate.template.md`：外科任务加固项补齐（链接锚点映射、结构化输出+缓存、分档排版与 fit solver、中文排版规则、redaction 细粒度策略与副作用）
- `library/pdf-layout-translation-playbook.md`：合并“目标 Plan”的关键要点（preflight schema、功能层快照与重建、坐标统一、DOM 数据结构、结构化翻译与缓存、排版分档与 penalty fit、redaction 粒度、QA 证据结构、工程模块 I/O、坑点清单）
- `examples/software-pdf-layout-translation/Plan.sample.md`：提升示例密度，避免示例过简带偏
- `stages/router/SKILL.md`：外科任务命中后默认强制 `Research → Plan`（除非 Research Gate 已满足且证据落盘）
- `stages/plan/SKILL.md`：Plan 质量自检阶段建议运行自检脚本；L3 Research Log 增加 URL 数门槛描述
- `stages/research/SKILL.md`：强化“来源必须可定位（URL/DOI/官方入口）”的落盘要求
- `protocols/02-deep-reading-and-research.md`：明确“用户未要求联网”不是跳过 Research Gate 的理由
- `protocols/10-gotchas.md`：新增调研 gotchas（L3 默认强制联网检索与可追溯来源）
- `v0.3.0/Plan.md`：补齐最小研究包（满足 L3 研究门禁与可追溯来源要求）

---

## v0.3.0 (2026-04-20)

### Added

- 协议层 `protocols/`：硬门禁状态机、Plan Mode 深度标准、真实数据优先验证、长程恢复、防兜底与降级、交付与输出契约、长任务运行等协议文件
- 外科手术型任务 playbooks：
  - `library/format-surgery-systems.md`（通用：阶段→技术→验证）
  - `library/pdf-layout-translation-playbook.md`（PDF：保排版翻译/功能保持）
- 深度示例包：
  - `examples/software-pdf-layout-translation/*`（外科任务：预检→IR→翻译→fit→写回→恢复功能→多维 QA）
- 通用标准库（让大任务 Plan 不再敷衍）：
  - `library/plan-quality-standard.md`（深计划质量标准）
  - `library/task-decomposition-standard.md`（Task 拆分标准）
  - `library/research-and-evidence-standard.md`（调研与证据标准）
  - `library/validation-real-data-first.md`（真实数据优先验证清单）
  - `library/software-engineering-operating-model.md`（通用工程作战模型）
  - `library/documentation-quality-standard.md`（文档交付质量标准）
  - `library/long-run-agent-operations.md`（长任务续跑与 Ops 作战手册）
- 深模板与门禁模板：
  - `templates/Plan.deep.template.md`
  - `templates/Task.deep.template.md`
  - `templates/ValidationMatrix.template.md`
  - `templates/PlanQualityGate.template.md`
  - `templates/ExecutionPreflight.template.md`
  - `templates/ResumptionBlock.template.md`
  - `templates/ChangeControl.template.md`
  - `templates/FallbackRegister.template.md`
- 自检脚本 `scripts/`：
  - 禁止短语扫描
  - Plan/Task 质量门禁校验
  - State 最小字段校验
- 补充模板（可选工件，服务长任务与证据落盘）：
  - `templates/ResearchLog.template.md`
  - `templates/DecisionLog.template.md`
  - `templates/TestReport.template.md`
  - `templates/ReviewReport.template.md`
  - `templates/FinalReport.template.md`

### Changed

- 主 `SKILL.md`：目录结构补齐 protocols/scripts；新增“协议加载地图”
- 各 stages：增加“必读协议”与关键模板引用，提升长期可执行性
- Router：对“格式/交互/排版保持”任务默认升级为 L3，并优先路由到 Research/Plan 深化
- templates 与 examples：顶部免责声明统一，明确“仅展示结构，不代表输出下限”
- `templates/Plan.deep.template.md`：新增 Pipeline Stages、QA Plan、Resume Strategy、Roadmap、Gotchas 等强制段落（解决流程/技术栈敷衍）
- `templates/PlanQualityGate.template.md`：外科任务加固项（签名/多渲染器/功能层快照/扫描页路线）
- `library/traceability.md`：新增协议/模板/脚本的需求落点追溯
- `State.md`：补齐 Next Action、Resumption Block、Gate Summary
- `scripts/validate_plan_task_quality.py`：L3 Plan 额外门禁（Pipeline/QA/Resume/Matrix）并做阶段表行数检查
- `library/pdf-layout-translation-playbook.md`：补齐研究起步包、低层对象工具（pikepdf/qpdf）、多渲染器 QA（pdfium/poppler）、扫描页路线门禁

### Fixed

- 修复“上下文压缩后停机”的规则缺口：恢复协议与 Resumption Block 成为一等工件
- 修复“模板/示例过简带偏”的问题：统一免责声明并强化 Plan/Task 门禁

### Notes

- improvement 目录为参考草案，不参与自检门禁

---

## v0.2.0 (2026-04-19)

### Added

- Track×Level 路由（Research/Software/Writing/Simple）
- stages 分阶段（router/brainstorm/research/plan/execute/validate/review/write）
- templates 与 examples 基础骨架
- State 记忆落盘与证据索引

---

## v0.1.0 (2026-03-19)

### Added

- 初始渐进式披露工作流骨架与版本目录（v0.1.0）
