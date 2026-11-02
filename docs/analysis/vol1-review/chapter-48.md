# 第 48 章《拍》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter48.tex`（原 298 行 → 修改后 296 行；7 节 48-1～48-7：两列波的相加 / 拍音和调制 / 旁频带 / 定域波列 / 粒子的概率幅 / 三维空间的波 / 简正模式）
- 英文：`_attachments/build-feynman/audit/en/I_48.txt`（48–1～48–7，正文 L36–L400；抓取文本中公式为 [math] 碎片；章末脚注为"曲线可表示成许多余弦之和"的说明）
- 旁证：`_attachments/reference/zh/Chapter48.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch48-candidates.md`（230 小块 + 47 大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 已知波动/相对论公式（和差化积、拍频、群速度、德布罗意关系、克莱因-戈尔登方程）逐式比对
- **行尾**：本章为 LF（第 44–52 章均如此），已核对修改后仍为 LF（bytes 38991→39125，CRLF=0，末尾无换行），**未转 CRLF**
- 单章入口：`python3 tools/make_chapter_check.py 48` 生成 `preview/chapter-48/check.tex`，并修正注释章名（《拍》）与 `cd` 路径（chapter-48）

## 结果

- **已修正 8 条（11 处；高 1、中 4、低 3）**；**存疑 6 项**（未改）。
- 单章编译：**13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍；因移动 wrapfigure 后再补跑第 3 遍，label 稳定提示消失）。
- 修改文件：`Chapters/VolumeI/Chapter48.tex`（8 增 / 11 删，**LF 保持**、末尾无换行）、`preview/chapter-48/check.tex`（仅注释）、本报告。未 commit，未动其他章。
- **本章无跨章引用**（所有 `\ref` 均指向本章公式/图；"第31章"为纯文本叙述；基线编译 0 undefined）。

## 高/中问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L222 | **引用错误**："[它与**式（48.1）**表示的波不完全一样]"——应指图 48.1（两列余弦波叠加图），`\ref` 却指向方程 (48.1)（$e^{i(a+b)}$），读者会看错对象 | "(It is not quite the same as a wave like Fig. 48–1, which has a series of maxima…)" | 改为"它与图\ref{figure:频率比为8-10…}表示的波不完全一样" |
| 2 | L67 | 节标题术语错："**拍符**和调制"（beat notes 误作"拍符"） | "48–2 Beat notes and modulation" | "拍音和调制"（参考/底本亦作"拍符"，为 OCR/底本误） |
| 3 | L99–L107 | wrapfigure 48-4（调制载波）插在句中："将“消息” / [图] / 发送出去…"被拆成两段 | "The way the 'information' is transmitted… is that when somebody talks into a microphone…" | 图移到"我们举一个数学处理上最简单的例子…"段首（该段引用图 48.4）；合并为"将“消息”发送出去…" |
| 4 | L127 | wrapfigure 48-5（频谱）插在词中间："一个是载 / [图] / 频加上调频" | "One is the carrier frequency plus the modulation frequency, and the other is…" | 图移到"所以，从另一个观点来看…"段首；合并为"一个是载频加上调频，另一个是载频减去调频" |
| 5 | L222 | wrapfigure 48-6（定域波列）插在词中间："如果这个相对概率是常 / [图] / 数，那就意味着…" | "This is a constant, which means that the probability is the same…" | 图移到"这里$\omega$是频率…"段首；合并为"如果这个相对概率是常数，那就意味着…" |

## 低严重度修正（已修）

- L56："但这是不是人们所听到的拍频呢**。**" → "…呢**？**"（英文为疑问句 "But is this the frequency at which the beats are heard?"）。
- L7："来回改变该波在**P 点**的相位" → "在**$P$**点的相位"（同段其余 $P$ 均为数学体，仅此一处缺失）。
- L135："第一个发送频道是**频道2~(!)**" → "频道2（！）"（中文全角标点；英文 "channel 2 (!)"）。

## 存疑项（未改）

1. "拍符"在公开中译本参考中亦作"拍符"（底本/OCR 同误）；本次按英文改"拍音"，若 Lead 认为应保留底本可回退。
2. 底本译名保留：**旁频带**（通译"边带"）、**定域波列**（通译"波包"）、**概率幅**、**简正模式**、**律音**（note）——未改。
3. L297 '"900.5"周 / "900"周' ← 英文 '"900½" oscillations / "900"'：数值等价（900.5=900½），底本写法，未改。
4. 式（48.15）的 `aligned` 写法（`e&^{…}`）虽非常规，但渲染正常（两行、`=` 对齐），未改公式。
5. 图注"频率比为8:10"与 label 内"8-10"并存（冒号/连字符），不影响渲染，未改 label。
6. L99 "调幅 （AM）"等处中英文间多余空格，属排版细节，未改。

## 覆盖性结论

- **段落/完整性**：7 节与英文 48–1～48–7 对应；逐句核对**无漏句、无漏段、无重复粘贴**；候选 47 条大块差异全部为公式剥离/图注错位噪声。
- **公式**（零改动，逐式核对）：48.1–48.5 和差化积链；48.6 $\cos\omega_1t+\cos\omega_2t=2\cos\frac12(\omega_1+\omega_2)t\cos\frac12(\omega_1-\omega_2)t$；48.7 复指数形式；48.8 $I=A_1^2+A_2^2+2A_1A_2\cos(\omega_1-\omega_2)t$；48.9 $S=(1+b\cos\omega_mt)\cos\omega_ct$；48.10 三波叠加；48.11 空间波相加；48.12 折射率 $n=1-\frac{Nq_e^2}{2\varepsilon_0m\omega^2}$；48.13 相速度；48.14 $k=\frac{\omega}{c}-\frac{a}{\omega c}$；48.15 两列空间波；48.16 调制速率；48.17 群速度；48.18 $v_g=\frac{c}{1+a/\omega^2}$；48.19 $\Psi=Ae^{i(\omega t-kx)}$；48.20–48.21 相对论 $E$、$p$；48.22 量子色散关系；48.23 三维声波方程；48.24 克莱因-戈尔登方程——**全部正确**。
- **数字/量纲**：800 kHz / 800,000 次/秒、790–810 kHz、795 kHz、20 kHz/10 kHz、500–1500 kHz、500 条线/1/30 s、$250\times500\times30$、4 MHz/6 MHz、54–60 MHz、$\omega_c/\omega_m=5$ 与 $\approx100$、8:10、"900½/900"等均与英文一致。
- **图表**：6 幅图（48.1–48.6）齐全，图注与英文 Fig. 48–1～48–6 对应；正文图引用全部解析（0 undefined）；本章无表格。
- **自动候选差异**：230 小块 + 47 大块绝大多数为公式剥离噪声与参考 OCR 讹字（叠→全/伙、另→男、筒→简、畸→蝴、佯谬→伴廖 等），**不据以改动**；确属本仓库的问题即上表 5 条 + 低 3 条。

## 验证

- 入口：`preview/chapter-48/check.tex`（`\setcounter{chapter}{47}`、`\input{../../Chapters/VolumeI/Chapter48.tex}`；注释章名/路径已改对）。
- 命令：`cd preview/chapter-48 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍；移动 wrapfigure 后补跑第 3 遍使 label 稳定）。
- 结果：13 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 文本抽查：修正点均生效（"拍音和调制""拍频呢？""在 P 点的相位""频道 2（！）""它与图48.1表示的波""将“消息”发送出去…""一个是载频加上调频""如果这个相对概率是常数"）；旧串（"拍符""拍频呢。""式（48.1）表示的波"）出现 0 次。
