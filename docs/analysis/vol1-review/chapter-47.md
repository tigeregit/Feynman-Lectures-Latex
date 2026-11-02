# 第 47 章《声、波动方程》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter47.tex`（248 行；5 节 47-1～47-5：波 / 声的传播 / 波动方程 / 波动方程的解 / 声速；编号公式 47.1–47.26 共 26 个；图 47.1–47.4 共 4 幅）
- **行尾：LF（第 44–52 章惯例），修改全程保持 LF，未转 CRLF**
- 英文：`_attachments/build-feynman/audit/en/I_47.txt`（371 行；公式抓取为分式碎片，逐式按片段 + 上下文核对）
- 旁证：`_attachments/reference/zh/Chapter47.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch47-candidates.md`（188 小块 + 45 大块，已逐条判定）
- 公式核对方式：eFLP 文本片段逐式比对 + 编译后 PDF 渲染号核对

## 结果

- **已修正 5 条（中 3、低 2；无高严重度）**；**存疑 6 项**（未改）。
- 单章编译：**10 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter47.tex`（5 行 5 处，**LF 保持原状**；`CRLF=0 / LF=248`）；`preview/chapter-47/check.tex`（仅注释：章名《声、波动方程》、`cd` 路径、验收标准行；本章无跨章引用，无需引用桩）；本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L45 | "假定高频的声音传播得比低频的快，那么短促尖锐的噪声将**发生在乐声之后**"——语义错误（不是"顺序发生在后"，而是会被听成一串乐音）；底本即误 | "If we had high frequencies travelling faster than low frequencies, a short, sharp noise would be **heard as a succession of musical sounds**." | "……那么短促尖锐的噪声**听起来就会像一连串的乐音**。" |
| 2 | L73 | $1~\text{atm}=1.013~3~\text{bar}$——`~` 把 "1.0133" 断开，实际渲染为"1.013 3 bar"（错误数字） | "1 atm=1.0133 bars" | $1~\text{atm}=1.0133~\text{bar}$ |
| 3 | L189 | "$\chi_1$对$x$的二阶微商**等于乘以**$\chi_1$对$t$的二阶微商"——漏掉因子 $\frac{1}{c_s^2}$，句子不完整/失真 | "the second derivative of χ1 with respect to x is equal to **1/c²_s times** the second derivative of χ1 with respect to t" | "……等于$\frac{1}{c_s^2}$乘以$\chi_1$对$t$的二阶微商。" |

## 低严重度（已修）

- L31："当初开始描写波现象时，我们并没有**指出**波在传播这一点"——eFLP 为 "did not notice"（没有注意到），非"指出"；改为"……我们起初并没有**注意到**其中有波的传播"。
- L232："它也可表示为$Nm$**或$\mu$**"——英文 "or as μ **per mole**"；改为"$Nm$，或**每摩尔的**$\mu$"。

## 存疑项（未改）

1. **L45 的底本误译**：中译本同样作"噪声将发生在乐声之后"；本次按 eFLP 改为"听起来像一连串乐音"，与底本不同，供 Lead 复核。
2. **式（47.1）用 $\lg$** 表示 $\log_{10}$（英文写作 log10）；中文数学惯例可接受，保留。
3. **"声压级$I$"**：英文符号亦为 I（"I(acoustic pressure level)=20log10(P/Pref) in dB"），与后文强度符号无冲突，保留。
4. **L232"$\mu$是分子量"**：英文 footnote 3 定义 molecular weight 为"1 mol 分子的克质量"，中译本作"分子量"，保留。
5. **图 47-3 图注中的 `\\` 换行、图 47-4 图注中的分式写法**：底本排版如此，未改。
6. **L139"（图\ref{…}）"** 的位置与英文 "…(Fig. 47–4):" 一致；本章仅 4 处图引用，无公式 `\ref`、无跨章引用，故无引用桩问题。

## 覆盖性结论

- **段落/完整性**：5 节与英文 47–1～47–5 逐段对应；无漏段、无漏句、无重复粘贴。候选"大块差异"45 条全部为公式剥离/图注/页眉噪声，逐条确认无正文缺失。
- **公式**：26 个编号公式 47.1–47.26 全部存在，编译渲染号与 eFLP 编号一一对应。逐式核对：
  - 47.1（声压级 $I=20\lg(P/P_\text{参})$ dB）、47.2（$P=P_0+P_e,\ \rho=\rho_0+\rho_e$）、47.3（$f(\rho_0+\rho_e)=f(\rho_0)+\rho_ef'(\rho_0)$）、47.4（$P_e=\kappa\rho_e$，$\kappa=(dP/d\rho)_0$）；
  - 47.5–47.9（质量守恒 → $\rho_e=-\rho_0\partial\chi/\partial x$）；47.10–47.11（薄层受力与运动方程）；
  - 47.12–47.14（消去 $P_e,\rho_e$ → 波动方程 $\partial^2\chi/\partial x^2=(1/c_s^2)\partial^2\chi/\partial t^2$）；
  - 47.15–47.19（$f(x-vt)$ 代入验证、左右行波、叠加原理）；47.20（光波方程）；
  - 47.21–47.26（声速：$c_s^2=(dP/d\rho)_0$、$P=\text{const}\,\rho^\gamma$、$c_s^2=\gamma P/\rho$、$c_s^2=\gamma kT/m=\gamma RT/\mu$、$kT=\frac{1}{3}m\langle v^2\rangle$、$c_s=(\gamma/3)^{1/2}v_\text{平均}$）。
  **系数、符号、上下标与 eFLP 一致**；仅上表第 2、3 条排版/漏字问题已修。
- **数字/单位**：$1~\text{bar}=10^5~\text{N}\cdot\text{m}^{-2}$；$1~\text{atm}=1.0133~\text{bar}$；$P_\text{参}=2\times10^{-10}$ bar；$P=10^3P_\text{参}=2\times10^{-7}$ bar ↔ 60 dB；100 dB/120 dB；$\gamma$；$1/\sqrt{3}$；$1/2$ 等均与 eFLP 一致（"1.013 3" 渲染错误已修）。
- **图**：4 幅（47.1–47.4）齐全，图注与英文一致；4 处图引用全部经 `\ref` 解析（0 未定义）。
- **术语**：声压级/声强级、分贝、等温/绝热、平均自由程、叠加原理、概率振幅、方均速率、分子量等与英文一致。
- **自动候选差异**：188 小块 + 45 大块绝大多数为参考文本 OCR 讹字与公式剥离噪声，**不据以改动**；确属本仓库的问题即上表/低严重度共 5 条。

## 验证

- 入口：`preview/chapter-47/check.tex`（`\setcounter{chapter}{46}`、`\input{../../Chapters/VolumeI/Chapter47.tex}`；本次仅修正注释章名/路径/验收标准行）。
- 命令：`cd preview/chapter-47 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：10 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；行尾复核 `CRLF=0 / LF=248`（未转 CRLF）。
- PDF 文本抽查：修正点均生效（"1atm=1.0133bar""听起来就会像一连串的乐音""等于1/c_s²乘以""起初并没有注意到其中有波的传播""或每摩尔的μ"）；旧串（"1.013 3""将发生在乐声之后""等于乘以""并没有指出""或μ"）出现 0 次。

## 未改动与建议

- 存疑 1–6 建议保持；本章无需跨章引用桩。
- 修改集中在 5 行（5+/5−），便于复核 diff。
