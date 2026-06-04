# -*- coding: utf-8 -*-
"""build_inline_css.py — inlina fonts.css + colors_and_type.css + styles.css
dentro do index.html (entre os marcadores BUILD:CSS-INLINE) para eliminar os
requests de CSS render-blocking (o maior gargalo de LCP/FCP do site).

Re-executável e idempotente: rode sempre que editar qualquer .css.
    python build_inline_css.py
"""
import os, re

HERE  = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "index.html")
ORDER = ["fonts.css", "colors_and_type.css", "styles.css"]  # ordem da cascata

START = "<!-- BUILD:CSS-INLINE-START -->"
END   = "<!-- BUILD:CSS-INLINE-END -->"

parts, total = [], 0
for name in ORDER:
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        css = fh.read().strip()
    total += len(css)
    parts.append("/* ===== %s ===== */\n%s" % (name, css))

inline = START + "\n<style>\n" + "\n\n".join(parts) + "\n</style>\n" + END

with open(INDEX, encoding="utf-8") as fh:
    html = fh.read()

pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
if not pattern.search(html):
    raise SystemExit("ERRO: marcadores BUILD:CSS-INLINE nao encontrados em index.html")

# lambda evita interpretacao de '\\' / grupos no CSS pelo re.sub
html = pattern.sub(lambda m: inline, html)

with open(INDEX, "w", encoding="utf-8") as fh:
    fh.write(html)

print("OK: CSS inline atualizado (%d arquivos, %d bytes brutos de CSS)." % (len(ORDER), total))
