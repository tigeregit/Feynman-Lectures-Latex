# 第 51 章《波》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter51.tex`（189 行；**实测行尾为 LF**，无末行换行；4 节 51.1～51.4：舷波 / 冲击波 / 固体中的波 / 表面波）
- 英文：`_attachments/build-feynman/audit/en/I_51.txt`（正文 L36–L216；图注另起行；公式为分式碎片）
- 旁证：`_attachments/reference/zh/Chapter51.txt`（公开中译本 OCR，全文无换行、错误多）；`_attachments/reference/candidates/ch51-candidates.md`（123 小块 + 28 大块，逐条判定）
- 段落对应：4 节与英文 51–1～51–4 一一对应；中文 38 个逻辑段（公式/图前后的接续句合并计）；英文抓取文本因公式碎片与图注另起行，不能直接按行数一一对应，逐段按内容核对，无缺段、无重复粘贴。
- 公式核对：1 个编号公式（51.1）+ 4 个无编号显示公式（激浪动量式、重力波、涟波、重力-毛细组合），另有 $u^2$ 结果式等行内公式；逐式核对符号、系数与量纲。
- 图：12 幅（51.1–51.12），图注逐条对照英文。

## 结果

- **已修正 18 条（高 9、中 5、低 4）**；**存疑 6 项**（未改）。
- 单章编译：**13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter51.tex`（15 行、18 处；UTF-8/LF 与 189 行、无末行换行保持原样，35331→35325 字节）；`preview/chapter-51/check.tex`（新建后修正注释章名《波》、`cd` 路径 chapter-51）；本报告。未 commit，未动其他章。

## 高严重度（已修，9 条）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L14 | "扩展到以$r_1$为半径的圆上**和**$r_1$小于源运动的距离"：把补充说明写成并列项，句子断裂 | "the wave from x1 expands by a radius r1 smaller than the distance that the source moves" | "圆上**，而**$r_1$小于……" |
| 2 | L55 | "**长度和宽度**一定的长水槽"：与原文"finite width and finite depth"不符（限定的是宽度与深度，不是长度） | "Consider water flowing in a long channel with finite width and finite depth." | "**宽度和深度**一定的长水槽" |
| 3 | L86 | "（称为**剪切变** ）"：漏"形"，术语不成立，且"变"后多空格 | "If a solid is distorted by pushing it sideways (called shearing)" | "（称为**剪切变形**）" |
| 4 | L86 | "发生**剪切变**一样"：同上，漏"形" | "like shearing a piece of “Jello,”" | "发生**剪切变形**一样" |
| 5 | L118 | "虽然在**当时或许能够找到**其原因"：把"在此期间可能已经找到"误成"当时或许能找到" | "although it may have been found in the meantime." | "虽然**在此期间也许已经找到了原因**" |
| 6 | L131 | "当然具有这种波的**水平均地讲**"：缺逗号，误读为"水平均" | "the water, of course, on the average, is standing still, but the wave moves." | "当然，具有这种波的水，平均地讲" |
| 7 | L136 图注 | "圆与圆之间的**对称性相移**"：误译 "systematic phase shifts"（系统的/有规律的相位移动，不是"对称性"） | "Note the systematic phase shifts from circle to circle." | "圆与圆之间**有规律的相位移动**" |
| 8 | L161 | "**按照通常的做法**"：误译 "as we always do"（正如我们通常遇到的那样），非"按惯例" | "When we have both gravity and capillary action, as we always do" | "**正如我们通常遇到的那样**" |
| 9 | L187 | "从瓶中**倒入流水中，两者相交后**可以看到在流水中有许多线条"：把"流出的牛奶流"误成"流水"，"crossing both ways"误成"两者相交" | "a large number of lines can be seen crossing both ways in the outgoing stream" | "从瓶中**倒出**，就可以看到**流出的牛奶中有许多线条纵横交叉**" |

## 中严重度（已修，5 条）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 10 | L40 图注 | "在相继的几个瞬间**及时拍下**的波前"：误译 "at successive instants"（相继瞬间），"及时"无着落 | "Wavefront “snapshots” at successive instants in time." | "在相继的几个瞬间**拍下**的波前" |
| 11 | L46 | "**直到**波传播到很远时，由于扩展而变弱，**直到**其压强……为止"：双重"直到"，前句无主 | "weakened to such an extent from spreading that the pressure bump is small compared with atmospheric pressure" | "**直到它传播得很远、因扩展而变弱，以致**其压强的变化小于大气压强时为止" |
| 12 | L46 | "因此，**一个人如果根据听到的声音来判断冲击波的到来已经太迟了**"：主谓断裂 | "So one cannot tell, acoustically, that the shock is coming until it is too late." | "因此，**靠听声音来判断冲击波的到来是来不及的**" |
| 13 | L62 图注 | "其中（b）比（a）**迟**"：漏 $\Delta t$，图注不完整 | "Two cross sections of a bore in a channel, with (b) at an interval Δt later than (a)." | "其中（b）比（a）**迟$\Delta t$**" |
| 14 | L88 | "则晶体的各向异性最终**得到了平衡**"：误译 "average out"（平均掉/相互抵消），非"平衡" | "the crystal anisotropies average out." | "则晶体的各向异性最终**相互抵消**" |

## 低严重度（已修，4 条）

- L20："仅为真空中光速的 **2/3 。**"全角句号前多空格 → "2/3。"（排版）。
- L57："所谓 **“激浪 ”**"后引号前多空格 → "“激浪”"（排版）。
- L116："（傅里叶分析 **）**。"全角右括号前多空格 → "（傅里叶分析）。"（排版）。
- L116："同时**一个**非常精密的新的地震仪……**它**及时地测出了"：英文为复数 "new seismographs" → "同时**一些**非常精密的新地震仪……及时地测出了"（英文 "new seismographs of great delicacy were made just in time"）。

## 存疑项（未改，6 项）

1. **L112"娜娜（Ñaña）"**：按西班牙语读音可作"尼亚尼亚"；但图 51.7 图内标签为"娜娜 N-S"，改图注会与图内文字不一致，底本译名保留。
2. **L22"切连科夫辐射"**：通行译名"切伦科夫辐射"，底本用"切连科夫"，属译名变体，未改。
3. **L57"它不是一个重要的结论"** ← "it is not a great generalization"："推广/概括"更贴切；底本作"结论"，语义偏移不大，未改。
4. **L107"横波不能在内核圆的里面传播"** ← "within the inner circle"："内核圆的里面"冗余，可作"内核圆内"；属底本表述，未改。
5. **L157"毛细引力"** ← "capillary attraction"：今多作"毛细吸引力/毛细力"；底本用词，未改。
6. **L80"绝热反应"** ← "adiabatic reactions"：物理上通常说"绝热过程"，但英文原文即作 reactions，未改。

## 覆盖性结论

- **段落/完整性**：4 节对应；中文 38 个逻辑段逐段与英文内容比对（公式/图前后的接续句合并计），无漏句、漏段、重复粘贴。候选 123 小块 + 28 大块绝大多数为公式剥离、图注/页眉错位与参考 OCR 讹字（速/束、弦/驴、槽/模、顶/项、露/圳、咚/噬 等），不据以改动；确属本仓库的问题即上表 18 条。
- **公式**：51.1 $\sin\theta=c_w/v$ 与 4 个无编号显示公式（激浪 $u^2=gh_2(h_1+h_2)/(2h_1)$、$v_\text{相}=\sqrt{g\lambda/(2\pi)}$、$\sqrt{2\pi T/(\lambda\rho)}$、$\sqrt{Tk/\rho+g/k}$）符号、系数、量纲均正确；编译渲染 51.1 正确。
- **数字/量纲**：2/3、1958、20%、1 atm、百万分之一、54.7/53.1 min、1960 年 5 月、3/2、1/2、$2\pi$ 均与英文一致；无数字错误。
- **术语/人名**：切连科夫、弗兰克、塔姆、科里奥利、Ñaña、Isabella、简正模式、基谐模式、涟波、激浪等已核对；译名取舍见存疑 1–2。
- **图/表**：12 幅图齐全，图注与英文逐条核对；图 51.4 英文原图无说明文字，保留空 `\caption{}`（输出"图 51.4"）；正文图引用全部经 `\ref` 解析（0 undefined），无硬编码图号；本章无表。注意图注已改而 `\label` 与图片文件名仍保留旧串（如"及时""对称性相移"），仅为内部标识/文件名，不影响输出；未改文件名以遵守修改范围。

## 验证

- 入口：`python3 tools/make_chapter_check.py 51` 生成 `preview/chapter-51/check.tex`；随后修正注释章名《波》、`cd` 路径 chapter-51。
- 命令：`cd preview/chapter-51 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：13 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；仅有 `TU/STHeiti(0)/b/n` 字形警告（正常噪音），无 `Missing character`。
- PDF 抽查：修正点均生效（"圆上，而 $r_1$""宽度和深度一定""剪切变形""在此期间也许已经找到了原因""当然，具有这种波的水""有规律的相位移动""正如我们通常遇到的那样""从瓶中倒出……纵横交叉""迟 $\Delta t$" 等）；旧串（"圆上和$r_1$小于""长度和宽度一定""按照通常的做法""倒入流水中""及时拍下的波前""对称性相移"）在 PDF 文本中出现 0 次。
- 未 commit；未运行全书构建；仅改动 `Chapters/VolumeI/Chapter51.tex`、`preview/chapter-51/`、本报告。
