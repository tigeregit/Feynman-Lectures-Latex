#!/usr/bin/env bash
# 生成 docs/figures/typography-*.png：原版式 vs 新版式同页对比截图
# 前置：已运行 preview/style-demo/build-demo.sh 得到两个 PDF
# 用法：bash docs/figures/make-typography-figures.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DEMO="$ROOT/preview/style-demo"
OUT="$ROOT/docs/figures"
mkdir -p "$OUT"

python3 - "$DEMO" "$OUT" <<'PY'
import subprocess, sys, os
demo, out = sys.argv[1], sys.argv[2]
pdfs = {
    'before': os.path.join(demo, 'build', 'style-demo-before.pdf'),
    'after':  os.path.join(demo, 'build', 'style-demo.pdf'),
}

def page_with(pdf, anchor):
    txt = subprocess.run(['pdftotext', pdf, '-'], capture_output=True,
                         check=True).stdout.decode('utf-8', 'replace')
    for i, p in enumerate(txt.split('\f'), 1):
        if anchor in p:
            return i
    raise SystemExit('anchor not found: %r in %s' % (anchor, pdf))

# 三组代表页：密集文字 / 图表 / 公式；新版式另加「元素一览」页
anchors = {
    'ch02': '沙粒和岩石是两回事吗',
    'ch07': '开普勒的面积定律',
    'ch13': '这两种能量的总和是恒量',
}
for key, anchor in anchors.items():
    for side in ('before', 'after'):
        pdf = pdfs[side]
        pg = page_with(pdf, anchor)
        dst = os.path.join(out, 'typography-%s-%s.png' % (side, key))
        subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', str(pg), '-l', str(pg),
                        '-singlefile', pdf, dst[:-4]], check=True)
        print('  %s -> page %d -> %s' % (os.path.basename(pdf), pg, os.path.basename(dst)))
    # 左右并排对比图
    subprocess.run(['magick',
                    os.path.join(out, 'typography-before-%s.png' % key),
                    '-bordercolor', '#dddddd', '-border', '6',
                    os.path.join(out, 'typography-after-%s.png' % key),
                    '+append', '-resize', '1600x',
                    os.path.join(out, 'typography-compare-%s.png' % key)], check=True)

# 新版元素一览页
pg = page_with(pdfs['after'], '新版元素一览')
subprocess.run(['pdftoppm', '-png', '-r', '150', '-f', str(pg), '-l', str(pg),
                '-singlefile', pdfs['after'],
                os.path.join(out, 'typography-elements')], check=True)
print('  elements -> page %d' % pg)
PY

echo "输出目录：$OUT"
ls -l "$OUT"/typography-*.png | awk '{print "  "$9, $5"B"}'
