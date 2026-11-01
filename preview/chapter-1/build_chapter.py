#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Chapter 1《原子的运动》阅读效率改造 —— 机械拼装脚本（零删改保证）

用法（在仓库根目录或任意目录均可）：
    python3 preview/chapter-1/build_chapter.py

做法：
  1. 从 `git show main:Chapters/VolumeI/Chapter1.tex` 读取原文（不依赖工作区状态）；
  2. 对每个正文段落用"切分锚点 + 断言唯一命中"的方式插入段落分隔/列表环境/
     语义宏（\term、\keyidea）；新增文字块（导读/小标题/小结/概念图/读图提示）
     整块用 %<<<NEW ... %>>>NEW 包住；
  3. 对每个被改动的段落做**逐字符内容校验**（复用 tools/verify_chapter.py 的
     content_chars），保证原文可见文字序列一字不差；
  4. 写回 Chapters/VolumeI/Chapter1.tex。

原文一个字都没有重抄：所有正文文字都从原文行切片得到，脚本只做"插入"。
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC_REL = "Chapters/VolumeI/Chapter1.tex"
OUT = REPO / SRC_REL

sys.path.insert(0, str(REPO / "tools"))
import verify_chapter as vc  # noqa: E402

NEW_OPEN = "%<<<NEW"
NEW_CLOSE = "%>>>NEW"


def newblock(*lines: str) -> str:
    """把若干行包成一个 NEW 标记块。"""
    return "\n".join([NEW_OPEN, *lines, NEW_CLOSE])


def rep(text: str, old: str, new: str) -> str:
    assert text.count(old) == 1, f"replace 目标不唯一/不存在: {old!r} count={text.count(old)}"
    return text.replace(old, new)


def cut_before(text: str, *anchors: str) -> list[str]:
    """在 anchors 之前切开；每个锚点必须在剩余文本中唯一命中。返回 len(anchors)+1 段。"""
    parts, rest = [], text
    for a in anchors:
        cnt = rest.count(a)
        assert cnt == 1, f"切分锚点不唯一/不存在: {a!r} count={cnt}"
        i = rest.index(a)
        parts.append(rest[:i].rstrip())
        rest = rest[i:]
    parts.append(rest)
    for p in parts:
        assert p.strip(), "切出了空段"
    return parts


def listify(env: str, items: list[str], label_prefix: bool = False) -> str:
    """生成列表：环境起止行的命令名放进 NEW 块（避免校验串入环境名），列表项为原文。"""
    out = [NEW_OPEN, "\\begin{%s}" % env, NEW_CLOSE]
    out.extend(items)
    out.extend([NEW_OPEN, "\\end{%s}" % env, NEW_CLOSE])
    return "\n".join(out)


# ---------------------------------------------------------------- 新增文字内容
CHAPTER_INTRO = newblock(
    r"\chapterintro{%",
    r"\textbf{一句话定位}：本章不推公式，只回答一个问题——世界是由什么构成的？答案是一句话：万物由原子构成。\par",
    r"\textbf{本章要点}：",
    r"\begin{itemize}",
    r"  \item 一切知识都只是近似；物理教学不能先列公理，只能一步一步来。",
    r"  \item 假如只能留一句话给下一代，那就是原子的假设：万物由不停运动的原子构成。",
    r"  \item 原子很小，半径约 $1\sim2\times10^{-8}$ 厘米；把水滴放大十亿倍才看得见分子排列。",
    r"  \item 固体、液体、气体、蒸发、溶解、燃烧，都是原子的运动与重新组合。",
    r"  \item 布朗运动与 X 射线晶体分析，是原子假说的直接证据。",
    r"\end{itemize}",
    r"\textbf{与前后章的关系}：本章是全书的开篇与总纲，只立下“原子”这一基本假设；第 2 章接着勾画物理学的基本概念，第 3 章讨论物理学与其他科学的关系。\par",
    r"}",
)

READING_PATH = newblock(
    r"\readingpath{速读路径：§1-1 看“为什么不先列公理”一段；§1-2 看“从水滴到原子核”的尺度阶梯图；§1-3、§1-4 各看两个段内小标题；每节末尾的“小结”可当复查清单。精读路径：按正文顺序读；§1-4 中讲化学命名的一段标了“选读”，跳过不影响主线。}",
)

RUNIN = {
    9: newblock(r"\runin{为什么不先列公理}"),
    15: newblock(r"\runin{实验怎么会出错}"),
    27: newblock(r"\runin{一句话的原子假说}"),
    71: newblock(r"\runin{熔解与绝对零度}"),
    85: newblock(r"\runin{蒸发为什么会冷却}"),
    97: newblock(r"\runin{盐如何溶解与结晶}"),
    120: newblock(r"\runin{碳怎样燃烧}"),
    132: newblock(r"\runin{紫罗兰的香气}"),
}

SUMMARY_S1 = newblock(
    r"\begin{summarybox}[§1-1 小结]",
    r"\begin{itemize}",
    r"  \item 物理知识可以浓缩为少数定律，但掌握它们并不容易。",
    r"  \item 不能先列公理：不知全部定律、概念又太陌生。",
    r"  \item 一切知识都只是近似；近似的定律在哲学上仍可能完全错误。",
    r"  \item 先教精确的陌生定律还是简单的近似定律？从简单近似起步。",
    r"\end{itemize}",
    r"\end{summarybox}",
)

SUMMARY_S2 = newblock(
    r"\begin{summarybox}[§1-2 小结]",
    r"\begin{itemize}",
    r"  \item 一句话：万物由不停运动、彼此吸引又排斥的原子构成。",
    r"  \item 原子半径约 $1\sim2\times10^{-8}$ 厘米；放大十亿倍才看得见分子排列。",
    r"  \item 压力来自分子撞击；压缩升温、膨胀降温都可用原子解释。",
    r"  \item 冰是规则排列的晶体；绝对零度时原子仍在振动，氦除外。",
    r"\end{itemize}",
    r"\end{summarybox}",
)

SUMMARY_S3 = newblock(
    r"\begin{summarybox}[§1-3 小结]",
    r"\begin{itemize}",
    r"  \item 蒸发是动态平衡：离开与回来的分子数相等时看不出变化。",
    r"  \item 分子带走能量使液体冷却——吹风加快蒸发，汤就凉了。",
    r"  \item 溶解与结晶同样取决于离开和回到晶体的比率。",
    r"  \item 温度升高时离开与回来的比率都增加，净方向难以预言。",
    r"\end{itemize}",
    r"\end{summarybox}",
)

SUMMARY_S4 = newblock(
    r"\begin{summarybox}[§1-4 小结]",
    r"\begin{itemize}",
    r"  \item 原子伙伴重排即化学反应，物理与化学过程没有明显界限。",
    r"  \item 碳与氧结合放热发光，就是燃烧与火焰的来历。",
    r"  \item 化学式是分子排列的二维画像，复杂分子需要三维描述。",
    r"  \item 原子假说的证据：布朗运动、X 射线晶体分析、预言处处相符。",
    r"\end{itemize}",
    r"\end{summarybox}",
)

CONCEPTMAP = newblock(
    r"\begin{conceptmap}[示意：从水滴到原子核的“尺度阶梯”]",
    r"\centering",
    r"\begin{tikzpicture}[font=\footnotesize]",
    r"  % (1) 水滴：肉眼可见的宏观尺度",
    r"  \fill[blue!10] (0,1.0) circle (0.9);",
    r"  \draw[blue!60!black,thick] (0,1.0) circle (0.9);",
    r"  \node at (0,1.0) {水滴};",
    r"  % 放大",
    r"  \draw[->,thick] (1.05,1.0) -- (2.35,1.0);",
    r"  \node[above] at (1.70,1.18) {放大};",
    r"  % (2) 原子：一滴水里挤满的粒子",
    r"  \fill[red!12] (3.40,1.0) circle (0.45);",
    r"  \draw[red!60!black,thick] (3.40,1.0) circle (0.45);",
    r"  \node at (3.40,1.0) {原子};",
    r"  % 再放大",
    r"  \draw[->,thick] (3.95,1.0) -- (5.25,1.0);",
    r"  \node[above] at (4.60,1.18) {再放大};",
    r"  % (3) 原子核：藏在原子中央的更小尺度",
    r"  \fill[red!70!black] (6.90,1.0) circle (0.16);",
    r"  \draw[red!70!black] (6.90,1.0) circle (0.16);",
    r"  \node[right=0.15cm] at (7.06,1.0) {原子核};",
    r"  % 三格标题",
    r"  \node[align=center,text width=3.2cm] at (0,-0.25)",
    r"      {\textbf{(1) 水滴}\\直径约 1/4 英寸};",
    r"  \node[align=center,text width=3.0cm] at (3.40,-0.25)",
    r"      {\textbf{(2) 原子}\\半径约 $1\sim2$\,\r{A}};",
    r"  \node[align=center,text width=3.4cm] at (6.90,-0.25)",
    r"      {\textbf{(3) 原子核}\\直径约 $10^{-13}$ 厘米\\（位于原子中央）};",
    r"\end{tikzpicture}",
    r"",
    r"\figsource{按 §1-2 正文的原子尺度数据绘制，非原书插图；原子核尺度取通行数量级}",
    r"\end{conceptmap}",
)

FIG1_CAPTION = (
    "    \\caption{放大10亿倍的水%\n"
    + newblock(r"\fighint{黑点氧、白点氢，每两个氢连一个氧；画面是二维理想化的}")
    + "\n}"
)
FIG7_CAPTION = (
    "    \\caption{食盐的晶体结构%\n"
    + newblock(r"\fighint{大球为氯离子、小球为钠离子；两套格点交错，没有独立的“食盐分子”}")
    + "\n}"
)


# ---------------------------------------------------------------- 逐行改造
def t_L9(text: str) -> str:
    """列表化：两个理由（第一/第二）。"""
    p1, rest = cut_before(text, " 第一，")
    item1, rest = cut_before(rest.lstrip(), " 第二，")
    item2, p2 = cut_before(rest.lstrip(), "因此，即使为了知道")
    return "\n".join(
        [
            p1,
            "",
            listify(
                "enumerate",
                [
                    "\\item[第一，]" + rep(item1, "第一，", ""),
                    "\\item[第二，]" + rep(item2, "第二，", ""),
                ],
            ),
            "",
            p2,
        ]
    )


def t_L11(text: str) -> str:
    """关键句：一切知识都只是近似。"""
    return rep(
        text,
        "实际上，人们知道的每件事都只是某种近似",
        "\\keyidea{实际上，人们知道的每件事都只是某种近似}",
    )


def t_L13(text: str) -> str:
    text = rep(text, "：实验是", "：\\term{实验}是")
    p1, p2 = cut_before(text, "但是，要从这些线索中作出重大的判断")
    return p1 + "\n\n" + p2


def t_L15(text: str) -> str:
    p1, p2, p3 = cut_before(
        text,
        "例如，一个物体的质量似乎是从来不变的",
        "因此，人们可能认为新的定律实际上并没有什么有意义的差别。",
    )
    return p1 + "\n\n" + p2 + "\n\n" + p3


def t_L19(text: str) -> str:
    """列表化：先教哪条定律的两个备选问句。"""
    p1, rest = cut_before(text, "是否应先教那些")
    item1, rest = cut_before(rest, "还是应先教简单的")
    item2, p2 = cut_before(rest, "前一条定律比较引人入胜")
    return "\n".join(
        [
            p1,
            "",
            listify("itemize", ["\\item " + item1, "\\item " + item2]),
            "",
            p2,
        ]
    )


def t_L27(text: str) -> str:
    return rep(
        text,
        "所有的物体都是用原子构成的——这些原子是一些小小的粒子，它们一直不停地运动着。",
        "\\keyidea{所有的物体都是用原子构成的——这些原子是一些小小的粒子，它们一直不停地运动着。}",
    )


def t_L35(text: str) -> str:
    p1, p2 = cut_before(text, "当然这是生物学的课题，但是现在我们继续观察下去")
    return p1 + "\n\n" + p2


def t_L37(text: str) -> str:
    """列表化：水面图象的两处理想化（首先/其次）。"""
    p1, rest = cut_before(text, "首先，各种粒子用简单的方式画成有明显的边缘")
    item1, rest = cut_before(rest, "其次，为了简便起见")
    item2, rest = cut_before(rest, "注意在图中有两类")
    p2, p3 = cut_before(rest, "另一件不能在图上说明的事实是")
    p2 = rep(p2, "小组称为一个分子", "小组称为一个\\term{分子}")
    return "\n".join(
        [
            p1,
            "",
            listify("itemize", ["\\item " + item1, "\\item " + item2]),
            "",
            p2,
            "",
            p3,
        ]
    )


def t_L47(text: str) -> str:
    text = rep(text, "这种跳动就是我们所说的热运动", "这种跳动就是我们所说的\\term{热运动}")
    p1, p2 = cut_before(text, "图\\ref{figure:水蒸气}是一幅水蒸气的图象。")
    return p1 + "\n\n" + p2


def t_L55(text: str) -> str:
    text = rep(text, "（实际上，是压强乘以面积）", "（实际上，是\\term{压强}乘以面积）")
    p1, rest = cut_before(text, "图\\ref{figure:一个配有活塞的汽缸}是一个盛气体的标准容器")
    p2, p3 = cut_before(rest, "由于有这么多的气体分子一直在撞击顶端的活塞")
    return p1 + "\n\n" + p2 + "\n\n" + p3


def t_L69(text: str) -> str:
    text = rep(
        text,
        "\\footnote{铅、锑、锡的合金，也称为活字合金。}",
        "\\aside{铅、锑、锡的合金，也称为活字合金。}",
    )
    parts = cut_before(
        text,
        "有趣的一点是，",
        "固体与液体的差别就在于",
        "图\\ref{figure:冰}是一种虚构的冰的排列状况",
        "在这里列出的冰的晶体图样中有许多",
    )
    return "\n\n".join(parts)


def t_L71(text: str) -> str:
    p1, p2 = cut_before(text, "原子所具有的这种最低的振动不足以使物质熔解")
    return p1 + "\n\n" + p2


def t_L81(text: str) -> str:
    """列表化：水面上"发现的东西"（首先/此外）+ 分段。"""
    text = rep(text, "存在着一种平衡", "存在着一种\\term{平衡}")
    text = rep(text, "少量的二氧化碳", "少量的\\term{二氧化碳}")
    p1, rest = cut_before(text, "设想水的表面上是空气")
    p2, rest = cut_before(rest, "首先，水面上有水的分子")
    item1, rest = cut_before(rest, "此外，我们还发现一些别的分子")
    item2, rest = cut_before(rest, "空气几乎完全是由")
    p3, rest = cut_before(rest, "那么在这种情况下会发生什么事呢")
    p4, p5 = cut_before(rest, "结果，我们看到那个看来死气沉沉的")
    return "\n".join(
        [
            p1,
            "",
            p2,
            "",
            listify("itemize", ["\\item " + item1, "\\item " + item2]),
            "",
            p3,
            "",
            p4,
            "",
            p5,
        ]
    )


def t_L83(text: str) -> str:
    return rep(
        text,
        "因为有多少分子离开水面就会有多少分子回到水面！",
        "\\keyidea{因为有多少分子离开水面就会有多少分子回到水面！}",
    )


def t_L85(text: str) -> str:
    p1, p2 = cut_before(text, "当然，当一个水蒸气分子从空气中跑向水面时")
    return p1 + "\n\n" + p2


def t_L97(text: str) -> str:
    text = rep(text, "离子就是带有额外电子的原子", "离子就是带有额外\\term{电子}的原子")
    text = rep(
        text,
        "所谓平衡我们指的是这种情况，即原子离开晶体的比率正好与回到晶体的比率相同。",
        "\\keyidea{所谓平衡我们指的是这种情况，即原子离开晶体的比率正好与回到晶体的比率相同。}",
    )
    parts = cut_before(
        text,
        "在图\\ref{figure:盐在水中的溶解}中有一个氯离子松开来了",
        "我们能不能从这幅图画中看出盐究竟是",
    )
    return "\n\n".join(parts)


def t_L118(text: str) -> str:
    p1, p2 = cut_before(text, "图\\ref{figure:碳在氧气中的燃烧}表示碳在氧气中的燃烧。")
    return p1 + "\n\n" + p2


def t_L120(text: str) -> str:
    text = rep(text, "这就是所谓的一氧化碳气体分子", "这就是所谓的\\term{一氧化碳}气体分子")
    text = rep(text, "的能量——动能", "的能量——\\term{动能}")
    p1, p2 = cut_before(text, "但是碳吸引氧的能力比氧吸引氧或者碳吸引碳的能力更大。")
    return p1 + "\n\n" + p2


def t_L132(text: str) -> str:
    text = rep(
        text,
        "所以一个化学式只是这样的分子的一个画象。",
        "\\keyidea{所以一个化学式只是这样的分子的一个画象。}",
    )
    parts = cut_before(
        text,
        "图\\ref{figure:空气中的紫罗兰香气分子}是空气中紫罗兰香气图。",
        "六个碳原子组成了一个环",
    )
    return "\n\n".join(parts)


def t_L134(text: str) -> str:
    text = rep(text, "——有机化学。", "——\\term{有机化学}。")
    p1, p2 = cut_before(text, "大约在20年前就能在某些情况下用物理方法来研究")
    return p1 + "\n\n" + p2


def t_L138(text: str) -> str:
    """离题旁白（化学命名）标 optional；环境起止行放进 NEW 块。"""
    return newblock(r"\begin{optional}") + "\n" + text + "\n" + newblock(r"\end{optional}")


def t_L148(text: str) -> str:
    p1, p2 = cut_before(text, "由于原子是如此之小，你用光学显微镜观察不到它")
    return p1 + "\n\n" + p2


def t_L154(text: str) -> str:
    p1, p2 = cut_before(text, "当我们说，我们是一堆原子")
    return p1 + "\n\n" + p2


TRANSFORMS = {
    9: t_L9,
    11: t_L11,
    13: t_L13,
    15: t_L15,
    19: t_L19,
    27: t_L27,
    35: t_L35,
    37: t_L37,
    47: t_L47,
    55: t_L55,
    69: t_L69,
    71: t_L71,
    81: t_L81,
    83: t_L83,
    85: t_L85,
    97: t_L97,
    118: t_L118,
    120: t_L120,
    132: t_L132,
    134: t_L134,
    138: t_L138,
    148: t_L148,
    154: t_L154,
}

CAPTION_FIXES = {32: FIG1_CAPTION, 102: FIG7_CAPTION}
BEFORE = {}  # 行号 -> 在该行前插入的 NEW 块
AFTER = {
    1: ["", CHAPTER_INTRO, "", READING_PATH],
    23: ["", SUMMARY_S1],
    47: ["", CONCEPTMAP],
    71: ["", SUMMARY_S2],
    108: ["", SUMMARY_S3],
    154: ["", SUMMARY_S4],
}
BEFORE = dict(RUNIN)


def main() -> int:
    raw = subprocess.run(
        ["git", "show", "main:" + SRC_REL], cwd=REPO, capture_output=True, check=True
    ).stdout.decode("utf-8")
    lines = raw.split("\n")
    # 末尾换行处理：split 后最后一个元素是 ""
    assert lines[-1] == ""

    out_lines: list[str] = []
    for idx, line in enumerate(lines[:-1], start=1):
        if idx in BEFORE:
            out_lines.append(BEFORE[idx])

        if idx in TRANSFORMS:
            frag = TRANSFORMS[idx](line)
            # 逐字符内容校验：改造片段剔除 NEW 后必须与原行一致
            a, b = vc.content_chars(line), vc.content_chars(frag)
            assert a == b, (
                f"L{idx} 内容校验失败\n原: {a}\n新: {b}\n首个差异: "
                f"{next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), 'len')}"
            )
            out_lines.append(frag)
        elif idx in CAPTION_FIXES:
            frag = CAPTION_FIXES[idx]
            a, b = vc.content_chars(line), vc.content_chars(frag)
            assert a == b, f"L{idx} 图注内容校验失败"
            out_lines.append(frag)
        else:
            out_lines.append(line)

        if idx in AFTER:
            out_lines.extend(AFTER[idx])

    text = "\n".join(out_lines) + "\n"

    # ---- 全局校验 1：全文零删改 ----
    new_blocks = re.findall(r"%<<<NEW(.*?)%>>>NEW", text, flags=re.S)
    new_text = "\n".join(new_blocks)
    cjk = lambda s: len(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]", s))
    orig_cjk = cjk(raw)
    body = re.sub(r"%<<<NEW.*?%>>>NEW", "\n", text, flags=re.S)
    assert vc.content_chars(raw) == vc.content_chars(text), "全文零删改校验失败"
    assert cjk(body) == orig_cjk, f"正文汉字数不符: {cjk(body)} vs {orig_cjk}"

    # ---- 全局校验 2：新增文字比例 ≤15% ----
    ratio = cjk(new_text) / orig_cjk
    assert ratio <= 0.15, f"新增文字超限: {ratio:.1%}"

    # ---- 校验 3：小结核查条目长度 ≤28 可见字符 ----
    for name, blk in (
        ("§1-1", SUMMARY_S1),
        ("§1-2", SUMMARY_S2),
        ("§1-3", SUMMARY_S3),
        ("§1-4", SUMMARY_S4),
    ):
        for item in re.findall(r"\\item\s+(.*)", blk):
            n = len(vc.content_chars(item))
            assert n <= 28, f"{name} 小结核查条目超 28 字（{n}）: {item}"

    # ---- 校验 4：配额 ----
    n_runin = len(re.findall(r"\\runin\{", new_text))
    n_term = len(re.findall(r"\\term\{", body))
    n_key = len(re.findall(r"\\keyidea\{", body))
    n_summary = len(re.findall(r"\\begin\{summarybox\}", new_text))
    n_fighint = len(re.findall(r"\\fighint\{", new_text))
    n_concept = len(re.findall(r"\\begin\{conceptmap\}", new_text))
    n_optional = len(re.findall(r"\\begin\{optional\}", new_text))
    assert 4 <= n_runin <= 8, n_runin
    assert 6 <= n_term <= 12, n_term
    assert 2 <= n_key <= 5, n_key
    assert n_summary == 4, n_summary
    assert 1 <= n_fighint <= 2, n_fighint
    assert n_concept == 1, n_concept
    assert n_optional <= 3, n_optional

    OUT.write_text(text, encoding="utf-8")
    print(f"已写入 {OUT.relative_to(REPO)}")
    print(
        f"原文汉字 {orig_cjk}；新增汉字 {cjk(new_text)}（{ratio:.1%}）；"
        f"runin={n_runin} term={n_term} keyidea={n_key} summarybox={n_summary} "
        f"fighint={n_fighint} conceptmap={n_concept} optional={n_optional}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
