#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为第 N 章生成单章编译入口 preview/chapter-N/check.tex（若已存在则不覆盖）。

用法：python3 tools/make_chapter_check.py 4 5 6      或   --range 4-11
"""
import argparse
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "preview", "chapter-2", "check.tex")


def make(n):
    outdir = os.path.join(ROOT, "preview", "chapter-%d" % n)
    out = os.path.join(outdir, "check.tex")
    if os.path.exists(out):
        print("exists:", out)
        return
    os.makedirs(outdir, exist_ok=True)
    s = open(TEMPLATE, encoding="utf-8").read()
    s = re.sub(r"第 \d+ 章", "第 %d 章" % n, s)
    s = re.sub(r"\\setcounter\{chapter\}\{\d+\}", r"\\setcounter{chapter}{%d}" % (n - 1), s)
    s = re.sub(r"Chapters/VolumeI/Chapter\d+\.tex", "Chapters/VolumeI/Chapter%d.tex" % n, s)
    s = re.sub(r"章号：第 \d+ 章 → \d+", "章号：第 %d 章 → %d" % (n, n - 1), s)
    open(out, "w", encoding="utf-8").write(s)
    print("wrote:", out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*", type=int)
    ap.add_argument("--range", dest="rng")
    a = ap.parse_args()
    if a.rng:
        lo, hi = a.rng.split("-")
        for n in range(int(lo), int(hi) + 1):
            make(n)
    for n in a.chapters:
        make(n)


if __name__ == "__main__":
    main()
