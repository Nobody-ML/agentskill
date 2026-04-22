> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Resumption Block（可续跑块）

```yaml
RESUMPTION_BLOCK_v0.3:
  mode: "Plan" # Plan | Execute | Validate | Review | Write | Repair
  track: "Software"
  work_type: "Build" # Build | Debug | Ops | -
  level: "L3"
  execution_auth: "required" # required | received | not_required | revoked | scope_changed
  current_task_group: "<Task Group name>"
  checkpoint_level: "checkpoint" # micro-check | checkpoint | milestone | final
  intent_lock_ref: "Plan.md#User-Intent-Lock"
  next_actions:
    - "<next action 1>"
    - "<next action 2>"
  blockers:
    - "<blocker (minimal input)>"
  last_evidence:
    - "<path/link>"
  risks:
    - "<risk>"
  forbidden:
    - "no unauthorized execution"
    - "no unplanned fallback"
```
