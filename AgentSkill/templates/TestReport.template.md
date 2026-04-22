> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Validation Matrix 与证据门禁生成。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Test / Validation Report（验证报告）

Version:
Track:
WorkType（仅 Software）:
Level:
scope: checkpoint / milestone / final
data_type: real / sanitized-real / synthetic
Last Updated:

---

## 0) What Was Validated（验证范围）

- Covered:
- Not covered（and why）:

---

## 1) Data Acquisition Log（真实数据获取尝试）

> 当 data_type != real/sanitized-real 时必须填写：尝试了哪些入口、为什么不可用、风险是什么。

- Attempt 1:
- Attempt 2:

---

## 2) Environment（环境信息）

- OS:
- Python/Node/etc:
- GPU/Driver（如适用）:
- Key dependencies:

---

## 3) Commands / Actions（命令与动作）

| Command / Action | Exit code | Summary | Artifacts (logs/reports/screenshots) |
|---|---:|---|---|
|  |  |  |  |

---

## 4) Dimensions Covered（覆盖维度）

- Correctness:
- Spec & Consistency:
- Failure modes:
- Performance/resource smoke:
- Docs/operability:
- Visual/UX（按需）:
- Security/compliance（按风险触发）:

---

## 5) Result（结论）

- passed / failed / missing
- Fail criteria hit（if failed）:
- Residual risks:

