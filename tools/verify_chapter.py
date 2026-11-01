#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""零删改校验：比对「原文」与「改造后章节」的可见内容字符序列。

用法
----
    python3 tools/verify_chapter.py 1
    python3 tools/verify_chapter.py 1 Chapters/VolumeI/Chapter1.tex
    python3 tools/verify_chapter.py 26 --orig-ref main
    python3 tools/verify_chapter.py 52 --context 3

规则
----
1. 「原文」默认从 git ref（默认 `main`）读取 `Chapters/VolumeI/ChapterN.tex`，
   也可用 `--orig-file` 指定文件；
2. 改造后文件中，所有**新增文字/新增图表**必须用成对注释标记包住：
       %<<<NEW
       ... 新增内容 ...
       %>>>NEW
   校验时会整体剔除这些块（标记本身是 LaTeX 注释，不影响排版）；
3. 两侧都剔除 LaTeX 注释、命令名、\label/\ref/\includegraphics 参数、
   花括号/方括号与空白，只保留内容字符（汉字、CJK 标点、拉丁字母、数字、
   引号/破折号/省略号/间隔号）；
4. 序列必须**逐字符完全一致**（只允许空白与段落切分不同）；
5. 退出码 0 = PASS；1 = FAIL（打印首个不一致位置与上下文）；2 = 用法/读取错误。

注意：本工具不修改任何文件，只读。
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CJK_KEEP = (
    r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
    r"\u3000-\u303f\uff00-\uffef"
    r"\u2018\u2019\u201c\u201d\u2014\u2026\u00b7"
    r"A-Za-z0-9]"
)
KEEP_RE = re.compile(CJK_KEEP)

# 参数整体不计入内容字符的宏（只影响编号/文件名，不是正文）
DROP_ARG_MACROS = ("label", "ref", "eqref", "pageref", "includegraphics", "index", "cite")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_new_blocks(text: str) -> str:
    """删除 %<<<NEW ... %>>>NEW 之间的新增内容。"""
    return re.sub(r"%<<<NEW.*?%>>>NEW", "\n", text, flags=re.S)


def strip_line_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        out.append(re.sub(r"(?<!\\)%.*", "", line))
    return "\n".join(out)


def remove_balanced(text: str, pos: int) -> str:
    """删除从 pos 处 '{' 开始的一个平衡花括号参数（含可选 [] 前缀）。"""
    while pos < len(text) and text[pos] in " \t\n":
        pos += 1
    # 可选参数：只有在能配平的情况下才跳过
    while pos < len(text) and text[pos] == "[":
        depth, i = 0, pos
        close = -1
        while i < len(text):
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
                if depth == 0:
                    close = i
                    break
            i += 1
        if close == -1:
            break
        pos = close + 1
        while pos < len(text) and text[pos] in " \t\n":
            pos += 1
    if pos >= len(text) or text[pos] != "{":
        return text
    depth, i = 0, pos
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[:pos] + text[i + 1:]
        i += 1
    raise ValueError("unbalanced braces near: " + text[pos:pos + 80])


def drop_arg_macros(text: str) -> str:
    for name in DROP_ARG_MACROS:
        pat = "\\" + name
        start = 0
        while True:
            i = text.find(pat, start)
            if i == -1:
                break
            # 确保是完整命令名（避免 \ref 匹配到 \refstepcounter 之类）
            j = i + len(pat)
            if j < len(text) and (text[j].isalpha() or text[j] == "@"):
                start = i + 1
                continue
            new = remove_balanced(text, j)
            if new == text:
                start = i + 1
                continue
            text = new
            start = i
    return text


def content_chars(text: str) -> str:
    text = strip_new_blocks(text)
    text = strip_line_comments(text)
    text = drop_arg_macros(text)
    text = re.sub(r"\\[A-Za-z]+", "", text)   # 其余命令名
    text = text.replace("\\", "")             # 控制符
    text = re.sub(r"[{}\[\]]", "", text)
    text = re.sub(r"\s+", "", text)
    return "".join(ch for ch in text if KEEP_RE.match(ch))


def first_diff(a: str, b: str):
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            return i
    if len(a) != len(b):
        return n
    return None


def load_original(chapter: int, orig_ref: str, orig_file: str | None) -> str:
    if orig_file:
        return read_text(Path(orig_file))
    rel = f"Chapters/VolumeI/Chapter{chapter}.tex"
    try:
        out = subprocess.run(
            ["git", "show", f"{orig_ref}:{rel}"],
            cwd=REPO, capture_output=True, check=True,
        )
        return out.stdout.decode("utf-8")
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(f"无法从 git {orig_ref}:{rel} 读取原文：{exc.stderr.decode(errors='ignore')}\n")
        raise SystemExit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description="零删改校验（原文 vs 改造后章节）")
    ap.add_argument("chapter", type=int, help="章号，如 1 / 26 / 52")
    ap.add_argument("transformed", nargs="?", help="改造后文件（默认 Chapters/VolumeI/ChapterN.tex）")
    ap.add_argument("--orig-ref", default="main", help="原文所在 git ref（默认 main）")
    ap.add_argument("--orig-file", default=None, help="直接指定原文文件（优先于 --orig-ref）")
    ap.add_argument("--context", type=int, default=2, help="失败时打印的上下文行数")
    args = ap.parse_args()

    tpath = Path(args.transformed) if args.transformed else REPO / f"Chapters/VolumeI/Chapter{args.chapter}.tex"
    if not tpath.exists():
        sys.stderr.write(f"找不到改造后文件：{tpath}\n")
        return 2

    orig_raw = load_original(args.chapter, args.orig_ref, args.orig_file)
    new_raw = read_text(tpath)
    orig = content_chars(orig_raw)
    new = content_chars(new_raw)

    if orig == new:
        print(f"[PASS] Chapter{args.chapter}: 内容字符 {len(new)}/{len(orig)} 完全一致（零删改）")
        print(f"       原文 {args.orig_ref}:Chapters/VolumeI/Chapter{args.chapter}.tex；改造后 {tpath.relative_to(REPO)}")
        return 0

    pos = first_diff(orig, new)
    print(f"[FAIL] Chapter{args.chapter}: 内容字符不一致")
    print(f"       原文长度 {len(orig)}，改造后 {len(new)}，首个差异位置 {pos}")
    lo = max(0, pos - 60)
    print(f"       原文上下文: …{orig[lo:pos + 60]}…")
    print(f"       改造上下文: …{new[lo:pos + 60]}…")
    if pos < len(orig) and pos < len(new):
        print(f"       原文字符 {orig[pos]!r} vs 改造字符 {new[pos]!r}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
