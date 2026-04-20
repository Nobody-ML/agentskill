# 图形绘制规范（SVG / Diagram Style Guide）

> 目的：用统一、克制、可复用的视觉语言表达复杂系统，避免“PPT 风格噪音”。
>
> 本目录下的 SVG 资产用于在 Markdown 中引用，作为 Mermaid 图的“高质感版”呈现。

---

## 1) 核心设计理念（The Core Philosophy）

1. **克制原则（Restraint）**：饱和度收敛 80%，避免大红大绿、粗黑边框、硬直角与重阴影。
2. **呼吸感（Negative Space）**：留白是最高级的排列方式；节点之间不拥挤，文字与边框保持安全距离。
3. **格式塔闭合（Gestalt Grouping）**：用底色、虚线容器、轻量分组让系统自动降噪模块化。
4. **绝对规整（Absolute Alignment）**：像素级对齐、统一间距与统一圆角，体现工程严谨性。

---

## 2) 视觉参数规范（Visual UI Specifications）

### 2.1 色彩系统（Color System）

绝对避免：
- 纯黑 `#000000`
- 刺眼纯白背景 `#FFFFFF`
- 高饱和原色

推荐画布背景（Canvas Background）：
- 亮色：`#F8F9FA`（本仓库 SVG 默认）

主体填充色（Surface / Fill Colors）：
- 科技蓝（中立/基础/数据）：`#E8F0FE`
- 柔和绿（成功/通过/输出）：`#E6F4EA`
- 警示红粉（错误/重负荷）：`#FCE8E6`
- 活力黄橙（输入/外部/提示）：`#FEF7E0`
- 神秘紫（主控/抽象/决策）：`#F3E8FF`

边框色（Border Colors）：
- 默认：`rgba(0,0,0,0.15)`（SVG 中等价实现为 `stroke-opacity≈0.15`）

文本色（Typography Colors）：
- 主文本：`#1F2937`
- 次要文本：`#6B7280`

### 2.2 形状与容器（Shapes & Containers）

- **严禁直角**：节点圆角 `8px–12px`；大容器 `16px–24px`
- 分组容器：使用**虚线框**（dashed），可配极低透明度底色（≈5%）

### 2.3 字体与排版（Typography）

- 字体：优先无衬线（Inter/Roboto/Noto Sans SC）
- 层级：节点正文 14px；注释 12px；标题 16–18px
- 行高：1.4–1.6（多行文本不拥挤）

### 2.4 连线与路由（Lines & Routing）

- 首选**正交路由（orthogonal）+ 圆角拐点**（更接近 `reference.svg` 的“软转角”）
- 默认线色：`#6B7280` / `#9CA3AF`
- 线宽：`1.5px–2px`
- 箭头：极简小三角（不要粗重箭头）

### 2.5 箭头系统（Arrows: markers / padding / corner radius）【新增・重点】

> 本次发现的大多数问题都来自箭头：端点侵入节点、拐角过硬、路线互相穿插/重叠、箭头与文本打架。
>
> **目标**：把“箭头”当作一套可复用的设计系统，强制一致性与可读性。

#### 2.5.1 Marker 规范（Arrowheads）

- `orient="auto-start-reverse"`：保证方向永远正确
- `markerWidth/markerHeight`：`6`
- **refX 建议 `10`**（比 `reference.svg` 的 `9` 更保守）：让箭头尖端不会“刺进”目标节点
- 不要在同一条线同时出现 `marker-start` 与 `marker-end`（除非明确是双向关系）

#### 2.5.2 端点留白（Endpoint padding）

**硬规则**：所有带箭头的连线必须满足：
- 线段**起点**在 source 节点边界外至少 `8px`
- 线段**终点**在 target 节点边界外至少 `8px`
- 箭头尖端不得落在任何节点的 fill 区域内

推荐常量：
- `EDGE_PAD = 10px`（默认）
- 当节点间距很小（线段可见长度会 < 10px）时，允许降到 `EDGE_PAD = 6px`，但必须不侵入节点。

#### 2.5.3 圆角策略（Corner radius）

仅靠 `stroke-linejoin=round` 仍会显得“硬折线”。建议对 90° 转弯显式加圆角（与 `reference.svg` 一致）：

- 推荐转角半径：`R = 12px`（大图可用 `16px`）
- 典型“先水平后垂直”转弯模板：

```svg
<!-- 从 (x0,y0) 水平到 x1，再向下到 y2 -->
<path d="
  M x0 y0
  H (x1-R)
  Q x1 y0  x1 (y0+R)
  V y2
" />
```

- 典型“先垂直后水平”转弯模板：

```svg
<path d="
  M x0 y0
  V (y1-R)
  Q x0 y1  (x0+R) y1
  H x2
" />
```

#### 2.5.4 Lane（车道）与扇出（Fan-out）规则

当同一处需要多条箭头（例如 Router fan-out）：
- 先画 **trunk（主干）**，再分叉
- trunk 段尽量不加箭头（箭头只放在最终指向的末端）
- 分叉后的平行线必须走不同 lane，避免“箭头与箭头重叠”
- 推荐 lane 间距：`24px`（至少 `16px`）
- 避免两条线完全共线重叠；如果不可避免，至少保证它们在视觉上分层（虚线/颜色）并且不带箭头重复指向同一端点。

#### 2.5.5 分层顺序（z-order / layering）【避免箭头压住文本与节点】

强制渲染顺序（与 `reference.svg` 对齐）：
1) 背景网格
2) 分组容器（box-group）
3) **Edges / Routing（箭头与线）**
4) 线上的标注（edge labels / pills）
5) 节点（rect/circle）
6) 节点文本

> 目的：线永远在节点下方，不允许“箭头穿进节点把文字划掉”。

#### 2.5.6 线标注规范（Edge labels）

若需要在线上放文字（如 `PASS`、`L2/L3`）：
- 使用 `12px` 小字
- **必须加白底 pill**（`fill=#FFFFFF`, `opacity≈0.8`, `rx=6`），避免与 dot-grid 干扰
- 标注位置应在空白区，不压线拐角、不压节点边缘

---

### 2.6 箭头 QA Checklist（交付前必过）【新增】

每张图至少过一遍：
1. XML 可解析（无 `&` 等未转义字符）
2. 所有 `marker-end` 的终点不落在节点 fill 区域内（满足 `EDGE_PAD`）
3. 所有折线路由都使用圆角（`Q`）或等效的软转角效果
4. 不存在“箭头与箭头完全重叠”的共线段（允许 trunk，但 trunk 不带多重箭头）
5. 不存在“箭头与文本重叠/擦边”
6. edges 位于 nodes 下方（分层顺序正确）

---

## 3) 标准绘图工作流（S.O.P）

1. 先写文本大纲（层级/容器/并列模块/数据起终点）
2. 设定画布与网格（强制对齐）
3. 先灰白占位（不着色）
4. 语义化上色（同类同色）
5. 严谨连线（正交 + 解交叉）
6. 微调（间距/圆角/图注）
7. 眯眼测试（Squint Test）：主干链路是否仍清晰

---

## 4) 仓库约定（Conventions）

### 4.1 SVG 资产位置

- 所有 SVG 存放：`droid_gpt-5.2-xhigh_codex_gpt-5.2-xhigh/AgentSkill/diagrams/*.svg`

### 4.2 命名规则

- `agentskill-*`：主 SKILL 的图
- `router-*` / `brainstorm-*`：各 stage 的图
- `v0.1.0-*`：历史版本文档的图

### 4.3 Markdown 引用方式

在 Mermaid 代码块下方追加：

```md
**SVG（排版版）**：![](diagrams/<name>.svg)
```

在 stage 子目录中引用时使用相对路径：
- `stages/*/SKILL.md` → `../../diagrams/<name>.svg`
- `v0.1.0/*.md` → `../diagrams/<name>.svg`
