# Task：AgentSkill v0.3.0 Hardening

Version: v0.3.0  
Track: Software  
WorkType: Build  
Level: L3  
Execution Authorization: not_required  
Last Updated: 2026-04-20  

---

## Task Status Legend

- `[ ]` pending
- `[~]` in progress
- `[x]` done
- `[!]` blocked (needs input)

---

## Execution Rules

1) 每个 Task Group 内允许批量推进；到组末统一做 Checkpoint Validation 并落盘证据。
2) 规则与模板不得互相打架：protocols 为硬规则中心；stages 引用 protocols；templates 是落盘结构；library 是清单与解释。
3) 禁止把模板/示例当成实际输出下限；模板与示例只展示结构。

---

## 0. Preflight

- [x] 确认允许修改范围：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/**
- [x] 确认禁止访问目录已落盘到 State
- [x] 确认本版本目标与验收写入 v0.3.0 Plan

---

## 1. Task Group：Hard Gates & Protocols

### Tasks

- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/00-hard-gates.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/01-plan-mode-and-deep-plan.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/02-deep-reading-and-research.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/03-execution-preflight.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/04-validation-real-data-first.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/05-resumption-and-anti-drift.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/06-delivery-and-review.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/07-fallback-and-boundaries.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/08-long-running-ops.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/09-output-contracts.md
- [x] 新增 protocols：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/protocols/10-gotchas.md
- [x] 加固 protocols/02：外科任务研究清单（PDF/排版/签名/多渲染器等）

### Checkpoint Validation

- [x] 抽样通读 + 一致性审计：关键门禁无自相矛盾；内部引用检查通过

---

## 2. Task Group：Deep Templates & Gate Templates

### Tasks

- [x] 新增深模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/Plan.deep.template.md
- [x] 新增深模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/Task.deep.template.md
- [x] 新增模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/ValidationMatrix.template.md
- [x] 新增模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/PlanQualityGate.template.md
- [x] 新增模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/ExecutionPreflight.template.md
- [x] 新增模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/ResumptionBlock.template.md
- [x] 新增模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/ChangeControl.template.md
- [x] 新增模板：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/FallbackRegister.template.md
- [x] 加固 PlanQualityGate：外科任务专用检查项（签名/多渲染器/功能层快照等）
- [x] 加固 Plan.deep.template：Pipeline Stages 深度门禁（行数与必备阶段提示）
- [x] 加固 Task.deep.template：验证节奏解释（micro-check vs checkpoint）

### Checkpoint Validation

- [x] templates 顶部免责声明统一（模板只展示结构，不代表输出下限）

---

## 3. Task Group：Self-validation Scripts

### Tasks

- [x] 新增脚本：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/scripts/scan_forbidden_phrases.py
- [x] 新增脚本：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/scripts/validate_plan_task_quality.py
- [x] 新增脚本：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/scripts/validate_workflow_state.py
- [x] 加固 Plan/Task 质量门禁脚本：L3 Plan 必含 Pipeline/QA/Resume/Matrix，并检查阶段表行数

### Checkpoint Validation

- [x] 运行脚本并记录退出码与输出（写入 State Evidence Index）

---

## 4. Task Group：Stage Hardening (Protocol Hook-up)

### Tasks

- [x] stages/plan 增加必读协议与深模板引用：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/plan/SKILL.md
- [x] stages/execute 增加必读协议与预检模板引用：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/execute/SKILL.md
- [x] stages/validate 增加必读协议与验证矩阵模板引用：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/validate/SKILL.md
- [x] stages/review 增加必读协议与交付模板引用：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/review/SKILL.md
- [x] stages/write 增加必读协议与输出契约引用：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/write/SKILL.md
- [x] stages/research 增加必读协议与门禁引用：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/research/SKILL.md
- [x] stages/router 增加 gotchas 与恢复协议提示：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/stages/router/SKILL.md
- [x] Router：明确 PDF 保排版翻译属于外科任务（L3）典型例子

### Checkpoint Validation

- [x] 全局搜索/抽检 stages：协议引用路径正确且无断链（内部引用检查通过）

---

## 5. Task Group：Templates and Examples Disclaimer Unification

### Tasks

- [x] templates 全量顶部免责声明统一：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates
- [x] examples 全量顶部免责声明统一：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/examples
- [x] 新增深度示例包：software-pdf-layout-translation（Plan/Task/State/Review）

### Checkpoint Validation

- [x] 运行禁止短语扫描脚本确认无违规（排除 improvement 目录）

---

## 5.1 Task Group：Playbooks for Format Surgery (PDF)

### Tasks

- [x] 加固 PDF playbook：研究起步包 + 阶段→技术→验证基线表
- [x] 加固 PDF playbook：签名/低层对象工具（pikepdf/qpdf）与多渲染器 QA（pdfium/poppler）显式化
- [x] 加固 PDF playbook：扫描页路线（inpainting/贴片/人工审校）门禁化

### Checkpoint Validation

- [x] 人工抽查：playbook 已包含研究起步包 + 阶段映射基线 + QA/签名/低层对象门禁，可直接支撑高密度 Plan

---

## 6. Task Group：State & Traceability

### Tasks

- [x] State.md 增加 Next Action、Resumption Block 与 Gate Summary：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/State.md
- [x] State.template.md 增加 Resumption Block 与 Gate Summary：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/templates/State.template.md
- [x] traceability 增补 protocols/templates/scripts 的落点：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/library/traceability.md
- [x] library 索引补充 protocols 定位：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/library/00-index.md

### Checkpoint Validation

- [x] 人工抽查 3 条需求：可从 traceability 定位到唯一落点（Plan Mode/ExecAuth/Real Data）

---

## 7. Task Group：Main SKILL Navigation

### Tasks

- [x] 主 SKILL 增加 protocols/scripts 目录与协议加载地图：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/SKILL.md
- [x] 更新 v0.3.0 Plan 与 Task：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.3.0/Plan.md，droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.3.0/Task.md

### Checkpoint Validation

- [x] 运行 Plan/Task 质量门禁脚本并通过

---

## Milestone Validation

- [x] 运行 python3 droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/scripts/scan_forbidden_phrases.py
- [x] 运行 python3 droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/scripts/validate_workflow_state.py
- [x] 运行 python3 droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/scripts/validate_plan_task_quality.py

---

## Final Validation

- [x] 全局检查：禁止目录未被引用为可访问范围（rg 抽检）
- [x] 全局检查：协议/阶段/模板引用一致且无冲突（内部引用检查通过）

---

## Final Review

- [x] 生成 Delivery Report（按 templates/DeliveryReport.template.md）：droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/v0.3.0/DeliveryReport.md
- [x] 为 v0.3.0 给出评分与后续整改清单（写入 Delivery Report）
