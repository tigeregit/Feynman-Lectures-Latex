#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《费曼物理学讲义（中文重排版）》文本可读性审计工具（仅用 Python3 标准库）。

用途
----
对 Chapters/VolumeI/Chapter1..52.tex、VolumeII/Chapter1.tex、VolumeIII/Chapter1.tex
做可复现的文本计量，输出到 docs/analysis/text/：
    01-总体统计.md
    02-长段落清单.csv
    03-列表化候选.csv
    04-纯文字墙节.csv
    05-强调与长句.md
    06-中英段落对照.csv
    06b-中英段落对齐明细.csv   （06 的附录明细）
    README.md

用法
----
    python3 tools/audit_text.py              # 生成全部产出
    python3 tools/audit_text.py --check      # 只打印口径自检，不写文件
    python3 tools/audit_text.py --en-dir DIR # 指定英文抓取目录（默认 _attachments/...）

统计口径（与产出文档中的"口径"一节一致）
--------------------------------------
* 段落 = LaTeX 源文件中由空行分隔的块，去掉图/表/展示公式/标题/脚注等结构内容后仍含汉字
  的正文块；一个块内若有 \\item，则按 item 再切成多个段落（列表项）。清洗后不含汉字的块
  （纯英文参考文献条目、纯结构块）不计入正文段落。
* 字数 = 汉字数 + 西文词数（连续拉丁字母串或数字串各计 1 词）；标点、行内公式、交叉引用
  编号不计。文档同时给出"汉字数"备查。
* 句 = 段落正文按 。！？ 切分后、含至少一个汉字的片段。
* 展示公式 = 顶层 equation / equation* / align / align* / flalign / gather / multline /
  eqnarray 环境与 \\[...\\]；aligned、split、cases 等作为公式内部结构不重复计数。
* 图 = figure + wrapfigure 环境数；表 = table + longtable 环境数（另报 tabular 数）。
* 内联公式 = 成对的 $...$ 数。
* 行号 = 源文件 1-based 行号；章行数按换行符计（与 wc -l 一致）。

约束：本工具不修改 Chapters/、主 tex、Figures/，也不做任何 git 操作。
"""
from __future__ import annotations

import argparse
import csv
import math
import os
import re
import statistics
from bisect import bisect_right
from collections import Counter

# ---------------------------------------------------------------------------
# 路径与常量
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTER_DIR = os.path.join(REPO_ROOT, "Chapters")
DEFAULT_EN_DIR = os.path.join(REPO_ROOT, "_attachments", "build-feynman", "audit", "en")
OUT_DIR = os.path.join(REPO_ROOT, "docs", "analysis", "text")

VOLUME_NAMES = {1: "第一卷", 2: "第二卷", 3: "第三卷"}

STRUCTURAL_ENVS = {
    # 图
    "figure", "figure*", "wrapfigure", "wrapfigure*",
    # 表
    "table", "table*", "longtable", "longtable*", "tabular", "tabular*", "tabularx",
    "tabu", "supertabular",
    # 展示公式（及公式内部结构）
    "equation", "equation*", "align", "align*", "flalign", "flalign*",
    "gather", "gather*", "multline", "multline*", "eqnarray", "eqnarray*",
    "displaymath", "math", "subequations", "aligned", "alignedat", "split",
    "cases", "array", "gathered",
    # 版面容器
    "minipage", "center",
}
TRANSPARENT_ENVS = {
    "small", "footnotesize", "scriptsize", "large", "Large", "LARGE",
    "quote", "quotation", "verse", "spacing", "enumerate", "itemize",
    "description", "flushleft", "flushright", "singlespace", "onehalfspace",
}
FORMULA_ENVS = {
    "equation", "equation*", "align", "align*", "flalign", "flalign*",
    "gather", "gather*", "multline", "multline*", "eqnarray", "eqnarray*",
    "displaymath", "math",
}
FIGURE_ENVS = {"figure", "figure*", "wrapfigure", "wrapfigure*"}
TABLE_ENVS = {"table", "table*", "longtable", "longtable*"}
TABULAR_ENVS = {"tabular", "tabular*", "tabularx", "tabu", "supertabular"}

ENV_EVENT_RE = re.compile(r"\\(begin|end)\s*\{([^{}]*)\}")
CMD_RE = re.compile(r"\\([A-Za-z]+)\*?")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
LATIN_WORD_RE = re.compile(r"[A-Za-z]+|\d+(?:\.\d+)?")
REF_RE = re.compile(r"\\ref\s*\{")
Uwave_RE = re.compile(r"\\uwave\s*\{")
FOOTNOTE_RE = re.compile(r"\\footnote\s*\{")
ITEM_RE = re.compile(r"\\item\b")
MATH_RUN_RE = re.compile(r"\x01+")

# 段落清洗时可"保留参数正文"的命令
TEXT_ARG_CMDS = {
    "uwave", "textbf", "textit", "emph", "underline", "text", "mbox",
    "textrm", "textnormal", "textsc", "textsuperscript", "textsubscript",
    "textup", "textsl", "textmd", "mathrm", "mathbf", "mathit", "mathsf",
    "mathtt", "operatorname", "mathnormal",
    # 单字符重音命令：\r{A} -> A
    "r", "c", "v", "u", "H", "b", "d", "t", "k",
}
# 只占位成空格的命令（间距、版式）
SPACE_CMDS = {
    "quad", "qquad", "enspace", "thinspace", "negthinspace", "medspace",
    "thickspace", "hfill", "vfill", "hskip", "vskip", "smallskip",
    "medskip", "bigskip", "noindent", "indent", "newline", "linebreak",
    "nolinebreak", "pagebreak", "clearpage", "newpage", "centering",
    "raggedright", "raggedleft", "normalsize", "small", "footnotesize",
    "tiny", "large", "Large", "LARGE", "huge", "Huge", "selectfont",
    "protect", "relax", "maketitle", "tableofcontents", "par",
}
MARKERS = "\x01\x02\x03\x04\x05\x06"

PARA_BINS = [
    ("1–50", 1, 50), ("51–100", 51, 100), ("101–150", 101, 150),
    ("151–200", 151, 200), ("201–250", 201, 250), ("251–300", 251, 300),
    ("301–400", 301, 400), ("401–500", 401, 500), ("501–800", 501, 800),
    ("801–1200", 801, 1200), ("1201+", 1201, 10 ** 9),
]
SENT_BINS = [
    ("1–10", 1, 10), ("11–20", 11, 20), ("21–30", 21, 30),
    ("31–40", 31, 40), ("41–50", 41, 50), ("51–70", 51, 70),
    ("71–99", 71, 99), ("100–149", 100, 149), ("150–199", 150, 199),
    ("200+", 200, 10 ** 9),
]

LONG_PARA = 300
LONG_PARA_P0 = 500
LONG_SENT = 80
TEXT_WALL = 1500


# ---------------------------------------------------------------------------
# 基础工具
# ---------------------------------------------------------------------------
def cjk_count(s: str) -> int:
    return len(CJK_RE.findall(s))


def is_cjk(ch: str) -> bool:
    return "\u4e00" <= ch <= "\u9fff"


def latin_word_count(s: str) -> int:
    return len(LATIN_WORD_RE.findall(s))


def zici_count(s: str) -> int:
    return cjk_count(s) + latin_word_count(s)


def quantile(values, q):
    if not values:
        return 0.0
    s = sorted(values)
    pos = (len(s) - 1) * q
    lo = int(math.floor(pos))
    hi = min(lo + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (pos - lo)


def fmt_int(x) -> str:
    return f"{int(round(x)):,}"


def fmt_pct(num, den) -> str:
    if not den:
        return "—"
    return f"{100.0 * num / den:.1f}%"


def one_line(s: str, limit: int = 0) -> str:
    t = re.sub(r"\s+", " ", s or "").strip()
    if limit and len(t) > limit:
        t = t[:limit] + "…"
    return t


# ---------------------------------------------------------------------------
# 章节清单
# ---------------------------------------------------------------------------
def chapter_files():
    out = []
    vol1 = os.path.join(CHAPTER_DIR, "VolumeI")
    for fn in os.listdir(vol1):
        m = re.fullmatch(r"Chapter(\d+)\.tex", fn)
        if not m:
            continue
        out.append((f"I-{int(m.group(1)):02d}", 1, int(m.group(1)),
                    os.path.join(vol1, fn)))
    out.sort(key=lambda x: x[2])
    for vol, sub in ((2, "VolumeII"), (3, "VolumeIII")):
        p = os.path.join(CHAPTER_DIR, sub, "Chapter1.tex")
        if os.path.exists(p):
            out.append((f"{'II' if vol == 2 else 'III'}-01", vol, 1, p))
    return out


# ---------------------------------------------------------------------------
# 环境扫描 / 掩码
# ---------------------------------------------------------------------------
def scan_envs(text):
    """返回 (env_records, structural_regions)。"""
    records = []
    stack = []
    struct_depth = 0
    struct_start = None
    regions = []
    for m in ENV_EVENT_RE.finditer(text):
        kind, name = m.group(1), m.group(2).strip()
        if kind == "begin":
            rec = {
                "name": name,
                "begin_pos": m.start(),
                "begin_end": m.end(),
                "parents": tuple(s["name"] for s in stack),
            }
            stack.append(rec)
            if name in STRUCTURAL_ENVS:
                if struct_depth == 0:
                    struct_start = m.start()
                struct_depth += 1
        else:
            idx = None
            for k in range(len(stack) - 1, -1, -1):
                if stack[k]["name"] == name:
                    idx = k
                    break
            if idx is None:
                continue
            rec = stack[idx]
            del stack[idx:]
            rec["end_pos"] = m.start()
            rec["end_end"] = m.end()
            records.append(rec)
            if name in STRUCTURAL_ENVS:
                struct_depth = max(0, struct_depth - 1)
                if struct_depth == 0 and struct_start is not None:
                    regions.append((struct_start, m.end()))
                    struct_start = None
    if struct_start is not None:
        regions.append((struct_start, len(text)))
    return records, regions


def find_display_brackets(text):
    """\\[...\\] 展示公式区间（排除 \\\\[2ex] 这类换行命令）。"""
    spans = []
    pos = 0
    open_re = re.compile(r"(?<!\\)\\\[")
    close_re = re.compile(r"(?<!\\)\\\]")
    while True:
        m = open_re.search(text, pos)
        if not m:
            break
        m2 = close_re.search(text, m.end())
        if not m2:
            spans.append((m.start(), len(text)))
            break
        spans.append((m.start(), m2.end()))
        pos = m2.end()
    return spans


def mask_spans(text, spans, marker):
    if not spans:
        return text
    chars = list(text)
    n = len(chars)
    for a, b in spans:
        a = max(0, a)
        b = min(b, n)
        for i in range(a, b):
            if chars[i] != "\n":
                chars[i] = marker
    return "".join(chars)


def find_heading(text, kind):
    out = []
    pat = re.compile(r"\\" + kind + r"\s*\*?\s*\{")
    for m in pat.finditer(text):
        i = m.end() - 1
        depth = 0
        j = i
        while j < len(text):
            ch = text[j]
            if ch == "\\":
                j += 2
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    out.append((text[i + 1:j], m.start(), i + 1, j, j + 1))
                    break
            j += 1
    return out


def clean_heading_title(raw):
    s = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?", " ", raw)
    s = s.replace("{", " ").replace("}", " ").replace("~", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


# ---------------------------------------------------------------------------
# 行内公式 / 脚注 / 注释
# ---------------------------------------------------------------------------
def find_inline_math(text):
    spans = []
    n = len(text)
    i = 0
    while i < n:
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "$":
            j = i + 1
            while j < n:
                c2 = text[j]
                if c2 == "\\":
                    j += 2
                    continue
                if c2 == "$":
                    break
                j += 1
            if j < n:
                spans.append((i, j + 1))
                i = j + 1
                continue
            i += 1
            continue
        i += 1
    return spans


def find_footnotes(text):
    spans = []
    for m in FOOTNOTE_RE.finditer(text):
        i = m.end() - 1
        depth = 0
        j = i
        while j < len(text):
            ch = text[j]
            if ch == "\\":
                j += 2
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    spans.append((m.start(), j + 1))
                    break
            j += 1
    return spans


def find_comments(text):
    spans = []
    for m in re.finditer(r"(?<!\\)%[^\n]*", text):
        spans.append((m.start(), m.end()))
    return spans


# ---------------------------------------------------------------------------
# 正文清洗
# ---------------------------------------------------------------------------
def _skip_ws(seg, i):
    n = len(seg)
    while i < n and seg[i] in " \t":
        i += 1
    return i


def _skip_optional(seg, i):
    n = len(seg)
    k = _skip_ws(seg, i)
    if k < n and seg[k] == "[":
        depth = 0
        j = k
        while j < n:
            ch = seg[j]
            if ch == "\\":
                j += 2
                continue
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    return j + 1
            j += 1
    return i


def _skip_balanced(seg, i):
    n = len(seg)
    if i >= n or seg[i] != "{":
        return None
    depth = 0
    j = i
    while j < n:
        ch = seg[j]
        if ch == "\\":
            j += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    return None


def normalize_pairs(pairs):
    tmp = []
    for ch, src in pairs:
        if ch in " \t\n\r\f\v":
            ch = " "
        if ch == " ":
            if not tmp or tmp[-1][0] == " ":
                continue
        tmp.append((ch, src))
    while tmp and tmp[-1][0] == " ":
        tmp.pop()
    out = []
    for idx, (ch, src) in enumerate(tmp):
        if ch == " ":
            prev = tmp[idx - 1][0] if idx > 0 else ""
            nxt = tmp[idx + 1][0] if idx + 1 < len(tmp) else ""
            if (is_cjk(prev) and is_cjk(nxt)) or nxt == "" or prev == "":
                continue
        out.append((ch, src))
    # 去掉段首残留标点（如手工题号命令被清掉后剩下的 "."）
    lead_punct = ".,、，。;；:：)])"
    while out and out[0][0] in lead_punct:
        out.pop(0)
    return out


def clean_segment(seg, abs_start):
    """清洗一个正文片段（结构环境/公式/脚注/注释已被掩码）。"""
    out = []
    srcs = []
    i = 0
    n = len(seg)
    uwave = 0
    while i < n:
        ch = seg[i]
        if ch in MARKERS:
            out.append(" ")
            srcs.append(abs_start + i)
            i += 1
            continue
        if ch == "\\":
            if i + 1 >= n:
                i += 1
                continue
            nxt = seg[i + 1]
            if nxt == "\\":
                out.append(" ")
                srcs.append(abs_start + i)
                i += 2
                continue
            if nxt in " \t\n":
                out.append(" ")
                srcs.append(abs_start + i)
                i += 2
                continue
            if nxt in "%&_#{}":
                out.append(nxt)
                srcs.append(abs_start + i)
                i += 2
                continue
            if nxt in ",;:!":
                out.append(" ")
                srcs.append(abs_start + i)
                i += 2
                continue
            m = CMD_RE.match(seg, i)
            if not m:
                out.append(" ")
                srcs.append(abs_start + i)
                i += 2
                continue
            cmd = m.group(1)
            j = m.end()
            if cmd == "uwave":
                uwave += 1
            if cmd in TEXT_ARG_CMDS:
                i = j  # 保留参数正文，只丢命令名
                continue
            if cmd in SPACE_CMDS:
                out.append(" ")
                srcs.append(abs_start + i)
                i = j
                continue
            if cmd == "item":
                i = _skip_optional(seg, j)
                out.append(" ")
                srcs.append(abs_start + m.start())
                continue
            if cmd in ("begin", "end"):
                k = j
                consumed = False
                for _ in range(3):  # begin{env} 后面可能跟 [..] 或 {..} 参数
                    k2 = _skip_ws(seg, k)
                    if k2 < n and seg[k2] == "[":
                        e = _skip_optional(seg, k2)
                    elif k2 < n and seg[k2] == "{":
                        e = _skip_balanced(seg, k2)
                    else:
                        break
                    if e is None:
                        break
                    consumed = True
                    k = e
                i = k if consumed else j
                out.append(" ")
                srcs.append(abs_start + m.start())
                continue
            # 其他命令：丢弃命令名及紧随的参数（最多 2 组）
            k = j
            while k < n and seg[k] in " \t":
                k += 1
            consumed = False
            while k < n and seg[k] in "[{":
                if seg[k] == "[":
                    e = _skip_optional(seg, k)
                else:
                    e = _skip_balanced(seg, k)
                if e is None:
                    break
                consumed = True
                k = e
                while k < n and seg[k] in " \t":
                    k += 1
            i = k if consumed else j
            out.append(" ")
            srcs.append(abs_start + m.start())
            continue
        if ch in "{}[]":
            i += 1
            continue
        out.append(ch)
        srcs.append(abs_start + i)
        i += 1
    pairs = normalize_pairs(list(zip(out, srcs)))
    text = "".join(ch for ch, _ in pairs)
    return {
        "text": text,
        "pairs": pairs,
        "cjk": cjk_count(text),
        "latin": latin_word_count(text),
        "zici": zici_count(text),
        "uwave": uwave,
    }


def split_sentences(text, pairs):
    sents = []
    cur = []
    for ch, src in pairs:
        cur.append((ch, src))
        if ch in "。！？":
            sents.append(cur)
            cur = []
    if cur:
        sents.append(cur)
    out = []
    for sent_pairs in sents:
        while sent_pairs and sent_pairs[0][0] == " ":
            sent_pairs = sent_pairs[1:]
        while sent_pairs and sent_pairs[-1][0] == " ":
            sent_pairs = sent_pairs[:-1]
        if not sent_pairs:
            continue
        s = "".join(ch for ch, _ in sent_pairs)
        if not cjk_count(s):
            continue
        out.append({
            "text": s,
            "zici": zici_count(s),
            "cjk": cjk_count(s),
            "src": sent_pairs[0][1],
        })
    return out


# ---------------------------------------------------------------------------
# 单章解析
# ---------------------------------------------------------------------------
def parse_chapter(key, vol, num, path):
    text = open(path, encoding="utf-8").read()
    n_lines = text.count("\n")
    line_starts = [0]
    for m in re.finditer(r"\n", text):
        line_starts.append(m.end())

    def pos_to_line(pos):
        return bisect_right(line_starts, pos)

    chapters_h = find_heading(text, "chapter")
    title = clean_heading_title(chapters_h[0][0]) if chapters_h else ""
    sections = []
    for raw, cpos, _ts, _te, _fend in find_heading(text, "section"):
        sections.append({
            "title": clean_heading_title(raw),
            "pos": cpos,
            "line": pos_to_line(cpos),
            "star": bool(re.match(r"\\section\s*\*", text[cpos:cpos + 12])),
        })

    env_records, struct_regions = scan_envs(text)
    bracket_spans = find_display_brackets(text)
    heading_spans = []
    for kind in ("chapter", "section", "subsection"):
        for _raw, cpos, _ts, _te, fend in find_heading(text, kind):
            heading_spans.append((cpos, fend))

    disp_eq_positions = []
    for rec in env_records:
        if rec["name"] in FORMULA_ENVS and not any(p in FORMULA_ENVS for p in rec["parents"]):
            disp_eq_positions.append(rec["begin_pos"])
    disp_eq_positions += [a for a, _b in bracket_spans]
    disp_eq_positions.sort()

    figure_positions = [r["begin_pos"] for r in env_records if r["name"] in FIGURE_ENVS]
    table_positions = [r["begin_pos"] for r in env_records if r["name"] in TABLE_ENVS]
    tabular_positions = [r["begin_pos"] for r in env_records if r["name"] in TABULAR_ENVS]

    # 先掩标题，再找脚注（脚注可能藏在展示公式里，必须在结构掩码之前找）
    masked = mask_spans(text, heading_spans, "\x02")
    footnote_spans = find_footnotes(masked)
    footnote_positions = [a for a, _ in footnote_spans]
    footnote_cjk = sum(cjk_count(text[a:b]) for a, b in footnote_spans)
    masked = mask_spans(masked, footnote_spans, "\x03")
    masked = mask_spans(masked, struct_regions + bracket_spans, "\x02")
    masked = mask_spans(masked, find_comments(masked), "\x04")
    math_spans = find_inline_math(masked)
    math_positions = [(a + b) // 2 for a, b in math_spans]
    masked = mask_spans(masked, math_spans, "\x01")

    # 正文内的强调/引用（标题、图表题、公式里的不计入正文口径）
    uwave_positions = [m.start() for m in Uwave_RE.finditer(masked)]
    ref_positions = [m.start() for m in REF_RE.finditer(masked)]
    item_positions_all = [m.start() for m in ITEM_RE.finditer(masked)]

    # 全文原始计数（含图表标题、公式内）
    raw_uwave = len(Uwave_RE.findall(text))
    raw_refs = len(REF_RE.findall(text))
    raw_inline_math = len(find_inline_math(text))
    # 正文汉字与原始汉字的差额来源（用于 01 的对照说明）
    struct_cjk = sum(cjk_count(text[a:b]) for a, b in struct_regions + bracket_spans)
    heading_cjk = sum(cjk_count(text[a:b]) for a, b in heading_spans)
    masked_no_struct = mask_spans(text, struct_regions + bracket_spans, "\x02")
    ref_label_cjk = sum(
        cjk_count(m.group(1))
        for m in re.finditer(r"\\(?:ref|label|eqref|cite)\s*\{([^{}]*)\}",
                             masked_no_struct))

    # 分空行块
    lines = masked.split("\n")
    offsets = []
    acc = 0
    for ln in lines:
        offsets.append(acc)
        acc += len(ln) + 1
    raw_blocks = []
    cur_start = None
    for idx, ln in enumerate(lines):
        if ln.strip() == "":
            if cur_start is not None:
                raw_blocks.append((cur_start, idx))
                cur_start = None
        else:
            if cur_start is None:
                cur_start = idx
    if cur_start is not None:
        raw_blocks.append((cur_start, len(lines)))

    sec_positions = [s["pos"] for s in sections]

    def section_of(pos):
        if not sec_positions or pos < sec_positions[0]:
            return -1
        return bisect_right(sec_positions, pos) - 1

    paragraphs = []
    for b_start, b_end in raw_blocks:
        abs_a = offsets[b_start]
        abs_b = offsets[b_end] if b_end < len(offsets) else len(masked)
        block_text = masked[abs_a:abs_b]
        item_pos = [m.start() for m in ITEM_RE.finditer(block_text)]
        cuts = [0] + item_pos + [len(block_text)]
        for si in range(len(cuts) - 1):
            sa, sb = cuts[si], cuts[si + 1]
            seg = block_text[sa:sb]
            if not seg.strip("\n "):
                continue
            cleaned = clean_segment(seg, abs_a + sa)
            if cleaned["cjk"] == 0 or not cleaned["pairs"]:
                continue
            p_a, p_b = abs_a + sa, abs_a + sb
            first_pos = cleaned["pairs"][0][1]
            sec_idx = section_of(first_pos)
            para = {
                "chapter_key": key,
                "volume": vol,
                "chapter_num": num,
                "start_line": pos_to_line(cleaned["pairs"][0][1]),
                "end_line": pos_to_line(cleaned["pairs"][-1][1]),
                "text": cleaned["text"],
                "cjk": cleaned["cjk"],
                "latin": cleaned["latin"],
                "zici": cleaned["zici"],
                "uwave": cleaned["uwave"],
                "is_list_item": si > 0,
                "raw": seg,
                "section_idx": sec_idx,
                "disp_eq": sum(1 for p in disp_eq_positions if p_a <= p < p_b),
                "figure": sum(1 for p in figure_positions if p_a <= p < p_b),
                "table": sum(1 for p in table_positions if p_a <= p < p_b),
                "tabular": sum(1 for p in tabular_positions if p_a <= p < p_b),
                "inline_math": sum(1 for p in math_positions if p_a <= p < p_b),
                "footnote": sum(1 for p in footnote_positions if p_a <= p < p_b),
            }
            para["sentences"] = split_sentences(cleaned["text"], cleaned["pairs"])
            para["n_sent"] = len(para["sentences"])
            paragraphs.append(para)

    # 节聚合
    sec_stats = []
    for si, sec in enumerate(sections):
        sec_stats.append({
            "idx": si, "title": sec["title"], "line": sec["line"], "star": sec["star"],
            "paras": [], "zici": 0, "cjk": 0, "n_long300": 0, "max_para": 0,
            "sent_lens": [], "disp_eq": 0, "figure": 0, "table": 0,
            "inline_math": 0, "uwave": 0, "footnote": 0,
        })
    for para in paragraphs:
        si = para["section_idx"]
        para["section_title"] = sections[si]["title"] if si >= 0 else "（章首未分节）"
        if si >= 0:
            st = sec_stats[si]
            st["paras"].append(para)
            st["zici"] += para["zici"]
            st["cjk"] += para["cjk"]
            if para["zici"] > LONG_PARA:
                st["n_long300"] += 1
            st["max_para"] = max(st["max_para"], para["zici"])
            st["sent_lens"].extend(s["zici"] for s in para["sentences"])
    for pos in disp_eq_positions:
        si = section_of(pos)
        if si >= 0:
            sec_stats[si]["disp_eq"] += 1
    for pos in figure_positions:
        si = section_of(pos)
        if si >= 0:
            sec_stats[si]["figure"] += 1
    for pos in table_positions:
        si = section_of(pos)
        if si >= 0:
            sec_stats[si]["table"] += 1
    for pos in math_positions:
        si = section_of(pos)
        if si >= 0:
            sec_stats[si]["inline_math"] += 1
    for pos in uwave_positions:
        si = section_of(pos)
        if si >= 0:
            sec_stats[si]["uwave"] += 1
    for pos in footnote_positions:
        si = section_of(pos)
        if si >= 0:
            sec_stats[si]["footnote"] += 1

    all_sent = [s["zici"] for p in paragraphs for s in p["sentences"]]
    body_cjk = sum(p["cjk"] for p in paragraphs)
    body_zici = sum(p["zici"] for p in paragraphs)
    return {
        "key": key,
        "cjk": body_cjk,
        "zici": body_zici,
        "volume": vol,
        "num": num,
        "path": os.path.relpath(path, REPO_ROOT),
        "title": title,
        "n_lines": n_lines,
        "n_sections": len(sections),
        "n_sections_star": sum(1 for s in sections if s["star"]),
        "n_raw_blocks": len(raw_blocks),
        "n_raw_cjk": cjk_count(text),
        "figures": len(figure_positions),
        "tables": len(table_positions),
        "tabulars": len(tabular_positions),
        "disp_eqs": len(disp_eq_positions),
        "inline_math": len(math_spans),
        "footnotes": len(footnote_spans),
        "footnote_cjk": footnote_cjk,
        "uwave": raw_uwave,
        "uwave_body": len(uwave_positions),
        "refs": raw_refs,
        "inline_math_raw": raw_inline_math,
        "struct_cjk": struct_cjk,
        "heading_cjk": heading_cjk,
        "ref_label_cjk": ref_label_cjk,
        "enumerate": len(re.findall(r"\\begin\{enumerate\}", text)),
        "itemize": len(re.findall(r"\\begin\{itemize\}", text)),
        "items": len(item_positions_all),
        "paragraphs": paragraphs,
        "sections": sec_stats,
        "sent_lens": all_sent,
        "line_starts": line_starts,
    }


def pos_to_line(chapter, pos):
    return bisect_right(chapter["line_starts"], pos)


# ---------------------------------------------------------------------------
# 英文段落重建（eFLP innerText 抓取文本 -> 段落）
# ---------------------------------------------------------------------------
EN_NOISE = {"MATHJAX", "◄", "▲", "►", "A", "B", "C", "D", "E", "Close"}
EN_SECTION_RE = re.compile(r"^(\d+)[–\-—](\d+)\s*(.*)$")
EN_FIGCAP_RE = re.compile(r"^(Fig\.|Figure|Table)\s*(\d+)[–\-—](\d+)")
EN_STOP_RE = re.compile(r"Copyright ©|Caltech and our partners")
EN_MATH_ITALIC_RE = re.compile(r"[\U0001D400-\U0001D7FF]")
EN_EQNUM_RE = re.compile(r"^\(\d+\.\d+\)$")
EN_LATIN2_RE = re.compile(r"[A-Za-z]{2,}")


def en_is_mathish(s):
    t = s.strip()
    if not t:
        return True
    if t in EN_NOISE:
        return True
    if EN_MATH_ITALIC_RE.search(t):
        return True
    if EN_EQNUM_RE.match(t):
        return True
    if len(t) <= 3:
        return True
    words = EN_LATIN2_RE.findall(t)
    letters = sum(len(w) for w in words)
    if letters == 0:
        return True
    nonspace = len(re.sub(r"\s", "", t))
    if " " not in t and letters < 0.45 * nonspace:
        return True
    return False


def en_block_is_nonprose(txt):
    """判断一个空行块是否是"非散文"内容（参考文献条目、数值表、公式表）。

    eFLP 抓取文本里，章末参考文献、正文数值表会以独立空行块出现；它们不是
    被翻译的正文段落，参与段落数对照会造成假差异，故在此过滤。
    """
    t = txt.strip()
    if not t:
        return True
    words = re.findall(r"[A-Za-z]+", t)
    n_words = len(words)
    if n_words < 4:
        return True
    if "↩" in t and n_words < 30:  # 短尾注/脚注条目
        return True
    if t.count("\t") >= 2:
        return True                      # 多制表符：表格行
    if re.match(r"^(?:Table|Fig\.|Figure)\s+\d+[–\-—]\d+", t):
        return True                      # 表格/图题块
    if re.match(r"^[A-Z][A-Za-z\-']+,\s+[A-Z]\.", t):
        return True                      # 参考文献条目（姓, 名首字母.）
    if n_words < 12 and re.search(r"[=≈∼]", t):
        return True                      # 公式/数值表小标题
    digits = sum(ch.isdigit() for ch in t)
    digit_ratio = digits / max(1, len(t))
    if digit_ratio > 0.12:
        return True                      # 数值表/公式表
    ref_hits = len(re.findall(
        r"\b(?:Journal|Press|Vol\.|pp\.|Phys\.|Amer\.|University|Society|Company|"
        r"Inc\.|Rev\.|Proc\.|Suppl\.|ed\.)\b", t))
    if ref_hits >= 2:
        return True                      # 参考文献条目
    if ref_hits >= 1 and re.search(r"\b(?:19|20)\d{2}\b", t):
        return True
    cap_ratio = sum(1 for w in words if w[0].isupper()) / n_words
    lower_ratio = sum(1 for w in words if w[0].islower()) / n_words
    if n_words >= 8 and cap_ratio > 0.65 and lower_ratio < 0.35:
        return True                      # 标题式条目
    return False


def parse_en(path):
    """把 eFLP innerText 抓取文本重建为英文段落。

    抓取文本的结构（important）：
      * 空行分隔的是"块"（HTML 块级元素：段落 / 展示公式 / 图题 / 标题等）；
      * 行内公式会把正文切成多行（单换行），但不产生空行；
      * 行间展示公式会被 MathJax 拆成一行一个符号的"公式块"（有空行包裹）。

    重建规则：
      1) 跳过 MATHJAX 之前的导航区、章标题/节标题块、图/表题块、版权区；
      2) 纯公式块直接跳过；
      3) 含正文的块按"上一块最后一行是否句末标点 + 本块首行是否大写开头"
         决定是否另起一段；不满足则视为被展示公式切开的同段续文而合并。

    返回 dict：paras=[{text, words}]（保守合并后的段落，段落数下界），
               text_blocks=含正文的空行块数（段落数上界，公式切割会造成虚高）。
    """
    lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    start = 0
    for k, ln in enumerate(lines):
        if ln.strip() == "MATHJAX":
            start = k + 1
            break
    blocks = []
    cur = []
    for ln in lines[start:]:
        if ln.strip() == "":
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(ln)
    if cur:
        blocks.append(cur)

    paras = []
    buf = []
    prev_end_punct = True
    first_para_found = False
    n_text_blocks = 0
    for bi, blk in enumerate(blocks):
        keep = []
        stop = False
        for ln in blk:
            s = ln.strip()
            if EN_STOP_RE.search(s):
                stop = True
                break
            if s in EN_NOISE:
                continue
            if EN_SECTION_RE.match(s) and len(s) < 120:
                continue
            if EN_FIGCAP_RE.match(s):
                continue
            keep.append(s)
        if not keep:
            if stop:
                break
            continue
        joined = " ".join(keep)
        if not first_para_found:
            # 丢弃章名/节标题导航块：词数少、且最后一行没有句末标点
            words_n = len(joined.split())
            last_terminal = any(keep[-1].endswith(e) for e in
                                (".", "!", "?", '.”', ".’", '”', '."'))
            if not last_terminal and words_n < 30:
                continue
            first_para_found = True
        last_line = keep[-1]
        ends_punct = any(last_line.endswith(e) for e in
                         (".", "!", "?", ":", '.”', ".’", '”', '."', ".)", "?)"))
        texts = [s for s in keep if not en_is_mathish(s)]
        if not texts:
            if stop:
                break
            continue  # 纯公式块
        if en_block_is_nonprose(" ".join(texts)):
            if stop:
                break
            continue  # 参考文献/数值表等非散文块
        n_text_blocks += 1
        starts_upper = bool(re.match(r'''^[A-Z0-9"“ (\[‘]''', texts[0]))
        if not buf:
            buf.append(texts)
            prev_end_punct = ends_punct
            continue
        if prev_end_punct and starts_upper:
            paras.append(buf)
            buf = [texts]
        else:
            buf.append(texts)
        prev_end_punct = ends_punct
        if stop:
            break
    if buf:
        paras.append(buf)
    out = []
    for p in paras:
        txt = re.sub(r"\s+", " ", " ".join(" ".join(x) for x in p)).strip()
        if len(txt) > 40:
            out.append({"text": txt, "words": len(LATIN_WORD_RE.findall(txt))})
    return {"paras": out, "text_blocks": n_text_blocks}


# ---------------------------------------------------------------------------
# 中英段落对齐（动态规划）
# ---------------------------------------------------------------------------
def align_paragraphs(zh, en, ratio):
    """zh: [zici], en: [words]；ratio = 中文期望字数/英词。返回操作列表。"""
    n, m = len(en), len(zh)
    INF = float("inf")
    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    bt = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0
    PEN_MERGE2 = 0.22
    PEN_MERGE3 = 0.42
    PEN_SKIP = 0.70
    CAP = 1.6

    def match_cost(z, w):
        w = max(1, w)
        c = abs(math.log(max(1.0, z) / max(1.0, ratio * w)))
        return min(c, CAP)

    for i in range(n + 1):
        row = dp[i]
        for j in range(m + 1):
            base = row[j]
            if base == INF:
                continue
            if i < n and j < m:
                c = base + match_cost(zh[j], en[i])
                if c < dp[i + 1][j + 1] - 1e-12:
                    dp[i + 1][j + 1] = c
                    bt[i + 1][j + 1] = (i, j, "match")
            if i + 1 < n and j < m:
                c = base + match_cost(zh[j], en[i] + en[i + 1]) + PEN_MERGE2
                if c < dp[i + 2][j + 1] - 1e-12:
                    dp[i + 2][j + 1] = c
                    bt[i + 2][j + 1] = (i, j, "merge2")
            if i + 2 < n and j < m:
                c = base + match_cost(zh[j], en[i] + en[i + 1] + en[i + 2]) + PEN_MERGE3
                if c < dp[i + 3][j + 1] - 1e-12:
                    dp[i + 3][j + 1] = c
                    bt[i + 3][j + 1] = (i, j, "merge3")
            if i < n:
                c = base + PEN_SKIP
                if c < dp[i + 1][j] - 1e-12:
                    dp[i + 1][j] = c
                    bt[i + 1][j] = (i, j, "en_only")
            if j < m:
                c = base + PEN_SKIP
                if c < dp[i][j + 1] - 1e-12:
                    dp[i][j + 1] = c
                    bt[i][j + 1] = (i, j, "zh_only")
    ops = []
    i, j = n, m
    guard = 0
    while (i > 0 or j > 0) and guard < 100000:
        guard += 1
        prev = bt[i][j]
        if prev is None:
            if i > 0:
                ops.append(("en_only", i - 1, j))
                i -= 1
            else:
                ops.append(("zh_only", i, j - 1))
                j -= 1
            continue
        pi, pj, kind = prev
        ops.append((kind, pi, pj))
        i, j = pi, pj
    ops.reverse()
    return ops


def analyze_zh_en(chapter, en_paras, ratio):
    """中文段落按"对照单元"组织：同一 \\item 列表的连续列表项合并为一个单元。

    原因：英文原文的对应内容通常是一整段（例如把开普勒三定律写成一段），而中文
    版用 enumerate 拆成 3 个列表项；若不合并，DP 会把这些短列表项误判为"被合并"。
    """
    units = []
    for idx, p in enumerate(chapter["paragraphs"]):
        if p["is_list_item"] and units and units[-1]["list"]:
            units[-1]["zici"] += p["zici"]
            units[-1]["text"] += " " + p["text"]
            units[-1]["members"].append(idx)
        else:
            units.append({"zici": p["zici"], "text": p["text"],
                          "list": p["is_list_item"], "members": [idx]})
    zh = [u["zici"] for u in units]
    en = [p["words"] for p in en_paras]
    result = {
        "n_zh": len(zh), "n_en": len(en),
        "zh_total": sum(zh), "en_total": sum(en),
        "ratio": ratio,
        "merges": [], "n_match": 0, "n_merge": 0, "n_merged_en": 0,
        "n_zh_only": 0, "n_en_only": 0, "coverage": 0.0, "max_matched_en": -1,
    }
    if not zh or not en:
        return result
    # 先用长度覆盖率判断是否“未译完”（第二/三卷第一章是节选试译）：
    # 覆盖率 = 中文字数 / (换算比 × 英文词数)，正常完整翻译应接近 1.0
    expected_zh = ratio * result["en_total"]
    len_coverage = (result["zh_total"] / expected_zh) if expected_zh else 0.0
    if len_coverage < 0.70:
        result["coverage"] = len_coverage
        result["partial"] = True
        result["merges"] = []
        result["n_match"] = 0
        return result
    result["coverage"] = min(1.0, len_coverage)
    ops = align_paragraphs(zh, en, ratio)
    for kind, i, j in ops:
        if kind == "match":
            result["n_match"] += 1
            if i is not None:
                result["max_matched_en"] = max(result["max_matched_en"], i)
        elif kind in ("merge2", "merge3"):
            result["n_match"] += 1
            k_en = 2 if kind == "merge2" else 3
            en_idx = [i + t for t in range(k_en)]
            result["max_matched_en"] = max(result["max_matched_en"], en_idx[-1])
            en_words = sum(en[t] for t in en_idx)
            expect = ratio * en_words
            z = zh[j]
            dev = abs(z - expect) / max(1.0, expect)
            indiv_dev = min(abs(z / max(1.0, ratio * en[t]) - 1.0) for t in en_idx)
            if dev < 0.25 and indiv_dev > 0.30:
                conf = "高"
            elif dev < 0.40:
                conf = "中"
            else:
                conf = "低"
            result["merges"].append({
                "zh_index": units[j]["members"][0], "zh_unit": j,
                "en_index": en_idx, "en_words": en_words,
                "zh_zici": z, "expect": expect, "dev": dev, "conf": conf,
                "kind": kind,
            })
            result["n_merge"] += 1
            result["n_merged_en"] += k_en
        elif kind == "zh_only":
            result["n_zh_only"] += 1
        elif kind == "en_only":
            result["n_en_only"] += 1
    return result


# ---------------------------------------------------------------------------
# 列表化候选检测
# ---------------------------------------------------------------------------
CN_NUM = "一二三四五六七八九十"
ORD_RE = re.compile(r"第([" + CN_NUM + r"]+)(?=[、，,：:.．])")
# 跨段题型：第一定律：/第二点：……（序数后跟 0-4 个非标点字符再接冒号/顿号）
CROSS_ORD_RE = re.compile(r"^第([" + CN_NUM + r"]+)[^，。！？、：:]{0,4}[：:，,、]")
BRACKET_RE = re.compile(r"[（(]\s*(\d{1,2})\s*[)）]")
YISHI_RE = re.compile(r"([一二三四五六七八九])是(?=[，,、：:])")
ROMAN_RE = re.compile(r"\\romannumeral\s*([0-9ivxIVX]+)")
SEQ_WORDS = ["首先", "其次", "再次", "然后", "接着", "最后", "最终", "此后"]
DIGIT_HEAD_RE = re.compile(r"^\s*(\d{1,2})\s*[.、．]")
SENT_START_MARKERS = [
    "但是", "但", "然而", "不过", "因此", "所以", "于是", "现在", "让我们",
    "另一方面", "换句话说", "这就是说", "例如", "比如", "首先", "其次",
    "最后", "总之", "事实上", "实际上", "当然", "显然", "相反", "同时",
    "此外", "而且", "并且", "因为", "由于", "如果", "假如", "由此可见",
    "为此", "具体来说", "更准确地说", "重要的是",
]


BRACKET_VALID_PREV = set("。；：，、（(\n\t \u3000、；：")


def bracket_markers(text):
    """只取"位于句首/分句首"的括号编号，避免把"式（3）"这类引用误判为列表。"""
    out = []
    for m in BRACKET_RE.finditer(text):
        prev = text[m.start() - 1] if m.start() > 0 else ""
        if prev == "" or prev in BRACKET_VALID_PREV:
            out.append(m.group(1))
    return out


def detect_para_markers(para):
    text = para["text"]
    raw = para.get("raw", "")
    found = []
    ms = ORD_RE.findall(text)
    if len(ms) >= 2:
        found.append(("中文序数（第X）", "第" + "/第".join(ms), f"出现 {len(ms)} 处"))
    ms = bracket_markers(text)
    if len(ms) >= 2:
        found.append(("括号序号", "/".join(ms), f"出现 {len(ms)} 处"))
    ms = YISHI_RE.findall(text)
    if len(ms) >= 2:
        found.append(("一是/二是", "/".join(x + "是" for x in ms), f"出现 {len(ms)} 处"))
    seq = [w for w in SEQ_WORDS if w in text]
    if len(seq) >= 2:
        found.append(("顺序词", "/".join(seq), f"出现 {len(seq)} 类"))
    m = re.match(r"\s*\\uppercase\s*\\expandafter\s*\{\\romannumeral\s*([0-9ivxIVX]+)",
                 raw)
    if m:
        found.append(("手工罗马序号", m.group(1), "非 LaTeX 列表，手写题号"))
    m = DIGIT_HEAD_RE.match(text)
    if m:
        found.append(("段首数字序号", m.group(1) + ".", "手写序号"))
    if text.count("；") >= 5 and para["n_sent"] <= 4:
        found.append(("分号并列", f"；×{text.count('；')}", "长句内并列举证"))
    return found


def _para_start_key(p):
    text = p["text"]
    raw = p.get("raw", "")
    m = DIGIT_HEAD_RE.match(text)
    if m:
        return ("跨段数字序号", int(m.group(1)))
    m = ORD_RE.match(text)
    if m:
        return ("跨段中文序数", CN_NUM.find(m.group(1)))
    m = CROSS_ORD_RE.match(text)
    if m:
        return ("跨段中文序数", CN_NUM.find(m.group(1)))
    m = BRACKET_RE.match(text)
    if m:
        return ("跨段括号序号", int(m.group(1)))
    m = ROMAN_RE.search(raw)
    if m and re.match(r"^\s*\\uppercase", raw):
        val = m.group(1)
        try:
            return ("跨段罗马序号", int(val) if val.isdigit() else -1)
        except ValueError:
            return ("跨段罗马序号", -1)
    for k, w in enumerate(("首先", "其次", "再次", "然后", "最后")):
        if text.startswith(w):
            return ("跨段顺序词", k)
    return None


def detect_cross_para_markers(paras):
    out = []
    n = len(paras)
    i = 0
    while i < n:
        key = _para_start_key(paras[i])
        if key is None:
            i += 1
            continue
        family, first_val = key
        run = [paras[i]]
        j = i + 1
        while j < n:
            key2 = _para_start_key(paras[j])
            if key2 is None or key2[0] != family:
                break
            expect = first_val + len(run) if family != "跨段顺序词" else key2[1]
            if key2[1] == expect or (family == "跨段顺序词" and key2[1] >= run[-1][1] if _para_start_key(run[-1]) else False):
                run.append(paras[j])
                j += 1
            else:
                break
        if len(run) >= 2:
            out.append({"family": family, "paras": run})
            i = j
        else:
            i += 1
    return out


# ---------------------------------------------------------------------------
# 全量分析
# ---------------------------------------------------------------------------
def build_analysis(en_dir=None):
    en_dir = en_dir or DEFAULT_EN_DIR
    chapters = []
    for key, vol, num, path in chapter_files():
        chapters.append(parse_chapter(key, vol, num, path))

    all_paras = [p for c in chapters for p in c["paragraphs"]]
    all_sents = [s for c in chapters for p in c["paragraphs"] for s in p["sentences"]]
    totals = {
        "chapters": len(chapters),
        "lines": sum(c["n_lines"] for c in chapters),
        "raw_cjk": sum(c["n_raw_cjk"] for c in chapters),
        "sections": sum(c["n_sections"] for c in chapters),
        "sections_star": sum(c["n_sections_star"] for c in chapters),
        "sections_plain": sum(c["n_sections"] - c["n_sections_star"] for c in chapters),
        "raw_blocks": sum(c["n_raw_blocks"] for c in chapters),
        "paragraphs": len(all_paras),
        "list_items": sum(1 for p in all_paras if p["is_list_item"]),
        "cjk": sum(p["cjk"] for p in all_paras),
        "zici": sum(p["zici"] for p in all_paras),
        "sentences": len(all_sents),
        "figures": sum(c["figures"] for c in chapters),
        "tables": sum(c["tables"] for c in chapters),
        "tabulars": sum(c["tabulars"] for c in chapters),
        "disp_eqs": sum(c["disp_eqs"] for c in chapters),
        "inline_math": sum(c["inline_math"] for c in chapters),
        "inline_math_raw": sum(c["inline_math_raw"] for c in chapters),
        "footnotes": sum(c["footnotes"] for c in chapters),
        "footnote_cjk": sum(c["footnote_cjk"] for c in chapters),
        "struct_cjk": sum(c["struct_cjk"] for c in chapters),
        "heading_cjk": sum(c["heading_cjk"] for c in chapters),
        "ref_label_cjk": sum(c["ref_label_cjk"] for c in chapters),
        "uwave": sum(c["uwave"] for c in chapters),
        "uwave_body": sum(c["uwave_body"] for c in chapters),
        "refs": sum(c["refs"] for c in chapters),
        "enumerate": sum(c["enumerate"] for c in chapters),
        "itemize": sum(c["itemize"] for c in chapters),
        "items": sum(c["items"] for c in chapters),
    }
    v1ch = [c for c in chapters if c["volume"] == 1]
    totals["vol1"] = {
        "lines": sum(c["n_lines"] for c in v1ch),
        "raw_cjk": sum(c["n_raw_cjk"] for c in v1ch),
        "raw_blocks": sum(c["n_raw_blocks"] for c in v1ch),
        "sections": sum(c["n_sections"] for c in v1ch),
        "paragraphs": sum(len(c["paragraphs"]) for c in v1ch),
        "cjk": sum(c["cjk"] for c in v1ch),
        "zici": sum(c["zici"] for c in v1ch),
        "figures": sum(c["figures"] for c in v1ch),
        "tables": sum(c["tables"] for c in v1ch),
        "disp_eqs": sum(c["disp_eqs"] for c in v1ch),
        "inline_math": sum(c["inline_math"] for c in v1ch),
        "footnotes": sum(c["footnotes"] for c in v1ch),
        "footnote_cjk": sum(c["footnote_cjk"] for c in v1ch),
        "struct_cjk": sum(c["struct_cjk"] for c in v1ch),
        "heading_cjk": sum(c["heading_cjk"] for c in v1ch),
        "ref_label_cjk": sum(c["ref_label_cjk"] for c in v1ch),
        "uwave": sum(c["uwave"] for c in v1ch),
        "uwave_body": sum(c["uwave_body"] for c in v1ch),
        "refs": sum(c["refs"] for c in v1ch),
        "inline_math_raw": sum(c["inline_math_raw"] for c in v1ch),
        "sections_plain": sum(c["n_sections"] - c["n_sections_star"] for c in v1ch),
        "sections_star": sum(c["n_sections_star"] for c in v1ch),
    }

    # 每段补章标题、每句补章键/行号
    for c in chapters:
        for p in c["paragraphs"]:
            p["chapter_title"] = c["title"]
            for s in p["sentences"]:
                s["chapter_key"] = c["key"]
                s["line"] = pos_to_line(c, s["src"])

    # 英文
    en_map = {}
    if os.path.isdir(en_dir):
        for key, _vol, _num, _path in chapter_files():
            p = os.path.join(en_dir, key.replace("-", "_") + ".txt")
            if os.path.exists(p):
                en_map[key] = parse_en(p)
    # 全局换算比：仅用第一卷（完整翻译），按总字数/总词数估计
    zh_vol1 = sum(c["zici"] for c in chapters if c["volume"] == 1)
    en_vol1 = sum(sum(p["words"] for p in en_map.get(c["key"], {"paras": []})["paras"])
                  for c in chapters if c["volume"] == 1)
    global_ratio = (zh_vol1 / en_vol1) if en_vol1 else 1.7

    compare = []
    for c in chapters:
        en_data = en_map.get(c["key"], {"paras": [], "text_blocks": 0})
        en_paras = en_data["paras"]
        res = analyze_zh_en(c, en_paras, global_ratio)
        res["chapter"] = c
        res["en_paras"] = en_paras
        res["en_text_blocks"] = en_data["text_blocks"]
        compare.append(res)

    return {
        "chapters": chapters,
        "totals": totals,
        "paragraphs": all_paras,
        "sentences": all_sents,
        "compare": compare,
        "en_available": bool(en_map),
        "en_dir": en_dir,
        "global_ratio": global_ratio,
    }


# ---------------------------------------------------------------------------
# 输出：01 总体统计
# ---------------------------------------------------------------------------
def describe_len(values):
    if not values:
        return {"mean": 0, "median": 0, "p90": 0, "p95": 0, "p99": 0, "max": 0,
                "n_gt300": 0, "n_gt500": 0, "n_gt1000": 0}
    return {
        "mean": statistics.mean(values),
        "median": quantile(values, 0.5),
        "p90": quantile(values, 0.9),
        "p95": quantile(values, 0.95),
        "p99": quantile(values, 0.99),
        "max": max(values),
        "n_gt300": sum(1 for v in values if v > LONG_PARA),
        "n_gt500": sum(1 for v in values if v > LONG_PARA_P0),
        "n_gt1000": sum(1 for v in values if v > 1000),
    }


def write_01(analysis, out_dir):
    totals = analysis["totals"]
    chapters = analysis["chapters"]
    paras = analysis["paragraphs"]
    sents = analysis["sentences"]
    plens = [p["zici"] for p in paras]
    cjklens = [p["cjk"] for p in paras]
    slens = [s["zici"] for s in sents]
    pd = describe_len(plens)
    sd = describe_len(slens)
    v1 = totals["vol1"]
    v1_plens = [p["zici"] for p in paras if p["volume"] == 1]
    n_gt80 = sum(1 for v in slens if v > 80)
    n_gt150 = sum(1 for v in slens if v > 150)
    n_gt200 = sum(1 for v in slens if v > 200)
    # 纯文字墙节数
    n_text_wall = sum(
        1 for c in chapters for st in c["sections"]
        if st["zici"] > TEXT_WALL and not st["figure"] and not st["table"]
        and not st["disp_eq"] and "参考文献" not in st["title"] and st["paras"]
    )

    L = []
    A = L.append
    A("# 01 总体统计：规模、段落长度、句长")
    A("")
    A("> 生成工具：`tools/audit_text.py`（`python3 tools/audit_text.py` 可完整复现）。")
    A("> 统计对象：`Chapters/VolumeI/Chapter1..52.tex`、`VolumeII/Chapter1.tex`、"
      "`VolumeIII/Chapter1.tex`，分支 `feat/reading-efficiency`。")
    A("")
    A("## 结论摘要")
    A("")
    A(f"1. **规模与结构**：全书 {totals['chapters']} 章、{totals['sections_plain']} 个 `\\section`"
      f"（另 {totals['sections_star']} 个 `\\section*`）、{fmt_int(totals['lines'])} 行、"
      f"原始汉字 {fmt_int(totals['raw_cjk'])} 个；清洗后**正文段落 {fmt_int(totals['paragraphs'])} 个**，"
      f"正文汉字 {fmt_int(totals['cjk'])} 个，总字数（汉字+西文词）{fmt_int(totals['zici'])}。"
      "全书**只有 1 个 `enumerate`、0 个 `itemize`**，即结构上完全没有列表。")
    A(f"2. **段落偏长**：段落字数均值 **{pd['mean']:.0f}**、中位 **{pd['median']:.0f}**、"
      f"p90 **{pd['p90']:.0f}**、最长 **{pd['max']}** 字；"
      f"**{pd['n_gt300']} 段（{fmt_pct(pd['n_gt300'], len(plens))}）超过 300 字**，"
      f"其中 {pd['n_gt500']} 段超过 500 字、{pd['n_gt1000']} 段超过 1000 字；"
      f"另有 **{n_text_wall} 节纯文字墙**（>1500 字且无图/表/展示公式，见 04）。")
    A(f"3. **句子偏长**：句长均值 **{sd['mean']:.0f}** 字、中位 **{sd['median']:.0f}**、"
      f"p90 **{sd['p90']:.0f}**、p99 **{sd['p99']:.0f}**、最长 **{sd['max']}** 字；"
      f"超过 80 字的句子 **{n_gt80}** 句、超过 150 字的 **{n_gt150}** 句、"
      f"超过 200 字的 **{n_gt200}** 句（清单见 05）。")
    n_uw_body_ch = sum(1 for c in chapters if c["uwave_body"] > 0)
    A(f"4. **强调断层**：`\\uwave` 共 **{totals['uwave']}** 处（正文内 {totals['uwave_body']} 处，"
      f"其余在图表标题里；第 44 章的 7 处全在表格标题内），正文强调只分布在 "
      f"{n_uw_body_ch} 章（第一卷 1–10 章），其余 {totals['chapters'] - n_uw_body_ch} 章零正文强调；对比图 "
      f"{totals['figures']} 幅、表 {totals['tables']} 张、展示公式 {totals['disp_eqs']} 个，"
      "“长段 + 长句 + 无重点标记”是大多数章节的默认状态（见 05）。")
    A(f"5. **列表化机会**：正文中\"第一/第二\"\"（1）（2）\"\"首先/其次/最后\"等枚举标记大量存在，"
      "但都以散文形式写成；`03-列表化候选.csv` 给出可直接改造的段落清单，"
      f"`02-长段落清单.csv` 给出 {pd['n_gt300']} 个 >300 字段落及建议切分点。"
      "这两份清单是阅读效率改造的优先工作面。")
    A("")
    A("## 一、统计口径")
    A("")
    A("| 指标 | 定义 |")
    A("|---|---|")
    A("| 章 / 节 | `\\chapter` / `\\section` 命令数；`\\section*` 单独计数、单独列（参考文献、小结） |")
    A("| 原始空行块 | LaTeX 源文件中被空行分隔的块（含图、表、公式、标题等结构块），用于和旧粗口径对照 |")
    A("| **正文段落** | 空行块中去掉图/表/展示公式/标题/脚注等结构内容后仍含汉字的块；"
      "块内若有 `\\item` 按列表项再切分；纯英文参考文献条目不计 |")
    A("| **字数** | 汉字数 + 西文词数（连续拉丁字母串、数字串各计 1 词）；标点、行内公式、"
      "`\\ref` 编号不计；同时给出\"汉字数\"备查 |")
    A("| **句** | 段落正文按 `。！？` 切分、且至少含 1 个汉字的片段；句子不跨段 |")
    A("| 展示公式 | 顶层 `equation/equation*/align/align*/flalign/gather/multline/eqnarray` 环境与 "
      "`\\[...\\]`；`aligned/split/cases` 等公式内部结构不重复计 |")
    A("| 图 / 表 | 图 = `figure`+`wrapfigure`；表 = `table`+`longtable`（另报 `tabular` 数） |")
    A("| 内联公式 | 成对的 `$...$` 数 |")
    A("| 行号 | 源文件 1-based 行号；行数按换行符计（与 `wc -l` 一致） |")
    A("")
    A("> 与旧粗口径的差异：旧口径把结构块也当成\"段落\"（约 2.4k 块），并把 `\\footnotesize` "
      "误计为脚注（\"136 个脚注\"实为 `\\footnote` 字符串出现数）；本表只统计清洗后的正文段落与"
      "真实脚注。详细对照见文末\"六\"。")
    A("")
    A("## 二、全书总量")
    A("")
    A("| 指标 | 全书 | 其中第一卷 | 第二/三卷（各 1 章节选） |")
    A("|---|---:|---:|---:|")
    A(f"| 章数 | {totals['chapters']} | 52 | 2 |")
    A(f"| 行数（换行符） | {fmt_int(totals['lines'])} | {fmt_int(v1['lines'])} | "
      f"{fmt_int(totals['lines'] - v1['lines'])} |")
    A(f"| `\\section` 数（不含 `\\section*`） | {totals['sections_plain']} | "
      f"{v1['sections_plain']} | {totals['sections_plain'] - v1['sections_plain']} |")
    A(f"| `\\section*` 数 | {totals['sections_star']} | {v1['sections_star']} | "
      f"{totals['sections_star'] - v1['sections_star']} |")
    A(f"| 原始汉字数 | {fmt_int(totals['raw_cjk'])} | {fmt_int(v1['raw_cjk'])} | "
      f"{fmt_int(totals['raw_cjk'] - v1['raw_cjk'])} |")
    A(f"| 原始空行块 | {fmt_int(totals['raw_blocks'])} | {fmt_int(v1['raw_blocks'])} | "
      f"{fmt_int(totals['raw_blocks'] - v1['raw_blocks'])} |")
    A(f"| **正文段落** | **{fmt_int(totals['paragraphs'])}** | {fmt_int(v1['paragraphs'])} | "
      f"{fmt_int(totals['paragraphs'] - v1['paragraphs'])} |")
    A(f"| 其中列表项段落 | {totals['list_items']} | — | — |")
    A(f"| 正文汉字数 | {fmt_int(totals['cjk'])} | {fmt_int(v1['cjk'])} | "
      f"{fmt_int(totals['cjk'] - v1['cjk'])} |")
    A(f"| 正文总字数 | {fmt_int(totals['zici'])} | {fmt_int(v1['zici'])} | "
      f"{fmt_int(totals['zici'] - v1['zici'])} |")
    A(f"| 句子数 | {fmt_int(totals['sentences'])} | — | — |")
    A(f"| 图（figure+wrapfigure） | {totals['figures']} | {v1['figures']} | "
      f"{totals['figures'] - v1['figures']} |")
    A(f"| 表（table+longtable） | {totals['tables']} | {v1['tables']} | "
      f"{totals['tables'] - v1['tables']} |")
    A(f"| `tabular` 环境数 | {totals['tabulars']} | — | — |")
    A(f"| 展示公式 | {totals['disp_eqs']} | {v1['disp_eqs']} | "
      f"{totals['disp_eqs'] - v1['disp_eqs']} |")
    A(f"| 内联公式（$…$ 对，正文） | {fmt_int(totals['inline_math'])} | "
      f"{fmt_int(v1['inline_math'])} | {fmt_int(totals['inline_math'] - v1['inline_math'])} |")
    A(f"| 内联公式（含图表标题等全文） | {fmt_int(totals['inline_math_raw'])} | "
      f"{fmt_int(v1['inline_math_raw'])} | "
      f"{fmt_int(totals['inline_math_raw'] - v1['inline_math_raw'])} |")
    A(f"| 脚注（`\\footnote`） | {totals['footnotes']} | {v1['footnotes']} | "
      f"{totals['footnotes'] - v1['footnotes']} |")
    A(f"| 脚注内汉字 | {fmt_int(totals['footnote_cjk'])} | {fmt_int(v1['footnote_cjk'])} | "
      f"{fmt_int(totals['footnote_cjk'] - v1['footnote_cjk'])} |")
    A(f"| `\\uwave` 强调 | {totals['uwave']} | {v1['uwave']} | "
      f"{totals['uwave'] - v1['uwave']} |")
    A(f"| `\\ref` 交叉引用 | {fmt_int(totals['refs'])} | {fmt_int(v1['refs'])} | "
      f"{fmt_int(totals['refs'] - v1['refs'])} |")
    A(f"| `itemize` / `enumerate` | {totals['itemize']} / {totals['enumerate']} | "
      f"{totals['itemize']} / {totals['enumerate']} | 0 / 0 |")
    A("")
    A("> 第二、三卷各只有第 1 章，且为**节选试译**（第二卷第一章中文仅 "
      f"{describe_short_chapter(analysis, 'II-01')}，第三卷第一章仅 "
      f"{describe_short_chapter(analysis, 'III-01')}），不能按完整章解读；"
      "全书统计实际上由第一卷 52 章主导。")
    A("")
    A("## 三、段落长度分布")
    A("")
    A("### 3.1 分箱（字数口径）")
    A("")
    A("| 字数区间 | 全书段数 | 占比 | 第一卷段数 | 第一卷占比 |")
    A("|---|---:|---:|---:|---:|")
    for label, lo, hi in PARA_BINS:
        n_all = sum(1 for v in plens if lo <= v <= hi)
        n_v1 = sum(1 for v in v1_plens if lo <= v <= hi)
        A(f"| {label} | {n_all} | {fmt_pct(n_all, len(plens))} | {n_v1} | {fmt_pct(n_v1, len(v1_plens))} |")
    A(f"| **合计** | **{len(plens)}** | 100% | **{len(v1_plens)}** | 100% |")
    A("")
    A("### 3.2 分位数与阈值")
    A("")
    A("| 口径 | 段落数 | 均值 | 中位 | p90 | p95 | p99 | 最长 | >300 字 | >500 字 | >1000 字 |")
    A("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

    def prow(name, vals):
        d = describe_len(vals)
        return (f"| {name} | {len(vals)} | {d['mean']:.1f} | {d['median']:.0f} | {d['p90']:.0f} | "
                f"{d['p95']:.0f} | {d['p99']:.0f} | {d['max']} | {d['n_gt300']} "
                f"（{fmt_pct(d['n_gt300'], len(vals))}） | {d['n_gt500']} | {d['n_gt1000']} |")

    A(prow("字数（汉字+西文词）", plens))
    A(prow("汉字数", cjklens))
    A("")
    A("## 四、句长分布")
    A("")
    A("### 4.1 分箱")
    A("")
    A("| 句长区间（字） | 句数 | 占比 |")
    A("|---|---:|---:|")
    for label, lo, hi in SENT_BINS:
        n = sum(1 for v in slens if lo <= v <= hi)
        A(f"| {label} | {n} | {fmt_pct(n, len(slens))} |")
    A(f"| **合计** | **{len(slens)}** | 100% |")
    A("")
    A("### 4.2 分位数与阈值")
    A("")
    A("| 指标 | 均值 | 中位 p50 | p90 | p95 | p99 | 最长 | >80 字 | >100 字 | >150 字 | >200 字 |")
    A("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    A(f"| 句长（字） | {sd['mean']:.1f} | {sd['median']:.0f} | {sd['p90']:.0f} | {sd['p95']:.0f} | "
      f"{sd['p99']:.0f} | {sd['max']} | {n_gt80} | {sum(1 for v in slens if v > 100)} | "
      f"{n_gt150} | {n_gt200} |")
    A("")
    A("> 句长按段落内 `。！？` 切分；引号、分号内的分句不单独切分，所以\"分号列举句\"整体算一句——"
      "这类句子恰恰最该改造成列表（见 `03`）。")
    A("")
    A("## 五、每章明细")
    A("")
    A("### 5.1 规模与结构")
    A("")
    A("| 章 | 标题 | 行数 | 节数 | 段落数 | 汉字数 | 图 | 表 | 展示公式 | 内联公式 | 脚注 | `\\uwave` |")
    A("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for c in chapters:
        A(f"| {c['key']} | {c['title']} | {c['n_lines']} | {c['n_sections']} | "
          f"{len(c['paragraphs'])} | {fmt_int(c['cjk'])} | {c['figures']} | {c['tables']} | "
          f"{c['disp_eqs']} | {c['inline_math']} | {c['footnotes']} | {c['uwave']} |")
    A(f"| **合计** | — | {fmt_int(totals['lines'])} | {totals['sections']} | "
      f"{fmt_int(totals['paragraphs'])} | {fmt_int(totals['cjk'])} | {totals['figures']} | "
      f"{totals['tables']} | {totals['disp_eqs']} | {fmt_int(totals['inline_math'])} | "
      f"{totals['footnotes']} | {totals['uwave']} |")
    A("")
    A("### 5.2 段落与句长")
    A("")
    A("| 章 | 段落数 | 段均字数 | 段中位 | 段最长 | >300字段数 | 句数 | 句均 | 句p90 | 句最长 |")
    A("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for c in chapters:
        pl = [p["zici"] for p in c["paragraphs"]]
        sl = c["sent_lens"]
        if not pl:
            A(f"| {c['key']} | 0 | — | — | — | 0 | 0 | — | — | — |")
            continue
        A(f"| {c['key']} | {len(pl)} | {statistics.mean(pl):.0f} | {quantile(pl, 0.5):.0f} | "
          f"{max(pl)} | {sum(1 for v in pl if v > LONG_PARA)} | {len(sl)} | "
          f"{(statistics.mean(sl) if sl else 0):.1f} | {(quantile(sl, 0.9) if sl else 0):.0f} | "
          f"{(max(sl) if sl else 0)} |")
    A("")
    A("### 5.3 段落均值最高的节（Top 15，至少 3 段）")
    A("")
    A("| 章 | 节 | 段落数 | 节字数 | 段落均值 | 节内图/表/公式 |")
    A("|---|---|---:|---:|---:|---|")
    sec_rows = []
    for c in chapters:
        for st in c["sections"]:
            if len(st["paras"]) >= 3:
                sec_rows.append((c["key"], st))
    sec_rows.sort(key=lambda x: -(x[1]["zici"] / max(1, len(x[1]["paras"]))))
    for key, st in sec_rows[:15]:
        A(f"| {key} | {st['title']} | {len(st['paras'])} | {st['zici']} | "
          f"{st['zici'] / max(1, len(st['paras'])):.0f} | {st['figure']}/{st['table']}/{st['disp_eq']} |")
    A("")
    A("## 六、与既有粗口径基线数字的对照")
    A("")
    A("| 指标 | 旧粗口径（背景数字） | 本次口径 | 差异原因 |")
    A("|---|---:|---:|---|")
    A(f"| 段落 / 块 | 约 2397 块 | 原始空行块 {fmt_int(totals['raw_blocks'])}；"
      f"正文段落 {fmt_int(totals['paragraphs'])} | 旧口径包含图/表/公式/标题块；本次按正文段落重算 |")
    A(f"| 段均字数 | 约 195 | {pd['mean']:.1f}（正文段） | 去掉结构块后均值略变 |")
    A(f"| 段中位字数 | 约 170 | {pd['median']:.0f} | 同上 |")
    A(f"| >300 字段占比 | 约 17% | {fmt_pct(pd['n_gt300'], len(plens))} | "
      "分母改为正文段，且字数含西文词 |")
    A(f"| 最长段落 | 1110 | {pd['max']} | 旧口径的 1110 含图表标题内汉字；本次只算段落正文，"
      "故略低 |")
    A(f"| 句均 / p90 / p99 / max | 35 / 63 / 104 / 237 | {sd['mean']:.0f} / {sd['p90']:.0f} / "
      f"{sd['p99']:.0f} / {sd['max']} | 本口径句长含西文词，与旧口径接近 |")
    A(f"| 展示公式 | 1106 | {totals['disp_eqs']} | 旧口径把 `aligned` 等公式内部结构重复计入（+48）|")
    A(f"| 脚注 | 136 | {totals['footnotes']} | 旧口径数 `\\footnote` 字符串，误含 `\\footnotesize`（78 处） |")
    A(f"| `\\section`（第一卷） | 290 | {v1['sections_plain']}（另有 3 个 `\\section*`） | 一致 |")
    A(f"| 图 / 表 | 294 幅图 | {totals['figures']} 图 / {totals['tables']} 表 | 图一致；表为 table+longtable |")
    A(f"| `\\uwave` 强调 | 455 | {totals['uwave']}（正文 {totals['uwave_body']}） | 一致；"
      "8 处在图表标题内，正文口径为 447 |")
    A(f"| 内联公式 | （未给） | {fmt_int(totals['inline_math_raw'])}（全文）/ "
      f"{fmt_int(totals['inline_math'])}（正文） | 图表标题、公式内不计入正文口径 |")
    A(f"| 汉字数 | 约 48.5 万 | {fmt_int(totals['raw_cjk'])}（原始）/ "
      f"{fmt_int(totals['cjk'])}（正文） | 一致；正文少的 "
      f"{fmt_int(totals['raw_cjk'] - totals['cjk'])} 个汉字来自：图/表/公式环境内文字 "
      f"{fmt_int(totals['struct_cjk'])}（含图题、表内文字、公式内 \\text{{}} 中文）、"
      f"章/节标题 {fmt_int(totals['heading_cjk'])}、脚注 {fmt_int(totals['footnote_cjk'])}、"
      f"`\\ref`/`\\label` 标签名 {fmt_int(totals['ref_label_cjk'])}（标签名不是可见正文），"
      "各项有少量重叠 |")
    A("")
    path = os.path.join(out_dir, "01-总体统计.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return path


def describe_short_chapter(analysis, key):
    for c in analysis["chapters"]:
        if c["key"] == key:
            return f"{fmt_int(c['cjk'])} 个汉字、{len(c['paragraphs'])} 段"
    return "—"


# ---------------------------------------------------------------------------
# 输出：02 长段落清单
# ---------------------------------------------------------------------------
def starts_with_marker(text):
    for m in SENT_START_MARKERS:
        if text.startswith(m):
            return m
    return None


def plan_splits(para):
    sents = para["sentences"]
    total = para["zici"]
    if total <= LONG_PARA or len(sents) < 2:
        return []
    target_n = max(2, math.ceil(total / 250.0))
    k = min(target_n - 1, len(sents) - 1)
    if k <= 0:
        return []
    cum = []
    acc = 0
    for s in sents:
        acc += s["zici"]
        cum.append(acc)
    chosen = []
    used = set()
    for t in range(1, target_n):
        desired = total * t / target_n
        cand = [j for j in range(len(sents) - 1) if j not in used]
        if not cand:
            break

        def score(j):
            dist = abs(cum[j] - desired) / max(1.0, total / target_n)
            marker = starts_with_marker(sents[j + 1]["text"])
            bonus = 0.8 if marker else 0.0
            if sents[j]["text"].rstrip().endswith(("：", ":")):
                bonus += 0.3
            return dist - bonus

        best = min(cand, key=score)
        used.add(best)
        chosen.append(best)
    chosen.sort()
    out = []
    for j in chosen:
        marker = starts_with_marker(sents[j + 1]["text"])
        out.append((j, cum[j], 100.0 * cum[j] / max(1, total), marker))
    return out


def split_reason(para, plan):
    reasons = []
    total = para["zici"]
    n_sent = para["n_sent"]
    max_sent = max((s["zici"] for s in para["sentences"]), default=0)
    if len(para["sentences"]) <= 1:
        reasons.append("整段只有 1 句，需先断句再切分")
    elif total > 800:
        reasons.append(f"超长段（{total} 字）")
    elif total > LONG_PARA_P0:
        reasons.append(f"重点长段（{total} 字，>500）")
    if n_sent >= 8:
        reasons.append(f"句数多（{n_sent} 句）")
    if max_sent > 100:
        reasons.append(f"含超长句（最长 {max_sent} 字）")
    markers = sorted({m for _j, _c, _p, m in plan if m})
    if markers:
        reasons.append("可在“" + "/".join(markers[:3]) + "”等转折/递进处断开")
    if len(plan) >= 2:
        reasons.append(f"需切 {len(plan)} 刀")
    if para["text"].count("；") >= 4:
        reasons.append("并列分句多，可同时改列表")
    return "；".join(reasons) if reasons else "长度超阈值"


def write_02(analysis, out_dir):
    paras = [p for p in analysis["paragraphs"] if p["zici"] > LONG_PARA]
    paras.sort(key=lambda p: (-p["zici"], p["chapter_key"], p["start_line"]))
    path = os.path.join(out_dir, "02-长段落清单.csv")
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["优先级", "卷", "章", "章标题", "节名", "段落起始行", "段落结束行", "字数",
                    "汉字数", "句数", "最长句字数", "内联公式数", "首40字", "建议切分点数",
                    "建议切分位置", "切分理由"])
        for p in paras:
            plan = plan_splits(p)
            max_sent = max((s["zici"] for s in p["sentences"]), default=0)
            pos_desc = "；".join(
                f"第{j + 1}句后（累计 {c} 字，{pct:.0f}%）" + (f"，下句以“{m}”起" if m else "")
                for j, c, pct, m in plan
            ) or "—"
            w.writerow([
                "P0（>500字）" if p["zici"] > LONG_PARA_P0 else "P1（301–500字）",
                VOLUME_NAMES[p["volume"]], p["chapter_key"], p["chapter_title"],
                p["section_title"], p["start_line"], p["end_line"], p["zici"], p["cjk"],
                p["n_sent"], max_sent, p["inline_math"], one_line(p["text"], 40),
                len(plan), pos_desc, split_reason(p, plan),
            ])
    return path


# ---------------------------------------------------------------------------
# 输出：03 列表化候选
# ---------------------------------------------------------------------------
def write_03(analysis, out_dir):
    rows = []
    for c in analysis["chapters"]:
        ch_paras = c["paragraphs"]
        cross = detect_cross_para_markers(ch_paras)
        in_cross = set()
        for ev in cross:
            for p in ev["paras"]:
                in_cross.add(id(p))
        for ev in cross:
            ps = ev["paras"]
            if ev["family"] == "跨段数字序号":
                seq = "/".join(DIGIT_HEAD_RE.match(p["text"]).group(1) + "."
                               for p in ps if DIGIT_HEAD_RE.match(p["text"]))
            elif ev["family"] == "跨段罗马序号":
                seq = "/".join(ROMAN_RE.search(p["raw"]).group(1)
                               for p in ps if ROMAN_RE.search(p["raw"]))
            else:
                seq = "/".join(p["text"][:4] for p in ps)
            rows.append({"chapter": c, "paras": ps, "family": ev["family"],
                         "seq": seq, "detail": f"连续 {len(ps)} 段均以序号开头",
                         "mode": "跨段"})
        for p in ch_paras:
            if id(p) in in_cross or p["is_list_item"]:
                continue
            for family, seq, detail in detect_para_markers(p):
                rows.append({"chapter": c, "paras": [p], "family": family,
                             "seq": seq, "detail": detail, "mode": "段内"})
    rows.sort(key=lambda r: (r["chapter"]["volume"], r["chapter"]["num"],
                             r["paras"][0]["start_line"]))
    path = os.path.join(out_dir, "03-列表化候选.csv")
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "章标题", "节名", "段落起始行", "段落结束行", "涉及段落数",
                    "字数", "标记类型", "标记序列", "标记数", "检测方式", "建议列表类型", "备注"])
        for r in rows:
            c = r["chapter"]
            ps = r["paras"]
            zici = sum(p["zici"] for p in ps)
            n_mark = max(1, str(r["seq"]).count("/") + 1)
            fam = r["family"]
            if fam in ("顺序词", "跨段顺序词"):
                stype = "步骤列表（有序列表 / 分步说明）"
            elif fam in ("括号序号", "跨段括号序号", "手工罗马序号", "跨段罗马序号",
                         "手工数字序号", "段首数字序号", "跨段数字序号"):
                stype = "有序列表（编号列表）"
            elif fam in ("中文序数（第X）", "跨段中文序数", "一是/二是"):
                stype = "有序列表或要点列表（按“第一/第二”编号）"
            elif fam == "分号并列":
                stype = "无序要点列表（或改写成并列短句）"
            else:
                stype = "有序列表"
            w.writerow([
                VOLUME_NAMES[c["volume"]], c["key"], c["title"], ps[0]["section_title"],
                ps[0]["start_line"], ps[-1]["end_line"], len(ps), zici, fam, r["seq"],
                n_mark, r["mode"], stype, r["detail"],
            ])
    return path, rows


# ---------------------------------------------------------------------------
# 输出：04 纯文字墙节
# ---------------------------------------------------------------------------
def write_04(analysis, out_dir):
    rows = []
    for c in analysis["chapters"]:
        for st in c["sections"]:
            if st["zici"] <= TEXT_WALL:
                continue
            if st["figure"] or st["table"] or st["disp_eq"]:
                continue
            if "参考文献" in st["title"]:
                continue
            n_par = len(st["paras"])
            if n_par == 0:
                continue
            avg = st["zici"] / n_par
            n_long = sum(1 for p in st["paras"] if p["zici"] > LONG_PARA)
            sents = st["sent_lens"]
            avg_sent = statistics.mean(sents) if sents else 0
            has_enum = sum(1 for p in st["paras"] if detect_para_markers(p))
            sug = []
            if n_long:
                sug.append(f"拆段（本节约 {n_long} 段 >300 字，见 02）")
            if has_enum:
                sug.append(f"枚举句改列表（约 {has_enum} 段含“第一/首先/（1）”等标记，见 03）")
            if n_par <= 2 and st["zici"] > 2000:
                sug.append("按论证层次拆成 2–3 个自然段并加小标题")
            elif n_par >= 3:
                sug.append("按“论点/例证/结论”重组为 2–3 段并加小标题")
            if st["inline_math"] == 0:
                sug.append("节内零公式零图表，是纯叙述：可补 1 张示意图或对照表")
            else:
                sug.append(f"内联公式 {st['inline_math']} 处但无展示公式：可把推导步骤列表化")
            if avg_sent > 45:
                sug.append(f"句均 {avg_sent:.0f} 字偏长，需断句")
            rows.append({"chapter": c, "sec": st, "n_par": n_par, "avg": avg,
                         "n_long": n_long, "avg_sent": avg_sent,
                         "sug": "；".join(sug)})
    rows.sort(key=lambda r: -r["sec"]["zici"])
    path = os.path.join(out_dir, "04-纯文字墙节.csv")
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["优先级", "卷", "章", "章标题", "节名", "节起始行", "字数", "段落数",
                    "段落均值", "最长段字数", ">300字段数", "图数", "表数", "展示公式数",
                    "内联公式数", "内联公式密度(处/千字)", "句数", "句均字数", "建议改造手段"])
        for i, r in enumerate(rows, 1):
            c, st = r["chapter"], r["sec"]
            dens = 1000.0 * st["inline_math"] / max(1, st["zici"])
            w.writerow([
                i, VOLUME_NAMES[c["volume"]], c["key"], c["title"], st["title"], st["line"],
                st["zici"], r["n_par"], f"{r['avg']:.0f}", st["max_para"], r["n_long"],
                st["figure"], st["table"], st["disp_eq"], st["inline_math"],
                f"{dens:.1f}", len(st["sent_lens"]), f"{r['avg_sent']:.1f}", r["sug"],
            ])
    return path, rows


# ---------------------------------------------------------------------------
# 输出：05 强调与长句
# ---------------------------------------------------------------------------
def write_05(analysis, out_dir):
    chapters = analysis["chapters"]
    totals = analysis["totals"]
    L = []
    A = L.append
    A("# 05 强调与长句：`\\uwave` 分布、长句清单、内联公式密度")
    A("")
    A("> 生成工具：`tools/audit_text.py`。口径见 `01-总体统计.md` 第一节。")
    A("")
    uw_nonzero = [(c, c["uwave"]) for c in chapters if c["uwave"]]
    long_sents = [s for s in analysis["sentences"] if s["zici"] > LONG_SENT]
    long_sents.sort(key=lambda s: (-s["zici"], s["chapter_key"], s["line"]))
    n_gt150 = sum(1 for s in long_sents if s["zici"] > 150)
    early = sum(n for c, n in uw_nonzero if c["volume"] == 1 and c["num"] <= 10)
    n_sec_uw = sum(1 for c in chapters for st in c["sections"] if st["uwave"] > 0)
    n_sec_text = sum(1 for c in chapters for st in c["sections"] if st["zici"] > 0)
    uw_body_ch = [c for c in chapters if c["uwave_body"] > 0]
    caption_only = [c for c in chapters if c["uwave"] > 0 and c["uwave_body"] == 0]
    A("## 结论摘要")
    A("")
    A(f"1. `\\uwave` 共 **{totals['uwave']}** 处（其中正文内 {totals['uwave_body']} 处，"
      f"其余 {totals['uwave'] - totals['uwave_body']} 处在图表标题里），正文强调只出现在 "
      f"**{len(uw_body_ch)} 章**（{', '.join(c['key'] for c in uw_body_ch)}）"
      + (f"；{', '.join(c['key'] for c in caption_only)} 的强调全在表格标题内" if caption_only else "")
      + f"；其余 {totals['chapters'] - len(uw_body_ch)} 章**没有任何正文强调标记**，"
      "读者无法快速定位重点。"
      f"按节看，{n_sec_text} 个有正文的节中只有 **{n_sec_uw} 节**有强调。")
    if uw_nonzero:
        top = max(uw_nonzero, key=lambda x: x[1])
        low = min(uw_nonzero, key=lambda x: x[1])
        A(f"2. 分布极不均匀：最多 {top[0]['key']}（{top[1]} 处，"
          f"{1000.0 * top[1] / max(1, top[0]['cjk']):.2f} 处/千字），"
          f"最少 {low[0]['key']}（{low[1]} 处）；1–10 章合计 {early} 处，占全部 "
          f"{fmt_pct(early, totals['uwave'])}。")
    A(f"3. 超过 {LONG_SENT} 字的句子共 **{len(long_sents)}** 句，>150 字 **{n_gt150}** 句；"
      f"最长句 **{long_sents[0]['zici']} 字**（{long_sents[0]['chapter_key']} 第 "
      f"{long_sents[0]['line']} 行，见第二节清单）。")
    sec_list = []
    for c in chapters:
        for st in c["sections"]:
            if st["zici"] >= 500:
                sec_list.append((c, st, 1000.0 * st["inline_math"] / st["zici"]))
    sec_list.sort(key=lambda x: -x[2])
    if sec_list:
        A(f"4. 内联公式最密的一节是 {sec_list[0][0]['key']}「{sec_list[0][1]['title']}」"
          f"（{sec_list[0][2]:.1f} 处/千字）；公式密集处往往同时是长句、长段高发区，"
          "断句与列表化要一起做。")
    A(f"5. 建议的强调规范：每个 `\\section` 至少用 1–3 处 `\\uwave` 标出关键术语/结论"
      f"（当前只有 {n_sec_uw}/{n_sec_text} 节有强调、{totals['chapters'] - len(uw_body_ch)} 章为零），"
      "并把 >150 字的 "
      f"{n_gt150} 句优先断句——这两项改动成本最低、可感知收益最高。")
    A("")
    A("## 一、`\\uwave` 按章分布")
    A("")
    A("| 章 | 标题 | `\\uwave`（全文） | 其中正文 | 该章汉字数 | 正文密度（处/千字） | 涉及段落数 |")
    A("|---|---|---:|---:|---:|---:|---:|")
    all_chapters_with_text = [c for c in chapters if c["cjk"] > 0]
    for c in all_chapters_with_text:
        n_par = sum(1 for p in c["paragraphs"] if p["uwave"])
        dens = 1000.0 * c["uwave_body"] / max(1, c["cjk"])
        A(f"| {c['key']} | {c['title']} | {c['uwave']} | {c['uwave_body']} | "
          f"{fmt_int(c['cjk'])} | {dens:.2f} | {n_par} |")
    A(f"| **合计** | — | **{totals['uwave']}** | **{totals['uwave_body']}** | "
      f"{fmt_int(totals['cjk'])} | "
      f"{1000.0 * totals['uwave_body'] / max(1, totals['cjk']):.2f} | — |")
    A("")
    A("> 表中 0 表示该章无 `\\uwave`；多数章为 0，说明强调标记只在第 1–10 章与第 44 章出现。")
    A("")
    A(f"## 二、超过 {LONG_SENT} 字的长句清单（共 {len(long_sents)} 句，按字数降序）")
    A("")
    A("行号 = 句子首字所在源文件行号（由清洗后的字符位置回溯）。")
    A("")
    A("| # | 章 | 行号 | 字数 | 句子摘录（前 60 字） |")
    A("|---:|---|---:|---:|---|")
    for i, s in enumerate(long_sents, 1):
        A(f"| {i} | {s['chapter_key']} | {s['line']} | {s['zici']} | {one_line(s['text'], 60)} |")
    A("")
    A("## 三、内联公式密度最高的节（Top 20，节字数 ≥500）")
    A("")
    A("| # | 章 | 节 | 节字数 | 内联公式 | 密度（处/千字） | 展示公式 |")
    A("|---:|---|---|---:|---:|---:|---:|")
    for i, (c, st, dens) in enumerate(sec_list[:20], 1):
        A(f"| {i} | {c['key']} | {st['title']} | {st['zici']} | {st['inline_math']} | "
          f"{dens:.1f} | {st['disp_eq']} |")
    A("")
    path = os.path.join(out_dir, "05-强调与长句.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return path


# ---------------------------------------------------------------------------
# 输出：06 中英段落对照
# ---------------------------------------------------------------------------
def write_06(analysis, out_dir):
    compare = analysis["compare"]
    global_ratio = analysis["global_ratio"]
    rows = []
    detail_rows = []
    for r in compare:
        c = r["chapter"]
        en_hi = r.get("en_text_blocks", 0)
        if not r["n_en"]:
            rows.append({
                "c": c, "n_zh": r["n_zh"], "n_en": 0, "en_hi": 0, "unc": 0,
                "diff": r["n_zh"], "ratio": 0, "match": 0, "merges": 0,
                "merges_hi": 0, "merged_en": 0, "merge_rate": 0, "zh_only": 0,
                "en_only": 0, "quality": "无英文数据", "zh_total": r["zh_total"],
                "en_total": 0, "zwr": 0, "samples": [], "coverage": 0,
                "note": "缺少英文抓取文件",
            })
            continue
        para_ratio = r["n_zh"] / r["n_en"] if r["n_en"] else 0
        merge_rate = r["n_merged_en"] / r["n_en"] if r["n_en"] else 0
        uncertainty = max(0, en_hi - r["n_en"])
        if r.get("partial"):
            quality = "不完整（未译完）"
        elif uncertainty <= 2:
            quality = "高"
        elif uncertainty <= 8:
            quality = "中"
        else:
            quality = "低（公式碎片多）"
        samples = []
        for m in sorted(r["merges"], key=lambda x: (x["conf"] != "高", -x["dev"])):
            p = c["paragraphs"][m["zh_index"]]
            samples.append(
                f"[{m['conf']}]行{p['start_line']}「{one_line(p['text'], 10)}」"
                f"(中{m['zh_zici']}字←英{m['en_words']}词)")
        if c["volume"] in (2, 3):
            note = ("第二/三卷第一章为节选试译（未译完），中文段落数远少于英文重建段数，"
                    "这是“未译”而不是“合并”")
        elif r["n_zh"] > en_hi:
            note = "中文段落数>英上界：本口径下中文拆分多于合并"
        elif r["n_zh"] >= r["n_en"]:
            note = "中段落数≥英重建段数，本口径下未显示合并"
        else:
            note = "中段落少于英重建段数，疑似存在段落合并（需人工核对 06b）"
        if uncertainty > 8 and c["volume"] == 1:
            note += "；英文公式碎片多，英段数区间 %d–%d，段差不宜直接解读" % (r["n_en"], en_hi)
        rows.append({
            "c": c, "n_zh": r["n_zh"], "n_en": r["n_en"], "en_hi": en_hi,
            "unc": uncertainty, "diff": r["n_zh"] - r["n_en"],
            "ratio": para_ratio, "match": r["n_match"], "merges": r["n_merge"],
            "merges_hi": sum(1 for m in r["merges"] if m["conf"] == "高"),
            "merged_en": r["n_merged_en"], "merge_rate": merge_rate,
            "zh_only": r["n_zh_only"], "en_only": r["n_en_only"],
            "quality": quality, "zh_total": r["zh_total"], "en_total": r["en_total"],
            "zwr": r["zh_total"] / r["en_total"] if r["en_total"] else 0,
            "samples": samples, "coverage": r["coverage"], "note": note,
        })
        for m in r["merges"]:
            p = c["paragraphs"][m["zh_index"]]
            en_ps = [r["en_paras"][k] for k in m["en_index"]]
            detail_rows.append({
                "c": c, "p": p, "m": m,
                "en_head": " + ".join(
                    "“" + " ".join(e["text"].split()[:6]) + "…”" for e in en_ps),
                "en_words": m["en_words"],
            })

    path = os.path.join(out_dir, "06-中英段落对照.csv")
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "章标题", "中段落数", "英段落数(重建下限)",
                    "英文段落上界(空行文本块)", "英文重建不确定度(=上界-下界)",
                    "中-英段差", "中/英段落数比(按下限)", "对齐匹配对数",
                    "疑似合并事件数", "其中高置信", "被合并英段数",
                    "合并率(被并英段/英重建段)", "中文增补/拆分段数", "英文未对齐段数",
                    "英文覆盖率", "对齐质量", "中文正文汉字数", "英文词数",
                    "中文字/英词比", "疑似合并位置（前 8 例）", "备注"])
        for r in rows:
            c = r["c"]
            w.writerow([
                VOLUME_NAMES[c["volume"]], c["key"], c["title"], r["n_zh"], r["n_en"],
                r["en_hi"], r["unc"], r["diff"],
                f"{r['ratio']:.2f}" if r["n_en"] else "—",
                r["match"], r["merges"], r["merges_hi"], r["merged_en"],
                f"{100 * r['merge_rate']:.1f}%" if r["n_en"] else "—",
                r["zh_only"], r["en_only"],
                f"{100 * r['coverage']:.0f}%" if r["n_en"] else "—", r["quality"],
                r["zh_total"], r["en_total"],
                f"{r['zwr']:.2f}" if r["en_total"] else "—",
                "；".join(r["samples"][:8]) + ("…" if len(r["samples"]) > 8 else ""),
                r["note"],
            ])
    path2 = os.path.join(out_dir, "06b-中英段落对齐明细.csv")
    with open(path2, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "章标题", "中文段落起始行", "中文段落首25字", "中文字数",
                    "合并英文段序号(从1起)", "英文段首词", "英词数和", "期望中文字数",
                    "实际/期望", "置信度", "备注"])
        for d in detail_rows:
            c, p, m = d["c"], d["p"], d["m"]
            w.writerow([
                VOLUME_NAMES[c["volume"]], c["key"], c["title"], p["start_line"],
                one_line(p["text"], 25), m["zh_zici"],
                "+".join(str(k + 1) for k in m["en_index"]), d["en_head"],
                d["en_words"], f"{m['expect']:.0f}",
                f"{m['zh_zici'] / max(1.0, m['expect']):.2f}", m["conf"],
                f"长度偏差 {100 * m['dev']:.0f}%；{m['kind']}；"
                "英文段落数为重建值，可能多切/少切 1–3 段",
            ])
    return path, path2, rows


# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------
def write_readme(analysis, out_dir, en_dir):
    totals = analysis["totals"]
    ratio = analysis["global_ratio"]
    v1cmp = [r for r in analysis["compare"]
             if r["chapter"]["volume"] == 1 and r["n_en"]]
    en_lo_total = sum(r["n_en"] for r in v1cmp)
    en_hi_total = sum(r.get("en_text_blocks", 0) for r in v1cmp)
    zh_total_cmp = sum(r["n_zh"] for r in v1cmp)
    n_zh_ge_lo = sum(1 for r in v1cmp if r["n_zh"] >= r["n_en"])
    split_chs = [r["chapter"]["key"] for r in v1cmp
                 if r["n_zh"] > r.get("en_text_blocks", 0)]
    L = []
    A = L.append
    A("# docs/analysis/text —— 文本可读性审计（可复现）")
    A("")
    A("本目录是《阅读效率提升方案》的**文本侧量化证据**：段落/句子长度、列表化机会、"
      "纯文字墙、强调缺失、中英段落对照。全部数字由 `tools/audit_text.py` 生成，可复现。")
    A("")
    A("## 文件索引")
    A("")
    A("| 文件 | 内容 | 主要用途 |")
    A("|---|---|---|")
    A("| `01-总体统计.md` | 全书/每章规模、段落长度分布、句长分布、每章明细、与旧口径对照 | 方案的总量证据 |")
    A("| `02-长段落清单.csv` | 全书 >300 字段落（>500 标 P0）、建议切分点与理由 | 优先改造清单 |")
    A("| `03-列表化候选.csv` | “第一/第二”“（1）（2）”“首先/其次/最后”等枚举式段落、建议列表类型 | 列表化改造清单 |")
    A("| `04-纯文字墙节.csv` | >1500 字且无图/表/展示公式的节、建议改造手段 | 按节组织改造 |")
    A("| `05-强调与长句.md` | `\\uwave` 按章分布、>80 字长句全清单、内联公式最密的节 | 强调规范与断句清单 |")
    A("| `06-中英段落对照.csv` | 每章中/英段落数（含区间）、疑似合并位置、对齐质量 | 中英段落结构对照，核实“译文合并段落”问题 |")
    A("| `06b-中英段落对齐明细.csv` | 疑似合并段的中英行号/内容/置信度明细 | 人工核对样例 |")
    A("| `tools/audit_text.py` | 生成工具（Python3 标准库，无第三方依赖） | 复现/二次分析 |")
    A("")
    A("> 所有 CSV 为 UTF-8（带 BOM，Excel 可直接打开）；数字口径见 `01` 第一节与下文各文件规则。")
    A("")
    A("## 复现命令")
    A("")
    A("在仓库 `Feynman-Lectures-Latex/` 根目录执行：")
    A("")
    A("```bash")
    A("# 生成全部产出（覆盖本目录文件）")
    A("python3 tools/audit_text.py")
    A("")
    A("# 只打印口径自检数字，不写文件")
    A("python3 tools/audit_text.py --check")
    A("")
    A("# 指定英文抓取目录（默认 _attachments/build-feynman/audit/en，本地忽略目录）")
    A("python3 tools/audit_text.py --en-dir _attachments/build-feynman/audit/en")
    A("```")
    A("")
    A("## 统计口径（简述）")
    A("")
    A(f"- **正文段落 {fmt_int(totals['paragraphs'])} 个**：LaTeX 源文件按空行分块，"
      "去掉图/表/展示公式/标题/脚注等结构内容后仍含汉字的块；块内 `\\item` 按列表项再切分；"
      "纯英文参考文献条目不计。")
    A("- **字数** = 汉字数 + 西文词数（连续拉丁字母串/数字串各计 1 词）；标点、行内公式、"
      "`\\ref` 编号不计。")
    A("- **句** = 段落正文按 `。！？` 切分且含汉字的片段。")
    A("- 详细定义见 `01-总体统计.md` 第一节“统计口径”。")
    A("")
    A("## 各文件的判定规则")
    A("")
    A("### 02 长段落（>300 字）")
    A("")
    A("- 阈值：字数 >300；其中 >500 标为 `P0`（重点段）。")
    A("- 建议切分点：目标“每段 ≤250 字”，按句末位置均匀取点，且优先落在转折/递进词"
      "（但是/因此/另一方面/首先/最后…）开头的下一句之前。")
    A("- “切分理由”按段落特征自动生成：超长段、句数多、含超长句、转折位置等。")
    A("")
    A("### 03 列表化候选")
    A("")
    A("检测以下标记（同一段落内或相邻连续段落之间）：")
    A("")
    A("1. 中文序数（`第一，`/`第二、`/`第三：`）；")
    A("2. 括号序号（`（1）`/`(1)`）；")
    A("3. 顺序词（`首先`/`其次`/`再次`/`然后`/`最后` 中 ≥2 类）；")
    A("4. `一是`/`二是`；")
    A("5. 手工罗马序号（`\\uppercase\\expandafter{\\romannumeralN}.`，如第 47 章，不是 LaTeX 列表）；")
    A("6. 段首数字序号（`1.`/`2.`，含跨段成序列）；")
    A("7. 分号并列（一段 ≥5 个 `；` 且句数 ≤4）。")
    A("")
    A("“建议列表类型”按标记族映射为有序列表/步骤列表/要点列表/表格。")
    A("")
    A("### 04 纯文字墙节")
    A("")
    A("判定：节字数 >1500，且该节图数=0、表数=0、展示公式数=0（`参考文献` 节除外）。"
      "建议改造手段由规则组合：拆段、列表化、加小标题、补示意图/对照表、断句。")
    A("")
    A("### 05 强调与长句")
    A("")
    A("`\\uwave` 按章计数；长句 = 段内按 `。！？` 切分后字数 >80 的句子，行号由清洗后的"
      "字符位置回溯到源文件行；内联公式密度 = 节内 `$…$` 对数 / 节字数 ×1000。")
    A("")
    A("### 06 中英段落对照——方法与误差")
    A("")
    A("英文数据来自 `_attachments/build-feynman/audit/en/I_XX.txt`（本地忽略目录，"
      "从官方 eFLP 页面用 `innerText` 抓取）。**该文本并非严格“每段一行”**：")
    A("")
    A("- 正文段落被空行分隔；但**展示公式会被 MathJax 拆成一行一个符号的公式块**，"
      "行内公式也会把正文切成多行，导致公式多的章节出现大量短碎片行；")
    A("- 因此本工具先丢弃导航区、公式块、图/表标题，再把被展示公式切开的正文块按"
      "“上一块最后一行是否句末标点 + 本块是否大写开头”重建为段落。")
    A("")
    A("由于重建规则对“段末是展示公式、下一段以大写开头”的情况无法完全区分，"
      "英文段落数只能给一个**区间**：")
    A("")
    A("- **下界**：重建合并后的段落数（保守合并，倾向少算）；")
    A("- **上界**：含正文的空行块数（每个公式块都被当成段落边界，倾向多算）；")
    A("- 06 CSV 的“英文重建不确定度 = 上界 − 下界”列给出该章的区间宽度；宽度 >8 的章"
      "（公式密集章）其“中-英段差”不宜直接解读为合并。")
    A("")
    A("对照方法：")
    A("")
    A("1. 中文段落取清洗后的正文段（与 01 同口径）；")
    A("2. 用中文总字数 / 英文总词数估计换算比（本次第一卷全局比约 "
      f"**{ratio:.2f} 汉字/英词**）；")
    A("3. 动态规划对齐（允许 1:1、2:1、3:1 合并与两侧跳过，长度偏差取对数惩罚），"
      "把“一个中文段吸收 2–3 个英文段”识别为**疑似合并**，并给高/中/低置信度；")
    A("4. 第二、三卷第 1 章为**节选试译**，英文覆盖率 <100%，其段落差是“未译完”而非合并。")
    A("")
    A(f"> 本次全局换算比 = 第一卷正文总字数 / 第一卷英文词数 ≈ {ratio:.3f}。")
    A("")
    A("**与背景基线的口径冲突（重要）**：任务背景给出的“多数章节约 15% 的段落被合并、"
      "ch25/ch23/ch21/ch19 合并严重”，在本次严格口径下**没有复现**：")
    A("")
    A(f"- 第一卷中文正文段落 {fmt_int(totals['vol1']['paragraphs'])} 个（对照时把 3 个列表项并为 "
      f"1 个单元，共 {fmt_int(zh_total_cmp)} 个对照单元），英文重建段落下界 "
      f"{fmt_int(en_lo_total)} 个、上界 {fmt_int(en_hi_total)} 个；中文段落数介于两者之间，"
      f"**{len(v1cmp)} 章中有 {n_zh_ge_lo} 章中文段落数≥英文重建下界**，"
      "即总体上看不出系统性“段落被合并”；")
    hi_conf = [m for r in analysis["compare"] for m in r["merges"] if m["conf"] == "高"]
    hi_conf_en = sum(2 if m["kind"] == "merge2" else 3 for m in hi_conf)
    n_all_merges = sum(1 for r in analysis["compare"] for m in r["merges"])
    A(f"- 全书检出的疑似合并共 {n_all_merges} 处（涉及 "
      f"{sum(r['n_merged_en'] for r in analysis['compare'])} 个英文段），其中达到高置信度的只有 "
      f"{len(hi_conf)} 处（涉及 {hi_conf_en} 个英文段），逐条列在 `06b`，可人工核对；"
      f"另有 {len(split_chs)} 章（{'/'.join(split_chs)}）中文段落数超过英文上界，"
      "说明中文拆分多于合并；")
    A("- 旧结论很可能来自把英文抓取文本里的**公式碎片/长行**当成段落的口径——公式多的章"
      "（如 I-19 上界比下界高 60%、I-23 高 43%、I-21 高 28%、I-25 高 15%），"
      "“空行文本块数”会被展示公式显著抬高，从而看起来像“中文少了很多段”；")
    A("- 具体到背景点名的四章：I-25 的**末段**确有明显合并（中文 1 段 803 字吸收了英文 3–4 段，"
      "涉及 368+ 英词，见 06b 行 200），但 I-23、I-21 本口径下没有高置信合并，I-19 有 1 处；"
      "“ch25/ch23/ch21/ch19 合并严重”只能部分成立（ch25 章末较明显），其余三章证据不足；")
    A("- 需要说明：若把英文侧上界（每一个空行文本块都算段落）当作真实段数，合并率会接近旧说法；"
      "但那会把被展示公式切开的同段续文误当段落，不可取。本报告采用的下界+区间口径更保守，"
      "结论应表述为：**在可核对的高置信样例里**存在中文合并/拆分段（见 06b），"
      "但“多数章节 15% 合并、四章严重”这一量级需要人工按 06b 行号抽样复核后再写入方案。")
    A("")
    A("误差来源与量级：")
    A("")
    A("- 英文段落重建在公式多的章节可能多切/少切 1–3 段（用“不确定度”列量化）；")
    A("- 中文段落按源文件空行切分：若译者把多段合并成一段且中间无空行，计为合并（正是要检测的问题）；"
      "若译者拆分段落，则表现为“中文增补/拆分段数”；")
    A("- 译文对原文的增删（脚注、译注、信息补充）会造成个别段落对齐偏移，请结合"
      "“对齐质量”“英文覆盖率”列，不要只看合并率。")
    A("")
    A("## 已知局限")
    A("")
    A("1. **句长口径**：分号、冒号内的分句不单独切分，因此含多个并列分句的句子会被算作一句"
      "（这恰是需要列表化的信号）；引号内引用也算在同一句内。")
    A("2. **字数口径**：行内公式与 `\\ref` 编号不计字数，公式密集段落会略偏短；"
      "西文词与数字按“串”计 1 词，与中文字符不严格等长。")
    A("3. **段落口径以 LaTeX 源文件空行为准**：图/表/展示公式若独占空行块，会把前后文字"
      "分成两段（与印刷排版一致）；若译者把公式与正文写在同一块内，则算作一段。")
    A("4. **英文侧为二次重建**，不是人工段落标注；06 的合并判定请以“置信度=高”的样例为准，"
      "具体段落需人工核对 `06b` 的行号。")
    A("5. 第二、三卷仅第 1 章且为节选，全书统计由第一卷主导；不要外推到第二/三卷其他章。")
    A("6. 本工具做**文本计量**，不评价翻译质量或知识正确性；切分/列表化建议是启发式规则，"
      "需编辑人工判断。")
    A("7. 英文抓取目录是本地忽略目录，不在 git 中；若在其他机器复现 06，需要先有同一批 "
      "`en/*.txt`，否则 06 会输出“缺少英文抓取文件”。")
    A("")
    A("## 本次运行摘要")
    A("")
    A(f"- 章节：{totals['chapters']}；行数：{fmt_int(totals['lines'])}；"
      f"正文段落：{fmt_int(totals['paragraphs'])}；正文汉字：{fmt_int(totals['cjk'])}；"
      f"句子：{fmt_int(totals['sentences'])}。")
    A(f"- 图：{totals['figures']}；表：{totals['tables']}；展示公式：{totals['disp_eqs']}；"
      f"内联公式：{fmt_int(totals['inline_math'])}；脚注：{totals['footnotes']}；"
      f"`\\uwave`：{totals['uwave']}。")
    A(f"- 英文抓取目录：`{os.path.relpath(en_dir, REPO_ROOT)}`。")
    A("")
    path = os.path.join(out_dir, "README.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return path


# ---------------------------------------------------------------------------
# --check
# ---------------------------------------------------------------------------
def run_check(analysis):
    t = analysis["totals"]
    paras = analysis["paragraphs"]
    sents = analysis["sentences"]
    pl = [p["zici"] for p in paras]
    sl = [s["zici"] for s in sents]
    d = describe_len(pl)
    d2 = describe_len(sl)
    print("=== 口径自检 ===")
    print(f"章数 {t['chapters']}  行数 {t['lines']}  原始汉字 {t['raw_cjk']}  "
          f"section {t['sections']} (+{t['sections_star']}*)  原始空行块 {t['raw_blocks']}")
    print(f"正文段落 {t['paragraphs']}  列表项 {t['list_items']}  正文汉字 {t['cjk']}  "
          f"总字数 {t['zici']}  句数 {t['sentences']}")
    print(f"图 {t['figures']}  表 {t['tables']}  tabular {t['tabulars']}  展示公式 "
          f"{t['disp_eqs']}  内联公式 {t['inline_math']}  脚注 {t['footnotes']}  "
          f"uwave {t['uwave']}  refs {t['refs']}")
    print(f"段落: mean {d['mean']:.1f} median {d['median']:.0f} p90 {d['p90']:.0f} "
          f"max {d['max']}  >300 {d['n_gt300']} ({fmt_pct(d['n_gt300'], len(pl))}) "
          f">500 {d['n_gt500']}")
    print(f"句子: mean {d2['mean']:.1f} median {d2['median']:.0f} p90 {d2['p90']:.0f} "
          f"p99 {d2['p99']:.0f} max {d2['max']} >80 {sum(1 for v in sl if v > 80)} "
          f">150 {sum(1 for v in sl if v > 150)}")
    print(f"全局中英字词比 {analysis['global_ratio']:.3f}")
    print("\n每章速览：")
    for c in analysis["chapters"]:
        print(f"  {c['key']:7s} {c['title'][:14]:16s} 行 {c['n_lines']:5d} 节 {c['n_sections']:3d} "
              f"段 {len(c['paragraphs']):4d} 字 {c['cjk']:6d} 图 {c['figures']:3d} "
              f"表 {c['tables']:2d} 式 {c['disp_eqs']:4d} 内联 {c['inline_math']:4d} "
              f"脚注 {c['footnotes']:2d} uw {c['uwave']:3d}")
    print("\n中英对照速览：")
    for r in analysis["compare"]:
        c = r["chapter"]
        print(f"  {c['key']:7s} 中段 {r['n_zh']:4d} 英段 {r['n_en']:4d} 匹配 {r['n_match']:4d} "
              f"合并 {r['n_merge']:3d} 并英段 {r['n_merged_en']:3d} 覆盖 {r['coverage']:.2f} "
              f"中字 {r['zh_total']:6d} 英词 {r['en_total']:6d}")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description="费曼讲义中文版文本可读性审计")
    ap.add_argument("--check", action="store_true", help="只打印自检数字")
    ap.add_argument("--en-dir", default=DEFAULT_EN_DIR, help="英文抓取目录")
    ap.add_argument("--out-dir", default=OUT_DIR, help="输出目录")
    args = ap.parse_args(argv)

    analysis = build_analysis(args.en_dir)
    if args.check:
        run_check(analysis)
        return

    os.makedirs(args.out_dir, exist_ok=True)
    p01 = write_01(analysis, args.out_dir)
    p02 = write_02(analysis, args.out_dir)
    p03, rows03 = write_03(analysis, args.out_dir)
    p04, rows04 = write_04(analysis, args.out_dir)
    p05 = write_05(analysis, args.out_dir)
    p06, p06b, rows06 = write_06(analysis, args.out_dir)
    preadme = write_readme(analysis, args.out_dir, args.en_dir)
    print("已生成：")
    for p in (p01, p02, p03, p04, p05, p06, p06b, preadme):
        print("  ", os.path.relpath(p, REPO_ROOT))
    n_long = sum(1 for p in analysis["paragraphs"] if p["zici"] > LONG_PARA)
    print(f"长段落 {n_long} / 列表化候选行 {len(rows03)} / 纯文字墙节 {len(rows04)} / "
          f"中英对照 {len(rows06)} 章")


if __name__ == "__main__":
    main()
