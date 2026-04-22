> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Plan：<Project / Task Name>

Version:
Track:
WorkType:
Level:
Current Mode: Plan
Execution Authorization: not_received
Plan Owner:
Last Updated:

---

## 0. Template Notice

本模板仅供结构参考。实际 Plan 必须根据任务复杂度、用户材料、调研证据、架构设计与验证需求扩展，并在进入执行前清除所有占位符。

---

## 1. User Intent Lock

```yaml
primary_goal:
secondary_goals: []
must_preserve: []
must_avoid: []
non_goals: []
style_preferences:
quality_bar:
latest_user_feedback:
scope_boundary:
```

---

## 2. Problem Frame

### 2.1 一句话目标

### 2.2 背景

### 2.3 用户真正想解决的问题

### 2.4 成功后的状态

### 2.5 当前风险

---

## 3. Current State / Gap Analysis

---

## 4. Inputs and Materials Read

### 4.1 Code / Repository Map

### 4.2 Data / Examples / Logs

---

## 5. Research Log

### 5.1 Research Summary

### 5.2 Research Gaps

### 5.3 Facts That Changed the Plan

（建议结构化落盘）

| Query | Source (link) | Source type | Extracted facts | Impact on plan | Open questions |
|---|---|---|---|---|---|
|  |  | official/standard/paper/source-code/other |  |  |  |

---

## 6. Requirements

### 6.1 Functional Requirements

### 6.2 Non-functional Requirements

### 6.3 Documentation Requirements

### 6.4 Operations / Monitoring Requirements

---

## 7. Non-goals

---

## 8. Constraints and Boundaries

### 8.1 Allowed

### 8.2 Forbidden

### 8.3 Files / Areas Allowed to Modify

### 8.4 Files / Areas Forbidden to Access or Modify

### 8.5 Fallback Policy

### 8.6 Tech Stack / Versions / License Notes（当涉及第三方库/工具时强制）

- stack:
- versions:
- license & risk notes:

---

## 9. Candidate Solutions

### Option A：Conservative

### Option B：Recommended

### Option C：Long-term / Advanced

---

## 10. Architecture Decision

---

## 11. Technical Chain / Method Chain

要求：至少一张图（Mermaid/PlantUML/ASCII），明确端到端链路与失败恢复路径。

### 11.1 Pipeline Stages（阶段流水线：阶段→技术→验证）

要求：至少一张表，避免“流程/技术栈敷衍”。

硬门禁（L3 默认；外科手术型任务强制）：
- 阶段行数不得少于 8（建议覆盖：Preflight → Parse/Extract → Enrich → IR/DOM → Protect → Transform → Fit/Typeset → Erase/Rewrite → Restore → QA → Deliver）
- 外科手术型任务必须明确：功能层快照/恢复、坐标统一、渲染/几何/功能 QA、多渲染器抽检（按需）

| Stage | Goal | Inputs → Outputs | Candidate tech | Recommended tech | Key risks | Validation & evidence |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### 11.2 Workdir & Resume Strategy（断点续跑与失败页隔离）

- workdir layout:
- resume markers:
- partial failure policy:

### 11.3 QA Plan（可感知质量/交互功能/几何一致性）

- render QA (screenshots / visual diff):
- geometry QA (overflow/overlap/out-of-box):
- function QA (links/toc/jumps/forms/annotations):
- multi-renderer QA (when needed):
- report artifacts:

### 11.4 MVP → Production Roadmap（路线图）

- MVP:
- Beta:
- Production:

### 11.5 Gotchas / Pitfalls（最容易踩的坑）

- pitfall:
- prevention:

---

## 12. Specification

### 12.1 Data Model

### 12.2 Interfaces

### 12.3 State

### 12.4 Error Handling

### 12.5 Logging / Monitoring

### 12.6 Performance / Resource Targets

### 12.7 Security / Privacy

---

## 13. Development / Work Strategy

要求：写明采用的策略组合（例如 SDD(spec-d-d) + 行为锁定 + 原型验证 + 契约先行 + 可观测性优先），并明确每一项对应的验证与证据。

### 13.1 Strategy by Area

---

## 14. Acceptance Contract

（可直接引用 `AcceptanceContract.md`，或在此内联）

---

## 15. Validation Matrix

（使用 `templates/ValidationMatrix.template.md`）

---

## 16. Real Data Strategy

---

## 17. Risk Register

---

## 18. Fallback Register

（默认应为空；只有 Plan 阶段登记并确认的项才允许执行）

---

## 19. Documentation Plan

---

## 20. Milestones

---

## 21. Task Mapping

---

## 22. Ready-to-Execute Gate

（使用 `templates/PlanQualityGate.template.md` 自检；并写明未通过项与修复计划）

---

## 23. Resumption Block

（使用 `templates/ResumptionBlock.template.md`）
