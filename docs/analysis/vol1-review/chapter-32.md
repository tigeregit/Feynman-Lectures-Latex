# 第 32 章《辐射阻尼、光的散射》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter32.tex`（219 行；5 节 32-1～32-5：辐射电阻 / 能量辐射率 / 辐射阻尼 / 独立的辐射源 / 光的散射）
- 英文：`_attachments/build-feynman/audit/en/I_32.txt`（32–1～32–5，正文 L39–L413；抓取文本中公式被拆成 [math] 碎片）
- 旁证：`_attachments/reference/zh/Chapter32.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch32-candidates.md`（194 小块 + 41 大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 已知电磁学公式（Larmor 公式、辐射电阻、Q 值、Thomson 散射截面）逐式比对；官方网页本次未抓取（不需要）
- 单章入口：`python3 tools/make_chapter_check.py 32` 生成 `preview/chapter-32/check.tex`，并已修正注释章名（《辐射阻尼、光的散射》）与 `cd` 路径（chapter-32）

## 结果

- **已修正 6 条（14 处；高 1、中 5、低 0）**；**存疑 6 项**（未改）。
- 单章编译：**11 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍；5 条基线 warning）。
- 修改文件：`Chapters/VolumeI/Chapter32.tex`（14 增 / 16 删，**CRLF 保持**、末尾无换行）、`preview/chapter-32/check.tex`（仅注释）、本报告。未 commit，未动其他章。

## 高/中问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L14、L32、L108、L154 | **4 处跨章引用未定义**（label 分别在第 28、29、23 章）：单章编译渲染"（??）"，产生 4 条 undefined reference | "We saw the formula (28.3)" / "(29.1)" / "(Fig. 23–2)" / "From Eq. (23.8)" | 硬编码为"（28.3）""（29.1）""（图23.2）""（23.8）"，单章 0 undefined |
| 2 | L145–L152 | wrapfigure 32.2 插在句子中间："…现在要计 / 算的是…"被图拆成两段（旧 PDF 中"算的是…"独立成段且位置异常） | "…what we now have to calculate is how much light we see and why it is blue." | figure 环境移到"如果在原子所在处…"段首；句子合并为"现在要计算的是，我们看见多少光以及它为什么是蓝色的。" |
| 3 | L206–L213 | wrapfigure 32.3 插在词中间："因为反正对于这个问 / 题只要有一个概念就行了）"被图隔开 | "the effect of one atom on the other is not important; it is just to get the idea anyway" | figure 移到"最后，还有一个关于偏振的重要特性"段首（该段引用此图）；合并为"…因为反正对于这个问题只要有一个概念就行了）…" |
| 4 | L63、L68 | 数字小数点中间被插入空格："$1.518~8$""$1.602~06$""$8.987~48$"（渲染为"1.518 8"等） | "e … numerically equal to 1.5188×10−14 … qe=1.60206×10−19 … 1/4πϵ0=8.98748×109" | 1.5188 / 1.60206 / 8.98748（共 4 处） |
| 5 | L72 | 自然频率误作 $\omega'_0$（后文与英文均为 $\omega_0$） | "which has a natural frequency ω0" | $\omega_0$ |
| 6 | L95 | "叫**电子半径**"漏"经典"（英文为 classical electron radius） | "It has been given a name, the classical electron radius" | "叫经典电子半径" |

## 存疑项（未改）

1. L215 "呈**火红色**" ← "yellow-red"（黄红色）：底本/参考同作"火红色"，属译法选择，未改。
2. L83 "找出**辐射子**的$Q$" ← "the Q for a radiator"：底本/参考同作"辐射子"（通行译名"辐射体"），未改。
3. L72 "几百万**里**" ← "millions of miles"：按上下文应为"英里"，底本用"里"，未改。
4. L101/L106 "$Na$原子"（数学斜体 Na）← "sodium atom"：底本排版如此，未改（可考虑正体"Na"）。
5. L16 "被它自己的**鞋带**拉住了" ← "holds itself back by its bootstraps"：底本比喻直译，未改。
6. 图 32.1 的 wrapfigure 位于引用它的段落之前两段（"应用电场表示式（29.1）"段首）；编译版面正常（0 overfull），未移动。

## 覆盖性结论

- **段落/完整性**：5 节与英文 32–1～32–5 对应；逐句核对**无漏句、无漏段、无重复粘贴**；候选 41 条大块差异全部为公式剥离/图注错位/页眉噪声。
- **公式**（零改动，逐式核对）：32.1 $S=\varepsilon_0c\langle E^2\rangle$；32.2 辐射能流；32.3 $dA=2\pi r^2\sin\theta d\theta$；32.4、32.5 Larmor 公式 $P=q^2a'^2/(6\pi\varepsilon_0c^3)$；32.6 $P=q^2\omega^4x_0^2/(12\pi\varepsilon_0c^3)$；32.7 $e^2=q_e^2/(4\pi\varepsilon_0)$；32.8 $Q=-\omega W/(dW/dt)$；32.9 $W=\frac12m\omega^2x_0^2$；32.10 $1/Q=4\pi e^2/(3\lambda m_ec^2)$；32.11 $r_0=e^2/m_ec^2=2.82\times10^{-15}$ m；32.12 $Q\approx5\times10^7$；32.13 $\Delta\lambda=4\pi r_0/3=1.18\times10^{-14}$ m；32.14 $A_R^2=A_1^2+A_2^2+2A_1A_2\cos(\phi_1-\phi_2)$；32.15/32.16 受迫振子响应；32.17 散射功率三级等式；32.18 $P=(\frac12\varepsilon_0cE_0^2)\sigma$；32.19 $\sigma_s=\frac{8\pi r_0^2}{3}\cdot\frac{\omega^4}{(\omega^2-\omega_0^2)^2}$——**全部正确**。
- **数字/量纲**：377 Ω、1.5188×10⁻¹⁴、1.60206×10⁻¹⁹、8.98748×10⁹、2.82×10⁻¹⁵ m、6000 Å、5×10⁷、10⁸、10⁷、10¹⁵ Hz、10⁻⁸ s、1.18×10⁻¹⁴ m、7 000 000 000 个波长、10⁻¹⁵ m、10⁻³⁰ m²、90° 均与英文一致（小数点空格问题已修）。
- **图表**：3 幅图（32.1–32.3）齐全；图注与英文 Fig. 32–1～32–3 一致；正文图引用全部解析（0 undefined）；本章无表格。
- **自动候选差异**：194 小块 + 41 大块绝大多数为公式剥离噪声与参考 OCR 讹字（毋→性、末→本/未、弧→强、电→虫、另→男 等），**不据以改动**；确属本仓库的问题即上表 6 条。

## 验证

- 入口：`preview/chapter-32/check.tex`（`\setcounter{chapter}{31}`、`\input{../../Chapters/VolumeI/Chapter32.tex}`；注释章名/路径已改对）。
- 命令：`cd preview/chapter-32 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：11 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 文本抽查：修正点均生效（"（28.3）""（29.1）""图 23.2""（23.8）""1.5188""经典电子半径""自然频率为 ω0"；"现在要计算的是…蓝色的"与"…因为反正对于这个问题只要有一个概念就行了）…"均连续成句、无断段）；旧串（"??""1.518 8""ω0′""叫电子半径"）出现 0 次。
