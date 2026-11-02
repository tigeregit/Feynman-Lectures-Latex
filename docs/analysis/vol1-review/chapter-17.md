# 第 17 章《时空》审查报告

- 审校员：rev2-s1；日期：2026-11-02
- 范围：`Chapters/VolumeI/Chapter17.tex`（222 行，CRLF）；对照：`_attachments/build-feynman/audit/en/I_17.txt`（17–1…17–5，5 节）、公开中译本旁证 `_attachments/reference/zh/Chapter17.txt`、候选差异 `_attachments/reference/candidates/ch17-candidates.md`（小块 228 / 大块 30，已逐条过滤）。
- 结果：**问题 16 项（高 2 / 中 4 / 低 10），已全部修正（共 18 处编辑）**；存疑 7 项未改。`git diff` 13 行（13 增 13 删，保持原 CRLF 行尾）。

## 问题表（已修）

| # | 行号 | 级别 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|---|
| 1 | L119 | 高 | "我们是从以速度 **$v$** 运动的宇宙飞船上来观察这一物体的"——飞船速度应为 $u$，否则与"物体速度 $v$""$v$ 和 $u$ 同向"自相矛盾 | "a space ship which itself is moving with a velocity u"（I_17 L138） | `以速度$v$运动` → `以速度$u$运动` |
| 2 | L219 | 高 | "动量等于**波长除以**普朗克常数"——关系反了（应为普朗克常数除以波长） | "the momentum … is h divided by the wavelength: p=h/λ"（L374） | 改作"动量等于普朗克常数除以波长"（公式 $p=h/\lambda$ 不变） |
| 3 | L124 | 中 | "但是应该用**作为**速度"——漏掉符号 $v'$，句子不成义 | "he would use v′ for the velocity"（L145） | 改作"但是应该用$v'$作为速度" |
| 4 | L90 | 中 | "在负**：**轴上P点处"——$t$ 被 OCR 成全角冒号 | "an object at P on the negative t-axis"（L108） | 改作"在负$t$轴上P点处" |
| 5 | L137 | 中 | "用不带**撤**的能量和动量"——"撤"应为"撇"（unprimed，与上文"打上一撇"呼应） | "in terms of the unprimed energy and momentum"（L186） | 改作"不带撇" |
| 6 | L219、L221 | 中 | 频率符号 ν 被写成 $v$：$E=hv$（2 处）、$v=c/\lambda$（1 处）；$v$ 在本章是速度，易致混淆 | "E=hν"、"ν=c/λ"、"using also E=p and E=hν"（L374、L379） | 改为 $E=h\nu$（2 处）、$\nu=c/\lambda$（1 处） |
| 7 | L61 | 低 | "几何学中所以我们…名称但值得注意"——缺两个逗号，句读粘连 | "We give it a different name because it is in a different geometry, but…"（L78） | "几何学中，"、"名称，" |
| 8 | L90 | 低 | "可以**低于**光速的速率从区域2…"——缺介词"以" | "by moving along at a speed less than the speed of light"（L108） | 改作"可以以低于光速的速率…" |
| 9 | L90 | 低 | "通过O和Q**␣**两点"——多余半角空格 | "the axis of time might go through both O and Q"（L108） | 删去空格 |
| 10 | L137 | 低 | "能量$E'$就是 **$m$** 乘上式"——英文为 $m_0$（静止质量），且下式分子用 $m_0$ | "The energy E′ is then simply m0 times the above expression"（L186） | 改作 $m_0$ |
| 11 | L152 | 低 | 新动量下标误作大写：$p'_X$ | "Next we must find the new momentum p′x"（L225–228） | 改作 $p'_x$ |
| 12 | L188 | 低 | "或者简单地用$p_i$**，**来表示一般分量"——多余逗号 | "or we could simply refer to a general component as pi"（L319） | 删去逗号 |
| 13 | L190 | 低 | "$p_z$是**z**方向的动量"——变量未用数学体（同句 $p_x$、$p_y$ 均为数学体） | "pz is that in the z-direction"（L321） | 改作 `$z$方向` |
| 14 | L192 | 低 | "所有粒子在**x，y和z**的每一个方向…"——变量未用数学体 | "the sums of all momenta in the x-direction, in the y-direction, and in the z-direction"（L323） | 改作 `$x$，$y$和$z$` |
| 15 | L210 | 低 | "在$\Sigma$上加一撇"——式 (17.15) 用的是 $\sum$，此处符号不一致 | "The prime on ∑ means that…"（L350） | 改作 `$\sum$` |
| 16 | L38 | 低 | 图 17-1 图注："（a）…粒子轨迹**：**（b）…"、"…粒子轨迹**：**（d）…"，两项之间应为分号 | "Three particle paths in space-time: (a)…; (b)…; (c)…; (d)…"（L67） | 两处"："改为"；" |

## 存疑项（未改）

1. **L30** "这时情况就完全不同了" ← "then this whole business would be irrelevant"：irrelevant（无关紧要、不成立）译"完全不同"，语义偏移；底本如此，未改。
2. **L32** "总是比它的'宽度'和'深度'更为重要" ← "is somehow greater"：greater（更实在、更大）译"重要"略偏；未改。
3. **L32** "看到一些别人的时间——比方说'滞后的'" ← "we would see 'behind,' so to speak, a little bit"：behind 指（时间上的）"后面/背后"，"滞后的"为意译；未改。
4. **L63** "如果我们找到一个x和y可以互换的奇妙空间，那似乎是荒唐的" ← "that is an absurdity if we are going to have a wonderful space with x's and y's that can be interchanged"：原文意思偏向"（不取 c=1）才荒唐"，译文读来像"存在这种空间才荒唐"；疑底本译法，未改。
5. **L90、L92** "可感知的过去/未来" ← "affective past / affective future"：affective（有影响的）译"可感知的"略偏（同句另有"有影响的过去/未来"），底本如此，未改。
6. **L204** "加一个中间带点的四边形" ← "with a square dot between"（方点符号 ⊡）：译文以"中间带点的四边形"描述该符号，可通，未改。
7. **L188–190** "不要轻视这些符号，要看到它们的出现是很有用的" ← "do not laugh at notations; invent them, they are powerful"："invent them / powerful"未充分译出；底本如此，未改。

## 覆盖性结论

- **节/段对应**：5 节 ↔ 5 节。逐段（含公式、图前后被 display 数学分开的文字块）对照英文，**无整段缺失、无重复粘贴、无错位**；中英"段落"切分因公式/浮动图不同而数量不同（如 §17-1 中文一句话被图 17-1/17-2 分隔），已逐句核对。
- **公式**：16 个编号公式 (17.1)–(17.16) 及全部中间公式（E′、1−v′²、p′ₓ 等）逐式对照英文，符号、系数、上下标均无误；本次仅改两处文字性错误（#2、#6），公式本体未动。
- **数字**：无年代/数字错误；3×10⁸ m、1/(3×10⁸) s、3.3 十亿分之一秒、0.511×10⁶ eV、八分钟、四年、45° 均与英文一致。
- **图**：图 17-1…17-4 四个 label 全部被正文引用（17-1 引用 4 次），图号与英文 17–1…17–4 对应；图 17-1 图注标点已修（#16）。
- **人名/术语**：洛伦兹、莫/乔（Moe/Joe）、闵可夫斯基、光锥、类空/类时间隔、四维矢量、四维动量、多普勒效应等均正确；跨章引用式 (11.5) 正常解析。
- **参考文本误（不改，仅记录）**：候选清单 25 条 CJK 级差异几乎全是参考 OCR 误（撇/撤、空/室、蜕/晓、叉/又、荒/功、若/车、隔/陋、呢/昵、步骤/又、四维矢量的"和拓"等），本仓库文字正确；唯一例外是 L137 我们的"撤"也确实错了（已修 #5）。

## 验证

- `preview/chapter-17/check.tex`：由 `python3 tools/make_chapter_check.py 17` 生成（章号 16、input Chapter17.tex）；因本章引用第 11 章式 (11.5)，另加 `\usepackage{xr}` + `\externaldocument{../../Chapters/VolumeI/Chapter11}` 解析跨章引用（依赖 `Chapters/VolumeI/Chapter11.aux`）。
- 连编 2 遍：**0 error / 0 Overfull / 0 Underfull / 0 Missing character / 0 undefined reference**；11 页；0 处"??"。PDF 抽查：式（11.5）、图17.1 图注分号、负 t 轴、"以速度 u"、"用 v′ 作为速度"、$E=h\nu$、$\nu=c/\lambda$、"普朗克常数除以波长"、$m_0$、$p'_x$、$\sum$ 均正确显示。
- 修改量：`git diff` 13 行（13 增 13 删）；未 commit，未改其他章、tools 或全书。
