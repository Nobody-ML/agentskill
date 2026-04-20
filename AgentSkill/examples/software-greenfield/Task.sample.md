# Task（节选）— software-greenfield

> 注意：本文件为演练包节选，仅用于展示工件格式与证据链，不是执行规范；实际任务必须以本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md` 为准。示例内容可改写、扩展或替换。

- [~] T-01 实现 CLI 入口与 `--help`
  - 关联验收契约：AC-001
  - 产出物：src/mytool/__main__.py
  - 验收方式：`python -m mytool --help` exit 0；输出写入 Evidence Index

- [ ] T-02 实现 `run config.yml` 成功路径
  - 关联验收契约：AC-002
  - 产出物：src/mytool/run.py
  - 验收方式：单测 + 手动命令（证据写入 Evidence Index）

- [ ] T-03 实现错误输入与可诊断错误信息
  - 关联验收契约：AC-003
  - 产出物：src/mytool/errors.py
  - 验收方式：单测断言错误信息

- [ ] T-04 编写最小测试集
  - 覆盖：AC-001/AC-002/AC-003
  - 验收方式：`pytest -q` exit 0

- [ ] T-05 补齐复现协议（Software）
  - 使用模板：`templates/ReproProtocol-Software.template.md`
  - 验收方式：State Evidence Index 可定位所有命令证据
