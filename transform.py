import re

LOGO_LIGHT = '''<svg class="hop-logo" viewBox="-6 0 246 64" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hopsite">
  <rect x="-2" y="26" width="9" height="12" rx="2" fill="#ED6B2A"/>
  <rect x="4" y="8" width="40" height="32" rx="7" fill="#23ACD6"/>
  <rect x="10" y="14" width="28" height="18" rx="2" fill="#00162E"/>
  <circle cx="18" cy="23" r="2.6" fill="#fff"/>
  <circle cx="30" cy="23" r="2.6" fill="#fff"/>
  <path d="M17 28 q7 5 14 0" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="12" y="40" width="6" height="12" rx="3" fill="#23ACD6"/>
  <rect x="30" y="40" width="6" height="12" rx="3" fill="#23ACD6"/>
  <rect x="10" y="50" width="10" height="5" rx="2.5" fill="#ED6B2A"/>
  <rect x="28" y="50" width="10" height="5" rx="2.5" fill="#ED6B2A"/>
  <text x="56" y="40" font-family="Urbanist, 'Trebuchet MS', sans-serif" font-weight="800" font-size="32" letter-spacing="-1">
    <tspan fill="#23ACD6">hop</tspan><tspan fill="#ffffff">site.</tspan>
  </text>
</svg>'''

TOPBAR = f'''<header class="hop-topbar">
  <a href="index.html" class="hop-topbar__logo" aria-label="Accueil Hopsite">
    {LOGO_LIGHT}
  </a>
  <a href="index.html" class="hop-topbar__back">&larr; Tous les guides</a>
</header>
'''

FOOTER = f'''<footer class="hop-footer">
  {LOGO_LIGHT}
  <p class="hop-footer__text">Une question, un projet, une demande complémentaire ?</p>
  <p class="hop-footer__contact">
    <a href="mailto:enzo@hopsite.fr">enzo@hopsite.fr</a>
    <span class="hop-footer__sep">&middot;</span>
    <a href="tel:+33786948062">07 86 94 80 62</a>
  </p>
  <p class="hop-footer__credit"><a href="index.html">&larr; Retour à l'accueil</a> &nbsp;|&nbsp; <a href="https://github.com/enzo0602/formation-ia-canva">github.com/enzo0602/formation-ia-canva</a></p>
</footer>
'''

FILES = [
    ("prompt-template-hopsite.html", 1, "Créer une page HTML avec Claude"),
    ("guide-f12-claude.html", 2, "Modifier un élément avec Claude (F12)"),
    ("guide-github-pages.html", 3, "Publier un fichier HTML sur GitHub Pages"),
    ("guide-connecter-github.html", 4, "Connecter GitHub à Claude — Token, push & commit"),
    ("guide-connecter-canva.html", 5, "Connecter Canva à Claude"),
    ("animations-demo.html", 6, "Animations Web — Communication 4.0"),
]

for fname, num, label in FILES:
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. link stylesheet before </head>
    html = html.replace("</head>", '  <link rel="stylesheet" href="hopsite-theme.css">\n</head>', 1)

    # 2. insert topbar right after <body ...> opening tag
    html = re.sub(r"(<body[^>]*>)", r"\1\n" + TOPBAR, html, count=1)

    # 3. insert footer before </body>
    html = html.replace("</body>", FOOTER + "</body>", 1)

    # 4. insert guide badge before first <h1
    badge = f'<div class="hop-guide-badge">Guide {num}</div>\n      '
    html = re.sub(r"(<h1)", badge + r"\1", html, count=1)

    # 5. update <title>
    html = re.sub(r"<title>.*?</title>", f"<title>Guide {num} : {label}</title>", html, count=1, flags=re.S)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"OK {fname} -> Guide {num} : {label}")
