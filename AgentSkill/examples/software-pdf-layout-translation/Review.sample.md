# Review（节选）— software-pdf-layout-translation

> 重要说明：本示例仅用于展示结构，不代表实际输出的最低详细程度。  
> 实际输出必须依据当前任务的 Level、用户需求、Skill 规则、Plan Quality Gate、Validation Matrix 和 Acceptance Contract 生成。  
> 大型任务不得因为示例简短而简化 Plan、Task、验证或交付。  
> 示例字段可以扩展，不得擅自删除与用户需求相关字段。  
> 示例不是推荐的最终篇幅。L2/L3 任务应显著长于示例，并包含具体资料、证据、架构、任务、验证和恢复信息。

---

## Review Summary（示例）

- Track：Software
- Level：L3
- Decision：PASS with Notes（示例）
- Score：8.2 / 10

---

## Evidence Index（示例入口）

- Checkpoint TG-1：`reports/preflight-<ts>.json`，抽样页 bbox 对齐截图
- Checkpoint TG-4：`reports/overflow-overlap-<ts>.json` + `screenshots/`
- Milestone：`reports/milestone-<ts>.md`（多 PDF 汇总）
- Final：`reports/final-validation-<ts>.md`（AC 覆盖矩阵）

---

## Rubric（节选）

1) Plan Depth（2.0/2.0）
   - 有阶段→技术→验证映射；Research Log 有一手资料；风险与 fallback 清晰
2) Correctness & Function（2.0/2.5）
   - 输出可打开；links/toc 抽检可用
   - 仍需扩大“命名目标/页面标签/注释/表单”的覆盖面（P1）
3) Layout Quality（2.0/2.5）
   - 大部分页面不溢出、不重叠
   - 个别复杂多栏页仍需更强 fit 策略（P1）
4) Operability & Docs（2.2/2.5）
   - workdir/报告/断点续跑可用；文档清晰

---

## Defects（示例）

- P0：无
- P1：
  - 复杂多栏页出现少量溢出，需补更强的行距/断行策略与回退策略（必须走 Plan 的 Fallback Register）
  - named destinations / page labels 的验证覆盖不足：需要补一组真实 PDF 做功能层回归
- P2：
  - 报告中建议加入“多渲染器抽检”默认启用条件说明（减少误判）

