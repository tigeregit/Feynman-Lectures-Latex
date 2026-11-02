# §3-1 引言 + §3-2 化学 · 精读审查报告

- 审校员：rev2-s1
- 中文正文范围：`Chapters/VolumeI/Chapter3.tex` L3–15（§3-1 引言：L3 起，正文 L5 共 1 段；§3-2 化学：L7 起，正文 L9、L11、L13 共 3 段）
- 英文对照：`_attachments/build-feynman/audit/en/I_03.txt` L37–47（3–1 Introduction：L37 起，正文 L39；3–2 Chemistry：L41 起，正文 L43、L45、L47）
- 说明：本章正文无阅读效率 `%<<<NEW … %>>>NEW` 导读块（与 00-conventions §0 一致），全部为 OCR 原文。本节无数字、年份、化学式、图表，故不涉及数字与图表核对；英文引用均逐字取自 I_03.txt。

## 问题表格

| # | 行号 | 严重度 | 类型 | 中文原文（≤30 字，问题处加粗） | 问题说明 | 英文依据（≤25 词原文引用） | 建议改法 |
|---|---|---|---|---|---|---|---|
| 1 | L5 | 中 | 错字 | 这些**坝域**中的…；这只是**意味看**它不是科学 | 两处 OCR 形近错字："坝域"不成词，应为"领域"（同段前文即作"许多领域内"）；"意味看"应为"意味着"（同句前半"并不意味着"亦证）。 | —（OCR 错字，无对应英文） | 这些领域中的…；这只是意味着它不是科学而已 |
| 2 | L5 | 中 | 术语/物理 | 例如，**爱好**就不是科学 | 英文为 "love is not a science"，love 指"爱、爱情"；译作"爱好（hobby）"改变了费曼的举例（他要说明"不是科学并不等于不好"，"爱"正是典型）。公开流传的同一中译本文字亦作"爱好"，应属底本翻译即如此，非本仓库 OCR 讹变。 | "For example, love is not a science." | 例如，爱就不是科学。（或"爱情"） |
| 3 | L9 | 中 | 错字 | 擅长下棋**之问**的差别 | "之问"应为"之间"（OCR 形近），"了解下棋规则与擅长下棋之间"才成句。 | —（OCR 错字；对应英文 the difference between knowing the rules of the game of chess, and being able to play） | 我们已经讨论过了解下棋规则与擅长下棋之间的差别。 |
| 4 | L9 | 低 | 漏字/多字 | 组成在矿石、土壤里所发现的**简单化合物** | 英文为 the various relatively simple compounds，中文漏译"各种（various）""相对（relatively）"两个限定词，把"相对简单的化合物"绝对化成"简单化合物"。 | "how they make the various relatively simple compounds found in rocks, earth, etc." | 组成矿石、土壤里所发现的各种相对简单的化合物 |
| 5 | L11 | 中 | 错字 | 力学定律起作用的**场台** | "场台"不成词，应为"场合"（OCR 形近）；与任务提示所疑一致。 | —（OCR 错字；对应英文 the method of statistics applied in a situation in which there are mechanical laws） | 力学定律起作用的场合 |
| 6 | L11 | 低 | 术语/物理 | 物理化学研究**反应率**和所发生的详细变化 | 化学术语 "reaction rates" 应作"反应速率"；"反应率"易与转化率、产率混淆。 | "physical chemistry to study the rates at which reactions occur" | 物理化学研究反应速率和所发生的详细变化 |
| 7 | L11 | 低 | 术语/物理 | 哪一些**分子**先飞离 | 英文 "Which pieces fly off first?"，pieces 指碰撞后飞离的碎片、基团；译"分子"把主体具体化错了（前文已说分子相撞）。 | "Which pieces fly off first?" | 哪些碎片先飞离 |
| 8 | L13 | 中 | 错字 | 从无机**村料**中制造…；然而，**育机**化学的主要任务 | 两处 OCR 形近错字："村料"应为"材料"；"育机化学"应为"有机化学"（同段前文两次均作"有机化学"）。 | —（OCR 错字；对应英文 from inorganic materials；organic chemistry） | 从无机材料中制造…；然而，有机化学的主要任务 |
| 9 | L13 | 中 | 术语/物理 | 许多物理化学和**量子化学**的定律 | 英文此处为 quantum mechanics（量子力学），与上一段 quantum chemistry（量子化学）是两门学科；中文两处都作"量子化学"，把量子力学与量子化学混同。 | "much physical chemistry and quantum mechanics can be applied to organic as well as to inorganic compounds" | 许多物理化学和量子力学的定律 |
| 10 | L13 | 低 | 术语/物理 | 在于**分析、综合**那些…物质 | 化学的 analysis and synthesis 应作"分析（分解）与合成"；"综合"是通用词，非化学术语"合成（synthesis）"。 | "in the analysis and synthesis of the substances which are formed in biological systems" | 而是在于分析、合成那些在生物系统以及在生命体中所形成的物质 |

## 存疑项

1. **L13 "如此神秘"** ← "so marvelous"：marvelous（奇妙、不可思议）译作"神秘（mysterious）"略偏，但句意可通（人们曾以为生命物质奇妙到无法人工合成）；是否改由 Lead 定。
2. **L13 "有机化学的主要任务"** ← "the main problems of organic chemistry"：problems（主要问题）被译成"任务（tasks）"，语义偏移；可能属原译风格，仅标注。
3. **L9 "在矿石、土壤里"** ← "found in rocks, earth, etc."：rocks 本义"岩石"，译"矿石"偏指可提炼金属的矿石，范围变窄；同句 earth→"土壤"无误。
4. **L11 "在任何化学状态中"** ← "In any chemical situation"：situation 指"化学过程、化学体系"，"化学状态"易被读成物质的状态；句意仍通。
5. **L11 "统计力学就是关于热现象或热力学的理论"** ← "the science of the phenomena of heat, or thermodynamics"：此处 or 为同位语（即热力学），中文"或"易读成二选一；不影响理解。

## 覆盖性结论

- **段落对应**：中文 §3-1（L3 标题、正文 L5，1 段）↔ 英文 3–1（I_03.txt L37 标题、正文 L39，1 段）；中文 §3-2（L7 标题、正文 L9、L11、L13，3 段）↔ 英文 3–2（L41 标题、正文 L43、L45、L47，3 段）。**4 段对 4 段，逐段 1:1**；§3-2 三段英文句数 11/6/6 与中文一致，§3-1 英文括号内两句在中文合为一句（内容无缺），无跨段错位、无合并/拆分、无整段缺失或重复粘贴。
- **完整性**：无漏句、无整段漏译；仅 L9 一处限定词漏译（various / relatively，见 #4）。
- **数字 / 年份 / 名称 / 术语**：本节无数字、年份、化学式；人名仅 Mendeleev，中文作"门捷列夫"（规范译名，无误）。无机化学、有机化学、物理化学、量子化学、统计力学、热力学、自然哲学均与英文对应；唯 L13 的 quantum mechanics 被译作"量子化学"（#9）。无数字类问题。
- **OCR 错字**：共 6 个单字讹变——坝域→领域、意味看→意味着、之问→之间、场台→场合、村料→材料、育机→有机；均不成词或与上下文矛盾，属明显 OCR 错误。其中"坝域/意味看/之问/场台/村料"在公开流传的同一中译本转录中亦见同样讹字，可佐证为 OCR 层问题；"育机"未在公开转录中核到，按形近（有↔育）判为 OCR。L5 的"爱好"则为底本翻译问题（非 OCR）。
- **总体判断**：4 段内容忠实、结构完整，**无高严重度问题**（无漏句漏段、无重复、无数字错误）。共 10 条：高 0 / 中 6 / 低 4。建议优先修 4 组 OCR 错字（#1、#3、#5、#8）与 #9（量子力学），#2（love→爱）建议一并改。
