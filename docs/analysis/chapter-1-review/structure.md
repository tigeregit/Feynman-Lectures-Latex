# 第 1 章《原子的运动》结构 · 图注 · 编译 · 数字一致性专项审计

> 审校员：reviewer-struct（task-5）　日期：2026-11-02　分支：`feat/reading-efficiency`
> 范围：`Chapters/VolumeI/Chapter1.tex`（386 行）的 LaTeX 结构、10 张图与图注、编译链、全章数字一致性。
> **不在本报告范围**：逐句语义/译文风格审查（由四位分节审校员负责）；本报告对跨范围问题只在「存疑项」提示，不重复计入问题表。
> 依据：`docs/analysis/chapter-1-review/00-conventions.md`；英文对照以 `_attachments/build-feynman/audit/en/I_01.txt` 为主，图注参照官方页 <https://www.feynmanlectures.caltech.edu/I_01.html>（直连被 Cloudflare 403，经 `r.jina.ai` 文本代理取回；原始 HTML 规定 1–1…1–9 为 `caption empty`，1–10 有图注）。

## 0. 结论速览

| 审计项 | 结论 | 关键计数 |
|---|---|---|
| LaTeX 结构 | ✅ 基本合格；1 处孤儿 label | 27/27 对 NEW 标记；环境全部配对；10 label 全库唯一；14 ref 全部有定义；0 悬空引用；1 个 label 未被引用（图 1.7）；`\uwave` 52 处括号全平衡；全文件花括号净深度 0 |
| 图与图注 | ⚠️ 10/10 图内容与图注/正文相符；1 张图正文未引用 | 10 张图逐张渲染核查（含 4 张指定关键图 read_image 抽查）；图号顺序与引用顺序一致（1→6→8→10，缺 1.7）；无中英标题重复（内嵌英文标题在 CropBox 外，成品不显示） |
| 编译 | ✅ 可编译、无致命错误 | 连编 2 遍：14 页 A4；0 error / 0 overfull / 0 underfull / 0 Missing character；5 条无害 warning；SimSun 提示为字体探测子进程噪音（**非 error**），可用 `-no-mktex=tfm` 完全消除 |
| 数字一致性 | ✅ 关键数字全部正确；1 处化学名格式；1 处跨范围语义 | 核对 29 项：27 项一致；化学名 `4-(` 缺连字符（低）；L343「一个氧原子」英文为 one hydrogen（语义，转 §1-4）；NEW 概念图 10⁻¹³ cm 数量级正确但原文无此内容 |

问题总计 **10 条**：高 0 / 中 2 / 低 8。

---

## 1. LaTeX 结构审计

### 1.1 检查项与结果

| 检查项 | 方法 | 结果 |
|---|---|---|
| `%<<<NEW` / `%>>>NEW` 配对 | 逐行扫描 + 栈配对 | **27 对**（第 3/18/28/33/38/50/63/68/78/91/100/112/117/137/206/213/236/241/253/270/283/294/317/334/349/353/377 行开，16/20/30/35/40/52/65/70/87/93/102/114/119/170/208/222/238/243/255/272/285/303/319/336/351/355/386 行闭），顺序正确、无交叠 |
| 环境配对 | 正则统计 begin/end | `itemize` 8/8、`enumerate` 1/1、`summarybox` 4/4、`conceptmap` 1/1、`tikzpicture` 1/1、`optional` 1/1、`wrapfigure` 9/9、`figure` 1/1，**全部配对** |
| label / ref | 全库 grep + 逐条比对 | 10 个 `\label`（全库无重名）；14 次 `\ref` 全部指向已定义 label；**0 悬空引用**；`figure:食盐的晶体结构` **0 次引用（孤儿）** |
| 宏参数 | 逐宏花括号/参数检查 | `\chapterintro`×1、`\readingpath`×1、`\runin`×8、`\term`×10、`\keyidea`×5、`\aside`×1、`\fighint`×2、`\figsource`×1、`\uwave`×52；全部参数完整，全局花括号净深度 0；`\fighint`/`\figsource` 均位于 NEW 标记内 |
| 数学模式 | 逐行 `$` 计数 + 渲染核对 | 全部成对；`$\mathrm{CO_2}$`→CO₂、`$\mathrm{O{=}C{=}O}$`→O=C=O 渲染正确（`{=}` 抑制关系符间距，写法正确） |
| 化学式 | 渲染检查 | 本章未用 `\chemfig`；`\mathrm{...}` 化学式写法与渲染均正确（化学式内容问题见 §2） |
| 图号与引用顺序 | 按行号排序 | 正文引用顺序 1.1(110) → 1.2(135) → 1.3(180) → 1.4(196/202) → 1.5(234/247) → 1.6(268/275) → **1.7（无）** → 1.8(313/315) → 1.9(339) → 1.10(363)：升序正确，仅缺 1.7 |
| wrapfigure 方向与排版 | 编译 + 逐页渲染 | 9 个 wrapfigure：`r,r,l,r,r,r,r,l,r`；2 个 `l`（图 1.3、1.9）均落在偶数页外侧，合理；无浮动警告、无溢出、无图文重叠（14 页逐页目检） |
| OCR 排版痕迹 | 正则扫描（半角标点、空格、Å/度分秒写法） | 半角句点 1 处（L26）；全角标点旁多余空格 12 处 + 宏间断空格 1 处；`\r{A}` 与字面 `Å` 混用；`105°3'` 用 ASCII 撇号（详见 §1.2） |

### 1.2 问题表格

| # | 行号 | 严重度 | 类型 | 中文原文（≤30 字，必要时标出问题处） | 问题说明 | 英文依据（≤25 词原文引用） | 建议改法 |
|---|---|---|---|---|---|---|---|
| 1 | L26 | 中 | 标点 | "掌握这些定律也是颇为困难的**.。**因此……" | OCR 残留：半角句点与全角句号连用；成品 PDF 中可见"困难的.。"（已用 pdftotext 复核 p.2），读者需停顿猜测，属明显排版痕迹 | "Even so, the laws are so hard to grasp" | 删去半角句点，作"掌握这些定律也是颇为困难的。" |
| 2 | L131 | 低 | LaTeX/结构 | "厘米，**$ 10^{-8} $**厘米现在称为1Å" | 行内数学模式内有多余空格（`$ 10^{-8} $`），成品中公式前后间隙偏大；同句 `$1\sim2\times10^{-8}$` 写法正常 | "Now 10−8 cm is called an angstrom" | 改为 `$10^{-8}$` 厘米 |
| 3 | L131、L135、L163 | 低 | LaTeX/结构 | "半径为**$1\sim2$\r{A}**"；"距离是**0.957Å**" | 同一物理量两种写法：`\r{A}`（L131、L163）与字面 `Å`（L131 的"1Å"、L135 的"0.957Å"）混用；全库未使用 `\AA`，第 5 章等其它章用字面 `Å`，本章写法不统一 | "1 or 2 angstroms (Å) in radius" | 统一为字面 `Å`（改 L131、L163 两处 `\r{A}`） |
| 4 | L135 | 低 | 标点/排版 | "实际上，这个角是**105°3'**，氢原子中心……" | 分/秒符号用 ASCII 撇号 `'`，成品中被渲染为右单引号"’"；eFLP 原文用 prime（′） | "In actual fact the angle is 105∘3′" | 改为"这个角是 $105^{\circ}3'$"（或用 `105°3′`） |
| 5 | L352 | 低 | 数字/量纲 | "比较完整的名称是**4(2, 2, 3, 6-**四甲基-5-环己烯基)-3-丁烯-2-酮" | 化学名在定位号 4 之后缺连字符（英文为 `4-(`）；括号内数字/位次（2,2,3,6-四甲基、5-环己烯基、3-丁烯-2-酮）均正确 | "4-(2, 2, 3, 6 tetramethyl-5-cyclohexenyl)-3-buten-2-one" | 改为"4-(2, 2, 3, 6-四甲基-5-环己烯基)-3-丁烯-2-酮" |
| 6 | L371 | 低 | 标点 | "……不能从这些生物是用**} \uwave{**服从物理定律……" | 两个相邻 `\uwave` 之间多一个空格；成品 PDF 中该处下划线断开并出现可感空隙（已渲染核对 p.13），原文应为连续下划线 | ——（无对应英文；属原文下划线断行残留） | 删去 `}` 与 `\uwave` 之间的空格（保留两个 `\uwave` 以维持 52 处计数） |
| 7 | L26、L31、L46、L94、L133、L198、L258、L273、L292、L371（12 处） | 低 | 标点 | 如 L26"加以浓缩**。 **这就是说"；L31"基本定律**， **然后"；L94"称呼都行**）： **\keyidea{" | 全角标点后残留 ASCII 空格（OCR 痕迹）；因 xeCJK 忽略汉字间空格，成品 PDF 中基本不可见（L371 宏间空格除外），但影响源码整洁与纯文本/OCR 复用 | ——（排版问题，无英文依据） | 删除这些空格（共 12 处，行号见表内清单） |
| 8 | L279–288（label 在 L287） | 中 | 图文 | "……**\label{figure:食盐的晶体结构}**"（图 1.7） | 图注存在但正文从未 `\ref` 该图（成品 PDF 中"图 1.7"只出现于图注）；英文在"严格地说……"之前有一句点明图 1.7 的话，中文漏译该句，导致图成为"孤儿图" | "Figure 1–7 is an illustration of the three-dimensional structure of common salt, sodium chloride." | 仅标注：建议由 §1-3 语义审校员确认补译该句并在句中加 `\ref{figure:食盐的晶体结构}`；若暂不补译，至少在图 1.7 所在段落加一处 `\ref` |
| 9 | L282–286（图 1.7 内容） | 低 | 图文 | 图注"食盐的晶体结构（读图提示：大球为氯离子、小球为钠离子……）" | 图内附有一张数据表：岩盐 NaCl 5.64 Å、钾钠盐 K–Cl 6.28 Å、AgCl/MgO/PbS/PbSe/PbTe 等；本章正文完全未涉及这些数据；表中"钾钠盐"（KCl）疑为"钾石盐"（sylvite）之误。图与本图注所述 NaCl 三维结构相符，但图内容超出正文语境 | 正文只有 "the three-dimensional structure of common salt, sodium chloride"（无数据表） | 仅标注：需上游确认图源（eFLP 该图由两幅 SVG 组成，疑为"表+图"两部分；若确为原图重绘，建议把"钾钠盐"改为"钾石盐"并在图注加一句"表中另列同结构晶体数据"） |
| 10 | L357–362（图 1.10） | 低 | 图文 | 图注"α鸢尾酮香料的分子结构图" | 图源 271×145 pt，按 `width=0.4\textwidth` 排入仅约 64 mm 宽，图中 CH₃/H/O 等原子符号约 5–6 pt，明显小于正文；英文原书该图为整栏宽度 | "Fig. 1–10. The substance pictured is α-irone." | 仅标注，建议将 width 提到 0.5–0.55\textwidth（wrapfigure 宽度同步调整） |

> 说明：#7 的 12 处空格所在行：L26×2（"浓缩。 这就是""定律}。 不过"）、L31（"定律， 然后"）、L46（"鉴定者}。 但是"）、L94×2（"都行）： \keyidea""运动着。} 当彼此"）、L133（"吸引。 如果"）、L198（"跑去， 因而"）、L258（"水面时， 则"）、L273（"地说， 这种"）、L292（"溶解， 但是"）、L371（"原子做的}。 换句话说"）。

---

## 2. 图与图注审计

### 2.1 图注对照表（10 行）

> 「英文官方图注」栏：eFLP 网页（<https://www.feynmanlectures.caltech.edu/I_01.html>）中 Figure 1–1…1–9 的图注为**空**（原始 HTML 为 `<div class="caption empty">`，仅显示 Figure 1–N），1–10 的图注为 "The substance pictured is α-irone."。中文图注对应的是原书图题（中文版图题），原书英文图题可从图源 PDF 内嵌英文标题得到佐证（见"图内英文标题"列）。

| 图号（PDF 页） | 中文图注（含 NEW 读图提示） | 英文官方图注 / 原书图题 | 判断 |
|---|---|---|---|
| 图 1.1（p.4） | 放大10亿倍的水（读图提示：黑点氧、白点氢，每两个氢连一个氧；画面是二维理想化的） | eFLP：空（仅 Figure 1–1）；图源内嵌英文标题 **WATER MAGNIFIED ONE BILLION TIMES** | ✅ 准确。数值（10 亿倍）、颜色约定（黑=O、白=H）与正文一致；每 O 连 2 H 与正文一致；"idealized in several ways" 由读音提示（二维理想化）+ 正文 L112–119 三点理想化（边缘、二维、动态）覆盖，图注本身不重复该句可接受 |
| 图 1.2（p.5） | 水蒸气 | eFLP：空；内嵌英文标题 **STEAM** | ✅ 准确。图中为 2 个完整 + 1 个半截水分子（对应正文"两个半或三个"），120° 画法与正文一致 |
| 图 1.3（p.6） | 汽缸 | eFLP：空；无内嵌标题；英文正文 "a standard vessel for holding gases (used in all textbooks), a cylinder with a piston in it" | ✅ 基本准确，信息偏少：图中活塞是主要构件，图注"汽缸"未体现；建议图注改"配有活塞的汽缸"（与 label 名一致）——低（仅建议） |
| 图 1.4（p.7） | 冰 | eFLP：空；内嵌英文标题 **ICE** | ✅ 准确。图中六方对称、60° 旋转回原位、多"孔"结构与正文一致；二维示意图性质由正文说明 |
| 图 1.5（p.8） | 空气中水的蒸发 | eFLP：空；无内嵌标题；英文正文 "Figure 1–5 shows the surface of water in air" | ✅ 基本准确（图为空气中的水面及其上方的水蒸气/O₂/N₂；"蒸发"是过程概括）；图例"氧/氢/氮"与正文一致；可接受 |
| 图 1.6（p.9） | 盐在水中的溶解 | eFLP：空；无内嵌标题；英文正文 "a solid dissolving in water"（法文版图题 "Sel se dissolvant dans l'eau"） | ✅ 准确。图例"氯（大）/钠（小）"与正文离子描述一致；水分子氢端朝氯离子、氧端朝钠离子的细节与正文相符 |
| 图 1.7（p.10） | 食盐的晶体结构（读图提示：大球为氯离子、小球为钠离子；两套格点交错，没有独立的"食盐分子"） | eFLP：空；英文正文 "Figure 1–7 is an illustration of the three-dimensional structure of common salt, sodium chloride." | ⚠️ 图注欠完整（缺"三维""氯化钠"）；内容与正文相符（NaCl 立方格点、d=a/2、两套格点交错；大球=Cl、小球=Na 与表头 ●Na/○Cl 及离子半径一致）。**但正文未引用该图（问题 #8），且图内含数据表（问题 #9）**；图注可改"食盐（氯化钠）的三维晶体结构" |
| 图 1.8（p.11） | 碳在氧气中的燃烧 | eFLP：空；内嵌英文标题 **CARBON BURNING IN OXYGEN** | ✅ 准确。图中白色球=碳（底部碳晶体堆）、黑色球=氧（O₂ 为双黑对、CO 为黑白对），与正文"碳在氧气中燃烧"一致 |
| 图 1.9（p.12） | 空气中的紫罗兰香气分子 | eFLP：空；内嵌英文标题 **ODOR OF VIOLETS**；英文正文 "a picture of the air in the neighborhood of a violet" | ✅ 准确（中文补"空气中"与正文一致）。图中含 N₂（斜线）、O₂（黑）、水蒸气（黑白小球）与一个由 C/O/H 组成的复杂"怪物"分子，与正文相符 |
| 图 1.10（p.13） | α鸢尾酮香料的分子结构图 | eFLP：**"Fig. 1–10. The substance pictured is α-irone."**；图内无标题 | ✅ 准确。图中为六元环 + 2,2,3,6-四甲基 + 5-环己烯双键 + 3-丁烯-2-酮侧链（C=C–C(=O)–CH₃），即 α-鸢尾酮；中文补"分子结构图""香料"可接受（"香料"为补充说明）。仅缩放过小（问题 #10） |

### 2.2 图内文字与图像内容核查

方法：`pdftotext` 取图内文字层 + `pdftoppm`（150 dpi，并另做 CropBox 版）转 PNG 后 `read_image` 逐张目检（10/10；其中水、冰、食盐、α鸢尾酮按要求重点放大核查）。

| 图 | pdftotext 图内文字 | 图像核查要点 | 与图注/正文 |
|---|---|---|---|
| 放大10亿倍的水 | 无（文字已转曲） | 大黑球=O、小白球=H，每个 O 连 2 个 H，二维密排；底部英文标题 WATER MAGNIFIED ONE BILLION TIMES（在 CropBox 外，成品不显示） | 相符 |
| 水蒸气 | 无（文字已转曲） | 2 个完整 + 1 个半截 H₂O，键角约 120°；底部 STEAM（CropBox 外） | 相符 |
| 一个配有活塞的汽缸 | 无 | 直立汽缸 + 活塞（带活塞杆），缸内小黑点带速度箭头 | 相符（正文"小黑点"） |
| 冰 | 无（文字已转曲） | 黑白球交替的六边形网络（六方对称）、多孔；底部 ICE（CropBox 外） | 相符 |
| 空气中水的蒸发 | `氧` `氢` `氮` | 水面上方：水蒸气分子、O₂、N₂；下方连续水相；图例"氧/氢/氮" | 相符 |
| 盐在水中的溶解 | `0` `氯` `O` `钠` | 水中散落大球（氯离子）与小球（钠离子），水分子包裹方式可辨；图例"氯（大）/钠（小）" | 相符 |
| 食盐的晶体结构 | `晶体` `岩盐` `钾钠盐` `方铅矿` `Cl` `Na` `K` `Ag` `Mg` `Pb` `Se` `Te` `a(Å)` `5.64…6.34` `最邻近距离 d = a/2`、坐标 `x/y/z`、编号 `1–8` | 左侧数据表（岩盐型晶体：岩盐/钾钠盐/AgCl/MgO/方铅矿/PbSe/PbTe）+ 右侧 NaCl 三维单胞（黑白球两套面心格点交错，d=a/2，编号 1–8；黑=Na 小、白=Cl 大） | 内容与图注/正文相符；表格数据超出本章正文（问题 #9） |
| 碳在氧气中的燃烧 | 无（文字已转曲） | 白色球堆=碳晶体；黑色双球=O₂；黑白对=CO；底部 CARBON BURNING IN OXYGEN（CropBox 外） | 相符 |
| 空气中的紫罗兰香气分子 | 无（文字已转曲） | N₂（斜线）/O₂（黑）/水蒸气（黑白小球）+ 复杂有机分子（大球=O 或 C、小球=H）；底部 ODOR OF VIOLETS（CropBox 外） | 相符 |
| α鸢尾酮香料的分子结构图 | 无（文字已转曲） | 六元环（2,2,3,6-四甲基、5-位双键）+ 3-丁烯-2-酮侧链，与 α-irone 系统名一致 | 相符 |

补充要点：
- **无中英标题重复问题**：5 张图源 PDF 内嵌英文标题，但均位于 PDF CropBox 之外，XeLaTeX 按 CropBox 裁切，成品 PDF 中不出现（已核对 p.4/5/6/7/10/11/12/13 渲染页）。
- 图源 PDF 均为 iLovePDF 裁剪的单页矢量图（1 页/图），尺寸 89×154 pt～366×178 pt，均为黑白线图。
- 图 1.7 的图内表格数据（5.64/6.28/5.54/4.20/5.97/6.14/6.34 Å）不属于英文正文本章内容，无法用英文核对（见问题 #9、存疑项）。

---

## 3. 编译记录

### 3.1 环境

- macOS；TeX Live 2026/Homebrew；`xelatex` = XeTeX 3.141592653-2.6-0.999998；poppler `pdftotext/pdftoppm`；`pdffonts/pdfinfo`。
- 入口：`preview/chapter-1/check.tex`（`\setcounter{chapter}{0}` + `\input{../../Chapters/VolumeI/Chapter1.tex}`）。
- 字体：`\setmainfont{Times New Roman}`；`\IfFontExistsTF{SimSun}{\setCJKmainfont{SimSun}}{\setCJKmainfont{Songti SC}}`。

### 3.2 任务指定基线命令（连编 2 遍）

```bash
cd Feynman-Lectures-Latex/preview/chapter-1
xelatex -interaction=nonstopmode -output-directory=build check.tex
xelatex -interaction=nonstopmode -output-directory=build check.tex
```

| 指标 | 第 1 遍 | 第 2 遍 |
|---|---|---|
| 退出码 | 0 | **0** |
| 输出页数 | 14 | **14**（A4 595.28×841.89 pt） |
| `!` 级 LaTeX error | 0 | **0** |
| Overfull / Underfull | 0 / 0 | **0 / 0** |
| Missing character | 0 | **0** |
| 未定义引用 | 14（首遍正常，需第二遍） | **0** |
| LaTeX/Package/Font Warning | —（另有 Rerun 提示） | **5**（见 3.3） |

第 1 遍末尾提示 `Label(s) may have changed. Rerun to get cross-references right.`；第 2 遍交叉引用全部解析，与"必须连编 2 遍"的模板用法一致。

### 3.3 5 条 warning 定性（均无害，不阻塞验收）

| # | warning | 定性 |
|---|---|---|
| 1 | `LaTeX Warning: You have requested package '../../styles/readability', but the package provides 'readability'.` | 导言区用带路径的 `\usepackage{../../styles/readability}` 所致；仅提示，不影响输出。可改用 `TEXINPUTS=../../styles:` + `\usepackage{readability}` 消除（不建议为此改主文件逻辑） |
| 2 | `Package hyperref Warning: Option 'colorlinks' has already been used ...` | readability.sty 内已 `\hypersetup{colorlinks}`，check 文档导言又传该选项；无影响 |
| 3 | `Package xeCJK Warning: Redefining CJKfamily '\CJKrmdefault' (STSong(0))` | ctex 先载 mac 字体集（STSong），随后 `\setCJKmainfont` 覆盖为 Songti SC，属预期重定义 |
| 4 | `LaTeX Font Warning: Font shape 'TU/STHeiti(0)/b/n' undefined ... using 'm/n' instead` | 黑体族无独立粗体字形（AutoFakeBold 未覆盖该族）；小节标题/页眉黑体不加粗，视觉可接受（低） |
| 5 | `LaTeX Font Warning: Some font shapes were not available, defaults substituted.` | 第 4 条的汇总提示 |

### 3.4 字体回退（SimSun → Songti SC）核查

- 本机 **无 SimSun**（`fc-list` 仅见 Songti SC/Tsongti 等）；`\IfFontExistsTF{SimSun}` 为假 → 执行 `\setCJKmainfont[AutoFakeBold=true]{Songti SC}`。
- 证据：日志中 `Font family 'SongtiSC(0)' created for font 'Songti SC'`（另有 ctex mac 字体集 `STSong(0)` 先行创建）；`pdffonts build/check.pdf` 显示嵌入 **STSongti-SC-Regular**（多子集）与 STHeiti、TimesNewRomanPSMT 等；**0 Missing character**，14 页中文正常。
- 结论：回退成功，与 `docs/analysis/pilot-notes.md` 的记录一致。

### 3.5 关于日志/终端里的 "I can't find file `SimSun'"（重点澄清）

任务给出的基线现象复现如下（仅出现在 **stdout**，不写入 `build/check.log`）：

```
kpathsea: Running mktextfm SimSun
/opt/homebrew/.../mktexnam: Could not map source abbreviation S for SimSun.
mktextfm: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1; ; nonstopmode; input SimSun
! I can't find file `SimSun'.
! Emergency stop.
mktextfm: `...' failed to make SimSun.tfm.
kpathsea: Appending font creation commands to build/missfont.log.
```

**性质：不是文档错误，也不算编译 error。** 原因：`\IfFontExistsTF{SimSun}` 探测字体时，XeTeX/kpathsea 在 fontconfig 找不到 SimSun 后会按 TFM 路径回退，从而 spawn `mktextfm` → `mf` 子进程；这两行 `!` 是 **METAFONT 子进程**的报错，不进入 `check.log`，不改变 xelatex 退出码（两遍均 0），文档随后正常回退 Songti SC 并输出 14 页；同时 `build/missfont.log` 被追加 1 行/遍（内容 `mktextfm SimSun`）。

**规避方式（均已实测）：**

| 方法 | 命令 | 结果 |
|---|---|---|
| ✅ 推荐：禁用 mktex | `xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex` | SimSun 噪音 **0 行**；两遍 exit 0；14 页；0 error；5 条 warning 不变；字体回退结果不变 |
| 环境变量 | `MKTEXTFM=0 xelatex -interaction=nonstopmode ...` | 同样抑制成功（0 行噪音、14 页、0 error） |
| 改 check.tex | 预先判断 `\IfFileExists` / 由构建脚本注入字体集 | 需改模板，不建议（本次未改任何文件） |

**推荐可复现命令（最终验证用）：**

```bash
cd Feynman-Lectures-Latex/preview/chapter-1
rm -rf build && mkdir -p build
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex

# 验收（全部应通过）
grep -c '^!' build/check.log              # 0
grep -c 'Overfull' build/check.log        # 0
grep -c 'Underfull' build/check.log       # 0
grep -c 'Missing character' build/check.log  # 0
pdfinfo build/check.pdf | grep '^Pages'   # 14
```

### 3.6 编译结论

- **可编译**：两遍后 14 页 A4，0 error、0 overfull、0 underfull、0 missing character；无致命错误。
- 任务指定命令与推荐命令（`-no-mktex=tfm`）产物等价；推荐命令可让 stdout 完全干净。
- 页数说明：本版式改造后 14 页（改造前基线 11 页，见 `docs/analysis/chapter-1-notes.md`）；`build/` 为 gitignore 目录，产物不入库。

---

## 4. 数字一致性核对（逐项）

> 方法：按 `read` 行号把中文数字/单位逐项与 eFLP 文本对读；"英文依据"为逐字引用（长句只截取关键短语）。

| # | 项目（中文位置） | 英文依据 | 结论 |
|---|---|---|---|
| 1 | 1/4 英寸（L106；NEW 概念图 L161） | "a drop of water a quarter of an inch on the side" | 数值一致；中文作"直径"，英文 "on the side" 指立方体边长（存疑，见 §5） |
| 2 | 2000 倍（L106） | "roughly two thousand times" | ✅ 一致 |
| 3 | 40 英尺（L106） | "roughly forty feet across" | ✅ 一致 |
| 4 | 2000 倍（L108） | "magnifying it two thousand times again" | ✅ 一致 |
| 5 | 15 英里（L108） | "extends about fifteen miles across" | ✅ 一致 |
| 6 | 250 倍（L110） | "magnify it another two hundred and fifty times" | ✅ 一致 |
| 7 | 10 亿倍（L110；图注 L99） | "a picture of water magnified a billion times" | ✅ 一致 |
| 8 | 1～2×10⁻⁸ 厘米（L10；L131；L217） | "The atoms are 1 or 2×10−8 cm in radius" | ✅ 一致（量纲 cm 正确） |
| 9 | 10⁻⁸ 厘米 = 1Å（L131） | "Now 10−8 cm is called an angstrom" | ✅ 一致 |
| 10 | 1～2 Å（L131；概念图 L163） | "1 or 2 angstroms (Å) in radius" | ✅ 一致（写法见问题 #3） |
| 11 | 100 个网球（L178） | "tennis balls (a hundred or so)" | ✅ 一致 |
| 12 | 120°（L135） | "there is a 120∘ angle between the hydrogen atoms" | ✅ 一致 |
| 13 | 105°3′（L135） | "In actual fact the angle is 105∘3′" | ✅ 数值一致（符号写法见问题 #4） |
| 14 | 0.957 Å（L135） | "the distance ... is 0.957 Å" | ✅ 一致 |
| 15 | 60°（L202） | "if we turn the picture around an axis by 60∘" | ✅ 一致 |
| 16 | 20 年（杯盖上的水，L249） | "sitting there for perhaps twenty years" | ✅ 一致 |
| 17 | 20 年前（物理方法，L345） | "For about twenty years it has been possible" | ✅ 一致 |
| 18 | 三种分子（L347） | "there are three slightly different molecules" | ✅ 一致 |
| 19 | 化学名 4(2, 2, 3, 6-…)-3-丁烯-2-酮（L352） | "4-(2, 2, 3, 6 tetramethyl-5-cyclohexenyl)-3-buten-2-one" | 位次/数字一致；"4" 后缺连字符（问题 #5） |
| 20 | NEW 概念图：原子核直径约 10⁻¹³ 厘米（L165） | 英文本章无"原子核"尺度；通行数据 ~1 fm = 10⁻¹³ cm | 数量级正确；属 NEW 增补（`\figsource` 已注明"非原书插图；原子核尺度取通行数量级"），非英文核对项 |
| 21 | 200 年（L24） | "two hundred years" | ✅ 一致 |
| 22 | 4 分钟（L31） | "you want to learn it in four minutes?" | ✅ 一致 |
| 23 | 100 英里/秒（L55） | "a speed of less than one hundred miles a second" | ✅ 一致 |
| 24 | 百万分之一（L55） | "constant to within one part in a million" | ✅ 一致 |
| 25 | 两倍的分子/密度增加一倍（L184） | "put twice as many molecules ... so as to double the density" | ✅ 一致 |
| 26 | 第 2 章/第 3 章（NEW，L14） | 目录：Ch.2 Basic Physics；Ch.3 The Relation of Physics to Other Sciences | ✅ 一致 |
| 27 | 六个碳原子/两个碳原子和三个氢原子（L341） | "The six carbons ... two carbons and three hydrogens sticking up here" | ✅ 一致 |
| 28 | 角度之差在秒以下（L369） | "agree, within seconds of arc" | ✅ 一致 |
| 29 | 两个碳原子与一个**氧**原子（L343） | "it consists of one hydrogen and two carbons tied on here" | ❌ 不一致：中文"氧"应为"氢"（语义/错字，属 §1-4 审校范围，转存疑项提示） |
| 30 | 图 1.7 表内 5.64 / 6.28 / 5.54 / 4.20 / 5.97 / 6.14 / 6.34 Å | 英文无此表 | 无法用英文核对（图内数据，见问题 #9） |

**小结**：英文正文中的数字/单位/数量级（含 10⁻⁸、10⁻¹³、10⁹、120°、105°3′、0.957 Å、60°、1/4 英寸、2000×2、250×、40 ft、15 mi、20 年×2、三种分子、化学名位次）**未发现数值/量纲错误**；仅 1 处化学名缺连字符（低）、1 处 NEW「直径」措辞存疑（低）、1 处「氧/氢」语义错误（跨范围，转 §1-4 审校员）。

---

## 5. 存疑项

1. **L106 / L161「直径约 1/4 英寸」**：英文为 "a drop of water a quarter of an inch on the side"（边长/跨度，按立方体理解），中文版译作"直径"；NEW 概念图沿用该措辞。数值 1/4 英寸本身正确，若上游要严格，可把 NEW 概念图 (1) 改为"约 1/4 英寸"或"约 1/4 英寸见方"；正文属 OCR 原文，建议仅标注。
2. **图 1.7 的图源与表格**：图内数据表（岩盐/钾钠盐/方铅矿/AgCl/MgO/PbSe/PbTe）在英文正文中没有对应；eFLP 该图由两幅 SVG（`f01-07_tc_iPad_big_a/b`）组成，疑为"数据表+三维单胞"两部分，若如此则本图为原图的中文重绘版（黑球标号 1–8、白圈标号 1–8 与原图描述吻合）。表中"钾钠盐"（KCl）疑为"钾石盐"（sylvite）之误，需上游确认图源后再定。
3. **L371 两个 `\uwave` 之间的空格**：删除空格即可消除下划线断口，但若合并为一个 `\uwave` 会使 `\uwave` 计数 52→51，可能触发"零删改"校验脚本的计数断言；建议只删空格、保留两个宏。
4. **与语义审校可能重叠的标点缺陷（仅提示，未计入问题表）**：
   - L106 "而没有任何其他东西并且即使我们用最好的光学显微镜"——"东西"后缺句读；
   - L180 "（所有教科书中都有这种图）一个配有活塞的汽缸"——"）"与"一个"之间缺标点（建议"——"或"："）；
   - L326 段末"……发现自己原来已到达人的鼻子中了"缺句号；
   - L343 "在某处有两个碳原子与一个氧原子联结在一起"——"氧"应为"氢"（见数字表 #29）。
5. **英文图注口径**：eFLP 网页 Figure 1–1…1–9 图注为空（仅图号），中文图注实际来自中文版图题；本报告以"图源 PDF 内嵌英文标题（5 张）+ 英文正文对应句（其余）"为对照依据。图 1.1 英文正文 "idealized in several ways" 的三点内容在中文正文 L112–119 已完整译出，NEW 读图提示亦补"二维理想化"，故未判为图注缺失。
6. **`\r{A}` 与字面 Å 的最终取舍**：本报告建议统一为字面 `Å`（全库 `\AA` 未使用、第 5 章用字面 Å）；若项目另有"物理量统一宏"规划，则改 L131/L135 的字面 Å 为 `\r{A}` 亦可，但需全库统一。

---

## 6. 覆盖性结论

- **结构**：386 行全文 + 脚本自动检查（标记、环境、label/ref、宏参数、括号、数学模式、OCRed 空格/标点、图号顺序）。结论：结构完整、可编译；唯一结构缺陷是图 1.7 的孤儿 label（根因是英文原句漏译，属 §1-3 语义范围）；NEW 标记 27/27 配对，无新增文字泄漏到标记外。
- **图**：10/10 图逐一渲染核查（含 4 张指定关键图的 `read_image` 抽查），图内文字用 `pdftotext` 提取；图注 10/10 与图/正文相符，其中 1 张（图 1.7）正文无引用、图内含本章未涉及的数据表，1 张（图 1.10）缩放过小；图源内嵌英文标题均落在 CropBox 外，成品无中英重复标题。图号与正文引用顺序一致（1→6→8→10，缺 1.7）。
- **编译**：任务指定命令连编 2 遍可复现：14 页、0 error、0 overfull/underfull、0 missing character、5 条无害 warning；SimSun 提示为 kpathsea 字体探测子进程噪音（不在 .log、不影响退出码），已给出 `-no-mktex=tfm`（推荐）与 `MKTEXTFM=0` 两种规避方式并实测通过。
- **数字**：英文正文数字/量纲逐项核对 29 项，27 项一致；无数量级/单位错误；仅化学名缺 1 个连字符、NEW「直径」措辞存疑、1 处「氧/氢」跨范围语义错误。
- **未覆盖**：逐句语义/译文风格/漏译漏句（由四位分节审校员负责；本报告仅在 §5 提示了 3 处标点与 1 处氧/氢，可能与他们的结论重叠）。
