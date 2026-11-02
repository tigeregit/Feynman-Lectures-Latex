# 第 33 章《偏振》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter33.tex`（205 行；7 节 33-1～33-7，9 幅图 33.1–33.9）
- 英文：`_attachments/build-feynman/audit/en/I_33.txt`（33–1～33–7；抓取文本中公式为分式碎片，段首词可查）
- 旁证：`_attachments/reference/zh/Chapter33.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch33-candidates.md`（236 小块 + 33 大块，已逐类核对）
- 公式核对方式：eFLP 文本片段 + 中译本旁证逐式比对

## 结果

- **已修正 5 条（5 处；中 1、低 4）**；**存疑 3 项**（未改）。
- 单章编译：**12 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter33.tex`（5 行，**CRLF 换行保持原状**）、`preview/chapter-33/check.tex`（仅注释：章名改《偏振》、`cd` 路径改 chapter-33、通过标准补 underfull/undefined ref）、本报告。本章**无跨章引用**（无需硬编码/xr）。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L91 | "此合电场对于$y$轴（即原来的**辐射方向**）稍稍倾斜了一点"——$y$ 轴是入射光原来的**偏振方向**，不是辐射方向 | "tilted slightly with respect to the y-axis, the original direction of polarization"（I_33 L98） | "（即原来的偏振方向）" |

## 低严重度修正（已修）

- L41："玻璃纸…**各向不同性**" → "**各向异性**"（"各向不同性"非标准词；英文 "is not isotropic"；且与 L64"各向异性物质"统一）。
- L179："冰洲石晶体（**CaCO3**）" → "（**$\mathrm{CaCO_3}$**）"（化学式下标；英文 CaCO3）。
- L120："产生振幅为**-1**的波" → "振幅为**$-1$**的波"（负号未入数学体，与同段"振幅为$-1$的场"不一致）。
- L25："复数电矢量的实部与虚部和场的**x坐标与y坐标**混淆" → "场的**$x$坐标与$y$坐标**"（变量未用数学体；后一句同词已用数学体）。

## 存疑项（未改）

1. **L60**"设想有一种由长形非对称分子组成的液体，**让在近分子的两端**带有正或负的平均电荷" ← "a liquid composed of long asymmetric molecules which carry a plus or minus average charge near the ends of the molecule"：句子缺主语、读来拗口；底本如此，未改（建议"这些分子在靠近两端处带有…"）。
2. **L33**"考察沿$90^\circ$角散射的光" ← "light scattered at 90°"：宜作"成 $90^\circ$ 角散射的光"；底本如此，未改。
3. **L64**"偏振片系由碘硫酸奎宁小晶体…当振动沿别的方向时，则**吸收不明显**" ← "…do not absorb appreciably"：herapathite 通行译名"碘硫酸奎宁"可留；"吸收不明显"稍弱（可作"几乎不吸收"），底本如此，仅标注。

## 覆盖性结论

- **段落/完整性**：7 节与英文 33–1～33–7 一一对应；逐句核对**无漏句、无漏段、无重复粘贴**；候选"大块差异"33 条全部为公式被剥离、图注/页眉错位噪声，无内容缺失。
- **公式**：编号公式 (33.1)–(33.8) 全部存在且逐式与英文一致——33.1 $b/a=B/[A\cos(i+r)]$；33.2 $A\cos(i-r)/a=(-1)/(-1)$；33.3 $B/b=\cos(i+r)/\cos(i-r)$；33.4 $(1-|B|^2)/(1-|b|^2)=|A|^2/|a|^2$；33.5 消元式；33.6 $|b|^2=\sin^2(i-r)/\sin^2(i+r)$；33.7 $|B|^2=\tan^2(i-r)/\tan^2(i+r)$；33.8 $b=-\sin(i-r)/\sin(i+r)$、$B=-\tan(i-r)/\tan(i+r)$；正入射 $B^2=b^2=(n-1)^2/(n+1)^2$——**均正确，本次未改动任何公式内容**。
- **数字/量纲**：$10^{-8}$ s、$90^\circ$、$45^\circ$、$\pi$、$\pi/2$、$n=4/3$、$(1/7)^2\approx2\%$、2% 均与英文一致，无数字错误。
- **图/引用**：9 幅图（33.1–33.9）齐全、图注与英文一致；正文图引用全部经 `\ref` 解析（7/2/12/12 次等），0 未定义、无硬编码图号；图 33.8/33.9 的双栏 `figure` 环境版式正常（已渲染抽检）；本章无表格。
- **人名/术语**：布儒斯特、菲涅耳、惠更斯、斯涅耳、克尔、线/圆/椭圆偏振、寻常/非常光线、光轴、四分之一与半波片、马吕斯定律（$\cos^2\theta$）、克尔盒等均正确；偏振方向、布儒斯特角、菲涅耳反射系数、双折射 o/e 光、旋光性论述逐段核对无误。
- **自动候选差异**：236 小块 + 33 大块绝大多数为公式剥离噪声与参考文本 OCR 讹字（几→儿、叠→谷/全/郊、逆→道、束→东、玻→琉、佯谬→伴廖、净辐→兆辑、绕→线、儒→侍 等），**不据以改动**；确属本仓库的问题即上表 + 低严重度 5 条。

## 验证

- 入口：`preview/chapter-33/check.tex`（`make_chapter_check.py 33` 生成，`\setcounter{chapter}{32}`、`\input{../../Chapters/VolumeI/Chapter33.tex}`；本次仅修正注释）。
- 命令：`cd preview/chapter-33 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：12 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`；PDF 中"??"0 处；公式编号 (33.1)–(33.8) 全部存在。
- PDF 渲染抽查：p8（图 33.6 + 式 33.1）、p9（式 33.2–33.7）、p10（式 33.8、CaCO₃、图 33.7）均正常；修正点均生效（"即原来的偏振方向""各向异性""振幅为 −1""场的 x 坐标与 y 坐标"），旧串（"辐射方向""各向不同性""场的x坐标"）出现 0 次。
