# Repro Protocol（Software）模板

> 注意：本模板仅提供参考结构，不是执行规范；实际输出必须遵循本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md`。模板与规则冲突时，以规则为准。

> 目的：任何“可用/修复/通过”的结论都能被他人复查。

---

## 1. 环境（Environment）

- OS：
- 语言与版本（Node/Python/Rust/...）：
- 包管理器与 lockfile：
- 必要系统依赖（如有）：

---

## 2. 安装与启动（Setup）

- 安装命令：
- 环境变量（列名，不写密钥）：
- 启动命令（如有）：

---

## 3. 验证集合（Verification Set）

最小要求：列出你实际运行过的命令与期望结果。

| 类型 | 命令 | 期望结果 | 证据入口 |
|---|---|---|---|
| test |  | exit 0 | State.md Evidence Index |
| lint/typecheck |  | exit 0 |  |
| manual |  | 观察到… |  |

---

## 4. 失败判据与回滚

- 失败判据：
- 回滚方式（如适用）：

---

## 5. Evidence Index 写入

把“命令 + exit code + 关键输出摘要 + 日志路径”写入 `State.md` Evidence Index。
