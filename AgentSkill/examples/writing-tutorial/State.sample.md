# State（节选）— writing-tutorial

> 注意：本文件为演练包节选，仅用于展示工件格式与证据链，不是执行规范；实际任务必须以本 skill 的 `SKILL.md` 与对应阶段的 `stages/*/SKILL.md` 为准。示例内容可改写、扩展或替换。

## 0. 元信息

- 当前任务：写一篇“超详细教程”（含图示与可运行示例），并可复查来源
- Track：Writing
- Level：L3
- 当前阶段：Write → Validate → Review

---

## 1. Memory（稳定事实）

- 目标读者：软件工程新手
- 风格：大白话但技术严谨（少比喻）
- 必须包含：总览图 + 流程图 + 对比表

---

## 5. Evidence Index（证据索引）

### Writing

- 来源条目：
  - SWEBOK v4.0a Chapter 01/02/05（requirements/architecture/testing）
  - Modern Software Engineering Ch.4–7（iteration/feedback/empiricism）

- 图示清单：
  - 图1：学习路径总览（Mermaid flowchart）
  - 图2：验证门禁（Mermaid stateDiagram）

- 示例可运行性：
  - 示例路径：examples/demo.py
  - 运行命令：`python examples/demo.py`
  - 输出摘要：prints "OK"
