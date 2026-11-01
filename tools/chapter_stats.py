#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""改造前后统计：段落/列表/小标题/术语/新增文字/选读比例等。

用法
----
    python3 tools/chapter_stats.py 1
    python3 tools/chapter_stats.py 1 --orig-ref main --json
    python3 tools/chapter_stats.py 26 --md docs/analysis/chapter-26-notes.md

口径
----
- 原文汉字数 = git ref（默认 main）中该章 CJK 汉字总数；
- 改造后原文汉字数 = 改造文件剔除 `%<<<NEW ... %>>>NEW` 新增块后的 CJK 汉字数
  （必须与原文相等，配合 tools/verify_chapter.py 使用）；
- 新增文字汉字数 = 新增块内 CJK 汉字数（导读/阅读路径/小标题/小结/图注提示/新增图表文字）；
- 正文段 = 剔除新增块、figure/wrapfigure/table/longtable/equation/align/summarybox/
  conceptmap/optional 等结构后的顶层空行块（含汉字者）；
- 列表项 = `\item` 出现次数（含 \item[...] 自定义标签）；
- 选读汉字数 = optional 环境内 CJK 汉字数。
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

STRUCT_ENVS = ("figure", "wrapfigure", "table", "longtable", "equation", "equation*",
               "align", "align*", "flalign", "gather", "multline", "eqnarray",
               "summarybox", "keybox", "conceptmap", "tikzpicture", "center")


def cjk(text: str) -> int:
    return len(CJK_RE.findall(text))


def strip_new_blocks(text: str) -> str:
    return re.sub(r"%<<<NEW.*?%>>>NEW", "\n", text, flags=re.S)


def strip_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in text.splitlines())


def drop_structured(text: str) -> str:
    """删除图/表/公式/框类等结构环境（整体），保留正文。"""
    for env in STRUCT_ENVS:
        pat = re.compile(r"\\begin\{%s\}.*?\\end\{%s\}" % (re.escape(env), re.escape(env)), re.S)
        while True:
            new = pat.sub("\n", text)
            if new == text:
                break
            text = new
    text = re.sub(r"\\\[.*?\\\]", "\n", text, flags=re.S)
    text = re.sub(r"\\(?:begin|end)\{[^}]*\}", "", text)
    return text


def top_blocks(text: str):
    blocks, cur = [], []
    for line in text.splitlines():
        if line.strip() == "":
            if cur:
                blocks.append("\n".join(cur))
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append("\n".join(cur))
    return blocks


def load_original(chapter: int, ref: str, orig_file: str | None) -> str:
    if orig_file:
        return Path(orig_file).read_text(encoding="utf-8")
    rel = f"Chapters/VolumeI/Chapter{chapter}.tex"
    try:
        out = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=REPO,
                             capture_output=True, check=True)
        return out.stdout.decode("utf-8")
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(f"无法读取原文 {ref}:{rel}: {exc.stderr.decode(errors='ignore')}\n")
        raise SystemExit(2)


def compute(chapter: int, orig_ref: str, orig_file: str | None):
    new_raw = Path(REPO / f"Chapters/VolumeI/Chapter{chapter}.tex").read_text(encoding="utf-8")
    orig_raw = load_original(chapter, orig_ref, orig_file)

    new_blocks = re.findall(r"%<<<NEW(.*?)%>>>NEW", new_raw, flags=re.S)
    new_text = "\n".join(new_blocks)
    body = strip_new_blocks(new_raw)
    body_plain = drop_structured(strip_comments(body))
    blocks = [b for b in top_blocks(body_plain) if cjk(b) > 0]
    lens = [cjk(b) for b in blocks]

    # 原文段落：与改造后同口径
    orig_plain = drop_structured(strip_comments(orig_raw))
    orig_blocks = [b for b in top_blocks(orig_plain) if cjk(b) > 0]
    orig_lens = [cjk(b) for b in orig_blocks]

    optional = "\n".join(re.findall(r"\\begin\{optional\}(.*?)\\end\{optional\}", body, flags=re.S))
    body_chars = cjk(body)
    return {
        "chapter": chapter,
        "orig_cjk": cjk(orig_raw),
        "body_cjk": body_chars,
        "new_cjk": cjk(new_text),
        "new_ratio": round(cjk(new_text) / max(1, body_chars), 4),
        "orig_paras": len(orig_lens),
        "orig_avg": round(sum(orig_lens) / len(orig_lens), 1) if orig_lens else 0,
        "orig_max": max(orig_lens) if orig_lens else 0,
        "orig_over250": sum(1 for n in orig_lens if n > 250),
        "paras": len(lens),
        "avg": round(sum(lens) / len(lens), 1) if lens else 0,
        "max": max(lens) if lens else 0,
        "over250": sum(1 for n in lens if n > 250),
        "list_items": len(re.findall(r"\\item", body)),
        "runin": len(re.findall(r"\\runin\{", new_text)),
        "term": len(re.findall(r"\\term\{", body)),
        "keyidea": len(re.findall(r"\\keyidea\{", body)),
        "pullquote": len(re.findall(r"\\pullquote\{", body)),
        "aside": len(re.findall(r"\\aside\{", body)),
        "fighint": len(re.findall(r"\\fighint\{", new_text)),
        "summarybox": len(re.findall(r"\\begin\{summarybox\}", body)),
        "conceptmap": len(re.findall(r"\\begin\{conceptmap\}", body)),
        "optional_paras": len(re.findall(r"\\begin\{optional\}", body)),
        "optional_cjk": cjk(optional),
        "figures": len(re.findall(r"\\begin\{figure\}|\\begin\{wrapfigure\}", body)),
        "tables": len(re.findall(r"\\begin\{table\}|\\begin\{longtable\}", body)),
        "verify_ok": body_chars == cjk(orig_raw),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="改造前后章节统计")
    ap.add_argument("chapter", type=int)
    ap.add_argument("--orig-ref", default="main")
    ap.add_argument("--orig-file", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--md", default=None, help="把 Markdown 表格追加到该文件")
    args = ap.parse_args()
    d = compute(args.chapter, args.orig_ref, args.orig_file)

    if args.json:
        print(json.dumps(d, ensure_ascii=False, indent=2))
        return 0

    lines = [
        f"## Chapter{args.chapter} 改造前后统计",
        "",
        "| 指标 | 原文 | 改造后 |",
        "|---|---:|---:|",
        f"| 汉字数（原文文字） | {d['orig_cjk']} | {d['body_cjk']} |",
        f"| 段落/正文段数 | {d['orig_paras']} | {d['paras']} |",
        f"| 平均段长 | {d['orig_avg']} | {d['avg']} |",
        f"| 最长段 | {d['orig_max']} | {d['max']} |",
        f"| >250 字段落 | {d['orig_over250']} | {d['over250']} |",
        f"| 列表项 | 0 | {d['list_items']} |",
        f"| 段内小标题 `\\runin` | 0 | {d['runin']} |",
        f"| 术语 `\\term` | 0 | {d['term']} |",
        f"| 关键句 `\\keyidea` | 0 | {d['keyidea']} |",
        f"| 引文 `\\pullquote` | 0 | {d['pullquote']} |",
        f"| 页边注 `\\aside` | 0 | {d['aside']} |",
        f"| 小结框 `summarybox` | 0 | {d['summarybox']} |",
        f"| 新增概念图 | 0 | {d['conceptmap']} |",
        f"| 新增文字（汉字） | 0 | {d['new_cjk']}（占原文 {d['new_ratio']:.1%}） |",
        f"| 选读 `optional` | 0 | {d['optional_paras']} 段 / {d['optional_cjk']} 字 |",
        f"| 图 / 表 | {d['figures']} / {d['tables']} | {d['figures']} / {d['tables']} |",
        f"| 零删改（字符数） | — | {'PASS' if d['verify_ok'] else 'FAIL（需先跑 verify_chapter.py）'} |",
    ]
    md = "\n".join(lines) + "\n"
    print(md)
    if args.md:
        with open(args.md, "a", encoding="utf-8") as fh:
            fh.write("\n" + md)
        print(f"已追加到 {args.md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
