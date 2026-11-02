# 第 40 章《统计力学原理》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter40.tex`（250 行；6 节 40-1～40-6：大气的指数变化律 / 玻尔兹曼定律 / 液体的蒸发 / 分子的速率分布 / 气体比热 / 经典物理的失败）
- 英文：`_attachments/build-feynman/audit/en/I_40.txt`（正文 L36–L395，含文末高斯积分脚注；抓取文本中公式为 [math] 碎片）
- 旁证：`_attachments/reference/zh/Chapter40.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch40-candidates.md`（309 小块 + 45 大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 已知统计力学公式（玻尔兹曼因子、麦克斯韦速率分布、能量均分、比热比）逐式比对；官方网页本次未抓取（不需要）
- 单章入口：`python3 tools/make_chapter_check.py 40` 生成 `preview/chapter-40/check.tex`，并已修正注释章名（《统计力学原理》）与 `cd` 路径（chapter-40）

## 结果

- **已修正 11 条（15 处；高 1、中 8、低 2）**；**存疑 6 项**（未改）。
- 单章编译：**13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍；5 条基线 warning）。
- 修改文件：`Chapters/VolumeI/Chapter40.tex`（16 增 / 20 删，**CRLF 保持**、末尾无换行）、`preview/chapter-40/check.tex`（仅注释）、本报告。未 commit，未动其他章。
- **本章无跨章引用**（基线编译即 0 undefined；全部 \ref 指向本章公式/图/表）。

## 高/严重问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L229 | **年份/人名错误**："大约在**1890年，金斯**又谈到这个疑难"（漏 Rayleigh） | "About 1905, Sir James Hopwood Jeans and Lord Rayleigh (John William Strutt) were to talk about this puzzle again." | 改为"大约在1905年，詹姆斯·霍普伍德·金斯爵士和瑞利勋爵（约翰·威廉·斯特拉特）又谈到了这个疑难。" |

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 2 | L225 | **物理含义错**："任何其他的力只能使$\gamma$变大" | "anything else will only make U higher" | "任何其他的力只能使$U$变大" |
| 3 | L53 | **公式内 OCR**："$exp[-(\text{每个原子的**是能**})/kT]$" | "e^{−the potential energy of each atom/kT}" | "每个原子的势能" |
| 4 | L185 | 漏"振动能"："总的$U$…也包括转动能" | "the total U includes not just the kinetic energy, but also the rotational and vibrational energies" | "而且也包括转动能和振动能" |
| 5 | L126 | **误译**："在一个**汽笛**上钻一个非常小的小孔" | "if we drill a little hole in the side of a gas pipe" | "在一根气管的侧壁上钻一个非常小的小孔" |
| 6 | L9–L16 | wrapfigure 40-1 插在句中："研**虽** / [图] / **然**我们知道了方均速度…"被拆成两段 | "Although we have the mean square velocity, we do not know how to answer…" | 图移到"我们以既没有风又没有其他扰动时…"段首；合并"虽然我们知道了方均速度…" |
| 7 | L82–L89 | wrapfigure 40-3 插在句中："只依赖于它们的距离 / [图] / $r_{ij}$，并且…" | "the force between any two molecules… depends only on their separation rij" | 图移到"在更深入一步的统计力学中…"段首；合并"…距离$r_{ij}$，并且可以用一个势函数…" |
| 8 | L136–L143 | wrapfigure 40-5 插在句中："写得很具一般 / [图] / 性。注意…" | "even though what we already have written is quite general" | 图移到"这种通过给出以某一最小的速度$z$分量…"段首；合并"…写得很具一般性。注意…" |
| 9 | L212–L219 | wrapfigure 40-6 插在句中："事实上，它比较小，但 / [图] / $1.22$并不太小…" | "In fact, it is lower, but 1.22 is not so much lower…" | 图移到"再进一步考虑的话，整个事情更显得神秘莫测…"段首；合并"…但$1.22$并不太小…" |

> 上述 4 处 figure 环境移动后均重新排版，编译 0 overfull，版面正常。

## 低严重度修正（已修）

- L143："每秒$1.796~289~917~3~m$" → "每秒$1.7962899173~m$"（小数点内被插入空格；英文 "1.7962899173 meters per second"）。
- L96："$\abs{V(r0)}$" → "$\abs{V(r_0)}$"（下标缺失，与同段前一处 $\abs{V(r_0)}$ 不一致）。

## 存疑项（未改）

1. L32 "它告诉了我们**高度**增大时，分子密度将如何下降" ← "which tells us how the density goes down as we go up **in energy**"：底本以"高度"代"能量"（势能随高度增大），语义等价，未改。
2. 表 40-1 标题"各种气体的**比热商**$\gamma$的值"：底本用词（通行作"比热比"），未改；数据与英文完全一致。
3. L221 "对H$_2$来说，$\gamma$从$-185~^\circ$C的$1.6$变化到在$2~000~^\circ$C的$1.3$"：英文 "from **about** 1.6 at −185°C to 1.3 at 2000°C"，漏"约"，未改。
4. L229 "这些话是**物理学家**第一次发现经典物理定律是错误的" ← "These words represent the first discovery…"：底本增补主语，未改。
5. L248 "在$100~^\circ$C，即绝对温度$373~^\circ$时" ← "At 100°C, or absolute temperature 373°"：单位"°"照底本，未改（严格应为 373 K）。
6. L53 附近"$exp[-(\text{K.E.})/kT]$"等处用英文缩写 K.E.、P.E.（底本风格），未改。

## 覆盖性结论

- **段落/完整性**：6 节与英文 40–1～40–6 对应；逐句核对**无漏句、无漏段、无重复粘贴**；候选 45 条大块差异全部为公式剥离/图注错位/页眉噪声。
- **公式**（零改动，逐式核对）：40.1 $n=n_0e^{-mgh/kT}$；40.2 $F=kT\frac{d}{dx}(\ln n)$；40.3 $n=(\text{常数})e^{-\text{P.E.}/kT}$；40.4 $n_{>u}\propto exp[-(\text{K.E.})/kT]$；40.5 $\int_{-\infty}^{\infty}f(u)du=1$；40.6 $\int_u^{\infty}uf(u)du=\text{常数}\times e^{-mu^2/2kT}$；40.7 $f(u)du=Ce^{-mu^2/2kT}du$；40.8 $f(p)dp=Ce^{-\text{K.E.}/kT}dp$；40.9 三维速度分布乘积式；40.10 $P_1/P_0=e^{-E_1/kT}/e^{-E_0/kT}$；40.11 $n_1=n_0e^{-(E_1-E_0)/kT}$——全部正确；文末高斯积分脚注（$I^2=\iint e^{-(x^2+y^2)}dxdy=\pi\int_0^\infty e^{-t}dt=\pi$）与英文一致。
- **数字/量纲**：1.7962899173 m/s（已修格式）、表 40–1 全部 10 组（He −180/1.660、Kr 19/1.68、Ar 15/1.668、H$_2$ 100/1.404、O$_2$ 100/1.399、HI 100/1.40、Br$_2$ 300/1.32、I$_2$ 185/1.30、NH$_3$ 15/1.310、C$_2$H$_6$ 15/1.22）、$\gamma$ 理论值 $5/3$、$9/7\approx1.286$、$13/12$、$12kT$、$1.66$、$1859$、$1905$、$-185~^\circ$C/$2~000~^\circ$C、$373~^\circ$ 均与英文一致（年份 1890→1905 已修）。
- **图表**：6 幅图（40.1–40.6）齐全，图注与英文 Fig. 40–1～40–6 一致；正文图引用全部解析（0 undefined）；表 40–1 数据/表头与英文一致；本章无跨章引用。
- **自动候选差异**：309 小块 + 45 大块绝大多数为公式剥离噪声与参考 OCR 讹字（氮→氨、碰撞→磁、爬→限、爬→有、垒→刍 等），**不据以改动**；确属本仓库的问题即上表 9 条 + 低 2 条。

## 验证

- 入口：`preview/chapter-40/check.tex`（`\setcounter{chapter}{39}`、`\input{../../Chapters/VolumeI/Chapter40.tex}`；注释章名/路径已改对）。
- 命令：`cd preview/chapter-40 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：13 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 文本抽查：修正点均生效（"每个原子的势能""转动能和振动能""只能使 U 变大""大约在 1905 年…瑞利勋爵""气管""1.7962899173 m""V (r₀)"；4 处被图拆断的句子均连续成句）；旧串（"每个原子的是能""只能使 γ 变大""1890 年""汽笛""1.796 289 917 3"）出现 0 次。
