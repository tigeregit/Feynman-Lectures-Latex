# 第 28 章《电磁辐射》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter28.tex`（129 行；4 节 28-1～28-4；34 个正文段）
- 英文：`_attachments/build-feynman/audit/en/I_28.txt`（28–1～28–4，正文 L36–170；抓取文本中公式为分式碎片）
- 旁证：`_attachments/reference/zh/Chapter28.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch28-candidates.md`（173 小块 + 16 大块，已逐条核对）
- 公式核对方式：eFLP 英文片段逐式比对 + 单章编译 PDF 渲染核验

## 结果

- **已修正 7 条（7 处；中 3、低 4）**；**存疑 6 项**（未改）。
- 单章编译：**8 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter28.tex`（7 行，**CRLF 换行保持原状**）、`preview/chapter-28/check.tex`（仅注释：章名改《电磁辐射》、`cd` 路径改 chapter-28）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L7 | "1860年的某一天"把年代译成了一个年份（Maxwell 1860 年代的工作） | "occurred to J. C. Maxwell one day in the 1860s"（L38） | "19世纪60年代的某一天" |
| 2 | L53 | 正文已按英文改为"1896年"，但底本译者注"应是1896年"仍在，页面成"1896年¹（注：应是1896年）"，自相矛盾（底本原为1898年＋注，前次数值修正只改正文、漏删注） | "radioactivity, discovered by Becquerel in 1896"（L105） | 删去 `\footnote{应是1896年。——译者注}` |
| 3 | L70 | 正文已补"除以$r$"，但底本译者注（"…应为…加速度除以$r$"）仍在；且脚注号紧贴 r 排成上标，PDF 中读作"加速度除以$r^2$"（见编译第 5 页） | "the $x$-component of $d^2e_{r'}/dt^2$ is simply the acceleration of $x$ itself at an earlier time divided by $r$"（L127） | 删去该 `\footnote{……。}`；正文保留"加速度除以$r$" |

## 低严重度修正（已修）

- **L9**："电的**斥力和引力**" → "电的**吸引力和排斥力**"（英文 "electric forces of attraction and repulsion"；原译"引力"易误读为万有引力）。
- **L40**："暂且假定电荷**带有光**" → "电荷**带有一盏灯**"（英文 "suppose that the charge carried a light"，a light＝灯/光源）。
- **L68**："**这很容易看出的**" → "**这是很容易看出的**"（缺谓语"是"）。
- **L88**："叫做**电偶振子**" → "叫做**电偶极振子**"（英文 "an electric dipole oscillator"；本章其余均作"偶极"，术语统一）。

## 存疑项（未改）

1. **L38**"…$\boldsymbol{e}_{r'}$是从测量 $\boldsymbol{E}$ 的 $P$ 点出发的单位矢量，**$r$** 是从 $P$ 到 $q$ 的距离"：同句下标不一致（e 带撇、r 不带撇）；英文此处亦作 er、r（而公式用带撇量），未改。
2. **L55**"知识渊博的**咬文嚼字者**" ← "purists"：宜作"纯粹主义者/苛求者"，底本作"咬文嚼字者"，语气可接受。
3. **L79**"我们写下式（28.3）的其余部分只是**作为一个阶梯**" ← "only to set the stage"（铺垫/铺陈）；底本译法，语义可通。
4. **L13**"遥远星体上的原子运动仍能产生足够的影响…"：漏译 "at this great distance"（在如此遥远的距离上）；底本同。
5. **L7**"只要有了电与磁，就会有光！" ← "Let there be electricity and magnetism, and there is light!"（仿《创世记》句式），底本译法，不算错。
6. 节标题"**偶极辐射子**" ← "The dipole radiator"：通行译法为"偶极辐射器/辐射体"，底本作"辐射子"（任务亦沿用），未改。

## 覆盖性结论

- **段落/完整性**：4 节 28-1～28-4 与英文对应；中文 34 个正文段 ↔ 英文 34 段（§28-1 19、§28-2 6、§28-3 4、§28-4 5；英文抓取行的公式/插图断行已按原书段归并）。逐句核对无漏句、无漏段、无重复粘贴；候选 16 条"大块差异"全部是公式剥离、页眉、图注噪声（含我们的译者注差异，即中等问题 2/3）。
- **公式**：编号式 28.1–28.6 逐式核对——28.1（$\boldsymbol{F}=GmM\boldsymbol{e}_r/r^2$）、28.2（$\boldsymbol{F}=q(\boldsymbol{E}+\boldsymbol{v}\times\boldsymbol{B})$）、28.3（含延迟/延迟变化率/二阶微商三项的场式）、28.4（$\boldsymbol{B}=-\boldsymbol{e}_{r'}\times\boldsymbol{E}/c$）、28.5（辐射项）、28.6（$E_x(t)=-\frac{q}{4\pi\varepsilon_0c^2r}a_x(t-r/c)$）**全部正确，未改动任何公式**；无数字/量纲错误（1860 年代、1896 年、50 亿光年、几千英里、90°/180°/45°、1/r 等均核对无误）。
- **图**：图 28.1–28.4 的编号、图注、正文 `\ref` 引用一一对应（编译渲染核验）；图注文字与英文一致。
- **人名/术语**：麦克斯韦（James Clerk Maxwell）、库仑、贝克勒尔、牛顿；量子电动力学、偶极辐射、电偶极振子（已修）、延迟时间/推迟、叠加原理、干涉、相位等均正确。（本章未出现赫兹/Hertz 字样，无需核对。）
- **自动候选差异**：173 小块 + 16 大块绝大多数为公式剥离噪声与参考文本 OCR 讹字（矛→予、几干→几千、昵→呢、到→遥、貌→角、撇→撤、加→叠 等），**不据以改动**；确属本仓库的问题即上表 7 条。

## 验证

- 入口：`preview/chapter-28/check.tex`（由 `tools/make_chapter_check.py 28` 生成；`\setcounter{chapter}{27}`、`\input{../../Chapters/VolumeI/Chapter28.tex}`；本次仅修正注释）。**本章无跨章 `\ref`**，修正前后均无未定义引用。
- 命令：`cd preview/chapter-28 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：8 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 文本抽查：修正点均生效（"19世纪60年代""电的吸引力和排斥力""带有一盏灯""这是很容易看出的""电偶极振子"）；两处译者注及"应是1896年""除以$r^2$"出现 0 次。
- 佐证：`git diff` 仅 7 行改动，无其他文件改动；候选清单未重跑（按要求使用现成文件）。
