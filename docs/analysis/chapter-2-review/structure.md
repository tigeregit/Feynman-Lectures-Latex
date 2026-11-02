# 第 2 章《基本物理》结构 · 表格 · 图 · 编译 · 数字一致性专项审计

> 审校员：reviewer-struct（task-10）　日期：2026-11-02　分支：`feat/reading-efficiency`
> 范围：`Chapters/VolumeI/Chapter2.tex`（131 行）的 LaTeX 结构、表 2.1/表 2.2 逐格核对、图 2.1「基本粒子」、编译链、全章数字一致性。
> **不在本报告范围**：逐句语义/译文风格审查（由四位分节审校员负责）。与分节报告重叠的条目已在说明中注明（如 §2-2 的 L47、§2-4 的 L104、表 2.2 表注）。
> 依据：`docs/analysis/chapter-2-review/00-conventions.md`；英文对照 `_attachments/build-feynman/audit/en/I_02.txt` 与官方页 <https://www.feynmanlectures.caltech.edu/I_02.html>（直连被 Cloudflare 403，经 `r.jina.ai` 文本代理取回；该页 Table 2–1/2–3 为 HTML 表可逐格读取，**Table 2–2 为图片** `t02-02_tc_big.svgz`，图片直连同样 403、Wayback/Internet Archive 不可用，故 Table 2–2 只有正文文字值可核对，详见 §4）。

## 0. 结论速览

| 审计项 | 结论 | 关键计数 |
|---|---|---|
| LaTeX 结构 | ⚠️ 环境全部配对、表格 3 列各行齐全、行尾 `\\` 齐、`\uwave` 60 处括号平衡；但 **3 个 label 全部是孤儿（全文 0 个 `\ref`）**，且两张表的 `\label` 放在 `\caption` **之前**，实测补 `\ref` 会输出"表??" | 2 table + 1 figure + 2 tabular 全部配对；0 悬空引用（因无 `\ref`）；3 孤儿 label；0 NEW 标记（本章无改造块） |
| 表 2.1 电磁波谱 | ✅ 9 行数值/名称/行为与英文 Table 2–1 **逐格一致** | 频率 9/9 一致；名称/行为 9/9 一致；仅"FM-TV"与英文"FM—TV"写法不同（低） |
| 表 2.2 基本相互作用 | ⚠️ 4 行数值/定律一致；**漏译英文表下注释**（强度为无量纲量、∼=数量级）；"all energy"多译"其他" | 强度 4/4 一致；表注缺失 1 条；措辞偏差 1 处 |
| 图 2.1 基本粒子 | ⚠️ 内容与正文大体相符（电荷列、分类、Λ 1115、ω 位置 780、e 0.51、ν 0、光子/引力子按正文省略）；**图内无 1154**；疑点：Y 行 S=−2 与衰变产物矛盾、Y 行只标一个 1395、隐藏英文残留、字号/尺寸偏大 | 逐项核对 17 项：一致 10、无法逐值核对（英文原表为图片）5、可疑 2 |
| 编译 | ✅ 可编译、无致命错误 | `-no-mktex=tfm` 连编 2 遍：14 页 A4；0 error / 0 overfull / 0 underfull / 0 Missing character / 0 未定义引用；5 条无害 warning；SimSun 探测噪音 0 行；Songti SC 回退成功 |
| 数字一致性 | ⚠️ 2 处错误（均属分节报告已列） | 核对 24 组：22 组一致；**L104 1154→1115（高）**、**L47 5×10^15→10^15（高）**；其余（92、1920、1 毫米/30 米/300 万吨、10⁻⁸/10⁻¹³ cm、ΔxΔp≥ℏ/2、10¹²、1.783×10⁻²⁷ g、0.510、206、780、186,000、1/137、10⁻²/10⁻⁴⁰/10⁻⁵/1、1947/1948、1961、约 30 种、表 2.1 全频率、表 2.2 全强度）均一致 |

问题总计 **14 条**：高 2 / 中 3 / 低 9（其中 4 条为与分节报告重叠的交叉登记）。

---

## 1. LaTeX 结构审计

### 1.1 检查项与结果

| 检查项 | 方法 | 结果 |
|---|---|---|
| 环境配对 | 正则统计 begin/end | `table` 2/2（L49、L118）、`tabular` 2/2（L54、L123）、`figure` 1/1（L95），全部配对 |
| label / ref | 全库 grep + 引用测试 | 3 个 label：`tab:电磁波谱`（L51）、`figure:基本粒子`（L99）、`tab:基本相互作用`（L120）；**全文 `\ref` 数为 0** → 3 个全部是孤儿 label；无悬空引用 |
| label 与 caption 次序 | 逐块检查 + 补 `\ref` 实测 | 表 2.1（L51 label → L52 caption）、表 2.2（L120 label → L121 caption）**label 在 caption 之前**（错误次序）；图 2.1 为 L98 caption → L99 label（正确）。在 build 内做引用测试：补 `\ref` 后连编 2 遍，两张表均输出**"表??"**，caption 包报 `\label without proper reference`（详见 §5.4） |
| 表格列数 | 逐行统计 `&` | 两张表全部行均为 **3 列**（表 2.1：9 行数据 + 表头；表 2.2：4 行数据 + 表头），无多列/缺列 |
| 行尾 `\\` | 逐行检查 | 数据行与表头行均以 `\\` 结束；末行 `\\ \bottomrule` 正确 |
| `\toprule/\midrule/\bottomrule` 位置 | 目检 + 渲染核对 | 位置正确：`\toprule` 在表头前、`\midrule` 在表头行末、`\bottomrule` 在末行；p.7/p.14 渲染三线表正常 |
| `\medskip` 位置 | 目检 | 位于 `\caption` 与 `tabular` 之间（L53、L122），仅增加间距，无结构问题 |
| 数学模式 | 逐行 `$` 计数 | 全部成对；`\sim`、`\hbar`、`\Delta x` 等均正常渲染 |
| `\uwave` | 逐行括号平衡 | 60 处全部成对，无跨行不平衡 |
| 表格行内文本 | 目检 | 表 2.1 第 3 列重复"波/粒子"（英文原表用右侧大括号跨行合并——等价，可接受）；表 2.2 表头"强度"无 `*` 号（英文 `Strength*`，因表注漏译，见问题 #5） |
| 图表引用方式 | grep 硬编码 | 正文 `图2.1` 硬编码 2 处（L93、L102），图号与实际编号（图 2.1）一致；表 2.1/2.2 正文无编号引用（英文原文亦未用编号引用 Table 2–1/2–3，可接受） |
| OCR 排版残留 | 正则扫描 | 无半角标点夹中文、无 `\ `（反斜杠+空格）误用、无制表符；多余的数学模式内空格/单位间距见问题 #14 |
| NEW 改造块 | grep | 本章 **0 个** `%<<<NEW` 标记、未使用 `\runin/\term/\keyidea/\fighint` 等 NEW 宏（与 conventions §0 一致） |

### 1.2 问题表格

| # | 行号 | 严重度 | 类型 | 中文原文（≤30 字，问题处加粗） | 问题说明 | 英文依据（≤25 词原文引用） | 建议改法 |
|---|---|---|---|---|---|---|---|
| 1 | L104 | 高 | 数字/量纲 | "**λ介子，质量为 1154MeV** 。另外三个……" | 英文与图 2.1 均为 **1115 MeV**（图内 Λ⁰ 标 1115），中文 1154 为数字颠倒；与同节插图自相矛盾。**§2-4 已列，本条为数字一致性交叉登记** | "There is a 'lambda,' with a mass of 1115 MeV" | "λ粒子，质量为 1115MeV。"（术语另见 §5） |
| 2 | L47 | 高 | 数字/量纲 | "频率范围为每秒**$ 5\times10^{14} $ 到$ 5\times10^{15} $** 周" | 英文与本章表 2.1 该行上限均为 **10¹⁵**，中文多乘一个 5，属上界错误，且与表 2.1 自相矛盾。**§2-2 已列** | "In the range of frequency from 5×10^14 to 10^15 cycles per second" | "在频率范围为每秒 $5\times10^{14}$ 到 $10^{15}$ 周的时候" |
| 3 | L51–52、L120–121 | 中 | LaTeX/结构 | "**\label{tab:电磁波谱}**\n\caption{电磁波谱}" | 两张表的 `\label` 放到 `\caption` 之前：caption 包报 `\label without proper reference`，实测补 `\ref` 后连编 2 遍仍输出"**表??**"（永远不会解析）。当前正文无 `\ref` 故未暴露，但属潜在引用错误。**§2-2 已列（判低）**；鉴于补引用即报错，本报告建议按"中"处理 | —（LaTeX 结构问题，无英文对应） | 把 L51 的 `\label` 移到 L52 `\caption` 之后、L120 的 `\label` 移到 L121 `\caption` 之后（与图 2.1 的 L98–99 写法一致） |
| 4 | L51、L99、L120 | 低 | LaTeX/结构 | "**\label{tab:电磁波谱}** / **\label{figure:基本粒子}** / **\label{tab:基本相互作用}**" | 3 个 label 全文 0 次 `\ref`，均为孤儿；正文以硬编码"图2.1"指向图（L93、L102），图号若变化将失同步。建议图 2.1 两处改用 `\ref{figure:基本粒子}`（需先按 #3 调序）；表 label 若保留编号体系可留给将来引用，否则可删 | —（结构问题） | L93、L102 的"图2.1"改为"图\ref{figure:基本粒子}"；两张表 label 保持（供后续引用）或按需删除 |
| 5 | L118–131（表 2.2） | 中 | 表格/图 | 表 2.2 只有 4 行，**无表下注释** | 英文 Table 2–3 表下有一整条注释说明"强度"是**无量纲**耦合常数量度、**∼ 表示"数量级"**；中文表完全缺失，读者无法理解"强度"列（且表头无 `*` 号）。**§2-4 已列（判低）；本报告从表格完整性角度建议按"中"处理** | "* The "strength" is a dimensionless measure of the coupling constant involved in each interaction (∼ means "of the order")." | 表下加注：*强度是各相互作用耦合常数的无量纲量度（∼ 表示"数量级"）。 |
| 6 | L127 | 低 | 表格/图 | "引力对**所有其他**能量" | 英文为 "Gravity to **all energy**"，中文多"其他"二字（疑衍文），字面上会被读成"除…之外的能量" | "Gravity to all energy" | "引力对所有能量" |
| 7 | L59 | 低 | 表格/图 | "**FM-TV**" | 英文 Table 2–1 作 "FM—TV"（em dash）；中文用半角连字符，属写法差异 | "FM—TV" | "FM—TV"（或"调频-电视"） |
| 8 | 图 2.1（L95–100） | 中 | 图文 | 图内顶行 "**Y⁻₁→Λ⁰+π⁻** … **S=−2**" | 图内 Y 行三态均标 **S=−2**，但衰变产物 Λ+π 的奇异数之和为 −1（Λ 的 S=−1，π 为 0）；强衰变的共振态应守恒 S，故图中 S=−2 与衰变产物矛盾，疑为制图/原表错误。英文 Table 2–2 为图片、本次未能目验，需上游核对（见 §4、§6） | —（英文 Table 2-2 为图片；正文未给 Y 的 S 值） | 仅标注、待核：若英文原表亦为 S=−2，则属原表缺陷；否则应改为 S=−1 |
| 9 | 图 2.1（L95–100） | 低 | 图文 | 图内 "Y⁻ … Y⁰ … Y⁺ … **1395**" | 三个 Y 共振态只在 Y⁺ 下方标一个 1395，Y⁻、Y⁰ 下无质量数字；若原表逐态标值则属漏标，若原表本就合并标一次则可接受（存疑） | —（英文 Table 2-2 为图片，正文未提 Y） | 仅标注：对照英文原表确认是否逐态标值 |
| 10 | 图 2.1（L95–100） | 低 | 图文 | 图 PDF 的 CropBox 外含 "Table 2-2 / Elementary Particles / 2-15" | 图 PDF 有一圈 CropBox 外内容（英文表题、原书页码 2-15）：LaTeX 按 CropBox 排入，**成品第 12 页渲染不可见**，但文本层残留这些字（pdftotext 第 12 页可提出 "Table 2-2"、"2-15"，复制/检索/无障碍阅读会读到）；若按 MediaBox 查看原图则会看到。**§2-4 已提示** | —（图内残留，无英文正文对应） | 建议重裁图 PDF（令 MediaBox=CropBox）或 `\includegraphics[trim=...]`，删除图外残留；至少知悉该现象 |
| 11 | 图 2.1（L95–100） | 低 | 图文 | "**\includegraphics[width=0.65\textwidth]**" | 图源 CropBox 为 180.6×388.7 pt（纵横比 2.15），按 0.65\textwidth 排入高约 **22.5 cm（版心 95%）**，独占第 12 页整页（两条引用段留在 p11）；图内中文用微软雅黑（无衬线），放大 1.64× 后字号约 14 pt，大于正文 12 pt，风格与正文宋体不一致 | —（版式问题） | 仅标注：建议 width 收到 0.50–0.55\textwidth（高约 17.3–19 cm），字号与正文更协调、图也更易与引用段同页；若保持大图，可在图注加读图提示 |
| 12 | L98 | 低 | 表格/图 | 「**\caption{基本粒子}**」 | 图注仅"基本粒子"（原书表题 Elementary Particles 的直译），无任何读图提示；该章唯一插图、又是信息密集的粒子分类图，读者不易看懂电荷列/实虚线含义 | "Table 2–2 Elementary Particles" | 仅标注、可选：图注可补"（原书表 2.2；质量单位 MeV，实线为粒子、虚线为共振态）"——属新增文字，需 Lead 决定 |
| 13 | L118（表 2.2 环境） | 低 | LaTeX/结构 | "**\begin{table}[H]**" | `[H]` 强制定位使表 2.2 落在第 13 页剩余空间之后，结果第 14 页**只有一张 4 行小表、约 85% 空白**（第 13 页正文已结束但余量不足）；同样 `[H]` 也使表 2.1 落在 p7 顶部、与所属 §2.2 被 §2.3 标题隔开（p7 页眉显示"2.3 量子物理学"） | —（版式问题） | 表 2.2 改用 `[htbp]`（或 `[!ht]`）让其浮动到 p13 底部，减少空白页；表 2.1 可留在原处（或同样改浮动） |
| 14 | L47、L74、L93、L104、L106、L108 | 低 | 标点 | 例：L47"每秒**$ 5\times10^{14} $  到$ 5\times10^{15}  $** 周"；L104"**1154MeV 。**"；L108"只有 **0.510MeV**" | OCR 残留的多余空格/单位间距不统一：数学模式内首尾空格（L47、L74 `$ 10^{-8} $`、L93 `$ 1.783\times10^{-27} $`）、双空格（L47）、数字与单位无空格（L104 1154MeV、L106 780MeV、L108 0.510MeV）与有空格（L93 1MeV、L112 186,000 英里）混用、L104"MeV 。"句号前空格。因 xeCJK 吞汉字间空格，多数在成品中不可见，但源码不洁且影响纯文本复用 | —（排版问题，无英文依据） | 删除数学模式内多余空格；统一"数字+空格+单位"（如"0.510 MeV"）；删 L104 句号前空格 |

---

## 2. 表 2.1「电磁波谱」逐格核对（对照英文 Table 2–1）

英文来源：官方页 HTML 表（`r.jina.ai` 取回），与 `I_02.txt` L80–95 一致。英文表用右侧大括号把 Waves / Particle 跨行合并；中文表逐行重复"波/粒子"，内容等价。

| 行 | 中文（L57–65） | 英文（Table 2–1） | 判断 |
|---|---|---|---|
| 1 | $10^{2}$ ／ 电扰动 ／ 场 | 10² ／ Electrical disturbance ／ Field | ✅ 一致 |
| 2 | $5\times10^{5}\sim10^{6}$ ／ 无线电广播 ／ 波 | 5×10⁵ – 10⁶ ／ Radio broadcast ／ Waves | ✅ 一致（范围符 ∼ vs –，可接受） |
| 3 | $10^{8}$ ／ FM-TV ／ 波 | 10⁸ ／ FM—TV ／ (Waves) | ✅ 数值/词义一致；"FM-TV" vs "FM—TV"（问题 #7，低） |
| 4 | $10^{10}$ ／ 雷达 ／ 波 | 10¹⁰ ／ Radar ／ (Waves) | ✅ 一致 |
| 5 | $5\times10^{14}\sim10^{15}$ ／ 光 ／ 波 | 5×10¹⁴ – 10¹⁵ ／ Light ／ (Waves) | ✅ 一致（注意正文 L47 作 5×10¹⁵，见问题 #2） |
| 6 | $10^{18}$ ／ X射线 ／ 粒子 | 10¹⁸ ／ X-rays ／ Particle | ✅ 一致 |
| 7 | $10^{21}$ ／ γ射线（核） ／ 粒子 | 10²¹ ／ γ-rays, nuclear ／ (Particle) | ✅ 一致 |
| 8 | $10^{24}$ ／ γ射线（"人造"） ／ 粒子 | 10²⁴ ／ γ-rays, "artificial" ／ (Particle) | ✅ 一致 |
| 9 | $10^{27}$ ／ γ射线（宇宙射线中） ／ 粒子 | 10²⁷ ／ γ-rays, in cosmic rays ／ (Particle) | ✅ 一致 |

**表 2.1 结论**：频率 9/9、名称 9/9、行为 9/9 全部与英文一致，无数字错误；表头"频率（周/秒）/名称/大略行为"与英文"Frequency in oscillations/sec / Name / Rough behavior"语义一致（"周/秒"=cycles/sec）。

---

## 3. 表 2.2「基本相互作用」逐格核对（对照英文 Table 2–3）

英文来源：官方页 HTML 表 + `I_02.txt` L140–147（含表下注释）。

| 行 | 中文（L126–129） | 英文（Table 2–3） | 判断 |
|---|---|---|---|
| 表头 | 耦合关系 ／ **强度** ／ 定律 | Coupling ／ **Strength\*** ／ Law | ⚠️ 中文表头"强度"缺 `*`（因表注缺失，问题 #5） |
| 1 | 光子对带电粒子 ／ $\sim10^{-2}$ ／ 已知 | Photon to charged particles ／ ∼10⁻² ／ Law known | ✅ 一致 |
| 2 | 引力对**所有其他**能量 ／ $\sim10^{-40}$ ／ 已知 | Gravity to **all energy** ／ ∼10⁻⁴⁰ ／ Law known | ⚠️ 强度/定律一致；"all energy"多"其他"（问题 #6，低） |
| 3 | 弱衰变 ／ $\sim10^{-5}$ ／ 部分已知 | Weak decays ／ ∼10⁻⁵ ／ Law partly known | ✅ 一致 |
| 4 | 介子对重子 ／ $\sim1$ ／ 不知（部分法则已知） | Mesons to baryons ／ ∼1 ／ Law unknown (some rules known) | ✅ 一致 |
| 表下注释 | **（无）** | \* The "strength" is a dimensionless measure of the coupling constant involved in each interaction (∼ means "of the order"). | ❌ **缺失**（问题 #5，中） |

**表 2.2 结论**：4 行强度值 4/4、定律描述 4/4 与英文一致；两处偏差：缺表注（中）、"所有其他能量"（低）。

---

## 4. 图 2.1「基本粒子」核对

### 4.1 图源与核对方法

- 图源：`Figures/VolumeI/Chapter2/基本粒子.pdf`（1 页，MediaBox 416.69×555.59 pt，**CropBox 118.25,87.15–298.86,475.88 pt** → 排入尺寸 180.6×388.7 pt）；
- 方法：`pdftotext`（该图有可提取文字层，253 个词条）+ `pdftoppm -cropbox -r 200/400/600` 渲染 + `read_image` 分区目检（表头/顶行/重子/介子/轻子/坐标轴）；图内文字位置用 `pdftotext -bbox` 精确核对行列归属。
- **英文 Table 2–2 的困难**：eFLP 该表是图片（`t02-02_tc_big.svgz`），直连 403（Cloudflare），Wayback / Internet Archive 均不可用，因此**无法逐格读取英文 Table 2–2 的原表数字**。本报告改用三重核对：① eFLP 正文明确给出的数值（1115、0.510、206 倍、780、零质量、光子/引力子省略、K*/φ/η 省略等）；② 中文正文与图内数值的**内部一致性**；③ 行列/电荷/分类结构与英文正文描述的对应。
- **任务关注的"1154 类错值"**：**图内不存在 1154**（全图数字已枚举：1400/1300/1200/1395/1319/1311/1196/1191/1189/1115/1100/1000/939/938/900…200/139.6/135.0/105.6/0.51/0/494/498）；**1154 出现在正文 L104**（见问题 #1），图中 Λ⁰ 正确标 **1115**。

### 4.2 图内数据逐项核对

| 项目 | 图内值 / 位置 | 英文依据（正文，Table 2–2 原表不可得） | 判断 |
|---|---|---|---|
| Λ⁰ | 1115（0 电荷列） | "There is a 'lambda,' with a mass of **1115** MeV" | ✅ 一致（正文 L104 误作 1154，见 #1） |
| n / p | 939（中性列）/ 938（+e 列） | "a neutron and a proton have almost the same mass" | ✅ 与正文不矛盾；电荷列正确 |
| Σ⁻ / Σ⁰ / Σ⁺ | 1196 / 1191 / 1189（−e / 0 / +e 列） | "three others, called sigmas, minus, neutral, and plus, with several masses almost the same" | ⚠️ 电荷列正确、三者质量相近 ✅；具体数值无法逐格核对（英文原表为图片） |
| Ξ⁻ / Ξ⁰ | 1319（−e）/ 1311（0） | "finally the xi doublet" | ⚠️ 排列正确；数值无法逐格核对 |
| Y⁻ / Y⁰ / Y⁺（虚线共振态） | "Y⁻₁→Λ⁰+π⁻" / "Y⁰₁→Λ⁰+π⁰" / "Y⁺₁→Λ⁰+π⁺"，仅标 1395 | 正文未提 Y（只存在于表中） | ⚠️ 见图内疑点 A、B |
| ω⁰→π⁺π⁺π⁻ | 虚线，位置 ≈780（**未印质量数字**） | "A thing called ω which goes into three pions has a mass **780** on this scale" | ✅ 位置与 780 一致（正文"on this scale"即按纵轴读值，合理） |
| ρ⁻ / ρ⁰ / ρ⁺→π⁺π⁻ | 虚线，位置 ≈750（未印数字） | "somewhat less certain is an object which disintegrates into two pions" | ✅ 与正文不矛盾 |
| K⁻ / K⁰K̄⁰ / K⁺ | 494 / 498 / 494（−e / 0 / +e 列） | "K-mesons, and they occur as a doublet, K⁺ and K⁰" | ⚠️ 排列正确；数值无法逐格核对 |
| π⁻ / π⁰ / π⁺ | 139.6 / 135.0 / 139.6 | "the pions, which come in three varieties, positive, negative, and neutral" | ⚠️ 排列正确；数值无法逐格核对 |
| μ⁻ | 105.6（−e 列） | "the muon, which has a mass much higher, **206 times** as heavy as an electron" | ✅ 105.6/0.51≈207，与"206 倍"在取整范围内一致 |
| e⁻ | 0.51（−e 列） | "the electron, which has a very small mass on this scale, only **0.510** MeV" | ✅ 一致（图中取两位 0.51） |
| ν⁰ | 0（中性列） | "a neutrino, and this particle has zero mass" | ✅ 一致 |
| 光子 / 引力子 | **未列** | "Several particles have been omitted … the photon and the graviton" | ✅ 正确地省略（正文明说图中略去） |
| K\*、φ、η | **未列** | "some of the newer resonances (K\*, ϕ, η)" omitted | ✅ 正确 |
| 电荷列布局 | −e / 0 / +e 三列 | "all neutral objects in one column, all positively charged ones to the right … negatively charged objects to the left" | ✅ 完全一致 |
| 分类 | 重子（Y,Ξ,Σ,Λ,n,p）／介子（ω,ρ,K,π）／轻子（μ,e,ν） | "baryons … mesons … leptons" 分类描述 | ✅ π 归介子、μ/e/ν 归轻子，正确 |
| 奇异性 S | Ξ=−2、Σ=−1、Λ=−1、n/p=0、ω/ρ=0、K=±1、π=0、轻子不标 | "Each particle in a multiplet has the same strangeness … Strangeness assignments are not applicable for leptons" | ✅ 除 Y 行外均合理；Y 行存疑（见疑点 A） |
| 实线/虚线 | 稳定粒子实线、共振态虚线 | "Particles are shown with a solid line and 'resonances' with a dashed one" | ✅ 一致 |
| 质量纵轴 | "质量(MeV)"，0–1400 | "the mass is given … called the MeV" | ✅ 一致 |

### 4.3 图内疑点（与 §6 存疑项对应）

- **疑点 A（问题 #8，中）**：顶行 Y 共振态标 **S=−2**，但其衰变产物 Λ+π 的奇异数为 −1；强衰变共振态应守恒奇异数，图内 S 与衰变产物矛盾，疑为制图/原表错误。英文原表为图片未能目验，需上游对照。
- **疑点 B（问题 #9，低）**：Y 行只有 Y⁺ 下方标 1395，Y⁻/Y⁰ 无质量数字；是否为原表合并标注，需对照英文原表。
- 其余：质量数值本身（1319/1311/1196/1191/1189/139.6/135.0/105.6/0.51/494/498）与 1960 年代通行数据一致且内部排序合理，未发现类似"1154"的明显错值；但因英文原表不可得，严格逐格一致性无法 100% 确认（见 §6-1）。

### 4.4 图注与版式

- 图注「基本粒子」= 英文 Table 2–2 表题 "Elementary Particles" 的直译，**准确**；英文原表无描述性图注，中文图注也未加说明（问题 #12：可选补读图提示）。
- 版式：图高约 22.5 cm（版心 95%），独占第 12 页；两条引用段（L93、L102）留在第 11 页，读者需翻页对照（问题 #11，低）。
- 图内中文为**微软雅黑**（无衬线），放大后约 14 pt，大于正文 12 pt 宋体（问题 #11，低）。
- 图 PDF 的 CropBox 外残留英文表题与页码，**成品渲染不可见**，但进入最终 PDF 文本层（问题 #10，低）。

---

## 5. 编译记录

### 5.1 环境与入口

- macOS；TeX Live 2026/Homebrew；`xelatex` = XeTeX 3.141592653-2.6-0.999998；poppler `pdftotext/pdftoppm`；`pdffonts/pdfinfo`。
- 入口：`preview/chapter-2/check.tex`（`\setcounter{chapter}{1}` + `\input{../../Chapters/VolumeI/Chapter2.tex}`，已由 Lead 建好）。

### 5.2 可复现命令（任务指定，连编 2 遍）

```bash
cd Feynman-Lectures-Latex/preview/chapter-2
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex

# 验收
grep -c '^!' build/check.log                # 0
grep -cE 'Overfull|Underfull' build/check.log   # 0
grep -c 'Missing character' build/check.log # 0
pdfinfo build/check.pdf | grep '^Pages'     # 14
pdffonts build/check.pdf                    # 应见 STSongti-SC-Regular（Songti SC 回退成功）
```

### 5.3 结果统计

| 指标 | 第 1 遍 | 第 2 遍 |
|---|---|---|
| 退出码 | 0 | **0** |
| 输出页数 | 14 | **14**（A4 595.28×841.89 pt） |
| `!` 级 LaTeX error | 0 | **0** |
| Overfull / Underfull | 0 / 0 | **0 / 0** |
| Missing character | 0 | **0** |
| 未定义引用 | 0（本章无 `\ref`） | **0** |
| Warning | 7 条（5 条基线 + hyperref `Rerun to get /PageLabels entry` + `Label(s) may have changed`，均为首遍正常提示） | **5 条**（见 5.3.1） |
| SimSun 探测噪音（`I can't find file`/`mktextfm`） | **0 行** | **0 行** |
| 字体嵌入 | — | STSongti-SC-Regular、STHeiti、TimesNewRomanPSMT 等全部嵌入 |

第 1 遍末尾提示 `Rerun to get /PageLabels entry`（hyperref 页标签，属正常首遍提示）；第 2 遍交叉引用与页标签稳定。

#### 5.3.1 5 条 warning 定性（均无害）

| # | warning | 定性 |
|---|---|---|
| 1 | `Package xeCJK Warning: Redefining CJKfamily '\CJKrmdefault' (STSong(0))` | ctex 先载 mac 字体集，随后 `\setCJKmainfont` 覆盖为 Songti SC，预期行为 |
| 2 | `LaTeX Warning: You have requested package '../../styles/readability', but the package provides 'readability'` | 带路径 `\usepackage` 所致，仅提示 |
| 3 | `Package hyperref Warning: Option 'colorlinks' has already been used` | readability.sty 内已设，无影响 |
| 4 | `LaTeX Font Warning: Font shape 'TU/STHeiti(0)/b/n' undefined ... using 'm/n' instead` | 黑体族无独立粗体字形，视觉可接受 |
| 5 | `LaTeX Font Warning: Some font shapes were not available, defaults substituted` | 第 4 条汇总 |

- **SimSun 说明**：本命令带 `-no-mktex=tfm`，stdout 中 SimSun 探测噪音为 **0 行**（第 1 章审计已证实该噪音来自 `\IfFontExistsTF{SimSun}` 触发的 mktextfm→mf 子进程，非 error；本机无 SimSun 时自动回退 Songti SC，`pdffonts` 可见 STSongti-SC-Regular 嵌入，0 Missing character）。
- 页数/页序：表 2.1 → p7；图 2.1 → p12（整页）；表 2.2 → p14（p14 仅一张表，约 85% 空白——见问题 #13）。

### 5.4 引用测试（label-before-caption 实证）

为验证问题 #3，在 `build/label_test/` 内复制入口并追加一行引用（不修改正文、不改 check.tex）：
`表\ref{tab:电磁波谱}、表\ref{tab:基本相互作用}、图\ref{figure:基本粒子}`。连编 2 遍结果：
- caption 包警告：`\label without proper reference on input line 51`、`… line 120`；
- 渲染输出：**"表??、表??、图2.1"**（两张表永远解析失败，图正常）——证实两张表的 label 次序必须修正（问题 #3）。

---

## 6. 数字一致性全表

> 依据：eFLP 正文逐字引用（Table 2–2 原表为图片处另注明）；"判断"按是否改变数值/量纲含义。

| # | 中文值（行号） | 英文值（依据） | 判断 |
|---|---|---|---|
| 1 | 92 种（L33） | "92 different kinds of atoms" | ✅ 一致 |
| 2 | 1920 年（L27、L29、L72） | "1920" / "about 1920" | ✅ 一致 |
| 3 | 1 毫米 / 30 米 / 三百万吨（L39） | "a millimeter across, thirty meters apart … three million tons" | ✅ 一致 |
| 4 | 10⁻⁸ cm（L74） | "An atom has a diameter of about 10−8 cm" | ✅ 一致 |
| 5 | 10⁻¹³ cm（L74） | "The nucleus has a diameter of about 10−13 cm" | ✅ 一致 |
| 6 | ΔxΔp≥ℏ/2（L74） | "ΔxΔp≥ℏ/2" | ✅ 一致 |
| 7 | 10¹² 周/秒（L78） | "above approximately 10^12 cycles per second" | ✅ 一致 |
| 8 | 1.783×10⁻²⁷ 克（L93） | "One MeV is equal to 1.783×10−27 gram" | ✅ 一致 |
| 9 | **1154 MeV（L104）** | "a 'lambda,' with a mass of **1115** MeV"（图内 Λ⁰ 亦 1115） | ❌ **不一致：1154→1115（高，问题 #1）** |
| 10 | 0.510 MeV（L108） | "only 0.510 MeV" | ✅ 一致 |
| 11 | 206 倍（L108） | "206 times as heavy as an electron" | ✅ 一致 |
| 12 | 780（L106） | "has a mass 780 on this scale" | ✅ 一致 |
| 13 | 186,000 英里（L112） | "186,000 miles a second" | ✅ 一致；中文括注"（300,000 公里）"为正确换算（英文无此括注） |
| 14 | 1/137（L114） | "some number, which is 1/137" | ✅ 一致 |
| 15 | ∼10⁻² / ∼10⁻⁴⁰ / ∼10⁻⁵ / ∼1（表 2.2） | "∼10−2 / ∼10−40 / ∼10−5 / ∼1" | ✅ 一致 |
| 16 | 1947 年或 1948 年（L89） | "in 1947 or 1948" | ✅ 一致 |
| 17 | 1961 年（L104、L106） | "in 1961" / "in 1961 we also found" | ✅ 一致 |
| 18 | 近 30 种粒子（L91） | "approximately thirty particles" | ✅ 一致 |
| 19 | 表 2.1 全部 9 个频率值 | Table 2–1 对应值 | ✅ 9/9 一致（见 §2） |
| 20 | 表 2.2 全部 4 个强度值 | Table 2–3 对应值 | ✅ 4/4 一致（见 §3） |
| 21 | 约 100 周/秒、500/1000 千周、1 千周=1000 周（L47） | "about one hundred cycles per second" / "500 or 1000 kilocycles (1 kilocycle=1000 cycles)" | ✅ 一致 |
| 22 | 10²⁴ 周、快 1000 倍（L47） | "say to 10^24 cycles per second" / "even a thousand times more rapid oscillation" | ✅ 一致 |
| 23 | **每秒 5×10¹⁴ 到 5×10¹⁵ 周（L47）** | "from 5×10^14 to **10^15** cycles per second"（表 2.1 亦 10¹⁵） | ❌ **不一致：多乘 5×（高，问题 #2）** |
| 24 | 序数 6 / 原子序数 8（L41） | "atom number six … it is called carbon" / "Atom number eight is called oxygen" | ✅ 一致 |

**数字小结**：24 组中 22 组一致；2 处错误均为分节报告已登记项（L104 1154→1115、L47 5×10¹⁵→10¹⁵），本报告从数字一致性角度复现并确认；表 2.1（9 个频率）与表 2.2（4 个强度）全部一致。

---

## 7. 存疑项

1. **表 2–2 英文原表不可得**：eFLP 该表为图片 `t02-02_tc_big.svgz`，直连 403（Cloudflare），Wayback 无快照、Internet Archive 书目受限，本报告只能用 eFLP 正文数值 + 图内内部一致性核对。图内 Σ/Ξ/K/π/μ 的具体数值（1196/1191/1189、1319/1311、494/498、139.6/135.0、105.6）**未能逐格与英文原表比对**；这些数值与 1960 年代通行数据一致、排序合理，暂未发现错值，但严格结论需上游以英文原表（或英文原书 PD）复核。
2. **图 2.1 顶行 Y 共振态 S=−2**（问题 #8）：与 Y→Λ+π 的奇异数矛盾，疑误；若英文原表亦作 S=−2 则属原表缺陷。需上游核对。
3. **图 2.1 的 Y 行质量标注**（问题 #9）：仅 Y⁺ 下有一个 1395；是否为原表合并标注需对照英文原表。
4. **λ/Σ 被称为"介子"**（L104 共 6 处）：Λ、Σ 是重子（超子），同段开头自称"统称为重子"，图 2.1 也把它们放在"重子"括号内——正文与图自相矛盾；英文只说 "a 'lambda'" / "sigmas"，未称 meson。**§2-4 已列为中等问题**，本报告从"正文-图一致性"角度附议（建议"λ超子/Λ 粒子、Σ 超子"）。
5. **表 2.2 表注严重度**：§2-4 判"低"，本报告判"中"（表注承载"强度"列的含义：无量纲、∼=数量级，缺了它 4 个数字无法正确解读）。建议 Lead 合并时取"中"。
6. **表 2.1 与被属章节分页**：表 2.1 落在 p7 顶部、紧接着是 §2.3 标题，而表属 §2.2；p7 页眉显示"2.3 量子物理学"。属版式小瑕疵（未单列问题行），可考虑改 `[htbp]` 或接受。
7. **图 2.1 的 CropBox 外残留**：成品渲染不可见、文本层可见（问题 #10）；若后续印刷/转换工具改用 MediaBox，英文表题"Table 2-2 Elementary Particles"和页码"2-15"可能显形，建议重裁图 PDF。

---

## 8. 覆盖性结论

- **结构**：131 行逐行 + 脚本检查（环境、label/ref、表格列/行尾、`\uwave`、数学模式、标点空格）。结论：环境与表格结构完整、3 列表格各行齐全、0 悬空引用；**主要结构缺陷是 3 个 label 全为孤儿、两张表 label 在 caption 之前（补引用即"表??"）**；无 NEW 块（本章未做阅读效率改造），未发现未定义引用或编译级结构错误。
- **表格**：表 2.1 与英文 Table 2–1 **9 行×3 列全部一致**；表 2.2 与 Table 2–3 数值 4/4 一致，但**漏译英文表下注释**、且有 1 处"所有其他能量"多字。两表均为三线表、3 列、行尾 `\\` 规范。
- **图**：图 2.1（原书 Table 2–2 的中文插图版）逐项核对 17 项：电荷列、分类（重子/介子/轻子）、Λ 1115、ω≈780、e 0.51、ν 0、光子/引力子省略、K*/φ/η 省略、实线/虚线等均正确；**图内无 1154 错值**；两处可疑（Y 行 S=−2、Y 行只标一个 1395）与一处图内隐藏文字残留、尺寸/字号偏大。图注「基本粒子」准确但无读图提示。
- **编译**：`-no-mktex=tfm` 连编 2 遍可复现：14 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 未定义引用，5 条无害 warning，SimSun 探测噪音 0 行，Songti SC 回退成功。可编译。
- **数字**：24 组数字核对，22 组一致；2 处错误（1154、5×10¹⁵）均与分节报告一致并已交叉登记；表 2.1/2.2 全部数值一致。
- **未覆盖/限制**：逐句语义与译文风格（四位分节审校员负责）；英文 Table 2–2 为图片且站点不可访问，图内非正文数值未能 100% 逐格对照（已在 §6/§7 明示）。
