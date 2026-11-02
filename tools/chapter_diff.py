#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""逐章“本仓库中文 vs 公开中译本（archive.org）”候选差异生成器。

用途：为第 1 卷各章的 OCR 校勘提供候选清单。公开中译本本身也是 OCR/转录文本，
只作“旁证”：差异可能来自（a）本仓库 OCR 讹变（大多数）、（b）底本翻译差异、
（c）参考文本自身 OCR 错误。需要审校员对照英文 I_NN.txt 逐条判定。

用法：
  python3 tools/chapter_diff.py --chapter 4
输出：_attachments/reference/candidates/ch4-candidates.md（本地忽略目录）
"""
import argparse
import difflib
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHDIR = os.path.join(ROOT, "Chapters", "VolumeI")
REFDIR = os.path.join(ROOT, "_attachments", "reference", "zh")
OUTDIR = os.path.join(ROOT, "_attachments", "reference", "candidates")


def npstr(s):
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]", "", s)


def strip_tex(s):
    """整段文本去 LaTeX（保留行结构：被删除的块用等量换行占位）。"""
    s = re.sub(r"%<<<NEW.*?%>>>NEW", lambda m: "\n" * m.group(0).count("\n"), s, flags=re.S)
    s = re.sub(r"%.*", "", s)
    s = re.sub(r"\\chapter\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\section\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\ref\{[^}]*\}", "", s)
    s = re.sub(r"\\footnote\{", "", s)
    # 整块环境（图/表/公式）：用等量换行占位，保持行号映射
    s = re.sub(r"\\begin\{(figure|wrapfigure|table|equation\*?|align\*?)\}(.*?)\\end\{\1\}",
               lambda m: "\n" * m.group(0).count("\n"), s, flags=re.S)
    s = re.sub(r"\\includegraphics\[[^\]]*\]\{[^}]*\}", "", s)
    s = re.sub(r"\\begin\{center\}|\\end\{center\}", "", s)
    s = re.sub(r"\$[^$]*\$", "", s)
    s = re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    return s.replace("\\", "")


def build_norm(tex):
    """返回 (normalized_str, line_of_index)。"""
    clean_tex = strip_tex(tex)
    lines = clean_tex.splitlines()
    norm_chars = []
    line_of = []
    for ln, line in enumerate(lines, 1):
        clean = line
        for c in clean:
            if re.match(r"[0-9A-Za-z\u4e00-\u9fff]", c):
                norm_chars.append(c)
                line_of.append(ln)
    return "".join(norm_chars), line_of


def esc(x):
    return x.replace("|", "\\|") if x else "∅"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, required=True)
    args = ap.parse_args()
    ch = args.chapter
    tex = open(os.path.join(CHDIR, "Chapter%d.tex" % ch), encoding="utf-8").read()
    ref_path = os.path.join(REFDIR, "Chapter%d.txt" % ch)
    ref = npstr(open(ref_path, encoding="utf-8", errors="replace").read())
    ours, line_of = build_norm(tex)

    sm = difflib.SequenceMatcher(None, ours, ref, autojunk=False)
    small, big = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        a, b = ours[i1:i2], ref[j1:j2]
        ln = line_of[i1] if i1 < len(line_of) else "?"
        ctx = ours[max(0, i1 - 10):i2 + 10]
        if len(a) <= 8 and len(b) <= 8:
            small.append((ln, a, b, ctx, i1))
        else:
            big.append((ln, a, b, ctx, i1))

    os.makedirs(OUTDIR, exist_ok=True)
    out = os.path.join(OUTDIR, "ch%d-candidates.md" % ch)
    with open(out, "w", encoding="utf-8") as f:
        f.write("# Chapter %d 候选差异（我们 vs 公开中译本参考）\n\n" % ch)
        f.write("- 本仓库正文字符 %d；参考文本字符 %d\n" % (len(ours), len(ref)))
        f.write("- 小块差异 %d 条（多半是 OCR 单字/词讹变）；大块差异 %d 条（漏句/底本差异/参考文本错误）\n" % (len(small), len(big)))
        f.write("- **参考文本本身也有 OCR 错误**，必须对照英文 I_%02d.txt 判断；若我们的写法正确、参考错，标记“参考误”即可。\n\n" % ch)
        f.write("## 一、小块差异（≤8 字）\n\n")
        f.write("| # | 行号 | 我们 | 参考 | 上下文（我们） |\n|---|---|---|---|---|\n")
        for k, (ln, a, b, ctx, _i) in enumerate(small, 1):
            f.write("| %d | L%s | %s | %s | …%s… |\n" % (k, ln, esc(a), esc(b), esc(ctx)))
        f.write("\n## 二、大块差异（>8 字）\n\n")
        f.write("| # | 行号 | 我们（节选） | 参考（节选） | 上下文（我们） |\n|---|---|---|---|---|\n")
        for k, (ln, a, b, ctx, _i) in enumerate(big, 1):
            f.write("| %d | L%s | %s | %s | …%s… |\n" % (k, ln, esc(a[:40]), esc(b[:40]), esc(ctx)))
    print("ch%-2d  ours=%6d ref=%6d  small=%d big=%d  -> %s" % (ch, len(ours), len(ref), len(small), len(big), out))


if __name__ == "__main__":
    main()
