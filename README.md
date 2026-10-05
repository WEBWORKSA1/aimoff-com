# AimOff.com

**Train your aim. Measure everything.** AimOff is a free, browser-based aim-training hub. It includes a 5-mode aim trainer, reaction and CPS tests, a sensitivity converter (with 72 game-pair pages), crosshair and mouse tools, guides, an "Aiming Off" navigation section, coaching lead-gen, contests, donations and sponsorship pages.

Pure static HTML/CSS/JS, hosted free on **GitHub Pages**.

- `STRATEGY.md`: why this idea, the revenue model, the 35-site competitive research and keywords
- `BUILD-PROMPT.md`: the phase-wise build prompt (phases 0–9)

## Structure
```
index.html, train.html, reaction-test.html, cps-test.html, sensitivity-converter.html, tools.html,
guides.html, aiming-off.html, videos.html, coaching.html (lead-gen), contests.html, support.html (donations),
advertise.html, careers.html, about.html, contact.html, privacy.html, terms.html, disclaimer.html, 404.html
convert/            72 game-to-game sensitivity pages + index
assets/css|js|img   styles, scripts (main, trainer, tools), icons, OG image
data/leaderboard.json  contest leaderboard (edit to publish verified entries)
tools/build.py      generator: edit tools/pages*.py, then run `python3 tools/build.py`
_layouts/           shared page layouts rendered by GitHub Pages' built-in Jekyll
```

**How it builds:** `python3 tools/build.py` writes each page as front matter plus body. GitHub Pages' built-in Jekyll wraps each one in a shared layout from `_layouts/`, which holds the header, footer and top sponsorship bar in one place, and also renders `sitemap.xml`. No extra service is needed.

**Optional auto-build:** copy `tools/build-workflow.yml` to `.github/workflows/build.yml` (GitHub web editor → Add file). After that, every push to `tools/`, `assets/` or `data/` regenerates the pages, and the PNG icons and social-share image (`assets/img/icon-192.png`, `icon-512.png`, `og.png`) are created automatically. Until you do this, those PNGs aren't in the repo, and the SVG favicon is used.

## Publish on GitHub Pages
1. Go to Settings → Pages → Source: **Deploy from a branch** → `main` / `(root)` → Save. (Jekyll stays enabled, and it renders the conversion pages.)
2. The site goes live at `https://webworksa1.github.io/aimoff-com/`.
3. To use the custom domain, add a file named `CNAME` containing `aimoff.com`, then at your registrar set the A records for `@` to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, and a CNAME for `www` → `webworksa1.github.io`. Then enable **Enforce HTTPS**.

## One-time setup
- **Forms:** submissions go through FormSubmit to the site inbox. The first submission triggers an activation email, so click it once and all forms go live. The inbox address is stored encoded and never appears in the page source as plain text.
- **AdSense:** after approval, set `ADSENSE_CLIENT = 'ca-pub-…'` in `tools/build.py`, run the build (or let the workflow do it), and replace the comment in `ads.txt` with Google’s line. Until then, ad slots show sponsor house ads that link to web.works/contact.
- **Analytics:** set `GA4_ID` in `tools/build.py` and rebuild.
- **Donations:** the PayPal donate button uses the same inbox as the PayPal account. Make sure a PayPal account exists for it.
- **Leaderboard:** add verified entries to `data/leaderboard.json`, for example `{"player":"name","score":98.4,"verified":true}`.

## Legal
Original content and code © AimOff.com. All rights reserved. Game names are trademarks of their respective owners and are used for compatibility only. See `disclaimer.html`.
