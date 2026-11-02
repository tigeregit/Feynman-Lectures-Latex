# 第 49 章《波模》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter49.tex`（修改前 218 行 / 26890 B → 修改后 216 行 / 26885 B；5 节 49-1～49-5：波的反射 / 具有固有频率的约束波 / 二维波模 / 耦合摆 / 线性系统；按语义约 33 段）
- 英文：`_attachments/build-feynman/audit/en/I_49.txt`（正文 L36–L268；抓取文本中公式被拆成分数/指数碎片，图注与表注独立成行）
- 旁证：`_attachments/reference/zh/Chapter49.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch49-candidates.md`（223 小块 + 33 大块，已逐条核对）
- 公式核对方式：eFLP 文本片段 + 反射/驻波、简正频率、矩形膜本征值、耦合摆方程独立复核
- **行尾**：本章为 LF（第 44–52 章均如此）；修改前后均 CRLF=0、末尾无换行，**未转 CRLF**
- 单章入口：`python3 tools/make_chapter_check.py 49` 确认 `preview/chapter-49/check.tex` 已存在，注释章名《波模》、`cd preview/chapter-49`、`\setcounter{chapter}{48}`、`\input{../../Chapters/VolumeI/Chapter49.tex}` 均正确；入口文件未改动

## 结果

- **已修正 10 条（12 处；高 2、中 4、低 4）**；**存疑 6 项**（未改）；**公式 0 改动**。
- 单章编译：**10 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter49.tex`（7 增 / 9 删，LF 保持）、`preview/chapter-49/build/`（重建）、本报告；**未 commit**，未动其他章、图文件或工具。
- 修正脚本：`/tmp/fix_ch49.py`，12 条替换逐条断言 `old` 恰命中 1 次，先 dry-run 打印 diff 再 `--apply`。

## 已修问题

| # | 级别 | 行号 | 问题 | 英文依据（逐字） | 修正 |
|---|---|---|---|---|---|
| 1 | 高 | L7 | "现在，如果对于墙来说不是这样"把"if it were not for the wall"误译成"对墙而言不是这样"，语义不通 | "Now if it were not for the wall, we know that the general solution for the motion is…" | "现在，如果没有那堵墙，那么我们知道运动的通解是……" |
| 2 | 高 | L80 | 漏"第"："两种模式的振动"与上句（第一种模式已在振动）、下句"这种模式"矛盾 | "Now, at the same time, we suppose that there is an oscillation of the second mode also." | "……同时还存在着**第二种**模式的振动。" |
| 3 | 中 | L157 | "声带上部是腔体"：above the vocal cords 是"声带上方"，不是声带的"上部" | "inside the mouth we have a cavity above the vocal cords" | "……声带**上方有一个腔体**……" |
| 4 | 中 | L219 | "就像弦的约束波一样。"独立成句，与下句割裂；英文中是同一句的状语 | "Like the confined waves of a string, there are definite frequencies for the solution of the wave equation for quantum mechanics." | 句号改逗号，并入："就像弦的约束波一样**，**量子力学波动方程的解中存在许多确定的频率。" |
| 5 | 中 | L88–L95 | 图 49-4 的 wrapfigure 插在"……一步是对 / [图] / 二维情况进行讨论"之间，句子被图截断 | "an easier step will be that to two dimensions" | 图移到该段段首，恢复"……一步是对二维情况进行讨论。" |
| 6 | 中 | L161–L168 | 图 49-5 的 wrapfigure 插在"非常简单的力学 / [图] / 系统"之间，词被图截断 | "not only do modes exist for complicated continuous systems, but also for very simple mechanical systems" | 图移到该段段首，恢复"……非常简单的力学系统也存在着波模。" |
| 7 | 低 | L157 | "在改变发声中的极端重要性"结构不成句（"在……中"不能作"重要性"的定语） | "The very great importance of the resonant frequencies of a cavity in modifying the voice sounds…" | "在改变发声**方面**的极端重要性" |
| 8 | 低 | L168 | 两个并列定语之间误用逗号，读成残句 | "a simple mechanical thing which has only two degrees of freedom, and requires only two variables to describe it, has only two modes" | "仅有两个自由度**、**只要求用两个变量来描述的一个简单的力学系统……" |
| 9 | 低 | L95 | "界面"（interface）应为"边界"（boundary），与本章"边界条件/矩形边界"不一致 | "Our first example of confining waves will be to confine a wave at one boundary." | "使波动在一个**边界**上受到限制" |
| 10 | 低 | L115 | "由波长，可立刻"逗号位置不当 | "from the wavelength we immediately get the frequency ω" | "同时由波长可立刻得到频率$\omega$" |

> 行号为修改前；#5、#6 为纯排版移动（图块本身未改），修改后第 5、8 页版式已逐页目视复核。

## 存疑项（未改）

1. **L124 "具有这种很长的形式"** ← "takes on the grand form"：grand 带反讽（"堂皇的/洋洋大观的形式"），"很长"是直译偏差；改动涉及语气，未改。
2. **L155 "固有频率间具有谐和地相关的概念"** ← "The idea that the natural frequencies are harmonically related…"：`谐和地相关`状语用法生硬，宜作"谐和相关的"；属底本措辞，未改。
3. **L168 "如果我们知道如何计算无穷大"** ← "if we know how to count infinities"：count 宜作"数（无穷大）"，"计算"不确；底本措辞，未改。
4. **L215 "它可能包含了数学物理的最普遍、最奇妙的原理的所有方面"** ← "which are all aspects of what is probably the most general and wonderful principle of mathematical physics"：主语与"可能"的辖域均偏移（宜作"这些概念也许都属于……的各个方面"）；改动较大，未改。
5. **L219 "存在许多确定的频率"**：英文仅 "definite frequencies"，"许多"为底本增饰；非事实错误，未删（本次只修同句断句）。
6. **图 49.4 内嵌文字"波边缘夹住"**：疑多一"波"字（应作"边缘夹住"/"波被边缘夹住"）；所在 `Figures/VolumeI/Chapter49/振动的矩形板.pdf` 不在本次允许修改范围，未改，建议后续修图。

## 覆盖性结论

- **段落/完整性**：5 节与英文 49–1～49–5 一一对应；把公式独立成行的排版段按语义合并后，中英段落逐段对应（中文 33 个语义段），逐句核对**无漏句、无漏段、无重复粘贴**。
- **公式**（未改动，逐式核对）：49.1–49.18 全部正确（含 49.11a/b）；49.11a 第四项 `+e^{(+ik_xx-ik_yy)}` 与英文一致（既有提交 bc997ae 已修正符号）；49.9、49.12 的推导与三角形关系复核无误。
- **物理表述**：49-1 反射与驻波（$y=F(x-ct)-F(-x-ct)$、节点条件）、49-2 简正频率 $\omega_n=n\pi c/L$、49-3 二维矩形膜 $1/\lambda^2=n^2/4a^2+m^2/4b^2$ 及 $a=2b$ 时的 $\omega^2$、49-4 耦合摆两模式 $\omega_0$ 与 $\sqrt{\omega_0^2+2k/m}$、49-5 线性系统与量子力学类比，逐节核对无物理错误。
- **图表**：5 幅图（49.1–49.5）+ 表 49.1 齐全，图注/表注与英文 Fig. 49–1～49–5、Table 49–1 对应；正文 9 处图引用、1 处表引用、20 处公式引用全部解析（0 undefined），无硬编码编号；表 49.1 五组 $(\omega/\omega_0)^2$=1.25/2.00/3.25/4.25/5.00、$\omega/\omega_0$=1.12/1.41/1.80/2.06/2.24 与式（49.12）相符。图 49.4 内嵌文字问题见存疑 6。
- **数字/术语**：2L、L、$\pi c/L$、2ω₁、3ω₁、90°、$m=0,1,2,\cdots$、$n$ 与 $m$ 的取值等均与英文一致；波节/波腹/驻波/模式/固有频率/耦合摆等术语正确。
- **自动候选差异**：223 小块 + 33 大块绝大多数为公式剥离噪声与参考 OCR 讹字（弦→驴/纺/骇、氦→氯/氢、叠→亚/合/全、另→男、句→旬/名、乘→生 等），**不据以改动**；确属本仓库的问题即上表 10 条。

## 验证

- 入口：`preview/chapter-49/check.tex`（`\setcounter{chapter}{48}`、`\input{../../Chapters/VolumeI/Chapter49.tex}`；工具确认已存在，未改）。
- 命令：`cd preview/chapter-49 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：10 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；日志中的 SimSun 探测与 STHeiti 字形 warning 为已知噪音。
- PDF 文本抽查：修正点均生效（"如果没有那堵墙""第二种模式的振动""声带上方有一个腔体""在改变发声方面""一样，量子力学波动方程""仅有两个自由度、""一个边界上""由波长可立刻"）；旧串（"对于墙来说不是这样""两种模式的振动""声带上部是腔体""改变发声中的""一样。量子力学""仅有两个自由度，只要求""界面上受到限制""由波长，可立刻"）出现 0 次。
- LF：bytes 26890→26885，CRLF=0，末尾无换行；`wc -l` 218→216。
- **未 commit**；除 `Chapters/VolumeI/Chapter49.tex`、`preview/chapter-49/build/` 与本报告外，未修改任何文件（`preview/chapter-49/check.tex` 未变动，`Figures/` 未动）。
