# 第 50 章《谐波》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter50.tex`，336 行（335 个 LF，**末尾无换行**；修改前 35 544 B → 修改后 35 561 B；CRLF=0，**行尾仍为 LF**）。
- 英文：`_attachments/build-feynman/audit/en/I_50.txt`，正文 L36–L528（50–1～50–6），图注独立成行（Fig. 50–1～50–5），章末脚注 L530–L533。
- 旁证：`_attachments/reference/zh/Chapter50.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch50-candidates.md`（275 小块 + 51 大块，逐条对照英文判定）。
- 公式核对：eFLP 文本片段 + 独立推导（三角恒等式、正交性积分、傅里叶系数归一化、能量定理、非线性/调制展开）。
- 单章入口：`python3 tools/make_chapter_check.py 50` 生成 `preview/chapter-50/check.tex`；注释章名改《谐波》、`cd` 路径改 chapter-50。

## 结果

- 已修正 **18 条（20 处；高 5、中 6、低 7）**；**存疑 10 项**（未改）。
- 单章编译：**12 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter50.tex`、`preview/chapter-50/check.tex`（仅注释）、本报告；**未 commit，未运行全书构建**。

## 高/中问题（已修）

| # | 行号 | 问题 | 英文依据（逐字） | 修正 |
|---|---|---|---|---|
| 1 | L41 | **句号断裂**："因为$\phi$是常数。所以频率为…"，因果关系被句号切断 | "and since ϕ is a constant, any sinusoidal oscillation at the frequency ω can be written as the sum of…" | "因为$\phi$是常数**，**所以频率为…" |
| 2 | L143 | 式（50.8）文字错："$[f(t)\cos7\omega t]$**对**平均值"，不成词 | "Average[f(t)⋅cos7ωt]=a7/2" | "…]**的**平均值" |
| 3 | L214 | 分段函数区间在 $t_0$ 重叠：$0\leqslant t\leqslant t_0$ 与 $t_0\leqslant t\leqslant T$ 使 $f(t_0)$ 同时为 0 和 1 | "f(t)=0, 0≤t<t0, and f(t)=1 for t0≤t≤T" | $0\leqslant t<t_0$ |
| 4 | L281 | 裸变量："$x$输出"——$x$ 在数学模式、下标"输出"在正文 | "If we plot xout as a function of time we get the solid curve shown in Fig. 50–5." | "$x_\text{输出}$" |
| 5 | L207–L214 | 图 50-3 的 wrapfigure 插在句中，把"…是很不符合物理学 / 原则的。…"拆成两段；下一页顶部整段被右移、左侧留白（wrap 跨页） | "It is rather unphysical anyway to insist that a function should be zero up to t0, but 1 right at t0."；"Fig. 50–3. Square-wave function." | 图移到 L214 段首，句子接回"…是很不符合物理学原则的。…"；图宽 0.38→0.32\textwidth（栏 0.4→0.34），保持 12 页并消除跨页留白 |
| 6 | L66 | "rich tone" 误译"重音"（重音＝accent） | "A tone with many strong harmonics is a 'rich' tone." | "丰满的音"（底本/参考亦误） |
| 7 | L89 | 钢琴 damper 误译"消音器"（2 处；消音器＝muffler） | "we cause the damper to be lifted"；"the damper will stop the vibration of the C strings" | "制音器"（2 处；底本亦作"消音器"） |
| 8 | L93 | "octave" 误译"一音阶"（2 处，且与同段"音阶/scale"混淆） | "an octave (C–C′, B–B′, etc.) has the ratio 1:2"；"the octave (still 1:2) is divided into 12 equal intervals" | "一个八度"（2 处） |
| 9 | L131 | 特征项缺系数：$a_9$ 项写成"$\cos16\omega t$和$\cos(-2\omega t)$" | "For the a9 term, we would find cos16ωt and cos(−2ωt)."（抓取文本此处亦脱漏斜体 a9） | 补 $a_9$：$a_9\cos16\omega t$和$a_9\cos(-2\omega t)$（由 $\cos9\omega t\cos7\omega t=\frac12[\cos16\omega t+\cos(-2\omega t)]$ 校） |
| 10 | L330 | 无主句："首先，相信耳朵对于声音是非线性的" | "it is believed that the ear is nonlinear" | "首先，**人们**相信耳朵…" |
| 11 | L216 | "explicit" 误译"明显"（数学术语应为"显式"） | "the function cannot be written in an explicit algebraic form" | "显式的代数形式" |

## 低严重度修正（已修）

- L18：图 50-1 图注"噪音"与正文"噪声"不一致（英文 "a noise"）→"噪声"。
- L255：式（50.24）左端缺 $(t)$（英文 "xout(t)=Kxin(t)"）→ 补 $(t)$。
- L290：式（50.27）用 `\mathrm{cos}` 而非算子 → `\cos`（与 50.26/50.28 一致）。
- L330："既听到…还听到…"搭配不当（"we hear harmonics and also sum and difference frequencies"）→"既…又…"。
- L13："持续音 ——"、L76："相等 （"、L95："感觉 （"三处全角标点前多余空格 → 删除。

## 存疑项（未改）

1. "正确的音调"（just intonation）：通译"纯律"，底本直译，保留。
2. "按平均律调音"（tempered）：通译"十二平均律/平均律"，保留。
3. "包括$b_0=0$"（with b0=0）：宜作"其中$b_0=0$"；底本/参考同，保留。
4. "在讨论光的传送时"（transmission of light）：宜作"传播"；底本同，保留。
5. "谐音"（L95、L330，harmonics）与全章"谐波"并用；音乐声学亦通，未统一。
6. "有人已经断定"（One worker has claimed）：语气偏强，宜"声称/认为"；底本同。
7. L13 "存在着或多或少持续音"：缺"的"，底本译笔，未改（可作"或多或少持续的律音"）。
8. 同段 $a_2$/$a_9$ 的 $1/2$ 因子：英文抓取文本与底本均未写；本次仅补 $a_9$ 系数，未补 $1/2$（不影响"平均值为零"的论证）。
9. 式（50.4）未列 $a_7$、$b_7$ 两行（英文有），以"+⋯ +⋯"概括；属排版简化，未改。
10. "律音/乐音"（note/tone）并用，底本译名，未统一。

## 覆盖性结论

- **段落/完整性**：6 节与英文 50–1～50–6 一一对应；中文正文 65 段 + 1 个脚注段。按段逐句对齐，**无漏句、无漏段、无重复粘贴**；中英段落切分差异仅来自公式前后续段与图注位置。
- **公式**：编号 50.1–50.32 全部存在并逐式核对——50.1 展开；50.2 级数；50.3–50.10 系数与正交性；50.11–50.12 正交积分；50.13–50.16 完备定义；50.17–50.18 复指数；50.19–50.21 方波与 $\pi/4$；50.22–50.23 能量定理；50.24–50.27 非线性响应；50.28–50.32 调制/和差频——**除表中 3 处（50.8 文字、50.24 补 $(t)$、50.27 cos 算子）外无改动，符号与数值均正确**。
- **数字**：1:2、2:3（基频 3:2）、$T_1=2\pi/\omega_0$、$T_2=2\pi/(2\omega_0)$、$T_1=2T_2$、7/8/6/9/5/16/−2/14 周期、4:5:6、$2^{1/12}$、$2^{7/12}=1.499$、12 个音程、$\pi^2/8$、$\pi^4/90$、第 45 章——与英文逐项一致。
- **人名/术语**：毕达哥拉斯（Pythagoras）、双簧管、音栓、整流、调制、和频/差频等正确；已改"重音/一音阶/消音器"三处术语误译。
- **图表**：5 幅图（50.1–50.5）齐全，图注与英文 Fig. 50–1～50–5 对应；正文 5 处图引用全部经 `\ref` 解析（0 undefined）；本章无表格；图 50-3 按上表搬移/缩放。
- **自动候选差异**：275 小块 + 51 大块绝大多数为公式剥离、图注/页眉错位与参考文本 OCR 讹字（驴/弦、昕/听、册/曲、侍/傅、男/另、骇/弦、震/需、光/兆、局/馈、朵/耳 等），**不据以改动**；确属本仓库的问题即上表 11 条 + 低严重度 7 条。

## 验证

- 入口：`preview/chapter-50/check.tex`（`\setcounter{chapter}{49}`、`\input{../../Chapters/VolumeI/Chapter50.tex}`；注释章名/路径已改对）。
- 命令：`cd preview/chapter-50 && rm -rf build && mkdir -p build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：**12 页 A4；error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0**；日志仅 SimSun/STHeiti 字体探测、xeCJK/hyperref 常规 warning，无排版告警。
- PDF 文本抽查：修正点均生效（"（a）噪声""因为 ϕ 是常数，所以""丰满的音""制音器""一个八度""[f(t)·cos7ωt]的平均值""显式的代数形式""x输出(t)""人们相信耳朵""既听到…又听到…"）；旧串（"噪音""重音""一音阶""消音器""对平均值""$x$输出"）出现 0 次。
- 修改范围：仅 `Chapters/VolumeI/Chapter50.tex`、`preview/chapter-50/`、本报告；**未 commit**，未运行全书构建。工作区其他章（44–49、51）的改动为既有审校成果，本次未触碰。
