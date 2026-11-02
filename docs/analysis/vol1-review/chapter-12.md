# 第 12 章《力的特性》审查报告

- **审查对象**：`Chapters/VolumeI/Chapter12.tex`（216 行；6 节；54 个内容段；4 图；编号公式 12.1–12.11 + 6 个无编号公式）
- **对照材料**：eFLP 英文 `_attachments/build-feynman/audit/en/I_12.txt`（202 行，正文段 L36–198）为主；公开中译本 `_attachments/reference/zh/Chapter12.txt`（15,209 字符，单行；仅旁证）；自动候选 `_attachments/reference/candidates/ch12-candidates.md`（270 条小块 + 28 条大块）逐条过。官方页未另取（本地 eFLP 抓取与官网一致）。
- **结果**：问题 **8 条（高 1 / 中 3 / 低 4）已全部修正**；存疑/未改 11 条（见 §4）。修正脚本 `/tmp/fix_ch12.py`（8 处断言式替换，全部命中；CRLF 保持，diff 仅 7 行）。
- **段落对应**：中英 **54 段 : 53 段**——§12-1 10:11（英文 E46/E48 两段在中文合并为 L15）、§12-2 12:11（E68 因插图拆为 L44/L46）、§12-3 6:5（E87 因插图拆段）、§12-4 17:17、§12-5 8:8、§12-6 1:1。**无漏段、无重复、无跨段错位。**

## 1. 高严重度（1 条，已修）

| 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|
| L193 | **伽利略变换公式错误**：末式写成 `m d²x′/dt² = F_{x′}−ma`，漏掉中间的 `=F_{x′}`，等式把已含 −ma 的 F_{x′} 又减了一次 ma | "m d²x′/dt² = Fx′ = Fx−ma"（I_12.txt L177–181） | `m\frac{d^2x'}{dt^2}=F_{x'}=F_x-ma` |

## 2. 中严重度（3 条，已修）

| 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|
| L54 | 底本误译：**"in spite of the enormous engineering value of an accurate analysis"** 被译成"尽管有大量精确分析的工程数据"（凭空多出"工程数据"，原意是"尽管精确的分析具有巨大工程价值"） | "It is quite difficult to do accurate quantitative experiments in friction, … in spite of the enormous engineering value of an accurate analysis."（L78） | "尽管精确的分析具有巨大的工程价值，要做精确的定量摩擦实验仍然是非常困难的……" |
| L197 | 底本误译：英文中 **throwing things outward toward the walls** 是"神秘的力"的分词修饰语，不是观察者"把东西抛向墙壁"；原译把施动者弄反 | "An observer in a rotating coordinate system … will find mysterious forces, not accounted for by any known origin of force, throwing things outward toward the walls."（L184） | "……观察者将会发现一些用任何已知起源的力都解释不了的神秘的力，这些力把东西向外甩向墙壁。" |
| L41 | 图 12.1 图注误译：英文 caption 为 **"for sliding contact"（滑动接触）**，中文作"接触面相对光滑时"，故改为"相对滑动时"（仅改图注文字；文件名与 `\label` 仍为历史命名，见 §4-11） | "Fig. 12–1. The relation between frictional force and the normal force for sliding contact."（L70） | "接触面相对滑动时的摩擦力与法向力的关系" |

## 3. 低严重度（4 条，已修）

| 行号 | 问题 | 修正 |
|---|---|---|
| L9 | 译者注脚注缺句末句号 | "……杜撰}" → "……杜撰。}" |
| L9 | "suggestion"误译"联想"（英文 "it is a suggestion that the forces will be simple"，应为"暗示/提示"） | "力是简单的则是一种联想"→"它暗示着力是简单的" |
| L21 | "and then"误译"此外"（英文 "everything can be defined, and then we do not know what we are talking about"） | "此外我们就不知道在说些什么了"→"然后我们就不知道自己在说些什么了" |
| L195 | "apparent"误译"明显的"（英文 "here is an apparent, mysterious new force of unknown origin"，意为"表面上的/虚表的"，非"显而易见"） | "这是一个明显的、……新力"→"这是一个表面上的、……新力" |

## 4. 存疑项（未改，供上游判断）

1. **L85** ε₀=8.85×10⁻¹² 与英文 8.854×10⁻¹² 的有效数字差异；8.85 是通行三位有效数字写法，非错误，未改。
2. **L210**"加速度产生引力的赝物"（"an imitation of gravitation"）；"赝物"生硬，底本如此。
3. **L119**"对这些情况的性质的第二部分分析"（英文 "The second part of the analysis of nature in these situations…"）；语序拗口但可解，未改。
4. **L17**"灰尘落到椅子上，逐渐溶化到油漆里"（"gets dissolved in the paint"；"溶化"非"溶解"，底本）。
5. **L31**"我们发现它越来越'不真实'"（"falser and falser"，底本译法）。
6. **L52**"看起来好像是结合在一起的"（"so that they appear to bind"；bind 宜作"卡住/咬合"，底本）。
7. **L7**"当两个球相互碰撞"（英文 "when two balls push against each other"，是相互挤压而非碰撞，底本）。
8. **L15**"$F=ma$ 这条定理"（law 全书多作"定律"，此处"定理"用词不统一）。
9. **L179**"下面，我们将讨论的这一类力可以称为赝力"（语序略拗，底本）。
10. **L216**`F=(1/r^2)exp(-r/r_0)` 中 exp 未用正体 `\exp`（纯排版，公式内容未动）。
11. 图 12.1 的文件名/`\label` 仍作"…相对光滑…"（本次只改图注文字，未重命名图件与标签，避免牵动路径/引用）。

## 5. 覆盖性结论

- **完整性**：逐段对照 eFLP 全部正文句（含 §12-1 关于"力的定义/戈斯/椅子"的哲学段、§12-4 场论段、§12-5 赝力段），无漏句、无重复粘贴、无整段错位；英文段落与中文段落的 2 处切口差异均为插图插入或英文相邻两段合并。
- **数字**：1/10¹⁰（L19）、ε₀ 8.85×10⁻¹²（L85，见存疑 1）、1/4πε₀ 8.99×10⁹ N·m²·C⁻²（L89）、e=1.60×10⁻¹⁹ C（L96）、e²=(1.52×10⁻¹⁴)²（L96）、核力作用范围 10⁻¹³ cm（L216 三处）、100 g（L79）、180°（L162）、7 次方（L71）——除 ε₀ 有效数字外均与英文一致，无数字/量纲错误。
- **公式**：编号式 12.1–12.11 与 6 个无编号式逐一核对；发现并修正 L193 伽利略变换式；其余与英文一致（12.3/12.7/12.8/12.9 此前已由 `fix/equations` 修正，本次复核无误）。
- **图**：图 12.1–12.4 的编号、图注、正文 `\ref` 引用一一对应（编译渲染核验）；图 12.1 图注误译已改；未新增/删除图。
- **人名/术语**：乔、莫（Joe/Moe）、约翰逊（Johansson）、伽利略、爱因斯坦、牛顿、马达加斯加均正确；赝力、磁感应强度、叠加原理、偶极矩、极性/非极性分子、胡克定律、法向力、干摩擦/滑动摩擦、静摩擦/动摩擦、π介子、奇异粒子等术语与英文一致。
- **候选清单**：270 条小差异绝大多数为公开中译本自身的 OCR 错误（"厦力/赝力""流涡/漩涡""粘结/黏结""记往/记住"等）或数学式/单位写法差异，未据其改动；28 条大块差异均为参考文本的公式残片、页眉、图注噪声，仅借此确认 L193 一处我们自身的公式问题。本仓库中文 OCR 质量较高（此前已修去重复段与错误公式），未再发现单字讹变。

## 6. 验证

- 单章入口：**`preview/chapter-12/check.tex`**（由 `tools/make_chapter_check.py 12` 生成；`\setcounter{chapter}{11}`；`\input{../../Chapters/VolumeI/Chapter12.tex}`）。
- 编译：`xelatex -no-mktex=tfm -interaction=nonstopmode` 连编 2 遍 → **14 页，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**。
- 版式抽查（PDF 渲染）：图 12.1–12.4、公式 12.1–12.11、L193 修正式、图注、脚注均正常，无孤行/溢版。
- 未提交 git；仅改动 `Chapters/VolumeI/Chapter12.tex`（diff 7 行、CRLF 保持），新建 `preview/chapter-12/` 与本报告。
