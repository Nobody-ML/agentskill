> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Execution Preflight（执行预检）

Version:
Track:
WorkType:
Level:
Task Group:
Planned Validation Level: micro-check / checkpoint / milestone / final
Execution Authorization: received
Date:

---

## 1) Authorization & Boundaries

- execution_auth_record_ref:
- allowed_paths:
- forbidden_paths:

---

## 2) Data Readiness

- data_sources:
- data_type: real / sanitized-real / synthetic
- data_acquisition_log_ref:
- missing_data_blockers:

---

## 3) Environment & Dependencies

- runtime:
- key dependencies:
- gpu/driver (if any):
- install / setup steps:

---

## 4) Commands to Run (Repro)

```bash
<commands>
```

---

## 5) Files to Change

- <path>

---

## 6) Risks & Rollback

- destructive_ops:
- backup_point:
- rollback_steps:

---

## 7) Observability

- logs:
- metrics:
- outputs:

---

## 8) Gate Result

```yaml
gate: "G6 Execution Preflight"
status: "pass" # pass | blocked | fail
why:
next_action:
```
