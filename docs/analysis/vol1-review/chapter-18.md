# 第 18 章《二维空间中的转动》审查报告

- **范围**：`Chapters/VolumeI/Chapter18.tex`（205 行，4 节，34 段，22 个编号公式，4 张图）；对照 `_attachments/build-feynman/audit/en/I_18.txt`（正文 L39–250）。
- **旁证**：`_attachments/reference/zh/Chapter18.txt`（公开中译本 OCR）、`_attachments/reference/candidates/ch18-candidates.md`（小块差异 164 条、大块 28 条，绝大多数为公式/页码/图注噪声；参考文本自身讹误如"弦/蓄""矩/插""阳/阴""勒/惑"一律未采纳）。
- **段落对应**：中文 34 段 ↔ 英文 34 段，逐段 1:1——§18-1 质心 13:13、§18-2 刚体的转动 10:10、§18-3 角动量 5:5、§18-4 角动量守恒 6:6；无漏段、无漏句、无重复粘贴。
- **结果**：问题 11 条（高 0 / 中 3 / 低 8），**已全部修正**；存疑 6 项未改。带断言脚本执行（11 条旧串各恰命中 1 次），`git diff` 仅 10 行变化（原文件 CRLF 行尾已保留）。
- **单章编译**：`preview/chapter-18/check.tex`（`python3 tools/make_chapter_check.py 18` 生成，`\setcounter{chapter}{17}` + input Chapter18）连编 2 遍：**0 error、0 overfull、0 underfull、0 missing character、0 undefined references，10 页**（与修改前一致）。

## 已修问题（行号为修改前行号）

| # | 行号 | 严重度 | 类型 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|---|---|
| 1 | L9 | 中 | 漏字/多字 | 句子断裂："存在着一个在数学上可以定义的平均位置，**但不一定是物体上的一个点沿抛物线运动**"——"沿抛物线运动"被错挂到"点"上 | "there is a mean position which is mathematically definable, but not necessarily a point of the material itself, which goes in a parabola" | "存在着一个在数学上可以定义的平均位置，它沿抛物线运动，但不一定是物体本身的一个点。" |
| 2 | L118 | 中 | 术语/物理 | 习题含义走样："读者可以证明，在平衡时，**必须保证**绕任何一根轴……都为零"（英文是说"只需验证任意一根轴"） | "Prove that it suffices to be sure that the sum of torques about any one axis (in two dimensions) is zero." | "读者可以证明：只需确认绕任意一根轴（在二维空间中）的转矩之和为零，就足够了。" |
| 3 | L62 | 中 | 术语/物理 | 图 18-1 图注"二维转动**动力学**图示"，英文为运动学（本节正文亦作"转动运动学"） | "Fig. 18–1. Kinematics of two-dimensional rotation." | 图注改为"二维转动的运动学图示"（label 名不动） |
| 4 | L22 | 低 | LaTeX/结构 | "不同标记的**Fi**"未入数学模式 | "the sum of all the Fi's for all the different indexes" | `$\boldsymbol{F}_i$` |
| 5 | L32 | 低 | LaTeX/结构 | "我们用**M**来代表所有质量的总和"未入数学模式（同段下文作 `$M$`） | "Let us say M is the sum of all the masses" | `$M$` |
| 6 | L65 | 低 | LaTeX/结构 | "如图（**\ref{…}**）所示"缺"图"字，渲染成"如图（18.1）所示" | "in the usual manner (Fig. 18–1)" | "如图\ref{figure:二维转动动力学图示}所示"（渲染"如图18.1所示"） |
| 7 | L65 | 低 | LaTeX/结构 | "它在**x**方向上的距离变化了多少"未入数学模式（同句"$y$方向"为数学） | "how much the distance x changes" | `$x$` |
| 8 | L87 | 低 | 术语/物理 | "物体转过一个微小**距离**时所做的功"——转动应为角度 | "the work that we do when we turn something a little bit" | "转过一个微小角度时所做的功" |
| 9 | L135 | 低 | LaTeX/结构 | "角动量**L**的变化率"未入数学模式 | "the rate of change of a quantity L" | `$L$` |
| 10 | L137 | 低 | LaTeX/结构 | "力的**x**分量等于质量乘加速度$x$的分量"（前一个 x 未入数学） | "the x-component of force is the mass times the x-component of acceleration" | "力的$x$分量……" |
| 11 | L156 | 低 | LaTeX/结构 | "但**L**的第二种形式对相对论也是正确的"未入数学模式 | "the second form for L given above is relativistically correct" | `$L$` |

## 公式逐式核对（22 个编号公式，均无误，未改动）

18.1 F_i=m_i d²r_i/dt²；18.2 F_i=d²(m_i r_i)/dt²；18.3 ∑F_i=F=d²(∑m_i r_i)/dt²；18.4 R=∑m_i r_i/M；18.5 F=d²(MR)/dt²=M d²R/dt²；18.6 Δx=−PQ sinθ=−rΔθ·(y/r)=−yΔθ；18.7 Δy=+xΔθ；18.8 v_x=−ωy, v_y=+ωx；18.9 v=ωr；18.10 ΔW=F_xΔx+F_yΔy；18.11 ΔW=(xF_y−yF_x)Δθ；18.12 τ_i=x_iF_yi−y_iF_xi；18.13 τ=∑τ_i；18.14 τ=xF_y−yF_x=xm d²y/dt²−ym d²x/dt²；18.15 乘积微商展开（三项符号均正确）；18.16 L=xm(dy/dt)−ym(dx/dt)=xp_y−yp_x；18.17 L=xp_y−yp_x=rp_切向=p·动量臂；18.18 τ=∑τ_i=∑dL_i/dt=dL/dt；18.19 τ=∑τ_i=τ_外=dL/dt；18.20 L_i=m_i v_i r_i=m_i r_i²ω；18.21 L=Iω；18.22 I=∑m_i r_i²。**未发现公式错误，故公式内一律未改。**

## 存疑项（未改）

1. **L167"L_i之和定义一个新的量"**：英文 "and that defines a new quantity which we call the total angular momentum L"，中文为底本直译（"之和定义……"），可读懂，未重写。
2. **L179"如果一个质点系统不受外转矩作用时"**：底本"如果……时"句式杂糅，属语法瑕疵而非内容错误，未改。
3. **图 18-4 图注"转动惯量与质量臂有关"**：英文 "The 'inertia for turning' depends upon the lever arm of the masses"；"质量臂"为生造缩略（正文作"离轴距离"），改动需同步 label，仅标注。
4. **L142/L156"虽然，"句首逗号**：底本即如此（"虽然，……但……"），属译风，未改。
5. **L120"用几何法来画出奇特的项"**：英文 "figure out, geometrically, what this strange thing xFy−yFx amounts to"，"画出"略偏（figure out=弄清），下文即配图说明，可读，未改。
6. **L11"（它们的数目极大……）"**：英文 "(There are millions of them, so i goes to 10^23, or something)"，底本未译"数百万"，不影响论述，未改。

## 覆盖性结论

- **完整性**：中英 34 段逐句核对，无整段/整句缺失或重复；4 节标题、4 张图、22 个编号公式一一对应。
- **数字/符号核对**：10^23、1/2、图 18-1～18-4、式 18.1～18.22 均与英文一致；无数字错误。
- **人名/术语**：牛顿、开普勒、质心、刚体、转矩/力矩、角动量、转动惯量、运动学/动力学等术语无误（图注"动力学→运动学"已修）。
- **图表**：4 张图 PDF 齐备（`Figures/VolumeI/Chapter18/`），图注与英文一致（图 18-1 已修），正文全部用 `\ref`，无未解析引用。
- **编译验证**：0 error / 0 overfull / 0 underfull / 0 missing character / 0 undefined references，10 页。
- **未改动项**：上述存疑 6 项；未改其他章、未 commit。
