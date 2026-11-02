# 第 1 卷剩余章节逐章审查 · 作业手册（审校员必读）

> 目标：把第 1 卷 **第 4–52 章**逐章对照 eFLP 英文原文精读，修正 OCR/翻译/数字/术语错误，单章编译通过，留下报告与提交。
> 第 1–3 章已完成（可参考 `docs/analysis/chapter-{1,2,3}-review.md` 的方法与力度）。

---

## 1. 每章的标准作业流程

### 第 0 步：读材料

| 材料 | 路径 |
|---|---|
| 要改的中文正文 | `Chapters/VolumeI/ChapterN.tex` |
| eFLP 英文原文 | `_attachments/build-feynman/audit/en/I_NN.txt`（NN 补零，如 I_04.txt；每段一行） |
| 公开中译本参考（**旁证，本身也有 OCR 错误**） | `_attachments/reference/zh/ChapterN.txt`（已按章切好） |
| 自动候选差异清单 | `_attachments/reference/candidates/chN-candidates.md`（若不存在，先运行 `python3 tools/chapter_diff.py --chapter N`） |
| 官方网页（需要时） | `https://www.feynmanlectures.caltech.edu/I_NN.html` |
| 单章编译模板 | `preview/chapter-2/check.tex`（复制到 `preview/chapter-N/check.tex` 并改章号/文件名） |

### 第 1 步：过一遍自动候选差异（效率最高）

`chN-candidates.md` 分两类：
- **一小块差异（≤8 字）**：多是 OCR 单字讹变，例如"查/察""旧/然"。逐条看上下文 + 英文判断：**我们错**（改）、**参考错**（不改，记一笔）、**底本译法差异**（不改，记一笔）。
- **大块差异（>8 字）**：可能是漏句、底本删改、公式/图环境噪声。重点看"我们为空、参考有字"（疑似漏译）与"我们有、参考为空"（参考漏抄）。

> 参考文本是 archive.org 上的公开中译本全文（OCR），其错误率不低；**永远以 eFLP 英文原文为准**，公开中译本只用于快速定位"我们 vs 底本"的差异。

### 第 2 步：通读全章、逐段对英文

自动清单抓不到"底本翻译错误"（如第 3 章的 glucose→"蔗糖"、ribosome→"微粒体"）。所以必须：
1. 把中文正文按段落与 `I_NN.txt` 的段落对齐（英文每段一行；中英段落数一般 1:1，若不等要找原因）；
2. 逐句核对：**漏句/漏段、重复粘贴、数字/年份/量纲、术语与物理化学事实、人名/专名、图表编号与引用**；
3. 记录所有问题（行号 + 英文依据 + 改法）。

### 第 3 步：写成"带断言的修正脚本"并执行

不要手工逐处编辑（易漏、易错）。写 `/tmp/fix_chN.py`：
```python
REPL = [("1-01", "旧串", "新串", 1), ...]   # (编号, 旧, 新, 期望命中次数)
```
- 每条旧串必须在文中**恰好命中期望次数**，否则脚本报错退出（防止改错位置）；
- 先 dry-run 打印 diff 自查，再 `--apply`；
- 参考 `docs/analysis/chapter-2-review.md` 与 `/tmp/fix_chapter3.py` 的写法（如仍在 /tmp）。

修正原则：
- **只改错误**，不重写译文风格；保留原译的用词与语气；
- 高置信度才改；底本译法可商榷的写进报告"存疑项"，不改；
- 旧字形"象/像""图象/图像"属全书统一问题，**不要单章批量改**；
- 章内硬编码图号（"图4-1""表4-1"）如与图注渲染格式不一致，改为 `图\ref{label}` / `表\ref{label}`（label 已存在时），并确保引用解析；
- 数字/公式/单位错误一律改，并在报告里给出中英对照。

### 第 4 步：单章编译

```bash
# 1) 建入口（若无 preview/chapter-N/check.tex）：复制 preview/chapter-2/check.tex
#    把 \setcounter{chapter}{1} 改成 {N-1}，\input 改成 ChapterN.tex
cd preview/chapter-N
rm -rf build && mkdir -p build
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex
xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex
# 验收：
grep -c '^!' build/check.log                 # 0
grep -c 'Overfull' build/check.log           # 0
grep -c 'Underfull' build/check.log          # 0
grep -c 'Missing character' build/check.log  # 0
grep -c 'undefined references' build/check.log  # 0
pdfinfo build/check.pdf | grep Pages
```
- 终端里 `I can't find file 'SimSun'` 是字体探测噪音，不算 error；
- 若改动导致 overfull/underfull，调整该处排版（必要时缩小改动范围）。

### 第 5 步：写报告 `docs/analysis/vol1-review/chapter-N.md`

简短即可（≤80 行）：
```markdown
# 第 N 章《章名》审查报告
- 范围/对照材料/段落对应（中英段数）
- 结果：问题总数（高/中/低），已修 X 条，存疑 Y 条
- 高/中问题表（行号 | 问题 | 英文依据 | 修正）
- 覆盖性结论（有无漏段/重复；数字/人名/图表核对结论）
- 验证：单章编译结果（页数/error/overfull/missing char）
- 未改动项与建议
```

### 第 6 步：向 Lead 汇报

`send_message` 给 `lead`，≤400 字：章号、问题数（高/中/低）、关键 3–5 条（行号+一句）、单章编译结果、是否创建/修改了 preview/chapter-N/check.tex。

---

## 2. 纪律

- **只改自己的章**：`Chapters/VolumeI/ChapterN.tex`；只新建/修改 `preview/chapter-N/` 与 `docs/analysis/vol1-review/chapter-N.md`。**不要碰其他章、不要改 tools/、docs/README、不要 git commit**（Lead 统一提交）。
- 不要运行全书编译（Lead 统一做）。
- 第 26、52 章有 `%<<<NEW … %>>>NEW` 阅读效率改造块：**这些块是后加导读，不是 OCR 原文**，只核对其事实陈述，不要当 OCR 错误改；其余章（4–25、27–51）没有 NEW 块。
- 报告与修正都要有**英文原文依据**（逐字引用 ≤25 词），不要凭印象。
- 遇到不确定的：写进报告存疑项，不要擅自大改。
