#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 Chapters/VolumeI/Chapter2.tex 机械拼装 ch2-pilot-body.tex。

原则：只做“插入”（分段、列表环境、强调宏、导读/小结/图），
不改动、不删除、不移动任何原文文字。所有切分锚点都断言唯一命中。
生成后请运行 verify_nodel.py 做二次校验。
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SRC = REPO / "Chapters/VolumeI/Chapter2.tex"
OUT = HERE / "ch2-pilot-body.tex"

LINES = SRC.read_text(encoding="utf-8").splitlines()


def L(n):
    s = LINES[n - 1].strip()
    assert s, f"line {n} empty"
    return s


def sub(s, old, new):
    c = s.count(old)
    assert c == 1, f"NOT UNIQUE ({c}): {old[:40]!r}"
    return s.replace(old, new)


def subn(s, pairs):
    for old, new in pairs:
        s = sub(s, old, new)
    return s


def split_at(s, anchor):
    c = s.count(anchor)
    assert c == 1, f"SPLIT anchor not unique ({c}): {anchor[:40]!r}"
    i = s.index(anchor)
    return s[:i], s[i:]


def wrap_span(s, start, end, macro):
    """把从 start 到 end（end 为紧随其后锚点）之间的文字包进 \\macro{...}。"""
    prefix, rest = split_at(s, start)
    mid, tail = split_at(rest, end)
    return prefix, mid, tail


def keyidea_between(s, start, end):
    pre, mid, tail = wrap_span(s, start, end, "keyidea")
    return pre + "\\keyidea{" + mid + "}" + tail


def keyidea_tail(s, start):
    """把 start 起的整段尾部包进 \\keyidea{...}。"""
    pre, mid = split_at(s, start)
    return pre + "\\keyidea{" + mid + "}"


out = []


def add(*blocks):
    out.extend(blocks)


# ============================================================
# 章首：新增导读（新增文字，不计入原文序列）
# ============================================================
add(
    r"""% !TEX program = xelatex
% ============================================================
% 第 2 章《基本物理》§2-1、§2-3 内容层改造样张 —— 正文
%
% 约定：
%   * 原文一字未删：只插入分段、列表环境、\runin / \term / \keyidea /
%     \pullquote / \aside、导读、小结与示意图；
%   * 本文件中“新增文字”如下（零删除校验时整块剔除）：
%       \chapterintro、\readingpath、\runin、\enterm、\figsource，
%       summarybox / conceptmap / figure 环境，\label；
%   * 原文文字只换了呈现方式（\footnote -> \aside、段落切分），
%     校验脚本：python3 verify_nodel.py
% ============================================================

\chapter{基本物理}

\chapterintro{%
\textbf{一句话定位}：本章不推公式，只画一张“物理学的世界观地图”——物理学家在做什么、已经知道什么、还不知道什么。\par
\textbf{本章要点}：
\begin{itemize}
  \item 基本物理的目标，是把无穷多的现象归结为少量基本事物和相互作用。
  \item “理解”就像看懂一盘象棋：先学会规则，再谈走法；规则对不对，有三种检验办法。
  \item 物理学史是一连串“综合”：热与力学、电与磁与光、化学与原子行为。
  \item 1920 年后的两大变化：空－时取代绝对空间与时间，量子力学改写了小尺度上的规则。
  \item 量子力学的三大观念：测不准原理、不可精确预言、波粒二象性；量子电动力学把光与物质统一起来。
\end{itemize}
\textbf{与前后章的关系}：上承第 1 章“原子假说”的结论，下接第 3 章“物理学与其他科学的关系”；本章界定的“基本物理”是全书的纲领。\par
\textbf{本样张范围}：只改造 §2-1 与 §2-3 两节（§2-2 未收录），用来演示“导读—分段—列表—路标—图示—小结”的完整改造链条。
}

\readingpath{速读路径：§2-1 全节（本章纲领）→ §2-3 只看五个段内小标题与文末小结 → 回读加粗术语。精读路径：按正文顺序读，遇到“选读”标记的段落可先跳过，不影响主线；每节末尾的“小结”可当复查清单。}

% ============================================================
% §2-1 引言
% ============================================================
\section{引言}

\runin{本章要问什么} """
    + L(5)
)

# ---- L7：拆成两段（纷繁现象 / 好奇心） ----
p7a, p7b = split_at(L(7), "在自然界的其他场合")
add(r"\runin{从纷繁现象到基本事物} " + p7a)
add(p7b)

# ---- L9：六个追问列表化 ----
s9 = L(9)
lead9, rest9 = split_at(s9, "沙粒和岩石是两回事吗？")
q1, rest9 = split_at(rest9, "月亮是不是一块巨大的岩石呢？")
q2, rest9 = split_at(rest9, "风是否与海洋中的水流相似")
q3, rest9 = split_at(rest9, "不同的运动有什么共同特征？")
q4, rest9 = split_at(rest9, "不同的声音有什么相似之处？")
q5, rest9 = split_at(rest9, "究竟有多少种颜色？")
q6, tail9 = split_at(rest9, "等等，等等。")
# lead9 = "例如，"；q1..q6 为六个追问；tail9 = "等等，等等。我们就是试图……"
add(
    lead9,
    r"""\begin{itemize}
  \item """
    + q1
    + r"""
  \item """
    + q2
    + r"""
  \item """
    + q3
    + r"""
  \item """
    + q4
    + r"""
  \item """
    + q5
    + r"""
  \item """
    + q6
    + r"""
\end{itemize}""",
    tail9,
)

# ---- L11：科学方法 ----
s11 = subn(
    L(11),
    [
        (r"\uwave{观察}", r"\term{观察}"),
        (r"\uwave{推理}", r"\term{推理}"),
        (r"\uwave{实验}", r"\term{实验}"),
        (r"\uwave{科学方法}", r"\term{科学方法}"),
        ("称之为基本物理中的基本观点", r"称之为\term{基本物理}中的基本观点"),
    ],
)
add(s11)

# ---- L13：拆三段 + 象棋译者注改页边注 + 章末金句改引文块 ----
s13 = sub(
    L(13),
    "（这里指的是国际象棋——译者注）",
    r"\aside{（这里指的是国际象棋——译者注）}",
)
p13a, rest13 = split_at(s13, "如果你们会下棋")
p13b, rest13 = split_at(rest13, "实际上我们今天还没找到一切规则")
p13c, quote13 = split_at(rest13, "如果我们知道了规则，就认为")
add(r"\runin{“理解”就像看懂一盘棋} " + p13a)
add(p13b)
add(p13c)
add(r"\pullquote{" + quote13 + "}")

# ---- L15：三种检验办法 -> enumerate，第 1 项 ----
s15 = L(15)
intro15, rest15 = split_at(s15, "第一，")
label1, item1 = split_at(rest15, "可能有这种情况：")
add(r"\runin{检验规则的三种办法} " + intro15)
add(
    r"""\begin{enumerate}
  \item["""
    + label1
    + "]"
    + item1
)

# ---- L17：第 2 项；象被俘的括号改“选读”；“新场合”判断改关键句 ----
s17 = L(17)
assert s17.startswith("第二种")
rest17 = s17[len("第二种"):]
p17a, rest17 = split_at(rest17, "（显然，")
opt17, p17b = split_at(rest17, "这也就是物理学中出现的情况")
p17b = sub(p17b, r"\uwave{新的}场合", "新的场合")
p17b = keyidea_between(
    p17b,
    "从基本物理的观点来看",
    "这是我们发现新规则的一条途径。",
)
add("  \\item[第二种]" + p17a)
# 括注直接解释“黑方块里的象”，属正文必要信息，不作 optional（optional 只留给真正的离题旁白）
add(opt17)
add(p17b)

# ---- L19：第 3 项；Alekhine 脚注改页边注 ----
s19 = sub(
    L(19),
    r"\footnote{世界著名弈棋手，系国际象棋大师。曾多次获得国际象棋世界冠军。——译者注}",
    r"\aside{世界著名弈棋手，系国际象棋大师。曾多次获得国际象棋世界冠军。——译者注}",
)
rest19 = s19[len("第三个"):]
add("  \\item[第三个]" + rest19)
add(r"\end{enumerate}")

# ---- §2-1 象棋三法示意图（紧跟“三种办法”，便于对照） ----
add(
    r"""
\begin{conceptmap}[示意：检验规则的三种办法]
\centering
\begin{tikzpicture}[font=\small,>=stealth,
  piece/.style={circle,draw,inner sep=1pt,font=\scriptsize},
  panelcap/.style={align=center,text width=3.6cm,font=\footnotesize,text=black!80}]
% ① 棋盘角落：棋子少，能精确预测
\begin{scope}
  \draw[step=.55,gray!55,thin] (0,0) grid (2.2,2.2);
  \node[piece,fill=black!75,text=white] at (.275,.275) {兵};
  \node[piece,fill=black!75,text=white] at (1.925,1.925) {王};
  \node[piece,fill=white] at (.275,1.925) {车};
  \node[panelcap,below=3mm] at (1.1,0) {(1) 角落里棋子少\\可以精确预测};
\end{scope}
% ② 象只走对角线：永远落在同色格
\begin{scope}[shift={(4.4,0)}]
  \foreach \x in {0,...,3} \foreach \y in {0,...,3} {
    \pgfmathparse{mod(\x+\y,2)==0 ? 1 : 0}
    \ifnum\pgfmathresult=1
      \fill[red!18] (\x*.55,\y*.55) rectangle ++(.55,.55);
    \fi
  }
  \draw[step=.55,gray!55,thin] (0,0) grid (2.2,2.2);
  \draw[-{Stealth[length=2mm]},thick,red!65!black,dashed]
      (.275,.275) -- (1.375,1.375) -- (1.925,1.925);
  \node[piece,fill=black!75,text=white] at (.275,.275) {象};
  \node[piece,fill=white] at (1.925,1.925) {象};
  \node[panelcap,below=3mm] at (1.1,0) {(2) 只走对角线\\永远落在同色格};
\end{scope}
% ③ 以车护王：粗略近似，把握意图
\begin{scope}[shift={(8.8,0)}]
  \draw[step=.55,gray!55,thin] (0,0) grid (2.2,2.2);
  \node[piece,fill=black!75,text=white] (k) at (1.1,1.1) {王};
  \node[piece,fill=white] (r1) at (.275,.275) {车};
  \node[piece,fill=white] (r2) at (1.925,1.925) {车};
  \draw[-{Stealth[length=2mm]},thick,red!65!black] (r1) to[out=40,in=220] (k);
  \draw[-{Stealth[length=2mm]},thick,red!65!black] (r2) to[out=220,in=40] (k);
  \node[panelcap,below=3mm] at (1.1,0) {(3) 以车护王\\粗略近似也管用};
\end{scope}
\end{tikzpicture}

\figsource{按 §2-1“三种检验办法”的文字描述绘制，非原书插图}
\end{conceptmap}
"""
)

# ---- L21：分类与综合；“两个问题”改关键句 ----
s21 = subn(
    L(21),
    [
        (r"\uwave{发现隐匿在实验后的定律}", "发现隐匿在实验后的定律"),
        (r"\uwave{把各类现象综合起来}", "把各类现象综合起来"),
    ],
)
s21 = keyidea_between(
    s21,
    "这就是今天基础理论物理面临的问题：",
    "在历史上，人们总能做到这一点",
)
add(r"\runin{分类、综合与拼图} " + s21)

# ---- L23：三次大综合 -> itemize（原文序数词作加粗引导语，避免超长列表标签） ----
s23 = L(23)
intro23, rest23 = split_at(s23, "首先，")
body_a, rest23 = split_at(rest23, "另一个巨大的综合，")
body_b, rest23 = split_at(rest23, "还有一个综合，")
body_c = rest23
lab_a, body_a = "首先，", body_a[len("首先，"):]
lab_b, body_b = "另一个巨大的综合，", body_b[len("另一个巨大的综合，"):]
lab_c, body_c = "还有一个综合，", body_c[len("还有一个综合，"):]
body_b = sub(body_b, r"\uwave{电磁场}", r"\term{电磁场}")
body_c = sub(body_c, r"\uwave{量子化学}", r"\term{量子化学}")
add(
    intro23,
    r"""\begin{itemize}
  \item \textbf{"""
    + lab_a
    + "}"
    + body_a
    + r"""
  \item \textbf{"""
    + lab_b
    + "}"
    + body_b
    + r"""
  \item \textbf{"""
    + lab_c
    + "}"
    + body_c
    + r"""
\end{itemize}""",
)

# ---- L25：世界由什么构成；末两句改关键句 ----
s25 = subn(
    L(25),
    [
        (r"\uwave{事物是用什么构成的}", "事物是用什么构成的"),
        (r"\uwave{总共存在多少基本元素}", "总共存在多少基本元素"),
    ],
)
pre25, ks25 = split_at(s25, "简言之，")
add(r"\runin{世界由什么构成} " + pre25 + r"\keyidea{" + ks25 + "}")

# ---- §2-1 小结 ----
add(
    r"""
\begin{summarybox}[§2-1 小结]
\begin{itemize}
  \item 基本物理要做的事：把无穷多的现象归结为少量基本事物与相互作用。
  \item “理解”的比喻：看懂一盘象棋——先找到规则，再解释具体走法。
  \item 规则对不对，有三种检验：简单系统可精确预测、由规则推出更一般的法则、用粗略近似把握意图。
  \item 已知规则最有趣之处，是它在“新场合”失效的地方——那是发现新规则的入口。
  \item 物理学史是一连串综合：热与力学、电与磁与光（电磁场）、化学与原子行为（量子化学）；本章最终追问：事物由什么构成、有多少基本元素。
\end{itemize}
\end{summarybox}
"""
)

# ============================================================
# §2-3 量子物理学
# ============================================================
add(r"""% ============================================================
% §2-3 量子物理学
% ============================================================
\section{量子物理学}""")

# ---- L72：拆两段；术语 量子力学、空－时 ----
s72 = subn(
    L(72),
    [
        ("发展起来的量子力学解释", r"发展起来的\term{量子力学}解释"),
        ("并称之为空－时", r"并称之为\term{空－时}"),
    ],
)
p72a, p72b = split_at(s72, "以后，人们又发现有关原子运动的规则也是有问题的")
add(r"\runin{经典物理的两道裂缝} " + p72a)
add(p72b)

# ---- L74：拆四段；测不准原理 ----
s74 = subn(
    L(74),
    [
        ("而测不准原理则要求", r"而\term{测不准原理}则要求"),
    ],
)
s74 = keyidea_between(
    s74,
    "动量的不确定性与位置的不确定性是并协的",
    "我们可以把这条定律写成",
)
p74a, rest74 = split_at(s74, "这条定则解释了这样一个十分神秘的佯谬")
p74b, rest74 = split_at(rest74, "起先曾认为原子核很大")
p74c, rest74 = split_at(rest74, "如果电子在原子核里出现")
p74d, p74e = split_at(rest74, "（记得我们曾经说过")
add(r"\runin{测不准原理} " + p74a)
add(p74b)
add(p74c)
add(p74d)
add(p74e)

# ---- L76：拆五段 + 选读（哲学家/斯德哥尔摩离题段） + 实验试金石引文 ----
s76 = subn(
    L(76),
    [
        ("可以利用探测光子的方法", r"可以利用探测\term{光子}的方法"),
        (
            "按照我们今天的理解，大自然的表现是这样的：根本不可能精确地预言在一定的实验中究竟会发生什么事情。",
            r"按照我们今天的理解，大自然的表现是这样的：\keyidea{根本不可能精确地预言在一定的实验中究竟会发生什么事情。}",
        ),
    ],
)
p76a, rest76 = split_at(s76, "这是一件糟透了的事")
p76b, rest76 = split_at(rest76, "顺便地说，")
opt76, rest76 = split_at(rest76, "科学的基本假设，它的基本哲学观念是什么呢？")
opt76a, opt76b = split_at(opt76, "对科学来说，这并不是必然的")
p76c, p76d = split_at(rest76, "假如结果是在基多所作的大多数实验")
p76c = sub(
    p76c,
    r"\uwave{实验是任何观念的正确性的唯一试金石}",
    "实验是任何观念的正确性的唯一试金石",
)
pre76c, quote76 = split_at(p76c, "我们在第一章里讲到过：")
add(r"\runin{不可精确预言} " + p76a)
add(p76b)
add(r"""\begin{optional}""" + opt76a)
add(opt76b + r"""\end{optional}""")
add(pre76c)
add(r"\pullquote{" + quote76 + "}")
add(p76d)

# ---- L78：拆两段；波粒二象性；“不存在区别”改关键句 ----
s78 = sub(
    L(78),
    "假定了量子力学的波粒二象性概念",
    r"假定了量子力学的\term{波粒二象性}概念",
)
p78a, p78b = split_at(s78, "这样，量子力学就将场的概念")
p78a = keyidea_tail(p78a, "实际上，每一种事物的行为都是一样的")
add(r"\runin{波粒二象性} " + p78a)
add(p78b)

# ---- L80：拆段 + 六个例证列表化；量子电动力学 ----
s80 = subn(
    L(80),
    [
        ("见解称为量子电动力学", r"见解称为\term{量子电动力学}"),
        (
            "这是光和物质，或电场与电荷之间的相互作用的基本理论，就物理学来说它是我们最伟大的成就。",
            r"\keyidea{这是光和物质，或电场与电荷之间的相互作用的基本理论，就物理学来说它是我们最伟大的成就。}",
        ),
    ],
)
p80a, rest80 = split_at(s80, "比如，从量子电动力学可以得出所有已知的电学、力学和化学定律：")
lead80, rest80 = split_at(rest80, "弹子碰撞的定律，")
it1, rest80 = split_at(rest80, "导线在磁场中运动的定律，")
it2, rest80 = split_at(rest80, "一氧化碳的比热，")
it3, rest80 = split_at(rest80, "霓虹灯的色彩，")
it4, rest80 = split_at(rest80, "盐的密度，")
it5, rest80 = split_at(rest80, "以及氢气与氧形成水的反应等，")
it6, rest80 = split_at(rest80, "全部都是这一理论的推论。")
close80, p80b = split_at(rest80, "所有这些细节")
add(r"\runin{量子电动力学} " + p80a)
add(lead80.rstrip())
add(
    r"""\begin{itemize}
  \item """
    + it1
    + r"""
  \item """
    + it2
    + r"""
  \item """
    + it3
    + r"""
  \item """
    + it4
    + r"""
  \item """
    + it5
    + r"""
  \item """
    + it6.rstrip()
    + r"""
\end{itemize}"""
)
add(close80)
add(p80b)

# ---- L82：拆两段；反粒子、正电子 ----
s82 = subn(
    L(82),
    [
        ("称为正电子的粒子", r"称为\term{正电子}的粒子"),
        ("总有一个反粒子", r"总有一个\term{反粒子}"),
    ],
)
p82a, p82b = split_at(s82, "电子的反粒子有另一个名称")
add(r"\runin{成就与边界} " + p82a)
add(p82b)

# ---- §2-3 三大观念关系图 + 小结 ----
add(
    r"""\begin{conceptmap}[示意：量子力学的三大观念]
\centering
\begin{tikzpicture}[font=\small,>=stealth,
  box/.style={draw,rounded corners=2pt,align=center,text width=3.15cm,
              inner sep=3pt,font=\footnotesize,fill=white},
  arr/.style={->,thick,gray!65}]
\node[box] (q) at (0,3.2) {\textbf{量子力学}\\(1920 年后)};
\node[box] (a) at (-4.3,1.2) {\textbf{1. 测不准原理}\\位置与动量不可同时确定};
\node[box] (b) at (0,1.2)   {\textbf{2. 不可精确预言}\\只能给出统计平均};
\node[box] (c) at (4.3,1.2) {\textbf{3. 波粒二象性}\\波与粒子没有区别};
\node[box,draw=blue!55] (d) at (0,-1.5) {\textbf{量子电动力学}\\统一光、电与物质};
\draw[arr] (q.south) -- (a.north);
\draw[arr] (q.south) -- (b.north);
\draw[arr] (q.south) -- (c.north);
\draw[arr] (a.south) to[out=-70,in=180] (d.west);
\draw[arr] (b.south) -- (d.north);
\draw[arr] (c.south) to[out=-110,in=0] (d.east);
\end{tikzpicture}

\figsource{按 §2-3 正文归纳绘制，非原书插图}
\end{conceptmap}

\begin{summarybox}[§2-3 小结]
\begin{itemize}
  \item 舞台变了：相对论把空间与时间合成空－时；小尺度上牛顿定律失效，日常直觉不再可靠。
  \item 测不准原理：位置与动量不能同时确定；它解释了原子为何“庞大”、电子为何不落入原子核。
  \item 量子力学放弃“精确预言”，只给统计平均；但科学没有崩溃——检验观念的标准仍然是实验。
  \item 波粒二象性：波与粒子不是两种东西；量子力学把场的波与粒子统一起来。
  \item 量子电动力学的成功与边界：它统一了光、电与物质，但电子质量与电荷仍是输入数据，核内规律尚不清楚。
\end{itemize}
\end{summarybox}"""
)

OUT.write_text("\n\n".join(out) + "\n", encoding="utf-8")
print("已写出：%s" % OUT)
print("文件大小：%d 字符" % len(OUT.read_text(encoding="utf-8")))
