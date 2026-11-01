#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""从 git main 的 Chapter26 原文机械生成「阅读效率改造版」。

原则（对照 docs/试点三章改造规范.md）：
  * 只做「插入」：插空行（切段）、插 NEW 块（导读/小结/小标题/图注提示/新增图）、
    用 \term/\keyidea 包裹原有文字、把 \footnote 原位换成 \aside、把原文句子放进列表环境；
  * 原文任何字符都不删、不改、不调序；
  * 生成后必须过 tools/verify_chapter.py 26（逐字符比对）与 tools/chapter_stats.py 26。

用法：python3 preview/chapter-26/build_chapter.py
输出：Chapters/VolumeI/Chapter26.tex（保留原文 CRLF 行尾）
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
REL = "Chapters/VolumeI/Chapter26.tex"

# ---------------------------------------------------------------- 原文
raw = subprocess.run(
    ["git", "show", f"main:{REL}"], cwd=REPO, capture_output=True, check=True
).stdout.decode("utf-8")
assert "\r\n" in raw, "原文应为 CRLF 行尾"
orig = raw.replace("\r\n", "\n")
lines = orig.split("\n")
assert len(lines) == 258, f"意外行数 {len(lines)}"
assert lines[0] == r"\chapter{光学：最短时间原理}", repr(lines[0])
assert lines[16] == r"\section{反射与折射}", repr(lines[16])
assert lines[83] == r"\section{费马最短时间原理}", repr(lines[83])
assert lines[138] == r"\section{费马原理的应用}", repr(lines[138])
assert lines[230] == r"\section{费马原理的更精确表述}", repr(lines[230])
assert lines[245] == r"\section{最短时间原理是怎样起作用的}", repr(lines[245])
assert lines[257].endswith("最短时间原理之间的关系。"), repr(lines[257][-30:])


def cut_before(text: str, anchors: list[str]) -> list[str]:
    """在若干唯一锚点前切分文本（不丢字符）。"""
    pieces: list[str] = []
    rest = text
    for a in anchors:
        assert rest.count(a) == 1, f"锚点不唯一或缺失: {a!r} in {rest[:80]!r}"
        i = rest.index(a)
        pieces.append(rest[:i])
        rest = rest[i:]
    pieces.append(rest)
    assert "".join(pieces) == text
    return pieces


# ---------------------------------------------------------------- NEW 文本
def new_block(*block_lines: str) -> list[str]:
    return ["%<<<NEW", *block_lines, "%>>>NEW"]


CHAPTERINTRO = [
    r"\chapterintro{%",
    r"\textbf{一句话定位}：本章只用一条原理——光走需时最少的路径——就把直线传播、镜面反射和折射串了起来，并顺势解释透镜与抛物面镜为什么长成那样。\par",
    r"\textbf{本章要点}：",
    r"\begin{itemize}",
    r"  \item 可见光只是电磁辐射谱系的一小段；不同波段要用不同的近似。",
    r"  \item 反射定律与斯涅耳折射定律，都能从费马原理推出来。",
    r"  \item 费马原理的准确表述不是“最短”，而是“邻近所有路径的时间几乎相同”。",
    r"  \item 透镜、椭球面镜、抛物面镜的共同点：让所有光路的传播时间相等。",
    r"  \item 用光子概率幅的叠加，可以看清光为什么“挑”费时最少的路径。",
    r"\end{itemize}",
    r"\textbf{与前后章的关系}：本章是光学几章的开篇，下接第 27 章《几何光学》；这里只讲几何光学的“一级近似”，更精确的波动处理留到第 28 章《电磁辐射》。}",
]

READINGPATH = [
    r"\readingpath{速读路径：§26.1 只记“三个大致的范围”→ §26.3 抓住费马原理的那句话 → §26.4 看落日、透镜、抛物面镜三个例子 → §26.5 读“正确的表述”。精读路径：按正文顺序读，§26.6 可放最后；每节末尾的小结和加粗术语可当复查清单。}",
]

SUMMARY_LIGHT = [
    r"\begin{summarybox}[§26.1 小结]",
    r"\begin{itemize}",
    r"  \item 光是电磁辐射谱系的一小段，各波段之间没有明确分界。",
    r"  \item 不同波段用不同近似：几何光学、波动光学、光子图像。",
    r"  \item 几何光学只是一级近似，本章只问“光在哪儿走”。",
    r"  \item “光进入眼睛”的种种理论，最后都要由事实来裁决。",
    r"\end{itemize}",
    r"\end{summarybox}",
]

SUMMARY_FERMAT = [
    r"\begin{summarybox}[§26.3 小结]",
    r"\begin{itemize}",
    r"  \item 费马原理：在一切可能路径中，光走需时最少的那条。",
    r"  \item 镜面反射可由它推出，结果就是入射角等于反射角。",
    r"  \item 折射时路径会“绕路”，但仍满足$\sin\theta_i=n\sin\theta_r$。",
    r"  \item 关键条件是速率：水中光速是空气中的$1/n$。",
    r"\end{itemize}",
    r"\end{summarybox}",
]

SUMMARY_APPLY = [
    r"\begin{summarybox}[§26.4 小结]",
    r"\begin{itemize}",
    r"  \item 倒易原理：光能沿一条路径走，就能沿它反向走。",
    r"  \item 玻璃板把光束平移；落日和海市蜃楼都是光走曲线。",
    r"  \item 透镜、椭球面镜、抛物面镜都在让所有光路等时。",
    r"  \item 费马原理能预言新关系：$n_{23}=n_{13}/n_{12}$，水中光速更慢。",
    r"\end{itemize}",
    r"\end{summarybox}",
]

SUMMARY_EXACT = [
    r"\begin{summarybox}[§26.5 小结]",
    r"\begin{itemize}",
    r"  \item 准确的表述：光所走的路径，其邻近路径所花时间几乎相同。",
    r"  \item 镜面反射对应时间的极小值，并不是极大值。",
    r"  \item 光用波“试探”邻近路径，试探的范围由波长决定。",
    r"  \item 缝窄到没有邻近路径可核对时，光反而像沿直线走。",
    r"\end{itemize}",
    r"\end{summarybox}",
]

CONCEPTMAP = [
    r"\begin{conceptmap}[示意：三种情形里的“最短时间”]",
    r"\centering",
    r"\begin{tikzpicture}[font=\small,",
    r"  panelcap/.style={align=center,text width=4.1cm,font=\footnotesize},",
    r"  ray/.style={thick},",
    r"  aux/.style={dashed,gray!80}]",
    r"% (1) 直线传播：两点之间直线最短",
    r"\begin{scope}",
    r"  \coordinate (A) at (0.25,0.9);",
    r"  \coordinate (B) at (2.35,0.9);",
    r"  \draw[ray] (A) -- (B);",
    r"  \fill (A) circle (1.2pt) node[above,font=\scriptsize] {$A$};",
    r"  \fill (B) circle (1.2pt) node[above,font=\scriptsize] {$B$};",
    r"  \node[panelcap,anchor=north] at (1.3,-1.75) {(1) 直线传播\\两点之间，直线最短};",
    r"\end{scope}",
    r"% (2) 镜面反射：入射角等于反射角",
    r"\begin{scope}[xshift=4.3cm]",
    r"  \draw[gray!65] (0,0) -- (2.6,0) node[right,black,font=\scriptsize] {$MM'$};",
    r"  \coordinate (A) at (0.3,1.2);",
    r"  \coordinate (B) at (2.3,1.2);",
    r"  \coordinate (C) at (1.15,0);",
    r"  \coordinate (Bp) at (2.3,-1.2);",
    r"  \draw[ray] (A) -- (C) -- (B);",
    r"  \draw[aux] (B) -- (Bp);",
    r"  \draw[aux] (C) -- (Bp);",
    r"  \fill (A) circle (1.2pt) node[above,font=\scriptsize] {$A$};",
    r"  \fill (B) circle (1.2pt) node[above,font=\scriptsize] {$B$};",
    r"  \fill (C) circle (1.2pt) node[below left,font=\scriptsize] {$C$};",
    r"  \fill (Bp) circle (1.2pt) node[below,font=\scriptsize] {$B'$};",
    r"  \node[panelcap,anchor=north] at (1.3,-1.75) {(2) 镜面反射\\$C$ 处入射角＝反射角};",
    r"\end{scope}",
    r"% (3) 折射：慢介质中走短程",
    r"\begin{scope}[xshift=8.6cm]",
    r"  \draw[gray!65] (0,0) -- (2.6,0) node[right,black,font=\scriptsize] {分界面};",
    r"  \coordinate (A) at (0.3,1.2);",
    r"  \coordinate (B) at (2.1,-1.2);",
    r"  \coordinate (C) at (1.45,0);",
    r"  \draw[ray] (A) -- (C) -- (B);",
    r"  \draw[aux] (C) -- (1.45,1.1);",
    r"  \draw[aux] (C) -- (1.45,-1.1);",
    r"  \fill (A) circle (1.2pt) node[above,font=\scriptsize] {$A$};",
    r"  \fill (B) circle (1.2pt) node[below,font=\scriptsize] {$B$};",
    r"  \fill (C) circle (1.2pt) node[above right,font=\scriptsize] {$C$};",
    r"  \node[panelcap,anchor=north] at (1.3,-1.75) {(3) 折射\\慢介质中走短程};",
    r"\end{scope}",
    r"\end{tikzpicture}",
    r"",
    r"\figsource{按§26.3—§26.4 的推导归纳绘制，非原书插图}",
    r"\end{conceptmap}",
]

FIG_HINT_MIRROR = r"\fighint{$B'$是$B$在镜后的镜像，$A\to C\to B'$是一条直线；$C$就是使总时间最短的入射点}"
FIG_HINT_CURVE = r"\fighint{横轴是光在镜面上的落点，纵轴是总时间；曲线底部附近很平坦，对应“相邻路径需时几乎相同”}"


def runin(title: str) -> list[str]:
    return new_block(r"\runin{%s}" % title)


# ---------------------------------------------------------------- 逐行操作
# PRE：在该行之前插入的源行（含 NEW 块）
PRE: dict[int, list[str]] = {
    2: new_block(*CHAPTERINTRO) + new_block(*READINGPATH),
    5: runin("从无线电波到γ射线"),
    9: runin("三种近似办法"),
    17: new_block(*SUMMARY_LIGHT) + [""],
    19: runin("从定性到定量"),
    88: runin("费马的想法"),
    91: [""],  # 把「回答是从 A 笔直走到 B 的那条！」切成新段
    139: new_block(*CONCEPTMAP) + [""] + new_block(*SUMMARY_FERMAT) + [""],
    162: runin("落日与海市蜃楼"),
    181: runin("会聚透镜"),
    231: new_block(*SUMMARY_APPLY) + [""],
    233: runin("正确的表述"),
    246: new_block(*SUMMARY_EXACT) + [""],
    248: runin("概率幅的图像"),
}

# WRAPS：行号 -> [(原文片段, 替换为)]；只包裹原有文字，不增删字符
WRAPS: dict[int, list[tuple[str, str]]] = {
    5: [(r"“波长”", r"“\term{波长}”")],
    9: [
        (r"叫做几何光学的方法", r"叫做\term{几何光学}的方法"),
        (r"其光子的能量", r"其\term{光子}的能量"),
    ],
    19: [(r"所谓的反射定律就是", r"所谓的\term{反射定律}就是")],
    66: [(r"称为斯涅耳定律", r"称为\term{斯涅耳定律}")],
    88: [
        (r"或费马原理", r"或\term{费马原理}"),
        (
            r"在从一点行进到另一点的所有可能的路径中，光走的是需时最短的路径。",
            r"\keyidea{在从一点行进到另一点的所有可能的路径中，光走的是需时最短的路径。}",
        ),
    ],
    99: [
        (
            r"因此，入射角等于反射角的这种说法与光射向镜面沿着需时最短的路径返回到$B$的说法是等效的。",
            r"\keyidea{因此，入射角等于反射角的这种说法与光射向镜面沿着需时最短的路径返回到$B$的说法是等效的。}",
        )
    ],
    141: [(r"首先是倒易原理", r"首先是\term{倒易原理}")],
    162: [
        (r"所谓的“焦点”", r"所谓的“\term{焦点}”"),
        (
            r"所以造成一个聚焦系统的问题，仅仅在于设计一个器件，使得光沿着所有不同路径走时所花的时间相等。",
            r"\keyidea{所以造成一个聚焦系统的问题，仅仅在于设计一个器件，使得光沿着所有不同路径走时所花的时间相等。}",
        ),
    ],
    181: [(r"我们称这种器件为会聚透镜", r"我们称这种器件为\term{会聚透镜}")],
    200: [(r"椭圆就是具有这样一种性质的曲线", r"\term{椭圆}就是具有这样一种性质的曲线")],
    217: [(r"的折射率$n$", r"的\term{折射率}$n$")],
    227: [(r"\footnote{", r"\aside{")],
    233: [
        (
            r"光取的是这样一条路径，在它邻近有许多取时几乎与它完全相同的其他路径。",
            r"\keyidea{光取的是这样一条路径，在它邻近有许多取时几乎与它完全相同的其他路径。}",
        )
    ],
    248: [
        (
            r"光子到达的机会与从始端到末端的总矢量的长度平方成正比",
            r"\keyidea{光子到达的机会与从始端到末端的总矢量的长度平方成正比}",
        )
    ],
}

# SPLITS：行号 -> 锚点列表（在锚点前插入空行 = 切段）
SPLITS: dict[int, list[str]] = {
    5: ["工程技术上所能得到的无线电波", "在一个波长范围与另一个波长范围之间"],
    15: [
        "另外一些观察到的重要事实是",
        "这曾经是惠更斯一度用来反对微粒说的一个最有力的证据。",
    ],
    19: ["对于前人来说，他们所面临的问题就是其中两个角之间有什么关系？"],
    25: [
        "现在的问题是，一个角与另一个角的关系如何？",
        "然而，这正是人们在全部希腊物理学中可以发现的用表列出实验结果的少数场合之一。",
    ],
    61: ["上面的数值表是公元140年作的"],
    99: ["换句话说，我们必须找出这个点", "这一命题最初由亚历山大的希罗（Hero）所述"],
    101: ["眼睛当然只觉察到实际射进它的光", "所以，认为有物体位于镜子后面的这种错觉"],
    105: [
        "那么我们怎么办？",
        "不论如何，我们来证明问题的最终解答是路径$ACB$",
        "所以，我们寻找这条规律的方法",
        "当距离$XC$很短时",
    ],
    162: [
        "这个现象的另一个例子是当人们在炎热的道路上驾车时",
        "其实我们真正见到的乃是从路上“反射”上来的天上的光",
        "作为最短时间原理的另一个重要例子",
        "但是，我们如何设法使光不仅能沿直线行进到达",
    ],
    181: ["同样地，如果我们取一条稍为倾斜的光线"],
    209: ["于是所有光线必须在相等的时间内从这里射到镜面"],
    213: ["有人会回答", "显然，最短时间的说法"],
    222: ["换句话说，我们可以预言一对新的介质的折射率"],
    227: ["只用斯涅耳定律"],
    233: ["假如我们有如图", "正确的表述如下："],
    235: ["但最短时间原理却是关于自然界行为方式的完全另一种哲学原理。"],
    242: [
        "回答是：是的，在某种程度上，它的确是这样做的。",
        "但对于无线电波，例如3厘米波，进行核对的距离就比较长了。",
    ],
    244: ["理由是手指靠得很近", "所有这些将在适当的时候加以解释"],
    258: ["设$C$点对应于时间的极小值", "几乎所有对于概率的积累都发生在"],
}

# 原文段落包 optional（原文文字，不加 NEW 标记）：
#   all        = 整段都是离题旁白
#   skip_first = 首段是过渡句保留，其余标选读
OPTIONAL_RANGES: dict[int, str] = {
    101: "all",
    213: "skip_first",
}


def apply_wraps(n: int, text: str) -> str:
    for old, new in WRAPS.get(n, []):
        assert text.count(old) == 1, f"L{n} 包裹锚点不唯一: {old!r}"
        text = text.replace(old, new)
    return text


def listify_9(text: str) -> list[str]:
    p = cut_before(
        text,
        ["其中的一个区域", "另一区域是", "下一个，如果我们考察很短的波长", "把整个事物统一于一个模型"],
    )
    return [
        p[0],
        "",
        "%<<<NEW", r"\begin{itemize}", "%>>>NEW",
        r"  \item " + p[1],
        "",
        r"  \item " + p[2],
        "",
        r"  \item " + p[3],
        "%<<<NEW", r"\end{itemize}", "%>>>NEW",
        "",
        p[4],
    ]


def listify_217(text: str) -> list[str]:
    p = cut_before(
        text,
        ["把空气（1）对水（2）的折射率叫做", "空气（1）对玻璃（3）的折射率叫做", "如果就水对玻璃的折射率"],
    )
    assert "但并无先验的理由" in p[3]
    i = p[3].index("但并无先验的理由")
    item3, tail = p[3][:i], p[3][i:]
    assert item3 and tail
    return [
        p[0],
        "",
        "%<<<NEW", r"\begin{itemize}", "%>>>NEW",
        r"  \item " + p[1],
        "",
        r"  \item " + p[2],
        "",
        r"  \item " + item3,
        "%<<<NEW", r"\end{itemize}", "%>>>NEW",
        "",
        tail,
    ]


def listify_248(text: str) -> list[str]:
    p = cut_before(
        text,
        [
            "取任一路径，并找出其相应的时间；",
            "然后写一复数或画一小的复矢量",
            "复矢量每秒的旋转周数就是光的频率。",
            "再取另一路径，比如说它具有不同的时间",
            "取所有可取的路径，并为每一条路径加上一个小矢量；",
            "那么答案就是，",
        ],
    )
    return [
        p[0],
        "",
        "%<<<NEW", r"\begin{enumerate}", "%>>>NEW",
        r"  \item " + p[1],
        "",
        r"  \item " + p[2] + p[3],
        "",
        r"  \item " + p[4],
        "",
        r"  \item " + p[5],
        "%<<<NEW", r"\end{enumerate}", "%>>>NEW",
        "",
        p[6],
    ]


def optional_wrap(n: int, text: str, mode: str) -> list[str]:
    paras = cut_before(text, SPLITS.pop(n))
    out: list[str] = []
    if mode == "skip_first":
        out += [paras[0], ""]
        paras = paras[1:]
    out += new_block(r"\begin{optional}")
    for i, p in enumerate(paras):
        if i:
            out.append("")
        out.append(p)
    out += new_block(r"\end{optional}")
    return out


def transform(n: int, text: str) -> list[str]:
    text = apply_wraps(n, text)
    if n == 9:
        return listify_9(text)
    if n == 217:
        return listify_217(text)
    if n == 248:
        return listify_248(text)
    if n in OPTIONAL_RANGES:
        return optional_wrap(n, text, OPTIONAL_RANGES[n])
    if n in SPLITS:
        return "\n\n".join(cut_before(text, SPLITS[n])).split("\n")
    return [text]


# ---------------------------------------------------------------- 组合
out: list[str] = []
for i, line in enumerate(lines, 1):
    if i in PRE:
        out.extend(PRE[i])
    out.extend(transform(i, line))

# 两处复杂图加读图提示（NEW 文字，嵌在图注内）
final: list[str] = []
for line in out:
    if line == r"    \caption{最短时间原理的说明}":
        final += [
            r"    \caption{最短时间原理的说明%<<<NEW",
            FIG_HINT_MIRROR + "%>>>NEW",
            "}",
        ]
    elif line == r"        \caption{C点相应于最短时间，但其附近各点相应于几乎与之相同的时间}":
        final += [
            r"        \caption{C点相应于最短时间，但其附近各点相应于几乎与之相同的时间%<<<NEW",
            FIG_HINT_CURVE + "%>>>NEW",
            "}",
        ]
    else:
        final.append(line)
out = final

assert out.count("%<<<NEW") == out.count("%>>>NEW"), "NEW 标记不成对"
new_src = "\r\n".join(out)
assert not new_src.endswith("\r\n")

# ---------------------------------------------------------------- 自检统计
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
STRUCT_ENVS = (
    "figure", "wrapfigure", "table", "longtable", "equation", "equation*", "align",
    "align*", "flalign", "gather", "multline", "eqnarray", "summarybox", "keybox",
    "conceptmap", "tikzpicture", "center",
)


def strip_new_blocks(t: str) -> str:
    return re.sub(r"%<<<NEW.*?%>>>NEW", "\n", t, flags=re.S)


def strip_comments(t: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in t.splitlines())


def drop_structured(t: str) -> str:
    for env in STRUCT_ENVS:
        pat = re.compile(r"\\begin\{%s\}.*?\\end\{%s\}" % (re.escape(env), re.escape(env)), re.S)
        while True:
            new = pat.sub("\n", t)
            if new == t:
                break
            t = new
    t = re.sub(r"\\\[.*?\\\]", "\n", t, flags=re.S)
    return re.sub(r"\\(?:begin|end)\{[^}]*\}", "", t)


body = drop_structured(strip_comments(strip_new_blocks(new_src)))
blocks: list[str] = []
cur: list[str] = []
for line in body.splitlines():
    if line.strip() == "":
        if cur:
            blocks.append("\n".join(cur))
            cur = []
    else:
        cur.append(line)
if cur:
    blocks.append("\n".join(cur))
lens = [len(CJK.findall(b)) for b in blocks if CJK.findall(b)]
over = [(n, blocks[i][:40].replace("\n", " ")) for i, n in enumerate(lens) if n > 250]
new_cjk = len(CJK.findall("\n".join(re.findall(r"%<<<NEW(.*?)%>>>NEW", new_src, flags=re.S))))
body_cjk = len(CJK.findall(strip_new_blocks(new_src)))
print(f"原文汉字 {len(CJK.findall(orig))}，改造后原文汉字 {body_cjk}，新增汉字 {new_cjk} "
      f"（{new_cjk / body_cjk:.1%}）")
print(f"正文块 {len(lens)}，平均 {sum(lens) / len(lens):.1f}，最长 {max(lens)}，>250 字 {len(over)} 块")
for n, s in over:
    print(f"  [>250] {n:>4}  {s}")
assert body_cjk == len(CJK.findall(orig)), "剔除 NEW 后汉字数不一致！"

target = REPO / REL
target.write_text(new_src, encoding="utf-8", newline="")
print(f"已写入 {target.relative_to(REPO)}（{len(out)} 行）")
