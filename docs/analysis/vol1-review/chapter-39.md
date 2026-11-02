# 第 39 章《气体分子动理论》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter39.tex`（300 行；5 节 39-1～39-5：物质的性质 / 气体的压强 / 辐射的压缩性 / 温度和动能 / 理想气体定律；编号公式 39.1–39.24 共 24 个）
- 英文：`_attachments/build-feynman/audit/en/I_39.txt`（623 行；公式抓取为分式碎片，逐式按片段 + 上下文核对）；官方页 <https://www.feynmanlectures.caltech.edu/I_39.html> 用于核对关键句（"only half … n/2"、"r atoms / 3r"、"come out even"）
- 旁证：`_attachments/reference/zh/Chapter39.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch39-candidates.md`（254 小块 + 53 大块，已逐条判定）
- 公式核对方式：eFLP 文本片段逐式比对 + 编译后 PDF 渲染号核对

## 结果

- **已修正 7 条（8 处；高 1、中 4、低 2）**；**存疑 6 项**（未改）。
- 单章编译：**14 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。修改前基线编译有 1 处 Overfull vbox（1.36pt，第 10 页），修订后排版变化、已消失。
- 修改文件：`Chapters/VolumeI/Chapter39.tex`（7 行 8 处，**CRLF 保持原状**）；`preview/chapter-39/check.tex`（章名/路径注释 + 1 个跨章图引用桩）；本报告。未 commit，未动其他章。

## 高严重度（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L300 | 把分子中的原子数 $r$ 误作 **$\gamma$**（与绝热指数 $\gamma=5/3$ 冲突）："由$\gamma$个原子组成……自由度数是$3\gamma$……$3\gamma kT/2$……其余的$3(\gamma-1)kT/2$" | "The number of degrees of freedom of a molecule composed of **r atoms** is **3r** … the rest, **3(r−1)kT**, is internal vibrational and rotational kinetic energy." | 由$r$个原子组成……自由度数是$3r$……$3rkT/2$……其余的$3(r-1)kT/2$ |

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 2 | L74 | 因子 2 的解释被译错/替换为可疑说法："对正的$v_x$，$v_x^2$的平均值等于对所有$v_x$所求平均值的一半"（条件平均值其实相等；与 eFLP 说明不符） | "No; of all the atoms, only half are headed toward the piston. The other half are headed the other way, so the number of atoms per unit volume that are hitting the piston is only **n/2**." | "……只有一半是朝着活塞跑的，另一半朝着相反的方向运动。**所以每单位体积中撞向活塞的原子数只有$n/2$。**" |
| 3 | 式 39.21（L216–219） | 公式缺平均符号 ⟨⟩："$\frac{1}{2}m_1v_1^2=\frac{1}{2}m_2v_2^2$"（前文明明是"平均值"） | "⟨½m₁v₁²⟩=⟨½m₂v₂²⟩" | 两侧加 `\left\langle … \right\rangle` |
| 4 | 式 39.24（L266–269）及紧随的推导式（L276–279） | 两处缺平均符号 ⟨⟩："$\frac{1}{2}Mv_{CM}^2=\frac{3}{2}kT$"、aligned 左端同为瞬时量 | "⟨½Mv²_CM⟩=3/2 kT"；"we multiply ½M and take the average, and thus we get ⟨½Mv²_CM⟩=…" | 两处左端加 `\left\langle … \right\rangle` |
| 5 | L250 | "不选 **$10^24$** 个分子"——上标缺花括号，实际渲染为 $10^2 4$（错误数字） | "Why they did not choose **10²⁴** objects, so it would come out even…" | $10^{24}$ |

## 低严重度（已修）

- L250："这样的偶数"→"以使数目凑成整数"（英文 "so it would come out even" 是"凑成整数"，不是"偶数"）。
- 图 39-3 图注：只写"从质心系来看两个不同分子间的碰撞"，漏英文图注中 $u_1=|\boldsymbol{v}_1-\boldsymbol{v}_{CM}|$、$u_2=|\boldsymbol{v}_2-\boldsymbol{v}_{CM}|$ 的定义（图内正是标 $u_1$、$u_2$）；已补。

## 存疑项（未改）

1. **中译本 L74 处多出的解释句**（"如果我们取⟨v_x⟩，则对负的v_x平方的平均和对正的v_x平方的平均一样……两倍"）来自中译本，**eFLP 原文没有**；本次按 eFLP 改为 "n/2" 说明，未补入底本多出的句子。
2. **L198 图引用**：`图\ref{figure:球截形的侧面积为}` 指向第 32 章图 32.1（英文原文即 "see Fig. 32–1"），属跨章引用；正文保留 `\ref`，单章编译用 check.tex 引用桩（渲染"图32.1"），全书合编正常。
3. **L250 "8.317~J:"**：底本用 ASCII 冒号分隔数值与公式（英文为冒号），保留。
4. **温度单位**：英文脚注用 "∘K"，中译本用 "K"（273.15 K、J·mol⁻¹·K⁻¹），保留。
5. **L231 "m₂v₂²/2" 与 ½ 写法混用**：底本如此，语义正确，保留。
6. **L237 脚注**"摄氏温标与开尔文温标一样，但 0°C 选在 273.15 K"：与英文脚注一致（英文 273.15 ∘K），保留。

## 覆盖性结论

- **段落/完整性**：5 节与英文 39–1～39–5 逐段对应；无漏段、无漏句、无重复粘贴；无跨章公式引用（仅 1 处跨章**图**引用）。
- **公式**：24 个编号公式 39.1–39.24 全部存在，编译渲染号与 eFLP 编号一一对应。逐式核对：
  - 压强推导：39.1（$P=F/A$）、39.2（$dW=-PdV$）、39.3（$F=nv_xA\cdot2mv_x$）、39.4（$P=2nmv_x^2$）、39.5（$P=nm\langle v_x^2\rangle$）、39.6、39.7（$=\langle v^2\rangle/3$）、39.8（$P=\frac{2}{3}n\langle mv^2/2\rangle$）、39.9（$PV=N\frac{2}{3}\langle mv^2/2\rangle$）；
  - 内能与绝热：39.10（$PV=\frac{2}{3}U$）、39.11（$PV=(\gamma-1)U$）、39.12（$dU=(PdV+VdP)/(\gamma-1)$）、39.13、39.14（$PV^\gamma=C$）；
  - 辐射压：39.15（$P=2np_xv_x$）、39.16（$PV=\frac{N}{3}\langle\boldsymbol{p}\cdot\boldsymbol{v}\rangle$）、39.17（$PV=U/3$）、39.18（$PV^{4/3}=C$）；
  - 能量均分与气体定律：39.19、39.20、39.21、39.22（$PV=NkT$）、39.23（$PV=NRT$）、39.24（⟨½Mv²_CM⟩=3/2 kT）。
  **系数、符号、上下标与 eFLP 一致**；仅上表第 1、3、4、5 条符号/排版问题已修。
- **数字/常数**：$k=1.38\times10^{-23}$ J/K、$N_0=6.02\times10^{23}$、$R=8.317$ J·mol⁻¹·K⁻¹、273.15 K、$10^{24}$、$\gamma=5/3$（单原子）、$\gamma=4/3$（光子气）、$3kT/2$、$kT/2$ 等均与 eFLP 一致；"8.317 J: R=N₀k=8.317 J·mol⁻¹·K⁻¹" 数值正确。
- **图/表**：4 幅图（39.1–39.4）齐全，图注与英文一致（图 39-3 已补 $u_1,u_2$ 定义）；本章无表格；图引用 4 处本地 `\ref` + 1 处跨章引用均解析（0 未定义）。
- **术语**：分子动理论、压强、绝热、辐射压强、自由度、能量均分、摩尔、阿伏伽德罗常数、理想气体定律等与英文一致。
- **自动候选差异**：254 小块 + 53 大块绝大多数为参考文本 OCR 讹字（四→匹、具→且、另→男、撇→撒 等）与公式剥离噪声，**不据以改动**；确属本仓库的问题即上表/低严重度共 7 条。

## 验证

- 入口：`preview/chapter-39/check.tex`（`\setcounter{chapter}{38}`、`\input{../../Chapters/VolumeI/Chapter39.tex}`；本次修正注释章名《气体分子动理论》、`cd` 路径 chapter-39、验收标准行，并加 1 个跨章图引用桩）。
- 命令：`cd preview/chapter-39 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：14 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 文本抽查：修正点均生效（"所以每单位体积中撞向活塞的原子数只有 n/2""由 r 个原子组成……3r""3rkT/2""3(r−1)kT/2""10²⁴ 个物体""图32.1"；图 39-3 图注含 $u_1,u_2$ 定义）。

## 未改动与建议

- 存疑 1–6 建议保持；其中跨章图引用（第 32 章图 32.1）如全书面统一为图号硬编码或改用 \ref 由 Lead 决定。
- 修改集中在 7 行（7+/7−，其中第 4、1 条各含 2 处替换），便于复核 diff。
