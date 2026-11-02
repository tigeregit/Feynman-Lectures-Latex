# 第 29 章《干涉》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter29.tex`（原 242 行；5 节 29-1～29-5：电磁波 / 辐射的能量 / 正弦波 / 两个偶极辐射子 / 干涉的数学）
- 英文：`_attachments/build-feynman/audit/en/I_29.txt`（29–1～29–5，正文 L36–L266；抓取文本中公式为分式碎片）
- 旁证：`_attachments/reference/zh/Chapter29.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch29-candidates.md`（205 小块 + 43 大块，已逐类核对）
- 辅助核对：1963 初版影印页（archive.org FLP Vol. I PDF p.650）核对"U/ψ"符号与图 29–10；官方网页 <https://www.feynmanlectures.caltech.edu/I_29.html> 经文本代理核对图注与 (29.1) 链接目标
- 公式核对方式：eFLP 文本片段 + 1963 初版印刷页 + 中译本 OCR 旁证逐式比对

## 结果

- **已修正 13 项（对应 17 处替换/移动操作：4 处图移动各含删除+插入、1 处补译整段、8 处文字替换）；高 1、中 7、低 5**；**存疑 7 项**（未改）。
- 单章编译：**10 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter29.tex`（+17/−15 行，**CRLF 换行保持原状**）、`preview/chapter-29/check.tex`（仅注释：章名改《干涉》、`cd` 路径改 chapter-29；另为跨章 `Eq:I:28:6` 加幻影标签占位）、本报告。未 commit，未动其他章。

## 高严重度（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L139–L141 之间 | **整段漏译**：英文 L128 一整段（"Thus, by using some cleverness in spacing and phasing our antennas… Here the picture is quite different."，约 90 词）在本仓库中缺失；公开中译本有该段（"这样，在天线的排列与相位配置上作一些巧妙的安排……此时图像就大不相同了。"），属本仓库漏抄 | "Thus, by using some cleverness in spacing and phasing our antennas, we can send the power all in one direction. … Let us take a situation in which the separation is ten wavelengths (Fig. 29–7) … Here the picture is quite different." | 在图 29-6/29-7 之后、L141 段之前补入整段译文（据底本 OCR 复原，衔接上下文） |

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 2 | L5–L12 | 图 29-1 的 wrapfigure 插在句子中间："…我们已定性说明在两个源〡（图）〡的辐射场中有极大与极小存在…" | 英文 Fig. 29–1 位于首段之后、"We have already physically analyzed…" 段之前 | 图移至首段之后，合并"…两个源的辐射场中…" |
| 3 | L56–L63 | 图 29-4 的 wrapfigure 插在句中："…正如我们以前所〡（图）〡提及的。…" | 英文 Fig. 29–4 位于 "First of all…" 段之后、"This means that the energy…" 段之前 | 图移至该段之后，合并"…所提及的。…" |
| 4 | L109–L116 | 图 29-5 的 wrapfigure 插在句中："…现在我们想知道在不同方向上的辐〡（图）〡射强度。…" | 英文 Fig. 29–5 位于 "Figure 29–5(a) represents…" 段之前 | 图移至该段之前，合并"…辐射强度。…" |
| 5 | L183–L190 | 图 29-9 的 wrapfigure 插在句中："…因而它与水平〡（图）〡轴的夹角为 ωt+φ₁…" | 英文 Fig. 29–9 位于 "Now suppose that we cannot remember…" 段之前 | 图移至该段之前，合并"…水平轴的夹角…" |
| 6 | L232 | "注意这不是出现在**图（图29.1）**中的同一个 θ"——双重"图"字，且英文指**式(29.1)**（eFLP 该处超链接目标为 mjx-eqn-EqI291） | "Note that this is *not* the same θ as appears in (29.1)." | "注意这不是出现在**式（\ref{Eq:I:29:1}）**中的同一个 θ" |
| 7 | L232 | "用一个像 **ψ** 那样不常用的符号"——原文符号为 **U**（1963 初版 p.650 印刷页与 eFLP 均为 U） | "We are torn between using an unconventional symbol like U or the conventional symbol θ (Fig. 29–10)." | "用一个像 **$U$** 那样不常用的符号" |
| 8 | L113 | 图 29-5 图注"来自**相聚**半个波长的两个偶极振子"——量词误作"聚"（正文均作"相距"） | "The intensities in various directions from two dipole oscillators one-half wavelength apart." | "来自**相距**半个波长的两个偶极振子…" |

## 低严重度修正（已修）

- L136 图 29-7 图注："两个**相聚**$10\lambda$的偶极子" → "两个**相距** $10\lambda$ 的偶极子"（与图注/正文用语统一）。
- L192："写出一些能表达与**图29-9**同样意义的东西" → 硬编码图号（连字符体例与渲染"图 29.9"不一致）→ `图\ref{figure:合成两个余弦波的几何方法}`。
- L239："例如，**图29-5**中在 $30^\circ$ 方向上的强度为 2" → `图\ref{figure:来自相聚半个波长的两个偶极振子的场在不同方向上的强度}`。
- L73："即固定**t**而观察波作为距离 r 的函数" → 裸变量入数学模式：`固定$t$`。
- L118："但一个振子振动的相位**α**比另一个落后半个周相" → 裸希腊字母入数学模式：`相位$\alpha$`。

## 存疑项（未改）

1. **L155/L159 分段**：英文 L147 一段（"…the sum R of two waves: R=… How do we do it?"）在中文里被显示公式分成 L155 与 L159（"怎样求呢？"）两段，属底本分段体例，未重排（无漏句）。
2. **L176/L181 分段**：英文 L180 段（"…the resultant amplitude is A_R=…, and the resultant phase is…"）在中文里被式(29.12)分成"合成振幅为"与"而合成相位为…"两段，底本分段，未重排。
3. **图 29-8 位置**：英文图 29–8 在"六根天线"段之后、"其理由是…"段之前；中文图置于"六根天线"段之前（段首），属浮动体位置差异，未造成断句，未动。
4. **图 29-6 画面**：本仓库所附图仅含 4/2/0、α=π/2 的强度分布图（疑为底本插图裁剪），与图注"一对偶极子天线"的文字略有出入；内容不误，未动。
5. **跨章文字引用**："第31章"（L116）、"第32章"（L65）、"第28章"（L141）为硬编码章号（项目无章 label），保留。
6. **中文方括号"［…］"**（L232 夹注）：底本体例，保留。
7. **L159 "怎样求呢？"**：独立成段过短（见存疑 1），属底本分段；未并段。

## 覆盖性结论

- **段落/完整性**：5 节与英文 29–1～29–5 对应；逐句核对**补上遗漏整段后无漏句、无漏段、无重复粘贴**；中文段落因"按句/按公式分段"体例多于英文（约 39 段 vs 英文约 35 段），属底本体例。
- **公式**：17 个编号公式 **29.1–29.17 全部存在**，且逐式与英文一致：29.1（$E=-qa(t-r/c)\sin\theta/4\pi\epsilon_0c^2r$）、29.2、29.3、29.4（$|\partial\phi/\partial r|=k=\omega/c$）、29.5–29.8（$\lambda=ct_0$、$\omega=ck$、$\lambda\nu=c$、$\omega\lambda=2\pi c$）、29.9–29.12（余弦和差公式与合成振幅）、29.13–29.16（复数法与 $A_R^2=A_1^2+A_2^2+2A_1A_2\cos(\phi_2-\phi_1)$）、29.17（$\phi_2-\phi_1=\alpha+2\pi d\sin\theta/\lambda$）；无编号公式（$\cos(A+B)$ 展开、$A=a\cos\Delta$、$B=-a\sin\Delta$、$e^{i\theta}+e^{-i\theta}=2\cos\theta$、$2\pi\lambda/4\lambda=\pi/2$）亦一致。**本次未改动任何公式内容**。
- **数字/物理结论**：强度 4/2/0、$36=6^2$、$\lambda/4$、$\lambda/2$、$10\lambda$、$2.5\lambda$、$30^\circ$、$90^\circ$、$180^\circ$、$360^\circ$、$d\sin\theta=\lambda/4\Rightarrow\phi_2-\phi_1=\pi/2$ 等均与英文一致；强度∝场平方、干涉项、相长/相消干涉、波区 $\lambda/r$ 量级等结论正确。
- **图**：10 幅图（29.1–29.10）齐全，图注与英文逐条一致（两处"相聚"已改为"相距"）；图 29-9/29-5 的硬编码引用已改 `\ref`，全部图/式引用解析（0 未定义）。
- **表**：本章无表。
- **自动候选差异**：205 小块 + 43 大块绝大多数为参考文本 OCR 噪声（公式与上下标剥离、"另→男、弧→强、答→管、轭→轿、矢→天/拓、栅→机"等），判"参考误"未采纳；确属本仓库的问题即上表/低严重度 13 项，其中唯一大块真实差异是**漏译整段**（已补，见高严重度 1）。

## 验证

- 入口：`preview/chapter-29/check.tex`（`\setcounter{chapter}{28}`、`\input{../../Chapters/VolumeI/Chapter29.tex}`；本次仅修正注释，并为跨章的式 (28.6) 加幻影标签占位）。
- 命令：`cd preview/chapter-29 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：10 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；PDF 中无 `??`。
- PDF 文本抽查：修正点均生效（"巧妙的安排…此时图像就大不相同了"整段在位、"式（28.6）"、"出现在式（29.1）"、"像 U 那样"、"两个相距 10λ"、"图 29.4/29.5/29.9"）；旧串（"图29-9""图29-5""$\psi$""相位α""固定t"）出现 0 次。
