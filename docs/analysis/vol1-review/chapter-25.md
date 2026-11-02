# 第 25 章《线性系统及其综述》审查报告

- 审校员：rev2-s1；日期：2026-11-03
- 范围：`Chapters/VolumeI/Chapter25.tex`（220 行，CRLF）；对照：`_attachments/build-feynman/audit/en/I_25.txt`（25–1…25–5，5 节）、公开中译本旁证 `_attachments/reference/zh/Chapter25.txt`、候选差异 `_attachments/reference/candidates/ch25-candidates.md`（小块 236 / 大块 33，已逐条过滤）。
- 结果：**问题 6 项（高 0 / 中 2 / 低 4），已全部修正（共 7 处替换、8 处文字编辑）**；存疑 6 项未改。`git diff` 6 行（6 增 6 删，保持原 CRLF 行尾）。

## 问题表（已修）

| # | 行号 | 级别 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|---|
| 1 | L98 | 中 | "**我们调制收音机时**，就是把刻度盘转到一个新的位置"——"retune（重新调谐）"误译成"调制（modulate）"，与全段"调谐"主题矛盾 | "When we retune the radio, we can make a new setting of the dial…"（I_25 L974） | 改作"我们重新调谐收音机时" |
| 2 | L100 | 中 | "我们只要知道**有多少个正弦波**构成这个已知力$F$"——傅里叶分解要确定的是每个正弦分量的**权重/幅度**，不是正弦波的**个数** | "We just have to know how much of each sine wave to put in to make the given F"（L1008） | 改作"我们只要知道每个正弦波要加多少来构成这个已知力$F$" |
| 3 | L212 | 低 | 并联电路段：第一个阻抗漏 hat（"流过**$Z_1$**的电流"），且"**在**$\hat{Z}_2$**上的**电流"表述不合原文 | "the current through Ẑ1 is equal to Î1=V̂/Ẑ1. The current in Ẑ2 is Î2=V̂/Ẑ2."（L1549） | 改作"流过$\hat{Z}_1$的电流"、"流过$\hat{Z}_2$的电流" |
| 4 | L71 | 低 | 图 25-1 图注"线性系统叠加的一个例子"漏"原理"（正文同句作"线性系统叠加原理的一个例子"） | "Fig. 25–1. An example of the principle of superposition for linear systems."（L845） | 图注改作"线性系统叠加原理的一个例子" |
| 5 | L110 | 低 | 图 25-4 图注"一连串强烈的**冲击力**"与正文术语"冲力（impulse）"不一致 | "Fig. 25–4. A complicated force may be treated as a succession of sharp impulses."（L1030） | 图注改作"…一连串强烈的冲力来处理" |
| 6 | L194 | 低 | 汽车类比段"减**振**器"（2 处）与同段"减**震**器"（3 处）混用 | —（英文一律 shock absorber，属中文用字不统一） | 两处"减振器"统一为"减震器" |

## 存疑项（未改）

1. **L87** "比如说以每秒550 kHz广播" ← "say 550 kilocycles per second"：kHz 已含"每秒"，"每秒550 kHz"语义重复；底本如此，可改"以550 kHz广播"，未改。
2. **L98** "［叫作中周（IF）频率］" ← "called IF frequency"：规范术语为"中频（IF）"，"中周"为旧称；底本如此，未改。
3. **L221** "以后我们还要更详细地讨论这些法则" ← "They will be discussed again in more detail next year."：英文指明"第二年（课程）"，中文泛化为"以后"；底本如此，未改。
4. **L93** 图 25-3 图注"尖锐的谐曲线" ← "A sharply tuned resonance curve."：宜作"尖锐调谐的共振曲线"；底本如此，未改。
5. **L128** "当它经过通常所处的位置——零点时" ← "as it passes zero, which is the place it likes to be"（它喜欢待的地方）；译文泛化，未改。
6. **L87** "780 000次" 千位分隔用空格，与同段"780 kHz""550 kHz"体例不一；仅提示，未改。

## 覆盖性结论

- **节/段对应**：5 节 ↔ 5 节（线性微分方程 / 解的叠加 / 线性系统中的振动 / 物理学中的类比 / 串联和并联阻抗）。中文 16/15/8/13/4 个文字块与英文对应段落（被公式、浮动图分隔）逐段核对：**无整段缺失、无重复粘贴、无错位**。
- **公式**：17 个编号公式 (25.1)–(25.17) 及全部无编号公式（$a$ 乘解、$b=e^{-c}$、并联阻抗复合式等）逐式对照英文，符号、系数、上下标无误；**本次未改动任何公式内容**。
- **数字**：780 kHz / 780 000 次、550 kHz、90% 的 90%、标度盘 10↔3、17、百分之五十、$1~H$/$1~V$/$1~A\cdot s^{-1}$、1 库仑/1 伏特/1 法拉等均与英文一致，无数字错误。
- **图**：6 图全部定义 label 并被正文引用（图 25.1–25.6），图号顺序与英文 25–1…25–6 对应；另有跨章引用图 24.2（Chapter 24 label），单章（经 xr）与全书均可解析。
- **人名/术语**：乔（Joe）、麦克斯韦、欧姆、亨利、法拉、基尔霍夫、傅里叶、格林函数、叠加原理、瞬变态、共振曲线、阻抗、冲力（impulse）等均正确。
- **参考文本误（不改，仅记录）**：候选清单 39 条 CJK 级差异全部是参考文本 OCR 误（如 句/名、瞬/朋、态/檀、叠加/登、擦/掠、簧/筑、幂/短 等），本仓库文字正确；大块差异均为参考网页眉/图注错位，无漏译。

## 验证

- `preview/chapter-25/check.tex`：由 `python3 tools/make_chapter_check.py 25` 生成（章号 24、input Chapter25.tex）；因正文引用第 24 章图 24.2，另加 `\usepackage{xr}` + `\externaldocument{../../Chapters/VolumeI/Chapter24}` 解析跨章引用（依赖 `Chapters/VolumeI/Chapter24.aux`）。
- 连编 2 遍：**0 error / 0 Overfull / 0 Underfull / 0 Missing character / 0 undefined reference**；11 页；0 处"??"。PDF 抽查："我们重新调谐收音机时"、"每个正弦波要加多少"、"流过 Ẑ1/Ẑ2 的电流"、图 25.1/25.4 图注、"减震器"、图 24.2 均正确显示。
- 修改量：`git diff` 6 行；未 commit，未改其他章、tools 或全书编译。
