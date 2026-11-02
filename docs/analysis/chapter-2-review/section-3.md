# §2-3 量子物理学 · 精读与内容审查

- 审查对象：`Chapters/VolumeI/Chapter2.tex` L70–84（§2-3；正文 L72 / L74 / L76 / L78 / L80 / L82，共 6 段）
- 对照文本：`_attachments/build-feynman/audit/en/I_02.txt` L96–109（2–3 Quantum physics；正文 L98 / L100 / L102 / L104 / L106 / L108）；L80 的漏句与 QED 定义另用官方网页 <https://www.feynmanlectures.caltech.edu/I_02.html> 复核，与 eFLP 抓取文本一致。
- 行号均为 `read` 工具显示行号。
- 结果：**高 3 · 中 4 · 低 6**（共 13 条）；另有存疑 7 项。数字与公式本身无错（见文末「数字/符号逐项核对」）。

## 问题清单

| # | 行号 | 严重度 | 类型 | 中文原文（≤30 字，问题处加粗） | 问题说明 | 英文依据（≤25 词原文引用） | 建议改法 |
|---|---|---|---|---|---|---|---|
| 1 | L74 | 低 | 术语/物理 | 量子力学中有许多**看法**。 | `aspects`（方面/侧面）译作“看法”，易被理解为“对量子力学有多种意见或解释”；本段下文列举的是量子力学的内容本身，并非观点之争。 | “Quantum mechanics has many aspects.”（L100） | 量子力学有许多方面。 |
| 2 | L74 | 中 | 错字 | 又知道它运动得**多块**。 | “how fast”＝多快；“块”是“快”的形近 OCR 错字，且出现在“不能同时知道位置与速度”的关键句，读者需停顿。 | “one cannot know both where something is and how fast it is moving”（L100） | 又知道它运动得多快。 |
| 3 | L74 | 高 | 术语/物理 | 二者的乘积**是常数**。 | 英文为“bounded by a small constant”（以一个小常数为界/下界），中文“是常数”把不等式说成等式，与紧接着的 ΔxΔp≥ℏ/2 自相矛盾，物理表述错误。 | “the product of the two is bounded by a small constant”（L100） | 二者的乘积以一个小的常数为下界。 |
| 4 | L74 | 低 | 错字 | 更详尽**的**解释它 | “解释”此处作动词，状语应用“地”；“的/地”误用。 | “but we shall explain it in more detail later”（L100） | 在以后将会更详尽地解释它。 |
| 5 | L74 | 中 | 错字 | 放大到一个大房间**大样大**。 | “大样大”不成句，应为“大房间那样大”，系 OCR 形近误字（“那”误作“大”）。 | “we would have to magnify it until the whole atom was the size of a large room”（L100） | 就要把整个原子放大到一个大房间那样大。 |
| 6 | L76 | 低 | 漏字/多字 | 比如有一个**实验室**在斯德哥尔摩观察天空 | 英文是“if one of the experiments is to look out at the sky”，指“其中一个实验”，不是“实验室”；多一“室”字使主语变成实验室。 | “if one of the experiments is to look out at the sky and see the aurora borealis in Stockholm”（L102） | 比如有一个实验是在斯德哥尔摩观察天空 |
| 7 | L76 | 中 | 漏字/多字 | 在一个**方向接头**上挂一个摆 | “universal joint”＝万向接头；本书 Chapter39 L233 即作“万向接头”，此处脱“万”字，成为非标准术语。 | “If we take a pendulum on a universal joint, and pull it out and let go”（L102） | 假如我们在一个万向接头上挂一个摆 |
| 8 | L76 | 中 | 错字 | 在事先就被告**诫**说 | 英文“we do not have to be told ahead of time”；“告诫”＝警告劝诫，与“told（被告知）”不符，语义偏移。 | “we do not have to be told ahead of time what this way will look like”（L102） | 而没有必要在事先就被告知说 |
| 9 | L80 | 高 | 术语/物理 | 新的**电子质子**相互作用的见解称为量子电动力学 | 英文为“the interaction of electrons and photons”；QED 是电子与光子的相互作用，不是电子与质子；同句后文“光和物质……相互作用的基本理论”亦可证。 | “the interaction of electrons and photons”（L106） | 关于电子与光子相互作用的新见解称为量子电动力学 |
| 10 | L80 | 高 | 漏句/漏译 | 就物理学来说它是我们最伟大的成就。**〔此处缺一整句〕** | 英文有一整句但中文完全无对应：“在这一个理论中，我们掌握着除引力与核过程以外的一切普通现象的基本规律”。中文从“……最伟大的成就。”直接跳到“比如，……”，整句漏译；而该句正是本节交代 QED 适用范围的关键信息。 | “In this one theory we have the basic rules for all ordinary phenomena except for gravitation and nuclear processes.”（L106） | 在“……最伟大的成就。”之后、“比如，从量子电动力学……”之前补：在这一理论中，我们掌握了除引力与核过程以外的一切普通现象的基本规律。 |
| 11 | L80 | 低 | 漏字/多字 | 就物理学来说它是我们**最伟大的成就** | 英文“our greatest success so far in physics”漏译“so far（迄今为止）”，语气绝对化，且与后文“目前……还没有发现例外”的时间限定不协调。 | “is our greatest success so far in physics”（L106） | 就物理学来说它是我们迄今为止最伟大的成就 |
| 12 | L80 | 低 | 术语/物理 | 这实际上**当然不可能** | 英文“which is almost never”（几乎从不）指“情况简单到能做近似的场合极少”，中文“当然不可能”把“极少”说成“不可能”，程度过强。 | “if the situation is simple enough for us to make an approximation, which is almost never”（L106） | 这实际上是几乎不可能的 |
| 13 | L82 | 低 | 漏字/多字 | **所有**世界上其他的数 | 英文“most of the other numbers in the world”（大多数），中文漏“大多数”而作“所有”，与下一句“实际上，这不完全正确”形成不必要的矛盾。 | “two numbers are put in and most of the other numbers in the world are supposed to come out”（L108） | 世界上大多数其他的数被认为可以从这两个数据推导出来 |

## 存疑项

1. **L74「并协的」**：英文“complementary”。标准物理术语为“互补”（Bohr 互补原理），全书仅此一处作“并协”，非通行译法但语义可通；是否统一为“互补的”请上游决定（未列入上表）。
2. **L74「描写这种习性」、L78「粒子的习性」「波的习性」**：behavior 一词在同节又译作“行为”（L72、L74、L78 多处），“习性”为旧译用词，前后不统一；语义可通，是否统一为“行为/表现”待定。
3. **L72「万有引力则大概是空－时的一种变态」**：modification 译作“变态”，现代汉语易生“异常”歧义；但可能为原译用词，若要统一术语可改“一种改变/变形”。仅标注，不改。
4. **L74「起先曾认为原子核很大」**：英文“It was first thought that this was because the nucleus was so big”，“这是因为”未译出，因果链略弱；不影响物理理解。
5. **L76「这些总是相当天真的，甚至还是错误的」**：英文“rather naive, and probably wrong”，“probably（大概/可能）”未译出，语气偏强；同句“对科学的成就来说”对应“to the scientific effort（科学事业/工作）”，“成就”略有偏移。仅标注。
6. **L74「于是以由这个定则所决定的最小的运动晃动着」**：英文“……with a certain amount of minimum motion in accordance with this rule”，“一定量的”未译出，且“以……运动晃动”略拗口；理解无碍。
7. **L76「看起来象什么」**：用“象”而非“像”，属旧式用字（全书“象/像”混用，非本段独有），未单列；另“空－时”用全角连字符，本章 L72/L116 内部一致，故不报（跨章与 Chapter17「空—时」不统一，供全局风格统一时参考）。

## 覆盖性结论

### 中英段落对应

| 中文 | 英文 | 结果 |
|---|---|---|
| L70 `\section{量子物理学}` | L96 “2–3 Quantum physics” | 对应 |
| L72（段首“说明了电磁场概念……”） | L98（段首“Having described the idea……”） | 逐句对应，无缺失 |
| L74（段首“量子力学中有许多看法。”） | L100（段首“Quantum mechanics has many aspects.”） | 逐句对应；问题 #1–5 |
| L76（段首“另一个由量子力学带来的……”） | L102（段首“Another most interesting change……”） | 逐句对应；问题 #6–8 |
| L78（段首“现在让我们回到量子力学……”） | L104（段首“Returning again to quantum mechanics……”） | 逐句对应，无问题 |
| L80（段首“于是，我们对电磁相互作用……”） | L106（段首“Thus we have a new view……”） | 缺 1 整句；问题 #9–12 |
| L82（段首“这样，在原则上……”） | L108（段首“In principle, then,……”） | 逐句对应；问题 #13 |

- 无整段缺失、无整段重复、无段落错位；句子层面仅 L80 漏 1 整句（#10）。
- L82 中“正电子”出现两次与英文原文一致（英文亦两次称 positron），**不属重复错误**，不要删改。
- 已核对且**无问题**的要点：1920 年前后的图景变化（Einstein 把空间与时间合为 space-time、以弯曲 space-time 表示引力、Newton 定律在原子世界失效）；小尺度行为“反常”、我们对其无直接经验；原子直径 $10^{-8}$ cm、原子核直径 $10^{-13}$ cm、把原子放大到房间大小时核只是小点；电子不塌入核的论证；晶体冷却到绝对零度原子仍振动；量子力学的统计本性（不能精确预言、光子发射时刻不可预言、没有内部“转轮”）；哲学家议论（“同样的条件必产生同样结果”不是科学的基本条件、斯德哥尔摩 vs 基多、极光、傅科摆式进动、实验是唯一试金石）；波粒二象性与场—粒子统一；每秒 $10^{12}$ 周以上尚无直接频率探测；QED 把化学与生命归结为物理；正电子与每个粒子的反粒子；QED 的两个输入数（电子质量与电荷）及化学的核质量参数。

### 数字/符号逐项核对

| 项目 | 中文（行号） | 英文 | 判断 |
|---|---|---|---|
| 原子直径 | $10^{-8}$ 厘米（L74） | 10−8 cm | ✓ |
| 原子核直径 | $10^{-13}$ 厘米（L74） | 10−13 cm | ✓ |
| 频率上限 | 每秒 $10^{12}$ 周以上（L78） | above approximately 1012 cycles per second | ✓ 指数 12 正确（“approximately/约”未译，可忽略） |
| 不确定关系 | $\Delta x\,\Delta p\geq\hbar/2$（L74） | ΔxΔp≥ℏ/2 | ✓ 公式与系数 ℏ/2 正确（但前一处分句错误，见 #3） |
| QED 输入数 | 两个基本数据：电子质量与电荷（L82） | two numbers: the mass of the electron and the charge of the electron | ✓ |
| 年份 | 1920 年后 / 1920 年之前（L72） | just after 1920 / before 1920 | ✓ |
| 房间比喻 | 大房间（L74） | the size of a large room | ✓（文字“大样大”待改，见 #5） |

### 总体判断

正文主体与英文原文一致，物理框架完整，未发现数字/量纲/公式系数错误。最严重者为 **L80 把 QED 说成“电子质子”相互作用（#9）** 与 **L80 漏译“除引力与核过程外一切普通现象的基本规律”整句（#10）**，次为 **L74 把“受小常数限制”写成“是常数”（#3）**——这三处直接改变物理含义，建议优先修正。4 处中等问题（L74 “多块”“大样大”、L76 “方向接头”“被告诫”）均为 OCR/形近性质，建议 Lead 一并改。低严重度 6 条为措辞、漏词与语气细化。

**附注（不在本报告修改范围）**：同源样张 `preview/content-pilot/ch2-pilot-body.tex` L162/166/178/184/190 含与 `Chapter2.tex` 完全相同的错误（“多块”“并协……是常数”“大样大”“方向接头”“被告诫”“电子质子”及缺句），其中错误句还被 `\keyidea{}` 标为要点；该样张日后若合并/定稿需同步修正。
