#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从公开中译本 djvu 全文中切出第 1 卷各章的中文参考文本。

思路：用本仓库 ChapterN.tex 首段的若干 20 字指纹在归一化后的中译本全文中查找，
取最早命中作为该章起点；下一章起点为其终点。输出：
  _attachments/reference/zh/ChapterN.txt    （该章中文参考文本，去空白）
  _attachments/reference/chapter_offsets.json（偏移表，供其它脚本复用）
用法：python3 tools/vol1_archive_align.py [--chapters 1-52]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVE = os.path.join(ROOT, "_attachments", "reference", "flp_cn_plain.txt")
OUTDIR = os.path.join(ROOT, "_attachments", "reference", "zh")
CHDIR = os.path.join(ROOT, "Chapters", "VolumeI")


def norm(s):
    return re.sub(r"\s+", "", s)


def npstr(s):
    """只保留汉字/字母/数字，去掉标点，用于抗 OCR 标点差异的指纹匹配。"""
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]", "", s)


def strip_tex(s):
    s = re.sub(r"%<<<NEW.*?%>>>NEW", "", s, flags=re.S)
    s = re.sub(r"%.*", "", s)
    s = re.sub(r"\\chapter\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\section\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\\ref\{[^}]*\}", "", s)
    s = re.sub(r"\\footnote\{", "", s)
    s = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", "", s, flags=re.S)
    s = re.sub(r"\\begin\{wrapfigure\}.*?\\end\{wrapfigure\}", "", s, flags=re.S)
    s = re.sub(r"\\begin\{table\}.*?\\end\{table\}", "", s, flags=re.S)
    s = re.sub(r"\\includegraphics\[[^\]]*\]\{[^}]*\}", "", s)
    s = re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}", r"\1", s)
    return s.replace("\\", "")


def fingerprints(tex, n=20, count=6):
    t = npstr(strip_tex(tex))
    # 跳过章节标题行：从第一个段落开始取指纹
    out = []
    paras = [p for p in re.split(r"\n\s*\n", strip_tex(tex)) if len(norm(p)) >= 40]
    for p in paras[:3]:
        p = npstr(p)
        for i in range(0, min(len(p), 400), 40):
            fp = p[i:i + n]
            if len(fp) == n:
                out.append(fp)
            if len(out) >= count:
                return out
    return out


def np_pos(raw_pos, posmap):
    lo, hi = 0, len(posmap) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if posmap[mid] < raw_pos:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main():
    raw = norm(open(ARCHIVE, encoding="utf-8", errors="replace").read())
    arch = npstr(raw)
    # np-arch 下标 -> raw 下标 的映射
    posmap = []
    for i, c in enumerate(raw):
        if re.match(r"[0-9A-Za-z\u4e00-\u9fff]", c):
            posmap.append(i)
    posmap.append(len(raw))
    os.makedirs(OUTDIR, exist_ok=True)
    spans = {}
    # 第 1 章正文起点（已知：跳过目录区）
    first = None
    for fp in fingerprints(open(os.path.join(CHDIR, "Chapter1.tex"), encoding="utf-8").read()):
        pos = arch.find(fp, 12000)
        if pos >= 0:
            pos = posmap[pos]
            first = pos if first is None else min(first, pos)
    if first is None:
        sys.exit("cannot locate chapter 1")
    starts = {1: first}
    for ch in range(2, 53):
        path = os.path.join(CHDIR, "Chapter%d.tex" % ch)
        if not os.path.exists(path):
            break
        tex = open(path, encoding="utf-8").read()
        best = None
        for fp in fingerprints(tex):
            pos = arch.find(fp, np_pos(starts[max(1, ch - 1)], posmap) + 500)
            if pos >= 0:
                pos = posmap[pos]
                best = pos if best is None else min(best, pos)
        if best is None:
            # 退路：用上一章终点前 20k 之后搜索更短的 12 字指纹
            for fp in fingerprints(tex, n=12, count=8):
                pos = arch.find(fp, np_pos(starts[ch - 1], posmap) + 500)
                if pos >= 0:
                    pos = posmap[pos]
                    best = pos if best is None else min(best, pos)
        starts[ch] = best
    # 终点 = 下一章起点（最后一章到文本末尾）
    ordered = [(c, p) for c, p in starts.items() if p is not None]
    ordered.sort()
    for i, (c, p) in enumerate(ordered):
        end = ordered[i + 1][1] if i + 1 < len(ordered) else len(raw)
        spans["%d" % c] = [p, end]
        with open(os.path.join(OUTDIR, "Chapter%d.txt" % c), "w", encoding="utf-8") as f:
            f.write(raw[p:end])
        print("Chapter%-2d  %7d..%7d  len=%6d  head=%s" % (c, p, end, end - p, raw[p:p + 18]))
    with open(os.path.join(ROOT, "_attachments", "reference", "chapter_offsets.json"), "w", encoding="utf-8") as f:
        json.dump(spans, f, ensure_ascii=False, indent=1)
    print("wrote", len(spans), "chapters")


if __name__ == "__main__":
    main()
