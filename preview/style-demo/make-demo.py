#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 preview/style-demo/style-demo-body.tex
从仓库 Chapters/VolumeI/Chapter{2,7,13}.tex 原样抽取代表性片段，
仅在「不改原文」的前提下插入 readability.sty 的新宏（插入内容在
原版式编译时由 style-demo.tex 里的降级宏丢弃）。
"""
import io
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CH = os.path.join(ROOT, 'Chapters', 'VolumeI')
OUT = os.path.join(os.path.dirname(__file__), 'style-demo-body.tex')


def read_lines(name):
    with io.open(os.path.join(CH, name), encoding='utf-8') as f:
        return f.read().split('\n')


def extract(name, first, last):
    """取 1-based 闭区间 [first, last] 行。"""
    lines = read_lines(name)
    chunk = '\n'.join(lines[first - 1:last]).strip('\n')
    return chunk


def must_replace(text, old, new, tag):
    if old not in text:
        sys.exit('[FAIL] 锚点未找到（%s）：%r' % (tag, old[:40]))
    return text.replace(old, new, 1)


# ---------------------------------------------------------------- 第二章
ch2 = extract('Chapter2.tex', 1, 19)

ch2 = must_replace(
    ch2, r'\chapter{基本物理}',
    r'''\chapter{基本物理}

\chapterintro{本章回答一个朴素的问题：\keyidea{物理学的“基本”到底指什么}？费曼用“看人下棋”的比喻说明：基本物理就是这盘宇宙大棋的规则。阅读时请抓住三件事：一、三种检验规则的思路；二、物理规律是逐层近似的；三、每次“综合”都带来新的问题。}
\readingpath{先读 \S 2.1 前四段建立直觉，再重点看“三种检验方法”，最后用页末小结回顾。}''',
    'ch2-chapter')

ch2 = must_replace(ch2, '有关物理学的最基本概念', '有关物理学的最\\term{基本概念}', 'ch2-term')

ch2 = must_replace(
    ch2, '好奇心驱使我们提出问题，把事物联系起来，而将它们的种种表现理解为：',
    r'\keyidea{好奇心驱使我们提出问题，把事物联系起来，而将它们的种种表现理解为：}',
    'ch2-keyidea')

ch2 = must_replace(
    ch2, '或许是由较少量的基本事物和相互作用以无穷多的方式组合后所产生的结果。',
    r'''或许是由较少量的基本事物和相互作用以无穷多的方式组合后所产生的结果。\aside{费曼在这里给本科生一个“世界观”：复杂现象可能由少量基本事物组合而成。}''',
    'ch2-aside')

ch2 = must_replace(
    ch2, '如果我们不能很好的分析这盘象棋游戏',
    r'\runin{三种检验方法}如果我们不能很好的分析这盘象棋游戏',
    'ch2-runin')

ch2 = ch2 + r'''

\begin{summarybox}[本节要点]
  \begin{itemize}
    \item 基本物理研究的是“规则”：用少量基本事物与相互作用解释纷繁现象。
    \item 检验规则有三条路：预测简单情形；用推论检验规则本身；用粗糙近似作判断。
    \item 已知规则只是近似，新场合（尤其规则失效处）才是发现新规则的地方。
  \end{itemize}
\end{summarybox}'''

# ---------------------------------------------------------------- 第七章
ch7 = extract('Chapter7.tex', 1, 46)

ch7 = must_replace(
    ch7, r'\chapter{万有引力理论}',
    r'''\chapter{万有引力理论}

\chapterintro{引力是第一个被“统一”的力：一条 $F=Gmm'/r^2$ 就能同时解释落体、月球、行星与潮汐。本章跟着费曼走一遍“观测数据 $\to$ 定律 $\to$ 动力学解释”的推理链。}''',
    'ch7-chapter')

ch7 = must_replace(
    ch7, r'\section{行星运动}',
    r'''\section{行星运动}
\readingpath{重点看开普勒三定律如何从第谷的观测数据中被“读”出来，以及牛顿如何用动力学解释它们。}''',
    'ch7-readingpath')

ch7 = must_replace(ch7, '那么什么是引力定律呢', r'那么什么是\term{引力定律}呢', 'ch7-term')

ch7 = must_replace(
    ch7, '如果要想发现什么东西，那么去细致地做一些实验要比展开冗长的哲学争辩好得多。',
    r'\keyidea{如果要想发现什么东西，那么去细致地做一些实验要比展开冗长的哲学争辩好得多。}',
    'ch7-keyidea')

ch7 = must_replace(
    ch7, '开普勒发现了涉及行星运动的一些非常优美、卓越而又简单的定律。',
    r'''开普勒发现了涉及行星运动的一些非常优美、卓越而又简单的定律。\aside{第谷的观测精度是开普勒定律的前提：没有好数据，就没有好定律。}''',
    'ch7-aside')

ch7 = must_replace(ch7, r'\caption{椭圆}', r'\caption{椭圆\figsource{《费曼物理学讲义》第一卷 §7-2}}', 'ch7-fig1')
ch7 = must_replace(ch7, r'\caption{开普勒的面积定律}',
                   r'\caption{开普勒的面积定律\figsource{《费曼物理学讲义》第一卷 §7-2}}', 'ch7-fig2')

ch7 = must_replace(
    ch7, '开普勒第三定律发现得较晚',
    r'\runin{开普勒第三定律}开普勒第三定律发现得较晚',
    'ch7-runin')

ch7 = ch7 + r'''

\begin{summarybox}[本节要点]
  \begin{itemize}
    \item 开普勒三定律把“行星怎么动”总结成三条精确而简单的规律。
    \item 牛顿用“力指向太阳 + 反平方”解释了面积定律与第三定律。
    \item 引力定律的普适性来自“天上的力”与“地上的力”被认定为同一种力。
  \end{itemize}
\end{summarybox}'''

# ---------------------------------------------------------------- 第十三章
ch13 = extract('Chapter13.tex', 1, 60)

ch13 = must_replace(
    ch13, r'\chapter{功与势能（上）}',
    r'''\chapter{功与势能（上）}

\chapterintro{本章用最朴素的例子把“动能 + 势能 = 恒量”推出来：先看自由落体，再推广到沿曲线运动、再到三维。公式不多，关键是理解每一步“求导—代牛顿定律—识别全导数”的结构。}''',
    'ch13-chapter')

ch13 = must_replace(
    ch13, r'\section{落体的能量}',
    r'''\section{落体的能量}
\readingpath{先看 $T+U=$ 恒量的结论，再跟上两条求导推导；看不懂推导时，先记住“动能变化率 = 力 × 速度”这个核心。}''',
    'ch13-readingpath')

ch13 = must_replace(
    ch13, '由于下落运动而具有动能$T$（或K.E.）',
    r'由于下落运动而具有\term{动能}$T$（\enterm{kinetic energy}，或K.E.）',
    'ch13-term')

ch13 = must_replace(
    ch13, '这两种能量的总和是恒量',
    r'\keyidea{这两种能量的总和是恒量}',
    'ch13-keyidea')

ch13 = must_replace(
    ch13, r'\caption{物体在重力作用下在一无摩擦的曲线上的运动}',
    r'\caption{物体在重力作用下在一无摩擦的曲线上的运动\figsource{《费曼物理学讲义》第一卷 §13-1}}',
    'ch13-fig')

ch13 = ch13 + r'''

\begin{summarybox}[本节要点]
  \begin{itemize}
    \item 能量守恒最简单的形式：$T+U=\text{恒量}$。
    \item 证明路径：对 $T$ 求时间导数，代入 $F=ma$，认出结果恰是 $-U$ 的导数。
    \item 该结论可推广到沿任意曲线运动，只要力是保守力。
  \end{itemize}
\end{summarybox}'''

# ---------------------------------------------------------------- 输出
body = r'''%% =====================================================================
%%  style-demo-body.tex —— 自动生成，请勿手改
%%  生成命令：cd preview/style-demo && python3 make-demo.py
%%  来源：Chapters/VolumeI/Chapter{2,7,13}.tex 原样片段（未删改原文）
%%  说明：readability.sty 的新宏是“插入式”标记；原版式编译时由
%%        style-demo.tex 中的降级宏丢弃/还原，正文文字不做任何删减。
%% =====================================================================

%% ===== 第二章：密集纯文字（§2.1 引言）=====
\setcounter{chapter}{1}
''' + ch2 + r'''

\clearpage

%% ===== 第七章：图表密集（§7.1--§7.3）=====
\setcounter{chapter}{6}
''' + ch7 + r'''

\clearpage

%% ===== 第十三章：公式密集（§13.1 落体的能量）=====
\setcounter{chapter}{12}
''' + ch13 + '\n'

with io.open(OUT, 'w', encoding='utf-8') as f:
    f.write(body)
print('written:', OUT, '(%d bytes)' % len(body.encode('utf-8')))
