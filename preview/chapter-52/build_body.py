#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Chapter52《物理定律的对称性》阅读效率改造正文拼装脚本（零删改）。

用法
----
    cd Feynman-Lectures-Latex
    python3 preview/chapter-52/build_body.py            # 生成 Chapters/VolumeI/Chapter52.tex
    python3 preview/chapter-52/build_body.py --check    # 只检查，不写文件

原则
----
1. 原文从 git ref（默认 main）读取，一字不删、不改、不调序；所有改动都是「插入」；
2. 每个锚点必须唯一命中（断言），避免手抄原文时引入错字；
3. 新增文字/新增图表用 %<<<NEW / %>>>NEW 包住，tools/verify_chapter.py 会整块剔除；
4. 列表/可选读环境的环境名本身也在 NEW 块内（否则 \begin{itemize} 会贡献 "itemize"
   字样，破坏字符序列比对）；\item 命令不标记，便于 chapter_stats.py 统计列表项。

复现校验
--------
    python3 tools/verify_chapter.py 52          # 应 PASS
    python3 tools/chapter_stats.py 52           # 统计
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ORIG_REL = "Chapters/VolumeI/Chapter52.tex"
OUT = REPO / ORIG_REL

# =====================================================================
# 新增文字块（全部走 %<<<NEW / %>>>NEW）
# =====================================================================

INTRO = r"""%<<<NEW
\chapterintro{%
\textbf{一句话定位}：本章不推新公式，而是追问“物理定律本身有没有对称性”，以及对称性与守恒定律之间那条惊人的联系。\par
\textbf{本章要点}：
\begin{itemize}
  \item 外尔的定义：对一样东西做某种操作后，它看起来仍和先前一样，它就是对称的。
  \item 空间平移、时间平移、空间转动、匀速直线运动、全同粒子交换，都是使物理定律不变的对称操作。
  \item 但并非一切都对称：整体放大、匀速转动都会露出破绽，时间反演只在微观层面成立。
  \item 量子力学中，每一条对称性都对应一条守恒定律：平移对应动量，时间平移对应能量，转动对应角动量。
  \item 镜像反射（宇称）曾被当作定律，弱衰变实验却把它打破；把物质与反物质也互换，对称性才失而复得。
\end{itemize}
\textbf{与前后章的关系}：上承第 11 章矢量分析、第 16 章相对论、第 20 章转动；作为第一卷的末章，它把散见于各章的对称性讨论收拢为一条主线，也为粒子物理留下伏笔。\par
}
\readingpath{速读路径：§52.1 看外尔的定义与表 52.1；§52.2 看五类操作、反例与文末对照表；§52.7、§52.8 看小结与加粗术语。精读路径：按正文顺序读；§52.2 的火柴棒教堂、超级狗骨与傅科摆，§52.6、§52.7、§52.8 的 $\tau$ 与 $\theta$ 之谜、吴健雄实验，是本章故事性最强的段落。每节末尾的小结可当复查清单。}
%>>>NEW
"""

# —— §52.2 五类对称操作：列表化（两段列表，中间保留「地理差别」原段，语序不变） ——
LIST52_2_LEAD = r"""%<<<NEW
\runin{五类对称操作} 以下几类操作都使物理定律保持不变。
\begin{itemize}
%>>>NEW
\item[%<<<NEW
\textbf{空间平移}%>>>NEW
]
"""

LIST52_2_ITEM_TIME = r"""\item[%<<<NEW
\textbf{时间平移}%>>>NEW
]
"""

LIST52_2_OPT_OPEN = r"""%<<<NEW
\begin{optional}
%>>>NEW
"""

LIST52_2_OPT_CLOSE = r"""%<<<NEW
\end{optional}
\end{itemize}
%>>>NEW
"""

LIST52_2_SECOND_OPEN = r"""%<<<NEW
\begin{itemize}
%>>>NEW
\item[%<<<NEW
\textbf{空间转动}%>>>NEW
]
"""

LIST52_2_ITEM_UNIFORM = r"""\item[%<<<NEW
\textbf{匀速运动}%>>>NEW
]
"""

LIST52_2_ITEM_IDENTICAL = r"""\item[%<<<NEW
\textbf{全同粒子}%>>>NEW
]
"""

LIST52_2_CLOSE = r"""%<<<NEW
\end{itemize}
%>>>NEW
"""

# —— §52.2 新增对照表 + 节末小结 ——
TABLE_52_2 = r"""%<<<NEW
\begin{table}[H]
    \caption{对称操作、改变的变量、守恒量与反例对照（守恒量见 §52.3）}
    \label{Table:52:2}
    \centering
    \small
    \begin{tabularx}{0.96\textwidth}{|>{\raggedright\arraybackslash}p{2.6cm}|>{\centering\arraybackslash}X|>{\centering\arraybackslash}X|>{\raggedright\arraybackslash}X|}
        \hline
        \textbf{对称操作} & \textbf{改变的变量} & \textbf{守恒量} & \textbf{反例 / 说明} \\
        \hline
        空间平移 & 位置 & 动量 & 环境（如地磁场）要一起搬走 \\
        时间平移 & 时刻 & 能量 & 环境要随时间相应改变 \\
        空间转动 & 取向角 & 角动量 & 周围物体要一起转动 \\
        匀速直线运动 & 速度 & 能量-动量 & 周围物体要一起匀速前进 \\
        全同粒子交换 & 粒子身份 & — & 交换后无法区分 \\
        \hline
        尺度缩放 & 整体放大 $k$ 倍 & — & 不成立：钠光波长、火柴棒教堂、“超级狗骨” \\
        匀速转动 & 角速度 $\omega$ & — & 不成立：离心力、科里奥利力、傅科摆 \\
        时间反演 & $t\to -t$ & — & 微观可逆；宏观不可逆（鸡蛋落地） \\
        \hline
    \end{tabularx}
\end{table}
%>>>NEW
"""

SUMMARY_52_2 = r"""%<<<NEW
\begin{summarybox}[§52.2 小结]
\begin{itemize}
  \item 平移与转动、匀速直线运动、全同粒子交换：定律不变。
  \item 前提：环境（如地磁场）要随仪器一起变换。
  \item 反例：整体放大、匀速转动都会破坏对称。
  \item 时间反演：微观可逆，宏观不可逆。
\end{itemize}
\end{summarybox}
%>>>NEW
"""

# —— §52.3 三对「对称性—守恒量」列表化 ——
LIST52_3_OPEN = r"""%<<<NEW
\begin{itemize}
%>>>NEW
\item """

LIST52_3_CLOSE = r"""%<<<NEW
\end{itemize}
%>>>NEW
"""

# —— §52.4 小结 ——
SUMMARY_52_4 = r"""%<<<NEW
\begin{summarybox}[§52.4 小结]
\begin{itemize}
  \item 镜像钟是否走得一样，是物理问题而非哲学问题。
  \item 物理与化学测量分不出左右，生命却只取一种手性。
  \item 这种不对称源于偶然的历史事件，不表明定律不对称。
\end{itemize}
\end{summarybox}
%>>>NEW
"""

# —— §52.5 小结 ——
SUMMARY_52_5 = r"""%<<<NEW
\begin{summarybox}[§52.5 小结]
\begin{itemize}
  \item 极矢量：镜像后箭头反向，如位移。
  \item 轴矢量：镜像后方向不变，如角速度。
  \item 左右互换时，轴矢量变号，磁铁的南北极也要互换。
\end{itemize}
\end{summarybox}
%>>>NEW
"""

# —— §52.7 小结 ——
SUMMARY_52_7 = r"""%<<<NEW
\begin{summarybox}[§52.7 小结]
\begin{itemize}
  \item $\tau$ 与 $\theta$ 的质量、寿命、产额相同。
  \item 但宇称守恒不允许同一粒子有两种这样的衰变。
  \item 吴健雄实验：极化钴发射电子有方向偏好。
  \item 弱衰变中宇称不守恒；法则只给倾向，原因不明。
\end{itemize}
\end{summarybox}
%>>>NEW
"""

# —— §52.8 小结 ——
SUMMARY_52_8 = r"""%<<<NEW
\begin{summarybox}[§52.8 小结]
\begin{itemize}
  \item 反粒子：质量相同、电荷相反，相遇即湮没。
  \item 用反物质造钟，可检验正反物质是否等价。
  \item 结果是：右旋物质与左旋反物质行为相同。
  \item 左右对称性以物质与反物质互换的形式保留。
\end{itemize}
\end{summarybox}
%>>>NEW
"""

# —— 读图提示（2 处） ——
FIG_HINT_VECTOR = r"""%<<<NEW
\fighint{把左图的位移箭头与右图的角速度箭头对比：镜像后一个反向，一个不反向。}
%>>>NEW
"""

FIG_HINT_DECAY = r"""%<<<NEW
\fighint{数一数末态的 $\pi$ 介子：$\tau^+$ 是三个，$\theta^+$ 是两个——这正是下文的关键。}
%>>>NEW
"""

# =====================================================================
# 操作清单：每条都是「插入」，锚点必须唯一命中
#   before : 在锚点前插入 payload
#   after  : 在锚点后插入 payload（payload="\n\n" 即切段）
#   replace: 整段替换（仅用于 \term/\keyidea 包裹原文，文字不变）
# =====================================================================
OPS = [
    # ---------- 章首导读 ----------
    ("replace", "\\chapter{物理定律的对称性}\n\n\\section{对称操作}",
     "\\chapter{物理定律的对称性}\n\n" + INTRO + "\n\\section{对称操作}",
     "章首 chapterintro + readingpath"),

    # ---------- §52.1 对称操作 ----------
    ("replace", "物理定律的对称性。在矢量分析（第11章）",
     "物理定律的\\term{对称性}。在矢量分析（第11章）", "术语：对称性"),
    ("replace", "其要点为，如果有一样东西，我们可以对它做某种事情，在做完之后，这个东西看起来仍旧和先前一样，那它就是对称的。",
     "其要点为，\\keyidea{如果有一样东西，我们可以对它做某种事情，在做完之后，这个东西看起来仍旧和先前一样，那它就是对称的。}",
     "关键句：外尔的对称性定义"),

    # ---------- §52.2 空间与时间的对称性 ----------
    ("before", "我们尝试做的第一件事情，比方说，就是使现象在空间中平移。", LIST52_2_LEAD,
     "runin 五类对称操作 + 列表1 开始 + 空间平移项"),
    ("before", "在今天，我们也同样相信，时间的移动对物理定律也不会有影响", LIST52_2_ITEM_TIME,
     "列表项：时间平移"),
    ("replace", "环境中的有关特征也要及时作相应的变动。当然这个对称性意味着",
     "环境中的有关特征也要及时作相应的变动。\n" + LIST52_2_OPT_OPEN + "当然这个对称性意味着",
     "选读：通用汽车股票玩笑（optional 开始）"),
    ("replace", "所遇到的情况将完全一样！\n\n我们也必须注意到地理情况的差别",
     "所遇到的情况将完全一样！\n" + LIST52_2_OPT_CLOSE + "\n我们也必须注意到地理情况的差别",
     "optional 结束 + 列表1 结束"),
    ("before", "我们曾相当详细地讨论过的另一件事是在空间的转动", LIST52_2_SECOND_OPEN,
     "列表2 开始 + 空间转动项"),
    ("before", "在较高级的水平上，有另一种对称性——匀速直线运动的对称性。", LIST52_2_ITEM_UNIFORM,
     "列表项：匀速运动"),
    ("before", "上面所提的对称性都具有几何的性质", LIST52_2_ITEM_IDENTICAL,
     "列表项：全同粒子"),
    ("replace", "也是些全同粒子——所有电子都相同",
     "也是些\\term{全同粒子}——所有电子都相同", "术语：全同粒子"),
    ("after", "这些原子是全同的。", "\n\n", "切段：全同粒子定义 / 讨论"),
    ("replace", "所有正$\\pi$介子都相同，等等。\n\n在列举了这么多使现象不改变的操作后",
     "所有正$\\pi$介子都相同，等等。\n" + LIST52_2_CLOSE + "\n在列举了这么多使现象不改变的操作后",
     "列表2 结束"),
    ("after", "因为按比例放大的火柴棒根本不够牢固。", "\n\n", "切段：火柴棒教堂 例证/反问"),
    ("after", "这根骨骼按完全不同的比例画得又大又结实。", "\n\n", "切段：超级狗骨 / 伽利略"),
    ("before", "下面我们来叙述一个很有趣的对称性，即时间的可逆性。",
     "%<<<NEW\n\\runin{时间的可逆性}\n%>>>NEW\n", "runin 时间的可逆性"),
    ("after", "就将无法辨别变化是往正方向发展还是往逆方向发展。", "\n\n", "切段：时间反演 宏观/微观"),
    ("after", "有些地方搞错了！”", "\n\n", "切段：影片倒放 / 鸡蛋落地"),
    ("before", "\\section{对称性与守恒定律}", TABLE_52_2 + SUMMARY_52_2 + "\n",
     "新增对照表 + §52.2 小结"),

    # ---------- §52.3 对称性与守恒定律 ----------
    ("replace", "有这么一件事实：在量子力学中，对于每一个对称的规律都有一条守恒定律与之相对应。",
     "有这么一件事实：\\keyidea{在量子力学中，对于每一个对称的规律都有一条\\term{守恒定律}与之相对应。}",
     "术语：守恒定律 + 关键句"),
    ("before", "举例说，物理定律对空间平移是对称的。", LIST52_3_OPEN,
     "§52.3 列表化开始"),
    ("replace", "\n\n物理定律对时间平移是对称的。", "\n\\item 物理定律对时间平移是对称的。",
     "§52.3 列表项：时间平移"),
    ("replace", "\n\n关于空间转动一定角度后的不变性与角动量守恒定律相对应。这些关系是非常有趣和非常美妙的！",
     "\n\\item 关于空间转动一定角度后的不变性与角动量守恒定律相对应。\n" + LIST52_3_CLOSE + "\n这些关系是非常有趣和非常美妙的！",
     "§52.3 列表项：空间转动 + 列表结束"),

    # ---------- §52.4 镜面反射 ----------
    ("before", "其次一个问题是在空间反射下的对称性。",
     "%<<<NEW\n\\runin{钟与它的镜像}\n%>>>NEW\n", "runin 钟与它的镜像"),
    ("replace", "其次一个问题是在空间反射下的对称性。",
     "其次一个问题是在\\term{空间反射}下的对称性。", "术语：空间反射"),
    ("after", "问题并不是镜子里的钟像什么。", "\n\n", "切段：镜像钟 设定/制造"),
    ("after", "它们都是实际存在的、物质的钟。", "\n\n", "切段：制造镜像钟 / 提出问题"),
    ("after", "任何系统中的实际状况并不一定具有我们所谈到的对称性。", "\n\n",
     "切段：地理学定义左右 / 定律是否对称"),
    ("replace", "如果确是如此，那么就不可能用任何物理现象来区分“右”和“左”",
     "\\keyidea{如果确是如此，那么就不可能用任何物理现象来区分“右”和“左”}",
     "关键句：无法绝对定义右与左"),
    ("after", "于是偏振面就向右旋转。", "\n\n", "切段：糖水旋光 / 细菌实验"),
    ("after", "它称为丙氨酸。", "\n\n", "切段：丙氨酸模型 / 合成"),
    ("after", "所示的两种结构的分子！", "\n\n", "切段：两种结构 / L 与 D"),
    ("after", "得到的是两类分子的等量混合物。", "\n\n", "切段：合成等量 / 生物只取 L"),
    ("before", "人们推测其理由如下。",
     "%<<<NEW\n\\runin{生命为何偏爱一种手性}\n%>>>NEW\n", "runin 生命为何偏爱一种手性"),
    ("after", "只是现在我们所试的是“左脚”）。", "\n\n", "切段：酶的选择 / 左旋蛙"),
    ("after", "但从这以后倾向性本身就传播开来。", "\n\n", "切段：偶然起源 / 倾向传播"),
    ("before", "\\section{极矢量与轴矢量}", SUMMARY_52_4 + "\n", "§52.4 小结"),

    # ---------- §52.5 极矢量与轴矢量 ----------
    ("before", "现在我们进一步讨论下去。",
     "%<<<NEW\n\\runin{右手规则只是习惯}\n%>>>NEW\n", "runin 右手规则只是习惯"),
    ("after", "它只是一种巧妙的方法。", "\n\n", "切段：右手规则是习惯 / 量不是矢量"),
    ("replace", "这一种矢量我们称为极矢量。", "这一种矢量我们称为\\term{极矢量}。", "术语：极矢量"),
    ("replace", "这种矢量称为轴矢量。", "这种矢量称为\\term{轴矢量}。", "术语：轴矢量"),
    ("after", "不应出现任何差别。", "\n\n", "切段：方程设计原则 / 角动量与磁场例子"),
    ("after", "必须是轴矢量。", "\n\n", "切段：磁场例子 / 反射下的磁极互换"),
    ("before", "\\label{figure:转轮与其镜像。注意角速度“矢量”方向并没有反转}",
     "", "占位（无操作）"),
    ("replace", "\\label{figure:转轮与其镜像。注意角速度“矢量”方向并没有反转}\n",
     "\\label{figure:转轮与其镜像。注意角速度“矢量”方向并没有反转}\n" + FIG_HINT_VECTOR,
     "读图提示：极矢量与轴矢量"),
    ("before", "\\section{哪一只是右手}", SUMMARY_52_5 + "\n", "§52.5 小结"),

    # ---------- §52.6 哪一只是右手 ----------
    ("before", "现在要告诉他有关我们的所有事情。",
     "%<<<NEW\n\\runin{火星人对话}\n%>>>NEW\n", "runin 火星人对话"),
    ("after", "因而我们可以定义一个绝对长度。", "\n\n", "切段：定义长度 / 描述外形"),
    ("after", "火星人甚至还做了一个有关我们的外形的模型。", "\n\n", "切段：外形模型 / 心脏在哪边"),

    # ---------- §52.7 宇称不守恒 ----------
    ("before", "由于出现了这种明显的失败，李政道和杨振宁建议",
     "%<<<NEW\n\\runin{吴健雄实验}\n%>>>NEW\n", "runin 吴健雄实验"),
    ("replace", "存在着一种称为$\\beta$衰变或弱衰变的现象。",
     "存在着一种称为$\\beta$衰变或\\term{弱衰变}的现象。", "术语：弱衰变"),
    # 注意：wrapfigure 前必须已有足够正文（≥1 行），否则 wrapfig 会把孤行拉伸；
    # 故此段不切分，保持「我们知道……相关联，」+ 图 +「存在着……」
    ("after", "这个粒子一度称为$\\tau$介子。", "\n\n", "切段：τ 粒子 / θ 粒子"),
    ("after", "根据电荷守恒，其中一个必须是中性的。", "\n\n", "切段：τ 与 θ 的对比 / 产物比例"),
    ("replace", "这一类量子力学的守恒关系称作宇称守恒。",
     "这一类量子力学的守恒关系称作\\term{宇称守恒}。", "术语：宇称守恒"),
    ("replace", "从根本上说，在物理学的这一个阶梯上，反射对称定律是不正确的。",
     "\\keyidea{从根本上说，在物理学的这一个阶梯上，反射对称定律是不正确的。}",
     "关键句：反射对称定律不成立"),
    ("replace", "\\label{figure:粒子衰变的简图}\n",
     "\\label{figure:粒子衰变的简图}\n" + FIG_HINT_DECAY,
     "读图提示：τ 与 θ 衰变简图"),
    ("before", "\\section{反物质}", SUMMARY_52_7 + "\n", "§52.7 小结"),

    # ---------- §52.8 反物质 ----------
    ("replace", "这就是物质与反物质的关系", "这就是物质与\\term{反物质}的关系", "术语：反物质"),
    ("replace", "正电子称为电子的反粒子", "正电子称为电子的\\term{反粒子}", "术语：反粒子"),
    ("after", "它也必须受到质疑。", "\n\n", "切段：查对称性表 / 狄拉克预言"),
    ("after", "而这些就是粒子与它的反粒子的特征。", "\n\n", "切段：正电子性质 / 其余反粒子"),
    ("after", "质子和反质子碰在一起彼此就会湮没。", "\n\n", "切段：反质子 / 反中子"),
    ("after", "正负粒子的质量是一样的，每件事都一样。", "\n\n", "切段：反原子 / 用反物质造钟"),
    ("before", "这样就出现了一个问题。",
     "%<<<NEW\n\\runin{四个钟}\n%>>>NEW\n", "runin 四个钟"),
    ("after", "将不会走得一样快。", "\n\n", "切段：镜像钟计数 / 四个钟"),
    ("after", "人们曾认为它们会走得一样快。", "\n\n", "切段：四个钟假设 / 右旋反物质"),
    ("replace", "即右旋的物质与左旋的反物质是对称的。",
     "即\\keyidea{右旋的物质与左旋的反物质是对称的}。", "关键句：右旋物质与左旋反物质对称"),
    ("before", "\\section{对称破缺}", SUMMARY_52_8 + "\n", "§52.8 小结"),

    # ---------- §52.9 对称破缺 ----------
    ("after", "我们怎样来理解这一点？", "\n\n", "切段：近乎对称之问 / 核力例子"),
    ("after", "它就不再有对称性。", "\n\n", "切段：圆的完美 / 行星轨道"),
    ("after", "还有许多柱子以及刻有龙头及贵族雕像的圆柱，等等。", "\n\n",
     "切段：日光城门 / 故意刻反的传说"),
]

# 去掉占位项
OPS = [op for op in OPS if op[3] != "占位（无操作）"]


def load_original(ref: str) -> str:
    out = subprocess.run(
        ["git", "show", f"{ref}:{ORIG_REL}"], cwd=REPO, capture_output=True, check=True
    )
    return out.stdout.decode("utf-8")


def apply_ops(text: str) -> str:
    for i, (kind, anchor, payload, note) in enumerate(OPS, 1):
        n = text.count(anchor)
        if n != 1:
            raise SystemExit(
                f"[FAIL] 第 {i} 条操作锚点命中 {n} 次（应为 1）：{note}\n"
                f"       锚点：{anchor[:80]!r}"
            )
        if kind == "before":
            text = text.replace(anchor, payload + anchor, 1)
        elif kind == "after":
            text = text.replace(anchor, anchor + payload, 1)
        elif kind == "replace":
            text = text.replace(anchor, payload, 1)
        else:
            raise SystemExit(f"未知操作类型：{kind}")
    return text


CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
STRUCT_ENVS = ("figure", "wrapfigure", "table", "longtable", "equation", "equation*",
               "align", "align*", "flalign", "gather", "multline", "eqnarray",
               "summarybox", "keybox", "conceptmap", "tikzpicture", "center")


def strip_new_blocks(text: str) -> str:
    return re.sub(r"%<<<NEW.*?%>>>NEW", "\n", text, flags=re.S)


def strip_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in text.splitlines())


def drop_structured(text: str) -> str:
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


def report(text: str) -> None:
    new_blocks = re.findall(r"%<<<NEW(.*?)%>>>NEW", text, flags=re.S)
    new_text = "\n".join(new_blocks)
    body = strip_new_blocks(text)
    body_plain = drop_structured(strip_comments(body))
    blocks = [b for b in top_blocks(body_plain) if CJK_RE.search(b)]
    lens = [len(CJK_RE.findall(b)) for b in blocks]
    over = [(n, re.sub(r"\s+", "", b)[:26]) for n, b in zip(lens, blocks) if n > 250]
    print(f"NEW 块数：{len(new_blocks)}")
    print(f"原文汉字（body）：{len(CJK_RE.findall(body))}")
    print(f"新增汉字：{len(CJK_RE.findall(new_text))}"
          f"（占原文 {len(CJK_RE.findall(new_text)) / max(1, len(CJK_RE.findall(body))):.1%}）")
    print(f"正文段/内容单元：{len(blocks)}，最长 {max(lens)}，>250 字：{len(over)}")
    for n, head in over:
        print(f"  [>{250}] {n} 字：{head}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--orig-ref", default="main")
    ap.add_argument("--check", action="store_true", help="只检查，不写文件")
    args = ap.parse_args()

    orig = load_original(args.orig_ref)
    new = apply_ops(orig)
    if args.check:
        print("[check] 所有锚点唯一命中；未写文件。")
        report(new)
        return 0
    OUT.write_text(new, encoding="utf-8")
    print(f"已写入 {OUT.relative_to(REPO)}")
    report(new)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
