# State（节选）— software-greenfield

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

## 0. 元信息

- 当前任务：从零实现一个小型 CLI 工具（含测试与发布前验证）
- Track：Software
- Level：L3
- 当前阶段：Execute → Validate → Review

---

## 1. Memory（稳定事实）

- 约束：不引入重依赖；必须有最小测试；输出需可复查证据
- 风险：没有 CI 时，本地验证证据必须写入 Evidence Index

---

## 3. Progress（进度）

- M1：定义验收契约 AC-XXX（done）
- M2：实现核心命令（in_progress）
- M3：补测试与验证证据（pending）

---

## 5. Evidence Index（证据索引）

### Software

- command: `python -m pytest -q`
  - exit_code: 0
  - summary: 12 passed
  - artifact: logs/test-2026-03-19.txt

- command: `python -m mytool --help`
  - exit_code: 0
  - summary: shows usage and subcommands
  - artifact: logs/help.txt
