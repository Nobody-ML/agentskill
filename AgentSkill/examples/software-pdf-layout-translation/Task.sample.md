# Task（节选）— software-pdf-layout-translation

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

Track：Software  
WorkType：Build  
Level：L3  
Execution Authorization：required  

任务状态标记：
- `[ ]` pending
- `[~]` in progress
- `[x]` done
- `[!]` blocked (needs input)

---

## 0) Preflight（执行前必过）

- [ ] 确认 Execution Authorization=received（用户单独回复 `开始执行`，并已落盘 time+scope）
- [ ] 确认本轮只推进一个 Task Group，到该组 Checkpoint 为止
- [ ] 确认数据来源与 data_type（real/sanitized-real/synthetic）
- [ ] 记录将运行的命令与将修改的文件范围

---

## TG-1：Preflight & MinerU Adapter

### Tasks

- [ ] T1.1 定义 `preflight.json` schema（覆盖签名/加密/links/toc/page labels 等）
- [ ] T1.2 实现快速预检（PyMuPDF），输出风险与 route_decision
- [ ] T1.3 实现 MinerU adapter：记录版本/backend，输出 middle.json 解析摘要

### Checkpoint Validation

- data_type: real/sanitized-real
- commands: `tool preflight <pdf>` / `tool extract <pdf>`
- expected evidence: `preflight.json` + middle.json 统计 + 抽样渲染
- pass/fail criteria: preflight 完整；middle.json 可解析；抽样页 bbox 视觉对齐

---

## TG-2：Functional Snapshot & Layout DOM（IR）

### Tasks

- [ ] T2.1 快照 links/toc/bookmarks/named destinations/page labels（func_snapshot.json）
- [ ] T2.2 设计 Layout DOM schema（稳定 unit_id，支持断点续跑与缓存）
- [ ] T2.3 IR 构建：middle.json + rawdict 合并（坐标统一为 pt/top-left）

### Checkpoint Validation

- expected evidence: dom.json + schema 校验 + unit_id 稳定性抽检
- fail criteria: 坐标不一致/ID 不稳定/功能对象缺失

---

## TG-3：Translation Engine（结构化 + 缓存）

### Tasks

- [ ] T3.1 定义 JSON 输出 schema（单位粒度、token 保护、术语表策略）
- [ ] T3.2 实现缓存（SQLite/JSONL）与批处理重试策略
- [ ] T3.3 产出 sidecar：原文/译文对照（可复查）

### Checkpoint Validation

- expected evidence: cache 命中率统计 + 单页若干 block 翻译对照

---

## TG-4：Typeset/Fit Solver（不溢出、不重叠）

### Tasks

- [ ] T4.1 定义 fit 策略顺序（换行→字号搜索→行距→压缩改写）
- [ ] T4.2 实现 overflow/overlap 检测（几何 QA）
- [ ] T4.3 字体策略：CJK 字体覆盖、缺字处理

### Checkpoint Validation

- expected evidence: overflow/overlap 报告 + 抽样页截图（标注失败 bbox）
- pass criteria: 抽样页无明显溢出/重叠，且字号可读

---

## TG-5：Erase/Rewrite/Restore + QA Report

### Tasks

- [ ] T5.1 透明删除原文字（born-digital 路线）；扫描页按 Plan 路线处理
- [ ] T5.2 写入译文（textbox/HTML），并恢复 links/toc 等功能层
- [ ] T5.3 QA：渲染 diff + 功能抽检 + 多引擎抽检（按 Plan）
- [ ] T5.4 输出 translated PDF + report.html + sidecars

### Checkpoint Validation

- expected evidence:
  - 输出 PDF 可打开、页数/页面尺寸一致
  - links/toc 统计与抽样点击证据
  - report.html + screenshots
- fail criteria: 白底覆盖、功能对象显著丢失、溢出/重叠不可接受

---

## Milestone Validation（端到端多 PDF）

- [ ] 覆盖 2–3 个不同类型 PDF（论文/书籍/多栏/目录）
- [ ] 证据：命令、输出路径、report 汇总、失败页清单

---

## Final Validation

- [ ] AC 全覆盖（Validation Matrix 有证据入口）
- [ ] 残余风险与限制写入交付说明

---

## Final Review

- [ ] 打分（0–10）+ P0/P1/P2 缺陷清单 + 返工条目

