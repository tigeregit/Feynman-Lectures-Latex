# 第 44 章《热力学定律》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter44.tex`（347 行，LF，末尾无换行；6 节 44-1～44-6：热机、第一定律 / 第二定律 / 可逆机 / 理想热机的效率 / 热力学温度 / 熵）
- 英文：`_attachments/build-feynman/audit/en/I_44.txt`（正文 L36–L341；L108、L192 为长行，已按全文读取；公式在抓取文本中分行）
- 旁证：`_attachments/reference/zh/Chapter44.txt`（单行 OCR，15 091 字符，本身有错）；`_attachments/reference/candidates/ch44-candidates.md`（513 小块 + 35 大块，逐条核对）
- 公式核对：eFLP 文本 + 卡诺效率/绝热关系/熵变公式逐式；未抓官方网页（不需要）
- 入口：`python3 tools/make_chapter_check.py 44` 显示入口已存在；`preview/chapter-44/check.tex` 注释章名《热力学定律》、`\setcounter{chapter}{43}`、`\input{../../Chapters/VolumeI/Chapter44.tex}` 均正确，本次未改

## 结果

- **已修正 18 条（高 4、中 9、低 4、排版 1）**；**存疑 6 项**（未改）。
- 单章编译：**16 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter44.tex`（17 行，L57 同段两处；LF 保持、末尾无换行）、本报告；`preview/chapter-44/` 仅重建编译产物，`check.tex` 未改。未 commit，未动其他章。

## 高/中问题（已修）

| # | 行号 | 问题 | 英文依据（I_44） | 修正 |
|---|---|---|---|---|
| 1 | L101 | 卡诺循环绝热膨胀 b→c 误作曲线（3） | L100 "following the curve marked (2), until the temperature falls to T2, at the point marked c" | 曲线（3）→（2） |
| 2 | L108 | 图 44.5 步骤号错：等温压缩是第三步 | L100 "following the curve marked (3) (Fig. 44–5, Step 3)" | 第二步→第三步 |
| 3 | L110 | 反向循环漏 $T_1$；等温吸热过程表述错 | L102 "started at point a, at temperature T1, expanded along the curve (4), expanded further at the temperature T2, absorbing heat Q2" | "温度为的$a$点"→"温度为$T_1$的$a$点"；"膨胀到温度T2后再吸收"→"在温度T2下进一步膨胀并吸收" |
| 4 | L330 | 表 44.1 第一定律误作"对系统有用的功" | L346 "Work done on a system=Increase in internal energy of the system" | "有用的功"→"所做的功" |
| 5 | L35 | "人人都看得出是不正确的"误译 that everybody read | L56 "Only Clapeyron’s simplified version, that everybody read, was incorrect." | "简化论证——大家都读过的那一个——才是不正确的" |
| 6 | L57 | "实验还证实"误译 our experience | L72 "our experience assures us that it is not going to happen that the hot one gets hotter" | "实验"→"经验还告诉我们" |
| 7 | L57 | "某工作臂"漏 the other | L72 "the other arm of a working machine could be rubbing something that is already hot" | "某工作臂"→"另一条工作臂" |
| 8 | L88 | "没有发生…相接触"不成句，漏 the heat of | L90 "the heat of the reservoirs, or the flame of the boiler, is in direct contact with something definitely cooler or warmer" | "没有任何地方让热库的热量或锅炉的火焰…相接触" |
| 9 | L97 | "液体也不一定必须能汽化"误译 the fluid does not even have to be a gas | L94 "The fluid does not even have to be a gas" | "流体甚至不一定必须是气体" |
| 10 | L121 | "所做的功能大于可逆机"易读成"功能" | L108 "can do more work than a reversible engine operating under the same temperature conditions" | "所做的功比可逆机更大" |
| 11 | L131 | "适当时候"误译 in just a moment | L118 "we shall discuss it in just a moment" | "马上就会讨论它" |
| 12 | L245 | "两个处在不同状态下的系统"误作 two systems | L259 "Consider the system in two different conditions" | "同一个系统的两个不同状态" |
| 13 | L283 | "因为假设T也随着变化"把条件误作原因 | L304 "provided that T changes also, such that TVγ−1=constant" | "只要T也随着变化，使得…" |

## 低严重度/排版（已修）

- L33："让蒸汽放到空气中去"→"让蒸汽跑到空气中去"；英文 "let the steam escape into the air"（L54）。
- L300："温度为T 的物体"→"温度为$T$ 的物体"；裸变量未入数学模式。
- L133："$Q_1$ -$Q_2$"→"$Q_1-Q_2$"；减号原在数学模式外，成了文本连字符。
- L243："因此单位是焦每度 ）。"→"…焦每度）。"；删句号前空格。
- L328 表 44.1：`\parbox` 宽度再减 8pt，消除外框超版心 5pt 的基线 overfull（16 页不变）。

## 存疑项（未改）

1. L300/L302/L308 "整个系统" ← "the whole world"（L317/L319/L332）：底本以"系统"代"世界"，与表 44.1"系统的总熵"一致；改"整个世界"会牵动全章措辞，保留。
2. L35 "全都包括在…命题里"漏 "implicitly"（L56 "all contained implicitly"）：语义可通，未改。
3. L88 "如果我们在左边稍微加热物体" ← "If we heat the object on the left a little"（L90）：现语序可读作"在左边加热"，未改。
4. L97 "一旦热量流入气体，活塞就非常缓慢地被顶出" ← "pulling the piston out very slowly as the heat flows into the gas"（L94）："一旦"与"as"略有出入，未改。
5. L223 "同样的原则也适用于热力学" ← "the principle just found is all there is to thermodynamics"（L220）：现译较弱，未改。
6. L18 "交叉在一起" ← "sometimes welded together"（L44）：交键比喻的"welded"未译出，未改。

## 覆盖性结论

- **段落/完整性**：6 节与英文 44–1～44–6 一一对应；逐段逐句核对，**无漏句、无漏段、无重复粘贴**。候选 513 小块 + 35 大块绝大多数为参考 OCR 讹字/公式剥离/页眉（碰→磁、可逆→可道、以致→以臻、毋须→组须、Clapeyron→克劳修斯、氦→氨、焦每度→焦繁度等），均以英文为准，不据以改动。
- **公式**：20 个编号公式（44.1–44.19 及 44.6a）齐全；逐式核对 44.4/44.5 的对数项、44.6/44.6a 的绝热关系、44.7/44.12 的 $Q/T$ 关系、44.13/44.14 的卡诺效率、44.15–44.19 的熵变，符号/系数/上下标均正确；无公式内容错误。
- **图表**：11 幅图（44.1–44.11）齐全，图注与英文 Fig. 44–1～44–11 一致；正文 `\ref` 全部解析（0 undefined），无硬编码图号；表 44.1 与英文 Table 44–1 内容一致（第一定律措辞已修）。
- **数字/人名/术语**：400 W、7 倍/7°、1°、0°、$\gamma>1$、$2Q_1$/$2W$ 等与英文一致；卡诺、克拉珀龙（Clapeyron）、香农、能斯特（Nernst）、普朗克、氦均正确；热机、热库、冷凝器、热垫、可逆机、工作物质、熵、状态函数、化学常数等术语一致。

## 验证

- 入口：`preview/chapter-44/check.tex`（章名《热力学定律》，`\setcounter{chapter}{43}`，`\input{../../Chapters/VolumeI/Chapter44.tex}`；本次未改）。
- 命令：`cd preview/chapter-44 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 统计：16 页；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。基线 overfull 1（表 44.1 外框 5pt）已消除；SimSun 探测与 STHeiti 字形 warning 为正常噪音。
- PDF 抽查：修正点均生效（"曲线（2）""第三步""温度为 $T_1$ 的 $a$ 点""对系统所做的功""大家都读过的那一个""经验还告诉我们""另一条工作臂""流体甚至不一定必须是气体""所做的功比可逆机更大""马上就会讨论它""同一个系统的两个不同状态""只要 $T$ 也随着变化"）；旧串出现 0 次。
- **未 commit**；只改了 `Chapters/VolumeI/Chapter44.tex` 与新增本报告，`preview/chapter-44/` 仅编译产物。
