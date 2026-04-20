# State（节选）— software-greenfield

> 注意：本文件为演练包节选，仅用于展示工件格式与证据链，不是执行规范；实际任务必须以本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md` 为准。示例内容可改写、扩展或替换。

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
