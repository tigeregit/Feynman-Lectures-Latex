# 第 37 章《量子行为》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter37.tex`（233 行；8 节 37-1～37-8：原子力学 / 子弹实验 / 波的实验 / 电子的实验 / 电子波的干涉 / 追踪电子 / 量子力学的基本原理 / 不确定性原理；42 段）
- 英文：`_attachments/build-feynman/audit/en/I_37.txt`（37–1～37–8，正文 L36–L331；抓取文本中幅度符号被拆成多行）
- 旁证：`_attachments/reference/zh/Chapter37.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch37-candidates.md`（226 小块 + 20 大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 中译本 OCR 旁证逐式比对（本章公式均为代数式，无编号错误风险）

## 结果

- **已修正 10 项（高 0、中 2、低 8）**；**存疑 6 项**（未改）。
- 单章编译：**14 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter37.tex`（+11/−11 行，**CRLF 换行保持原状**）、`preview/chapter-37/check.tex`（仅注释：章名改《量子行为》、`cd` 路径改 chapter-37）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L214 | "这是一种**节约**，它或许是后退的一步"——retrenchment（缩减、退守）误译为"节约"，与紧接的"后退的一步"自相矛盾 | "It must be recognized that this is a retrenchment in our earlier ideal of understanding nature. It may be a backward step…" | "这是一种**退让**，它或许是后退的一步" |
| 2 | L220–L228 | 图 37-6 的 wrapfigure 插在句子中间："…这是前面所表述的较为一般的不确定性原理的特殊情况。比较普遍的表〡（图）〡述是，人们不可能…"；英文 Fig. 37–6 位于"…as shown in Fig. 37–6."段之后、"Now in order to do this…"段之前 | Fig. 37–6 图注位于英文 L327（"Now in order to do this…"段之前） | 图移至 L230 段之后、L232 段之前；合并为"比较普遍的**表述是**，人们不可能…" |

## 低严重度修正（已修）

- L21："事实上，它包含的只是奥秘" → "事实上，它包含的正是那**唯一的**奥秘"（原文 "In reality, it contains the only mystery."，漏译"唯一"）。
- L7："下一个论题是**包含着大量物质的物体**的性质" → "下一个论题是**较大块物质的行为**"（"relatively large pieces of matter" 误译；下文"力学与热学性质"仍通顺）。
- L121："$P_{12}$要比$P_1+P_2$**还大两倍以上**" → "$P_{12}$**是$P_1+P_2$的两倍还多**"（"more than twice as large as P1+P2"；原表述易被读成"大两倍"即 3 倍以上）。
- L135："我们同时在两个位置上见到闪光**多好**……让我们做一下实验吧！" → "我们在两个位置上同时见到闪光……**那就**让我们做一下实验吧！"（英文为条件句 "If it should happen…"，无"多好"的愿望语气）。
- L101："颗粒到达某个**x**位置" → "某个 **$x$** 位置"（正文裸变量入数学模式）。
- L113："当两个孔都打开时测得的结果**P12**并不是" → "结果 **$P_{12}$** 并不是"。
- L135："看到来自图中标有**A**的位置" → "标有 **$A$** 的位置"（图内标注用数学体）。

## 存疑项（未改）

1. **L34"射率"**（"机枪射击的射率十分低"等两处）：底本用词，可作"发射率/射击速率"，理解无碍，未改。
2. **L52"在波源的后面"** ← "To the right of the source"：方位词差异（图上波源在左、墙在右），底本如此，未改。
3. **L234"屏障"** ← "screen"：此处指可动的屏/板，可作"屏/挡板"，底本如此，未改。
4. **L214"我们只能预言可能性！"** ← "We can only predict the odds!"：可作"几率/概率"，底本措辞，未改。
5. **"绝对值平方"**（L125/L185）：通常作"绝对值的平方/模平方"，底本用词，未改。
6. **图 37-2/37-4/37-5 的浮动体位置**相对英文书版次略偏前或偏后（英文图注在段前/段后，中文浮动体就近放置），均未造成断句，未动。

## 覆盖性结论

- **完整性**：8 节与英文 37–1～37–8 一一对应；逐句核对**无漏句、无漏段、无重复粘贴**；中文 42 段 vs 英文约 40 段（中文按句/按图分段，底本体例）。
- **公式**：8 个编号公式 **37.1–37.8 全部存在且逐式与英文一致**：37.1（$P_{12}=P_1+P_2$）；37.2（$I_1=|\hat h_1|^2,~I_2=|\hat h_2|^2,~I_{12}=|\hat h_1+\hat h_2|^2$）；37.3（$|\hat h_1+\hat h_2|^2$ 展开式含 $2|\hat h_1||\hat h_2|\cos\delta$）；37.4（$I_{12}=I_1+I_2+2\sqrt{I_1I_2}\cos\delta$）；37.5（$P_{12}\neq P_1+P_2$）；37.6（$P$=概率、$\phi$=概率幅、$P=|\phi|^2$）；37.7（$\phi=\phi_1+\phi_2$、$P=|\phi_1+\phi_2|^2$）；37.8（$P=P_1+P_2$）。行内式 $\Delta x\geqslant\hbar/(2\Delta p)$、$p=h/\lambda$、$P_1=|\hat\phi_1|^2$、$P_{12}=|\hat\phi_1+\hat\phi_2|^2$ 等均一致。**本次未改动任何公式内容**。
- **数字/物理事实**：强度 4/2/0、$36=6^2$、$\lambda/2$、$\lambda/4$、相位差 $\pi$、半波长奇数倍、1926–1927 年、$x=0$ 处板的反冲方向等核对一致；"$P_{12}$ 是 $P_1+P_2$ 的两倍还多"的表述已按英文修正。
- **术语**：概率幅、干涉、相长/相消干涉、理想实验、不确定性原理、约化普朗克常数、波区等与英文一致。
- **图**：6 幅图（37.1–37.6）齐全，图注与英文逐条一致（Fig. 37–1 "Interference experiment with bullets." 至 Fig. 37–6 "An experiment in which the recoil of the wall is measured."）；图号 37.1–37.6 与 eFLP Fig. 37–1～37–6 顺序一致；**22 处 `\ref` 全部解析（0 未定义）**；本章无跨章 `\ref`，单章编译无需占位标签。
- **自动候选差异**：226 小块 + 20 大块绝大多数为参考文本 OCR 噪声（咔嗒→卡噶、遮→庶/诞、薛定谔→薛定谓、钨丝→忽丝、约化普朗克常数漏字、公式整体剥离等），判"参考误"未采纳；确属本仓库的问题即上表 10 项。

## 验证

- 入口：`preview/chapter-37/check.tex`（`\setcounter{chapter}{36}`、`\input{../../Chapters/VolumeI/Chapter37.tex}`；本次仅修正注释）。
- 命令：`cd preview/chapter-37 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：14 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；PDF 中无 `??`。
- PDF 文本抽查：修正点均生效（"较大块物质的行为""唯一的奥秘""是一种退让""$P_{12}$ 是 $P_1+P_2$ 的两倍还多""那就让我们做一下实验吧""某个 $x$ 位置""结果 $P_{12}$""标有 $A$ 的位置""比较普遍的表述是"）；旧串（"节约""包含着大量物质的物体""还大两倍以上""多好""某个x位置""结果P12""标有A的"）出现 0 次。
