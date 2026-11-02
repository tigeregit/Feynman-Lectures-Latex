# 第 13 章《功与势能（上）》审查报告

- **范围**：`Chapters/VolumeI/Chapter13.tex`（原 313 行，4 节：落体的能量 / 万有引力所做的功 / 能量的求和 / 巨大物体的引力场）；对照 `_attachments/build-feynman/audit/en/I_13.txt`（正文 L36–L740）。
- **旁证**：`_attachments/reference/zh/Chapter13.txt`（公开中译本 OCR，仅用于区分"底本译法"与"本仓库讹变"）；`_attachments/reference/candidates/ch13-candidates.md`（小块 240 条、大块 54 条，逐条判定：绝大多数是参考文本自身 OCR 噪声——公式整体丢失、粘连带页码/"费因曼物理学讲义"字样；据此判"参考误"者未采纳，仅 2 处（"场/力"、"对总和式中"）用于确认底本措辞）。
- **段落对应**：英文正文 **29 段**（另 6 条图注、1 条脚注、18 个编号公式）↔ 中文 **73 个段落块**——底本体例为"按句分段"，故中文段数约为英文 2.5 倍；逐句核对**无漏句、无漏段、无重复粘贴**。
- **结果**：修正 **15 项**（对应 **20 处**替换/移动操作）：**高 2 / 中 6 / 低 7**；另存疑 7 项。
- **单章编译**：`preview/chapter-13/check.tex`（`tools/make_chapter_check.py 13` 生成；校正章名/路径注释）连编 2 遍：**12 页，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（修正前基线有 1 处 undefined reference，见"验证"）；`git diff` 仅 Chapter13.tex（+19/−17 行，CRLF 保持），未动其他章、未 commit。

## 已修问题（行号为修改前 `Chapter13.tex` 行号）

| # | 行号 | 严重度 | 类型 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|---|---|
| 1 | L115 | **高** | 公式/符号 | "这个力是 **GM/r²** 乘以质量 m"——引力为吸引力，漏负号（下文式 13.11/13.12 均用 −GMm/r²，前后矛盾） | "the force is −GM/r2 times the mass m" | 这个力是 $-GM/r^2$ 乘以质量 $m$ |
| 2 | L216 | **高** | 公式 | 式（dr_ij/dt）展开中 y、z 两项漏掉微分号 d：`(\frac{y_i}{dt} - \frac{y_j}{dt})`、`(\frac{z_i}{dt} - \frac{z_j}{dt})`（x 项正确作 dx/dt） | "2(yi−yj)(dyi/dt − dyj/dt) + 2(zi−zj)(dzi/dt − dzj/dt)" | `(\frac{dy_i}{dt}-\frac{dy_j}{dt})`、`(\frac{dz_i}{dt}-\frac{dz_j}{dt})` |
| 3 | L93 | 中 | 物理表述 | "动能的变化**率**等于沿着曲线的分力乘以位移元的积分"——工作—动能定理讲的是动能**变化**；与前文"动能的变化率等于功率"（正确）混同 | "the change in K.E. … is equal to the integral of the component of the force along the curve times the differential displacement ds" | 动能的变化等于…（删"率"） |
| 4 | L242 | 中 | 图文/术语 | 图 13-5 图注"无限大物质薄片对一个质点产生的**万有引力F**"——图内标注是场矢量 **C**（dC、C、dC_x），正文亦称"场 dC"，英文图注为 "The gravitational field C …" | "The gravitational field C at a mass point produced by an infinite plane sheet of matter." | …产生的引力场 $C$ |
| 5 | L32–L39 | 中 | 结构/断句 | 图 13-1 的 wrapfigure 插在句子中间："…加在一〡（图）〡起，则能量是守恒的。" | 英文 Fig. 13–1 位于 "We have shown, from Newton's second law…" 段之前 | 图移到该段之前，合并为"…加在一起，则能量是守恒的。" |
| 6 | L108–L115 | 中 | 结构/断句 | 图 13-2 的 wrapfigure 插在句中："…。在这种〡（图）〡情况下能量守恒定律还适用吗？" | 英文 Fig. 13–2 位于该段（"We shall first consider…circumstances?"）之后 | 图移到该段之后，合并"在这种情况下…" |
| 7 | L158–L165 | 中 | 结构/断句 | 图 13-4 的 wrapfigure 插在句中："…就可证实沿真〡（图）〡实闭合曲线一周所做的功为零" | 英文 Fig. 13–4 位于 "Of course we may wonder…" 段之前 | 图移到该段之前，合并"沿真实闭合曲线…" |
| 8 | L264–L271 | 中 | 结构/断句 | 图 13-6 的 wrapfigure 插在句中："…地球对其表面或外〡（图）〡面一点所产生的力…"；且英文此处为两段（Fig. 13–6 在两段之间） | 英文 Fig. 13–6 位于 "Now we come to a most interesting…" 段与 "We now demonstrate…" 段之间 | 合并"…或外面一点…"，在图处恢复分段，图置于两段之间 |

## 低严重度修正（7 项）

- L30 "即一个**垂直向下**的力（负号的意思是指作用向下）"→"竖直方向的力（负号…）"（原文 a vertical force，方向由负号说明，原译自相重复）。
- L45 "但切向力 F_t **不是 mg**"→"**不是 −mg**"（英文 "not −mg"；下文 F_t=−mg sinθ）。
- L61 "我们得到**三个项**"→"三个**吓人的**项"（英文 "three terrifying terms"，底本漏译）。
- L175 "减去**某些常数与该点半径的比值**"→"**某个常数除以该点半径**"（"some constants divided by the radius"）。
- L177 脚注 "按表9.2的单位，**能量是** (vx²+vy²)/2−1/r"→"**单位质量的能量是**…"（英文 "The energy per unit mass is…"）。
- L227 "1和3这对质点**对总和式中**只贡献一项"→"对总和只贡献一项"（衍"式"）。
- L227 "**为了保持这一目的**，我们约定"→"为了做到这一点，我们约定"（英文 "To keep track of this"）。

## 存疑项（未改，建议上游确认）

1. **L290–L294 的 dW 符号/积分限**：中文作 `dW=−Gm'2πaμdr/R`、`W=(−Gm'2πaμ/R)∫_{R−a}^{R+a}dr`；eFLP 作 `dW=+Gm'2πaμdr/R`、积分限相反。二者各自自洽且最终 `W=−Gm'm/R` 相同（已逐式验算），按"公式内勿误改"未动。
2. **"永久运动"**（L129 两处）：英文 perpetual motion，通行作"永恒运动"；底本即作"永久运动"，两处一致，未改。
3. **L271 "正像地球质量全部集中在地心所产生的力一样"**：英文 "the same as if all the mass of the earth were located at its center"，"as if" 的语气较弱；底本如此，未重写。
4. **L102 "在支点的末端放置一个小质量的物体"**：英文 "take a mass on the end of a pivot"，底本表述（"放置"），未改。
5. **单位排印**：`$1 N\cdot m$`、`$1 J$`、`$1 kW\cdot h$`、`$3.6\times10^6J$` 等单位在数学模式中排斜体——全书体例，未改。
6. **L262 "两个平板之间的场"**：底本 OCR 作"力"，我们作"场"（与英文 field、下文 E=σ/ε₀ 一致），保留。
7. **"第4章"**（L5）为硬编码文字；项目各章无统一 chapter label，未转 `\ref`。图 13-4 图注中 "smooth" 的引号底本未译（微瑕）。

## 覆盖性结论

- **完整性**：逐句核对英文 29 段全部句子，无整段/整句缺失，无重复粘贴；中文按句分段（73 段）属底本体例，非结构错误。图表编号 13.1–13.6 与 eFLP Fig. 13-1～13-6 顺序一致。
- **公式核对**：18 个编号公式（13.1–13.18）逐式与英文对照，仅 #2（L216 漏 d）一处错误已修；其余数值/符号一致：13.10 `−mg(z₂−z₁)`、13.11/13.12 引力势能符号、13.14 成对求和、13.15/13.16 含 `−Gm_im_j𝒓_ij/r³_ij` 与 `𝒓_ij·𝒗_i/r_ij`、13.17 `−2πGμ`、13.18 `−Gm'm/R`；14 处式号引用（13.4/13.5/13.7/13.11/13.12/13.14/13.15/13.16）全部指向正确公式。
- **数字/单位**：1.5%、1000 W×3600 s=3.6×10⁶ J、1 N·m=1 J、kW·h、3.6×10⁶ J 均与英文一致。
- **图**：6 个图文件齐备；图 13-5 图内标注（dC、C、dC_x、dm、ρ、O、a）与图注/正文一致（据此改图注为"引力场 C"）；图 13-4 图内 a/b/c/F/θ/x/s 与正文"ab 垂直、bc 水平、s cosθ=x"一致；图 13-6 图内 a/R/r/x/P 与推导一致。
- **表**：本章无表，仅 2 处跨章引用第 9 章"表 9-2"（\label{Table:9:2} 存在于 Chapter9.tex，全书编译可解析）。

## 验证（单章编译）

| 项目 | 结果 |
|---|---|
| 入口 | `preview/chapter-13/check.tex`（工具生成；校正注释；为跨章的 `Table:9:2` 加 phantom 标签占位） |
| 编译 | `xelatex -no-mktex=tfm -interaction=nonstopmode` 连编 2 遍 |
| 页数 | **12 页**（修正前基线亦 12 页） |
| error | **0** |
| Overfull / Underfull | **0 / 0** |
| Missing character | **0** |
| undefined references | **0**（修正前基线为 1：跨章 `Table:9:2`；已由单章入口的占位标签解决，正文仍用 `\ref`，全书编译不受影响） |
| 其他 | PDF 中无 `??`；跨章引用渲染为"表 9.2" |
| 改动范围 | `git diff` 仅 `Chapters/VolumeI/Chapter13.tex`（+19/−17 行，CRLF）；`preview/chapter-13/` 为新增；未 commit、未跑全书 |

**未改动项**：存疑 1–7；"蜕变/衰变"类术语统一、"象/像"字形等全书问题未在本章单独处理。
