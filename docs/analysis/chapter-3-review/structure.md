# 第 3 章《物理学与其他科学的关系》结构 · 图 · 编译 · 数字 · 段落完整性专项审计

> 审校员：reviewer-struct（task-15）　日期：2026-11-02　分支：`feat/reading-efficiency`
> 范围：`Chapters/VolumeI/Chapter3.tex`（102 行）的 LaTeX 结构、2 张图逐张核对、**段落完整性**、编译链、全章数字/人名/术语一致性。
> **不在本报告范围**：逐句语义与译文风格（由四位分节审校员负责）。本报告对跨范围问题只在「存疑项」提示。
> 依据：`docs/analysis/chapter-3-review/00-conventions.md`；英文对照 `_attachments/build-feynman/audit/en/I_03.txt`（eFLP 抓取文本，125 行；Fig. 3–N 单独占行）。

## 0. 结论速览

| 审计项 | 结论 | 关键计数 |
|---|---|---|
| 段落完整性（重点） | ✅ **"缺一段"的怀疑不成立** | 中文 34 段 ↔ 英文 34 个正文段 **一一对应**；英文第 35 行 L123 `How I'm rushing through this!…` 是 **eFLP 脚注**（正文 L91 "…on the earth.¹" 的脚注 1，行尾带 ↩ 标记），中文已用 `\footnote` 完整放在 L67 同一锚点（471 汉字）。无整段漏译、无合并、无重复 |
| LaTeX 结构 | ⚠️ 环境配对、caption/label 次序正确；但引用体系未使用：**0 个 `\ref`、2 个 label 全孤儿、4 处硬编码"图3-1/图3-2"**，而图注渲染为"图 3.1/图 3.2"（连字符 vs 点号，同页可见不一致） | `figure` 1/1、`wrapfigure` 1/1 配对；`\uwave` 50 处平衡；0 个 `%<<<NEW`；数学模式全部成对；1 处全角空格 T+1 处宏间空格 |
| 图 3.1 克莱布斯循环 | ⚠️ 内容与图注/正文相符（循环闭环、每个反应标注酶名）；**但 0.5\textwidth 缩放过小，图内标注约 3.5–4 pt 基本无法阅读**，与正文"图3-1中每个反应中都写上了酶的名称"矛盾 | 图源 344.5×295.5 pt（CropBox=MediaBox）；渲染核对通过 |
| 图 3.2 部分DNA分子结构图 | ⚠️ 结构示意正确（双链、糖-磷酸骨架、碱基对 A/B/C/D，配对的"左链 BAADC → 右链 ABBCD"与正文示例完全一致）；**但每个糖环旁误标"脱氧核糖核酸"（DNA 全称），应为"脱氧核糖"** | 图源 182.6×397.7 pt（CropBox=MediaBox）；无图外残留 |
| 编译 | ✅ 可编译、无致命错误 | `-no-mktex=tfm` 连编 2 遍：**12 页 A4**；0 error / 0 overfull / 0 underfull / 0 Missing character / 0 未定义引用；5 条无害 warning；SimSun 探测噪音 0 行；Songti SC 回退成功 |
| 数字/人名/术语 | ⚠️ 数字与年份全部一致；人名 6/6 一致；**生物术语 2 处误译**（glucose→"蔗糖"应为"葡萄糖"；ribosome→"微粒体"应为"核糖体"） | 数字 14 组一致；人名 6 组一致；术语 2 错 + 图内 1 错 |

问题总计 **12 条**：高 0 / 中 5 / 低 7（其中 3 条为与分节报告可能重叠的交叉登记）。

---

## 1. LaTeX 结构审计

### 1.1 检查项与结果

| 检查项 | 方法 | 结果 |
|---|---|---|
| 环境配对 | 正则统计 begin/end | `figure` 1/1（L30–35）、`wrapfigure` 1/1（L47–51），全部配对 |
| label / ref | grep + 全库比对 | 2 个 label：`figure:克莱布斯循环`（L34）、`figure:部分DNA分子结构图`（L50）；**全文 `\ref` 数 = 0** → 2 个 label 全部孤儿；无悬空引用 |
| 硬编码图号 | grep `图3-N` | 4 处：L28、L39、L41 的"图3-1"，L54 的"图3-2"（**连字符风格**）；而 ctexbook 渲染的图注为"图 3.1/图 3.2"（**点号风格**）→ 同页可见两种写法（p4 图注"图 3.1"+正文"图3-1"；p6 图注"图 3.2"+正文"图3-2"） |
| caption / label 次序 | 逐块检查 | figure 3.1：L33 caption → L34 label ✅；wrapfigure 3.2：L49 caption → L50 label ✅（次序正确，与第 2 章表格不同） |
| 图宽 | 逐项 | 图 3.1 `width=0.5\textwidth`（80.5 mm）；图 3.2 `width=0.35\textwidth`（56.3 mm），wrapfigure 框 0.4\textwidth（64.4 mm） |
| `\uwave` | 逐行括号平衡 | 50 处全部成对，无跨行不平衡 |
| 数学模式 | 逐行 `$` 计数 | 全部成对（仅 `$\mathrm{C}^{12}$`、`$\mathrm{C}^{13}$` 两处） |
| 括号/环境整体平衡 | 全文件扫描 | 花括号净深度 0，无越界 `}` |
| `%<<<NEW` 标记 | grep | **0 个**（本章未做阅读效率改造，符合 conventions §0） |
| OCR 排版残留 | 正则扫描 | 无半角标点夹中文、无 `\ `（反斜杠+空格）误用、无双 ASCII 空格；1 处 U+3000 全角空格（L41）、1 处宏间空格拆词（L62）、1 处双连字符化学式（L45）、1 处全角百分号（L28） |

### 1.2 问题表格

| # | 行号 | 严重度 | 类型 | 中文原文（≤30 字，问题处加粗） | 问题说明 | 英文依据（≤25 词原文引用） | 建议改法 |
|---|---|---|---|---|---|---|---|
| 1 | L28、L39、L41、L54 | 中 | LaTeX/结构、图文 | "我们在**图3-1**中总结了…"；"**图3-1**中每个反应中都写上了…"；"**图3-1**的循环中最重要的是…"；"如**图3-2**所示" | 全章 0 个 `\ref`、2 个 label 全孤儿，正文用硬编码"图3-1/图3-2"（连字符）；而图注经 LaTeX 编号渲染为"图 3.1/图 3.2"（点号）——同一页出现两种图号写法，且图序变化时引用不会更新。项目 visual 审计已记录本章 2 个 label 为"仅硬编码编号引用"。建议统一为 `\ref` | —（LaTeX 引用体系问题） | 把 4 处"图3-1/图3-2"改为"图\ref{figure:克莱布斯循环}"/"图\ref{figure:部分DNA分子结构图}"（输出"图 3.1/图 3.2"与图注一致） |
| 2 | 图 3.1（L30–35） | 中 | 图文 | "\includegraphics[width=**0.5\textwidth**]{Chapter3/克莱布斯循环}" | 图源 344.5×295.5 pt（121.5 mm 宽），按 0.5\textwidth（80.5 mm）排入＝缩放 **0.66 倍**；图内最小标注原生字号约 5.5–6 pt，成品中约 **3.5–4 pt**，酶名/化合物名基本无法辨认（实测图内文字连通域高 17 px@300 dpi→4.1 pt）。而正文明确说"图3-1中每个反应中都写上了酶的名称"，读者实际读不到 → 图文功能受损 | "The names of the enzymes are written in Fig. 3–1 at each reaction." | 图宽增至 0.75–0.85\textwidth（高约 104–118 mm，仍在版心内），或换用中文重绘/放大版；至少在图注注明"图内为英文原图" |
| 3 | 图 3.2（L47–51），图内标注 | 中 | 图文、术语 | 图内每个糖环旁标 "**脱氧核糖核酸**" | 图 3.2 的每个五元糖环旁标注"脱氧核糖核酸"（= deoxyribonucleic acid，DNA 全称）；该单元应为"**脱氧核糖**"（deoxyribose），与正文"每条链的骨架是一列糖与磷酸基"矛盾。全图 10 处重复此错标 | "The backbone of each of these chains … is a series of sugar and phosphate groups" | 图内标注改为"脱氧核糖"（4 字），"脱氧核糖核酸/DNA"只保留给分子整体 |
| 4 | L26 | 中 | 术语 | "…接收光线而产生**蔗糖**的机构，植物在夜间消耗**蔗糖**…" | 英文为 **glucose**（葡萄糖），中文误作"蔗糖"（sucrose，二糖）——化学/生物含义错误（**全段 3 处**，英文 glucose 2 处 + 1 处指代） | "there is machinery for picking up light and generating glucose, which is consumed in the dark" | "…产生**葡萄糖**的机构，植物在夜间消耗**葡萄糖**…" |
| 5 | L60 | 中 | 术语 | "在细胞中存在一种叫做**微粒体**的小小粒子…但是**微粒体**并不在细胞核内" | 英文 **ribosomes**（核糖体）；"微粒体"= microsome，是内质网碎片，与核糖体是不同结构（术语错误，**全段 4 处**：两种写法/指代都出现） | "There are in the cell tiny particles called ribosomes … But the ribosomes are not in the nucleus" | "…叫做**核糖体**的小小粒子…但是**核糖体**并不在细胞核内…" |
| 6 | L62 | 低 | 标点 | "…这就是：\uwave{所有的物} \uwave{质都是由原子组成的}" | 一个词"物质"被两个 `\uwave` 加一个**空格**拆开；成品 p7 呈现"所有的物 质都是…"，字间出现可见空隙且下划线断开。（同类问题第 1 章 L371 已由 Lead 修） | "…it is that all things are made of atoms" | 删除 `}` 与 `\uwave` 之间的空格（保留两段 `\uwave` 以维持计数），或合并为一个 `\uwave{所有的物质都是由原子组成的}` |
| 7 | L41 | 低 | 标点 | "…就是这样的"盒子"。**\u3000**所以GTP比GDP具有更多的能量" | 源码含 U+3000 全角空格，成品 p5 显示为"盒子”。␣所以 GTP"的可见空档（比正常字距大）；应为普通句间空白 | —（排版问题） | 删除全角空格，作"…的"盒子"。所以GTP…" |
| 8 | L45 | 低 | 标点 | "其骨架是**CO--NH**，等等" | 化学式骨架用了双连字符 `--`，LaTeX 渲染为 en dash"CO–NH"；英文原文为单连字符 "CO-NH"（单键） | "chains in which the backbone is CO-NH, etc." | "其骨架是 CO-NH，等等" |
| 9 | L28 | 低 | 标点 | "大约只占**1％**左右" | 使用全角百分号"％"；与全章数字（阿拉伯数字 + 半角符号）风格不一致 | "perhaps a percent or so" | "大约只占 1% 左右" |
| 10 | L47–51 | 低 | LaTeX/结构 | "\begin{wrapfigure}{l}{0.4\textwidth}\n    \includegraphics…" | wrapfigure 内缺 `\centering`：图 3.2 实际宽 0.35\textwidth，在 0.4\textwidth 图框内**左对齐**，右侧留白不对称；图 3.1 的 figure 环境则用了 `\centering`，两图版式不一致 | —（版式问题） | 在 `\includegraphics` 前加 `\centering` |
| 11 | L49 | 低 | 图文 | "\caption{**部分DNA分子结构图**}" | 英文原图注为 "Schematic diagram of DNA."；中文图注沿用"文件名式"写法（缺"示意图"）。"部分"可由图只画出 5 对碱基解释，但整体不及"DNA 分子结构示意图"准确 | "Fig. 3–2. Schematic diagram of DNA." | "DNA 分子结构示意图"（或"部分 DNA 分子结构示意图"） |
| 12 | 图 3.1（L30–35）图内 | 低 | 图文 | 图内标题 "**CITRIC ACID CYCLE**"（英文） | 图内标题与全图标注均为英文，而中文图注为"克莱布斯循环"（二者为同义词：柠檬酸循环=Krebs 循环）；中英并置对中文读者略突兀，且与正文使用"克莱布斯循环/呼吸循环"不统一 | "Fig. 3–1. The Krebs cycle." | 仅标注：可在图注补"（即柠檬酸循环）"，或在图注说明图内为英文原图 |

---

## 2. 图逐张核对

### 2.1 图 3.1「克莱布斯循环」（L30–35，p4）

| 核对项 | 结果 |
|---|---|
| 图源 | `Figures/VolumeI/Chapter3/克莱布斯循环.pdf`，1 页；pdfinfo：344.54×295.46 pt；**MediaBox = CropBox**（无图外隐藏区）；无文本层（文字已转曲，`pdftotext` 为空） |
| 循环是否闭环 | ✅ 闭环：乙酰辅酶 A（acetyl coenzyme A）→ 柠檬酸（citrate）→ 顺乌头酸（cis-aconitate）→ 异柠檬酸（d-isocitrate）→ 草酰琥珀酸（oxalosuccinate）→ α-酮戊二酸（α-ketoglutarate）→ 琥珀酰辅酶 A（succinyl coenzyme A）→ 琥珀酸（succinate）→ 延胡索酸（fumarate）→ L-苹果酸（L-malate）→ 草酰乙酸（oxaloacetate）→（citrogenase）→ 柠檬酸，箭头首尾相接成环 |
| 与正文相符 | ✅ "每个反应标酶名"——图中每个箭头旁均标注酶名（CITRATE SYNTHETASE/ACONITASE/ISOCITRIC DEHYDROGENASE/α-KETOGLUTARATE DEHYDROGENASE/SUCCINIC DEHYDROGENASE/FUMARASE/malic dehydrogenase 等）；GDP/GTP 步骤亦在图中（succinate 一步出现 GTP↔GDP）；循环名称与正文"克莱布斯循环/呼吸循环"一致（图内标题 CITRIC ACID CYCLE 为同义名） |
| 图注 | "克莱布斯循环"↔ 英文 "The Krebs cycle." ✅ 准确 |
| 图宽/字号 | ⚠️ 0.5\textwidth = 80.5 mm（缩放 0.66×），图内标注约 3.5–4 pt，**不可读**（问题 #2）；建议 0.75–0.85\textwidth |
| CropBox 外残留 | ✅ 无（CropBox=MediaBox） |

### 2.2 图 3.2「部分DNA分子结构图」（L47–51，p6）

| 核对项 | 结果 |
|---|---|
| 图源 | `Figures/VolumeI/Chapter3/部分DNA分子结构图.pdf`，1 页；182.61×397.70 pt；**MediaBox = CropBox**（无图外隐藏区）；有中文文本层（可见标注"脱氧核糖核酸"，10 处） |
| 结构示意 | ✅ 双链示意正确：两条竖链各由"五元糖环 + 磷酸基（O=P–OH 等）"构成骨架，糖环之间以碱基对横档相连；碱基对自上而下为 B:A、A:B、A:B、D:C、C:D，即左链 B-A-A-D-C、右链 A-B-B-C-D——与正文示例"左边 BAADC…… 的补体 ABBCD……"**完全一致**；只画 5 对碱基，符合"部分" |
| 与正文相符 | ✅ 正文"DNA 分子是一对彼此缠绕在一起的链"（图为平面示意图，英文原注即 "Schematic"）；"骨架是一列糖与磷酸基"✅；"四种碱基 A、B、C、D"✅ |
| 图内标注 | ❌ 每个糖环旁标"脱氧核糖核酸"（DNA 全称），应为"脱氧核糖"（deoxyribose）——问题 #3；另图内中文用无衬线字体、偏粗，与正文宋体不一致（低，未单列） |
| 图注 | "部分DNA分子结构图" ↔ 英文 "Schematic diagram of DNA."——基本准确，缺"示意图"（问题 #11） |
| 图宽/字号 | ✅ 0.35\textwidth = 56.3 mm，图内标注渲染约 8.8 pt，可读；wrapfigure 缺 `\centering`（问题 #10） |
| CropBox 外残留 | ✅ 无（CropBox=MediaBox；文本层内容均可见） |

### 2.3 图注对照表

| 图 | 中文图注 | 英文官方图注 | 判断 |
|---|---|---|---|
| 图 3.1 | 克莱布斯循环 | "Fig. 3–1. The Krebs cycle." | ✅ 准确（逐词对应）；图内英文标题 "CITRIC ACID CYCLE" 为同义名（问题 #12，低） |
| 图 3.2 | 部分DNA分子结构图 | "Fig. 3–2. Schematic diagram of DNA." | ⚠️ 基本准确：中文补"部分"可由图仅示 5 对碱基解释，但缺"示意"；建议改"DNA 分子结构示意图"（问题 #11） |

---

## 3. 段落完整性（重点）

### 3.1 中英段落逐段对应表

中文 34 个正文段（`read` 行号）↔ 英文 I_03.txt 34 个正文段（L39–L121）**一一对应**，无合并、无重复：

| # | 中文行号 | 英文行号 | 英文段首 | 判断 |
|---:|---:|---:|---|---|
| 1 | L5 | L39 | Physics is the most fundamental… | ✅ 对应 |
| 2 | L9 | L43 | The science which is perhaps the most deeply… | ✅ |
| 3 | L11 | L45 | There is also a branch of physics and chemistry… | ✅ |
| 4 | L13 | L47 | The other branch of chemistry is organic chemistry… | ✅ |
| 5 | L18 | L51 | Thus we come to the science of biology… | ✅ |
| 6 | L20 | L53 | There was an interesting early relationship… | ✅ |
| 7 | L22 | L55 | If we look at the processes of biology… | ✅ |
| 8 | L24 | L57 | The opposite effect is that… | ✅ |
| 9 | L26 | L59 | Biology is such an enormously wide field… | ✅ |
| 10 | L28 | L63 | In the cells of living systems…（引出 Fig. 3–1） | ✅ |
| 11 | L37 | L65 | Here we see a whole series of molecules… | ✅ |
| 12 | L39 | L67 | An enzyme is made of another substance… | ✅ |
| 13 | L41 | L69 | The most important feature of the cycle… | ✅ |
| 14 | L43 | L71 | Physics is of great importance in biology… | ✅ |
| 15 | L45 | L73 | Now, we return to the description of enzymes… | ✅ |
| 16 | L52 | L75 | Another problem is how do the enzymes know…（引出 DNA） | ✅ |
| 17 | L54 | L79 | The structure of the substance DNA was studied… | ✅ |
| 18 | L56 | L81 | Attached to each sugar along the line… | ✅ |
| 19 | L58 | L83 | What then about reproduction?… | ✅ |
| 20 | L60 | L85 | Next comes the question… | ✅ |
| 21 | L62 | L87 | Certainly no subject or field… | ✅ |
| 22 | L67 | L91 | In this rapid-fire explanation of the whole world… | ✅ |
| 23 | L69 | L93 | One of the most impressive discoveries… | ✅ |
| 24 | L71 | L95 | It is the nuclear "burning" of hydrogen… | ✅ |
| 25 | L77 | L99 | We turn now to what are called earth sciences… | ✅ |
| 26 | L79 | L101 | The question basic to geology is… | ✅ |
| 27 | L81 | L103 | What about the inside of the earth?… | ✅ |
| 28 | L86 | L107 | Next, we consider the science of psychology… | ✅ |
| 29 | L88 | L109 | The other branches of psychology… | ✅ |
| 30 | L94 | L113 | In order for physics to be useful… | ✅ |
| 31 | L96 | L115 | There is another kind of problem… | ✅ |
| 32 | L98 | L117 | There is no historical question being studied… | ✅ |
| 33 | L100 | L119 | Finally, there is a physical problem… | ✅ |
| 34 | L102 | L121 | A poet once said… | ✅ |
| ★ | **L67 脚注** | **L123** | How I'm rushing through this!…（eFLP 脚注，行尾 ↩） | ✅ 对应（见 §3.2） |

### 3.2 "第 35 段"之谜：L123 是脚注，不是漏译

- 英文正文 L91 末尾为 "…the stars are made of atoms of the same kind as those on the earth.**1**" —— 带**脚注标记 1**；I_03.txt 的 L123 末尾带 **↩** 符号，内容 "How I'm rushing through this! How much each sentence…What men are poets…" 正是该脚注 1 的全文。
- 中文在 L67 同一锚点（"星体是用同地球上一样的原子组成的"之后）用 `\footnote{…}` 完整放入该段：**471 汉字**，逐句覆盖英文 L123 全部 16 个句子（"在这里我是讲得多么匆促啊！…诗人就很可能默不作声。"），并额外含一处译者方括号注（帕洛玛天文台 200 英寸望远镜说明）与 OCR 错字（"部是"→都是、"里光"→？，见 §6）。
- 因此 **35 vs 34 的差异 = "英文脚注被抽成独立行"，不是中文漏段**。实测该脚注在 p7–p8 页底正常排印（跨页），锚点与编号正确。

### 3.3 合并 / 重复检查

- 34 个中文段与 34 个英文段一一对应（§3.1），中文段"汉字数/英文词数"比值为 1.29–1.90（L67 含脚注为 2.86；去掉脚注后正文部分恰为 **1.65**，与全章一致），无某段长度约为相邻两段之和的异常 → **无两段合并**。
- 34 段段首两两不同（无重复粘贴的段落）；脚注内容与正文其它段无重复 → **无整段重复**。
- 结论：**无整段缺失、无合并、无重复；中文段落完整**。

---

## 4. 编译记录

### 4.1 环境与入口

- macOS；TeX Live 2026/Homebrew；`xelatex` = XeTeX 3.141592653-2.6-0.999998；poppler `pdftotext/pdftoppm`、`pdffonts/pdfinfo`。
- 入口：`preview/chapter-3/check.tex`（`\setcounter{chapter}{2}` + `\input{../../Chapters/VolumeI/Chapter3.tex}`，Lead 已建好）。

### 4.2 可复现命令

```bash
cd Feynman-Lectures-Latex/preview/chapter-3
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex

# 验收
grep -c '^!' build/check.log                     # 0
grep -cE 'Overfull|Underfull' build/check.log    # 0
grep -c 'Missing character' build/check.log      # 0
pdfinfo build/check.pdf | grep '^Pages'          # 12
```

### 4.3 结果统计

| 指标 | 第 1 遍 | 第 2 遍 |
|---|---|---|
| 退出码 | 0 | **0** |
| 页数 | 12 | **12**（A4 595.28×841.89 pt） |
| `!` 级 LaTeX error | 0 | **0** |
| Overfull / Underfull | 0 / 0 | **0 / 0** |
| Missing character | 0 | **0** |
| 未定义引用 | 0（本章无 `\ref`） | **0** |
| Warning | 7 条（5 条基线 + hyperref `Rerun to get /PageLabels` + `Label(s) may have changed`，首遍正常） | **5 条**（见 4.3.1） |
| SimSun 探测噪音（`I can't find file`/`mktextfm`） | **0 行** | **0 行** |

#### 4.3.1 5 条 warning 定性（均无害）

| # | warning | 定性 |
|---|---|---|
| 1 | `Package xeCJK Warning: Redefining CJKfamily '\CJKrmdefault' (STSong(0))` | ctex 先载 mac 字体集、随后 `\setCJKmainfont` 覆盖，预期行为 |
| 2 | `LaTeX Warning: You have requested package '../../styles/readability', but the package provides 'readability'` | 带路径 `\usepackage` 所致 |
| 3 | `Package hyperref Warning: Option 'colorlinks' has already been used` | readability.sty 内已设，无影响 |
| 4 | `LaTeX Font Warning: Font shape 'TU/STHeiti(0)/b/n' undefined … using 'm/n'` | 黑体族无独立粗体字形 |
| 5 | `LaTeX Font Warning: Some font shapes were not available, defaults substituted` | 第 4 条汇总 |

- 字体回退：本机无 SimSun → Songti SC（`pdffonts` 显示 STSongti-SC-Regular 嵌入；0 Missing character）；PDF 另含图 3.2 自带的 CairoFont-0-1 / DejaVuSans-Bold 子集（图内标注用）。
- 版式位置：图 3.1 → **p4**（顶部，图注"图 3.1 克莱布斯循环"）；图 3.2 → **p6**（wrapfigure 左侧，图注"图 3.2 部分 DNA 分子结构图"）；长脚注跨 **p7–p8** 页底。
- 0 error / 0 overfull / 0 underfull / 0 Missing character → **可编译，无致命问题**。

---

## 5. 数字 / 人名 / 术语一致性

### 5.1 数字

| # | 中文值（行号） | 英文值（依据） | 判断 |
|---|---|---|---|
| 1 | 5 到 10 个分子（L24） | "five or ten molecules at a time" | ✅ 一致 |
| 2 | 约 1％（L28） | "perhaps a percent or so" | ✅ 数值一致（写法见问题 #9） |
| 3 | 3 秒钟后 / 10 秒钟后（L43） | "after three seconds … again after ten seconds" | ✅ 一致 |
| 4 | 6 个或 7 个中子，6 个质子（L43） | "six neutrons or seven neutrons, together with the six protons" | ✅ 一致 |
| 5 | C12 / C13 / C14（L43、L71） | "C12 and C13 … radioactive isotopes like C14" | ✅ 一致 |
| 6 | 3 种或 4 种脱氢酶（L39） | "three or four hydrogen-reducing enzymes" | ✅ 一致 |
| 7 | 20 种不同的氨基酸（L45，两处） | "twenty different amino acids" | ✅ 一致 |
| 8 | 1960 年以来（L45） | "since 1960" | ✅ 一致 |
| 9 | 56 个或 60 个左右的氨基酸（L45） | "some fifty-six or sixty amino acids" | ✅ 一致 |
| 10 | 1000 个以上原子，接近 2000 个（L45） | "more than a thousand atoms (or nearly two thousand if we include hydrogens)" | ✅ 一致 |
| 11 | 四种碱基（L56） | "there are four kinds" | ✅ 一致 |
| 12 | 一百万年前（L67 脚注） | "one-million-year-old light" | ✅ 一致 |
| 13 | 200 英寸光学望远镜（L67 译者注） | 英文脚注只说 "the greater eye of Palomar"（未给数字）；Hale 望远镜确实为 200 英寸 | ✅ 事实正确（译者增补；见 §6-2） |
| 14 | 大约一百多年前 / 几百万年后（L100） | "over a hundred years" / "A few million years later" | ✅ 一致 |

### 5.2 人名 / 专名

| 中文（行号） | 英文 | 判断 |
|---|---|---|
| 门捷列夫（L9） | Mendeleev | ✅ 一致（"门捷列夫周期表"= periodic chart of Mendeleev） |
| 梅耶（Mayer）（L20） | Mayer | ✅ 一致 |
| 克莱布斯（Krebs）（L37） | Krebs | ✅ 一致 |
| 帕洛玛（Palomar）（L67） | Palomar | ✅ 一致 |
| 朱庇特（木星）（L67） | Jupiter | ✅ 一致 |
| 威尔逊（Wilson）（L67 译者注） | （英文无；译者注） | ⚠️ 见 §6-2（历史上 "Mount Wilson and Palomar Observatories" 可解释，今名应为 Palomar Observatory） |
| 巴斯德（L.Pasteur）（L102） | Louis Pasteur | ✅ 一致（缩写 L.） |

### 5.3 化学 / 生物术语

| # | 中文（行号） | 英文 | 判断 |
|---|---|---|---|
| 1 | 脱氧核糖核酸 / DNA（L52、L60） | "DNA (short for desoxyribose nucleic acid)" | ✅ 一致（"脱氧核糖核酸"为 DNA 今名） |
| 2 | **蔗糖（L26 三处）** | glucose | ❌ **误译**：应为"葡萄糖"（问题 #4） |
| 3 | **微粒体（L60 四处）** | ribosomes | ❌ **误译**：应为"核糖体"（问题 #5） |
| 4 | 乙酰胆碱（L24） | acetylcholine | ✅ |
| 5 | 肌球蛋白 / 肌动球蛋白（L24） | myosin / actomyosin | ✅ |
| 6 | 端板（L24） | endplate | ✅ |
| 7 | 统计力学（L11） | statistical mechanics | ✅ |
| 8 | 能量守恒定律（L20） | conservation of energy | ✅ |
| 9 | 活化能 / 势垒（L37） | activation energy / energy barrier | ✅ |
| 10 | 酵素 / 酶（L37） | ferments / enzymes | ✅ |
| 11 | 脯氨酸 / 亚氨基酸（L45） | proline / imino acid | ✅ |
| 12 | 血红蛋白（L45） | hemoglobin | ✅ |
| 13 | 腺嘌呤 / 胸腺嘧啶 / 胞嘧啶 / 鸟嘌呤（L56） | adenine / thymine / cytosine / guanine | ✅ 4/4 |
| 14 | 二磷酸鸟嘌呤核苷 / 三磷酸鸟嘌呤核苷（L41） | guanosine-di-phosphate / guanosine-tri-phosphate | ✅ |
| 15 | 脱氧核糖核酸（**图 3.2 图内糖环标注**） | deoxyribose（糖） | ❌ 图内误标（问题 #3） |
| 16 | 光合作用 / 葡萄糖代谢链（L26） | photosynthesis | ✅（"光合作用"正确；同段 glucose 误译见 #2） |

---

## 6. 存疑项

1. **英文脚注 vs 正文段的判读**：I_03.txt 把 L123 当独立行，但该行行尾带 "↩"、且正文 L91 有脚注标记 "1"——本报告据此判定其为 eFLP 脚注，中文 `\footnote` 对应。若上游以"中文版应为 35 段"为前提，请复核此判读（证据见 §3.2）。
2. **译者注"威尔逊（Wilson）山帕洛玛天文台"**（L67）：200 英寸 Hale 望远镜在今天属于 Palomar Observatory（帕洛玛山）；但历史上 1948–1980 年该台由 "Mount Wilson and Palomar Observatories" 联合管理，译者注的表述可以理解。若求严格今名，建议改"帕洛玛天文台（Palomar Observatory）"。
3. **L67 脚注的 OCR 错字**："星体和地球**部**是用同样的原子组成的"（应为"都"）、"捕获一百万年前发出的**里光**"（疑为"星光"或"光"）、"在这**个**简短的叙述"（英文 "in this brief story"）等；另脚注内有一处方括号译者注。属 §3-4 语义审校范围，本报告仅提示。
4. **本章其它 OCR 错字（示例，未计入问题表，交分节审校）**：L5"意味看"（着）、L18"进面"（进而）、L28"反直"（反应）、L39"化学反也"（反应）、L41"陈非"（除非）、L41"附加能最"（能量）、L77"现存"（现在）等；不影响本报告的结构/图/数字结论。
5. **图 3.1 的图源**：图内为英文标注的柠檬酸循环图（含 "CITRIC ACID CYCLE" 标题），与 eFLP Fig. 3–1 是否同一版本未能目验（eFLP 图直连 403，Wayback 不可用）；若原书图为另一版本（中文版原图可能带中文标注），建议上游核对是否替换。
6. **"图3-1"编号风格**：本章 4 处硬编码为连字符风格；项目 visual 审计记录全库"图N.M"61 处 vs "图N-M"11 处，属全库统一问题，建议随引用体系一并改为 `\ref`（输出点号风格）。
7. **长脚注跨页**：L67 脚注 471 字，跨 p7–p8 页底。排印正常（0 overfull），但阅读体验一般；可考虑改为章末注，属版式选择，仅标注。

---

## 7. 覆盖性结论

- **段落完整性（重点）**：中文 34 段 ↔ 英文 34 个正文段一一对应（§3.1），**无整段缺失、无合并、无重复**；英文第 35 行 L123 经证据判定为 eFLP 脚注（正文 L91 脚注 1），中文已用 `\footnote` 完整译出（471 汉字）并置于正确锚点（L67）→ **"漏掉 How I'm rushing through this! 整段"的怀疑不成立**，无需补译正文；仅脚注内有少量 OCR 错字待 §3-4 审校处理。
- **结构**：2 个 figure/wrapfigure 环境配对、caption→label 次序正确、`\uwave` 50 处平衡、0 个 NEW 标记、数学模式成对；**主要结构缺陷是引用体系未使用**（0 个 `\ref`、2 个孤儿 label、4 处硬编码"图3-1/图3-2"与图注"图 3.1/图 3.2"风格不一致）。
- **图**：2/2 图内容与图注/正文相符（Krebs 循环闭环且每步有酶名；DNA 双链示意、碱基配对与正文 BAADC→ABBCD 示例一致）；两张图 CropBox=MediaBox，**无图外残留/隐藏文字**；主要问题是图 3.1 缩小后标注约 4 pt 不可读（中）、图 3.2 糖环误标"脱氧核糖核酸"（中）、图 3.2 图注缺"示意"（低）。
- **编译**：`-no-mktex=tfm` 连编 2 遍可复现：**12 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 未定义引用**，5 条无害 warning；SimSun 探测噪音 0 行；Songti SC 回退成功（PDF 嵌入 STSongti-SC-Regular）；图 3.1→p4、图 3.2→p6、脚注跨 p7–p8。
- **数字/人名/术语**：数字 14 组、人名 6 组全部与英文一致；术语 2 处误译（glucose→"蔗糖"、ribosome→"微粒体"）+ 图 3.2 图内糖环误标 1 处；无数字/年份/量纲错误。
- **未覆盖**：逐句语义与译文风格（四位分节审校员负责）；本报告 §6 提示的 OCR 错字、脚注错字与"微粒体/核糖体"等若与分节报告重叠，以分节报告为准。
