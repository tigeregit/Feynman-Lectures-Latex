#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""费曼物理学讲义（中文 LaTeX 版）插图现状审计脚本。

只读扫描 Chapters/ 与 Figures/，不修改任何源文件；把结构化统计写入
docs/analysis/visual/ 与 docs/analysis/visual/data/。

用法（在仓库根目录）：
    python3 tools/audit_figures.py            # 全量统计
    python3 tools/audit_figures.py --no-pdfinfo   # 跳过 pdfinfo（更快，无精确尺寸）

依赖：Python3 标准库；可选 poppler 的 pdfinfo（用于读取图片 PDF 的真实
页面尺寸 = 图形包围盒）。PNG/JPEG 尺寸用文件头解析，不依赖 Pillow。

编译期信息（图号、页码、所在节）来自 _attachments/build-feynman/Chapters/**/*.aux，
若该目录不存在则退化为源文件顺序编号。
"""
import argparse
import csv
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_MD_DIR = os.path.join(ROOT, "docs", "analysis", "visual")
DATA_DIR = os.path.join(OUT_MD_DIR, "data")
BUILD_DIR = os.path.join(ROOT, "_attachments", "build-feynman")

# 编译版式（见 _attachments/build-feynman/Feynman Lectures on Physics.log）
TEXTWIDTH_PT = 459.7983
TEXTHEIGHT_PT = 676.04005
PT_PER_CM = 72.27 / 2.54

CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

GRAPHIC_EXTS = ["", ".pdf", ".png", ".jpg", ".jpeg", ".PDF", ".PNG", ".JPG", ".JPEG"]

ENVS_FIG = ("figure", "wrapfigure")
ENVS_TABLE = ("table", "wraptable", "longtable", "tabular")  # tabular 只用于标记“有表”
DISP_EQ_ENVS = ("equation", "align", "alignat", "gather", "multline", "eqnarray",
                "flalign", "displaymath")
LIST_ENVS = ("itemize", "enumerate", "description")

CHAPTER_RE = re.compile(r"Chapter(\d+)\.tex$")


# --------------------------------------------------------------------------
# 基础工具
# --------------------------------------------------------------------------
def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_comment_line(line):
    """去掉行内未转义的 % 注释，返回去注释后的文本（保留行数）。"""
    out = []
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == "\\" and i + 1 < n:
            out.append(line[i:i + 2])
            i += 2
            continue
        if ch == "%":
            break
        out.append(ch)
        i += 1
    return "".join(out)


def brace_group(s, start):
    """s[start] == '{'，返回 (内容, 结束位置+1)；失败返回 (None, start)。"""
    if start >= len(s) or s[start] != "{":
        return None, start
    depth = 0
    i = start
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[start + 1:i], i + 1
        i += 1
    return None, start


def find_commands(text, cmd):
    """在文本中找 \\cmd{...}（跳过注释），返回 [(内容, 起, 止, 行内偏移)]"""
    res = []
    pat = re.compile(r"\\" + re.escape(cmd) + r"(?![a-zA-Z@])\s*\*?\s*(?=\{)")
    for m in pat.finditer(text):
        content, end = brace_group(text, m.end())
        if content is None:
            continue
        starred = "*" in m.group(0)
        res.append((content, m.start(), end, starred))
    return res


def cjk_count(s):
    return len(CJK_RE.findall(s))


def clean_tex_for_count(s):
    """去掉注释、命令名与常见控制序列，用于粗算可读文字量（本审计以 CJK 计）。"""
    return s


def safe_rel(path):
    return os.path.relpath(path, ROOT)


def md5_of(path, chunk=1 << 20):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


# --------------------------------------------------------------------------
# 章节 & 节解析
# --------------------------------------------------------------------------
def parse_chapters():
    chapters = []
    for vol in ("VolumeI", "VolumeII", "VolumeIII"):
        for path in sorted(glob.glob(os.path.join(ROOT, "Chapters", vol, "Chapter*.tex")),
                           key=lambda p: int(CHAPTER_RE.search(p).group(1))):
            m = CHAPTER_RE.search(path)
            chno = int(m.group(1))
            raw = read_text(path)
            lines = [strip_comment_line(l) for l in raw.split("\n")]
            # 原始行（含注释）用于代码引用展示
            raw_lines = raw.split("\n")
            ch_title = ""
            mch = re.search(r"\\chapter\*?\{", raw)
            if mch:
                ch_title, _ = brace_group(raw, mch.end() - 1)
            chapters.append(dict(
                volume=vol, chapter_no=chno, path=safe_rel(path),
                title=(ch_title or "").strip(), lines=lines, raw_lines=raw_lines,
                raw=raw,
            ))
    return chapters


def parse_sections(ch):
    lines = ch["lines"]
    starts = []
    for i, line in enumerate(lines):
        m = re.match(r"^\s*\\section(\*)?\{(.*)\}\s*$", line)
        if m:
            starts.append((i, m.group(2).strip(), m.group(1) == "*"))
    secs = []
    numbered = 0
    for k, (i, title, starred) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        body = "\n".join(lines[i + 1:end])
        if not starred:
            numbered += 1
        title = re.sub(r"\\(normalsize|small|large|footnotesize)\s*", "", title).strip()
        secs.append(dict(
            chapter=ch, section_no=(None if starred else numbered),
            starred=starred, title=title,
            start_line=i + 1,            # \section 所在行（1-based）
            body_start=i + 2,
            end_line=end,                # 下一 \section 前一行（1-based, 含）
            han=cjk_count(body),
            raw_body="\n".join(ch["raw_lines"][i + 1:end]),
            body=body,
        ))
    return secs


def count_env(body):
    """统计某个节正文中的环境数量。"""
    def cnt(names):
        return sum(len(re.findall(r"\\begin\{" + re.escape(n) + r"\*?\}", body)) for n in names)
    n_fig = cnt(("figure", "wrapfigure"))
    n_table = sum(len(re.findall(r"\\begin\{" + re.escape(n) + r"\}", body)) for n in ("table", "wraptable", "longtable"))
    n_eq = 0
    for n in DISP_EQ_ENVS:
        n_eq += len(re.findall(r"\\begin\{" + re.escape(n) + r"\*?\}", body))
    n_eq += len(re.findall(r"\\\[", body))
    n_list = cnt(LIST_ENVS)
    return n_fig, n_table, n_eq, n_list


# --------------------------------------------------------------------------
# 图表环境解析
# --------------------------------------------------------------------------
def parse_figure_blocks(ch):
    """解析章内 figure / wrapfigure 区块及其中的 caption / label / includegraphics。"""
    lines = ch["raw_lines"]
    blocks = []
    i = 0
    n = len(lines)
    cur_no = 0
    while i < n:
        m = re.match(r"^\s*\\begin\{(figure|wrapfigure)\}(\s*\[[^\]]*\])?", strip_comment_line(lines[i]))
        if not m:
            i += 1
            continue
        env = m.group(1)
        start = i
        j = i + 1
        while j < n and not re.match(r"^\s*\\end\{" + env + r"\}", strip_comment_line(lines[j])):
            j += 1
        end = min(j, n - 1)
        block_lines = [strip_comment_line(x) for x in lines[start:end + 1]]
        block_raw = "\n".join(lines[start:end + 1])
        block = "\n".join(block_lines)
        # wrapfigure 的宽度参数
        wrap_ratio = None
        mw = re.match(r"^\s*\\begin\{wrapfigure\}(\[[^\]]*\])?\{[^}]*\}\{([^}]*)\}", block_lines[0])
        if mw and mw.group(2):
            wrap_ratio = mw.group(2).strip()
        # 计算块内起始行号偏移，便于报告 caption 行
        offset = 0
        captions = []
        for cm in re.finditer(r"\\caption(\*?)\s*\{", block):
            content, endpos = brace_group(block, cm.end() - 1)
            if content is None:
                continue
            line_no = start + block[:cm.start()].count("\n") + 1
            captions.append(dict(text=content, line=line_no, starred=cm.group(1) == "*"))
        labels = []
        for lm in re.finditer(r"\\label\{([^}]*)\}", block):
            line_no = start + block[:lm.start()].count("\n") + 1
            labels.append(dict(name=lm.group(1).strip(), line=line_no))
        imgs = []
        for im in re.finditer(r"\\includegraphics(\s*\[[^\]]*\])?\s*\{", block):
            opts = (im.group(1) or "").strip()
            path, _ = brace_group(block, im.end() - 1)
            if path is None:
                continue
            line_no = start + block[:im.start()].count("\n") + 1
            imgs.append(dict(path=path.strip(), opts=opts, line=line_no))
        blocks.append(dict(
            chapter=ch, env=env, start_line=start + 1, end_line=end + 1,
            wrap_ratio=wrap_ratio, block=block, captions=captions,
            labels=labels, imgs=imgs, first_img=imgs[0] if imgs else None,
        ))
        i = end + 1
    return blocks


def parse_inline_graphics(ch, blocks):
    """figure/wrapfigure 之外的 \\includegraphics。"""
    lines = ch["lines"]
    block_ranges = [(b["start_line"], b["end_line"]) for b in blocks]
    extra = []
    for i, line in enumerate(lines):
        lineno = i + 1
        for im in re.finditer(r"\\includegraphics(\s*\[[^\]]*\])?\s*\{([^}]*)\}", line):
            if any(a <= lineno <= b for a, b in block_ranges):
                continue
            extra.append(dict(line=lineno, path=im.group(2).strip(),
                              opts=(im.group(1) or "").strip()))
    return extra


# --------------------------------------------------------------------------
# aux 编译信息
# --------------------------------------------------------------------------
def parse_aux_for(chapter):
    """读取该章编译 aux，返回 lof / lot / label_info / toc_sections / end_page。"""
    vol = chapter["volume"]
    aux = os.path.join(BUILD_DIR, "Chapters", vol,
                       "Chapter%d.aux" % chapter["chapter_no"])
    info = dict(lof=[], lot=[], labels={}, toc_sections=[], toc_chapter=None,
                end_page=None, exists=False)
    if not os.path.exists(aux):
        return info
    info["exists"] = True
    txt = read_text(aux)

    def parse_contentsline(kind):
        res = []
        for m in re.finditer(r"\\contentsline \{" + kind + r"\}", txt):
            content, end = brace_group(txt, m.end())
            if content is None:
                continue
            line_start = txt.find("\n", end)
            tail = txt[end:line_start if line_start > 0 else len(txt)]
            mm = re.match(r"\s*\{(\d+)\}", tail)
            page = int(mm.group(1)) if mm else None
            # numberline
            number = None
            mn = re.search(r"\\numberline \{([^}]*)\}", content)
            if mn:
                number = mn.group(1).strip()
            # 去掉命令后的 caption 文本
            cap = re.sub(r"\\numberline \{[^}]*\}", "", content).strip()
            if cap.startswith("{"):
                inner, iend = brace_group(cap, 0)
                if inner is not None and iend == len(cap):
                    cap = inner
            cap = re.sub(r"\\ignorespaces\s*", "", cap).strip()
            res.append(dict(number=number, caption=cap, page=page))
        return res

    info["lof"] = parse_contentsline("figure")
    info["lot"] = parse_contentsline("table")
    for sec in parse_contentsline("section"):
        info["toc_sections"].append(sec)
    # chapter TOC 行：\contentsline {chapter}{...}{页码}
    for m in re.finditer(r"\\contentsline \{chapter\}", txt):
        content, end = brace_group(txt, m.end())
        if content is None:
            continue
        tail = txt[end:end + 24]
        mm = re.search(r"\{(\d+)\}", tail)
        mn = re.search(r"\\numberline \{", content)
        number = title = None
        if mn:
            num, ne = brace_group(content, mn.end() - 1)
            number = (num or "").strip()
            title = content[ne:].strip()
        if mm:
            info["toc_chapter"] = dict(number=number, title=title, page=int(mm.group(1)))
            break
    m = re.search(r"\\setcounter\{page\}\{(\d+)\}", txt)
    if m:
        info["end_page"] = int(m.group(1))
    for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}", txt):
        name = m.group(1)
        if not name.startswith("figure:") and not name.startswith("tab:"):
            continue
        info["labels"][name] = dict(
            number=m.group(2).strip(), page=m.group(3).strip(),
            section=m.group(4).strip(),
        )
    return info


# --------------------------------------------------------------------------
# 图形文件尺寸 / 解析
# --------------------------------------------------------------------------
def pdfinfo_dims(path):
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=30)
        if out.returncode != 0:
            return None
        w = h = None
        pages = None
        for line in out.stdout.splitlines():
            if line.startswith("Pages:"):
                pages = int(re.search(r"(\d+)", line).group(1))
            elif line.startswith("Page size:") or line.startswith("Page size"):
                mm = re.search(r"([\d.]+)\s*x\s*([\d.]+)\s*pts", line)
                if mm:
                    w, h = float(mm.group(1)), float(mm.group(2))
        if w and h:
            return dict(width_pt=round(w, 2), height_pt=round(h, 2), pages=pages or 1)
    except Exception:
        return None
    return None


def png_dims(path):
    try:
        with open(path, "rb") as f:
            head = f.read(33)
        if head[:8] != b"\x89PNG\r\n\x1a\n":
            return None
        w = int.from_bytes(head[16:20], "big")
        h = int.from_bytes(head[20:24], "big")
        return dict(width_px=w, height_px=h)
    except Exception:
        return None


def jpg_dims(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                          0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h = int.from_bytes(data[i + 5:i + 7], "big")
                w = int.from_bytes(data[i + 7:i + 9], "big")
                return dict(width_px=w, height_px=h)
            if marker in (0xD8, 0xD9):
                i += 2
                continue
            seglen = int.from_bytes(data[i + 2:i + 4], "big")
            if seglen <= 0:
                break
            i += 2 + seglen
    except Exception:
        return None
    return None


def graphic_dims(path, use_pdfinfo=True):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        if not use_pdfinfo:
            return None
        return pdfinfo_dims(path)
    if ext == ".png":
        return png_dims(path)
    if ext in (".jpg", ".jpeg"):
        return jpg_dims(path)
    return None


def resolve_graphic(chapter, inc_path):
    """把 \\includegraphics{ChapterN/xxx} 解析为 Figures/VolumeX/... 真实文件。"""
    bases = [os.path.join(ROOT, "Figures", chapter["volume"])]
    # 主 tex 在 \part 之后切换 graphicspath；对 VolumeI 章仍以 VolumeI 为准
    for base in bases:
        for ext in GRAPHIC_EXTS:
            cand = os.path.join(base, inc_path + ext)
            if os.path.isfile(cand):
                return cand
    # 兜底：全库按 basename 查
    stem = os.path.basename(inc_path)
    for cand in glob.glob(os.path.join(ROOT, "Figures", "**", stem + ".*"), recursive=True):
        return cand
    return None


# --------------------------------------------------------------------------
# 引用解析
# --------------------------------------------------------------------------
def parse_all_refs(chapters):
    labels = {}     # name -> dict(chapter, line)
    refs = defaultdict(list)  # name -> [dict(chapter, line)]
    for ch in chapters:
        for i, line in enumerate(ch["lines"]):
            for lm in re.finditer(r"\\label\{([^}]*)\}", line):
                name = lm.group(1).strip()
                labels.setdefault(name, []).append(
                    dict(chapter=ch, line=i + 1))
            for rm in re.finditer(r"\\(?:ref|eqref|pageref|autoref)\{([^}]*)\}", line):
                refs[rm.group(1).strip()].append(dict(chapter=ch, line=i + 1))
    return labels, refs


HARD_REF_RE = re.compile(r"(图|表|式)\s*(\d+)\s*[\.\-]\s*(\d+)")


def parse_hardcoded_refs(chapter):
    r"""正文中手写的“图N.M/表N.M/式N.M”。

    排除假阳性：编号出现在命令参数里的情况
    （如 \includegraphics{Chapter20/当图20.2的...}、\label{tab:表8.1}、
    \ref{figure:当图20.2的...}、手工编号的 \caption*{表 8.1}）。
    """
    res = []
    skip_spans = []
    for i, line in enumerate(chapter["lines"]):
        spans = []
        for cmd in ("includegraphics", "label", "ref", "eqref", "pageref", "autoref", "caption"):
            for m in re.finditer(r"\\" + cmd + r"\b", line):
                start = line.find("{", m.end())
                if start < 0:
                    continue
                depth = 0
                j = start
                while j < len(line):
                    c = line[j]
                    if c == "\\":
                        j += 2
                        continue
                    if c == "{":
                        depth += 1
                    elif c == "}":
                        depth -= 1
                        if depth == 0:
                            break
                    j += 1
                spans.append((start, j + 1))
        for m in HARD_REF_RE.finditer(line):
            if any(a <= m.start() < b for a, b in spans):
                continue
            res.append(dict(kind=m.group(1), major=int(m.group(2)),
                            minor=int(m.group(3)), line=i + 1,
                            context=line[max(0, m.start() - 60):m.end() + 60]))
    return res


# --------------------------------------------------------------------------
# 主流程
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-pdfinfo", action="store_true", help="跳过 pdfinfo")
    args = ap.parse_args()
    use_pdfinfo = not args.no_pdfinfo

    os.makedirs(DATA_DIR, exist_ok=True)
    chapters = parse_chapters()
    print("章数:", len(chapters))

    # ---------------- 节统计 ----------------
    sections = []
    for ch in chapters:
        secs = parse_sections(ch)
        ch["sections"] = secs
        for s in secs:
            n_fig, n_table, n_eq, n_list = count_env(s["body"])
            s.update(n_fig=n_fig, n_table=n_table, n_eq=n_eq, n_list=n_list)
            sections.append(s)

    # ---------------- 图表块 ----------------
    blocks = []
    for ch in chapters:
        bs = parse_figure_blocks(ch)
        ch["blocks"] = bs
        blocks.extend(bs)
    print("figure/wrapfigure 区块:", len(blocks))

    # ---------------- aux 编译信息 ----------------
    for ch in chapters:
        ch["aux"] = parse_aux_for(ch)
        n_aux = len(ch["aux"]["lof"])
        caps = sum(len([c for c in b["captions"] if not c["starred"]]) for b in ch["blocks"])
        if ch["aux"]["exists"] and n_aux != caps:
            print("  [!] 编译图数与源 caption 数不一致: %s aux=%d caps=%d"
                  % (ch["path"], n_aux, caps))

    # 把编译图号/页码/所在节按顺序回填到 block（每个非星号 caption 对应一个 LOF 条目）
    for ch in chapters:
        lof = ch["aux"]["lof"]
        idx = 0
        for b in ch["blocks"]:
            b["compiled"] = []
            for c in b["captions"]:
                if c["starred"]:
                    b["compiled"].append(None)
                    continue
                item = lof[idx] if idx < len(lof) else None
                b["compiled"].append(item)
                # 若该 block 内 label 数量==非星号 caption 数量，则按下标对应
                idx += 1
        # 块内 label → 编译图号（label 出现在对应 caption 之后）
        b_idx = 0
        for b in ch["blocks"]:
            for c_i, c in enumerate(b["captions"]):
                if c["starred"]:
                    continue
                comp = b["compiled"][c_i] if c_i < len(b["compiled"]) else None
                if comp:
                    b.setdefault("__numbers__", []).append(comp["number"])
        # label 顺序与 caption 顺序对齐（正常情况 1:1；无 label 的 caption 缺失）
        labels_in_block = [l["name"] for l in b["labels"]]
        comp_list = [x for x in b["compiled"] if x]
        for k, name in enumerate(labels_in_block):
            if k < len(comp_list):
                ch["aux"]["labels"].setdefault(name, dict(
                    number=comp_list[k]["number"],
                    page=str(comp_list[k]["page"]),
                    section=""))
                ch["aux"]["labels"][name].update(
                    number=comp_list[k]["number"],
                    page=str(comp_list[k]["page"]))

    # ---------------- 节页码映射（来自编译 TOC） ----------------
    for ch in chapters:
        tocsecs = ch["aux"].get("toc_sections") or []
        numbered = [s for s in ch["sections"] if s["section_no"] is not None]
        for k, s in enumerate(numbered):
            if k < len(tocsecs) and tocsecs[k].get("page"):
                s["page_start"] = tocsecs[k]["page"]
                if k + 1 < len(tocsecs) and tocsecs[k + 1].get("page"):
                    s["page_end"] = tocsecs[k + 1]["page"]
                elif ch["aux"].get("end_page"):
                    s["page_end"] = ch["aux"]["end_page"] - 1
            else:
                s["page_start"] = s.get("page_start")
        # 星号节不参与页码映射
        for s in ch["sections"]:
            s.setdefault("page_start", "")
            s.setdefault("page_end", "")

    # ---------------- 引用 ----------------
    labels, refs = parse_all_refs(chapters)
    fig_labels = {k: v for k, v in labels.items() if k.startswith("figure:")}
    tab_labels = {k: v for k, v in labels.items() if k.startswith(("tab:", "Table:"))}
    dup_labels = {k: v for k, v in labels.items() if len(v) > 1}

    # ---------------- 图形文件清单 ----------------
    file_records = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "Figures", "**", "*"), recursive=True)):
        if not os.path.isfile(path):
            continue
        rec = dict(path=safe_rel(path), ext=os.path.splitext(path)[1].lower().lstrip("."),
                   bytes=os.path.getsize(path), md5=md5_of(path))
        dims = graphic_dims(path, use_pdfinfo=use_pdfinfo)
        rec.update(dims or {})
        if rec.get("width_pt") and rec.get("height_pt"):
            rec["aspect"] = round(rec["height_pt"] / rec["width_pt"], 3)
            rec["dim_source"] = "pdfinfo"
        elif rec.get("width_px") and rec.get("height_px"):
            rec["aspect"] = round(rec["height_px"] / rec["width_px"], 3)
            rec["dim_source"] = "header"
        else:
            rec["aspect"] = None
            rec["dim_source"] = ""
        file_records[path] = rec

    # ---------------- 解析 includegraphics 引用关系 ----------------
    inc_uses = []
    used_files = defaultdict(list)  # 绝对路径 -> [use]
    for ch in chapters:
        for b in ch["blocks"]:
            for im in b["imgs"]:
                resolved = resolve_graphic(ch, im["path"])
                use = dict(chapter=ch, block=b, line=im["line"], inc_path=im["path"],
                           opts=im["opts"], resolved=resolved)
                inc_uses.append(use)
                if resolved:
                    used_files[resolved].append(use)
        for im in parse_inline_graphics(ch, ch["blocks"]):
            resolved = resolve_graphic(ch, im["path"])
            use = dict(chapter=ch, block=None, line=im["line"], inc_path=im["path"],
                       opts=im["opts"], resolved=resolved)
            inc_uses.append(use)
            if resolved:
                used_files[resolved].append(use)

    # 主 tex 里的 titlepage 图片
    main_tex = read_text(os.path.join(ROOT, "Feynman Lectures on Physics.tex"))
    main_inc = []
    for m in re.finditer(r"\\includegraphics(\s*\[[^\]]*\])?\s*\{([^}]*)\}", main_tex):
        p = m.group(2).strip()
        line = main_tex[:m.start()].count("\n") + 1
        cand = os.path.join(ROOT, "Figures", "VolumeI", p)
        for ext in GRAPHIC_EXTS:
            if os.path.isfile(cand + ext):
                cand = cand + ext
                break
        main_inc.append(dict(line=line, path=p, resolved=cand if os.path.isfile(cand) else None))
        if os.path.isfile(cand):
            used_files[cand].append(dict(chapter=None, block=None, line=line,
                                         inc_path=p, opts=(m.group(1) or "").strip(),
                                         resolved=cand))

    # 未使用的图文件（孤儿）
    orphans = [r for p, r in file_records.items() if p not in used_files]
    # 内容重复文件
    md5_groups = defaultdict(list)
    for p, r in file_records.items():
        md5_groups[r["md5"]].append(r["path"])
    dups = [v for v in md5_groups.values() if len(v) > 1]

    # ---------------- 宽高 & 排版风险 ----------------
    def parse_width_ratio(opts):
        m = re.search(r"width\s*=\s*([\d.]+)\s*\\(?:textwidth|linewidth|columnwidth)", opts or "")
        if m:
            return float(m.group(1)), "textwidth"
        m = re.search(r"width\s*=\s*([\d.]+)\s*cm", opts or "")
        if m:
            return float(m.group(1)) / (TEXTWIDTH_PT / PT_PER_CM), "cm"
        m = re.search(r"height\s*=\s*([\d.]+)", opts or "")
        if m:
            return None, "height-only"
        return None, ""

    for use in inc_uses:
        ratio, unit = parse_width_ratio(use["opts"])
        use["width_ratio"] = ratio
        use["width_unit"] = unit
        rec = file_records.get(use["resolved"]) if use["resolved"] else None
        use["aspect"] = rec.get("aspect") if rec else None
        use["file_ext"] = rec.get("ext") if rec else None
        if ratio and use["aspect"]:
            h_pt = ratio * TEXTWIDTH_PT * use["aspect"]
            use["est_height_cm"] = round(h_pt / PT_PER_CM, 2)
            use["overflow_flag"] = h_pt > TEXTHEIGHT_PT
        else:
            use["est_height_cm"] = None
            use["overflow_flag"] = False

    # ---------------- 节内图表归属（源） ----------------
    for ch in chapters:
        for s in ch["sections"]:
            s["fig_blocks"] = [b for b in ch["blocks"]
                               if s["start_line"] <= b["start_line"] <= s["end_line"]]

    # ---------------- 图号引用一致性 ----------------
    chmap = {}
    for ch in chapters:
        chmap[(ch["volume"], ch["chapter_no"])] = ch
    # 每章编译图号集合
    for ch in chapters:
        ch["figure_numbers"] = [x["number"] for x in ch["aux"]["lof"]]
    hard_refs = []
    for ch in chapters:
        for hr in parse_hardcoded_refs(ch):
            hr["chapter"] = ch
            hard_refs.append(hr)
    # 硬编码引用 vs 本章图号
    for hr in hard_refs:
        ch = hr["chapter"]
        same_ch = hr["major"] == ch["chapter_no"]
        exists = False
        if hr["kind"] == "图":
            exists = ("%d.%d" % (hr["major"], hr["minor"])) in ch["figure_numbers"]
        elif hr["kind"] == "表":
            tab_nums = [x["number"] for x in ch["aux"]["lot"]]
            exists = ("%d.%d" % (hr["major"], hr["minor"])) in tab_nums
        hr["same_chapter"] = same_ch
        hr["number_exists"] = exists

    # 引用位置 vs 图块位置（阅读顺序）
    for ch in chapters:
        for b in ch["blocks"]:
            ref_lines = []
            for lab in b["labels"]:
                ref_lines += [r["line"] for r in refs.get(lab["name"], [])
                              if r["chapter"] is ch]
            b["ref_lines"] = sorted(ref_lines)
            if ref_lines:
                b["first_ref_line"] = min(ref_lines)
                b["ref_before_figure"] = min(ref_lines) < b["start_line"]
                b["ref_distance_lines"] = min(ref_lines) - b["start_line"]
            else:
                b["first_ref_line"] = None

    # ---------------- 输出 data/ ----------------
    # sections.csv
    with open(os.path.join(DATA_DIR, "sections.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "章标题", "节序", "节标题", "起始行", "结束行",
                    "正文汉字数", "figure块", "table块", "展示公式", "列表",
                    "有图有表", "编译图数", "节起始页", "节结束页", "图密度(图/千字)"])
        for ch in chapters:
            for s in ch["sections"]:
                fig_nums = []
                for b in s.get("fig_blocks", []):
                    for c in b.get("compiled", []):
                        if c:
                            fig_nums.append(c["number"])
                w.writerow([ch["volume"], ch["chapter_no"], ch["title"],
                            s["section_no"] if s["section_no"] is not None else "",
                            s["title"], s["start_line"], s["end_line"], s["han"],
                            s["n_fig"], s["n_table"], s["n_eq"], s["n_list"],
                            "是" if (s["n_fig"] or s["n_table"]) else "否",
                            len(fig_nums), s.get("page_start", ""), s.get("page_end", ""),
                            round(len(fig_nums) / (s["han"] / 1000), 2) if s["han"] else ""])

    # figures-compiled.csv
    with open(os.path.join(DATA_DIR, "figures-compiled.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "章标题", "环境", "块起始行", "块结束行", "图片路径",
                    "声明宽度", "解析文件", "图号", "页码", "caption数", "图注",
                    "label", "正文首次引用行", "引用在图前", "引用距图行数"])
        for ch in chapters:
            for b in ch["blocks"]:
                comp_numbers = [c["number"] if c else "" for c in b.get("compiled", [])]
                pages = [str(c["page"]) if c else "" for c in b.get("compiled", [])]
                cap_texts = ["[星号无编号]" if c["starred"] else c["text"] for c in b["captions"]]
                labels_str = ";".join(l["name"] for l in b["labels"])
                w.writerow([ch["volume"], ch["chapter_no"], ch["title"], b["env"],
                            b["start_line"], b["end_line"],
                            ";".join(i["path"] for i in b["imgs"]),
                            ";".join(i["opts"] for i in b["imgs"]),
                            ";".join(safe_rel(u["resolved"]) for u in used_files_of_block(inc_uses, b)),
                            ";".join(comp_numbers), ";".join(pages),
                            len(b["captions"]), " ‖ ".join(cap_texts), labels_str,
                            b.get("first_ref_line") or "",
                            "是" if b.get("ref_before_figure") else "否",
                            b.get("ref_distance_lines", "")])

    # figure-files.csv（全量文件清单，含未引用）
    with open(os.path.join(DATA_DIR, "figure-files.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["路径", "章目录", "类型", "KB", "页数", "宽pt", "高pt", "宽高比",
                    "像素宽", "像素高", "引用次数", "引用章", "用于caption", "md5前8"])
        for p, r in sorted(file_records.items()):
            uses = used_files.get(p, [])
            chapters_used = sorted({"V%s-Ch%d" % (u["chapter"]["volume"][-1], u["chapter"]["chapter_no"])
                                    if u["chapter"] else "titlepage" for u in uses})
            cap_used = False
            for u in uses:
                if u.get("block"):
                    cap_used = True
            w.writerow([r["path"], os.path.basename(os.path.dirname(p)), r["ext"],
                        round(r["bytes"] / 1024, 1), r.get("pages", ""),
                        r.get("width_pt", ""), r.get("height_pt", ""), r.get("aspect", ""),
                        r.get("width_px", ""), r.get("height_px", ""),
                        len(uses), ",".join(chapters_used), "是" if cap_used else "否",
                        r["md5"][:8]])

    # 顶层 figure-inventory.csv：题目要求的 6 项产出之一
    write_inventory(file_records, used_files)

    # hardcoded-refs.csv
    with open(os.path.join(DATA_DIR, "hardcoded-refs.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "行", "类型", "编号", "本章图号存在", "同一章号", "上下文"])
        for hr in hard_refs:
            w.writerow([hr["chapter"]["volume"], hr["chapter"]["chapter_no"], hr["line"],
                        hr["kind"], "%d.%d" % (hr["major"], hr["minor"]),
                        "是" if hr["number_exists"] else "否",
                        "是" if hr["same_chapter"] else "否",
                        hr["context"].replace("\n", " ")])

    # unreferenced-labels.csv
    with open(os.path.join(DATA_DIR, "unreferenced-labels.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["label", "卷", "章", "行", "编译图号", "图注/标题"])
        for name, occ in sorted(fig_labels.items()):
            if name in refs:
                continue
            for o in occ:
                ch = o["chapter"]
                info = ch["aux"]["labels"].get(name, {})
                # 找该 label 所属块的 caption
                cap = ""
                for b in ch["blocks"]:
                    if any(l["name"] == name for l in b["labels"]):
                        caps = [c["text"] for c in b["captions"] if not c["starred"]]
                        cap = caps[0] if caps else "[无caption]"
                w.writerow([name, ch["volume"], ch["chapter_no"], o["line"],
                            info.get("number", ""), cap])

    # ---------------- 硬编码图号集合（供未引用 label 判定“正文其实提到过”） ----------------
    for ch in chapters:
        ch["hard_numbers"] = set()
        for hr in parse_hardcoded_refs(ch):
            if hr["kind"] == "图":
                ch["hard_numbers"].add("%d.%d" % (hr["major"], hr["minor"]))
    for name, occ in fig_labels.items():
        for o in occ:
            ch = o["chapter"]
            info = ch["aux"]["labels"].get(name, {})
            num = info.get("number")
            o["compiled_number"] = num
            o["hard_referenced"] = num in ch.get("hard_numbers", set()) if num else False

    # ---------------- stats.json ----------------
    stats = build_stats(chapters, sections, blocks, inc_uses, file_records, used_files,
                        fig_labels, tab_labels, refs, dup_labels, orphans, dups,
                        hard_refs, labels_in_tex=labels)
    with open(os.path.join(DATA_DIR, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2, default=str)

    # chapter-summary.csv
    with open(os.path.join(DATA_DIR, "chapter-summary.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "标题", "节数", "汉字数", "figure块", "编译图数", "表数",
                    "页数", "图/页", "字/页", "图版面估算占比", "硬编码图号引用",
                    "有解释的图注", "未用label引用图"])
        for c in stats["per_chapter"]:
            w.writerow([c["volume"], c["chapter_no"], c["title"], c["sections"], c["han"],
                        c["blocks"], c["figures"], c["tables"], c["pages"],
                        c["fig_per_page"], c["han_per_page"],
                        c["fig_area_ratio"], c["hard_refs"],
                        "%d/%d" % (c["caption_rich"], c["caption_total"]),
                        c["unreferenced_labels"]])

    # heavy-sections.csv（文字大户，候选池）
    with open(os.path.join(DATA_DIR, "heavy-sections.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["层级", "卷", "章", "章标题", "节序", "节标题", "起始行", "结束行",
                    "汉字数", "figure块", "table块", "展示公式", "列表", "节起始页"])
        for h in stats["heavy_sections"]["v1_list"]:
            w.writerow(["A(>1500无图无表)", h["volume"], h["chapter_no"], h["chapter_title"],
                        h["section_no"], h["title"], h["start"], h["end"], h["han"],
                        0, 0, h["eq"], h["list"], ""])
        for h in stats["heavy_sections"]["strict_list"]:
            w.writerow(["B(>2000且无图/表/公式/列表)", h["volume"], h["chapter_no"],
                        h["chapter_title"], h["section_no"], h["title"], h["start"],
                        h["end"], h["han"], 0, 0, 0, 0, ""])

    # table-inventory.csv（表清单，供复用建议）
    with open(os.path.join(DATA_DIR, "table-inventory.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["卷", "章", "行号", "编号", "页码", "表题"])
        for ch in chapters:
            for item in ch["aux"]["lot"]:
                # 定位行号
                lineno = ""
                for i, line in enumerate(ch["raw_lines"]):
                    mm = re.search(r"\\caption\{(.*)", line)
                    if mm and item["caption"] and mm.group(1)[:6] in item["caption"]:
                        lineno = i + 1
                        break
                w.writerow([ch["volume"], ch["chapter_no"], lineno, item["number"],
                            item["page"], item["caption"]])

    print_summary(stats, chapters)


def used_files_of_block(inc_uses, block):
    return [u for u in inc_uses if u["block"] is block]


# --------------------------------------------------------------------------
# figure-inventory.csv（顶层要求产出）
# --------------------------------------------------------------------------
def write_inventory(file_records, used_files):
    out = os.path.join(OUT_MD_DIR, "figure-inventory.csv")
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["路径", "所属章", "类型", "宽pt", "高pt", "宽高比", "尺寸类别",
                    "文件KB", "是否被引用", "引用次数", "被引章/位置", "备注"])
        for p, r in sorted(file_records.items(),
                           key=lambda kv: natural_key(kv[0])):
            uses = used_files.get(p, [])
            chapters_used = []
            for u in uses:
                if u["chapter"] is None:
                    chapters_used.append("主文件titlepage")
                else:
                    chapters_used.append("%s-Ch%d L%d" % (
                        u["chapter"]["volume"], u["chapter"]["chapter_no"], u["line"]))
            aspect = r.get("aspect")
            if aspect is None:
                cat = "未知"
            elif aspect > 2.2:
                cat = "超竖长"
            elif aspect > 1.3:
                cat = "竖长"
            elif aspect >= 0.77:
                cat = "近方形"
            elif aspect >= 0.45:
                cat = "横长"
            else:
                cat = "超横长"
            note = []
            if not uses:
                note.append("未被任何章节引用（孤儿文件）")
            if r.get("pages") and r["pages"] > 1:
                note.append("多页PDF")
            if r.get("width_pt") and (r["width_pt"] < 60 or r["height_pt"] < 40):
                note.append("包围盒过小（可能字体/线条过细）")
            w.writerow([r["path"], os.path.basename(os.path.dirname(p)), r["ext"],
                        r.get("width_pt", ""), r.get("height_pt", ""),
                        aspect if aspect is not None else "",
                        cat, round(r["bytes"] / 1024, 1),
                        "是" if uses else "否", len(uses),
                        ";".join(chapters_used), "；".join(note)])


def natural_key(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


# --------------------------------------------------------------------------
# 汇总统计
# --------------------------------------------------------------------------
def build_stats(chapters, sections, blocks, inc_uses, file_records, used_files,
                fig_labels, tab_labels, refs, dup_labels, orphans, dups,
                hard_refs, labels_in_tex):
    def vol_stats(vol):
        chs = [c for c in chapters if c["volume"] == vol]
        secs = [s for c in chs for s in c["sections"]]
        numbered = [s for s in secs if not s["starred"]]
        # 页区间
        pages = []
        for c in chs:
            if c["aux"].get("toc_chapter") and c["aux"].get("end_page"):
                pages.append(c["aux"]["end_page"] - c["aux"]["toc_chapter"]["page"])
        return dict(
            chapters=len(chs), sections=len(numbered),
            sections_all=len(secs), starred=len(secs) - len(numbered),
            han=sum(s["han"] for s in secs),
            figures=sum(len(c["aux"]["lof"]) for c in chs),
            blocks=sum(len(c["blocks"]) for c in chs),
            tables=sum(len(c["aux"]["lot"]) for c in chs),
            pages=sum(pages) if pages else None,
            section_han_avg=round(sum(s["han"] for s in numbered) / len(numbered), 1) if numbered else 0,
            section_han_max=max([s["han"] for s in numbered], default=0),
        )

    ext_counter = Counter(r["ext"] for r in file_records.values())
    dim_known = [r for r in file_records.values() if r.get("aspect")]
    aspect_cats = Counter()
    for r in dim_known:
        a = r["aspect"]
        if a > 2.2:
            aspect_cats["超竖长(>2.2)"] += 1
        elif a > 1.3:
            aspect_cats["竖长(1.3-2.2)"] += 1
        elif a >= 0.77:
            aspect_cats["近方形(0.77-1.3)"] += 1
        elif a >= 0.45:
            aspect_cats["横长(0.45-0.77)"] += 1
        else:
            aspect_cats["超横长(<0.45)"] += 1

    # 每章统计
    per_chapter = []
    for ch in chapters:
        secs = ch["sections"]
        na = ch["aux"]
        page_span = None
        if na.get("toc_chapter") and na.get("end_page"):
            page_span = na["end_page"] - na["toc_chapter"]["page"]
        vtxt = {"VolumeI": "V1", "VolumeII": "V2", "VolumeIII": "V3"}[ch["volume"]]
        ch_tall = 0.0
        ch_cap_rich = 0
        ch_cap_total = 0
        for u in inc_uses:
            if u["chapter"] is ch and u.get("est_height_cm"):
                ch_tall += u["est_height_cm"]
        for b in ch["blocks"]:
            for c in b["captions"]:
                if c["starred"]:
                    continue
                ch_cap_total += 1
                txt = re.sub(r"\\footnotesize|\\relax|\\small", "", c["text"])
                if re.search(r"[，。；：]", txt) or cjk_count(txt) > 15:
                    ch_cap_rich += 1
        per_chapter.append(dict(
            hard_refs=sum(1 for h in hard_refs
                          if h["chapter"]["volume"] == ch["volume"]
                          and h["chapter"]["chapter_no"] == ch["chapter_no"]),
            caption_rich=ch_cap_rich, caption_total=ch_cap_total,
            fig_area_ratio=round(ch_tall / (page_span * TEXTHEIGHT_PT / PT_PER_CM), 3)
            if page_span else None,
            volume=vtxt, chapter_no=ch["chapter_no"], title=ch["title"],
            sections=len(secs), han=sum(s["han"] for s in secs),
            blocks=len(ch["blocks"]),
            figures=len(na["lof"]), tables=len(na["lot"]),
            pages=page_span,
            fig_per_page=round(len(na["lof"]) / page_span, 2) if page_span else None,
            han_per_page=round(sum(s["han"] for s in secs) / page_span, 0) if page_span else None,
            unreferenced_labels=sum(1 for k, v in fig_labels.items()
                                    if k in na["labels"] and k not in refs),
            heavy_sections=[dict(title=s["title"], han=s["han"], start=s["start_line"],
                                 fig=s["n_fig"], tab=s["n_table"], eq=s["n_eq"])
                            for s in secs if s["han"] > 1500],
        ))

    # 文字大户（>1500 字且无图无表）
    heavy = [dict(volume=s["chapter"]["volume"], chapter_no=s["chapter"]["chapter_no"],
                  chapter_title=s["chapter"]["title"], title=s["title"],
                  section_no=s["section_no"], han=s["han"],
                  start=s["start_line"], end=s["end_line"],
                  eq=s["n_eq"], list=s["n_list"])
             for s in sections if not s["starred"] and s["han"] > 1500
             and s["n_fig"] == 0 and s["n_table"] == 0]
    heavy_v1 = [h for h in heavy if h["volume"] == "VolumeI"]
    heavy_b = [dict(volume=s["chapter"]["volume"], chapter_no=s["chapter"]["chapter_no"],
                    chapter_title=s["chapter"]["title"], title=s["title"],
                    section_no=s["section_no"], han=s["han"],
                    start=s["start_line"], end=s["end_line"])
               for s in sections if not s["starred"]
               if s["han"] > 2000 and s["n_fig"] == 0 and s["n_table"] == 0
               and s["n_eq"] == 0 and s["n_list"] == 0 and s["chapter"]["volume"] == "VolumeI"]

    # 节图密度（图/千字）
    sec_density = []
    for s in sections:
        n_comp = 0
        for b in s.get("fig_blocks", []):
            n_comp += len([c for c in b.get("compiled", []) if c])
        sec_density.append(dict(
            volume=s["chapter"]["volume"], chapter_no=s["chapter"]["chapter_no"],
            title=s["title"], han=s["han"], figures=n_comp,
            density=round(n_comp / (s["han"] / 1000), 2) if s["han"] else None))

    # 引用一致性
    fig_label_refs = {k: v for k, v in refs.items() if k.startswith("figure:")}
    unref = [k for k in fig_labels if k not in refs]
    cross = []
    for k, occ in fig_labels.items():
        for o in occ:
            for r in refs.get(k, []):
                if r["chapter"] is not o["chapter"]:
                    cross.append(dict(label=k, def_ch=o["chapter"]["chapter_no"],
                                      ref_ch=r["chapter"]["chapter_no"], ref_line=r["line"]))

    # 图注分析（编译 LOF）
    all_lof = []
    for ch in chapters:
        for item in ch["aux"]["lof"]:
            all_lof.append(dict(chapter=ch, number=item["number"],
                                caption=item["caption"], page=item["page"]))
    def cap_is_empty(c):
        c = (c or "").strip()
        c = re.sub(r"\\relax|\\ignorespaces|\\footnotesize|\\small", "", c).strip()
        return c == ""
    empty_caps = [x for x in all_lof if cap_is_empty(x["caption"])]
    formula_caps = [x for x in all_lof if re.search(r"\$", x["caption"] or "")
                    and cjk_count(x["caption"] or "") < 15]
    punct_caps = [x for x in all_lof if re.search(r"[，。；：]", x["caption"] or "")]
    bold_prefix = [x for x in all_lof if "footnotesize" in (x["caption"] or "")]
    source_caps = [x for x in all_lof if re.search(r"转载自|来源|摘自|引自|after |from ", x["caption"] or "")]
    short_caps = [x for x in all_lof if cjk_count(x["caption"] or "") <= 10 and not re.search(r"\$", x["caption"] or "")]

    # 未被正文提及的图（label 引用 / 硬编码编号 / 星号图 三类都算“提到”）
    mentioned_numbers = {}
    for ch in chapters:
        mentioned_numbers[ch["volume"], ch["chapter_no"]] = set(ch.get("hard_numbers", set()))
    never_mentioned = []
    for ch in chapters:
        for item in ch["aux"]["lof"]:
            num = item["number"]
            lab_ref = False
            for b in ch["blocks"]:
                pass
        # 更直接：label -> number -> refs
        for lab, occ in fig_labels.items():
            for o in occ:
                if o["chapter"] is not ch:
                    continue
                num = o.get("compiled_number")
                hard = num in ch.get("hard_numbers", set())
                if lab not in refs and not hard:
                    never_mentioned.append(dict(
                        volume=ch["volume"], chapter_no=ch["chapter_no"],
                        number=num, label=lab, line=o["line"]))
    # 只有硬编码编号、没有 label 引用的图
    hard_only = []
    for name, occ in fig_labels.items():
        for o in occ:
            if name in refs:
                continue
            ch = o["chapter"]
            num = o.get("compiled_number")
            if num and num in ch.get("hard_numbers", set()):
                hard_only.append(dict(volume=ch["volume"], chapter_no=ch["chapter_no"],
                                      number=num, label=name, line=o["line"]))

    # 图注 vs 文件名 一致性
    cap_filename = dict(exact=0, contains=0, none=0, total=0, examples=[])
    for ch in chapters:
        for b in ch["blocks"]:
            stems = [os.path.splitext(os.path.basename(i["path"]))[0] for i in b["imgs"]]
            for c in b["captions"]:
                if c["starred"]:
                    continue
                txt = re.sub(r"\\(footnotesize|small|normalsize|relax)\s*", "", c["text"]).strip()
                txt = txt.replace("$", "")
                if not txt:
                    continue
                cap_filename["total"] += 1
                hit = "none"
                for stem in stems:
                    st = stem.replace("$", "")
                    if txt == st:
                        hit = "exact"
                        break
                    if txt and (txt in st or st in txt):
                        hit = "contains"
                cap_filename[hit] += 1
                if hit == "none" and len(cap_filename["examples"]) < 12:
                    cap_filename["examples"].append(dict(
                        chapter=ch["chapter_no"], caption=txt, stems=stems))

    # 表格 label 位置（\label 在 \caption 之前 = 编号错位隐患）
    bad_tab_labels = []
    for ch in chapters:
        lines = ch["raw_lines"]
        for i, line in enumerate(lines):
            if re.search(r"\\begin\{table\}", line):
                j = i + 1
                lab_line = cap_line = None
                while j < len(lines) and not re.search(r"\\end\{table\}", lines[j]):
                    if lab_line is None and re.search(r"\\label\{", lines[j]):
                        lab_line = j + 1
                    if cap_line is None and re.search(r"\\caption", lines[j]):
                        cap_line = j + 1
                    j += 1
                if lab_line and cap_line and lab_line < cap_line:
                    bad_tab_labels.append(dict(
                        volume=ch["volume"], chapter_no=ch["chapter_no"],
                        label_line=lab_line, caption_line=cap_line))

    # 图文件尺寸统计
    dims = [r for r in file_records.values() if r.get("width_pt") and r.get("height_pt")]
    dims_sorted_w = sorted(r["width_pt"] for r in dims)
    dims_sorted_h = sorted(r["height_pt"] for r in dims)
    bytes_sorted = sorted(r["bytes"] for r in file_records.values())
    sizes = dict(
        n=len(dims),
        width_pt=dict(min=round(dims_sorted_w[0], 1) if dims_sorted_w else None,
                      p25=round(dims_sorted_w[len(dims_sorted_w) // 4], 1) if dims_sorted_w else None,
                      median=round(median(dims_sorted_w), 1) if dims_sorted_w else None,
                      p75=round(dims_sorted_w[3 * len(dims_sorted_w) // 4], 1) if dims_sorted_w else None,
                      max=round(dims_sorted_w[-1], 1) if dims_sorted_w else None),
        height_pt=dict(min=round(dims_sorted_h[0], 1) if dims_sorted_h else None,
                       median=round(median(dims_sorted_h), 1) if dims_sorted_h else None,
                       max=round(dims_sorted_h[-1], 1) if dims_sorted_h else None),
        bytes=dict(min=round(bytes_sorted[0] / 1024, 1),
                   median=round(median(bytes_sorted) / 1024, 1),
                   max=round(bytes_sorted[-1] / 1024, 1)),
        extreme_tall=[dict(path=r["path"], aspect=r["aspect"]) for r in sorted(
            dims, key=lambda r: -r["aspect"])[:5]],
        extreme_wide=[dict(path=r["path"], aspect=r["aspect"]) for r in sorted(
            dims, key=lambda r: r["aspect"])[:5]],
        smallest=[dict(path=r["path"], w=r["width_pt"], h=r["height_pt"]) for r in sorted(
            dims, key=lambda r: r["width_pt"] * r["height_pt"])[:5]],
        largest=[dict(path=r["path"], w=r["width_pt"], h=r["height_pt"]) for r in sorted(
            dims, key=lambda r: -(r["width_pt"] * r["height_pt"]))[:5]],
    )

    # 文件名统计
    fname_stats = dict(total=len(file_records), over_20=0, over_30=0,
                       with_punct=0, with_parens=0, longest=[])
    for r in file_records.values():
        stem = os.path.splitext(os.path.basename(r["path"]))[0]
        fname_stats["total"] += 0
        if len(stem) > 20:
            fname_stats["over_20"] += 1
        if len(stem) > 30:
            fname_stats["over_30"] += 1
        if re.search(r"[，。；：、]", stem):
            fname_stats["with_punct"] += 1
        if re.search(r"[（(].*[）)]", stem):
            fname_stats["with_parens"] += 1
    fname_stats["longest"] = sorted(
        [dict(path=r["path"], n=len(os.path.splitext(os.path.basename(r["path"]))[0]))
         for r in file_records.values()], key=lambda x: -x["n"])[:8]

    # 被重复使用的图文件
    reuse = [dict(path=r["path"], count=len(used_files.get(p, [])))
             for p, r in file_records.items() if len(used_files.get(p, [])) > 1]

    # 块级别统计
    wrap_n = sum(1 for b in blocks if b["env"] == "wrapfigure")
    captions_total = sum(len(b["captions"]) for b in blocks)
    starred = sum(1 for b in blocks for c in b["captions"] if c["starred"])
    multi_cap_blocks = sum(1 for b in blocks if len(b["captions"]) > 1)
    no_label_blocks = sum(1 for b in blocks if not b["labels"] and
                          any(not c["starred"] for c in b["captions"]))
    unlabeled_captions = sum(1 for b in blocks
                             for c in b["captions"] if not c["starred"]
                             and len(b["labels"]) < len([x for x in b["captions"] if not x["starred"]]))
    ref_before = sum(1 for b in blocks if b.get("ref_before_figure"))
    ref_after = sum(1 for b in blocks if b.get("first_ref_line") and not b.get("ref_before_figure"))
    ref_none = sum(1 for b in blocks if not b.get("first_ref_line"))

    overflow = [u for u in inc_uses if u.get("overflow_flag")]
    tiny = [u for u in inc_uses if u.get("est_height_cm") is not None and u["est_height_cm"] < 2.5]
    tall = [u for u in inc_uses if u.get("est_height_cm") is not None
            and u["est_height_cm"] >= 0.85 * TEXTHEIGHT_PT / PT_PER_CM]
    unresolved = [u for u in inc_uses if not u["resolved"]]

    hard_bad = [h for h in hard_refs if h["kind"] in ("图", "表")
                and (not h["number_exists"])]

    stats = dict(
        generated_by="tools/audit_figures.py",
        textwidth_pt=TEXTWIDTH_PT, textheight_pt=TEXTHEIGHT_PT,
        volumes=dict(VolumeI=vol_stats("VolumeI"), VolumeII=vol_stats("VolumeII"),
                     VolumeIII=vol_stats("VolumeIII")),
        files=dict(total=len(file_records), by_ext=dict(ext_counter),
                   dim_known=len(dim_known), aspect_cats=dict(aspect_cats),
                   orphans=len(orphans),
                   orphan_list=[dict(path=o["path"], ext=o["ext"], kb=round(o["bytes"] / 1024, 1))
                                for o in orphans],
                   duplicates=dups),
        figures=dict(never_mentioned=never_mentioned,
                     hard_only_referenced=hard_only,
                     naver_mentioned_count=len(never_mentioned),
                     hard_only_count=len(hard_only)),
        caption_filename=cap_filename,
        sizes=sizes,
        filenames=fname_stats,
        reuse=reuse,
        bad_table_labels=bad_tab_labels,
        blocks=dict(total=len(blocks), wrapfigure=wrap_n,
                    figure=len(blocks) - wrap_n, captions=captions_total,
                    starred=starred, multi_caption_blocks=multi_cap_blocks,
                    blocks_without_label=no_label_blocks,
                    captions_without_label=unlabeled_captions,
                    ref_before=ref_before, ref_after=ref_after, ref_none=ref_none),
        labels=dict(total=len(labels_in_tex), figure=len(fig_labels), table=len(tab_labels),
                    table_tab_prefix=sum(1 for k in tab_labels if k.startswith("tab:")),
                    table_Table_prefix=sum(1 for k in tab_labels if k.startswith("Table:")),
                    figure_referenced=len(fig_labels) - len(unref),
                    figure_unreferenced=len(unref),
                    unreferenced_list=unref,
                    table_unreferenced=[k for k in tab_labels if k not in refs],
                    duplicates={k: [(o["chapter"]["volume"], o["chapter"]["chapter_no"], o["line"])
                                    for o in v] for k, v in dup_labels.items()},
                    ref_calls_to_figures=sum(len(v) for v in fig_label_refs.values())),
        captions=dict(total=len(all_lof), empty=len(empty_caps),
                      empty_list=[(x["chapter"]["volume"], x["chapter"]["chapter_no"],
                                   x["number"]) for x in empty_caps],
                      formula_only=len(formula_caps),
                      with_punctuation=len(punct_caps),
                      with_footnotesize=len(bold_prefix),
                      with_source_credit=len(source_caps),
                      source_credit_list=[(x["chapter"]["volume"], x["chapter"]["chapter_no"],
                                           x["number"], x["caption"][:90]) for x in source_caps],
                      bare_title=len(short_caps),
                      median_han=median([cjk_count(x["caption"] or "") for x in all_lof])),
        placement=dict(unresolved=len(unresolved),
                       unresolved_list=[(u["chapter"]["volume"], u["chapter"]["chapter_no"],
                                         u["line"], u["inc_path"]) for u in unresolved],
                       overflow_risk=len(overflow),
                       overflow_list=[(u["chapter"]["volume"], u["chapter"]["chapter_no"],
                                       u["line"], u["inc_path"], u["est_height_cm"])
                                      for u in overflow],
                       tiny=len(tiny),
                       tiny_list=[(u["chapter"]["volume"], u["chapter"]["chapter_no"],
                                   u["line"], u["inc_path"], u["est_height_cm"]) for u in tiny],
                       tall=len(tall),
                       tall_list=[(u["chapter"]["volume"], u["chapter"]["chapter_no"],
                                   u["line"], u["inc_path"], u["est_height_cm"],
                                   u["aspect"]) for u in tall]),
        heavy_sections=dict(all=len(heavy), v1=len(heavy_v1),
                            v1_sum_han=sum(h["han"] for h in heavy_v1),
                            v1_list=heavy_v1,
                            strict_v1=len(heavy_b), strict_list=heavy_b),
        per_chapter=per_chapter,
        section_density=sec_density,
        hardcoded_refs=dict(total=len(hard_refs),
                            by_kind=dict(Counter(h["kind"] for h in hard_refs)),
                            bad=[dict(volume=h["chapter"]["volume"],
                                      chapter_no=h["chapter"]["chapter_no"],
                                      line=h["line"], kind=h["kind"],
                                      number="%d.%d" % (h["major"], h["minor"]),
                                      context=h["context"]) for h in hard_bad]),
        cross_chapter_refs=cross,
    )
    return stats


def median(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    n = len(xs)
    return xs[n // 2] if n % 2 else round((xs[n // 2 - 1] + xs[n // 2]) / 2, 1)


def print_summary(stats, chapters):
    print("\n=== 概览 ===")
    for v, s in stats["volumes"].items():
        print(v, s)
    print("文件:", stats["files"]["total"], stats["files"]["by_ext"],
          "孤儿:", stats["files"]["orphans"])
    print("块:", stats["blocks"])
    print("labels:", {k: v for k, v in stats["labels"].items() if k != "unreferenced_list"})
    print("caption:", stats["captions"])
    print("placement:", {k: v for k, v in stats["placement"].items()
                         if not k.endswith("_list")})
    print("heavy:", {k: v for k, v in stats["heavy_sections"].items()
                     if not k.endswith("_list")})
    print("hardcoded:", stats["hardcoded_refs"]["total"],
          stats["hardcoded_refs"]["by_kind"],
          "bad:", len(stats["hardcoded_refs"]["bad"]))
    print("\n=== 未引用 label ===")
    for u in stats["labels"]["unreferenced_list"]:
        print(" ", u)
    print("\n=== 孤儿文件 ===")
    for o in stats["files"]["orphan_list"]:
        print(" ", o)

    # 章节图密度表
    print("\n=== 每章（页数/图数/图密度） ===")
    print("章 | 标题 | 节数 | 汉字 | 图 | 表 | 页 | 图/页 | 字/页")
    for c in stats["per_chapter"]:
        print("%s-%s | %s | %s | %s | %s | %s | %s | %s | %s" % (
            c["volume"][-1], c["chapter_no"], c["title"], c["sections"], c["han"],
            c["figures"], c["tables"], c["pages"], c["fig_per_page"], c["han_per_page"]))


if __name__ == "__main__":
    main()
