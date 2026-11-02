# 第 23 章《共振》审查报告

- 范围：`Chapters/VolumeI/Chapter23.tex`（原 312 行 →321 行，4 节）。对照 `_attachments/build-feynman/audit/en/I_23.txt`（585 行，公式被拆成多行）、官方页 <https://www.feynmanlectures.caltech.edu/I_23.html>；旁证 `_attachments/reference/zh/Chapter23.txt` 与 `ch23-candidates.md`（小块差异 327 条、大块 53 条；逐条判定，多数为参考文本 OCR 噪声/公式噪声，实际需改 17 处）。
- 段落对应：按节逐段核对（§23-1 复数和简谐运动、§23-2 有阻尼的受迫振子、§23-3 电共振、§23-4 自然界中的共振现象）；**发现并补回 1 个整段（"宽度"讨论）与 1 张图（图 23-5）**，其余无漏段、无重复。
- 结果：**已修 17 处（高 5、中 5、低 7）**，存疑 7 条（不改）。`preview/chapter-23/check.tex` 已由 `tools/make_chapter_check.py 23` 生成并修正注释章名/路径。行号为修改前。

## 高/中问题表

| 行号 | 问题（原文） | 英文依据（逐字引用） | 修正 |
|---|---|---|---|
| L264 后 | **漏整段**（中文从"与共振频率相对应"直接跳到下一例） | "But what about the width? What determines the width? … not really the natural width γ … two reasons … strained … slit of the spectrometer … inhomogeneities" | 补回整段："但是，宽度有多大？……由什么来确定宽度呢？……这有两个原因……不能随便断定图\ref{…}的宽度是自然的，还是由晶体中的不均匀性或分光计狭缝的有限宽度所引起的。" |
| L199 | **漏图**：正文写"（图23-5）"，但图 23-5（RLC 振荡电路）未排入；图文件 `Figures/VolumeI/Chapter23/由电阻、电容和电感组成的振荡电路.pdf` 本已存在，导致图 23-5 缺失、其后图号整体错位 | "Fig. 23–5. An oscillatory electrical circuit with resistance, inductance, and capacitance." | 补图（含图注/标签），并把"图23-5"改为"图\ref{figure:由电阻、电容和电感组成的振荡电路}"；图号 23.6–23.11 随之归位 |
| L43 | **公式被吞**："可以看到方程的实部不仅包含，还有。" | "the real part of the equation would not involve just λx²_r, but also −λx²_i" | "……不仅包含$\lambda x_r^2$，还有$-\lambda x_i^2$。" |
| L81 | **公式被吞**："$x$写成的实部，并把它们代入" | "we write F as the real part of F̂e^{iωt} and x as the real part of x̂e^{iωt}" | "$x$写成$\hat{x}e^{i\omega t}$的实部" |
| L239 | **公式被吞**："因为$\hat{I}=d\hat{q}/dt=i\omega\hat{q}$，所以我们能用代替，并得出" | "since Î=dq̂/dt=iωq̂, we can just substitute Î/iω for q̂" | "所以我们能用$\hat{I}/i\omega$代替$\hat{q}$，并得出" |
| L105 | "作为复数$\hat{x}$的实数部分的物理量$x$"**漏 $e^{i\omega t}$** | "the physical x, which is the real part of the complex x̂e^{iωt}" | 作为复数$\hat{x}e^{i\omega t}$的实数部分的物理量$x$ |
| L50 | "观察一下就很容易立即写出的方程"**漏 $x$**，句子不完整 | "it is very simple to write immediately … what the equation is for x" | ……就很容易立即写出$x$的方程： |
| L262 | "它转动的周期为$12.42~h-12~h$是由于地球的转动（潮汐是两个隆起部分）。由于月亮也在转动，还要加上一点。"句意断裂（易读成减法） | "at a period of 12.42 hours—12 hours for the earth (the tide is a double bump), plus a little more because the moon is going around" | "它转动的周期为$12.42~h$——$12~h$来自地球的转动（潮汐是两个隆起部分），由于月亮也在转动，还要再长一点。" |
| L230 | 表 23.1 第一列"**阻抗**"（impedance）对应 resistance | "resistance / drag coeff. (c=γm) / resistance (R=γL)" | 阻力 |
| L262 | "得出的$\omega_0$是**$10.20~h$**"（10 小时 20 分≈10.33 h） | "The ω0 obtained from Fig. 23–6 comes out 10 hours and 20 minutes" | 得出的$\omega_0$是$10$小时$20$分 |

**低 7 处（已修）**：L12"$i$表示$a$的虚部"→"下标$i$…"；L217"表23-1"硬编码→`表\ref{Table:23:1}`；L234"品质因素"→"品质因数"；L271 文献"Introduction to Solid State，Physics"→"Introduction to Solid State Physics"；L296"（Physics Review）"→"（Physical Review）"；L303 图 23-10 图注开头多余 `\\`；L310 图 23-11 图注"$n_\circ$"→"$n$"。

## 存疑项（未改，需 Lead 决定）

1. **L101 与 L27 的 $\hat{F}$ 相差一个符号**：前文（23.1 式）为 $\hat{F}=F_0e^{-i\Delta}$，L101 为 $\hat{F}=F_0e^{i\Delta}$——**eFLP 官方页原文亦如此**（书本身前后不一致，底本照译），未改，建议不动。
2. 表 23.1 第一列"刚性"（stiffness）：规范术语或作"劲度/刚度"，底本用"刚性"，保留。
3. L262"被拉扁成双潮汐"（squashed prolate into a double tide）：底本措辞，保留。
4. 图 23-6 图注"$S_2-$潮汐""$M_2-$潮汐"的连字符写法（英文 S₂-tide / M₂-tide），保留。
5. L161"留给读者"（英文 "leave it to the student"）；底本用"读者"，保留。
6. L285"经典能量的含义实际上与波振动的频率有关"漏英文 "a wave amplitude"（波振幅），底本简化，保留。
7. L239"除了被$i\omega$去除之外"（= 除以 iω）措辞生硬，未改。

## 覆盖性结论

- **段落/内容**：§23-1–§23-4 与英文逐段对应；补回"宽度"整段后无漏段；无重复粘贴。英文该段位于 Fig. 23–7 之后，中文补在氯化钠段之后（图注之前一页范围内），内容与次序正确。
- **公式**：23.1–23.20 逐式核对（复振幅定义 23.1、受迫振动 23.2–23.5、阻尼方程 23.6/23.6a、复响应 23.7–23.10、模与相位 23.11/23.12、窄共振近似 23.13、电容/电阻/电感 23.14–23.16、串联电路 23.17/23.18、复阻抗 23.19/23.20）；系数、符号、平方根内符号均与 eFLP 一致；23.6a 用 `equation*`+`\tag{23.6a}` 手工编号，`\ref` 解析正常。
- **数字**：12.42 h、12 h、10.5 h、10 小时 20 分、0.17 μm、Q=1000 与 Q=5、100,000 eV、10⁻⁵ eV、Q=10¹⁰、零频偏移 10¹⁰ cm、1962-01-01 等均与 eFLP 一致（"10.20 h"已改）。
- **图**：11 张图（图 23.1–23.11）齐全，顺序与正文引用一致；`Figures/VolumeI/Chapter23/` 下 11 个 PDF 全部被引用（无缺失、无冗余）。新增图 23-5 后，正文中所有图号引用（含宽度段"图23-7"）均解析正确。
- **表**：表 23.1 三列八行与 eFLP 逐格对照一致（"阻抗→阻力""品质因数"已改；"刚性"保留）。
- **人名/文献**：喀拉喀托、穆斯堡尔、Munk & MacDonald (1960)、Barnes (1932)/Kittel (1956)、Holden et al. (1949)、Bonner & Evans (1948)、Ferro-Luzzi et al. (1962) 等引用核对无误；"Physics Review"已改为 "Physical Review"。

## 验证（单章编译）

`preview/chapter-23/` 连编 2 遍：**0 error、0 Overfull、0 Underfull、0 Missing character、0 undefined references；PDF 13 页（A4）**。

## 未改动与建议

- 存疑 1–7 建议保持；若全书统一"stiffness→劲度"，建议全书批量处理而非本章单独改。
- 修改集中：新增图 23-5（7 行）+ 宽度段（1 段）+ 15 处行内修正；git diff 24+/15−（含新增段/图）。
