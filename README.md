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
```

The HTML pages and PNG images are generated automatically by the **Build site** GitHub Action (`.github/workflows/build.yml`) whenever anything in `tools/`, `assets/` or `data/` changes. Edit the sources, push, and the site rebuilds itself.

## Publish on GitHub Pages
1. Go to Settings → Pages → Source: **Deploy from a branch** → `main` / `(root)` → Save.
2. The site goes live at `https://webworksa1.github.io/aimoff-com/`.
3. To use the custom domain, add a file named `CNAME` containing `aimoff.com`, then at your registrar set the A records for `@` to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, and a CNAME for `www` → `webworksa1.github.io`. Then enable **Enforce HTTPS**.

## One-time setup
- **Forms:** submissions go through FormSubmit to the site inbox. The first submission triggers an activation email, so click it once and all forms go live. The inbox address is stored encoded and never appears in the page source as plain text.
- **AdSense:** after approval, set `ADSENSE_CLIENT = 'ca-pub-…'` in `tools/build.py` and replace the comment in `ads.txt` with Google’s line. Until then, ad slots show sponsor house ads that link to web.works/contact.
- **Analytics:** set `GA4_ID` in `tools/build.py`.
- **Donations:** the PayPal donate button uses the same inbox as the PayPal account. Make sure a PayPal account exists for it.
- **Leaderboard:** add verified entries to `data/leaderboard.json`, for example `{"player":"name","score":98.4,"verified":true}`.

## Legal
Original content and code © AimOff.com. All rights reserved. Game names are trademarks of their respective owners and are used for compatibility only. See `disclaimer.html`.
