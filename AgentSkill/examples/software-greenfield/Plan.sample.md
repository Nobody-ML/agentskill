# Plan（节选）— software-greenfield

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

Track：Software  
Level：L3

---

## 1. 目标（Goal）

一句话目标：从零实现一个 `mytool` CLI：读取配置并执行一个命令步骤，提供清晰错误信息，并有最小测试与证据。

### 成功标准（验收）
- [ ] CLI 基本可用（help/错误输入/成功路径）
- [ ] 最小测试集覆盖关键路径与失败路径
- [ ] Evidence Index 可定位验证证据

---

## 3. 产出物（Deliverables）

- 可执行 CLI（包/入口脚本）
- 测试用例
- 复现协议（Software）

---

## 6.3 Stakeholders & Concerns（节选）

- 用户/使用者：希望命令易用、错误提示可诊断
- 维护者：希望结构清晰、修改成本低
- 运行者：希望命令执行可预测，不产生隐藏副作用

---

## 6.4 Quality Attributes（节选）

Top attributes：
1) 可维护性（maintainability）
2) 可诊断性（diagnosability）
3) 可复现性（reproducibility）

Trade-off（示例）：
- 选择更严格的配置校验 → 更早失败（提升可诊断性），但需要更详细的错误信息维护成本

---

## 6.5 ADR（节选）

- ADR-001：配置校验策略（严格 schema vs 宽松解析）
- ADR-002：错误类型与返回码约定

---

## 7.1 依赖与前置条件（Dependency Map）

| 依赖 | 类型 | Owner/来源 | 获取方式 | 阻塞等级 | 备注 |
|---|---|---|---|---|---|
| Python 3.11+ | 外部 | 用户环境 | 已安装 | P0 | 版本过低需升级 |
| pytest | 外部 | PyPI | pip install | P1 | 默认要求安装；替代测试框架需用户确认并更新验证方案（写入 Decision Log） |

---

## 7.2 验收契约（Acceptance Contract）

| ID | 标题 | 行为断言（Pass/Fail） | 证据要求 | 负责任务 | 状态 |
|---|---|---|---|---|---|
| AC-001 | help 可用 | `mytool --help` 返回 0 并展示子命令 | 命令输出摘要 | T-01 | pending |
| AC-002 | 成功执行 | `mytool run config.yml` 返回 0 并执行目标命令 | 测试 + 手动命令输出 | T-02 | pending |
| AC-003 | 错误输入可诊断 | 缺参数/配置缺字段时返回非 0，并给出可读错误信息 | 测试断言错误信息 | T-03 | pending |

---

## 8. 验证方案（Validation Plan）

- 单测：覆盖 AC-001/002/003
- 手动：跑 `--help` 与一个最小配置示例

---

## 8.4 复现协议（Repro Protocol）

使用模板：`templates/ReproProtocol-Software.template.md`
