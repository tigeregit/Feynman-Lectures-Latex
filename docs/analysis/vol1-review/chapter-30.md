# 第 30 章《衍射》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter30.tex`（310 行；7 节 30-1～30-7，正文约 40 段）
- 英文：`_attachments/build-feynman/audit/en/I_30.txt`（30–1～30–7；抓取文本中公式为分式/碎片）
- 旁证：`_attachments/reference/zh/Chapter30.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch30-candidates.md`（385 小块 + 47 大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 参考中译本 OCR 逐式比对；12 幅图逐幅渲染核对图注/内容

## 结果

- **已修正 13 条（14 处；中 3、低 8、结构 2）**；**存疑 3 项**（未改）。
- 单章编译：**15 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter30.tex`（13 行，**CRLF 换行保持原状**）、`preview/chapter-30/check.tex`（仅注释：章名改《衍射》、`cd` 路径改 chapter-30）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L57 | 强度系数排版致语义错：`$I=4n^2I_0/9 \pi^2$`、`$4/9 \pi^2$` 渲染为 (4/9)π²，与紧随的"0.045 倍/不到 5%"矛盾 | "I=I0(4n2/9π2)"；"4/9π2 times the maximum intensity, which is about 0.045" | `$I=4n^2I_0/(9\pi^2)$`、`$4/(9\pi^2)$` |
| 2 | L108 | m=0 为唯一解的间距条件漏 /2：中文作"$d$小于$\lambda$"（λ/2<d<λ 时 m=±1 亦可解） | "corresponds to m=0, where d is less than λ/2; in fact, this is the only solution" | 其中$d$小于$\lambda/2$ |
| 3 | L122 | 同上：连续极限所对照的有限间隔条件 | "the same general kind of a picture as for finite spacing with d<λ/2" | 与有限间隔$d<\lambda/2$同样类型的图 |

## 低严重度修正（已修）

- L5："衍射**．**至今"（全角句点"．"）→ "衍射。至今"（标点）
- L94："（图30-4）"**硬编码图号** → `图\ref{figure:从光栅上相邻划线散射的光线的程差是}`（与正文其余 `\ref` 一致）
- L143：**图 30–6 缺正文引用**（该图 label 原为孤儿）→ 补"（图\ref{figure:瑞利判据的说明。一个花样的极大值落在另一个花样的第一极小值上}）"（英文 "called Rayleigh's criterion, is usually used (Fig. 30–6)"）
- L160："故长为**L**的天线装置" → 长为 `$L$`（数学体缺失）
- L203："如果要求出**P**点的强度" → `$P$`点（数学体缺失）
- L234："仅取决于距离**r**" → `$r$`（数学体缺失）
- L236："单位面积电荷数**η**的乘积" → `$\eta$`（数学体缺失）
- L310："对任意距离**z**都正确" → `$z$`（数学体缺失）

## 结构类（单章编译需要，见说明）

- L34："与式（`\ref{Eq:I:29:12}`）一致" → 硬编码"式（29.12）"（**跨章**引用第 29 章式 29.12，单章编译无法解析；全书编号仍为 29.12）
- L162："（`\ref{figure:抛物面镜}`）" → 硬编码"（图26.12）"（**跨章**引用第 26 章图 26–12，`label` 在 `Chapter26.tex`；全书编号为 26.12）

## 存疑项（未改）

1. **L106–110 直射/反射与"补角"**：eFLP 原句措辞含混（"θout is the supplement of θin so the light comes out in the same direction …"），中文按物理正确的对应表述（θout=θin 为沿原方向的新光束；补角解为反射光束）；疑英文抓取句有 OCR/原书互换，底本同，未改。
2. **L220 "XY面"**：英文 "xy-plane"；底本作大写 XY，未改（记法习惯）。
3. **式(30.8) 排版**：`$I=4I_m\sin^2\frac{1}{2}\varPhi/\varPhi^2$`（sin²½Φ/Φ²）与 eFLP 印刷式一致，未改（如需更清晰可加括号）。

## 覆盖性结论

- **段落/完整性**：7 节与英文 30–1～30–7 对应；逐句核对无漏句、无漏段、无重复粘贴；候选"大块差异"47 条全部是公式被剥离/图注错位噪声。
- **公式**：编号公式 30.1–30.19 全部存在并逐式与英文核对一致（30.1–30.3 振幅求和/强度；30.4–30.7 相位差与光栅方程；30.8 连续极限；30.9 分辨本领；30.10–30.19 平面源场）；已修正 L57 系数排版与 L108/L122 的 λ/2。
- **数字**：4/(9π²)≈0.045、1.22、3π/2、3π/2n、mn、2π 等均核对无误；无其他数字错误。
- **图表**：12 幅（30.1–30.12）全部存在，修改后均被正文 `\ref` 引用；图注与英文一致；图 30–6 补引用、图 30–4 硬编码改 `\ref`；图 26–12 跨章引用硬编码。
- **术语**：衍射光栅、分辨本领、瑞利判据、倒易原理、考纽蜷线（Cornu spiral）、振幅矢量和等与英文一致；无术语误译。

## 验证

- 入口：`preview/chapter-30/check.tex`（`\setcounter{chapter}{29}`、`\input{../../Chapters/VolumeI/Chapter30.tex}`；本次仅改注释）。
- 命令：`cd preview/chapter-30 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：15 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 文本抽查：修正点均生效（"衍射。""式（29.12）""I = 4n²I₀/(9π²)""d 小于 λ/2""（图30.6）""（图26.12）""长为 L""P 点的强度""距离 r""电荷数 η""距离 z"）；旧串（"衍射．""（图30-4）""4/9 π²""$d$小于$\lambda$"等）出现 0 次。

## 未改动项与建议

- 为单章编译将 2 处跨章引用硬编码（式29.12、图26.12）；若上游统一改用 `\ref`，可恢复 `\ref{Eq:I:29:12}` 与 `\ref{figure:抛物面镜}`（全书编译时均能解析）。
- 存疑 3 项未改。
