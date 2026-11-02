# 第 10 章《动量守恒》审查报告

- **范围**：`Chapters/VolumeI/Chapter10.tex`（203 行，5 节，42 段）；对照 `_attachments/build-feynman/audit/en/I_10.txt`（正文 L36–229）。
- **旁证**：`_attachments/reference/zh/Chapter10.txt`（公开中译本 OCR，仅用于定位本仓库讹变）、`_attachments/reference/candidates/ch10-candidates.md`（本次生成：小块差异 158 条、大块 28 条，绝大多数是公式/页码/图注噪声，已逐条判定）。
- **段落对应**：中文 42 段 ↔ 英文 42 段，逐段 1:1——§10-1 6:6、§10-2 8:8、§10-3 15:15、§10-4 7:7、§10-5 6:6；无漏段、无漏句、无重复粘贴（仅 L7 英文括注 "—a hundred million billion" 底本未译，见存疑 2）。
- **结果**：问题 16 条（高 1 / 中 8 / 低 7），**已全部修正**；另有存疑 6 项、旁证误判（参考文本自身 OCR 错）若干未计入。修正使用带断言脚本（16 条旧串各恰命中 1 次）执行，`git diff` 仅 12 行变化。
- **单章编译**：`preview/chapter-10/check.tex`（新建，`\setcounter{chapter}{9}` + input Chapter10）连编 2 遍：**0 error、0 overfull、0 underfull、0 missing character、0 undefined references，11 页**。

## 已修问题（行号为修改前 `Chapter10.tex` 行号）

| # | 行号 | 严重度 | 类型 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|---|---|
| 1 | L195 | **高** | 公式 | 速度平方关系记号错位：`$v^2=v^2_x+v^2_y+v^2_z$`（意为 (v²)ₓ…） | "where v2=v2x+v2y+v2z" | `$v^2=v_x^2+v_y^2+v_z^2$` |
| 2 | L5 | 中 | 错字 | "完整的**棚圆**"不成词 | "a perfect ellipse" | 椭圆 |
| 3 | L7 | 中 | 错字 | "如此困难的**占老**的三体问题" | "the old three-body problem" | 古老 |
| 4 | L15 | 中 | 术语/物理 | "总效应是在某个别的**方面**上"（direction 误作 aspect） | "the total effect … is in some other direction" | 方向 |
| 5 | L68 | 中 | 术语/物理 | "伽利略不能用**光滑的东西**来做实验"（sliding things 误译） | "He could not do experiments by sliding things" | 靠让物体滑动 |
| 6 | L161 | 中 | 漏句/漏译 | 漏 "opposite"：只写"速率彼此相等" | "velocities … are equal to and opposite each other" | 速度大小相等、方向相反 |
| 7 | L165 | 中 | 术语/物理 | "齿轮、**转轴**或部件"（wheels 误作 axle） | "gears, wheels, or parts" | 轮子 |
| 8 | L165 | 中 | 术语/物理 | "没有地方可以**消耗**能量"（impounded 误作 consume） | "nowhere for the energy to be impounded" | 储存能量 |
| 9 | L184 | 中 | 标点 | "这里$m_0$**。**是物体的静止质量"（衍句号，底本 m₀ 被 OCR 成 m。的残留） | "where m0 is the mass of the body at rest" | 删句号 |
| 10 | L57 | 低 | LaTeX/结构 | "以速度**v**向左运动"未入数学模式（同句前一个 v 为 `$v$`） | "with a velocity v" | `$v$` |
| 11 | L5 | 低 | 标点 | `$s=…$**,**则更为容易` 半角逗号 | — | 全角逗号 |
| 12 | L29 | 低 | 标点 | `$m_1v_1+m_2v_2$**,**并称为` 半角逗号 | — | 全角逗号 |
| 13 | L29 | 低 | 标点 | `$(m_1v_1+m_2v_2)$**,**即两个动量之和` 半角逗号 | — | 全角逗号 |
| 14 | L5 | 低 | 排版 | `$32ft \cdot s^{-2}$` 数字与单位间缺空格（Ch15/16 同体例用 `~`） | "32 ft/sec²" | `$32~ft \cdot s^{-2}$` |
| 15 | L38 | 低 | LaTeX/结构 | 方程 10.3 省略号作 `...`（全书其余处用 `\cdots`） | "m1v1+m2v2+m3v3+⋯" | `\cdots` |
| 16 | L135 | 低 | 标点 | "相碰撞**，**并结合在一起"（并列动词间衍逗号，参考底本无） | "collides … and sticks together" | 删逗号 |

## 存疑项（未改）

1. **力符号 f/F**：正文 3 处用 `$f$`、`$f_x$`、`$f=ma$`；eFLP 作 F、Fx、F=ma，本卷 Ch9/Ch12 亦用 F。但公开中译本本章 OCR 亦作 f（Ch9 作 F），判为底本记号差异，非错讹，未改（如 Lead 要求全书统一 F 可另行批量处理）。
2. **L7 漏译括注**：英文 "(about 10^17—a hundred million billion)" 的 "—a hundred million billion" 底本即未译；中文数字体系下 10^17 已明确，补译反显生硬，未补。
3. **L7 "气体、木块、铁块"**：英文仅 "a gas or a block of iron"，"木块"为底本增补举例，未删。
4. **L101 "我们从两个质量相等……将静止不动出发"**：对应 "We start with the knowledge that…"，底本语序拗口但可解，未重写。
5. **L59 "在两种铝的数量之间"**：对应 "some right amount in between"，底本表述略拗，未改。
6. **L68 "将两个滑块静止置放在槽的中心"**：拟作"静止地置放"更顺，属风格问题，未改。

## 覆盖性结论

- **完整性**：中英 42 段逐句核对，无整段/整句缺失或重复；唯 L7 一处英文括注底本未译（存疑 2）。
- **数字/公式核对**：32 ft/s²、s=s₀+v₀t+16t²、10^17、2 : 1、2v、v/2、3 : 1、1/3、186000 mi/s、m₀、v²＝vₓ²+v_y²+v_z² 等逐项核对，仅 v² 记号 1 处有误（#1）已修；8 个编号公式（10.1–10.8）与英文及 \ref 顺序一致。
- **人名/术语**：牛顿、伽利略、爱因斯坦无误；铜/铝/金与英文 copper/aluminum/gold 一致（参考文本 OCR 作"钢/铅"，为旁证错误，未采纳）；气垫、雷管、滑块、油灰、弹性碰撞、伽利略相对性等术语无误。
- **图**：Fig. 10-1～10-8 与中文 8 图一一对应，8 个 PDF 齐备，图注齐全，正文全部用 `\ref`（渲染为图10.1–10.8），无未解析引用。
- **编译验证**：0 error / 0 overfull / 0 underfull / 0 missing character / 0 undefined references，11 页。
- **未改动项**：f/F 记号（存疑 1）；"象/像"等全书字形统一问题未触碰；未改其他章、未 commit。
