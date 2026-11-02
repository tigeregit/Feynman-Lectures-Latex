# 第 24 章《瞬变态》审查报告

- 任务：task-36（第 1 卷剩余章节第三批）；日期：2026-11-03；分支 `feat/reading-efficiency`
- 范围：`Chapters/VolumeI/Chapter24.tex`（238 行 → **修改后 238 行**，CRLF 保留、末尾无换行）
- 对照材料：
  - 英文原文 `_attachments/build-feynman/audit/en/I_24.txt`（24-1~24-3 正文 L36–L380；公式为纯文本抓取形式）
  - 公开中译本 `_attachments/reference/zh/Chapter24.txt`（旁证；OCR 质量差，公式成乱码，多数候选差异为参考噪声）
  - 自动候选 `_attachments/reference/candidates/ch24-candidates.md`（217 小 + 39 大；逐条过，大块差异均为公式/图注/页眉噪声，**无"我们漏句"项**）
- 单章编译入口：`python3 tools/make_chapter_check.py 24` 生成 `preview/chapter-24/check.tex`（章号 23）

## 结果概览

- 问题 **11 条（高 1 / 中 5 / 低 5）**，**已全部修复**；13 处替换（含数字格式 3 处），带断言脚本 `/tmp/fix_ch24.py`（每条 old 恰命中 1 次才执行；保留 CRLF）。
- 单章编译：`-no-mktex=tfm` 连编 2 遍：**8 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined reference**；5 条基线 warning（xeCJK 重定义、带路径 usepackage、hyperref colorlinks、黑体字形缺、字形汇总）。
- **公式内容零改动**：22 个编号公式 (24.1)–(24.22) 逐式核对，全部与英文一致（仅把共轭星号改为上标，见低问题）。

## 高/中问题（行号为修改后文件当前行号）

| 行号 | 问题 | 英文依据（逐字 ≤25 词） | 修正 |
|---|---|---|---|
| L56 | **跨章引用未定义**：`\ref{Table:23:1}` 的 label 在第 23 章 → 单章编译渲染"表??"，产生 undefined reference（基线 1 条） | "see Table 23–1" | 改为硬编码"（见表23.1）"（第 23 章 aux 编号 23.1） |
| L75–81（原 L75/L82） | **wrapfigure 24.1 插在句子中间**：把"…通过解运动微分方程本身 / 来精确地分析这种运动。"拆成两段（"本身"结尾单独成段、下段以"来精确地"开头） | "The equation and Fig. 24–1 give us an idea of what we expect, and now we shall do it exactly by solving the differential equation for the motion." | figure 环境移到该段段首，句子接回："…微分方程本身来精确地分析这种运动。" |
| L140–146（原 L141/L148） | **wrapfigure 24.2 插在词中间**：把"…看清屏 / 幕上的唯一的一条径迹…"拆成两段（"屏"与"幕"被图隔开） | "…the rest of the circuit is only a technical detail. We would like to repeat the experiment many, many times, since the persistence of vision is not good enough…" | figure 环境移到"现在我们来看一看…"段首；合并为"…看清屏幕上的唯一的一条径迹，所以…" |
| L146 | 术语/OCR："视觉的**住留**" | "the persistence of vision" | 视觉的暂留 |
| L131 | OCR："但是，**当今**$F(t)\equiv 0$时" | "But when we put F(t)≡0…" | 但是，当$F(t)\equiv 0$时 |
| L23 | OCR："**确定**有些能量贮存在振动中" | "There is some energy stored in the oscillation, but…" | 确实有些能量贮存在振动中 |

## 低问题（已修）

L60 数字格式："$1~000$"→"1000"、"$1/1~000$"→"1/1000"（共 3 处，渲染成"1 000"含空格）；L60 译句不通："让我们首先对一个$Q$值很高的系统将发生什么情况得出一个大致的看法。"→"让我们先大致设想一下，对于一个$Q$值很高的系统将会发生什么情况。"；L11 共轭星号未上标："$\hat{A}\hat{A}*$"→"$\hat{A}\hat{A}^*$"；L152、L169（原 L154/L171）图文件行尾多余空格 ×2 删除。

## 存疑项（未改）

1. 图 24.3–24.6 的 `\caption{}` 为空：eFLP 原书这几张示波器照片无图注（仅图号），故保留空图注；若后续需要中文图注可补。
2. 图 24.2 图注"演示瞬变态的电路"对应英文 "An electrical circuit for demonstrating transients."（"电"由"电路"隐含），未改。
3. L23 "在方括号里的**表示式**"：底本用"表示式"（其余处用"表达式"），属用词统一问题，未改。
4. 表 23.1 为跨章引用，单章采用硬编码"表23.1"；若全书统一处理跨章引用可改回 `\ref`（第 23 章 aux 编号为 23.1）。
5. L60 "这难道是不合理的吗？"：英文 "Is it not reasonable…?" 的反问译法，语义可通，未改。
6. 图 24.3–24.6 在正文中以"图\ref{figure:24-3}到\ref{figure:24-6}"引用，label 名沿用原文件，渲染编号正确（图 24.3–24.6），未改名。

## 覆盖性结论

- **段落**：英文 24-1~24-3 正文（L36–L380）与中文逐段核对（中文因公式/图被拆为 47 个排版段），**无整段缺失、无合并、无重复、无漏句**；候选 39 条大块差异经核对均为公式/图注/页眉噪声。
- **公式**（零改动，逐式核对）：(24.1) 受迫振子方程、(24.2) 功率、(24.3) 平均功率、(24.4) ⟨P⟩=½γmω²x₀²、(24.5) ⟨P⟩=R⟨I²⟩、(24.6) ⟨E⟩、(24.7) Q 定义、(24.8) dE/dt=−ωE/Q、(24.9) E=E₀e^{−ω₀t/Q}、(24.10) 猜测解、(24.11) 试解代入、(24.12) 特征方程、(24.13) α 两根、(24.14)(24.15) 两个 α、(24.16)(24.17)(24.18) 解 x₁/x₂、(24.19) 通解、(24.20) 实数解、(24.21) A_I、(24.22) 完整解——全部与英文一致。
- **数字/量纲**：Q/(2π)=1000、1/1000、每秒闭开关 60 次、1/2、γ/2、ω₀²−γ²/4、2π 等全部一致；单位/符号无错。
- **图表**：6 张图编号 24.1–24.6 与全部 `\ref` 解析（0 undefined）；图 24.1/24.2 图注与英文 captions 对应，24.3–24.6 无图注（同 eFLP）；图 24.1/24.2 移动位置后 0 overfull、版面正常。
- **编译**：8 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined reference；2 遍通过。

## 未改动项与建议

- 空图注（24.3–24.6）、"表示式"等底本用词保留。
- 跨章表引用的硬编码"表23.1"需全书统一处理时再改 `\ref`。
