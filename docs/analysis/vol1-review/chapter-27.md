# 第 27 章《几何光学》审查报告

## 范围与材料

- 正文：`Chapters/VolumeI/Chapter27.tex`（239 行；7 节 27-1～27-7，正文 35 段）
- 英文：`_attachments/build-feynman/audit/en/I_27.txt`（27–1～27–7，正文 L36–L200；抓取文本中公式为 [math]/分式碎片）
- 旁证：`_attachments/reference/zh/Chapter27.txt`（公开中译本 OCR，本身有错）；`_attachments/reference/candidates/ch27-candidates.md`（266 小块 + 21 大块，已逐类核对）
- 辅助核对：公开中译本（新千年版第 1 卷）印刷页 OCR/图像（archive.org PDF，第 290–298 页），用于逐式核对公式版式与图注（官方网页本次抓取受限，未用）
- 公式核对方式：eFLP 文本片段 + 中译本印刷页逐式比对

## 结果

- **已修正 5 条（6 处；中 2、低 3）**；**存疑 7 项**（未改）。
- 单章编译：**11 页 A4，0 error / 0 overfull / 0 underfull / 0 Missing character / 0 undefined references**（连编 2 遍）。
- 修改文件：`Chapters/VolumeI/Chapter27.tex`（5 行，**CRLF 换行保持原状**）、`preview/chapter-27/check.tex`（仅注释：章名改《几何光学》、`cd` 路径改 chapter-27）、本报告。未 commit，未动其他章。

## 中等问题（已修）

| # | 行号 | 问题 | 英文依据 | 修正 |
|---|---|---|---|---|
| 1 | L226 | 两处"**径向放大率**"为非标准术语（英文指放大多少倍直径） | "a lens that magnifies more than 2000 diameters … a system of lenses that magnifies 10,000 diameters" | "放大倍数大于$2~000$倍"/"放大倍数为$10~000$倍" |
| 2 | L239 | "透镜的**张角**为$\theta$"与紧随的公式 $\lambda/(2n\sin\theta)$ 矛盾（θ 应为半角） | "if the opening half-angle of the lens is called θ" | "透镜的**半张角**为$\theta$" |

## 低严重度修正（已修）

- L52："由公式可见，当**$s$一个**增加时，另一个则减少" → "当**其中一个**增加时"（底本印刷即"当 s 一个增加时"，不成句；英文 "as one s increases, the other decreases"）。
- L87："从密介质朝疏介质看**其中一个点**时" → "看**一个点**时"（英文 "see a point in the rare medium"；"其中"无着落）。
- L153："即**s**趋于无穷远" → "即**$s$**趋于无穷远"（数学体缺失；中译本印刷为斜体 s）。

## 存疑项（未改）

1. **L5"类似器件的微小误差"** ← "the small errors in lenses and similar details"：details（细节）译作"器件"，语义偏移；底本同，未改（建议"类似细节"）。
2. **L123"将在有限的生命中给我们节省许多精力"** ← "in the few times in our lives that we might have to chase the light through five surfaces"：漏"一生中难得几次"之意；底本同，仅标注。
3. **L155"购到"**：宜作"买到/购得"；底本同。
4. **图 27-1 图注为空**（`\caption{}`）：经核对，英文 eFLP 图题亦只有 "Figure 27–1"（无说明文字），中译本印刷页图注亦仅"图 27-1"，故**保留空图注**，输出"图 27.1"正确。
5. **公式 $\lambda/(2n\sin\theta)$**：中译本印刷作 $\lambda/(n\sin\theta)$（缺 2）；本仓库作 $\lambda/(2n\sin\theta)$，**与英文一致，不改**（已见中译本 p298 印刷）。
6. **段落切分**：中文 35 段；3 处相邻英文段在中文 .tex 中合并（L16–21 把"这就是讨论曲面成像时所需要的全部几何学！"并入前段；L38–48 把"如果我们有一点$O$…"并入前段；L52–66 把"从以上两式…""这种形式…"并入前段）。内容无缺，属显示公式前后缺分段（疑为转录/排版），未改；若需严格对齐可补空行（会引起版面变化）。
7. **"W.R.Hamilton"**：中译本印刷作"W. R. Hamilton"（空格差异）；低，未改。

## 覆盖性结论

- **段落/完整性**：7 节与英文 27–1～27–7 对应；逐句核对无漏句、无漏段、无重复粘贴；候选"大块差异"21 条全部是公式被剥离/图注错位噪声，读来无缺失；段落合并见存疑 6。
- **公式**：编号公式 27.1–27.17 全部存在；编译 `.aux` 核对标签渲染号 27.1–27.17 全对；逐式与英文片段/中译本印刷页核对——27.1（$\Delta\approx h^2/2s$）、27.2、27.3（单球面折射公式）、27.4、27.5、27.6、27.7–27.11（两表面/薄透镜焦距）、27.12（$1/s+1/s'=1/f$）、27.13–27.16（放大率公式与 $xx'=f^2$）、27.17（$t_2-t_1>1/\nu$）**均正确**；无公式内容错误（仅存疑 5 的底本印刷差异，本仓库版本正确）。
- **数字/量纲**：75 个表面、5 个表面、2 000 倍、10 000 倍、3/4、2f 等均与英文/中译本一致；无数字错误。
- **人名/术语**：哈密顿（W. R. Hamilton）、斯涅尔（Snell）；几何光学、折射率、焦距、物距/像距、曲率半径、主平面、球面像差、色差、分辨本领、半张角（已修）等与英文一致。
- **图/表**：9 幅图（27.1–27.9）齐全，图注与英文一致；图 27-1 无说明文字（保留空注，见存疑 4）；正文图引用全部经 `\ref` 解析（0 未定义），无硬编码图号；本章无表格。
- **自动候选差异**：266 小块 + 21 大块绝大多数为公式剥离噪声与参考文本 OCR 讹字（若→车、句→名、妥→受、疏→芍、凹→加、聚→察/诊、况→祝、另→男、距→中、斑→班、假→候、凭→赁 等），**不据以改动**；确属本仓库的问题即上表/低严重度 5 条。
- **附注**：`_attachments` 下 4 个 `Chapter27.tex` 副本与工作区正文一致（修改前），所修问题位于底本转录层，只需改 `Chapters/VolumeI/Chapter27.tex` 一处。

## 验证

- 入口：`preview/chapter-27/check.tex`（`\setcounter{chapter}{26}`、`\input{../../Chapters/VolumeI/Chapter27.tex}`；本次仅修正注释）。
- 命令：`cd preview/chapter-27 && rm -rf build && mkdir build && xelatex -no-mktex=tfm -interaction=nonstopmode -output-directory=build check.tex`（连编 2 遍）。
- 结果：11 页 A4；`error=0 / overfull=0 / underfull=0 / Missing character=0 / undefined references=0`。
- PDF 文本抽查：修正点均生效（"当其中一个增加时""看一个点时""即 s 趋于无穷远""放大倍数大于 2 000 倍""半张角为 θ"）；旧串（"径向放大率""当 s 一个增加""看其中一个点"）出现 0 次。
