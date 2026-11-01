#!/usr/bin/env bash
# 构建「阅读效率版」全书（新版式 + 已改造章节）
#
# 说明：
#  - 仓库里的 Chapters/ 会先同步到 _attachments/build-feynman/reading-efficiency/ 再编译，
#    避免 latexmk 在仓库目录产生 .aux/.toc 等中间文件；
#  - _attachments/ 是本地忽略目录（见 .git/info/exclude），不随 git 提交；
#  - Figures/ 与 Cover.pdf 用软链接。
#
# 用法：在仓库根目录执行
#   bash tools/build_reading_efficiency_book.sh
# 产物：
#   _attachments/build-feynman/reading-efficiency/Feynman Lectures on Physics.pdf
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$REPO/_attachments/build-feynman/reading-efficiency"
MAIN="Feynman Lectures on Physics.tex"

mkdir -p "$BUILD"
cd "$BUILD"

# 1) 同步源文件（章节目录整体替换，确保与仓库一致）
cp "$REPO/$MAIN" "$BUILD/"
cp "$REPO/styles/readability.sty" "$BUILD/"
rm -rf "$BUILD/Chapters"
cp -R "$REPO/Chapters" "$BUILD/Chapters"
[ -e "$BUILD/Figures" ] || ln -sfn "$REPO/Figures" "$BUILD/Figures"
[ -e "$BUILD/Cover.pdf" ] || ln -sfn "$REPO/Cover.pdf" "$BUILD/Cover.pdf"

# 2) 编译（latexmk 自动处理多遍）
latexmk -xelatex -interaction=nonstopmode -file-line-error "$MAIN"

# 3) 报告
PDF="$BUILD/Feynman Lectures on Physics.pdf"
echo
echo "输出: $PDF"
pdfinfo "$PDF" | grep -E 'Pages|Page size'
echo "error:    $(grep -c '^!' "$BUILD/Feynman Lectures on Physics.log" || true)"
echo "Overfull: $(grep -c 'Overfull' "$BUILD/Feynman Lectures on Physics.log" || true)"
echo "Underfull:$(grep -c 'Underfull' "$BUILD/Feynman Lectures on Physics.log" || true)"
