## State（节选）— software-pdf-layout-translation

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

---

# State（统一记忆与进度）

## 0. 元信息

- 当前任务/项目名：PDF Layout Translation（保排版翻译）
- Track：Software
- WorkType：Build
- Level：L3
- 当前阶段：Plan
- Execution Authorization：required

---

## 1. Memory（稳定事实）

### 1.1 用户意图锁（节选）

- must_preserve：
  - 页数、页面尺寸、背景/底色/插图不被破坏
  - links / toc / bookmarks / named destinations 尽量保留或可重建
  - 输出是新的 translated PDF，原 PDF 保留
- must_avoid：
  - 白底覆盖（背景可能非白）
  - 执行期擅自兜底/降级（兜底必须 Plan 阶段登记并确认）

### 1.2 数据与验证策略（节选）

- real-data-first：优先使用用户提供真实 PDF；其次仓库 fixture；最后才允许 synthetic，并需用户确认
- 验证节奏：checkpoint（每个 Task Group）→ milestone（端到端多 PDF）→ final（全验收矩阵）

---

## 2. Progress（进度与阻塞）

- 当前任务组：TG-PLAN（Deep Plan + Research + Spec）
- Next Action：
  1) 完成 Research Log（≥8 来源，含官方文档/源码/issue 证据）
  2) 完成 Pipeline Stages 表（阶段→技术→验证映射）
  3) 完成 Acceptance Contract + Validation Matrix
  4) 输出“请求授权”回执，等待用户单独回复 `开始执行`

---

## 3. Resumption Block（可续跑块）

```yaml
RESUMPTION_BLOCK:
  mode: Plan
  level: L3
  execution_auth: required
  current_task_group: TG-PLAN
  next_actions:
    - fill Research Log (>=8 sources)
    - fill Pipeline Stages mapping table
    - write AC + Validation Matrix
  blockers:
    - "Need real PDF sample(s) or fixture path(s)"
  evidence_index: []
```

