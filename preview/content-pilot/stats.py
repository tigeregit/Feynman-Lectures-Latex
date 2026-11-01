#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""统计改造前后指标：段落数/平均段长/最大段长/列表/小标题/术语/图/选读比例等。

口径：
- 原文文字 = Chapter2.tex 中该节的全部 CJK 汉字（含脚注/译者注/公式外文字）；
- 改造后“内容单元” = 正文段 + 列表项 + 引文块（pullquote）+ 选读段；
  四类互不重叠、字数合计必须等于原文文字数（由本脚本断言）；
- 列表项长度含 \item[...] 中被移到标签里的原文序数词；
- 新增文字（导读/小标题/小结/图注）单独统计，不计入原文。
"""
import re
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SRC = REPO / "Chapters/VolumeI/Chapter2.tex"
BODY = HERE / "ch2-pilot-body.tex"

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
ORIG_SECTIONS = {"§2-1": (5, 25), "§2-3": (72, 82)}


def cjk(s):
    return len(CJK.findall(s))


def strip_comments(t):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in t.splitlines())


def strip_balanced_macros(s, names):
    for name in names:
        pat = "\\" + name
        while pat in s:
            i = s.index(pat)
            j = s.index("{", i)
            depth, k = 0, j
            while k < len(s):
                if s[k] == "{":
                    depth += 1
                elif s[k] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            s = s[:i] + s[k + 1:]
    return s


def plain_cjk(s, drop_new=True):
    s = strip_comments(s)
    if drop_new:
        s = strip_balanced_macros(s, ["runin"])
    s = re.sub(r"\\[A-Za-z]+", "", s)
    s = s.replace("{", "").replace("}", "")
    return cjk(s)


# ---------------- 原文 ----------------
lines = SRC.read_text(encoding="utf-8").splitlines()
orig = {}
for name, (a, b) in ORIG_SECTIONS.items():
    lens = []
    for i in range(a, b + 1):
        t = lines[i - 1].strip()
        if t:
            lens.append(plain_cjk(t, drop_new=False))
    orig[name] = dict(chars=sum(lens), paras=len(lens),
                      avg=round(sum(lens) / len(lens), 1), lens=lens,
                      max=max(lens), over250=sum(1 for n in lens if n > 250))

# ---------------- 改造后 ----------------
raw = strip_comments(BODY.read_text(encoding="utf-8"))
blocks, cur, depth = [], [], 0
for ln in raw.splitlines():
    depth += len(re.findall(r"\\begin\{", ln))
    depth -= len(re.findall(r"\\end\{", ln))
    if ln.strip() == "" and depth == 0:
        if cur:
            blocks.append("\n".join(cur))
            cur = []
    else:
        cur.append(ln)
if cur:
    blocks.append("\n".join(cur))

NEW_BLOCKS = ["\\chapterintro", "\\readingpath", "\\begin{conceptmap}",
              "\\begin{summarybox}", "\\begin{keybox}", "\\chapter{", "\\section{"]

res = {k: dict(text=[], items=[], quotes=[], optional=[], lists=0,
               runin=0, term=0, keyidea=0, pullquote=0, aside=0,
               conceptmap=0, summarybox=0, summary_items=0,
               chapterintro=0, readingpath=0) for k in orig}
cur_sec = None
for b in blocks:
    st = b.strip()
    if st.startswith("\\chapterintro"):
        res["§2-1"]["chapterintro"] += 1
        continue
    if st.startswith("\\readingpath"):
        res["§2-1"]["readingpath"] += 1
        continue
    m = re.match(r"\\section\{(.+?)\}", st)
    if m:
        cur_sec = "§2-1" if m.group(1) == "引言" else "§2-3"
        continue
    if cur_sec is None or st.startswith("\\chapter{"):
        continue
    s = res[cur_sec]
    s["runin"] += len(re.findall(r"\\runin\{", b))
    s["term"] += len(re.findall(r"\\term\{", b))
    s["keyidea"] += len(re.findall(r"\\keyidea\{", b))
    s["pullquote"] += len(re.findall(r"\\pullquote\{", b))
    s["aside"] += len(re.findall(r"\\aside\{", b))
    if "\\begin{conceptmap}" in b:
        s["conceptmap"] += 1
        continue
    if "\\begin{summarybox}" in b:
        s["summarybox"] += 1
        s["summary_items"] += len(re.findall(r"\\item", b))
        continue
    if st.startswith("\\begin{optional}"):
        inner = re.sub(r"\\begin\{optional\}|\\end\{optional\}", "", b)
        for para in re.split(r"\n\s*\n", inner):
            if plain_cjk(para):
                s["optional"].append(plain_cjk(para))
        continue
    if "\\begin{itemize}" in b or "\\begin{enumerate}" in b:
        s["lists"] += 1
        marks = list(re.finditer(r"\\item(?:\[([^\]]*)\])?", b))
        for idx, mm in enumerate(marks):
            start = mm.end()
            end = marks[idx + 1].start() if idx + 1 < len(marks) else len(b)
            body = b[start:end]
            label = mm.group(1) or ""
            subparas = [x for x in re.split(r"\n\s*\n", body) if plain_cjk(x)]
            if not subparas:
                s["items"].append(plain_cjk(label))
            else:
                s["items"].append(plain_cjk(label) + plain_cjk(subparas[0]))
                for sp in subparas[1:]:
                    s["items"].append(plain_cjk(sp))
        continue
    if st.startswith("\\pullquote"):
        i = b.index("{")
        depth, k = 0, i
        while k < len(b):
            if b[k] == "{":
                depth += 1
            elif b[k] == "}":
                depth -= 1
                if depth == 0:
                    break
            k += 1
        s["quotes"].append(plain_cjk(b[i + 1:k], drop_new=False))
        continue
    if st.startswith("\\begin{"):
        continue
    n = plain_cjk(b)
    if n:
        s["text"].append(n)

# ---- optional 占比：从各节原文块中独立扫描（含嵌套在列表项内的 optional） ----
sect_raw = {}
for m in re.finditer(r"\\section\{(.+?)\}", raw):
    pass
ms = list(re.finditer(r"\\section\{(.+?)\}", raw))
starts = [m.start() for m in ms] + [len(raw)]
for idx, m in enumerate(ms):
    sect_raw[m.group(1)] = raw[m.end():starts[idx + 1]]

opt_metrics = {}
for title, sec in sect_raw.items():
    tot = 0
    paras = 0
    for mm in re.finditer(r"\\begin\{optional\}(.*?)\\end\{optional\}", sec, re.S):
        inner = mm.group(1)
        for para in re.split(r"\n\s*\n", inner):
            if plain_cjk(para):
                tot += plain_cjk(para)
                paras += 1
    opt_metrics[title] = (tot, paras)

out = {}
for name in orig:
    o, s = orig[name], res[name]
    units = s["text"] + s["items"] + s["quotes"] + s["optional"]
    assert sum(units) == o["chars"], (name, sum(units), o["chars"])
    out[name] = {
        "orig": o,
        "after": {
            "units": len(units),
            "text_paras": len(s["text"]),
            "list_items": len(s["items"]),
            "quotes": len(s["quotes"]),
            "optional_paras_detected": len(s["optional"]),
            "avg_unit": round(sum(units) / len(units), 1),
            "avg_text": round(sum(s["text"]) / len(s["text"]), 1) if s["text"] else 0,
            "max_unit": max(units),
            "max_text": max(s["text"]) if s["text"] else 0,
            "over250": sum(1 for n in units if n > 250),
            "text_lens": s["text"], "item_lens": s["items"],
            "quote_lens": s["quotes"], "optional_lens": s["optional"],
            "lists": s["lists"], "runin": s["runin"], "term": s["term"],
            "keyidea": s["keyidea"], "pullquote": s["pullquote"],
            "aside": s["aside"], "conceptmap": s["conceptmap"],
            "summarybox": s["summarybox"], "summary_items": s["summary_items"],
        },
        "optional_chars": opt_metrics["引言" if name == "§2-1" else "量子物理学"][0],
        "optional_paras": opt_metrics["引言" if name == "§2-1" else "量子物理学"][1],
    }

tot = sum(v["orig"]["chars"] for v in out.values())
tot_opt = sum(v["optional_chars"] for v in out.values())
print(json.dumps(out, ensure_ascii=False, indent=1))
print()
for name, v in out.items():
    o, a = v["orig"], v["after"]
    print(f"{name}: 原文 {o['chars']} 字/{o['paras']} 段/均 {o['avg']}/最大 {o['max']}/>250 {o['over250']}"
          f"  →  改造后 {a['units']} 个内容单元（正文段 {a['text_paras']} + 列表项 {a['list_items']}"
          f" + 引文 {a['quotes']} + 选读段 {v['optional_paras']}），均 {a['avg_unit']}，最大 {a['max_unit']}，>250 {a['over250']}"
          f"；列表 {a['lists']} 个、小标题 {a['runin']}、术语 {a['term']}、关键句 {a['keyidea']}、引文 {a['pullquote']}、页边注 {a['aside']}、图 {a['conceptmap']}、小结 {a['summarybox']}（{a['summary_items']} 条）")
print(f"\n合计原文 {tot} 字；选读 {tot_opt} 字 = {100.0*tot_opt/tot:.1f}%；"
      f"列表 {sum(v['after']['lists'] for v in out.values())} 个；"
      f"项 {sum(v['after']['list_items'] for v in out.values())}；"
      f"小标题 {sum(v['after']['runin'] for v in out.values())}；"
      f"术语 {sum(v['after']['term'] for v in out.values())}；"
      f"关键句 {sum(v['after']['keyidea'] for v in out.values())}；"
      f"引文 {sum(v['after']['pullquote'] for v in out.values())}；"
      f"页边注 {sum(v['after']['aside'] for v in out.values())}；"
      f"图 {sum(v['after']['conceptmap'] for v in out.values())}；"
      f"小结 {sum(v['after']['summary_items'] for v in out.values())} 条")
