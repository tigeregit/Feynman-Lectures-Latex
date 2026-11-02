# 第 15 章《狭义相对论》审查报告

- 范围：`Chapters/VolumeI/Chapter15.tex`（原 292 行，9 节；修后 290 行）。对照 `_attachments/build-feynman/audit/en/I_15.txt`（419 行，公式被拆成多行；正文 41 段 + 1 条脚注）、官方页 <https://www.feynmanlectures.caltech.edu/I_15.html>；旁证 `_attachments/reference/zh/Chapter15.txt` 与 `ch15-candidates.md`（小块差异 253 条、大块 43 条；逐条判定，多数为参考文本 OCR 噪声或底本译法，实际需改 27 处）。
- 段落对应：中英段落非 1:1（英文公式拆行）；按节逐一核对：§15-1 相对性原理、§15-2 洛伦兹变换、§15-3 迈克耳逊-莫雷实验、§15-4 时间的变换、§15-5 洛伦兹收缩、§15-6 同时性、§15-7 四维矢量、§15-8 相对论力学、§15-9 质能相当性——**无整段缺失、无重复粘贴**。
- 结果：**已修 27 处（高 4、中 6、低 17）**，存疑 10 条（不改，交 Lead 复核）。修改均为行内替换（L51–53 段落合并使后文行号 −2），已保留 CRLF。
- `preview/chapter-15/check.tex` 由 `python3 tools/make_chapter_check.py 15` 生成；本报告修正其注释章名/路径，并加入"跨章引用桩"（见存疑 8）。

## 高/中问题表（行号为修改前）

| 行号 | 问题（原文） | 英文依据（逐字引用） | 修正 |
|---|---|---|---|
| L147 | **漏整句**：段首直接从"必须看看钟的机构"开始 | "This slowing of the clocks in a moving system is a very peculiar phenomenon, and is worth an explanation. In order to understand this, we have to watch the machinery of the clock" | 段首补："这种运动系统中的时钟减慢是一种非常奇特的现象，值得解释一下。为了理解这一点，我们必须看看钟的机构……" |
| L51–53 | **段落断裂**：L51 以"而应"结束，L52 空行，L53 以"当是（$c-u$）"开头，"应当"被拆成两段 | "the apparent speed … should not be c but should be c−u" | 合并为"……不应当是$c$而应当是（$c-u$）。例如……"（该句回到同一段） |
| L107 | 公式 **$(ut3)^2$** 缺下标 | "(ct3)2=L2+(ut3)2" | $(ut_3)^2$ |
| L178 | 上下文写"两个相应的时间$t_1$与$t_2$"，**缺撇号** | "the two corresponding times t′1 and t′2 differ by an amount" | $t'_1$ 与 $t'_2$ |
| L47 | "假定我们以速度驱车前进"**缺 $u$** | "a car that is going at a speed u" | 假定我们以速度$u$驱车前进 |
| L72 | "**稍微花一点时间**来讨论"（at some length 误译） | "we shall have to discuss these ideas … at some length" | 我们将不得不用一些篇幅来讨论 |
| L87 | 时间符号 **$t$** 应为 $t_1$（下文公式用 $t_1$） | "the time … is t1, and the time for the return is t2" | 所需的时间为$t_1$，返回的时间为$t_2$ |
| L145 | 句子被"。"截断且多"的原因"："……这段时间$2t_3$。由那个……算出的结果不一样的原因，对于……" | "That is because the time 2t3 … is not the same when calculated by a man … as when calculated by a stationary observer" | "……所花的这段时间$2t_3$，由那个在飞船上做实验的人算出的结果与由另一个观看飞船飞行的静止观察者算出的结果不一样。对于在飞船上的人来说，时间就是$2L/c$……" |
| L164 | "路程也**不会超过600米以上**"（much more than 误译） | "cannot travel … much more than 600 meters" | 也不会比600米多多少 |
| L292 | "由**物质没**而完全转化"**缺字** | "matter is annihilated—converted totally to energy" | 由物质湮没而完全转化为能量 |

**低 17 处（已修，摘要）**：L16 多余句号（"$m_0$。表示"→"$m_0$表示"）；半角标点→全角共 11 处（L43、L87、L91×2、L105×2、L127、L134、L145、L164、L166）；L80 图注"迈克尔逊"→"迈克耳逊"（与正文 9 处统一）；L147"一米尺"→"一根米尺"；L162"以致"→"以至"；L222"当v大到接近于c"→数学体 $v$/$c$；L222 脚注补句号；L216 动量符号 $\boldsymbol{P}$→$\boldsymbol{p}$（全卷他处均用 $\boldsymbol{p}$，英文为 p）。

## 存疑项（未改，需 Lead 决定）

1. **L16"$3 \times 10^8~m \cdot s^{-1}$"**：英文 "3×10⁵ km⋅sec⁻¹"，中文换算为 m/s 数值等价（正确），未改；若求单位与原文一致可改 $3\times10^5$ km·s⁻¹。
2. **L222"（约700 ft远）""1/1000 in"**：保留英制符号 ft/in（原文如此、上文用 mi），未统一为"英尺/英寸"。
3. **L222"射到邻近一个实验室"**：原文 "rush out to Bridge Lab"（Bridge 实验室专名）未译出，底本如此，未改。
4. **L160"嘿！假如果真发生这种事"**：原文 "Ah no, if that should happen"，否定语气 "no" 未译出，未改。
5. **L72"说明在前"**：原文 "so we say in advance"，底本作"说明在前"，保留未动。
6. **§15-8 标题"相对论力学"**：英文 "Relativistic dynamics"；传统译法，保留。
7. **图文件名**：仍为 `Chapter15/迈克尔逊-莫雷实验的示意图.pdf`（label 含"迈克尔逊"），仅图注统一为"迈克耳逊"；是否重命名图文件/改 label 待 Lead 定（影响全书面）。
8. **跨章引用 `\ref{Eq:I:9:1}`（L253）**：正文保留 `\ref`（全书合编由第 9 章提供，正常）；单章编译无法解析，已在 `preview/chapter-15/check.tex` 加引用桩 `\@namedef{r@Eq:I:9:1}{{9.1}{1}{}{}{}}` 解决，不属正文错误。
9. **"负电子"（L292）**：原文 "An electron and a positron"；"负电子"即电子，可接受，未改。
10. **装置字母（L85"光源A…玻璃片B…镜子C和E"）用普通字体**：与全书版面惯例一致，未改。

## 覆盖性结论

- **公式**：15.1–15.18 逐式核对（15.1 质量公式、15.2 伽利略变换、15.3 洛伦兹变换、15.4/15.5 光程时间、15.6/15.7 收缩与时间、15.8 转动类比、15.9 不变量、15.10 动量、15.11 级数展开、15.12–15.18 质能关系推导）；除上表两处符号错误外，上下标、系数（1/2、3/8）、符号方向均正确。15 个 `\label` 与全部 `\ref` 一一对应。
- **数字**：200 多年、1905/1915、20 年、1887、18 年、186000 mi/s、100000/86000 mi/s、$3\times10^8$ m/s、5 mi/s、20 亿–30 亿分之一、18 mi/s、$2.2\times10^{-6}$ s、600 m、10 km、2 μs、9/10、1/4,000,000、8,000,000、2000 倍、700 ft、1/1000 in、纸厚 1/4、20 kilotons、1 g —— 均与 eFLP 一致。
- **人名/专名**：惠更斯(Huygens)、庞加莱(Poincaré)、迈克耳逊(Michelson)、莫雷(Morley)、洛伦兹、爱因斯坦、乔(Joe)/莫(Moe)——均一致（迈克耳逊已统一）。
- **图**：图 15.1、15.2、15.3 的图号、图注（含 a/b/c 三小图）与正文引用一致；引用均用 `\ref`。
- **脚注**：同步加速器比赛脚注（L222）完整，仅补句末句号。
- **无漏段/重复**；§15-1…§15-9 各节内容完整。

## 验证（单章编译）

`preview/chapter-15/` 连编 2 遍：**0 error、0 Overfull、0 Underfull、0 Missing character、0 undefined references；PDF 14 页（A4）**。跨章引用桩使 `Eq:I:9:1` 正确渲染为"式（9.1）"。

## 未改动与建议

- 存疑 1–10 建议 Lead 复核；其中 2、3、7 属版面/专名统一问题，7 若改需同步改 `\includegraphics` 路径与 label。
- 修改集中在 21 行（21+/23−；L51–53 合并减少 2 行），便于复核 diff。
