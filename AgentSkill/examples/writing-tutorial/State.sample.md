# State（节选）— writing-tutorial

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

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
