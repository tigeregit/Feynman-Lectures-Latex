# 第 7 章《万有引力理论》审查报告

- 范围：`Chapters/VolumeI/Chapter7.tex`（215 行，8 节）。对照 `_attachments/build-feynman/audit/en/I_07.txt`（168 行；正文 34 段 + 3 条脚注）、官方页 <https://www.feynmanlectures.caltech.edu/I_07.html>；旁证 `_attachments/reference/zh/Chapter7.txt` 与 `ch7-candidates.md`（小块差异 400 条、大块差异 33 条，已逐条判定：多数为参考文本 OCR 噪声或底本译法差异，实际需改者 44 处）。
- 段落对应：中文正文 40 段 ↔ 英文正文 34 段（英文段在中文中拆分：L80→L65/L67/L74；L104→L104/L106/L108；L129→L167/L175；L151→L195/L197），**无整段缺失、无重复粘贴**。
- 结果：**已修 44 处（逐处计：高 3、中 21、低 20），存疑 9 条（不改，交 Lead 复核）**。修改全部为行内替换，未改动行数/结构；已按 CRLF 原格式保存。

## 高/中问题表（行号为修改前行号；均已在同一位置修正）

| 行号 | 问题（原文） | 英文依据（逐字引用） | 修正 |
|---|---|---|---|
|（按问题组列出；"星系/银河系"含 8 处、"切向指向→切向直线"含 2 处字符修改）||||
| L11 | **15 世纪初叶** | "Beginning in the sixteenth century there were great debates" | 16 世纪初叶（Tycho 1546–1601、Copernicus 1543，15 世纪明显错误） |
| L191 | 漏一句：粒子"穿过太阳时被吸收"的机制 | "when the sun is nearby, the particles coming toward the earth through the sun are partially absorbed, so fewer of them are coming from the sun" | 补："……所以这些冲量都互相抵消。但是，如果考虑到太阳在地球附近，那么跑向地球的粒子穿过太阳时要被吸收一部分，所以来自太阳的粒子比来自另一边的粒子要少一些。" |
| L195 | 漏一句：电子两个固有特性 | "We have considered two natural aspects of the same thing, an electron." | 补："……这个数值不是偶然的。我们研究的是同一事物，即电子的两个固有特性。这个大得难以置信的数字是一个自然常数……" |
| L5 | 这个**称述** | "This statement can be expressed mathematically" | 这个陈述 |
| L33 | 轨道的大小**使用**……来量度的 | "the size is measured by the length of the greatest diameter" | 是用 |
| L57 | 第一秒内落下 **4.9 米**（同段后文及全章均用"16 英尺"） | "falls 16 feet in the first second" | 在第一秒内落下 16 英尺（计量单位与全章、原文统一） |
| L74（跨 L67） | 一条……子弹将循之而行的切向**指向** | "the tangential, straight line path that the bullet would take" | 切向直线（"切向直"→"线。"，跨图环境的断句已接顺） |
| L86 | 远的一边的**水波**是"不平衡的" | "The water on the far side is 'unbalanced'" | 水 |
| L94 | **罗末**(Roemer) | "studied very carefully by Rømer" | 罗默(Roemer) |
| L102 | 人们曾**视图**在引力定律的基础上 | "Attempts were made to analyze the motions … on the basis of the law of gravitation" | 试图 |
| L102 | 应处在**那个**位置才能造成 | "They calculated where such a planet would have to be" | 哪个位置 |
| L104 | 这些定律能够**扩展到离我们最近的相对距离较小那几个行星之外**吗？ | "do they extend beyond the relatively small distances of the nearest planets?" | 能够推广到离我们最近的几个行星那样较小的距离之外吗？ |
| L106 | 相对位置所作的**测量** | "Careful measurements of the relative positions" | 所作的仔细测量 |
| L108 | 天狼星 A **不再焦点上** | "the star Sirius A is not at the focus" | 不在焦点上 |
| L104 | 照片没有被**偏转** | "so that we will know that the photograph was not turned" | 照片没有被旋转过 |
| L142、L144 | **银河系**（8 处：某一银河系/这个银河系/这些银河系/银河系团/银河系的形状/一个银河系的规模等） | "look at an entire galaxy … The shape of this galaxy … a cluster of galaxies" | 星系/星系团（galaxy 不是"银河系"；"银河系的旋臂"一并改为"星系的旋臂"） |
| L213 | 尽管牛顿引力定律**创造了所有这些惊人的成就** | "In spite of all the excitement it created, Newton's law … is not correct!" | 尽管牛顿引力定律引起了所有这些轰动（底本误译 excitement） |
| L215 | **大自然的另一方面量子力学**还没推广到万有引力 | "The quantum-mechanical aspects of nature have not yet been carried over to gravitation." | 自然界的量子力学方面还没有推广到引力中去 |

**低 20 处（已修，摘要）**："简单的原理→两个简单的原理"（L9）、"各椭圆的其中一个焦点上→椭圆的一个焦点上"（L36）、"这必定→就必定"（L46）、"等时间→相等时间"（L51）、"而如果，一个→而如果一个"（L57 缺句读）、"小球……可以用→，这可以用"（L67）、"那些→哪些"（L76）、"首先，他分析了月球的运动→他对月球运动的分析就是一个预言"（L76，漏译 prediction）、"迷→谜"（L78）、"太阳，月球和地球→太阳、月球和地球"（L92）、"而在其背后有没有→又没有一个机制"（L189）、"研究了一下→研究一下"（L191）、"错在那里→错在哪里"（L191）、"冲量力→冲量"（L191）、"不致于→不至于"（L191）、"根本没有必要→还没有必要"（L205）、"作绕圆周运动→绕圆周运动"（L207）、"瞬时发生地→瞬时发生的"（L213）、"那一个→哪一个"（L215）、"看看是否牛顿定律→看看牛顿定律"（L215）。

## 存疑项（未改，需 Lead 决定）

1. **L94 脚注与正文**：正文 1676 年正确（eFLP："This was done in 1676."）；脚注作"原文为1656，经查证为1676"——底本脚注更长（"原文误为1656……据考证罗默1676年文中并未估计光速，首次估计为1678年惠更斯"），本仓库有删节。建议补齐或改写脚注，使其与正文/新千年版一致。
2. **L179**："卡文迪什也声言他称了地球，但是他实际测量的是引力定律的系数G。"——eFLP 及官方页无此句（只有 "This experiment has been called 'weighing the earth' by some people…"），底本有；历史无误但比原文多一句，是否删保留由 Lead 定。
3. **L55"非凡触觉"**：底本作"非凡感悟力"（a feeling for generalities）；"触觉"可通但可疑，未改。
4. **L86"最后，我们得到两次潮汐"**：英文 "we get two tidal bulges"（两个潮汐隆起），底本作"两次涨潮"；语义可通，未改。
5. **L102"以致人们从未看到过它"**：英文 "which men had not seen"（非结果关系），"以致"逻辑略偏；底本如此，未改。
6. **象/像类旧写法**（"现像""想像"等）：按手册"全书统一问题，不单章批量改"未动（L94、L184、L193、L195）。
7. **硬编码图号**：图7.1–7.14 共 14 处，实测编译后图注编号与硬编码完全一致（图 7.1…7.14），故未改为 `\ref`（手册仅要求格式不一致时改）。
8. **L17"一束线"（a loop of string）、"平头钉"（tacks）**：底本作"一段线/图钉"，本仓库写法可通，未改。
9. **L11"希恩(Hven)"**：底本译名，未改；L142"甚至对更大的距离引力定律也是正确的"缺逗号，属低，未改。

## 覆盖性结论与核对

- **数字/量纲**逐个核对无误：Kepler 3/2 次方；240,000 英里/27 天；4000 英里/60 倍/1/3600/1/20 英寸；8000 英里/2000 英尺/4.9 米（已改 16 英尺）/5 英里/25000 英里；太阳系 10⁵ 倍、50,000–100,000 光年、8⅓ 光分、几千万光年；1862–1904；1750；1909；1947/7 年；G=6.670×10⁻¹¹ N·m²/kg²；1/(4.17×10⁴²)；10⁻²⁴ s、2×10¹⁰ 年、10⁻⁴²、10⁹ 年、10%、100 °C、10⁻⁹；24 h/12 h；1676（脚注见存疑 1）。
- **人名**：第谷·布拉赫、开普勒、哥白尼、伽利略、牛顿、罗默（已改"罗末"）、亚当斯、勒维耶(Le Verrier)、卡文迪什、加加林、季托夫、厄缶(Eötvös)、迪凯(Dicke)、爱因斯坦——均与 eFLP 一致。
- **公式/记号**：`F=G mm'/r²`、`T²∝a³（T∝a^{3/2}）`、`(16/5280)×8000` 平方根≈5 英里、`\num{4.17d42}`、`\numb{d-24}`、`\numb{2d10}`、`\numb{d-42}`、`\numb{d9}` 编译渲染正常（PDF 实测 4.17×10⁴²、10⁻²⁴、2×10¹⁰、10⁻⁴²、10⁹）。
- **图**：14 张图（wrapfigure 7.1–7.6、双栏 figure 7.7–7.12、7.13、7.14）顺序与正文引用一一对应；图注与 `\ref` 均解析，无缺失引用。
- **无漏段/重复**；脚注 3 条（矢径、切线、证明）齐全，第 4 条为译者注（见存疑 1）。

## 验证（单章编译）

`preview/chapter-7/check.tex`（已建；章号 6、input Chapter7.tex；顺手把注释里的章名/路径"第 7 章《基本物理》/cd preview/chapter-2"改为《万有引力理论》/chapter-7）：连编 2 遍 → **0 error、0 Overfull、0 Underfull、0 Missing character、0 undefined references；PDF 14 页（A4）**。

## 未改动与建议

- 存疑 1、2、3、4、5 建议 Lead 复核后统一处理；其余存疑 6–9 属全书统一或底本风格，建议保持。
- 修改均为行内替换（27 行受影响），便于 Lead 复核 diff。
