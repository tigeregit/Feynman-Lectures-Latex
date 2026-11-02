# 第 43 章《扩散》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter43.tex`（337 行；**实测行尾为 LF，非 CRLF**，长行；6 节 43.1～43.6：分子间的碰撞 / 平均自由程 / 漂移速率 / 离子电导率 / 分子扩散 / 热导率）
- 英文：`_attachments/build-feynman/audit/en/I_43.txt`（正文 L36 起；图注 L119、L182 另起行）
- 旁证：`_attachments/reference/zh/Chapter43.txt`（公开中译本 OCR，全文无换行、错误多）；`_attachments/reference/candidates/ch43-candidates.md`（282 小块 + 48 大块，逐条判定）
- 段落对应：6 节与英文 43–1～43–6 一一对应；中文 45 个段落块（含公式后的接续句）逐段比对英文，无缺段、无重复粘贴
- 公式核对：43 个编号公式（43.1–43.43）+ 3 个无编号公式，逐式比对英文、量纲与前后文推导

## 结果

- **已修正 13 条（高 0、中 5、低 8）**；**存疑 6 项**（未改）。
- 单章编译：**13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（aux 稳定）。
- 修改文件：`Chapters/VolumeI/Chapter43.tex`（改 12 行、共 13 处，L63 一行两处；UTF-8/LF 与 337 行、无末行换行均保持原样，33660→33664 字节）；`preview/chapter-43/check.tex`（新建后修正注释章名/路径 + 跨章引用桩）；本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L7 | "而是力图趋向于平衡——**离子位于容器的终端**"：把"平衡状态＝停在容器端"误成"离子就在容器终端"，与前句"离子正在运动"自相矛盾 | "it is trying to get to equilibrium, which is to be sitting at the end of the container." | "……而是力图趋向于平衡——**停在容器的端壁上**。" |
| 2 | L20 | "都正好是**$1/N$**"漏译 "as large"（一个分子的碰撞概率并非 1/N，而是它的 1/N） | "the chance, or probability, of a hit for any one molecule is just 1/N as large" | "都正好是**它的**$1/N$" |
| 3 | L22 | "将……问题**略加改动**"：diversion 误译为"改动"，原文是"岔开一下去回答这个问题" | "we may make a small diversion to answer the question: “What are the times between collisions?”" | "但是我们可以**稍作插叙，来回答**……**这个问题**。" |
| 4 | L78 | "各种可能的平均——**权重平均**"：把 "the mean"（算术平均）误译成加权平均 | "The various possible averages—the mean, the root-mean-square, etc.—are all nearly equal" | "各种可能的平均——**算术平均**，方均根……" |
| 5 | L159 | 破折号只开不闭（"——在我们这里这是一个足够好的近似，那么"），标点断裂 | "If E is the same everywhere between the plates, which is a good enough approximation for now" | "……足够好的近似**——**那么……" |

## 低严重度修正（已修）

- L63：变量裸排"开始随**t** 越来越大"→"随**$t$**越来越大"（英文 "gets less as t gets bigger and bigger"）。
- L63：$e^{-1} \approx 0.37\cdots$ 多余 `\cdots`（英文 "is $e^{-1}\approx 0.37$."）→ $e^{-1}\approx 0.37$。
- L76：式（43.9）标签"平均自由**路**程"多一"路"（英文 "Mean free path $l=\tau v$."，同段正文与参考底本均作"平均自由程"）→"平均自由程"。
- L144："它与下述情况有关：**有**论证中"→"**在**论证中"（英文 "The argument is made as though all collisions were separated by the mean time τ."）。
- L119："以及由$\boldsymbol{F}$产生的加速度"漏译 "the same"→"但由$\boldsymbol{F}$产生的加速度**则不变**"（英文 "It will have a new starting velocity, but the same acceleration from F."）。
- L73："平均距离"与"（记为$l$）"之间多一空格 → 删空格。
- L335："热流率"与全角"）"之间多一空格 → 删空格。
- L337：`式（$\ref{Eq:I:43:43}$）` 把 `\ref` 放进数学模式（数字字体与全书不一致）→ `式（\ref{Eq:I:43:43}）`。

## 存疑项（未改）

1. **L115"沉淀"**（sedimentation）：底本用词，物理书现多作"沉降"；与"离心分离"并列尚可通，未改。
2. **L188"“风生流”"**（no "wind" currents）：底本自造词，实指对流气流；改写属风格问题，未改。
3. **L7"它的速度只在和其他分子发生碰撞并失去动量以前增加"**：直译 "increases only until it collides…"，"只在……以前"略拗口但意思不误。
4. **L144"在碰撞开始时，它的速度为零"**：照译英文 "At the beginning of the collision it had zero velocity."；按物理应为"自由飞行开始时"，属原文表述，未改。
5. **L291 行内 $e^{-U/(kT)}$ 与式（43.37）$e^{-U/kT}$** 写法不一（数学等价），未统一。
6. **图 43.2 的 wrapfigure 位置**（L150–L157）：插在"两个正｜对面的器壁"之间，编译后浮动到页底、正文连续可读，未调整版式。

## 覆盖性结论

- **段落/完整性**：6 节逐段对应，45 个段落块与英文段行一一对应；无漏句、漏段、重复粘贴。大块候选差异 48 条全部为公式被剥离、图注/页眉错位噪声（如"第43章扩散|447"页码、公式碎片），逐条确认无正文缺失。
- **公式**：43.1–43.43 全部存在，编译渲染号与 eFLP 编号一一对应；逐式核对：43.1–43.8（碰撞概率与指数衰减）、43.9–43.12（平均自由程与碰撞截面）、43.13–43.15（漂移速度与迁移率）、43.16–43.20（离子电导与欧姆定律）、43.21–43.27（扩散流、$D=lv/3$）、43.28–43.31（爱因斯坦关系 $D=\mu kT$）、43.32–43.40（统计力学推导）、43.41–43.43（热导率）——**符号、系数、上下标均正确，未发现公式内容错误**；仅上述两处排版性修正（43.9 标签、L337 `\ref`）。
- **数字**：1h/60 次/1 min、1 s 内 1/60、2 min、$e^{-1}\approx0.37$、1/2、1/3、$2l$、$\tfrac32 kT$、$\gamma-1$、$nl\sigma_c=1$ 均与英文一致；本章无年份、无实验数据表。
- **术语**：平均自由程、碰撞截面、迁移率、扩散系数、热导率、分子动理论、S 分子等与英文一致；"权重平均"已改，"沉淀""风生流"见存疑。
- **图/表**：2 幅图（43.1 碰撞截面、43.2 电离气体的电流）齐全，图注与英文一致；正文 3 处图引用均经 `\ref` 解析（0 undefined）；本章无表。
- **跨章引用**：L311 引第 40 章式（40.2）（`Eq:I:40:2`）；单章编译无法解析，已在 `preview/chapter-43/check.tex` 加引用桩 `r@Eq:I:40:2`→40.2，PDF 实测渲染"式（40.2）"；正文保留 `\ref` 不变，全书合编时由第 40 章提供真实标签。
- **自动候选差异**：282 小块绝大多数为参考 OCR 讹字（倍/借、究/完、靶/车、兜/完、问/间、淆/请、叠/番 等），不据以改动；参考 #277"考虑**离子气体中的电流**时"（底本误译，底本另加译者注"严格地讲此处应为考虑分子扩散时"）本仓库已作"考虑分子扩散时"，正确。

## 验证

- 入口：`python3 tools/make_chapter_check.py 43` 生成 `preview/chapter-43/check.tex`；随后修正注释章名《扩散》、`cd` 路径 chapter-43、验收标准行，并加 1 个跨章引用桩。
- 命令：`cd preview/chapter-43 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 3 遍：第 1 遍 29 个未定义引用、第 2 遍 0 个但仍提示 "Label(s) may have changed"（wrapfigure 两遍排版常见）、第 3 遍 `.aux` 稳定、提示消失）。
- 结果：13 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；仅有 `Font shape TU/STHeiti(0)/b/n undefined` 字形警告（正常噪音，与 "I can't find file SimSun" 同类），无 `Missing character`。
- PDF 抽查：修正点均生效（"停在容器的端壁上""它的 1/N""稍作插叙""算术平均""随 t""e−1≈0.37""平均自由程 l=τv""则不变""在论证中""近似——那么""式（43.43）"）；旧串（"随t""权重平均""略加改动""离子位于容器的终端""平均自由路程""热流率 ）"）出现 0 次。
- 未 commit；未运行全书构建；仅改动 `Chapters/VolumeI/Chapter43.tex`、`preview/chapter-43/`、本报告。
