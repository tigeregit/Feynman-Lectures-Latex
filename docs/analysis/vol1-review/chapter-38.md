# 第 38 章《波动观点与粒子观点的关系》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter38.tex`（246 行；6 节 38-1～38-6，正文约 35 段）
- 英文：`_attachments/build-feynman/audit/en/I_38.txt`（38–1～38–6；抓取文本中公式为分式碎片）
- 旁证：`_attachments/reference/zh/Chapter38.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch38-candidates.md`（已逐类核对）
- 公式核对方式：eFLP 文本片段 + 参考中译本 OCR 逐式比对；9 幅图逐幅核对图注/内容

## 结果

- **已修正 11 处（9 条：中 5、低 4）**；**存疑 3 项**（未改）。
- 单章编译：**13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter38.tex`（9 行，**CRLF 换行保持原状**）、`preview/chapter-38/check.tex`（仅注释：章名改《波动观点与粒子观点的关系》、`cd` 路径改 chapter-38）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L43 | 缺 eFLP 脚注（对 ±B 的精化说明 ±B/2，整条漏译） | "More precisely, the error in our knowledge of y is ±B/2. But we are now only interested in the general idea…" | 补 `\footnote{更精确地说，我们对$y$的位置知识的误差为$\pm B/2$。但眼下我们只关心基本概念，因此不必去管因子$2$。}` |
| 2 | L52 | 公式 `$h/2\Delta y$` 有歧义（易读作 (h/2)Δy） | "the uncertainty in the vertical momentum must exceed ℏ/2Δy" | $h/(2\Delta y)$ |
| 3 | L90 | "$\omega$ 是每秒的**振动数**"（ω 为角频率，应为弧度/秒） | "ω is the number of radians per second" | $\omega$ 是每秒的**弧度数** |
| 4 | L167 | 三处把 ℏ 写成 h，与紧随的式(38.10)的 $\hbar^2$ 及"约化普朗克常数"自相矛盾 | "the spread in momentum is roughly ℏ/a … $p\approx\hbar/a$ … $\hbar2/2ma2$" | $h/a$、$p\approx h/a$、$h^2/(2ma^2)$ → $\hbar$ 版（3 处） |
| 5 | L180 | 玻尔半径数值错：0.528 Å（英文与物理值均为 0.529 Å；式 38.12 两处） | "a0=ℏ2/me2 =0.529 angstrom, =0.529×10−10 meter" | 0.529（2 处） |

## 低严重度修正（已修）

- L45："（图38-2的$C$处）"**硬编码图号** → `图\ref{figure:粒子穿过狭缝的衍射}`（图中引用统一）
- L47："就与y的不确定量成反比" → `$y$`（数学体缺失）
- L117："CaCO3的图案" → `CaCO$_3$`（化学式下标）
- L182："波尔半径" → **玻尔半径**（Bohr；本书其他章一律作"玻尔"）

## 存疑项（未改）

1. **Eq (38.3) 与 L52 的 h/ℏ**：eFLP（2013）作 ΔyΔp_y≥ℏ/2、L52 作 "ℏ/2Δy"；中文（两版中译本均）沿 1963 旧版作 ≈h、h/(2Δy)（与上文 p₀λ=h 的量级论证一致）。属旧版写法差异，未改（本报告只把 L52 的括号歧义修成 h/(2Δy)）。
2. **图 38-5/38-6 图注为空**：eFLP 图注有说明文字（"The pattern produced by the diffraction … sodium chloride"；"The x-ray diffraction pattern of myoglobin"），中文底本仅编号（空 `\caption`）；正文 L121 已说明两图内容。未补，建议上游决定。
3. **L115 "我们不能取两个相距五层的平面再应用这个公式！"**：eFLP "we cannot take a plane five layers farther back and use this formula"（取隔五层的平面作参考面）；底本同，仅标注。

## 覆盖性结论

- **段落/完整性**：6 节与英文 38–1～38–6 对应；逐句核对无漏句、无漏段、无重复粘贴；候选差异绝大多数为公式剥离/参考文本 OCR 噪声。
- **公式**：编号公式 38.1–38.17 全部存在并逐式与英文一致（$E=\hbar\omega$、$p=\hbar k$、$\Delta y\Delta p_y\approx h$、光栅 $\Delta\lambda/\lambda=1/Nm$、$\Delta k=2\pi/L$、$\Delta\omega=2\pi/T$、$2d\sin\theta=n\lambda$、$E=\hbar^2/2ma^2-e^2/a$、$a_0=\hbar^2/me^2$、$E_0=-13.6$ eV、能级差公式与里兹组合原则）；已修正 L52 括号、L167 h→ℏ、L180 0.528→0.529。
- **数字**：0.529 Å / 0.529×10⁻¹⁰ m、13.6 eV、±B、B/2、λ/2、2π 等核对无误；无其他数字错误。
- **图**：9 幅（38.1–38.9）全部存在且被正文引用（修改后无硬编码图号）；图注与英文一致（38-5/38-6 见存疑 2）。
- **术语**：概率波幅、波列、波数、衍射光栅、分辨本领、晶胞/点阵、玻尔半径、里德伯能量、里兹组合原则、波粒二象性等与英文一致。

## 验证

- 入口：`preview/chapter-38/check.tex`（`\setcounter{chapter}{37}`、`\input{../../Chapters/VolumeI/Chapter38.tex}`；本次仅改注释）。
- 命令：`cd preview/chapter-38 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：13 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 抽查：修正点均生效（脚注"更精确地说…±B/2"、"图38.2的 C 处"、"$y$ 的不确定量"、"h/(2Δy)"、"ω 是每秒的弧度数"、CaCO₃、ℏ/a、ℏ²/(2ma²)、0.529 Å、"玻尔半径"）；旧串（"图38-2"、h/a、0.528、"波尔半径"）出现 0 次。

## 未改动项与建议

- 存疑 3 项未改；若上游要求与 eFLP 2013 完全一致，可把 Eq (38.3) 改为 ΔyΔp_y≥ℏ/2、L52 改为 ℏ/(2Δy)，并补 38-5/38-6 图注。
