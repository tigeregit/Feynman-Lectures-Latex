# 第 8 章《运动》审查报告

- 任务：task-20（第 1 卷剩余章节计划第一批）；日期：2026-11-02；分支 `feat/reading-efficiency`
- 范围：`Chapters/VolumeI/Chapter8.tex`（修改前 343 行 → **修改后 341 行**）
- 对照材料：
  - 英文原文 `_attachments/build-feynman/audit/en/I_08.txt`（英文正文 29 段，L36–L146；Table/Fig 各占行）
  - 官方页 <https://www.feynmanlectures.caltech.edu/I_08.html>（经 `r.jina.ai` 文本/HTML 取回：核对 Table 8–1~8–4 数值、Zeno/气球/88 ft/s 等数字；确认**本章 eFLP 无脚注**）
  - 公开中译本 `_attachments/reference/zh/Chapter8.txt`（旁证，OCR 质量差：数字/单位混写、"英尺→ft"、公式成乱码；多数候选差异为参考文本自身噪声）
  - 自动候选差异 `_attachments/reference/candidates/ch8-candidates.md`（550 小 + 47 大；原缺，按 playbook 用 `python3 tools/chapter_diff.py --chapter 8` 生成）

## 结果概览

- 问题 **24 条（高 2 / 中 12 / 低 10）**，**已全部修复**；另存疑 8 条未改。
- 修改方式：带断言的 `/tmp/fix_ch8.py`——42 处替换，每条断言"old 串恰好命中 1 次"才执行（防误改），先 dry-run 复核 diff 再 `--apply`；保留原文件 CRLF 行尾。
- 单章编译：新建 `preview/chapter-8/check.tex`（`\setcounter{chapter}{7}` + `\input{Chapter8.tex}`），`-no-mktex=tfm` 连编 2 遍：**13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined reference**；5 条基线 warning（xeCJK 重定义、带路径 usepackage、hyperref colorlinks、黑体字形缺、字形汇总），无 SimSun 噪音。

## 高/中问题（行号为修改后文件当前行号）

| 行号 | 问题 | 英文依据（逐字 ≤25 词） | 修正 |
|---|---|---|---|
| L9 | **单位错误**："开过一百公里的汽车" | "in describing the motion of a car that is going a hundred miles" | 一百英里 |
| L9、L34、L68、L81、L83、L122、L175、L180、L199、L203、L241、L248、L342 | **表格编号与引用体系错乱**：表 8.1/8.2 用 `\caption*` 手工编号不占计数器，导数表/速度表被自动编号成"表 8.1/8.2"（与前两表**重号**）；L122 `\ref{tab:表8.2}` 解析成"表 8.1"（指错表）；正文硬编码"表8.3/表8.4"与渲染编号不符；4 个图/表 label 中 2 个是失效孤儿 label | 英文 Table 8–1、8–2、8–3、8–4 顺序；Fig. 8–1…8–4 | 四表统一改 `\caption{\label{...}}` 自动编号 8.1–8.4，label 移到 caption 之后；正文 6 处表引用、3 处硬编码图引用（图8.1/8.2/8.4）改为 `\ref`；删除失效 label `tab:表8.1`、`tab:表8.2` |
| L81 | "人们还知道，在那些半分钟的标记处，汽车开到了那里"（把"必须知道车在哪里"译错） | "one would have to know where the car is at the half-minute marks, too" | 人们还必须知道在那些半分钟的标记处汽车在哪里 |
| L81 | "我们假定这个曲线图可以这样来解释" | "we suppose that the graph means something, that the car has some position…" | 我们假定这个曲线图意味着某种东西，即汽车在所有的中间时刻都具有某个位置 |
| L95 | OCR："**而着**并不是容易做到的" | "and this is not so easy to do" | 而这并不是容易做到的 |
| L95 | OCR："我们必须**静确定定义**每一件事" | "we have to define everything precisely" | 我们必须精确地定义每一件事 |
| L101 | 玩笑译错："当然，这是被某些思想混乱的人所促成的。" | "being helped, of course, by some very confusing Greeks" | 当然，这也多亏了一些非常令人困惑的希腊人。 |
| L101 | "但在到达**跑步的终点**时" | "but on arriving at the end of that run" | 但在跑到那段路程的终点时 |
| L107 | OCR："走上**正规**了" | —（正轨） | 走上正轨了 |
| L109 | **invented 误作"发现"**："牛顿和莱布尼兹**发现**…微积分的**发现**是为了描述运动" | "This idea was invented by Newton and by Leibniz… Calculus was invented in order to describe motion" | 牛顿和莱布尼茨**发明**…微积分的**发明** |
| L141 | "前缀 Δ 不是一个**常数**"（"乘数/因子"混淆） | "The prefix Δ is not a multiplier" | 不是一个乘数 |
| L217 | OCR："**知道**路程的终点为止" | "We proceed similarly for each second, to the end of the run" | 直到路程的终点为止 |
| L277 | 三维距离错："测量第三个距离，即到 **z 轴**的距离" | "measuring a third distance, the z-distance… distances are now measured from coordinate planes" | 即到 xy 平面的距离（z 距离） |
| L293 | "考虑**两个相继的质点**"（应为两个相继位置） | "consider two successive positions of the particle" | 考虑质点的两个相继位置 |

## 低问题（已修）

L9 "粗糙一些"→"粗略一些"；L83 "遵循简单的法则以简单的方式"→"较简单的法则、以较简单的方式"；L95 "如此之类"→"诸如此类"；L101 半角括号 "芝诺(Zeno)/阿基利斯(Achilles)"→全角；L101 "错在那里"→"错在哪里"；L103 "并且更公正和理智地"→"而是更公正、理智地"；L105 脚注"苏格拉底的太太。。"→"。"；L234 "微分， 即"→"微分，即"；L327 "匀加速度($-g$)"→"（$-g$）"；L40/L74 `\includegraphics` 选项内 3 处多余空格删除；L342 行尾多余空格删除。

## 存疑项（未改）

1. **本章脚注**：eFLP 官方页 raw HTML 中无任何 footnote；中文两条脚注（L105"这一定是苏格拉底的太太"、L153"此处暗指 y=Ax²+Bx+C 这样的形式"）疑为中译本**译者注**，未加"——译者注"标记。建议上游确认后补标记（本报告未擅自加）。
2. "阿基利斯"（常译"阿基里斯"）：底本译名，保留。"莱布尼兹"已按标准名改"莱布尼茨"。
3. L279 "到 x 轴的距离和到 y 轴的距离"：英文原文亦作 "how far it is from each of the two axes"，属原文表述，未改（仅 3D 处补 xy 平面）。
4. L250 "速度总是每秒改变 32 英尺每秒"：系 "32 feet per second, per second" 的直译，保留底本风格。
5. 表 8.1/8.2 与图并排的 minipage 版式（表左图右、图 `totalheight=0.8\textheight`）为中文版既有排版，未动。
6. "毋需"等底本异形词保留。
7. L5 "描述它在运动以及如何运动这一事实"略拗口但语义无误，未改。
8. 参考中译本"100km"亦为底本误译；本次按英文改"一百英里"，未随参考。

## 覆盖性结论

- **段落**：英文 29 个正文段逐段核对（中文因公式显示被拆为 57 个排版段），**无整段缺失、无合并、无重复、无漏句**；候选 47 条大块差异经核对均为公式/图表环境噪声或参考文本自身 OCR 噪声（无"我们漏句"项）。
- **公式**：`s=16t²`、`v=x/ε`、`v=lim Δs/Δt`、`ds/dt`、`s=ΣvΔt`、`s=∫v dt`、`a=dv/dt=32`、`a=d²s/dt²`、`v_x=dx/dt` 等及 (8.1)–(8.19) 编号与引用全部正确（编译后 0 undefined）。
- **数字/量纲**：车表 0/1200/4000/9000/9500/9600/13000/18000/23500/24000；落体表 0/16/64/144/256/400/576；v=32t、160 ft/s、88 ft/s（=60 mph）、7 分钟、5000/4900/5100 ft/min、1/1000 小时、0.1/0.001 s、416.16/16.16/161.6/160.016/400.160016、Zeno 的 10 倍/100 m/10 m/1 m/10 cm、气球 100 cm³/s 与 1000 cm³、g=32 ft/s²——全部与英文一致（唯一错项"一百公里"已改）。
- **图表**：4 表 4 图编号与正文引用全部一致（表 8.1–8.4、图 8.1–8.4）；表头/图注与英文 Table 8–1~8–4、Fig. 8–1~8–4 对应。
- **编译**：13 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined reference；2 遍通过。

## 未改动项与建议

- 两条译者注脚注建议加"——译者注"（需 Lead 确认，未改）。
- 若需与英文原书版式统一，表 8.1/8.2 与图并排的 minipage 可后续调整（本次仅动编号，不动版式）。
