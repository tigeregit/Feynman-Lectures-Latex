# 第 26 章《光学：最短时间原理》审查报告

- **范围**：`Chapters/VolumeI/Chapter26.tex`（525 行；6 节；14 图；2 表；27 对 `%<<<NEW … %>>>NEW` 标记）。对照 `_attachments/build-feynman/audit/en/I_26.txt`（正文 L36–167）、`_attachments/reference/zh/Chapter26.txt`（对应改造前原文）、`_attachments/reference/candidates/ch26-candidates.md`。
- **NEW 块处理**：27 对标记完整保留（修改前后均 27 对，未触碰标记本身）；新增的导读/速读路径/小标题/小结框/概念图/图注提示一律不当 OCR 错误改，只核对事实陈述——核对结论：与正文一致，仅修正 2 条事实性表述（#11、#12）。
- **结果**：问题 12 条（高 0 / 中 6 / 低 6），**已全部修正**；存疑 7 项未改。带断言脚本执行（12 条旧串各恰命中 1 次，NEW 标记成对性校验通过），`git diff` 仅 12 行变化（原 CRLF 行尾保留）。

## 中等问题（已修，行号为修改前行号）

| # | 行号 | 类型 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|---|
| 1 | L309 | 错字 | 图 26-6 图注"当一束光通过一块透明**版**时" | "A beam of light is offset as it passes through a transparent block." | 透明板 |
| 2 | L316 | 错字 | 图 26-7 图注"**地平线附件**，表观太阳比真实太阳高出约1/2度" | "Near the horizon, the apparent sun is higher than the true sun by about 1/2 degree." | 地平线附近 |
| 3 | L495 | 术语/物理 | "量子**动力学**上精确的观点"（量子动力学≠量子力学；参考底本作"量子力学"） | "from what we now believe is the correct, quantum-dynamically accurate viewpoint" | 量子力学上精确 |
| 4 | L226 | 公式 | 角度近似式写成严格等号：∠XCF = ∠BCN′ = θr | "EXC=ECN=θi and XCF≈BCN′=θr (when X is near C)" | ∠XCF **≈** ∠BCN′ = θr，并在 L224 补"（当$X$靠近$C$时）" |
| 5 | L460 | 术语/物理 | "需时最短或**最终**的路径"（extreme 误作 final；下文正讨论极小/极大） | "light decides which is the shortest time, or the extreme one, and chooses that path" | 需时最短或取极值的路径 |
| 6 | L485 | 术语/物理（NEW 块） | §26.5 小结"缝窄到没有邻近路径可核对时，光**反而像沿直线走**"——与正文相反（缝越窄，D′ 收到的辐射反而更多） | "if we prevent the radiation from checking the paths by closing the slit … there is but one path available, and the radiation takes it! With a narrow slit, more radiation reaches D′" | 光只走唯一可用的那条路径 |

## 低问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 7 | L191 | "以**$X$**标出的线表示河岸"（图注线标为小写 x，与动点 X 混淆） | "The line marked x is the shoreline." | $x$ |
| 8 | L171 | "距离跟**B**点在镜面以上的距离相同"未入数学模式 | "the same distance below … as the point B is above the plane" | $B$ |
| 9 | L386 | "不论**X**取在哪里"未入数学模式 | "no matter where X is chosen" | $X$ |
| 10 | L224 | 配合 #4 补出英文明示的条件"（当$X$靠近$C$时）" | "…θr (when X is near C)" | 见 #4 |
| 11 | L16 | 速读路径"**每节末尾**的小结和加粗术语"（实际仅 §26.1/26.3/26.4/26.5 有小结框） | —（NEW 块事实陈述） | 小结框和加粗术语 |
| 12 | L77 | "深入到定量一些的**内容方向**"（features 误作"方向"） | "go a little further into the quantitative features" | 内容方面 |

## 存疑项（未改）

1. **L267"设想有一颗数$10^9mi$远的星"** ← "Imagine a star billions of miles away"：底本作"数10^9 mi"，表述生硬但可解，未改。
2. **L275"我也能理解抛物面镜"** ← "I can understand mirrors, too"：底本把 mirrors 具体化为"抛物面镜"（范围变窄）；属底本译法，未改。
3. **L275"我也能画一个透镜"** ← "I can figure out a lens, too"："画"略偏（应为设计/算出），句意可通，未改。
4. **L89"托勒玫"**：旧译名（今多作"托勒密"），底本与参考文本一致，未改。
5. **两表 `\caption{}` 为空**：英文表 26–1/26–2 亦无文字标题，仅编号；与全书其他章一致，未改。
6. **L331"许多与缝隙边缘平行的条纹"** ← "a lot of fringes along the edges too"："平行"为底本增补，未改。
7. **NEW 导读"更精确的波动处理留到第 28 章《电磁辐射》"**：第 28 章含"干涉"等波动内容，判断成立，未改。

## 覆盖性结论

- **结构**：6 节与英文 26–1…26–6 一一对应；逐段核对无漏段、无漏句、无重复粘贴。修改前 `tools/verify_chapter.py 26` 为 PASS（10551/10551 零删改），可证 NEW 改造未增删原文内容。
- **表格**：Table 26–1、26–2 共 16 组角度数值逐项核对，与英文完全一致（如 20°：15.5°/15°，30°：22.5°/22°，60°：40.5°/40.5°，80°：50°/48°）。
- **公式**：编号式 (26.1)–(26.6) 及角度近似式逐式核对，仅 #4 一处 = → ≈ 修正；其余未动。
- **图**：14 张与 Fig. 26–1…26–14 一一对应，图文件齐备，图注全部核对（#1、#2 两处文字修正）。
- **人名/术语**：托勒玫、斯涅耳、希罗、费马、帕洛玛望远镜、斯涅耳定律、倒易原理、椭球/抛物面镜等无误。
- **NEW 块**：27 对标记完整；chapterintro/readingpath/runin×8/summarybox×4/conceptmap/figsource/fighint×2 的事实陈述与正文一致，仅 2 条修正（#6、#11），概念图（三情形"最短时间"）物理图像核对无误。

## 验证

- **单章编译**：`preview/chapter-26/check.tex`（`python3 tools/make_chapter_check.py 26`，文件已存在未覆盖，章号 25 + input Chapter26）连编 2 遍：**0 error / 0 overfull / 0 underfull / 0 missing character / 0 undefined references，15 页**（与修改前一致）。
- **零删改校验**：修改前 PASS；修改后 `verify_chapter.py 26` **FAIL（10559 vs 10551，首个差异 L77"向/面"）——属预期**：本轮 12 处均为有意内容修订，未删除任何原文；NEW 标记结构与新增内容未被破坏（除 #6、#11 两条事实修正）。

## 未改动项与建议

- 存疑 7 项均保持底本原貌；"托勒玫/托勒密"等译名统一建议由 Lead 在全卷层面决定。
- 未改其他章、未 commit；未运行全书编译。
