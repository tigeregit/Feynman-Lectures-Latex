#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""零删除验证：抽取 Chapter2.tex 原文与改造后正文的“可见内容字符序列”，逐节比对。

口径：
- 内容字符 = CJK 汉字 + CJK 标点 + 拉丁字母/数字 + 少数保留符号；
- 去掉 LaTeX 命令名、环境名、花括号、列表标签方括号、空白、注释；
- “新增文字”整体剔除：\\chapterintro / \\readingpath / \\runin / \\enterm / \\figsource
  的参数，summarybox / conceptmap / figure / table / tikzpicture 环境整体，\\label 参数；
- 原文中的 \\footnote 文本、\\aside 文本、\\pullquote 文本、\\item[...] 标签内的原文
  均计入（它们都是原文文字，只是换了呈现方式）。
退出码 0 = 全部一致。
"""
import re
import sys
import difflib
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SRC = REPO / "Chapters/VolumeI/Chapter2.tex"
BODY = HERE / "ch2-pilot-body.tex"

# 原文行号（1-based）：§2-1 正文 5-25；§2-3 正文 72-82
SECTIONS = {"§2-1 引言": (5, 25, "引言"), "§2-3 量子物理学": (72, 82, "量子物理学")}

# 视为“新增文字”的参数宏（其参数不计入原文序列）
NEW_ARG_MACROS = ["chapterintro", "readingpath", "runin", "enterm", "figsource", "label"]
# 视为“新增内容”的整体环境
NEW_ENVS = ["summarybox", "conceptmap", "figure", "table", "tikzpicture", "center"]

KEEP_RE = re.compile(
    r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"      # CJK 统一表意文字
    r"\u3000-\u303f\uff00-\uffef"                     # CJK 标点 / 全角符号
    r"\u2018\u2019\u201c\u201d\u2014\u2026\u00b7"     # 弯引号、破折号、省略号、间隔号
    r"A-Za-z0-9]"                                     # 拉丁字母数字
)


def read(path):
    return path.read_text(encoding="utf-8")


def strip_comments(text):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in text.splitlines())


def remove_balanced_arg(text, pos):
    """从 pos 处的 '{' 开始删除一个平衡花括号参数，返回新文本。"""
    assert text[pos] == "{", (pos, text[pos - 40:pos + 40])
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


def remove_new_content(text):
    """删除新增文字/环境，返回剩余文本。"""
    # 1) 删除整体环境（环境名固定，从 \begin{env} 删到 \end{env}）
    for env in NEW_ENVS:
        begin, end = "\\begin{%s}" % env, "\\end{%s}" % env
        while begin in text:
            i = text.index(begin)
            j = text.find(end, i)
            if j == -1:
                raise ValueError("unclosed env: " + env)
            text = text[:i] + "\n" + text[j + len(end):]
    # 2) 删除 \begin{...}/\end{...} 包装（保留环境内文字）
    text = re.sub(r"\\(?:begin|end)\{[^}]*\}", "", text)
    # 3) 删除新增宏的参数（可带一个 [] 可选参数）
    for name in NEW_ARG_MACROS:
        pat = "\\" + name
        while pat in text:
            i = text.index(pat)
            j = i + len(pat)
            while j < len(text) and text[j] in " \t\n":
                j += 1
            while j < len(text) and text[j] == "[":
                k = text.index("]", j)
                j = k + 1
                while j < len(text) and text[j] in " \t\n":
                    j += 1
            if j < len(text) and text[j] == "{":
                text = remove_balanced_arg(text, j)
            else:
                text = text[:i] + text[j:]
    return text


def content_chars(text):
    """去掉 LaTeX 命令/括号/空白后，抽取内容字符序列。"""
    text = strip_comments(text)
    text = re.sub(r"\\[A-Za-z]+", "", text)   # 命令名
    text = text.replace("\\", "")             # 其余控制符
    text = re.sub(r"[{}\[\]]", "", text)      # 花括号、列表标签方括号
    text = re.sub(r"\s+", "", text)           # 空白
    return "".join(ch for ch in text if KEEP_RE.match(ch))


def slice_sections(text):
    """按 \\section{...} 切分正文，返回 {标题: 内容}。"""
    result = {}
    ms = list(re.finditer(r"\\section\{", text))
    starts = [m.start() for m in ms] + [len(text)]
    for idx, m in enumerate(ms):
        i = m.end() - 1
        depth, j = 0, i
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        result[text[i + 1:j]] = text[j + 1:starts[idx + 1]]
    return result


def main():
    src_lines = read(SRC).splitlines()
    body = read(BODY)
    bodies = slice_sections(body)
    print("原文：%s" % SRC)
    print("改造：%s" % BODY)
    print("改造正文 section：" + "、".join(bodies))
    print()
    ok_all = True
    for name, (a, b, title) in SECTIONS.items():
        if title not in bodies:
            print(f"[FAIL] {name}: 找不到 section {{{title}}}")
            ok_all = False
            continue
        orig_chars = content_chars("\n".join(src_lines[a - 1:b]))
        trans = content_chars(remove_new_content(bodies[title]))
        same = orig_chars == trans
        print(f"[{'PASS' if same else 'FAIL'}] {name}：原文 {len(orig_chars)} 字符 / 改造 {len(trans)} 字符")
        if not same:
            ok_all = False
            sm = difflib.SequenceMatcher(None, orig_chars, trans, autojunk=False)
            for tag, i1, i2, j1, j2 in sm.get_opcodes():
                if tag == "equal":
                    continue
                print(f"    {tag}: 原文[{i1}:{i2}]={orig_chars[i1:i2]!r} -> 改造[{j1}:{j2}]={trans[j1:j2]!r}")
                ctx = orig_chars[max(0, i1 - 30):i1]
                print(f"      原文上下文: …{ctx}【此处】{orig_chars[i1:i1 + 30]}…")
    print()
    print("结论：" + ("全部一致，零删除验证通过。" if ok_all else "存在差异，需要修正。"))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
