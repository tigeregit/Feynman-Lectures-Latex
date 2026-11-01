# 阅读效率提升 · 交付索引（分支 `feat/reading-efficiency`）

本目录是《费曼物理学讲义》中文 LaTeX 版「阅读效率提升」的方案与证据汇总。**正文尚未改动**——本分支只交付：方案、可复现审计、样式原型、内容试点样张。

## 1. 先看什么

| 顺序 | 文件 | 说明 |
|---|---|---|
| 1 | [阅读效率提升方案.md](阅读效率提升方案.md) | **主方案**：诊断、六层改造、删减策略、实施路线、验收指标、风险 |
| 2 | [../preview/content-pilot/ch2-pilot.pdf](../preview/content-pilot/ch2-pilot.pdf) | 内容层样张（第 2 章 §2-1/§2-3，9 页，零删字） |
| 3 | [../preview/style-demo/style-demo-before.pdf](../preview/style-demo/style-demo-before.pdf) / [style-demo.pdf](../preview/style-demo/style-demo.pdf) | 版式层前后对比样张（同一正文，原版 8 页 / 新版 14 页） |
| 4 | [figures/](figures/) | 前后对比截图（内容层 2 张、版式层 3 组 + 元素一览） |

## 2. 审计与报告

| 目录 | 内容 | 主要结论 |
|---|---|---|
| [analysis/text/](analysis/text/) | 文本审计（段落/句子/列表/强调/中英对照） | 2,080 段；段均 222 字、>500 字 108 段；0 列表；137 处列表化候选；13 个纯文字墙节；正文强调只在前 10 章 |
| [analysis/visual/](analysis/visual/) | 插图审计 + 34 条可视化候选 + 8 个图表替代实例 + 复用建议 | 110/290 节无图；343 条图注中 74.6% 只是文件名；65 处硬编码图号 |
| [analysis/typography/](analysis/typography/) | 版式实测、样式包设计、全书试编译 | 版式层实测 718 页（+3.31%）、0 error、Underfull 187→0 |
| [analysis/pilot-notes.md](analysis/pilot-notes.md) | 第 2 章试点说明 | 零删字 PASS；§2-1 段均 221.8→87.1；§2-3 508.2→108.9 |

## 3. 可复现工具

```bash
# 文本审计（约 1 秒，生成 docs/analysis/text/ 全部数据）
python3 tools/audit_text.py

# 图示审计（约 4 秒，需要 pdfinfo）
python3 tools/audit_figures.py

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
