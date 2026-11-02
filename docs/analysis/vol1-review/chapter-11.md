# 第 11 章《矢量》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter11.tex`（382 行；7 节：11-1 物理学中的对称性 … 11-7 矢量的标积）
- 英文：`_attachments/build-feynman/audit/en/I_11.txt`（11–1～11–7，正文段 L36–L136，共 37 段；公式在抓取文本中为 [math] 占位）
- 旁证：`_attachments/reference/zh/Chapter11.txt`（公开中译本 OCR，本身有错）；候选差异 `_attachments/reference/candidates/ch11-candidates.md`（本次运行 `python3 tools/chapter_diff.py --chapter 11` 生成：295 小块 + 42 大块）
- 官方网页 feynmanlectures.caltech.edu 本次被 Cloudflare 拦截（curl 403），公式以 eFLP 文本结构与数学一致性核对代替

## 结果

- **已修正 24 处**（按问题计：中 5 条 7 处、低 8 组 17 处；**无高严重度**）；**存疑 8 项**（未改）。
- 单章编译：**14 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter11.tex`（正文 17 行，**CRLF 换行保持原状**）、`preview/chapter-11/check.tex`（仅注释：章名改《矢量》、`cd` 路径改 chapter-11）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L82 | "来表示坐标$x'$和$y$开始"缺撇号 | "by expressing the coordinates [math] and [math] in terms of [math], [math], and [math]"（即 x′、y′） | 改为"$x'$和$y'$" |
| 2 | L167、L171 | 方程组内多余逗号："F_y,=y"、"F_{y'},=y'" | "This equation … stands for the three equations [math] or, alternatively, for [math]" | 删逗号，作 $F_y=y$、$F_{y'}=y'$ |
| 3 | L183 | "如果把这些变换应用于$a_{x'}$和$b_{x'}$以得出$a_{x'}$和$b_{x'}$"前后重复，第一对应为未带撇量 | "If we apply those transformations to [math] and [math] to get [math]" | 改为"应用于$a_x$和$b_x$以得出$a_{x'}$和$b_{x'}$" |
| 4 | L366 | 两处单位矢量记号丢失："我们用表示单位矢量""如果要求某矢量在方向上的分量" | "Let us call this unit vector [math]; then [math]. Then, if we want the component … in the direction of [math]" | 补为"我们用$\boldsymbol{i}$表示单位矢量""在$\boldsymbol{i}$方向上的分量"（公开中译本同） |
| 5 | L380 | "立用这种方法"（OCR 讹字，不成词） | "By this means we can go from the components of a vector to the vector itself." | "应用这种方法"（公开中译本同） |

## 低严重度修正（已修）

- L82、L161 各删除一处夹在中文与公式之间的制表符（tab）。
- L92 删除多余/半角逗号："为了用$F_x$和$F_y$，来表示$F_{x'}$，，"→"…$F_y$来表示$F_{x'}$，"；"用$F_x$，和$F_y$，"→"用$F_x$和$F_y$"。
- L230、L279（3 处）、L284、L292、L305、L353 共 8 处公式后半角逗号 `,` 改全角"，"。
- L159 补两处句读（"特定点$P$我们…"→"$P$，我们…"；"按照习惯假如…"→"按照习惯，假如…"）；L161"换句话说任何…"→"换句话说，任何…"。
- L288"那加速度$a_{\bot}$就是"衍字"那"→"加速度$a_{\bot}$就是"（中译本无"那"）。
- L340"以及a与b的分量"→"以及$\boldsymbol{a}$与$\boldsymbol{b}$的分量"（补矢量记号）。

## 存疑项（未改）

1. **L5"较为直观的形式"** ← "Weyl's more general form"：general 宜作"一般"；公开中译本亦作"直观"，属底本译法，不改。
2. **L9"墙壁正在影响着我们的装置"** ← "the wall is pushing on the apparatus"："影响"宜作"推/挤压"；底本译法。
3. **L153"非常有用的数学工具"** ← "a very powerful mathematical machinery"："powerful"宜作"强有力的"；底本译法。
4. **L318"最好此式是成立的"** ← "It had better be—and if we substitute Eq. (11.5) we do indeed find that it is."：底本直译，语义可通。
5. **L70"我们已经得出了$F$的公式，把式（11.1）代入F的式子"**：英文两处均指 the formula for F_{x'}（L52 段），中文疑脱下标；底本 OCR（"Ex/Fs"）无法确证，未改。
6. **段落切分与英文不齐 3 处**：英文 L52+L54 中文并为一段；英文 L64 中文拆为两段；英文 L90+L92 中文并为一段。中文正文 36 段 vs 英文 37 段（净 -1），**内容完整无缺**，疑为底本排版，未改。
7. **图 11-6**（"在短时间间隔…一个粒子的位移"）`wrapfigure` 位于减法段（L217–224），正文首次引用在速度段（L230），浮动位置偏早；改动会牵动版面，未改。
8. **正文个别矢量字母未用黑体**（L92"力$F$"、L101"力F的分量"、L70"F的式子"）：录入记号问题、涉全书统一性，未单章改。

## 覆盖性结论

- **段落/完整性**：7 节与英文 11-1～11-7 一一对应；逐句核对全部句子有落点，**无漏句、无漏段、无重复粘贴**；段落数差异见存疑 6。
- **公式**：编号公式 11.1–11.25（含 11.4a/b/c）全部存在；编译 `.aux` 核对每个 `Eq:I:11:N` 标签的渲染号与 N 一致（11.1–11.25 全对）；公式关系自查一致（11.5/11.6 同形；11.8/11.9 右端一致；11.17 距离不变；11.19–11.21 标积；11.22–11.25）。未发现公式内容错误，问题均为符号/标点讹误（上表 #1–#4 已修）。
- **数字/量纲**：本章数字极少——"转过180°""第4章""一牛顿""等于1"，均与英文一致；**无数字/量纲错误**。
- **人名/术语**：外尔(H.Weyl)、乔（Joe）、莫（Moe）一致；对称性/不变性、平移、转动、标量、矢量、分量、标积/点积、单位矢量、位移、速度、加速度、动能、功，均与英文一致。
- **图**：8 张图（11.1–11.8）齐全；图注与英文 Fig. 11–1～11–8 一致；正文 12 处图引用全部经 `\ref` 解析（0 未定义），无硬编码图号。
- **自动候选差异**：295 小块 + 42 大块绝大多数是"我们"的 `\ref`/公式被剥离及参考 OCR 噪声；确属我们错误的是 L380"立用"（已修）及上述符号/标点；其余为参考文本讹字（如 莫→英、罩→单、惑→感、问→间、叙→令、矢→拓/撩、撇→撤/撒），**不据以改动**。
- **建议**：存疑 1–4 为底本译法，若 Lead 统一术语再改；存疑 6 的段落切分若要求严格对齐英文可增/删空行，但会引起版面变化，建议全章统一处理。

## 验证

- 入口：`preview/chapter-11/check.tex`（章号 `\setcounter{chapter}{10}`、`\input{../../Chapters/VolumeI/Chapter11.tex}`；本次仅修正注释）。
- 命令：`cd preview/chapter-11 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`，14 页 A4。
- PDF 文本抽查：修正点已生效（"我们用 i 表示单位矢量""坐标 x′ 和 y′""应用这种方法""加速度 a⊥ 就是"）；旧串（"立用""那加速度""我们用表示""Fy,=y"）出现 0 次。
