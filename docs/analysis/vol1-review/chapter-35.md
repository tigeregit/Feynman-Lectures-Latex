# 第 35 章《色视觉》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter35.tex`（205 行，205 个 CRLF，末行无换行；6 节；41 个正文段，其中 3 段被 `wrapfigure` 分成前后两截）
- 英文：`_attachments/build-feynman/audit/en/I_35.txt`（正文 L39–L148，41 段；图注另列）
- 旁证：`_attachments/reference/zh/Chapter35.txt`（公开中译本 OCR，单行 36,758 字符，本身有讹字）；`_attachments/reference/candidates/ch35-candidates.md`（128 条小块 + 25 条大块，逐条对照英文判定）
- 段落对应：中英 **41 : 41**，无漏段、无重复、无跨段错位；图 35–1～35–10 与正文引用一一对应，无表格

## 结果

- **修正 27 条**：高 8、中 13、低 5，另参考文献格式 1 组（14 处空格/标点，计入总条数）。
- **存疑 7 项**（未改，见下）。
- 实际改动 **22 行**，行数结构不变（205 行 / 205 CRLF）；未用 sed，全部经带断言的 Python 脚本替换。
- 单章编译：**14 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。

## 高严重度（8 条，已修）
| 行号 | 问题 | 英文依据（逐字） | 修正 |
|---|---|---|---|
| L16 | "在这一章中将讨论视觉的生理方面"把本章与下一章的内容对调；漏"下一章" | "In the present chapter we shall discuss mainly the observable phenomena of human vision, and in the next chapter … the physiological aspects of vision" | "在这一章中我们将主要讨论人类视觉中可观察到的现象，而在下一章中讨论视觉的生理方面……" |
| L35 | "巨蟹座星云"（Cancer）误译，Crab nebula 在金牛座 | "the ring nebula and the Crab nebula." | "蟹状星云" |
| L56 | "大量的**颜色**"与后文"红色/黄色"并列，显系"蓝色"之误 | "A certain light may have a lot of blue, considerable red, very little yellow" | "大量的**蓝色**" |
| L71 | "为了增加任何舞台效果，这种光从来没有被使用过"因果颠倒、不成句 | "this color is never used for any stage effect" | "这种颜色从未用于任何舞台效果" |
| L102 | 漏英文脚注 1（薛定谔论文出处），中文只剩脚注 2 | "Schrödinger wrote a wonderful paper on color vision in which he developed this theory of vector analysis as applied to the mixing of colors." | 补 `\footnote{Über das Verhältnis … 471--490.}`；原脚注自动变为 2 |
| L112 | "**钟形**面积"：色品图边界是马蹄形，"oddly shaped"非钟形 | "all the colors that we can ever see are enclosed in the oddly shaped area bounded by the curve." | "以曲线为边界的**形状奇特的区域**" |
| L176 | "1958 年……**色素**从来没有被看到过"漏"颜色"限定，易误读为视紫质 | "In 1958 it could be said that the color pigments had never been seen at all." | "**色视觉色素**从来没有被看到过" |
| L187 | "并且是在已经确定这种色素是什么色素，而把另一种用对第一种不灵敏的红色漂白之后得到的"语法断裂、语义反置 | "having already determined what one pigment was, bleaching the other one in the red where the first one is insensitive" | "这是在已经确定其中一种色素是什么之后，用第一种色素不敏感的红光把另一种色素漂白而得到的" |

## 中严重度（13 条，已修）
| 行号 | 问题 | 英文依据 / 说明 | 修正 |
|---|---|---|---|
| L35 | "威尔逊山天文台帕洛玛天文台"缺连接词，且漏 W. C. | "W. C. Miller of the Mt. Wilson and Palomar Observatories" | "威尔逊山和帕洛玛天文台的 W. C. 米勒先生" |
| L56 | "光谱的不同波长**在我们就看到**不同的颜色"不成句 | "which appear to us to have different colors" | "在我们看来就是不同的颜色" |
| L80 | 裸 `Z` 未入数学模式 | 英文 "say Z" | "比如说$Z$" |
| L102 | 裸 `Z` 未入数学模式 | "the new light Z" | "新的光$Z$" |
| L104 | "三种**颜色**……混合**色**"误译 paints / mixed pigments | "three paints … a greater variety of mixed pigments" | "三种**颜料**……更多种混合**颜料**" |
| L104 | "若我们……。"条件句无主句，句号断裂 | "let us use red, blue, and yellow in our projector" | "现在我们在投影灯中改用……。" |
| L106 | 两处裸 `X`；"从……配制"介词不当 | "X could always be made, say, of red, blue, and yellow"；"red plus X could be made out of blue and yellow" | "$X$……由……配制"；"红色加上$X$可以由蓝色和黄色配制出来" |
| L131 | "**两条**弯曲边界线"：英文单数，色品图只有一条连续边界 | "the curved boundary line" | "那条弯曲边界线" |
| L135 | "混合法则都**符合**这一假说的**结果**"搭配错误 | "all of the rules of color mixing would be a consequence of this proposition" | "都是这一假说的结果" |
| L137 | "缺少蓝色的**色素沉积**"语法/术语不当 | "another the blue pigmentation" | "一种应是缺少红色色素，另一种……绿色色素，再一种……蓝色色素" |
| L156 | "如果像这种理论所说的，他缺少……之一是正确的话"句子断裂 | "If the theory that he is missing one of the three pieces of information is right" | "如果这种认为他缺少三部分信息之一的理论是正确的" |
| L156 | "所有直线的**焦点**"：直线会聚处应为交点 | "the point of focus of all the lines" | "所有直线的**交点**" |
| L165 | 同上，"有一个**焦点**" | "has a focus near the red end of the boundary curve" | "有一个**交点**" |

## 低严重度（5 条 + 参考文献 1 组）

| 行号 | 问题 | 修正 |
|---|---|---|
| L64 | "**在用**两个数字"不成句（英文 "By using two numbers"） | "**若用**两个数字"；并去掉 `（$R$）`、`（$G$）` 多余括弧 |
| L75 | "看起来与$Y$**是**不可区别的" | "看起来与$Y$不可区别" |
| L135 | "交换闪变"（flickering back and forth）用词不当 | "交替闪变" |
| L135 | "**到达**某一强度时"（英文 "there comes an intensity"） | "**达到**某一强度时" |
| L156 | "一种特殊类型的称为患绿色盲者的颜色混合"定语错位 | "一种特殊类型的色盲者（称为患绿色盲者）的颜色混合" |
| L196/200/202/204 | 参考文献缩写/卷期/标点不统一：`M.H.Pirenne`、`Energy, Quanta and Vision`、`N.D.`、`No.8`、`Vol.II/I`、`September, 1957`、`W.A.`、`Teddington England`、`1957.Published`、`Robert S,`、`S.Woodworth` | 统一为 `M. H. Pirenne`、`Energy, Quanta, and Vision`、`N. D.`、`No. 8`（含逗号）、`Vol. II/I`、`September 1957`、`W. A.`、`Teddington, England`、`1957. Published`、`Robert S.,`、`S. Woodworth` |

## 存疑项（未改，供上游判断）

1. **L62** "绿色带红" ← "reddish green"：语序与术语（宜"带红的绿色"）；底本同，未改。
2. **L131** "这是紫红色的轨迹" ← "the locus of the purples"：purples 或可作"紫色"；底本译法，未改。
3. **L135** "再一种色素在绿色区吸收很强" ← "another absorbs in the green"：英文无"很强"；疑为底本增饰，未改。
4. **L135** "它是这样测得的，即一种色光，其最小数量应是多少才能使眼睛恰好看到它"：可改为"找出恰好能看到它所需的色光最小量"；底本句式，未改。
5. **L176** "从视网膜获得的色素主要是由一种叫做视紫质的色素组成的"：`色素……色素`重复；底本同，未改。
6. **L176** "它的响应曲线和眼睛的灵敏度完美地相适合……符合得非常好"：语义重复；可作"完美地吻合，如图 35.9 所示"，未改。
7. **L178** "当被光漂白后强度就有所改变" ← "have an intensity change"：`强度`含义偏泛，或应作"吸收强度"；未改。

## 覆盖性结论

- **完整性**：6 节与英文 35–1～35–6 对应；41 段逐句核对，无漏句、无漏段、无重复粘贴；3 处 `wrapfigure` 前后的断句仅为排版分截，内容连续。
- **公式**：编号式 35.1–35.6 全部存在，`Y=rR+gG`、`X=Y`、`X+Z=Y+Z`、`X=aA+bB+cC`、`Y=a′A+b′B+c′C`、`Z=X+Y=(a+a′)A+(b+b′)B+(c+c′)C` 均与英文一致；未改公式本体，只把正文裸 `X/Y/Z` 收入数学模式。
- **数字/事实**：650 nm、16 Hz、男性 8%/女性 0.5%、1877/1958、一百万比一、50 比 50、1/4 与 3/4 均正确；修正了蟹状星云、Wilson/Palomar 并列、颜料/光混合等事实与逻辑问题。
- **图表**：图 35.1–35.10 齐全，图注与英文一致；正文图引用全部经 `\ref` 解析（0 undefined），无硬编码图号；本章无表。
- **自动候选**：128 条小块 + 25 条大块绝大多数是参考文本 OCR 讹变（壑/蹇、晰/断、勒/勤、晕/党、杆/枉、盏/荔等）或公式/页眉噪声，未据以改动；本次所修问题多为底本翻译、逻辑与排版层，另有少量单字讹变（在用→若用、到达→达到），自动候选未覆盖。

## 验证

- 入口：`preview/chapter-35/check.tex`（`\setcounter{chapter}{34}`、`\input{../../Chapters/VolumeI/Chapter35.tex}`）；仅改注释：章名《基本物理》→《色视觉》，`cd preview/chapter-2`→`cd preview/chapter-35`。
- 命令：`cd preview/chapter-35 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`，连编 2 遍。
- 结果：**14 页；error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0**。PDF 文本抽查：旧串 0 次，新串均出现；第 8 页底部脚注 1/2 排版正常，德文标题无缺字。
- 改动范围：仅 `Chapters/VolumeI/Chapter35.tex`（22 行，CRLF 保持）、`preview/chapter-35/check.tex`（仅注释）、本报告及 `preview/chapter-35/build/` 编译产物；**未 git commit，未运行全书构建，未改其他章**。
