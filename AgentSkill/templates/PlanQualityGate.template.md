> 重要说明：本模板仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为模板简短而简化 Plan、Task、验证或交付。  
> 字段可以扩展，不得擅自删除与用户需求相关字段。

# Plan Quality Gate（Ready-to-Execute 自检清单）

用途：
- 在请求执行授权前，做一次硬自检，避免 Plan 写得像摘要导致执行失控。

---

## 0) Gate Result

```yaml
gate: "G4 Plan Quality Gate"
status: "blocked" # pass | blocked | fail
blocking_items:
  - "<item>"
```

---

## 1) Plan 完整性

- [ ] 已写 User Intent Lock（primary_goal / must_preserve / must_avoid / non_goals）
- [ ] 已写当前差距（Gap Analysis）与失败样例（若有）
- [ ] 已写 Inputs and Materials Read（读了什么、结论、影响）
- [ ] 已写 Research Log（来源、事实、影响、Open questions）
- [ ] （需要外部事实时）Research Log 达到最低研究包：≥8 来源、≥3 一手资料、≥1 源码/issue 证据，并记录版本/日期

---

## 2) 架构与规格

- [ ] 已给候选路线并有推荐路线（含取舍理由）
- [ ] 已写 Architecture Decision（关键权衡与理由）
- [ ] 已画技术链路/方法链路图（端到端 + 失败恢复）
- [ ] 已给出“阶段流水线”与阶段→技术→验证映射表（避免流程/技术栈敷衍）
- [ ] 已写 Specification（接口/状态/错误语义/观测点）
- [ ] 已写 Tech Stack / Versions / License Notes（当涉及第三方库/工具/格式内核时强制）

---

## 3) 验收与验证（硬门禁）

- [ ] 已写 Acceptance Contract（AC-XXX 可验证）
- [ ] 已写 Validation Matrix（AC→验证→证据）
- [ ] 已写 Real Data Strategy（真实数据优先；缺失处理）
- [ ] 已写验证节奏（micro-check/checkpoint/milestone/final）
- [ ] （可感知质量/交互功能/格式保持类任务）已写 QA Plan（渲染/几何/功能/多渲染器）并定义证据产物

### 3.1 外科手术型任务加固（格式/交互/排版保持，命中即强制）

当任务属于“外科手术型”（例如 PDF 保排版翻译、保持链接/目录/书签/注释/表单、禁止白底覆盖）时，额外强制：

- [ ] 已写 Domain Preflight 规范（preflight.json 字段至少覆盖：加密/权限/签名、outline、links、forms、named destinations、page labels、附件/元数据风险）
- [ ] 已写坐标统一策略（含旋转页），并定义验证方式（bbox 可视化抽检/对齐证据）
- [ ] 已写功能层策略：快照→删除→重建（links/toc/bookmarks/named destinations/annotations/forms/page labels）
- [ ] 已写“链接锚点映射/热区重建”的生产级路线（token 保护 → typeset 记录 bbox → insert_link 重建）（MVP 可先做 links 统计，但必须写升级路径）
- [ ] 已写 Transform 结构化输出与缓存策略（例如：JSON schema + cache key + SQLite/JSONL 落盘），以支撑断点续跑与反复排版迭代
- [ ] 已写 Typesetting 分档能力（textbox/htmlbox → shaping 引擎），并定义 fit solver 的失败判据与重写策略（不能只靠无限缩字号）
- [ ] 已写中文/混排排版规则（禁则、标点避头尾、引用编号/单位/变量不可拆等），并说明如何在 QA 中检测
- [ ] 已写“扫描页/图片型页”的路线与门禁（inpainting/贴片/人工审校），并在 Fallback Register 中登记（如需要）
- [ ] 已写 redaction 细粒度策略（按行/按 span 生成矩形、排除公式/链接敏感区），并明确“redaction 可能移除重叠链接”的验证与修复路线
- [ ] 已写多渲染器 QA 抽检策略（至少 2 引擎按需抽检），并定义证据产物
- [ ] 已写数字签名的交付事实：译文版修改正文通常不保持原签名有效性（必须显式告知）

---

## 4) 边界与兜底

- [ ] Allowed/Forbidden 边界明确（含禁止访问目录）
- [ ] 允许修改的范围明确（路径/模块）
- [ ] Fallback Policy 明确：默认禁止；允许项已登记并获得确认

---

## 5) Task 映射

- [ ] Plan 已映射到 Task Group（每段对应哪些任务组）
- [ ] Task Group 都有 Checkpoint Validation
- [ ] 已写 Milestone/Final Validation 与 Final Review

---

## 6) 可续跑

- [ ] 已写 Resumption Block（Mode/Auth/Next Action/Blockers/Evidence）
- [ ] State.md 已更新 Next Action 与 Evidence Index
- [ ] （长任务/批处理/文件夹任务）已写 Workdir & Resume Strategy（断点续跑、失败页隔离、恢复标记）
