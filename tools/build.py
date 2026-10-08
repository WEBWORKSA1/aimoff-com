#!/usr/bin/env python3
"""AimOff.com static site generator.

Run from the repo root:  python3 tools/build.py
Edits go in tools/pages.py (page bodies) and the settings below; the script writes
plain .html files into the repo root, so GitHub Pages serves them with no build step.
"""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
import pages as P

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# ---- Settings you will edit once ----------------------------------------
SITE = 'https://aimoff.com'          # canonical domain
ADSENSE_CLIENT = 'ca-pub-6620975821265271'  # Google AdSense publisher ID
GA4_ID = ''                           # e.g. 'G-XXXXXXXXXX'
SPONSOR_URL = 'https://web.works/contact'
# --------------------------------------------------------------------------

NAV = [
    ('train.html', 'Aim Trainer'),
    ('Tests', [('reaction-test.html', '⚡ Reaction Time Test'), ('cps-test.html', '🖱️ CPS / Click Speed Test'), ('train.html?mode=tracking', '🎯 Tracking Test'), ('train.html?mode=precision', '🔬 Precision Test')]),
    ('Tools', [('sensitivity-converter.html', '🔁 Sensitivity Converter'), ('tools.html#edpi', '🧮 eDPI & cm/360'), ('tools.html#crosshair', '✛ Crosshair Generator'),
               ('tools.html#mouse', '🖲️ Mouse Tests (DPI, Hz, double-click)'), ('tools.html#fov', '🔭 FOV Converter'), ('convert/index.html', '📚 All game-to-game conversions')]),
    ('guides.html', 'Guides'),
    ('aiming-off.html', 'Aiming Off'),
    ('videos.html', 'Videos'),
    ('contests.html', 'Contests'),
]

LIQ = object()  # sentinel: render Liquid placeholders instead of values

def rel(depth):
    return '../' * depth

def nav_html(active, d):
    out = []
    for href, label in NAV:
        if isinstance(label, list):
            items = ''.join(f'<a href="{rel(d)}{h}">{t}</a>' for h, t in label)
            out.append(f'<li class="dd"><button aria-haspopup="true">{href} ▾</button><div class="dd-menu">{items}</div></li>')
        else:
            cls = (' class="active"' if href == active else '') if active != LIQ else f"{{% if page.active == '{href}' %}} class=\"active\"{{% endif %}}"
            out.append(f'<li><a href="{rel(d)}{href}"{cls}>{label}</a></li>')
    out.append(f'<li><a href="{rel(d)}support.html">❤ Support</a></li>')
    return ''.join(out)

LOGO = ('<svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="13" fill="none" stroke="currentColor" stroke-width="2.5"/>'
        '<circle cx="16" cy="16" r="6" fill="none" stroke="#22e3c4" stroke-width="2.5"/><circle cx="21" cy="12" r="2.6" fill="#ff4d6d"/>'
        '<path d="M16 1v6M16 25v6M1 16h6M25 16h6" stroke="currentColor" stroke-width="2.5"/></svg>')

def head(title, desc, path, d, extra_schema=None, noindex=False, liquid=False):
    canon = f'{SITE}/{path}' if path != 'index.html' else f'{SITE}/'
    if liquid: canon = '{{ page.canon }}'
    ads = (f'<meta name="google-adsense-account" content="{ADSENSE_CLIENT}">\n'
           f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>') if ADSENSE_CLIENT else ''
    ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>'
          f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>") if GA4_ID else ''
    schema = [{
        '@context': 'https://schema.org', '@type': 'WebSite', 'name': 'AimOff', 'url': SITE + '/',
        'potentialAction': {'@type': 'SearchAction', 'target': SITE + '/guides.html?q={search_term_string}', 'query-input': 'required name=search_term_string'}
    }, {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'AimOff.com', 'url': SITE + '/', 'logo': SITE + '/assets/img/icon-512.png'}]
    if extra_schema: schema.extend(extra_schema)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    schema_json = json.dumps(schema)
    if liquid: robots, schema_json = '{{ page.robots }}', '{{ page.schema }}'
    return f'''<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="AimOff">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#070b14">
<link rel="icon" href="{rel(d)}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{rel(d)}assets/img/icon-192.png">
<link rel="manifest" href="{rel(d)}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel(d)}assets/css/style.css">
<script type="application/ld+json">{schema_json}</script>
{ads}{ga}
</head>'''

def topbar():
    return (f'<div class="topbar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — '
            f'<a href="{SPONSOR_URL}" target="_blank" rel="noopener">click here</a></div>')

def header(active, d):
    return f'''<a class="skip" href="#main">Skip to content</a>
{topbar()}
<header class="site-header"><div class="container nav">
<a class="brand" href="{rel(d)}index.html" aria-label="AimOff home">{LOGO}<span>Aim<b>Off</b></span></a>
<ul class="nav-links" id="nav">{nav_html(active, d)}</ul>
<div class="nav-cta"><a class="btn btn-primary btn-sm" href="{rel(d)}coaching.html">Free Aim Assessment</a>
<button class="icon-btn" data-theme-toggle aria-label="Toggle light/dark theme">☾</button>
<button class="icon-btn burger" aria-label="Menu" aria-controls="nav" aria-expanded="false">☰</button></div>
</div></header>'''

def footer(d):
    r = rel(d)
    return f'''<footer class="site-footer"><div class="container">
<div class="foot-grid">
 <div><a class="brand" href="{r}index.html">{LOGO}<span>Aim<b>Off</b></span></a>
  <p class="muted small mt">Free aim training, reaction & click tests, sensitivity tools and aiming guides — for gamers, competitors and anyone who wants to hit what they aim at.</p>
  <a class="btn btn-gold btn-sm" href="{r}support.html">❤ Support AimOff</a></div>
 <div><h4>Train & Test</h4><ul><li><a href="{r}train.html">Aim Trainer</a></li><li><a href="{r}reaction-test.html">Reaction Time Test</a></li><li><a href="{r}cps-test.html">CPS Test</a></li><li><a href="{r}train.html?mode=tracking">Tracking Test</a></li><li><a href="{r}contests.html">Monthly Contests</a></li></ul></div>
 <div><h4>Tools & Learn</h4><ul><li><a href="{r}sensitivity-converter.html">Sensitivity Converter</a></li><li><a href="{r}tools.html">eDPI · Crosshair · Mouse</a></li><li><a href="{r}convert/index.html">Game Conversions</a></li><li><a href="{r}guides.html">Guides</a></li><li><a href="{r}aiming-off.html">Aiming Off (Navigation)</a></li><li><a href="{r}videos.html">Videos</a></li></ul></div>
 <div><h4>Work with us</h4><ul><li><a href="{r}coaching.html">Find a Coach</a></li><li><a href="{r}coaching.html#become-coach">Become a Coach</a></li><li><a href="{r}advertise.html">Advertise & Sponsor</a></li><li><a href="{r}careers.html">Careers & Talent</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{SPONSOR_URL}" target="_blank" rel="noopener">Buy / Partner on this domain</a></li></ul></div>
 <div><h4>Weekly aim drills, free</h4><p class="muted small">One 10-minute routine + contest alerts every week. No spam.</p>
  <form class="js-form" data-subject="Newsletter signup" data-success="You're in! First drill arrives this week.">
   <input class="hp" name="_honey" tabindex="-1" autocomplete="off">
   <input type="hidden" name="form" value="newsletter">
   <div class="newsletter"><input type="email" name="email" required placeholder="you@email.com" aria-label="Email"><button class="btn btn-primary btn-sm" type="submit">Join</button></div>
   <div class="form-msg" role="status"></div></form></div>
</div>
<div class="legal">
 <p><b>Trademark & copyright disclosure:</b> AimOff.com is an independent website. “AimOff” is used here as a site name built from the common English phrase “aim off” (a long-standing term in navigation and target sports for deliberately aiming to one side of a target). We claim no exclusive rights in the generic phrase “aim off” and are not affiliated with, endorsed by, or sponsored by any company, product, team or organisation using a similar name. All game titles, publisher names and other trademarks mentioned (e.g. Counter-Strike 2, Valorant, Apex Legends, Overwatch 2, Call of Duty, Fortnite) belong to their respective owners and are used only to describe compatibility (nominative fair use). Embedded videos remain the property of their creators and are shown via YouTube’s official embed player. Original site text, code, tools and graphics © <span data-year>2026</span> AimOff.com — all rights reserved. See our <a href="{r}disclaimer.html">Disclaimer</a>, <a href="{r}privacy.html">Privacy Policy</a> and <a href="{r}terms.html">Terms</a>.</p>
 <p>Some links may be affiliate links; we may earn a commission at no extra cost to you. Advertising helps keep every tool free.</p>
</div></div></footer>
<div class="cookie" id="cookie" hidden><b>Cookies & ads</b><p class="muted small" style="margin:.4em 0 .8em">We use essential storage for your scores and settings. With your consent, Google and partners use cookies to show and measure ads. <a href="{r}privacy.html">Learn more</a>.</p>
<div style="display:flex;gap:8px"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-secondary btn-sm" data-consent="essential">Essential only</button></div></div>
<div class="modal" id="lead-modal" hidden role="dialog" aria-labelledby="lm-title"><div class="card"><button class="close" aria-label="Close">×</button>
<span class="eyebrow">Free download</span><h3 id="lm-title">Get the 14-Day Aim Plan</h3>
<p class="muted">A day-by-day routine (flicks, tracking, switching, micro-adjusting) built around the free AimOff drills — plus a personal sensitivity check.</p>
<form class="js-form" data-subject="Lead magnet: 14-Day Aim Plan" data-success="Check your inbox — your 14-day plan is on the way!">
<input class="hp" name="_honey" tabindex="-1" autocomplete="off"><input type="hidden" name="form" value="14-day-aim-plan">
<div class="field"><input name="name" placeholder="First name" required aria-label="First name"></div>
<div class="field"><input type="email" name="email" placeholder="Email" required aria-label="Email"></div>
<div class="field"><select name="main_game" aria-label="Main game"><option>Valorant</option><option>Counter-Strike 2</option><option>Apex Legends</option><option>Fortnite</option><option>Overwatch 2</option><option>Call of Duty</option><option>Other</option></select></div>
<button class="btn btn-primary btn-block" type="submit">Send me the plan</button><div class="form-msg" role="status"></div></form></div></div>'''

def render(path, title, desc, body, active='', scripts=(), schema=None, noindex=False, sticky=True, liquid=False):
    d = path.count('/')
    r = rel(d)
    sc = ''.join(f'<script src="{r}assets/js/{s}" defer></script>' for s in scripts)
    stick = (f'<div class="sticky-cta"><a class="btn btn-primary btn-sm" href="{r}coaching.html">\U0001f3af Free Aim Assessment</a></div>') if sticky else ''
    if liquid:
        title, desc, sc, stick, body, active = '{{ page.title }}', '{{ page.description }}', '{{ page.scripts }}', '{{ page.sticky }}', '{{ content }}', LIQ
    parts = dict(sc=sc, stick=stick)
    html = (head(title, desc, path, d, schema, noindex, liquid) + '\n<body>\n' + header(active, d) +
            f'\n<main id="main">\n{body.replace("{R}", r)}\n</main>\n' + footer(d) + stick +
            f'\n<script src="{r}assets/js/main.js" defer></script>{sc}\n</body></html>\n')
    return html, parts

def page(path, title, desc, body, active='', scripts=(), schema=None, noindex=False, sticky=True):
    html, _ = render(path, title, desc, body, active, scripts, schema, noindex, sticky)
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    return path

def yaml_block(k, v):
    return f'{k}: |-\n' + ''.join('  ' + line + '\n' for line in v.split('\n'))

def jekyll_main_pages():
    """Rewrite every top-level page as front matter + body over shared layouts (_layouts/default*.html),
    so the header/footer live in one place. GitHub Pages' Jekyll renders them to identical HTML."""
    os.makedirs(os.path.join(ROOT, '_layouts'), exist_ok=True)
    for d in (0, 1):
        lay, _ = render('x/' * d + 'x.html', '', '', '', liquid=True)
        open(os.path.join(ROOT, '_layouts', f'default{d}.html'), 'w', encoding='utf-8').write(lay)
    pages = list(P.PAGES) + [p for p in P.conversion_pages() if p['path'] == 'convert/index.html']
    for p in pages:
        d = p['path'].count('/')
        html, parts = render(**p)
        canon = f"{SITE}/{p['path']}" if p['path'] != 'index.html' else f'{SITE}/'
        schema = [json.loads(html.split('<script type="application/ld+json">')[1].split('</script>')[0])][0]
        robots = '<meta name="robots" content="noindex">' if p.get('noindex') else '<meta name="robots" content="index,follow,max-image-preview:large">'
        fm = ('---\n' + f'layout: default{d}\n' + yaml_block('title', p['title']) + yaml_block('description', p['desc']) +
              yaml_block('canon', canon) + yaml_block('robots', robots) + yaml_block('schema', json.dumps(schema, ensure_ascii=False)) +
              yaml_block('active', p.get('active', '') or '-') + yaml_block('scripts', parts['sc'] or '') + yaml_block('sticky', parts['stick'] or '') + '---\n')
        body = p['body'].replace('{R}', rel(d))
        assert '{{' not in body and '{%' not in body, p['path']
        with open(os.path.join(ROOT, p['path']), 'w', encoding='utf-8') as f:
            f.write(fm + body)

def jekyll_convert_pages():
    """Replace the 72 generated conversion pages with tiny Jekyll stubs + one shared layout.
    GitHub Pages' built-in Jekyll renders them to the identical HTML, keeping the repo small."""
    tpl = P.conv_page('x', 'y', P.LIQUID)
    tpl['path'] = 'convert/{{ page.a }}-to-{{ page.b }}-sensitivity.html'
    out = page(**tpl)
    os.makedirs(os.path.join(ROOT, '_layouts'), exist_ok=True)
    os.replace(os.path.join(ROOT, out), os.path.join(ROOT, '_layouts', 'convert.html'))
    for a in P.GAMES:
        for b in P.GAMES:
            if a == b or 'csgo' in (a, b):
                continue
            v = P.conv_values(a, b)
            fm = '---\nlayout: convert\n' + ''.join(f"{k}: '{v[k]}'\n" for k in ['a', 'b', 'na', 'nb', 'ya', 'yb', 'm', 'nbplus', 'rows']) + '---\n'
            with open(os.path.join(ROOT, 'convert', f'{a}-to-{b}-sensitivity.html'), 'w', encoding='utf-8') as f:
                f.write(fm)

SITEMAP = """---
layout: null
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{%- for p in site.html_pages %}{% unless p.url contains '404' %}
<url><loc>https://aimoff.com{{ p.url }}</loc><lastmod>{{ site.time | date: '%Y-%m-%d' }}</lastmod></url>{% endunless %}{% endfor %}
</urlset>
"""

def main():
    built = []
    for p in P.PAGES:
        built.append(page(**p))
    for p in P.conversion_pages():
        built.append(page(**p))
    jekyll_convert_pages()
    jekyll_main_pages()
    # sitemap.xml is rendered by GitHub Pages' Jekyll from every page that has front matter
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(SITEMAP)
    print(f'Built {len(built)} pages')

if __name__ == '__main__':
    main()
