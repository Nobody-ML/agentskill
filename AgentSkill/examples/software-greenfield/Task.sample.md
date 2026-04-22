# Task（节选）— software-greenfield

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

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
