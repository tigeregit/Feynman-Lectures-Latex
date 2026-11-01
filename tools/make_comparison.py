#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""生成「原版 vs 阅读效率版」三章对比册（LaTeX + 页面自动配对）。

用法
----
    python3 tools/make_comparison.py \
        --before "_attachments/build-feynman/Feynman Lectures on Physics.pdf" \
        --after  "_attachments/build-feynman/reading-efficiency/Feynman Lectures on Physics.pdf" \
        --out    preview/comparison

流程
----
1. 从两份 PDF 各自定位第 1/26/52 章的起始 PDF 页（用 pdftotext 逐页找章标题）；
2. 对每章取 4 个采样页（章首、正文 1、正文 2、章尾附近），在原版章范围内取页；
3. 对每个原版采样页，在「阅读效率版」该章范围内按 CJK 二元组 Jaccard 相似度找最佳对应页；
4. 生成 A4 横向对比册 TeX（左原版 / 右新版，每对一页），并编译为 PDF；
5. 输出 pairs.json 供复查。

依赖：pdftotext / pdftoppm / xelatex（均已在环境中）。
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def pdf_pages(pdf: Path) -> int:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, check=True).stdout.decode()
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1))


def page_text(pdf: Path, page: int) -> str:
    out = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-enc", "UTF-8", str(pdf), "-"],
        capture_output=True, check=False,
    ).stdout.decode("utf-8", errors="ignore")
    return out


def cjk_bigrams(text: str) -> set[str]:
    chars = CJK_RE.findall(text)
    return {chars[i] + chars[i + 1] for i in range(len(chars) - 1)}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def find_pdf_page_by_printed(pdf: Path, printed: int, span: int = 140) -> int:
    """扫描 PDF，找到页眉/页脚中印刷页码 = printed 的 PDF 页（1-based）。"""
    total = pdf_pages(pdf)
    for page in range(max(1, printed), min(total, printed + span) + 1):
        text = page_text(pdf, page)
        head = text[:80].replace("\n", " ")
        tokens = re.findall(r"\d+", head)
        if tokens and tokens[0] == str(printed):
            return page
    raise SystemExit(f"在 {pdf} 中找不到印刷页码 {printed} 对应的 PDF 页")


def page_offset(pdf: Path) -> int:
    """offset = PDF 页 - 印刷页。从末尾往前找带阿拉伯数字页码的正文页反推。"""
    total = pdf_pages(pdf)
    for page in range(total, max(1, total - 40), -1):
        text = page_text(pdf, page).strip()
        first = text.split()
        if first and first[0].isdigit():
            number = int(first[0])
            off = page - number
            if 0 < off < 100:
                return off
    raise SystemExit(f"无法从 {pdf} 反推页码 offset")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True)
    ap.add_argument("--after", required=True)
    ap.add_argument("--out", default="preview/comparison")
    ap.add_argument("--chapters", default="1,26,52")
    args = ap.parse_args()

    before = (REPO / args.before).resolve()
    after = (REPO / args.after).resolve()
    outdir = REPO / args.out
    outdir.mkdir(parents=True, exist_ok=True)
    chapters = [int(x) for x in args.chapters.split(",")]

    # 1) 从原版 .toc 解析全部章起始印刷页（按出现顺序编号 1..N）
    toc = before.parent / "Feynman Lectures on Physics.toc"
    if not toc.exists():
        raise SystemExit(f"找不到 {toc}")
    toc_txt = toc.read_text(encoding="utf-8", errors="ignore")
    starts = [int(m.group(1)) for m in re.finditer(r"\\contentsline \{chapter\}\{.*?\}\{(\d+)\}", toc_txt)]
    if len(starts) < max(chapters):
        raise SystemExit(f"toc 只解析到 {len(starts)} 章")
    print("章起始印刷页（前 5 章）:", starts[:5], "… 第 52 章:", starts[51] if len(starts) > 51 else "?")

    # 2) 计算 offset（PDF 页 - 印刷页）
    off_b = page_offset(before)
    off_a = page_offset(after)
    print(f"offset: before={off_b} after={off_a}")

    titles = {1: "原子的运动", 26: "光学：最短时间原理", 52: "物理定律的对称性"}
    total_pages_b = pdf_pages(before)
    pairs = []
    for ch in chapters:
        b_start = starts[ch - 1] + off_b
        b_next = (starts[ch] if ch < len(starts) else total_pages_b - off_b) + off_b
        b_end = min(b_next - 1, total_pages_b)
        a_start = starts[ch - 1] + off_a
        a_next = (starts[ch] if ch < len(starts) else pdf_pages(after) - off_a) + off_a
        a_end = min(a_next - 1, pdf_pages(after))
        span = max(1, b_end - b_start)
        samples = sorted({b_start, b_start + span // 3, b_start + 2 * span // 3, max(b_start, b_end - 1)})
        a_texts = {p: cjk_bigrams(page_text(after, p)) for p in range(a_start, a_end + 1)}
        for bpage in samples:
            bt = cjk_bigrams(page_text(before, bpage))
            apage, score = max(((p, jaccard(bt, t)) for p, t in a_texts.items()), key=lambda x: x[1])
            pairs.append({
                "chapter": ch, "title": titles[ch],
                "before_page": bpage, "after_page": apage,
                "before_printed": bpage - off_b, "after_printed": apage - off_a,
                "similarity": round(score, 3),
            })
            print(f"ch{ch}: before p{bpage}(印刷{bpage-off_b}) -> after p{apage}(印刷{apage-off_a}) sim={score:.2f}")

    (outdir / "pairs.json").write_text(json.dumps(pairs, ensure_ascii=False, indent=2), encoding="utf-8")

    # 3) 复制 PDF 为简单文件名（避免空格路径问题）
    import shutil
    shutil.copy2(before, outdir / "before.pdf")
    shutil.copy2(after, outdir / "after.pdf")

    # 4) 生成对比册 TeX
    body = []
    for pr in pairs:
        body.append(
            "\\comparisonpair{%s}{%d}{%d}{before.pdf}{%d}{after.pdf}{%d}"
            % (pr["title"], pr["before_printed"], pr["after_printed"], pr["before_page"], pr["after_page"])
        )
    tex = r"""\documentclass[UTF8,10pt,a4paper,landscape]{ctexart}
\usepackage[margin=9mm]{geometry}
\usepackage{graphicx,xcolor,fancyhdr}
\setCJKmainfont[AutoFakeBold=true]{Songti SC}
\definecolor{accent}{RGB}{31,78,121}
\definecolor{grayline}{RGB}{170,170,170}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\small\color{grayline}第 \thepage\ 页 / 原版（左） vs 阅读效率版（右）}
\renewcommand{\headrulewidth}{0pt}

\newcommand{\comparisonpair}[7]{%
  \clearpage
  \noindent
  \begin{minipage}[t]{0.487\textwidth}
    \centering
    {\small\color{accent}\textbf{原版}（印刷第 #2 页）}\par\vspace{1mm}
    \includegraphics[page=#5,width=\linewidth,height=0.80\textheight,keepaspectratio]{#4}
  \end{minipage}\hfill
  \begin{minipage}[t]{0.487\textwidth}
    \centering
    {\small\color{accent}\textbf{阅读效率版}（印刷第 #3 页）}\par\vspace{1mm}
    \includegraphics[page=#7,width=\linewidth,height=0.80\textheight,keepaspectratio]{#6}
  \end{minipage}
  \vspace{1mm}
  \begin{center}\small 第 #1 章 · 对照（原版 #2 / 新版 #3）\end{center}
}

\begin{document}
\begin{center}
  {\LARGE\bfseries 费曼物理学讲义 · 阅读效率改造对比册}\par\vspace{2mm}
  {\small 第 1 章（首）· 第 26 章（中）· 第 52 章（末）｜左：原版（695 页）｜右：阅读效率版（新版式 + 三章内容改造）}
\end{center}
""" + "\n".join(body) + "\n\\end{document}\n"
    texpath = outdir / "三章对比册.tex"
    texpath.write_text(tex, encoding="utf-8")
    print(f"写入 {texpath}")

    # 5) 编译
    for _ in range(2):
        rc = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory", str(outdir), str(texpath)],
            cwd=outdir, capture_output=True,
        )
        if rc.returncode != 0:
            sys.stderr.write(rc.stdout.decode(errors="ignore")[-3000:])
            sys.stderr.write("\n编译失败；请查看日志。\n")
            return 1
    print(f"输出 {outdir / '三章对比册.pdf'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
