# Review（示例输出）— software-greenfield

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

【Review】总分: 8.1/10 | 结论: PASS

## 证据（摘要）

- AC-001：`python -m mytool --help` exit 0（证据：State.sample.md#EvidenceIndex help.txt）
- AC-002：`pytest -q` 覆盖成功路径（证据：State.sample.md#EvidenceIndex test-2026-03-19.txt）
- AC-003：测试断言错误信息（证据：tests/test_errors.py::test_missing_field）

## 评分（节选）

- 正确性：8.5（契约覆盖）
- 设计与架构：7.5（模块边界清晰，但 config schema 可再收敛）
- 可维护性：8.0（错误类型集中，日志清晰）
- 测试与验证：8.5（关键路径+失败路径）
- 安全与鲁棒性：7.8（输入校验到位，暂无外部执行注入风险说明）

## 整改清单

### P0
- [ ] 无

### P1
- [ ] 给 config schema 增加更明确的字段约束与错误提示（减少用户试错）

### P2
- [ ] 增加一个“dry-run”模式，便于仅验证配置
