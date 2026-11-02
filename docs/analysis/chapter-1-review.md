# 第 1 章《原子的运动》精读与内容审查报告

> **日期**：2026-11-02　**分支**：`feat/reading-efficiency`
> **审查对象**：`Chapters/VolumeI/Chapter1.tex`（386 行；4 节；10 张插图；正文汉字约 1.04 万）
> **对照材料**：eFLP 官方英文 I_01（本地抓取 `_attachments/build-feynman/audit/en/I_01.txt`；官网 <https://www.feynmanlectures.caltech.edu/I_01.html> 经文本代理取回；目录 <https://www.feynmanlectures.caltech.edu/I_toc.html>）
> **一句话结论**：本章内容**总体忠实于英文原文、物理结论与数字全部正确**；但 OCR/底本层面存在 **68 处应修问题（高 6 / 中 20 / 低 42）**，均已修正并验证（单章编译 0 error、全书编译 726 页 0 error）；另有一批"译法取舍 / 图源 / 全书字形统一"事项留待上游决策（见 §5）。

---

## 0. 结论速览

| 项目 | 结果 |
|---|---|
| 审查方式 | 5 名审校员分节精读（§1-1 / §1-2 / §1-3 / §1-4 / 结构·图注·编译·数字）+ Lead 逐条复核英文依据后统一修文 |
| 发现问题 | 5 份分报告原始 73 条（含跨报告重复），去重后 **68 个修正点 + 16 条建议/存疑** |
| 严重度 | **高 6**（漏句、重复、物理/化学错误）／**中 20**（句读断裂、术语误译、OCR 错字）／**低 42**（标点、错字、措辞） |
| 已修正 | **68 条全部写入正文**，另清理 12 处全角标点后 OCR 空格、1 处宏间断空格 |
| 单章编译 | xelatex 连编 2 遍：**14 页，0 error / 0 overfull / 0 underfull / 0 Missing character**（5 条无害 warning），与修正前一致 |
| 全书编译 | **726 页，0 error（.log）/ 0 Missing character**；Overfull 2 处（均为既有问题） |
| 结构校验 | label 10/10 唯一、ref 15/15 有定义（修正前 14，新增 1 处指向图 1.7）、0 悬空、0 孤儿；NEW 标记 27/27 配对；环境全部配对；`\uwave` 52 处（维持原计数） |
| 零删改校验 | `tools/verify_chapter.py 1` 由 PASS → **FAIL（预期）**：该脚本是"阅读效率改造零删改"验收，内容修正必然改字；不是内容错误信号（详见 §6.5） |
| 回滚 | `git checkout -- Chapters/VolumeI/Chapter1.tex`（本报告与分报告为新增文件，可单独保留） |

---

## 1. 审查方法与材料

### 1.1 材料

| 材料 | 位置 / 链接 | 用途 |
|---|---|---|
| 中文正文 | `Chapters/VolumeI/Chapter1.tex` | 审查对象；`%<<<NEW … %>>>NEW` 为后加导读层，不计入 OCR 保真问题，但其事实陈述一并核对 |
| 英文原文（本地抓取） | `_attachments/build-feynman/audit/en/I_01.txt`（142 行，每段一行） | 主要逐句对照底本 |
| 英文官网 | <https://www.feynmanlectures.caltech.edu/I_01.html>、<https://www.feynmanlectures.caltech.edu/I_toc.html> | 图注、章节归属、措辞核对（直连被 Cloudflare 拦截，经文本代理取回） |
| 图件 | `Figures/VolumeI/Chapter1/*.pdf`（10 张） | `pdftoppm` 渲染 + `read_image` 目视核对，`pdftotext` 提取图内文字 |
| 编译入口 | `preview/chapter-1/check.tex` | 单章编译验证 |

### 1.2 流程

1. 按英文段落把中文正文逐段对齐（中文分段更细，来自阅读效率改造的切分，切口不算错误）；
2. 逐句比对语义：OCR 错字/漏字/漏句/重复、标点断裂、数字与量纲、术语与物理/化学事实；
3. 数字、图号、图注、label/ref 由结构审校员独立核对；
4. 5 份分报告汇总后，**Lead 逐条回到英文原文复核**（不盲信分报告），对存疑项区分"源译本误译 / OCR 讹变 / 译法取舍"，再决定是否改动；
5. 68 条修正写成带断言的脚本（每条锚点必须恰好命中 1 次）统一执行，随后编译 + 渲染抽查。

### 1.3 分工与分报告

| 审校员 | 范围 | 分报告 |
|---|---|---|
| reviewer-s1 | §1-1 引言（L22–88，含章首导读 L3–20 事实核对） | [section-1.md](chapter-1-review/section-1.md) |
| reviewer-s2 | §1-2 物质是原子构成的（L89–223，4 图 + NEW 概念图） | [section-2.md](chapter-1-review/section-2.md) |
| reviewer-s3 | §1-3 原子过程（L224–304，3 图） | [section-3.md](chapter-1-review/section-3.md) |
| reviewer-s4 | §1-4 化学反应（L305–386，3 图 + 选读块） | [section-4.md](chapter-1-review/section-4.md) |
| reviewer-struct | 全章结构 / 图注 / 编译 / 数字一致性 | [structure.md](chapter-1-review/structure.md) |
| Lead | 汇总裁定、复核英文依据、执行修正、编译验证 | 本报告 |

> 工作约定（问题分类、严重度定义、报告格式）见 [chapter-1-review/00-conventions.md](chapter-1-review/00-conventions.md)。

---

## 2. 高严重度问题（6 条，已全部修正）

| # | 行号 | 问题 | 英文依据 | 修正后 |
|---|---|---|---|---|
| H1 | L135 | "在通常的气压下**在整个房间里只有少数几个分子**"——照字面是物理错误（一个房间约含 10²⁶ 个分子）；且"三个以上"与下句"两个半或三个"矛盾 | "at ordinary atmospheric pressure there certainly would not be as many as three water molecules **in this figure**" | "在通常的气压下，这样一张图里不会有三个水分子那么多。" |
| H2 | L249 | "**杯盖上的**可能已放了二十年的水"——把"一杯盖着盖子的水"误译成"水在杯盖上"，比喻的物理场景错位 | "a glass of water with a cover, that has been sitting there for perhaps twenty years" | "——一杯盖着盖子、可能已在那里放了二十年的水——" |
| H3 | L268 | **漏译整句** "Figure 1–7 is an illustration of the three-dimensional structure of common salt, sodium chloride."；导致图 1.7 的 label 全文 0 次被引用（孤儿图）、正文从未提图 1.7 | 同左 | 句末补："图\ref{figure:食盐的晶体结构}是普通食盐——氯化钠——的三维结构图。" |
| H4 | L273 | **OCR 复读**：同句内"所有的离子都由于电的作用而吸引在一起"出现两次；第二处本应译出原因从句（水的负氧端、正氢端对离子的引力），属重复 + 漏译 | "…but when we put the salt into water, we find, **because of the attractions of the negative oxygen and positive hydrogen for the ions**, that some of the ions jiggle loose." | "……但是当我们把食盐投到水里后，就会发现，由于带负电的氧和带正电的氢对离子的引力，有一些离子离散了。" |
| H5 | L343 | **化学事实错误**："在某处有**两个碳原子与一个氧原子**联结在一起"——英文为"一个氢和两个碳" | "it consists of **one hydrogen and two carbons** tied on here" | "在某处有一个氢原子和两个碳原子联结在一起" |
| H6 | L373 | **整句漏译**："…而是制造出一种处处都不相同的排列——不同种类的原子以多种方式排列着，不断变化、从不重复——"整句缺失，假设句因此没有主句，费曼"重复的原子 vs 处处不同的原子"这一关键对照消失 | "If instead of arranging the atoms …, **we make an arrangement which is always different from place to place, with different kinds of atoms arranged in many ways, continually changing, not repeating**, how much more marvelously…" | 全句补译并理顺（详见 §7 条目 4-15） |

---

## 3. 中严重度问题（20 条，已全部修正）

| 行号 | 问题（摘要） | 处置 |
|---|---|---|
| L46 | "科学的原则——或者简直可称为科学的定义为："破折号括注未闭合、缺谓语框架；almost 误作"简直" | 改为"科学的原则——几乎可以说就是科学的定义——是下面这句话：" |
| L46 | "从某种意义上说，实验为我们提供了种种线索，因此可以说……"倒置了 in the sense that 的主从关系 | 改为"实验本身也帮助产生这些定律，因为它向我们提供了种种线索。" |
| L53 | "First, in a trivial way"译成"通常是"；"these things are easily fixed"译成"容易确定的" | 改为"首先，是在无关紧要的方面：假如仪器上有了毛病而你没有注意到；但是这类问题容易修好……" |
| L57 | **"告诉情况"→"高速情况"**（本段唯一明显 OCR 错字） | 已改 |
| L57/L67 | **"质量守恒定律"→"质量不变定律"**（constant-mass law ≠ conservation of mass，两处同错） | 已改 |
| L94 | 原子假说引句在"运动着"后用句号截断，后半句"当彼此略微离开时……"成为残句 | 句号改逗号，`\keyidea` 收在"运动着，"后，句子合为完整一句 |
| L106 | "…而没有任何其他东西**并且**即使我们…"两句无标点粘连；"大房间**那大**"漏"么" | 补句号；"那么大" |
| L123 | "这些粒子也不是**挤到一块儿**"——原意是"不能彼此挤穿（互不可入）" | 改为"这些粒子也不会彼此挤穿" |
| L180 | "（所有教科书中都有这种图）**一个配有活塞的汽缸**，由于…"同位语被直接粘连，读不通 | 改为"（……），即一个配有活塞的汽缸。由于……" |
| L198 | "抓住一根**冰棍**的一端……阻止我们把它**拉出去**"——a needle of ice 是"冰针"，resists our pushing it aside 是"阻止把它推到一边" | 改为"拿住一根冰针的一端……阻止我们把它推到一边去" |
| L204 | "**敞形**结构则会**倒坍**"——敞开结构（open structure）；两字形近误写/搭配不当 | 改为"敞开结构则会倒塌" |
| L219 | NEW 小结把"氦例外"挂在"振动"上（正文明确氦在绝对零度仍有运动），例外的正确内容是"不凝固" | 改为"绝对零度时原子仍在振动（氦即使在绝对零度也不凝固）。" |
| L251 | "归根到底'没有任何事情发生'如果现在…"引号后缺句号、"归根到底"后缺逗号，两句粘连 | 补"，"与"。" |
| L284 | NEW 读图提示"大球为氯离子、小球为钠离子"与图 1.7 不符：图中两色球**近似等径**（实测直径 40 vs 45 px），靠**实心/空心**区分（表头 ●=Na、○=Cl） | 改为"实心球为钠离子、空心球为氯离子" |
| L341 | "链的**第二个端点**的碳上有一个氧原子"——second from the end 是"倒数第二个" | 改为"链上倒数第二个碳原子上有一个氧原子" |
| L352 | 化学名"4(2, 2, 3, 6-四甲基…)…"在定位号 4 后缺连字符（其余位次/数字与英文逐字符一致） | 改为"4-(2, 2, 3, 6-四甲基-5-环己烯基)-3-丁烯-2-酮" |
| L373 | "**向**紫罗兰香气那样复杂的东西"（向→像）；"排列**的**非常复杂"（的→得） | 已改（并入 H6 全句重写） |
| L373 | "这些波浪**冲向水泥堤岸**时会……**奇妙的浪花**"——原文是"水流过水泥地面时发出哗哗声、形成奇妙花纹"；"一流溪水永远只能是一堆原子"漏译"all the life of a stream of water" | 已按英文重写该句（详见 §7 条目 4-14） |
| L133 | "如果继续加热**到**分子间的引力不足以将彼此拉住**时**"句式杂糅；"not enough to hold them together"漏"把它们" | 改为"如果继续加热，直到分子间的引力不足以把它们彼此拉住时……" |
| L94 | 引句"所有的物体都是**用**原子构成的"——中译本通行为"由原子构成"（豆瓣原文摘录等均作"由"），OCR 由→用 | 改为"由原子构成" |

> 说明：上表 20 条为"中"级；其中 L94 的"用/由"在分报告中被列为存疑（网络上有两种写法），Lead 依据公开中译本原文摘录与搭配习惯定为 OCR 讹字并修正。

---

## 4. 低严重度问题（42 条，已全部修正）

低级别修正以 **OCR 错字/漏字、标点断裂、术语不精确**为主，全部条目见 §7 明细表。典型情形：

- **半角标点残留**：L26 "困难的**.**。"（成品 PDF 中可见"困难的.。"）；
- **全角标点后多余空格 12 处**（L26×2、L31、L46、L94×2、L133、L198、L258、L273、L292、L371）+ L371 两个 `\uwave` 之间的 1 处宏间空格；
- **形近错字**：L204 敞**形**→敞**开**、L211 不**致于**→不**至于**、L55 **著**→**着**、L48 想**像**→想**象**、L367 大得多的**的**→大得多的、L375 **如何**→**何等**；
- **术语不精确**：L72 正确性→精确度、L72/L74 适应→衔接/嵌入、L202 "一种六边形的对称性"→"对称性中有一部分是六边形的"、L204 许多→大多数、L209 "在适当的位置"→"在原地"、L337 简单而对称→笔直而对称、L337 原子队列→原子排列、L369 "秒以下"→"几角秒以内"、L315 "很典型的特征"→"极其奇特的特征之一"、L26/L74 map-or-outline 与 L116 almost schematically 等漏译补偿；
- **句读/标点**：L184 逗号→分号、L186 逗号→句号、L320 缺句号、L326 段末缺句号、L343 陈述句误用问号；
- **排版/格式**：L131 `$ 10^{-8} $` 数学空格、`\r{A}` 与字面 Å 混用（统一为字面 Å）、L135 `105°3'` 的 ASCII 撇号→角分符号（$105^{\circ}3'$）、NEW 概念图"直径约 1/4 英寸"→"约 1/4 英寸见方"（原文 on the side）。

---

## 5. 未改动项、存疑与建议（交上游决策）

### 5.1 图与版式（未改动）

1. **图 1.7 图内数据表**：图内含"岩盐/钾钠盐/AgCl/MgO/方铅矿…"数据表，本章正文完全未涉及；且"**钾钠盐**"（KCl）应为"**钾石盐**"（sylvite）。属图源重绘问题，需重制图或图注说明。
2. **图 1.10 缩放过小**：图源 271×145 pt 按 `width=0.4\textwidth` 排入约 64 mm，图内原子符号仅约 5–6 pt；建议提到 0.5–0.55\textwidth（wrapfigure 宽度同步调整）。本次未动版式，避免改变页数。
3. **图注偏简**：图 1.3 图注"汽缸"可改"配有活塞的汽缸"（与 label、英文正文一致）；图 1.7 图注可补"三维/氯化钠"。eFLP 网页 Figure 1–1…1–9 本身为 `caption empty`（图注在图内/无独立文字），故中文简短图名**不算错误**，仅建议。
4. **图 1–2 的 wrapfigure 位置**比英文原书提前一段（英文在"热运动"段之后、"水蒸气"段之前；中文排在"原子半径"段前）。排版差异，未动。
5. **脚注缺失**：英文 diamond 处脚注 "One can burn a diamond in air." 本章无对应脚注（项目系统性省略脚注）；未补。

### 5.2 译法存疑（未改，保留中译本风格）

- L315 "saturated and happy"译"饱和的、**适宜的**分子"（拟人语气减弱）；
- L345 "For about twenty years"译"大约在20年前"（宜作"近二十年来"）；
- L337/L343 "detective work"译"探索工作"（原文侦探比喻弱化）；
- L326 结尾由英文单数"这一小块物质"泛化为复数；
- L26 章首 "to help **us** develop a ‘feel’"译"有助于**你们**……产生一种切身的感受"；
- L44 "unlearn"译"抛弃以前的谬见"（语义偏重，但可读）。

### 5.3 全书层面（不应单章处理）

- **旧字形统一**：本章仍用"图象"×10、"画象"×2、"象……这样"×3（1986 年前字形），而全书多数章节已用"图像/画像"；建议全书统一（本次未动，以免单章割裂）。
- **`\r{A}` vs 字面 Å**：已在本章统一为字面 Å，建议全书同口径。
- **1963 初版 vs 新千年版**：L135 原句与 1963 初版措辞一致（"整个房间"的说法的确困扰过读者），本次按物理正确性 + 新千年版修正；若项目以 1963 初版为底本，建议在图注/勘误表中记一笔。
- **阅读效率指标**：L373 补译后为 280 字，使本章 ">250 字段落" 由 0 变 1（原改造指标为 0）；如需维持指标，可在"……那么事情会变得更加不可思议吗？"后分段（内容零改动）。
- **NEW 概念图第三格"原子核"**（10⁻¹³ cm）超出本章正文内容，`\figsource` 已注明"按通行数量级绘制，非原书插图"，保留。

---

## 6. 验证记录

### 6.1 单章编译（修正后）

```bash
cd Feynman-Lectures-Latex/preview/chapter-1
rm -rf build && mkdir -p build
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex   # 第 1 遍
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex   # 第 2 遍
```

| 指标 | 修正前（基线） | 修正后 |
|---|---|---|
| `!` 级 error（`.log`） | 0 | **0** |
| 页数 | 14 | **14** |
| Overfull / Underfull | 0 / 0 | **0 / 0** |
| Missing character | 0 | **0** |
| 未定义引用 | 0（两遍后） | **0** |
| warning | 5（无害） | **5（无害）** |

5 条 warning 与基线完全相同（包裹路径、hyperref 选项、xeCJK 字体重定义、黑体字形替换 ×2），均无害。终端里 `! I can't find file 'SimSun'` 是 `\IfFontExistsTF{SimSun}` 触发 kpathsea→mktextfm→mf 的**字体探测子进程噪音**（不写入 `.log`、不影响退出码）；本机无 SimSun 时正确回退 Songti SC（PDF 嵌入 STSongti-SC）。

### 6.2 结构静态校验（修正后）

| 检查项 | 结果 |
|---|---|
| `\label` | 10 个，全库唯一，无重复 |
| `\ref` | 15 次（修正前 14），全部有定义，**0 悬空** |
| 孤儿 label | **0**（图 1.7 已补引用） |
| `%<<<NEW` / `%>>>NEW` | 27 对，顺序正确 |
| 环境配对 | wrapfigure 9/9、itemize 8/8、enumerate 1/1、summarybox 4/4、conceptmap 1/1、tikzpicture 1/1、optional 1/1、figure 1/1 |
| 宏计数 | `\uwave` 52（与原 52 一致）、`\keyidea` 5、`\runin` 8、`\fighint` 2 |
| 残留 OCR 痕迹 | 半角句点 `.。` 0；全角标点前后空格 0；`\r{A}` 0；`°3'` 0 |

### 6.3 渲染抽查（`pdftotext build/check.pdf`）

已确认修正后的版面文本正确出现：`一个氢原子和两个碳原子`、`图1.7是普通食盐——氯化钠——的三维结构图`、`105◦3′`、`1Å / 1～2Å / 0.957Å`、`实心球为钠离子`、`一杯盖着盖子`、`处处都不相同`、`高速情况`、`地图或轮廓`、`质量不变`、`冰针`、`约 1/4 英寸见方`。

### 6.4 全书编译（修正后）

```bash
# 注意：既有 build.sh 未把 styles/readability.sty 复制进编译工作区，首次需手动补（本地忽略目录）
cp styles/readability.sty _attachments/build-feynman/
bash _attachments/build-feynman/build.sh
```

| 指标 | 结果 |
|---|---|
| 页数 | **726**（与 docs/README 记载的全书 726 页一致） |
| `.log` 中 `!` error | **0** |
| Missing character | **0** |
| Overfull | 2 处（1.36 pt vbox + 5.0 pt hbox，均为既有问题，见 `docs/analysis/typography/03-全书试编译报告.md`、`_attachments/build-feynman/校对报告.md`） |

### 6.5 零删改校验：PASS → FAIL（预期，非错误）

```text
$ python3 tools/verify_chapter.py 1
[FAIL] Chapter1: 内容字符不一致
       原文长度 11317，改造后 11424，首个差异位置 222
       原文字符 '说' vs 改造字符 '，'
```

说明：`verify_chapter.py` 服务于"阅读效率改造（零删改）"验收——它把当前正文与 `main` 分支的 OCR 原文逐字符比对。**内容审查修正必然改字**，因此该检查从 PASS 变为 FAIL 是预期行为，不代表内容错误。`docs/analysis/chapter-1-notes.md` 的"零删改 PASS"结论仅对该改造任务成立，本报告已在其文件头加注说明。

### 6.6 回滚与复现

```bash
# 回滚正文（只回滚正文；本报告目录可保留）
git checkout -- Chapters/VolumeI/Chapter1.tex

# 复核本报告的 68 处修正
git diff --stat                      # 49 行、约 180 处字符级改动
git diff -U0 Chapters/VolumeI/Chapter1.tex
```

---

## 7. 修正明细（68 条）


### §1-1 引言

| 编号 | 行号 | 严重度 | 类型 | 修正前（节选） | 修正后（节选） | 依据 |
|---|---|---|---|---|---|---|
| 1-01 | L26 | 低 | 标点 | 颇为困难的.。因此 | 颇为困难的。因此 | OCR 半角句点残留 |
| 1-02 | L26 | 低 | 空格 | 加以浓缩。 这就是说 | 加以浓缩。这就是 | 标点后空格 |
| 1-03 | L26 | 低 | 空格 | \uwave{定律}。 不过 | \uwave{定律}。不过 | 标点后空格 |
| 1-04 | L26 | 低 | 漏译 | 还没有一个大致的了解之前 | 还没有一张地图或轮廓之前 | map or outline 漏译 |
| 1-05 | L31 | 低 | 空格 | 基本定律， 然后 | 基本定律，然后 | 标点后空格 |
| 1-06 | L46 | 中 | 句读/误译 | 科学的原则——或者简直可称为科学的定义为： | 科学的原则——几乎可以说就是科学的定义——是下面这句话： | The principle of science, the definition, almost, is the following: |
| 1-07 | L46 | 低 | 空格 | \uwave{鉴定者}。 但是 | \uwave{鉴定者}。但是 | 标点后空格 |
| 1-08 | L46 | 中 | 误译 | 从某种意义上说，实验为我们提供了种种线索，因此可以说是实验本身促成了这些定律的产… | 实验本身也帮助产生这些定律，因为它向我们提供了种种线索。 | Experiment, itself, helps to produce these laws, in the sense that it gives us hints. |
| 1-09 | L48 | 低 | 术语 | 作出重大的判断 | 作出伟大的概括 | the great generalizations |
| 1-10 | L48 | 低 | 错字 | 这个想像过程 | 这个想象过程 | 用字统一：想象 |
| 1-11 | L53 | 中 | 句读/误译 | 首先，通常是：仪器上有些毛病，而你又没有注意，但是这种问题是容易确定的，可以反复… | 首先，是在无关紧要的方面：假如仪器上有了毛病而你没有注意到；但是这类问题容易修好… | First, in a trivial way ... these things are easily fixed |
| 1-12 | L55 | 低 | 错字 | 随著速度的加大而增加 | 随着速度的加大而增加 | 繁体/异体字 |
| 1-13 | L57 | 中 | OCR错字 | 但是对于告诉情况这就不正确了 | 但是对于高速情况这就不正确了 | OCR：告诉↔高速（But for high speeds we are wrong） |
| 1-14 | L57 | 中 | 物理术语 | 而用简单的质量守恒定律作为一种很好的近似 | 而用简单的质量不变定律作为一种很好的近似 | constant-mass law ≠ conservation of mass |
| 1-15 | L67 | 中 | 物理术语 | 先教简单的“质量守恒”定律 | 先教简单的“质量不变”定律 | 同上 |
| 1-16 | L72 | 低 | 术语 | 它的正确性如何，它怎样适应其他的各种事情 | 它的精确度如何，它怎样与其余的一切相衔接 | how accurate it is / how it fits into everything else |
| 1-17 | L72 | 低 | 术语 | 比较奇特和比较有趣 | 比较奇妙，也比较有趣 | more wonderful, and more fun |
| 1-18 | L74 | 低 | 漏译 | 的轮廓继续讲下去 | 的轮廓（或者说总图）继续讲下去 | our outline, or general map |
| 1-19 | L74 | 低 | 术语 | 它们又是怎样适应整体结构的 | 它们又是怎样嵌入整体结构的 | how it fits into the big structure |

### §1-2 物质是原子构成的

| 编号 | 行号 | 严重度 | 类型 | 修正前（节选） | 修正后（节选） | 依据 |
|---|---|---|---|---|---|---|
| 2-01 | L94 | 低 | OCR错字 | 所有的物体都是用原子构成的 | 所有的物体都是由原子构成的 | 中译本原文“由原子构成”；OCR 由→用 |
| 2-02 | L94 | 中 | 标点 | 运动着。} 当彼此略微离开时相互吸引， 当彼此过于挤紧时又互相排斥。 | 运动着，}当彼此略微离开时相互吸引，当彼此过于挤紧时又互相排斥。 | 英文为同一句；句号切断、空格残留 |
| 2-03 | L106 | 中 | 标点 | 而没有任何其他东西并且即使我们 | 而没有任何其他东西。即使我们 | 英文为两句（…water. Even if we magnify…） |
| 2-04 | L106 | 中 | 漏字 | 相当于一个大房间那大） | 相当于一个大房间那么大） | 漏字“么” |
| 2-05 | L116 | 低 | 漏译 | 把它们都画成二维的排列 | 把它们几乎按示意图的方式画成二维排列 | sketched almost schematically |
| 2-06 | L123 | 中 | 误译 | 这些粒子也不是挤到一块儿 | 这些粒子也不会彼此挤穿 | do not squeeze through each other |
| 2-07 | L131 | 低 | 错字/排版 | $ 10^{-8} $厘米现在称为1Å | $10^{-8}$厘米称为1Å | Now 为语气词；数学环境空格 |
| 2-08 | L133 | 低 | 误译 | 它们并没有飞逝 | 它们并没有飞散 | things do not just fly apart |
| 2-09 | L133 | 中 | 句法/标点 | 如果继续加热到分子间的引力不足以将彼此拉住时 | 如果继续加热，直到分子间的引力不足以把它们彼此拉住时 | if the heating continues there comes a time when… |
| 2-10 | L135 | 高 | 物理/数字 | 这张水蒸气图象有一个不足之处：在通常的气压下在整个房间里只有少数几个分子，决不可… | 这张水蒸气图象有一个不足之处：在通常的气压下，这样一张图里不会有三个水分子那么多… | at ordinary atmospheric pressure there certainly would not be as many as three water molecules in this figure |
| 2-11 | L180 | 中 | 标点 | （所有教科书中都有这种图）一个配有活塞的汽缸，由于不论水分子的形状如何，情况都是… | （所有教科书中都有这种图），即一个配有活塞的汽缸。由于不论水分子的形状如何，情况… | a cylinder with a piston in it（同位语被粘连） |
| 2-12 | L184 | 低 | 标点 | 碰撞的次数也将增加一倍，由于每次碰撞仍然和先前那样“有力”，压力就正比于密度。 | 碰撞的次数也将增加一倍；而且由于每次碰撞仍然和先前那样“有力”，压力就正比于密度… | 英文逗号＋and since 分句 |
| 2-13 | L186 | 低 | 标点 | 因此压力将增加，你们看，原子理论的概念是多么简单！ | 因此压力将增加。你们看，原子理论的概念是多么简单！ | 英文为两句 |
| 2-14 | L198 | 中 | 误译 | 如果我们抓住一根冰棍的一端，另一端就会阻止我们把它拉出去。 | 如果我们拿住一根冰针的一端，另一端就会阻止我们把它推到一边去。 | a needle of ice / resists our pushing it aside |
| 2-15 | L200 | 低 | 句法 | 取决于晶体另一端的与之相距千百万个原子的排列位置。 | 取决于晶体另一端与之相隔千百万个原子的那些原子的位置。 | 句法杂糅 |
| 2-16 | L202 | 低 | 术语统一 | 冰融解时会缩小 | 冰熔解时会缩小 | 术语统一（熔解） |
| 2-17 | L202 | 低 | 漏译 | 正确的特征之一是这里具有一种六边形的对称性 | 其正确的特征之一是：这里所呈现的对称性中有一部分是六边形的 | there is a part of the symmetry that is hexagonal |
| 2-18 | L204 | 低 | 术语 | 许多简单的物质在融解时都要膨胀 | 大多数简单的物质在熔解时都要膨胀 | Most simple substances |
| 2-19 | L204 | 中 | OCR错字 | 但是敞形结构则会倒坍 | 但是敞开结构则会倒塌 | OCR：敞形↔敞开；an open structure collapses |
| 2-20 | L209 | 低 | 误译 | 所有的原子仍都“在适当的位置”上振动 | 所有的原子仍都“在原地”振动 | vibrating “in place” |
| 2-21 | L211 | 低 | 错字 | 使之不致于凝固 | 使之不至于凝固 | 形近误写 |
| 2-22 | L219 | 中 | NEW块 | 绝对零度时原子仍在振动，氦除外。 | 绝对零度时原子仍在振动（氦即使在绝对零度也不凝固）。 | NEW 小结把“例外”挂错对象 |

### §1-3 原子过程

| 编号 | 行号 | 严重度 | 类型 | 修正前（节选） | 修正后（节选） | 依据 |
|---|---|---|---|---|---|---|
| 3-01 | L249 | 高 | 误译 | ——杯盖上的可能已放了二十年的水—— | ——一杯盖着盖子、可能已在那里放了二十年的水—— | a glass of water with a cover |
| 3-02 | L251 | 中 | 标点 | 归根到底“没有任何事情发生”如果现在 | 归根到底，“没有任何事情发生”。如果现在 | 缺逗号/句号，两句粘连 |
| 3-03 | L258 | 低 | 空格 | 回到水面时， 则产生了热量 | 回到水面时，则产生了热量 | 标点后空格 |
| 3-04 | L268 | 高 | 漏句 | 并且是“食盐原子”的有规则的排列。 | 并且是“食盐原子”的有规则的排列。图\ref{figure:食盐的晶体结构}是普… | 漏译：Figure 1–7 is an illustration of the three-dimensional structure of common salt, sodium chloride. |
| 3-05 | L273 | 高 | 重复+漏译 | 就会发现，所有的离子都由于电的作用而吸引在一起，有一些离子离散了。 | 就会发现，由于带负电的氧和带正电的氢对离子的引力，有一些离子离散了。 | OCR 复读＋漏译 because of the attractions of the negative oxygen and positive hydrogen |
| 3-06 | L284 | 中 | NEW块/图文 | 大球为氯离子、小球为钠离子 | 实心球为钠离子、空心球为氯离子 | 图1-7 两色球等径，实心=Na、空心=Cl |
| 3-07 | L292 | 低 | 空格 | 更易溶解， 但是某些物质 | 更易溶解，但是某些物质 | 标点后空格 |
| 3-08 | L273 | 低 | 空格 | 严格地说， 这种晶体 | 严格地说，这种晶体 | 标点后空格 |

### §1-4 化学反应

| 编号 | 行号 | 严重度 | 类型 | 修正前（节选） | 修正后（节选） | 依据 |
|---|---|---|---|---|---|---|
| 4-01 | L315 | 低 | 术语 | 这是此类原子过程的一个很典型的特征。 | 这是这类原子过程极其奇特的特征之一。 | one of the very peculiar characteristics |
| 4-02 | L320 | 低 | 标点 | 也可以是金刚石）现在，比如说 | 也可以是金刚石）。现在，比如说 | 缺句号 |
| 4-04 | L326 | 低 | 标点 | 到达人的鼻子中了 | 到达人的鼻子中了。 | 段末缺句号 |
| 4-05 | L337 | 低 | 术语 | 二氧化碳分子的结构是简单而对称的 | 二氧化碳分子的结构是笔直而对称的 | the carbon dioxide molecule is straight and symmetrical |
| 4-06 | L337 | 低 | 误译 | 那些非常复杂的原子队列 | 那些非常复杂的原子排列 | arrangements of atoms |
| 4-07 | L339 | 低 | 漏译 | 是空气中紫罗兰香气图。 | 画的是紫罗兰附近的空气。 | a picture of the air in the neighborhood of a violet |
| 4-08 | L341 | 中 | 误译 | 链的第二个端点的碳上有一个氧原子 | 链上倒数第二个碳原子上有一个氧原子 | with an oxygen second from the end |
| 4-09 | L343 | 高 | 物理错误 | 在某处有两个碳原子与一个氧原子联结在一起 | 在某处有一个氢原子和两个碳原子联结在一起 | it consists of one hydrogen and two carbons |
| 4-10 | L343 | 低 | 标点 | 混合后究竟会发生什么事？ | 混合后究竟会发生什么事。 | 英文为陈述句 |
| 4-11 | L352 | 中 | 化学名 | 名称是4(2, 2, 3, 6-四甲基 | 名称是4-(2, 2, 3, 6-四甲基 | 化学名缺连字符 |
| 4-12 | L367 | 低 | 多字 | 看到大得多的的东西 | 看到大得多的东西 | 重复“的” |
| 4-13 | L369 | 低 | 单位 | 角度之差在秒以下 | 角度之差在几角秒以内 | within seconds of arc（角秒） |
| 4-14 | L373 | 中 | 误译 | 如果水——它只不过是些小滴，地球上到处都有——可以形成波浪和泡沫，那这些波浪冲向… | 如果水——它只不过是这些小小的团块，在地球上一英里接一英里地绵延——可以形成波浪… | nothing but these little blobs, mile upon mile of the same thing over the earth; make rushing noises and strange patterns as it runs over cement; all the life of a stream of water; how much more is possible? |
| 4-15 | L373 | 高 | 漏译+错字 | 假设我们不是把原子排成确定的形式，再三重复，不断反复，或者甚至形成向紫罗兰香气那… | 假设我们不是把原子排成某种确定的形式，再三重复、不断反复，或者甚至形成像紫罗兰香… | 整句漏译 we make an arrangement which is always different from place to place…；向→像；排列的→排列得；staggers the imagination |
| 4-16 | L375 | 低 | OCR错字 | 将会具有如何丰富和生动的内容！ | 将会具有何等丰富和生动的内容！ | OCR：如何↔何等 |

### 结构/排版补充

| 编号 | 行号 | 严重度 | 类型 | 修正前（节选） | 修正后（节选） | 依据 |
|---|---|---|---|---|---|---|
| 5-01 | L131 | 低 | 排版 | 半径为$1\sim2$\r{A} | 半径为$1\sim2$Å | 统一 Å 写法（全库用字面 Å） |
| 5-02 | L163 | 低 | 排版 | $1\sim2$\,\r{A} | $1\sim2$\,Å | 统一 Å 写法（概念图） |
| 5-03 | L135 | 低 | 排版 | 这个角是105°3' | 这个角是$105^{\circ}3'$ | ASCII 撇号→角分符号（105∘3′） |
| 5-04 | L161 | 低 | NEW块精度 | 直径约 1/4 英寸 | 约 1/4 英寸见方 | 英文 a quarter of an inch on the side（不是直径） |

---

## 8. 相关文件

| 文件 | 说明 |
|---|---|
| [chapter-1-review/00-conventions.md](chapter-1-review/00-conventions.md) | 审校工作约定（分类/严重度/格式/纪律） |
| [chapter-1-review/section-1.md](chapter-1-review/section-1.md) | §1-1 分报告（14 条 + 7 存疑） |
| [chapter-1-review/section-2.md](chapter-1-review/section-2.md) | §1-2 分报告（21 条 + 8 存疑） |
| [chapter-1-review/section-3.md](chapter-1-review/section-3.md) | §1-3 分报告（6 条 + 6 存疑） |
| [chapter-1-review/section-4.md](chapter-1-review/section-4.md) | §1-4 分报告（22 条 + 9 存疑） |
| [chapter-1-review/structure.md](chapter-1-review/structure.md) | 结构/图注/编译/数字专项审计（10 条 + 6 存疑） |
| `Chapters/VolumeI/Chapter1.tex` | 已修正正文（`git diff` 可逐行复核） |
