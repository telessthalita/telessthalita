"""Gera os SVGs animados do README (cabeçalho e faixa de tecnologias).

Como usar: edite as listas abaixo e rode `python scripts/gerar_svgs.py`.
Os arquivos saem em assets/. Fontes monoespaçadas deixam as posições previsíveis.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

BG = "#120b20"
PURPLE = "#7b2fff"
LILAC = "#b99cff"
ACCENT = "#d9c2ff"
INK = "#f0eaff"
SOFT = "#a99cc7"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, 'DejaVu Sans Mono', 'Courier New', monospace"
CH = 0.6  # largura aproximada de um caractere monoespaçado, em "em"

NAME = "Thalita Teles"
SUBTITLE = "desenvolvedora fullstack + engenheira de IA"
NOW = "agora: construindo um app de finanças pra casal e estudando engenharia de IA"
BUBBLE = "oi! eu sou a Friday"

STACK_TOP = ["JavaScript", "Python", "React", "Vue", "Node.js", "FastAPI", "Supabase", "Postgres"]
STACK_BOTTOM = ["LLMs", "Ollama", "n8n", "TypeScript", "C#", "SQL", "APIs REST", "Automação", "Git"]


def header() -> str:
    w, h = 1200, 340
    fs = 92
    x0, y0 = 48, 190
    step = fs * CH
    letters = []
    for i, ch in enumerate(NAME):
        if ch == " ":
            continue
        letters.append(
            f'<text class="l" x="{x0 + i * step:.1f}" y="{y0}" '
            f'style="animation-delay:{i * 0.07:.2f}s,{1.4 + i * 0.12:.2f}s">{escape(ch)}</text>'
        )

    sub_fs = 26
    sub_y = 246
    sub_w = len(SUBTITLE) * sub_fs * CH
    n = len(SUBTITLE)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Thalita Teles, desenvolvedora fullstack e engenheira de IA">
<style>
  text {{ font-family: {MONO}; }}
  .l {{ font-size: {fs}px; font-weight: 700; fill: {INK}; opacity: 0;
        animation: rise .6s cubic-bezier(.2,.8,.2,1) forwards, wave 4s ease-in-out infinite; }}
  @keyframes rise {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: none; }} }}
  @keyframes wave {{
    0%, 100% {{ transform: translateY(0); fill: {INK}; }}
    8% {{ transform: translateY(-10px); fill: {ACCENT}; }}
    16% {{ transform: translateY(0); fill: {INK}; }}
  }}
  .sub {{ font-size: {sub_fs}px; fill: {LILAC}; }}
  .clip {{ animation: type 3.2s steps({n}) 1.2s both; }}
  @keyframes type {{ from {{ width: 0; }} to {{ width: {sub_w + 4:.0f}px; }} }}
  .cursor {{ animation: move 3.2s steps({n}) 1.2s both, blink .9s steps(2) infinite; }}
  @keyframes move {{ from {{ transform: translateX(0); }} to {{ transform: translateX({sub_w:.0f}px); }} }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  .now {{ font-size: 17px; fill: {SOFT}; }}
  .dot {{ animation: pulse 2.4s ease-out infinite; transform-origin: 56px 300px; }}
  @keyframes pulse {{ 0% {{ r: 5; opacity: 1; }} 70% {{ r: 12; opacity: 0; }} 100% {{ r: 12; opacity: 0; }} }}
  .eyes {{ transform-origin: 1040px 120px; animation: lid 5s infinite; }}
  @keyframes lid {{ 0%, 92%, 100% {{ transform: scaleY(1); }} 95% {{ transform: scaleY(.1); }} }}
  .pupils {{ animation: look 7s ease-in-out infinite; }}
  @keyframes look {{
    0%, 20% {{ transform: translate(0, 0); }}
    30%, 45% {{ transform: translate(-9px, 4px); }}
    55%, 70% {{ transform: translate(8px, -3px); }}
    80%, 100% {{ transform: translate(0, 0); }}
  }}
  .bubble {{ animation: pop 7s ease-in-out infinite; transform-origin: 1040px 70px; }}
  @keyframes pop {{ 0%, 8% {{ opacity: 0; transform: scale(.6); }} 14%, 60% {{ opacity: 1; transform: scale(1); }} 68%, 100% {{ opacity: 0; transform: scale(.6); }} }}
</style>
<defs>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/>
    <feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .06 0"/></filter>
  <clipPath id="typing"><rect class="clip" x="{x0}" y="{sub_y - sub_fs}" height="{sub_fs + 10}" width="0"/></clipPath>
</defs>
<rect width="{w}" height="{h}" fill="{BG}"/>
<rect width="{w}" height="{h}" filter="url(#grain)"/>
<rect x="{x0}" y="36" width="40" height="40" fill="{PURPLE}"/>
<text x="{x0 + 20}" y="63" text-anchor="middle" font-size="17" font-weight="700" fill="#fff">TT</text>
<text x="{x0 + 56}" y="62" font-size="15" fill="{SOFT}">thalita teles · Sergipe, Brasil</text>
{''.join(letters)}
<text class="sub" x="{x0}" y="{sub_y}" clip-path="url(#typing)">{escape(SUBTITLE)}</text>
<rect class="cursor" x="{x0 + 2}" y="{sub_y - sub_fs + 4}" width="13" height="{sub_fs}" fill="{ACCENT}"/>
<circle class="dot" cx="56" cy="300" r="5" fill="{ACCENT}"/>
<circle cx="56" cy="300" r="5" fill="{ACCENT}"/>
<text class="now" x="74" y="306">{escape(NOW)}</text>
<g class="bubble">
  <rect x="955" y="50" width="170" height="34" fill="{PURPLE}"/>
  <path d="M1030 84 l10 12 l6 -12 z" fill="{PURPLE}"/>
  <text x="1040" y="72" text-anchor="middle" font-size="15" fill="#fff">{escape(BUBBLE)}</text>
</g>
<g class="eyes">
  <ellipse cx="1012" cy="125" rx="20" ry="23" fill="#fff"/>
  <ellipse cx="1068" cy="125" rx="20" ry="23" fill="#fff"/>
  <g class="pupils"><circle cx="1012" cy="125" r="10" fill="{BG}"/><circle cx="1068" cy="125" r="10" fill="{BG}"/></g>
</g>
<rect y="{h - 6}" width="{w}" height="6" fill="{PURPLE}"/>
</svg>
"""


def row(words, y, fs, cls, hollow):
    """Uma linha da faixa: as palavras duas vezes seguidas, pra rolar sem emenda."""
    gap = fs * 1.4
    parts, x = [], 0.0
    for i, word in enumerate(words):
        style = "hollow" if (hollow and i % 2) else "solid"
        parts.append(f'<text class="{style}" x="{x:.1f}" y="{y}" font-size="{fs}">{escape(word)}</text>')
        x += len(word) * fs * CH + gap / 2
        parts.append(f'<text class="star" x="{x:.1f}" y="{y}" font-size="{fs * 0.7:.0f}">✳</text>')
        x += fs * CH + gap / 2
    width = x
    one = "".join(parts)
    return f'<g class="{cls}"><g>{one}</g><g transform="translate({width:.1f} 0)">{one}</g></g>', width


def stack() -> str:
    w, h = 1200, 150
    top, wt = row(STACK_TOP, 64, 40, "r0", True)
    bottom, wb = row(STACK_BOTTOM, 112, 26, "r1", False)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Tecnologias: {escape(', '.join(STACK_TOP + STACK_BOTTOM))}">
<style>
  text {{ font-family: {MONO}; font-weight: 700; }}
  .solid {{ fill: #fff; }}
  .hollow {{ fill: none; stroke: #fff; stroke-width: 1.4; }}
  .star {{ fill: {ACCENT}; }}
  .r1 .solid {{ fill: {ACCENT}; font-weight: 400; }}
  .r1 .star {{ fill: #fff; }}
  .r0 {{ animation: left 26s linear infinite; }}
  .r1 {{ animation: right 22s linear infinite; }}
  @keyframes left {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-{wt:.1f}px); }} }}
  @keyframes right {{ from {{ transform: translateX(-{wb:.1f}px); }} to {{ transform: translateX(0); }} }}
</style>
<rect width="{w}" height="{h}" fill="{BG}"/>
<g transform="rotate(-2 600 75)">
  <rect x="-40" y="14" width="{w + 80}" height="122" fill="{PURPLE}"/>
  {top}
  {bottom}
</g>
</svg>
"""


(OUT / "header.svg").write_text(header(), encoding="utf-8")
(OUT / "stack.svg").write_text(stack(), encoding="utf-8")
print("ok:", ", ".join(p.name for p in OUT.glob("*.svg")))
