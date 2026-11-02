# 第 41 章《布朗运动》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter41.tex`（276 行；4 节 41-1～41-4，6 幅图 41.1–41.6，21 个编号公式 (41.1)–(41.21)）
- 英文：`_attachments/build-feynman/audit/en/I_41.txt`（41–1～41–4；抓取文本中公式为分式碎片）
- 旁证：`_attachments/reference/zh/Chapter41.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch41-candidates.md`（小块/大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 中译本旁证逐式比对

## 结果

- **已修正 6 条（6 处；中 3、低 3）**；**存疑 3 项**（未改）。
- 单章编译：**13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter41.tex`（6 行，**CRLF 换行保持原状**）、`preview/chapter-41/check.tex`（注释改章名/路径，另加 xr 解析跨章式引用）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L32 | "可以证明这**常常**也就是涨落的起源"——涨落与耗散的关系是普遍成立的，英文为 always | "it turns out that that is always the source of the fluctuations also" | 改作"这也**总是**涨落的起源" |
| 2 | L48 | 电子热运动被译成"**有规则地**来回跳动"——热涨落本质无规，与紧接的"电子密度的涨落"矛盾 | "the electrons in the resistor are jiggling around" | 改作"**无规则地**来回跳动" |
| 3 | L221 | "（**第32章**）"——所指标量叠加/矢量相加的讨论在第 30 章，英文为 Chapter 30 | "adding a lot of arrows at different angles (Chapter 30)" | 改作"（第30章）" |

## 低严重度修正（已修）

- L59："假定有**一**像在讨论光时讲到的那样的荷电振子" → "假定有**一个**像…"（缺量词，句子不完整）。
- L125："这样一个能**等价地**在三个方向上振动的振子" → "能**同样地**…"（英文 "oscillate equally in three directions"；该处"等/价地"被 wrapfigure 分隔）。
- L250："只取一维运动求出$x^2$的平均值，**以作备考**" → "**以作准备**"（英文 "just to prepare ourselves"；"备考"义为应考，语义不符）。

## 存疑项（未改）

1. **L277**"$1~mol$ 原来的定义是这么多克的氧——$16~g$（现在用碳）" ← "so and so many grams of oxygen-16 (now carbon is used)"：英文指同位素氧-16，"16 g" 丢失同位素含义（数值上 1 mol O-16 恰为 16 g）；底本如此，未改。
2. **L155**"一定有某些东西从根本上**明显地**和绝对地错了" ← "fundamentally, powerfully, and absolutely wrong"：powerfully 译"明显地"语义略偏（可作"严重地、强有力地"）；底本如此，未改。
3. **L171**"能级彼此分开相等的间隔$\hbar\omega$"（英文为 ℏω0；同页图注英文亦作 ℏω）：ω 与 ω0 混用，属底本记号不统一，未改。

## 覆盖性结论

- **段落/完整性**：4 节与英文 41–1～41–4 一一对应；逐句核对**无漏句、无漏段、无重复粘贴**；候选"大块差异"均为图注/页眉错位噪声。
- **公式**：21 个编号公式 (41.1)–(41.21) 及 11 个无编号公式逐式与英文核对，**全部正确**（本次未改任何公式内容）。重点：
  - 能量均分：$\langle\theta^2\rangle=kT/(I\omega_0^2)$ (41.1)；$\langle V_L^2\rangle=L\omega_0^2kT$ (41.2)；$P(\omega)d\omega=(2/\pi)kTd\omega$ (41.3)。
  - 辐射热平衡：$1/Q=(dW/dt)/(\omega_0W)=\gamma/\omega_0$；$\gamma=(2/3)r_0\omega_0^2/c$ (41.6)；$dW/dt=(2/3)r_0\omega_0^2kT/c$ (41.7)；$\sigma_s=\frac{8\pi r_0^2}{3}\frac{\omega^4}{(\omega^2-\omega_0^2)^2+\gamma^2\omega^2}$ (41.8)、近似式 (41.9)、(41.10)；$I(\omega_0)=\frac{9\gamma^2kT}{4\pi^2r_0^2\omega_0^2}$ (41.12)；$I(\omega)=\omega^2kT/(\pi^2c^2)$ (41.13)。
  - 量子振子：$\langle E\rangle=\frac{N_0\hbar\omega(0+x+2x^2+\cdots)}{N_0(1+x+x^2+\cdots)}$ (41.14)；$\langle E\rangle=\frac{\hbar\omega}{e^{\hbar\omega/kT}-1}$ (41.15)；$I(\omega)d\omega=\frac{\hbar\omega^3d\omega}{\pi^2c^2(e^{\hbar\omega/kT}-1)}$ (41.16)。
  - 无规行走：$\langle R^2\rangle=\alpha t$ (41.17)；$\langle R_N^2\rangle=NL^2$ (41.18)；$m\ddot x+\mu\dot x=F_{\text{外}}$ (41.19)；$d\langle x^2\rangle/dt=2kT/\mu$ (41.20)；$\langle R^2\rangle=6kTt/\mu$ (41.21)。
- **数字/量纲**：1827、$3kT/2$、$1\text{–}2~\mu m$、$1~mm\!\cdot\!s^{-1}$、$Q\approx10^8$、$10^{14}$ 次/s、$10^{12}$ 次/0.01 s、$16~g$、$1~mol$、$PV=RT$ 均与英文一致；无数字错误。
- **图/引用**：6 幅图（41.1–41.6）齐全、图注与英文一致；正文图引用全部经 `\ref` 解析；跨章公式引用 4 处（(19.8)、(32.8)、(32.12)、(32.19)）经 xr 解析；无表格。
- **人名/术语**：布朗（Robert Brown）、爱因斯坦、斯莫卢霍夫斯基、玻尔兹曼、金斯（Sir James Jeans）、普朗克、麦克斯韦、约翰逊、瑞利、阿伏伽德罗；能量均分、约翰逊噪声、黑体辐射、瑞利定律、截断因子、量子振子、无规行走、玻尔兹曼常量等均正确。
- **自动候选差异**：37 条 CJK 级差异全部是参考文本 OCR 误（悟/司、贮/凤、另/男、悬/基、停/售、叩/员、爵/狠、谬/雇、踉踉跄跄/跟跟踊踊、卢/户、测/调 等），**不据以改动**。

## 验证

- 入口：`preview/chapter-41/check.tex`（`make_chapter_check.py 41` 生成；注释改为《布朗运动》、`cd` 路径 chapter-41；另加 `\usepackage{xr}` + `\externaldocument` Chapter19、Chapter32 解析跨章公式引用，依赖两章 `.aux`）。
- 命令：`cd preview/chapter-41 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：13 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；PDF 中"??"0 处；图号 41.1–41.6 全部存在。
- PDF 抽查：修正点均生效（"这也总是涨落的起源""无规则地来回跳动""（第 30 章）""假定有一个像…""能同样地…""以作准备"）；旧串（"常常也就是""有规则地""第32章""以作备考"）出现 0 次；跨章引用渲染为（19.8）（32.8）（32.12）（32.19）。
