# 第 16 章《相对论中的能量与动量》审查报告

- 任务：task-28（第 1 卷剩余章节第二批）；日期：2026-11-02；分支 `feat/reading-efficiency`
- 范围：`Chapters/VolumeI/Chapter16.tex`（204 行 → **修改后 204 行**，CRLF 保留）
- 对照材料：
  - 英文原文 `_attachments/build-feynman/audit/en/I_16.txt`（49 个正文段；公式为抓取后的纯文本形式）
  - 公开中译本 `_attachments/reference/zh/Chapter16.txt`（旁证；OCR 质量差，数字/公式成乱码，多数差异为参考噪声）
  - 自动候选 `_attachments/reference/candidates/ch16-candidates.md`（223 小 + 35 大；逐条过，大块差异均为公式/页眉/图注噪声，**无"我们漏句"项**）
- 单章编译入口：`python3 tools/make_chapter_check.py 16` 生成 `preview/chapter-16/check.tex`（章号 15）

## 结果概览

- 问题 **22 条（高 1 / 中 20 / 低 1）**，**已全部修复**；24 处替换（含 figure 环境移动 2 处），带断言脚本 `/tmp/fix_ch16.py`（每条 old 恰命中 1 次才执行；保留 CRLF、末尾无换行）。
- 单章编译：`-no-mktex=tfm` 连编 2 遍：**12 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined reference**；5 条基线 warning（xeCJK 重定义、带路径 usepackage、hyperref colorlinks、黑体字形缺、字形汇总）。
- **公式内容零改动**：14 个公式 (16.1)–(16.14) 逐式核对，全部与英文一致（见覆盖性结论）。

## 高/中问题（行号为修改后文件当前行号）

| 行号 | 问题 | 英文依据（逐字 ≤25 词） | 修正 |
|---|---|---|---|
| L105 | **跨章引用未定义**：2 处 `\ref{figure:光束经过的斜向路程示意图}` 的 label 在第 15 章 → 单章编译渲染"图??"，产生 undefined reference（基线 2 条） | "We have already (Section 15–4) discussed…" / "(see Fig. 15-3(c))" | 改为硬编码"（图15.3）""（见图15.3(c)）"，单章 0 undefined |
| L169（原 L163/170） | wrapfigure 插在句子中间，把"…非弹性碰撞的过程。为了 / 简单起见…"拆成两段（"为了"成段尾），句子被图打断 | —（版式） | figure 环境移到"现在，我们承认动量是守恒的…"段首，且"为了简单起见"接回同段 |
| L31 | 术语/OCR："正像**子**运动时"（缺 μ）、"**伴**谬"、"一对**李**生子"、"才称为是一种**“谬”**" | "Just as the muons last longer when they are moving" | "正像$\mu$子运动时"、"佯谬"、"孪生子"、"“佯谬”" |
| L9 | OCR："它给**子**吾等…""曾给**于**现代观念"；段末缺句号 | "it has profound influences on our ideas" | "给予""给予"，并补"。" |
| L13 | OCR："不往外看**面**去谈论""物理学家相当**笨抽**" | "It is self-evident that it is meaningless to talk about…" / "the physicists are rather stupid" | "而""笨拙" |
| L19 | 人名拼写："傅科（**Foucsult**）"；OCR："绕轴转**功**" | "the so-called Foucault pendulum" | "Foucault"；"绕轴转动" |
| L21 | OCR："如果周围没有星体**成**星云" | "if there were no stars and nebulae around" | "星体和星云" |
| L115 | 标点缺失："质量是必须按照这种方式变化的**我们必须说**…（…任何东西）。"（缺句号和左括号，右括号孤悬） | "(We have to say 'a few other assumptions' because…)" | "变化的。（我们必须说…任何东西）。" |
| L115 | OCR："把动量设为一个**常熟**乘上速度" | "we shall not assume that the momentum is a constant times the velocity" | "常数" |
| L120 | 衍文："论证$m$**。**的公式必须是"；多余逗号："把系数$m$**，**称为" | "the formula for mv must be…" / "call this coefficient mv the 'mass'" | 删"。"、删逗号 |
| L62 | 缺逗号："速度是$v_{x'}$**就**说明位移…" | "the velocity is vx′, which means that…" | 加"，" |
| L187 | 漏字："碘、**等**的质量"（漏"氙"）；缺句号："$m_w$**现在**如果…" | "iodine, xenon, and so on" / "they each have a mass mw. Now suppose…" | "碘、氙等"；"$m_w$。现在" |
| L195 | 漏字："以速率**运动**的物体"（缺 v） | "the mass in motion at speed v is the mass m0 at rest divided by…" | "以速率$v$运动的物体" |

## 低问题（已修）

L120 "$m$，称为" 中多余逗号（属上表同条，归低）。

## 存疑项（未改）

1. 跨章引用"图15.3"为**硬编码权宜**：单章预览无法解析第 15 章 label；若 Lead 统一处理全书跨章引用，可在全书编译环境改回 `\ref`（编号会渲染为"15.3"）。
2. L15 "牛顿就已确实认为"（英文 "Newton believed that it was true"）语序略拗口，语义无误，未改。
3. L9 "几位盲人…这个古老的故事或许是哲学家对相对论所抱有的观点的另一个例子" 与英文 "another example…of the theory of relativity from the philosopher's point of view" 措辞略异，语义可通，未改。
4. 底本把英文 "(Section 15–4)" 译作"（图15-3）"，本次保留图引用（仅改硬编码并补 (c)）。
5. 图 16.2/16.3 在中文版并列于一个 figure 环境（各自编号），版式保留未动。
6. eFLP 2006/2013 勘误未逐条比对（以抓取文本 I_16.txt 为准）；本章抓取文本未见脚注标记。

## 覆盖性结论

- **段落**：英文 49 个正文段逐段核对（中文因公式显示拆为更多排版段），**无整段缺失、无合并、无重复、无漏句**；候选 35 条大块差异经核对均为公式/图注/页眉噪声。
- **公式**（零改动，逐式核对）：(16.1) 正变换 LT、(16.2) 逆变换、(16.3) x′=vx′t′、(16.4) x、(16.5) t、(16.6) 速度叠加 vx=(u+vx′)/(1+uvx′/c²)、(16.7) vy=vy′√(1−u²/c²)、(16.8) p=mvv、(16.9) mw/mv=√(1−u²/c²)、(16.10) mu=m0/√(1−u²/c²)、(16.11) M0=2mw、(16.12) ΔT=(mu−m0)c²、(16.13) E²−P²c²=m0²c⁴、(16.14) Pc=Ev/c——全部与英文一致。
- **数字/单位**：186,000 mi/s（光速，×3 处）、100,000 mi/s（飞船，×2）、200,000 mi/s（"代数和"错误值）、1/2、1/4、4/5、1/n、c/2 等全部与英文一致；单位写法"$mi \cdot s^{-1}$"保留底本风格。
- **图表**：4 图编号 16.1–16.4 与正文 `\ref` 全部解析（0 undefined）；图注与英文 Fig. 16–1~16–4 captions 对应；图 16.4 因移位置已重新排版且 0 overfull。
- **编译**：12 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined reference；2 遍通过。

## 未改动项与建议

- 跨章引用硬编码"图15.3"需全书统一时再处理（见存疑 1）。
- 其余存疑项均为底本译法/版式，保持不动。
