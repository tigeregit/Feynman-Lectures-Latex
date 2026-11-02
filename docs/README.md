# 阅读效率提升 · 交付索引（分支 `feat/reading-efficiency`）

本目录是《费曼物理学讲义》中文 LaTeX 版「阅读效率提升」的方案与证据汇总。

**当前状态（2026-11-02）**：方案已通过；版式层已接入主文件；内容层按评审决定完成**第 1 章（首）、第 26 章（中）、第 52 章（末）**三章试点（零删改 PASS），并产出「原版 vs 阅读效率版」对比册。全书 **695 → 726 页（+4.46%）**、0 error。其余章节正文未改。

## 1. 先看什么

| 顺序 | 文件 | 说明 |
|---|---|---|
| 1 | [阅读效率提升方案.md](阅读效率提升方案.md) | **主方案**：诊断、六层改造、删减策略、实施路线、验收指标、风险 |
| 2 | [../preview/content-pilot/ch2-pilot.pdf](../preview/content-pilot/ch2-pilot.pdf) | 内容层样张（第 2 章 §2-1/§2-3，9 页，零删字） |
| 3 | [../preview/style-demo/style-demo-before.pdf](../preview/style-demo/style-demo-before.pdf) / [style-demo.pdf](../preview/style-demo/style-demo.pdf) | 版式层前后对比样张（同一正文，原版 8 页 / 新版 14 页） |
| 4 | [figures/](figures/) | 前后对比截图（内容层 2 张、版式层 3 组 + 元素一览） |
| 5 | [../preview/comparison/三章对比册.pdf](../preview/comparison/三章对比册.pdf) | **首/中/末三章：原版（左）vs 阅读效率版（右）并排对比册** |
| 6 | [试点三章改造规范.md](试点三章改造规范.md) | 三章改造的硬约束、配额、零删改标记法与校验流程 |

### 三章试点结果速览

| 章 | 段落数 | 平均段长 | 最长段 | 列表/小标题 | 新增文字 | 零删改 |
|---|---:|---:|---:|---:|---:|---|
| 第 1 章 原子的运动 | 47→81 | 215.9→125.3 | 704→245 | 8/8 | 8.8% | PASS |
| 第 26 章 光学：最短时间原理 | 49→95 | 185.7→95.8 | 715→228 | 10/8 | 8.7% | PASS |
| 第 52 章 物理定律的对称性 | 77→107 | 177.4→127.7 | 511→242 | 8/8 | 7.5% | PASS |

详见 [chapter-1-notes](analysis/chapter-1-notes.md)、[chapter-26-notes](analysis/chapter-26-notes.md)、[chapter-52-notes](analysis/chapter-52-notes.md) 与方案 §8.5。

## 2. 审计与报告

| 目录 | 内容 | 主要结论 |
|---|---|---|
| [analysis/text/](analysis/text/) | 文本审计（段落/句子/列表/强调/中英对照） | 2,080 段；段均 222 字、>500 字 108 段；0 列表；137 处列表化候选；13 个纯文字墙节；正文强调只在前 10 章 |
| [analysis/visual/](analysis/visual/) | 插图审计 + 34 条可视化候选 + 8 个图表替代实例 + 复用建议 | 110/290 节无图；343 条图注中 74.6% 只是文件名；65 处硬编码图号 |
| [analysis/typography/](analysis/typography/) | 版式实测、样式包设计、全书试编译 | 版式层实测 718 页（+3.31%）、0 error、Underfull 187→0 |
| [analysis/pilot-notes.md](analysis/pilot-notes.md) | 第 2 章试点说明 | 零删字 PASS；§2-1 段均 221.8→87.1；§2-3 508.2→108.9 |
| [analysis/chapter-1-notes.md](analysis/chapter-1-notes.md) 等 | 三章改造说明（chapter-1/26/52-notes.md） | 零删改校验、统计、复核点 |
| [analysis/chapter-1-review.md](analysis/chapter-1-review.md) | **第 1 章精读与内容审查**（OCR/漏译/物理化学错误修正 + 编译验证） | 对照 eFLP 英文原文审出 68 处问题（高 6/中 20/低 42），已全部修正；单章 0 error、全书 726 页 0 error |
| [analysis/chapter-2-review.md](analysis/chapter-2-review.md) | **第 2 章精读与内容审查**（OCR/源译错误修正 + 表格/图/数字核对） | 审出 81 处问题（高 5/中 20/低 56），已全部修正；补回 QED 漏句、修正 2 处数字；单章 0 error、全书 726 页 0 error |
| [analysis/chapter-3-review.md](analysis/chapter-3-review.md) | **第 3 章精读与内容审查**（OCR/源译错误修正 + 图/段落完整性核对） | 审出 75 处问题（高 1/中 41/低 33），已全部修正；确认无漏段（英文"第 35 段"实为脚注）；单章 12 页 0 error、全书 726 页 0 error |

## 3. 可复现工具

```bash
# 文本审计（约 1 秒，生成 docs/analysis/text/ 全部数据）
python3 tools/audit_text.py

# 图示审计（约 4 秒，需要 pdfinfo）
python3 tools/audit_figures.py

# 三章零删改校验 + 改造统计
python3 tools/verify_chapter.py 1        # 章号 1/26/52；PASS 才算通过
python3 tools/chapter_stats.py 1

# 生成「原版 vs 阅读效率版」对比册（需先构建两版全书 PDF）
python3 tools/make_comparison.py \
  --before "_attachments/build-feynman/Feynman Lectures on Physics.pdf" \
  --after  "_attachments/build-feynman/reading-efficiency/Feynman Lectures on Physics.pdf" \
  --out    preview/comparison

# 内容样张编译（需 XeLaTeX）
cd preview/content-pilot && xelatex -interaction=nonstopmode ch2-pilot.tex   # 连编 2 遍

# 版式样张编译（原版 + 新版）
bash preview/style-demo/build-demo.sh

# 全书试编译（套用 readability.sty，产物在 _attachments 本地忽略目录）
# 见 docs/analysis/typography/03-全书试编译报告.md 的“复现命令”
```

## 4. 样式包

[`../styles/readability.sty`](../styles/readability.sty)：正文零改动、样式集中管理。

- 选项：`mode=color|mono`、`skim`（隐藏选读）、`screen`
- 接口：`\runin` `\term` `\enterm` `\keyidea` `\pullquote` `summarybox` `keybox` `conceptmap` `optional` `\aside` `\chapterintro` `\readingpath` `\figsource`
- 集成：主文件导言区最后一行 `\usepackage{readability}`（详见 [analysis/typography/02-样式包设计.md](analysis/typography/02-样式包设计.md)）

## 5. 目录约定

- `_attachments/` 是本地忽略目录（编译工作区/成品/英文对照语料），不随分支提交。
- `preview/**/build/` 为编译产物，已加入 `.gitignore`；交付 PDF 另存在 `preview/` 对应目录。
- 所有审计数字由 `tools/` 脚本生成；口径与误差见各目录 README。
