#!/usr/bin/env bash
# 编译「原版式 vs 新版式」前后对比样张（各两遍，产物在 build/）
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p build

echo "[1/4] 生成样张正文（从 Chapters/ 抽取）"
python3 make-demo.py

echo "[2/4] 编译新版式 PDF"
xelatex -interaction=nonstopmode -output-directory=build style-demo.tex
xelatex -interaction=nonstopmode -output-directory=build style-demo.tex

echo "[3/4] 编译原版式 PDF"
xelatex -interaction=nonstopmode -output-directory=build -jobname=style-demo-before \
        "\def\demomode{before}\input{style-demo.tex}"
xelatex -interaction=nonstopmode -output-directory=build -jobname=style-demo-before \
        "\def\demomode{before}\input{style-demo.tex}"

echo "[4/4] 完成："
echo "  新版式: preview/style-demo/build/style-demo.pdf"
echo "  原版式: preview/style-demo/build/style-demo-before.pdf"
echo "（对比 PNG 由 docs/figures/make-typography-figures.sh 生成）"
