# 第 52 章《物理定律的对称性》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter52.tex`（420 行，LF；9 节；修改前 28 对 `%<<<NEW … %>>>NEW` 标记）。
- 英文：`_attachments/build-feynman/audit/en/I_52.txt`（正文 L36–L205，52–1…52–9；图注另起行）。
- 旁证：`_attachments/reference/zh/Chapter52.txt`（单行 25,566 字符，含前置页，OCR 噪声很大）；`_attachments/reference/candidates/ch52-candidates.md`（180 条小块 + 17 条大块，逐条对照英文判定）。
- 段落对应：中英按句末标点切分 **375 句 : 375 句**；9 节一一对应；无漏段、无重复粘贴、无跨节错位。

## NEW 块处理说明

- 修改前后均 **28 对** `%<<<NEW` / `%>>>NEW`（grep 计数 28/28），标记本身未删、未移动、未改写。
- 新增内容构成：`chapterintro` + `readingpath` 各 1，`runin` 标题 8，`summarybox` 5（§52.2/52.4/52.5/52.7/52.8），`fighint` 2，表 52.2 1，§52.2/§52.3 的 itemize 包装，1 个 `optional`。
- 事实核对结论：导读、条目、图注提示、表 52.2 与正文一致；修正 **4 条**事实陈述（#1、#2、#3、#8），其余不改。

## 结果

- **问题 13 条（高 3 / 中 3 / 低 7），已全部修正**；**存疑 8 项**未改。
- 带断言脚本 `/tmp/fix_ch52.py`（13 条）及两处补充断言替换（#10 的 μ 介子术语统一、L16 标点润色）：每次替换均恰命中 1 次；`git diff` 仅 11 行（11 insertions / 11 deletions）；LF 与 420 个换行保持，未整文件重写。
- 单章编译：**18 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**。

## 已修问题表（行号为修改前行号）

| # | 行号 | 严重度 | 问题 | 英文依据（逐字，≤25 词） | 修正 |
|---|---|---|---|---|---|
| 1 | L16 | 中 | 速读路径把 τ/θ 与吴健雄实验分派给 §52.6、§52.7、§52.8；实际两件事都只在 §52.7（§52.6 为火星人对话，§52.8 为反物质/四个钟） | "There was a certain charged particle which disintegrated into three π-mesons ... The first such experiment was carried out by Miss Wu from Columbia" | 改为"§52.6 的火星人对话、§52.7 的 τ 与 θ 之谜、吴健雄实验、§52.8 的四个钟" |
| 2 | L16 | 低 | "每节末尾的小结"不实：9 节中仅 §52.2/52.4/52.5/52.7/52.8 有小结框 | —（NEW 块事实核对） | "文中的小结框可当复查清单" |
| 3 | L142 | 中 | §52.2 小结首条漏掉"时间平移"，与本节五类操作不符 | "That the laws are symmetrical under translation in time means, in quantum mechanics, that energy is conserved." | 补为"空间平移、时间平移、空间转动、匀速直线运动、全同粒子交换" |
| 4 | L166 | 低 | 公式前句末无标点，句子直接接 `equation*`，形成标点断裂 | "the absolute square of ψ′, which is the probability of the event, is then equal to the absolute square of ψ:" | 句末补"：" |
| 5 | L200 | 低 | 图 52.1 图注以 `\\` 开头，PDF 中"图 52.1"独占一行，与其余图注格式不一致 | "Fig. 52–1.(a) L-alanine (left), and (b) D-alanine (right)." | 删去图注首部 `\\` |
| 6 | L203 | 低 | "图 52.1 是一种……模型"（把图说成模型）；英文是"图**示出**模型" | "Figure 52–1 shows a model of an amino acid that comes out of a protein." | "图……**展示了**一种……模型" |
| 7 | L222 | 高 | "the right things"与"lopsided"被误译为"右旋"（共 4 个"右旋"），与本节"生命只用 L-丙氨酸"矛盾；"make them lopsided"指造成不对称，不是右旋 | "all the enzymes digest the right things ... make them lopsided because the enzymes are lopsided" | "只消化'合适'的东西，制造'合适'的东西……变成有倾向性的，因为酶本身就是有倾向性的" |
| 8 | L295 | 高 | §52.5 小结"左右互换时，轴矢量变号"与上一条"轴矢量镜像后方向不变"自相矛盾；正文说的是把**坐标系**从右手改为左手时轴矢量变号 | "if we change to a left-hand coordinate system, we change the sign of L, but p and r do not change" | "把坐标系从右手改为左手时，轴矢量变号……" |
| 9 | L344 | 低 | 裸 Unicode "β"未入数学模式，与本章其余 `$\beta$` 排版不一致 | "the electrons in a β-disintegration tend to go away from it" | `$\beta$衰变` |
| 10 | L346 | 高 | "ν介子"把中微子当成介子；同句后文又称"两个中微子"，自相矛盾 | "the disintegration of the π into μ and ν; μ into an electron and two neutrinos" | "π 介子蜕变为 μ 介子和 ν 中微子" |
| 11 | L386 | 中 | "另外还有这种物质制造一个左旋的钟"不成句；英文为"also out of matter" | "Now let us make, also out of matter, a clock which we call the left-hand clock." | "另外**还用**这种物质制造一个左旋的钟" |
| 12 | L417 | 低 | 日光（Nikkō）的东照宫阳明门是神社之门，不是"城门" | "There is a gate in Japan, a gate in Nikkō, which is sometimes called by the Japanese the most beautiful gate in all Japan" | "全日本最美的**门**" |
| 13 | L417 | 低 | 同上，"这个城门非常精致" | "This gate is very elaborate" | "**这座门**非常精致" |

## 存疑项（未改）

1. **L350"瓦帕斯特拉"** ← "Boehm and Wapstra"：通译多作"瓦普斯特拉/维普斯塔拉"；本仓库与参考文本均非"普"，未改。
2. **L371"（由安德森在本学院发现）"** ← "discovered at Caltech by Anderson"：或可作"加州理工学院"；底本作"本学院"，保留作者口吻，未改。
3. **L390"究竟哪两种钟是相同的，如果发生这种情况的话？"** ← "which goes with which, if either?"：底本译法较松，后文已用两个问句澄清，未改。
4. **L182"就像一对精确的物与像一样"** ← "as exact mirror images"：底本用光学"物与像"，未改。
5. **L216/L220"有倾向性"** ← "lopsided/lopsidedness"：底本术语，未改；本轮只改 L222 误作"右旋"处。
6. **L409"其次一个问题是"** ← "The next question is"：底本同，未改（建议"下一个问题是"）。
7. **L110"挥笔写字，写完再写"** ← "The moving finger writes, and having writ, moves on."：底本意译，未改。
8. **L417"贵族雕像"** ← "princes carved into the pillars"：底本作"贵族"，未改（或作"王侯雕像"）。

## 覆盖性结论

- **完整性**：9 节与英文 52–1…52–9 一一对应；375 句对 375 句，逐句核对无漏句、无重复、无跨段错位。
- **公式**：2 个展示式（ψ′=ψe^{iΔ}；|ψ′|²=|ψ|²）与 L=r×p、F=qv×B 等行内式逐式核对，**均正确，未改动任何公式**。
- **图**：图 52.1–52.5 共 5 幅，图文件齐备，图注与英文图题一一对应；正文 8 处图引用（另 1 处表引用）全部解析（0 undefined）；仅图 52.1 图注格式修正（#5）。
- **表**：表 52.1 的 9 项对称操作与英文 Table 52–1 完全一致；表 52.2 为 NEW 块，逐行核对"改变的变量/守恒量/反例"无误（另见 #3 对 §52.2 小结的补全）。
- **数字/年份**：1954、14%/86%、5ℏ/4ℏ、17,000,000,000、6 ft、三天、上午 10:00、五个原子、五倍、第 33 章等均与英文一致；无数字错误。
- **人名/术语**：外尔、伽利略、洛伦兹、科里奥利、傅科、薛定谔、狄拉克、安德森、李政道、杨振宁、吴健雄、博姆、瓦帕斯特拉（存疑，见存疑 1）、日光等逐一核对；宇称守恒、极矢量/轴矢量、反粒子、β 衰变、τ/θ 之谜等术语与正文一致。
- **反物质/CP**：§52.8"右旋物质与左旋反物质行为相同"与英文 "matter to the 'right' works the same way as antimatter to the 'left'" 一致；本章只涉及 C（电荷共轭）+P（镜像）的组合，未把 T 反演写进结论，NEW 导读亦未误称 CPT。
- **候选清单**：180 条小块 + 17 条大块绝大多数是公开中译本自身的 OCR 讹字、公式剥离、页眉/图注错位噪声（如"男/另""晓/蜕""钼/钴""瓦粕/瓦帕"），**未据候选清单改动**；本仓库确实存在的底本层问题（ν 介子、右旋、还有）由英文逐句比对发现。
- **NEW 块**：28 对标记完整；5 个小结框、8 个 runin、2 个 fighint、表 52.2 与正文事实核对，仅修正 4 条事实陈述（#1、#2、#3、#8），标记与结构未动。

## 验证

- 入口：`preview/chapter-52/check.tex` 已存在，`\setcounter{chapter}{51}`、`\input{../../Chapters/VolumeI/Chapter52.tex}`；本次**未改其结构或内容**。
- 命令：`cd preview/chapter-52 && rm -rf build && mkdir -p build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 统计：**18 页**；`grep -c '^!'`=0，Overfull=0，Underfull=0，Missing character=0，undefined references=0。剩余 warning 为 xeCJK 重定义 STSong、`TU/STHeiti(0)/b/n` 字形缺失、hyperref colorlinks 重复等模板噪音。
- 零删改校验：修改前 `python3 tools/verify_chapter.py 52` **PASS（15304/15304）**；修改后 **FAIL（15314 vs 15304，首个差异为 L166 新增的"："）——属预期**：本轮 13 条问题、15 次脚本替换（含 1 次标点润色）均为有意修订，未删除任何段落或句子；NEW 标记 28 对保持。
- 版式观察（未改）：§52.4 小结框跨第 9/10 页（第 3 条落在第 10 页）；第 18 页仅 4 行，分页把"完美"拆到两页。均属分页换行，不是内容错误。
- 改动范围：仅 `Chapters/VolumeI/Chapter52.tex`、`preview/chapter-52/build/` 产物与本报告；未改 `check.tex`，未改其他章节，未 commit，未运行全书编译。
