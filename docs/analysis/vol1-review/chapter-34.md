# 第 34 章《辐射中的相对论性效应》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter34.tex`（354 行；9 节 34-1～34-9；13 图；27 个编号公式）
- 英文：`_attachments/build-feynman/audit/en/I_34.txt`（34–1～34–9，正文 L36–L381；抓取文本中公式为分式碎片，已按上下文逐式还原核对）
- 旁证：`_attachments/reference/zh/Chapter34.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch34-candidates.md`（354 小块 + 51 大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 中文正文逐式比对（重点：34.9/34.10–34.14 多普勒、34.15–34.18 洛伦兹变换与四元矢量、34.19–34.21 波矢、34.22–34.23 光行差、34.24–34.27 光的动量）

## 结果

- **已修正 12 条（中 3、低 9）**；**存疑 6 项**（未改）。
- 单章编译：**15 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter34.tex`（12 行，**CRLF 换行保持原状**）、`preview/chapter-34/check.tex`（`make_chapter_check.py 34` 生成，仅改注释：章名《辐射中的相对论性效应》、`cd` 路径 chapter-34）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L126 | 术语前后不一致：第一处作"短幅摆线"（L73，正确），第二处作"**内摆线**"（hypocycloid，另一曲线） | "the cusps of the curtate cycloid are enormously sharp compared with the distance between them" | "短幅摆线" |
| 2 | L128 | 否定答句译反："我们会从任何一种'脉冲'**得不到光吗？会的**"——与下文（平坦脉冲不产生光）及英文相反 | "will we not get light from any kind of a 'pulse'? No." | "从任何一种'脉冲'都能得到光吗？不能。" |
| 3 | L261 | 四元矢量类比的下标错位："把$\omega$设想为**$t'$**，把$k$设想为**$x'$**除以$c^2$"（应为不带撇，旧的对应旧的、新的对应新的） | "if ω is thought of as being like t, and k is thought of as being like x divided by c2, then the new ω′ will be like t′…" | "把$\omega$设想为$t$，把$k$设想为$x$除以$c^2$" |

## 低严重度修正（已修）

- L44："这段时间即光**必需**走过的总距离" → "**必须**"（必需/必须误用，英文 "the total distance that the light has to go"）。
- L59："这仅仅意味着**时间t**的原点改变一个常量" → "时间**$t$**"（数学体缺失；同段其余 t 均为 `$t$`）。
- L64："我们就得到了$x'$（和$y'$）与**t**关系的曲线图" → "与**$t$**"（同上）。
- L184："电子正以速率**v**朝着我们运动" → "速率**$v$**"（数学体缺失）。
- L195："整个振子以速度**v**沿着趋向观察者的方向运动" → "速度**$v$**"（数学体缺失）。
- L215："必须把结果除以$\sqrt{1-v^2/c^2}$**因而**，若…" → 补句号"…$c^2}$**。**因而，若…"（英文此处为句末 "…divide by √(1−v²/c²). So if…"）。
- L325："再设电场沿$x$方向**运动**，故电荷也沿$x$方向运动" → 删"运动"（英文 "the electric field is in the x-direction"；"运动"的是电荷，不是场）。
- L86：跨章引用"根据式（**\ref{Eq:I:28:2}**）" → 硬编码"（**28.2**）"（单章编译所需；全书编号不变）。
- L228：脚注"与式（**\ref{Eq:I:16:2}**）不同" → 硬编码"（**16.2**）"（同上）。

## 存疑项（未改）

1. **L158"他们知道地球以外的宇宙万物"** ← "they were conscious of the external universe"：底本即如此，"知道……宇宙万物"语义略宽（宜作"关注/了解外部宇宙"），未改。
2. **L184"同步加速器用作产生高能电子，没有用作产生高能光子的多"** ← "the synchrotron is used, not so much to make high-energy electrons … as to make very energetic photons"：底本句式（"没有……的多"）可读，未改。
3. **L248"即每$2\pi$米所含的波的数目"** ← "the number of waves per meter"：英文表述本身不严谨（$k=2\pi/\lambda$），中文按物理正确的"每 $2\pi$ 米"译出，未改。
4. **L327"现来决定辐射压力的大小"** ← "Let us determine how strong the radiation pressure is"：底本"现来"疑漏"在"（现在来），语义无碍，未改。
5. **L355 波的能量用$\mathcal{E}$（英文作 E）**：沿用第 33 章符号（该章用 `\mathcal{E}` 表示波的能量），未改。
6. **式（34.24）功的记号用$dw/dt$（英文$dW/dt$）**：中文以 $w$ 表示功、$W$ 表示能量，底本即如此（参考文本亦作 dw/dt），未改。

## 覆盖性结论

- **结构**：9 节与英文 34–1…34–9 一一对应；逐段核对无漏段、无漏句、无重复粘贴。
- **公式**：27 个编号式（34.1–34.27）及若干无编号式逐式核对，未发现公式错误，**公式内一律未改**；重点核对通过——洛伦兹变换及其逆（34.15）、相位不变式与 ω′/k′（34.16–34.18）、波矢与 $\sum'k_\mu x_\mu$（34.19–34.21）、光行差（34.22–34.23）、光压与光子动量（34.24–34.27）。
- **图**：13 张图与 Fig. 34–1…34–13 一一对应，图文件齐备，图注逐条核对无误。
- **数字**：0.511×10⁶ eV、3×10⁸、10⁴ Gs、1.5×10⁴ Gs、10⁵ Gs、3.3 m、3.7 m、20 m、1.5 GeV、10⁹ eV、8×10⁶、64×10¹²、(1/64)×10⁻¹²、3/2 次方、v=0.94c、1054 年、900 年等均与英文一致。
- **人名/术语**：洛伦兹变换、多普勒效应、同步辐射、轫致辐射、光行差、四元矢量、德布罗意关系、光压等术语无误。
- **跨章引用**：`Eq:I:28:2`、`Eq:I:16:2` 两处硬编码为"28.2""16.2"（保证单章编译 0 undefined ref；对应标签在 Chapter28 L26、Chapter16 L51 存在，全书渲染编号不变，属预期处理）；文字性"第28章/第16章/第17章/上一章"保留。
- **旁证**：参考文本自身 OCR 讹误（如"内摆线""轫/韧""引力/磁力"混用等）未采纳，均以 eFLP 英文为准。

## 验证

- **单章编译**：`preview/chapter-34/check.tex`（章号 33 + input Chapter34，含 readability 版式层）连编 2 遍：**0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references，15 页**（与修改前一致）。
- **核对方式**：逐行 `git diff` 核对（仅 12 行变化）；渲染 PDF 抽查全部 12 处修正均正确显示（含"短幅摆线"两处、式（28.2）/（16.2）、"都能得到光吗？不能"、"如果把 ω 设想为 t…"等）。

## 未改动项与建议

- 存疑 6 项保持底本原貌；未改其他章、未 commit、未运行全书编译。
