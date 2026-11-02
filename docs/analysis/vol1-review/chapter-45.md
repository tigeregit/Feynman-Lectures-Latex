# 第 45 章《热力学示例》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter45.tex`（原 275 行；3 节 45-1～45-3；修后 276 行，**LF 行尾保持原状**，无 CRLF）
- 英文：`_attachments/build-feynman/audit/en/I_45.txt`（正文 L36–L393；公式在抓取文本中被拆成分数/符号碎片；图注 L115、L121、L258、L262；脚注①在 L395，脚注②在 L396–L420）
- 旁证：`_attachments/reference/zh/Chapter45.txt`（公开中译本 OCR，单行，本身有错）；`_attachments/reference/candidates/ch45-candidates.md`（小块 323 条、大块 44 条，已逐条对照英文判定）
- 段落对应：英文正文 42 个段落块（不含 4 条图注、2 条脚注），中文 29 个叙述段（另 3 个图环境）。底本存在段落合并：L120–138 合并英文 L191/L193/L204 三段；L166–190 合并英文 L228/L235/L245/L252 四段；逐句均可对应，无整段缺失。

## 结果

- **已修正 22 条（高 7 / 中 7 / 低 8）**；其中 45-02 含 2 处，45-22 为版式修正；**存疑 5 项**（未改）。
- 单章编译：**11 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍；另补第 3 遍以消除 `Label(s) may have changed` 的 rerun 警告）。
- 修改文件：`Chapters/VolumeI/Chapter45.tex`、`preview/chapter-45/check.tex`（仅注释：章名改《热力学示例》、`cd` 路径改 chapter-45）、本报告。未 commit，未运行全书构建。

## 高严重度（已修，7 条）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L15 | “写成下标：$(\partial P/\partial T)V$”中 $V$ 未作下标，渲染为乘 $V$ | “write the variable that is held constant as a subscript, (∂P/∂T)V” | `$(\partial P/\partial T)_V$` |
| 2 | L55 | 两处 `$(\partial U/\partial T) V$` 同样把下标 $V$ 排成普通变量 | “ΔU=(∂U/∂T)VΔT, so that (∂U/∂T)V=ΔQ/ΔT” | 两处均改 `$(\partial U/\partial T)_V$` |
| 3 | L133 | “分别以 $A$、$B$ 代替 $P$、$V$”漏负号；类比式是 $\Delta U=\Delta Q+A\Delta B$ 对应 $\Delta U=\Delta Q-P\Delta V$ | “substituting A and B for −P and V” | “代替 $-P$、$V$” |
| 4 | L212 | 阴影面积写作 `$\Delta P (VG -VL)$`，$V_G$、$V_L$ 的字母连排成乘积 | “approximately ΔP(VG−VL), where ... VG is the volume of the gas” | `$\Delta P (V_G -V_L)$` |
| 5 | L223 | “通常 $VG$ 远大于 $VL$，所以 $V_G-V_L=V_G$”既有同样的下标错误，又把近似式写成等式 | “VG−VL≈VG=RT/P per mole” | `$V_G$`、`$V_L$`；第一处 `=` 改 `\approx` |
| 6 | L232 | $n$ 的定义漏“每单位体积”，与式 (45.16) 的分子数密度及 $P=nkT$ 矛盾 | “the number of molecules per unit volume of vapor above a liquid” | “液面上方单位体积蒸气中的分子数” |
| 7 | L237 | 漏英文段末句：潜热 $L$ 与 $U_G-U_L$ 及 $P(V_G-V_L)$ 的关系（焓差的由来） | “the change in internal energy UG−UL is equal to the heat L put in minus the work done P(VG−VL)”；“L=(UG+PVG)−(UL+PVL)” | 补“由于在体积改变时压强保持不变…所以 $L=(U_G+PV_G)-(U_L+PV_L)$。” |

## 中严重度（已修，7 条）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 8 | L63 | “在温度T 下”为裸变量 $T$ | “as it expands isothermally at temperature T” | “温度$T$下” |
| 9 | L129 | “把带子拉长一点点”与英文 relaxed（放松）方向相反；拉伸时橡胶放热，放松时才需吸热 | “when the band is relaxed a little bit” | “把带子放松一点点” |
| 10 | L138 | “电池的电压E 呢”为裸变量 $E$ | “Why is ΔU/ΔZ not simply the voltage E of the battery?” | “电压$E$呢” |
| 11 | L140 | performance 误译成“各种特殊性”，句子无着落 | “they prefer equations which describe performance under constant pressure” | “他们喜欢描述等压性能的方程” |
| 12 | L185 | 漏“per mole”；$P=RT/V$ 只对一摩尔成立 | “the pressure per mole is equal to P=RT/V” | “对于一摩尔理想气体，压强等于” |
| 13 | L245 | 漏英文脚注 1（黑体辐射中 $(\partial P/\partial V)_T=0$ 的解释）；中文只剩数学脚注 | “In this case (∂P/∂V)T=0 ... regardless of the volume of the box.” | 补 `\footnote{…}`；原脚注自动变为 2 |
| 14 | L205 | 初改后图 45.4 的 `wrapfigure` 落到第 8 页底部，图注越出页面被裁切；编译统计不报此类问题 | 英文图注完整；PDF 第 8 页底部可见裁切 | 图前加 `\clearpage`，图回到第 9 页顶部，图注完整（第 8 页底留白约 5 行） |

## 低严重度（已修，8 处）

- L55：“所须加入物质中的热量”→“所需…”（“须/需”形近，底本同）
- L138：“我们来看看热力学能对电池内的性能说些什么”→“我们来看看热力学对电池的性能说些什么”（“热力学能”易误读为内能）
- L201、L203：“压力足够大”“保持压力不变”→“压强…”（2 处；全章另有 45 处“压强”）
- L219：`P_\text{蒸汽}`→`P_\text{蒸气}`（与全章 33 处“蒸气”统一）
- L241：`P_\text{溶解}`→`P_\text{熔解}`（英文 Pmelt；与“熔解潜热”“熔解过程”统一）
- L250：“Stefan-Boltzman”→“Stefan-Boltzmann”（英文拼写）
- L7：“物理化学，蒸发，气体液化等段落”→“物理化学、蒸发、气体液化等段落”（并列名词用顿号）

## 存疑项（未改）

1. **L5“热力学的应用是一门相当困难和复杂的课题”** ← “Thermodynamics is a rather difficult and complex subject when we come to apply it.”：中文把“应用”作主语，底本译法；未改，若严格对齐可作“热力学在应用方面…”。
2. **L138“别致的方法”** ← “a nifty way”：别致偏“独特/雅致”，“巧妙”更贴；同句“产生一种化学反应” ← “produce a chemical reaction”亦略生硬。属底本译风，未改。
3. **L241 熔解公式的下标 $V$**：`(∂P_\text{熔解}/∂T)_V` 与 eFLP 原文 `(∂Pmelt/∂T)V` 一致；相变斜率通常沿共存线求而非定容，疑为原文记号瑕疵，按“公式原则上不改”保留（只改 $P$ 的下标用字）。
4. **L198 图 45.3 图注**：末句“在中央部分，液体和蒸气并存”漏英文“in the cylinder”；图注开头已说“在汽缸中进行压缩”，未补。
5. **L190“许多时候人们往往总是自找麻烦”**：“往往”与“总是”语义重复；底本译风，未改。

## 覆盖性结论

- **段落/完整性**：3 节与英文 45–1～45–3 对应；逐句核对无漏段、无重复粘贴；已补回英文段末句（L237）与脚注 1（L245）。底本段落合并见“范围与材料”，内容无缺。
- **公式**：编号公式 45.1–45.17 全部存在；逐式核对——45.1 的 $\Delta f$ 分解、45.5 的卡诺论证（含 $\Delta V\Delta P=\Delta Q\Delta T/T$ 与 $T(\partial P/\partial T)_V$）、45.7、45.9、45.14–45.17 均正确；除 45-02、45-15 的下标与 $\approx$，以及 45-14/45-18 的 $P$ 下标用字外，未改公式结构。45.4、45.11、45.17 未被正文 `\ref` 引用但 label 正常，不影响编译。
- **数字/单位**：$6.5$、$\pi^4/15$、$\pi^4/90$、$\sigma=5.67\times10^{-8}\ \mathrm{W\cdot m^{-2}\cdot K^{-4}}$、$4\sigma/c$、$1/4$、$1/2$、$RT^2$、$PV=U/3$、$U=3PV$ 均与英文一致。
- **图表**：图 45.1–45.4 齐全；4 条图注与英文逐句对照；全部 `\ref` 解析（0 undefined）；图 45.4 版式已修；本章无表格。
- **术语/人名**：泽曼斯基、克劳修斯-克拉珀龙、斯特藩-玻耳兹曼、焓、定容比热、蒸气压、动理温度等与英文一致；已修 performance/relaxed/“每摩尔”/“每单位体积”四处语义问题。
- **候选差异**：323 小 + 44 大，绝大多数为参考文本 OCR 噪声或公式/图注剥离；未据参考文本改动任何一处，参考的讹字（蒸/蒜、熵/炉、膨胀/脱胀、焓/熔、幂/宕等）均判为参考误、保留本库正确写法。

## 验证

- 入口：`preview/chapter-45/check.tex`（`\setcounter{chapter}{44}`、`\input{../../Chapters/VolumeI/Chapter45.tex}`；本次仅修正注释）。
- 命令：`cd preview/chapter-45 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍；第 3 遍消除 rerun 警告）。
- 结果：**11 页 A4；error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0；第 3 遍后 `Label(s) may have changed` 亦为 0**。
- 源文件/PDF 抽查：旧串（`$VG$`、`$VL$`、`P_\text{蒸汽}`、`P_\text{溶解}`、`Stefan-Boltzman`、“拉长一点点”、“各种特殊性”、“电压E ”）出现 0 次；新串（“放松一点点”“代替 −P”“等压性能”“一摩尔理想气体”“单位体积蒸气”“体积改变时压强保持不变”“Stefan-Boltzmann”）均已出现；第 9 页图 45.4 图注完整、第 10 页脚注 1 正常。
- 行尾：字节检查 `CRLF=0`，仍为 LF；修后 276 行（+1 行为 `\clearpage` 版式修正）。
- 未 commit，未运行全书构建；仅改上述正文、入口注释与本报告。
