# 第 4 章《能量守恒》审查报告

- **审查对象**：`Chapters/VolumeI/Chapter4.tex`（154 行；4 节；32 个正文段；7 图 + 公式 4.1–4.6 + 2 条脚注）
- **对照材料**：eFLP 英文 `_attachments/build-feynman/audit/en/I_04.txt`（169 行，每段一行；正文段 L36–163）为主；公开中译本 `_attachments/reference/zh/Chapter4.txt`（单行 UTF-8，28,538 字节）仅作旁证；自动候选 `_attachments/reference/candidates/ch4-candidates.md`（257 条小块 + 21 条大块差异）已逐条过。官方页未另取（本地 eFLP 抓取与官网一致）。
- **结果**：问题 **24 条（高 1 / 中 10 / 低 13）**，已全部修正；存疑 6 条未改（见 §4）。修正脚本 `/tmp/fix_ch4.py`（24 处断言式替换，全部命中；CRLF 保持，diff 16 行）。
- **段落对应**：中英 **32 段 : 32 段**——§4-1 7:7、§4-2 14:14、§4-3 3:3、§4-4 8:8。eFLP 抓取文本中 E86/E93/E99/E107/E132 等段被公式断行切碎，已按原书段落归并后核对，**无漏段、无重复、无跨段错位**。

## 1. 高严重度（1 条，已修）

| 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|
| L92 | **整句漏译（OCR 掉句）**：中文"正是从力的分解来得出这个斯蒂维纽司(Stevinus)所发现的方法就铭刻在他的墓碑上"不成句，缺"的结论。然而在这里，巧妙总是相对的。可以用另一种更高明的方法来推导这个结果，这个由"（公开中译本有该句，可证漏抄） | "Note that we deduced this from the conservation of energy, and not from force components. Cleverness, however, is relative. It can be deduced in a way which is even more brilliant, discovered by Stevinus and inscribed on his tombstone."（I_04.txt L112） | 补回："……来得出这个结论的。然而在这里，巧妙总是相对的。可以用另一种更高明的方法来推导这个结果，这个由斯蒂维纽司(Stevinus)所发现的方法就铭刻在他的墓碑上……" |

## 2. 中严重度（10 条，已修）

| 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|
| L92 | **底本删节补回**：英文脚注 2（Stevinus 墓碑从未找到、他以类似图作标志）与句末玩笑句在中文缺失（公开中译本亦无，属底本删节）。补回后为避免脚注与图 4.6 图注在页底相撞，墓碑注改为**文内括注** | "Stevinus' tombstone has never been found. He used a similar diagram as his trademark."；"(If you get an epitaph like that on your gravestone, you are doing fine.)"（L166、L112） | 墓碑注作括注补入"墓碑上（斯蒂维纽司的墓碑从未找到，他把一个类似的图作为自己的标志）"；补"（如果你墓碑上刻着这样的墓志铭，那你就干得不错。）" |
| L92 | OCR 单字讹变致语义反转："但这是**不准的**"（该句讲"推广不难"） | "…but that is easy."（L91） | "但这是**不难的**" |
| L5 | 冒号误入破句："它是物理学**：**最基本的定律之一"；"考查"（全书统作"考察"） | "one of the most basic laws of physics"（L36） | "它是物理学最基本的定律之一"；"考察" |
| L49 | 底本误译："获得**自由的能量**"（free power 被当成"自由能"） | "obtaining free power"（L80） | "获得免费的功" |
| L60 | 分号误作逗号，句读断裂："超过1英尺**；**我们就能创造永恒运动" | "for if 3X exceeds one foot we can make perpetual motion"（L86） | "超过1英尺**，**我们就能……" |
| L70、L74 | 公式 4.4 文字讹变："（力在作用下所通过的距离）" | "(distance force acts through)"（L101–102） | "（力的作用所通过的距离）" |
| L140 | 底本误译＋括号半角/不配对："( 这里……使实验**"斜着"**做）"；"sideways"应为水平方向 | "we can do this experiment 'sideways' if we like"（L149） | "（这里……使实验"**平着**"做）" |
| L142 | 语法不成句："**假若**极其仔细和精致地安排了机械的各个组成部分**后**" | "with great care and delicacy in the arrangement of the parts one can try…"（L151） | "**在**极其仔细和精致地安排了机械的各个组成部分后" |
| L144 | 底本术语误译："我们知道它不是电能，不是重力能，也不纯粹是**化学能**" | "We know that it is not electrical, not gravitational, and not purely **kinetic**"（L153） | "……也不纯粹是**动能**" |
| L148 | 主谓间缺逗号："第一条是电荷守恒定律**这只是**意味着" | "The first of the three is the conservation of charge, and that merely means…"（L157） | "电荷守恒定律**，**这只是意味着" |

## 3. 低严重度（13 条，已修）

| 行号 | 问题 | 修正 |
|---|---|---|
| L9 | "又有几天，经过仔细的清点表明总共有30块"（英文 Another day，指某一天） | "又有一天……" |
| L9 | 破折号误作"一"："她知道**—**块积木重3英两" | "一块积木" |
| L9 | "goes to open"漏"要"（她尚未打开即被孩子拦住） | "母亲走过去**要**打开这个箱子" |
| L27 | 破折号误作"一"："她发现了**—**系列的项" | "一系列" |
| L38 | 全角空格嵌入句读："永恒运动，　假如我们" | "永恒运动。假如我们" |
| L49 | 破折号后误用分号："——一台可逆机；在它使" | "——一台可逆机，在它使" |
| L92 | 两段 `\uwave` 间夹空格："都是一 回事" | "都是一回事" |
| L101 | 句号讹作逗号："走过1260英寸，如果我们" | "走过1260英寸。如果我们" |
| L130 | 漏译短语："它能升高的高度"缺"corresponding to its velocity" | 补"（这个高度与它的速度相对应）" |
| L135 | 段末缺句号："能量守恒定律是正确的" | 补"。" |
| L140 | 省略号后多句号："直到能量失掉为止……。" | "……" |
| L148 | 并列成分用逗号："电子，μ介子和中微子" | "电子、μ介子和中微子" |
| L154 | 形近字："**大**阳形成了降雨" | "太阳" |

## 4. 存疑项（未改，供上游判断）

1. **L142**"多么奇怪！" ← "What a dream!"：底本（公开中译本同）译作"奇怪"，语气偏；改"多么奇妙"更贴，但属底本译法，未动。
2. **L148**"存在着一些**奇异粒子**，例如中子和质子" ← "There are a number of **strange** particles, a neutron and a proton are examples, which are called baryons."（L157）"奇异粒子"是现代术语（strange particles），但费曼此处举例中子是重子，用词偏口语；是否改"奇特的粒子"请定。
3. **L31/L146**"以一定数量的**滴状**形式出现""一个个的**滴状**形式" ← "little **blobs**"；"滴状"为底本译法（公开中译本作"颗粒"），未动。
4. **L140**"弹性能就是关于弹簧被伸长时这个事实的**表述**" ← "Elastic energy is the **formula** for a spring when it is stretched."（L149）"formula"未译出，底本即如此。
5. **L146**"其他的守恒定律也有**联带**的关系" ← "linked together"；"联带"可改"连带"，属用词，未动。
6. **图号体例**：正文"图4.1–4.7"为硬编码，未改 `图\ref{label}`；编译核验图注渲染为"图 4.x"，正文因 xeCJK 在"图"与数字间自动加空隙，显示一致（与第 2/3 章体例相同），`\label` 虽为孤儿但无编译风险。

## 5. 覆盖性结论

- **完整性**：无漏段、无重复粘贴、无整段错位；英文每句均可对应（唯一整句漏译为 L92，已补）。
- **数字/量纲**：28/27/26/30/25 块积木、3 英两/16 英两、6 英寸/1/4 英寸、3–4–5 斜面、3/5 磅、5/3 英尺、20 英寸/每英寸 10 圈/126/1260 英寸/1 吨=2000 磅/1.6 磅、8 英尺/60 磅/2 英尺/100 磅/4-2-1 英寸/W=55 磅、3x=1 英尺、p 与 1/p、75 条法则、二十亿分之一、10 夸脱/秒＝150 加仑/分——全部与英文一致，无数字错误。
- **公式/图**：公式 4.1–4.6 编号、内容、`\ref` 引用正确；图 4.1–4.7 与图注、正文引用一一对应（编译渲染核验），无错配。
- **人名/专名**：丹尼斯、布鲁斯、卡诺、斯蒂维纽司、爱因斯坦、普朗克等均正确。
- **候选清单**：257 小差异多为公开中译本自身 OCR 误或底本用字差异（英两/oz、英尺/ft、考查/考察、指出/表明等），未据其改动；其中确属本库 OCR 讹变的 4 处（L9"又有几天"、L9"—块"、L27"—系列"、L60"不准"）已改。21 条大块差异除 L92 漏句外，均为参考文本的公式/图注/页眉噪声或脚注位置差异。

## 6. 验证

- 单章入口：**新建 `preview/chapter-4/check.tex`**（复制 chapter-2 模板；`\setcounter{chapter}{3}`；`\input{../../Chapters/VolumeI/Chapter4.tex}`；加载 `styles/readability`）。
- 编译：xelatex 连编 2 遍 → **10 页，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**。
- 版式抽查（PDF 渲染）：图 4.2/4.3/4.4/4.5/4.6/4.7、公式 4.1–4.6、脚注 1/2 均正常；补入的玩笑句、文内墓碑注、L130 括注无孤行/溢版。
- 未提交 git；仅改动 `Chapters/VolumeI/Chapter4.tex`、新建 `preview/chapter-4/`、本报告。
