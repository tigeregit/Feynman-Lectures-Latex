# 第 21 章《谐振子》审查报告

- **范围**：`Chapters/VolumeI/Chapter21.tex`（原 185 行，5 节：线性微分方程 / 谐振子 / 简谐运动和圆周运动 / 初始条件 / 受迫振动）；对照 `_attachments/build-feynman/audit/en/I_21.txt`（正文 L36–L225）。
- **旁证**：`_attachments/reference/zh/Chapter21.txt`（公开中译本 OCR，仅用于区分"底本译法/底本笔误"与"本仓库讹变"）；`_attachments/reference/candidates/ch21-candidates.md`（小块 196 条、大块 38 条，逐条判定；绝大多数为参考文本自身 OCR 噪声——公式与上下标整体丢失——判"参考误"者未采纳）。
- **段落对应**：英文 5 节 **18 个正文段**（另 3 条图注、12 个编号公式、若干无编号公式）；中文 **42 个段落块**——底本体例为"按句/按公式分段"，故中文段数约为英文 2.3 倍；逐句核对**无漏句、无漏段、无重复粘贴**。
- **结果**：修正 **7 项**：**中 2 / 低 5**；另存疑 4 项；12 个编号公式逐一核对**未发现公式错误**（"公式内勿误改"，未动任何公式内容）。
- **单章编译**：`preview/chapter-21/check.tex`（`tools/make_chapter_check.py 21` 生成；校正章名/路径注释）连编 2 遍：**8 页，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（修正前基线有 2 处跨章未定义引用，见"验证"）；`git diff` 仅 Chapter21.tex（+7/−7 行，CRLF 保持），未动其他章、未 commit。

## 已修问题（行号为修改前 `Chapter21.tex` 行号）

| # | 行号 | 严重度 | 类型 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|---|---|
| 1 | L73 | 中 | 误译 | "让我们**各有各的说法吧**！"——把 "Let us put it differently."（换一种说法）误读为"各人有各人的叫法"，与下句"不同的 Δ 对应不同相位的运动"（对同一事的另一种表述）不接 | "We might say that Δ is a phase shift from some defined zero. Let us put it differently. Different Δ's correspond to motions in different phases." | 我们换一种说法吧。 |
| 2 | L105 | 中 | 图/式引用 | "人为地给式（**21.3**）再补充一个用 y 表示的方程式"——原文为 Eq. (21.2)（1963 初版与 eFLP 官网均作 21.2；底本误作 21.3） | "we may still artificially supplement Eq. (21.2) with another equation using y" | 人为地给式（`\ref{Eq:I:21:2}`）再补充… |
| 3 | L36 | 低 | LaTeX/结构 | "又一次得到了式（**21.3**）"——硬编码式号（同句前一处已用 `\ref`） | "we got Eq. (21.3) again!" | 式（`\ref{Eq:I:21:3}`） |
| 4 | L38 | 低 | LaTeX/结构 | "要得到**x**项前有不同系数的方程"——正文裸变量 x 未入数学模式 | "an equation with a different constant multiplying x" | 要得到 $x$ 项前… |
| 5 | L43 | 低 | 漏字 | "；**我们**记住 ω₀ 与这个振子的固有运动有关"——漏"让"（let us remember） | "let us remember that ω0 refers to the natural motion of this oscillator" | ；让我们记住… |
| 6 | L77 | 低 | LaTeX/结构 | "在某一给定时刻的位置**x**是圆的半径乘 cosθ"——裸变量 x（同句 y 已用 `$y$`） | "the position x, at a given moment, is the radius of the circle times cosθ" | 位置 $x$ 是… |
| 7 | L175 | 低 | LaTeX/结构 | "只要**C**取得适当"——裸变量 C（同段其余 C 均为 `$C$`） | "provided we pick C just right" | 只要 $C$ 取得适当 |

## 存疑项（未改，建议上游确认）

1. **L38 "经过小小的挫折和一番尝试后"**（"After a little cut and try"）：`cut and try` 意为"试凑、反复尝试"，"挫折"系字面直译；底本即如此，未重写（建议可作"经过一番试凑之后"）。
2. **L36 "令人惊讶的是"**（"Thus we discover to our horror"）：底本用"惊讶"弱化了原文的夸张幽默，未改。
3. **L155/L160 "外策力"**（"external driving force"）：底本用词（旧译），现代通行作"驱动力/策动力"，本章两处一致，未改。
4. **图 21-2 / 图 21-3 合并在同一个 `figure` 环境**：按 eFLP，图 21-2 在其讨论段前、图 21-3 在演示实验段之后；现版两块 minipage 同处一浮动体，PDF 中图 21-3 浮于其描述段之前（跨页版式可接受，未拆分，避免过度改动）。
5. **L73 "1s 内"**：单位与数字连排（`1s`），不影响语义，未改。

## 覆盖性结论

- **完整性**：逐句核对英文 18 个正文段全部句子，无整段/整句缺失、无重复粘贴；中文按句分段（42 段）属底本体例。节标题 5 个与 eFLP 一致（线性微分方程 / 谐振子 / 简谐运动和圆周运动 / 初始条件 / 受迫振动）。
- **公式核对**（12 个编号公式 + 全部行内式，逐式与英文对照，**均正确**）：21.1（n 阶常系数线性方程）、21.2（md²x/dt²=−kx）、21.3、21.4、21.5（t₀=2π√(m/k)）、21.6（(a)(b)(c) 三种通解，编号落在 (b) 行、`\ref` 解析为 21.6）、21.7（a_x=−ω₀²x）、21.8、21.9、21.10、21.11、21.12（C=F₀/[m(ω₀²−ω²)]）；行内式含 dt 链式法则、A=a cosΔ、B=−a sinΔ、x₀=A、v₀=ω₀B、U=½ka²cos²、T=½mω₀²a²sin²、T+U=½mω₀²a² 均一致。
- **数字/物理结论**：t=1.570 → 周期 6.28"秒"、t=π/2=1.57080、t₀=2π/ω₀、能量∝振幅平方（2 倍振幅→4 倍能量）、平均动能=平均势能=总能量一半、共振时 C→∞——全部与英文一致。
- **图**：3 图齐备；图注与 eFLP 官网逐条核对一致（Fig. 21-1 "A mass on a spring…"、21-2 "A particle moving in a circular path at constant speed."、21-3 "Demonstration of the equivalence…"）；图号 21.1–21.3 与 eFLP Fig. 21-1～21-3 顺序一致，3 处 `\ref` 全部解析。
- **交叉引用**：2 处跨章引用——式 (9.12)（`\label{Eq:I:9:12}`，Chapter9.tex 存在）与图 9-4（`\label{figure:悬于弹簧上的重物运动曲线}`，Chapter9.tex 存在，第 9 章第 4 图）；全书编译可正常解析（单章入口用占位标签，见下）。
- **表**：本章无表。

## 验证（单章编译）

| 项目 | 结果 |
|---|---|
| 入口 | `preview/chapter-21/check.tex`（工具生成；校正注释；为跨章的式 9.12、图 9.4 加 phantom 标签占位） |
| 编译 | `xelatex -no-mktex=tfm -interaction=nonstopmode` 连编 2 遍 |
| 页数 | **8 页**（修正前基线亦 8 页） |
| error | **0** |
| Overfull / Underfull | **0 / 0** |
| Missing character | **0** |
| undefined references | **0**（修正前基线为 2：`Eq:I:9:12`、`figure:悬于弹簧上的重物运动曲线`；已由单章入口的幻影标签解决，正文仍用 `\ref`，全书编译不受影响） |
| 其他 | PDF 中无 `??`；跨章引用渲染为"式（9.12）"、"图 9.4" |
| 改动范围 | `git diff` 仅 `Chapters/VolumeI/Chapter21.tex`（+7/−7 行，CRLF）；`preview/chapter-21/` 为新增；未 commit、未跑全书 |

**未改动项**：存疑 1–5；"外策力"等底本旧译、"象/像"字形等全书问题未在本章单独处理。
