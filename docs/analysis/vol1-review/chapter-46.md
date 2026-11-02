# 第 46 章《棘轮和掣爪》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter46.tex`（133 行，**LF 行尾保持原状**；5 节 46-1～46-5，正文约 43 段）
- 英文：`_attachments/build-feynman/audit/en/I_46.txt`（46–1～46–5；公式/表格在抓取文本中为分式碎片）
- 旁证：`_attachments/reference/zh/Chapter46.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch46-candidates.md`（已逐类核对）
- 公式核对方式：eFLP 文本片段 + 参考中译本 OCR 逐式比对；2 幅图 + 1 张表逐幅渲染核对

## 结果

- **已修正 6 处（6 条：中 2、低 4）**；**存疑 2 项**（未改）。
- 单章编译：**10 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter46.tex`（6 行，**LF 行尾保持**）、`preview/chapter-46/check.tex`（仅注释：章名改《棘轮和掣爪》、`cd` 路径改 chapter-46）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L111 | "这一类碰撞正与另一类碰撞**相似**"——原意是两类碰撞**同样可能**（可逆性论证的关键一环） | "one kind of collision is just as likely as another" | 这一类碰撞与另一类碰撞是同样可能的 |
| 2 | L113 | "只是白的归白，黑的归黑，它就永远不会回到原来的状态"——与上文"没有特殊的安排"自相矛盾，"回到原来的状态"指代错位 | "If we start with the gas in no special arrangement, just whites and blacks, it will never get back." | 只不过是些白分子和黑分子，它就永远不会回到分开的状态 |

## 低严重度修正（已修）

- L35："而**给于**叶片那边" → 给予（错字；表 46-1 图内亦作"给予"）
- L67："但它**总是经常**推在一个斜面上" → "但它总是推在一个斜面上"（冗余，英文 "always"）
- L91："每个**原了**都有一定的能量" → 每个原子（形近错字）
- L103：$\Delta S=\int_{V_1}^{V_2}p\,dV/T$ 中压强符号作小写 $p$，与上句 `dQ=PdV` 不一致 → $P$

## 存疑项（未改）

1. **eFLP 章题脚注（2006 年编者补注）**："See Parrondo and Español, Am. J. Phys. 64(9), 1125 (1996) for a critical analysis of this chapter." 中文两版中译本均无此注；属 eFLP 编者补注而非原书内容，未补。
2. **L127 "我们一定是碰到了能产生这种情况的最可能的涨落"**：英文 "we must surely take the most likely fluctuation which could produce it"，"take" 译作"碰到了"语义略偏；底本同，未改。

## 覆盖性结论

- **段落/完整性**：5 节与英文 46–1～46–5 对应；逐句核对无漏句、无漏段、无重复粘贴；候选"大块差异"全部为公式/表格剥离噪声。
- **思想实验论证**：棘轮-掣爪不能永动（同温时正/反转概率同为 $e^{-\varepsilon/kT}$ 相抵）、热机模式（正向需 $\varepsilon+L\theta$、反向需 $\varepsilon$，可逆条件 $(\varepsilon+L\theta)/T_1=\varepsilon/T_2$、$Q_1/Q_2=T_1/T_2$、功/吸热 $=(T_1-T_2)/T_1$）、$T_2>T_1$ 时反向转动、角速度式 (46.1)、麦克斯韦妖、不可逆性来自"有序→无序"、熵的微观定义（可区分排列数目的对数）、氖/氩混合熵增 $Nk\ln2$、涨落说 vs 初始有序说、宇宙学结尾——均与英文一致，未曲解原意。
- **公式**：编号公式 46.1 及表 46–1 全部核对一致；正文 $\Delta S=\int dQ/T$、$dQ=P\,dV$、$\Delta S=Nk\ln(V_2/V_1)$ 均正确（已统一压强符号 $P$）。
- **图表**：2 幅图（46-1 棘轮与掣爪装置、46-2 $\omega$–$L$ 曲线）与表 46-1（图像）逐幅渲染核对，内容与英文一致；全部 label 均被正文 `\ref` 引用，无硬编码图号；图注/表注与英文一致。
- **术语**：棘轮、掣爪（底本用词，标准工程术语作"棘爪"）、布朗运动、卡诺循环、麦克斯韦妖、熵、涨落、推迟场/超前场等与英文一致。

## 验证

- 入口：`preview/chapter-46/check.tex`（`\setcounter{chapter}{45}`、`\input{../../Chapters/VolumeI/Chapter46.tex}`；本次仅改注释）。
- 命令：`cd preview/chapter-46 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：10 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 抽查：修正点均生效（"给予叶片""总是推在""每个原子""$P\,dV/T$""同样可能的""回到分开的状态"）；旧串（"给于""原了""总是经常""白的归白""相似。"）出现 0 次。
- 行尾：`file` 确认本章仍为 LF（无 CRLF），与第 44–52 章惯例一致。

## 未改动项与建议

- 存疑 2 项未改。
- 底本统一用"掣爪"（标准工程术语为"棘爪"），属全书译法，未单章改；如需统一应全书替换。
