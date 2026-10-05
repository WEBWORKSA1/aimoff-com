# AimOff.com: Phase-Wise Build Prompt

Use these prompts in order with any capable AI coding assistant or developer to rebuild or extend AimOff.com. Each phase is self-contained and ends with acceptance criteria. v1 of this repository already implements Phases 1–8.

---

## Phase 0: Master context (paste first, every session)

> You are building **AimOff.com**, a modern, fast, responsive, fully static website hosted free on **GitHub Pages** (no server, no build step required to serve). Concept: a free browser-based **aim-training & aiming-skills hub** (aim trainer, reaction test, CPS test, sensitivity converter, crosshair and mouse tools, guides), with a signature section on the navigation technique **"aiming off"**. Brand line: *"Train your aim. Measure everything."* Philosophy: *smart aim beats lucky aim.*
> Monetisation: Google AdSense, YouTube embeds and our own channel, affiliates, sponsorships, coaching lead generation, donations, and monthly contests with prizes.
> Hard rules:
> 1. On top of **every** page, show: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linked to `https://web.works/contact`.
> 2. Every form and contact link routes to ONE inbox. **That address must never appear in plain text** in HTML, JS, docs or repo files. Store it as an encoded string, assemble it at runtime, and submit forms via a JS POST to a form relay (FormSubmit AJAX endpoint).
> 3. Avoid trademark or copyright conflicts: no publisher logos or game assets; game names only for compatibility (nominative use); a full trademark and copyright disclosure in the footer plus a Disclaimer page.
> 4. Stack: semantic HTML5, one CSS file, vanilla JS (no framework), Google Fonts (Inter + Space Grotesk), dark-first theme with a light toggle. Lighthouse target: 90+ in every category.

## Phase 1: Foundation & design system
> Create the repo structure: `index.html`, `assets/css/style.css`, `assets/js/main.js`, `assets/img/`, `tools/build.py` (Python templater that writes static pages), `data/`, `convert/`. Build the design tokens (colours: bg #070b14, accent #22e3c4, violet #7c5cff, hot #ff4d6d, gold #ffc145), typography scale with clamp(), buttons, cards, grids (2/3/4 columns collapsing to 1 on mobile), forms, tables, accordions, the sponsorship top bar, a sticky header with dropdowns and a mobile burger, and a footer with newsletter, link columns and the legal disclosure. Add a skip link, focus styles and reduced-motion support.
> **Accept when:** every page shares the header and footer, there is no horizontal scroll at 360 px, and the theme toggle persists.

## Phase 2: Core tools (the traffic engine)
> Build: (a) a **canvas Aim Trainer** with Gridshot, Flick, Tracking, Reflex and Precision modes, 30/60 s, S/M/L targets, crosshair colour, HUD (score, time, hits, accuracy, personal best), tiers (Rookie→Legend), local history, share, and "enter contest" and "free assessment" CTAs on the results screen. (b) A **Reaction Time Test**: 5-try average, early-click detection, percentile and tier. (c) A **CPS Test**: 1/5/10/30/60 s, live CPS and ranks. (d) A **Sensitivity Converter** using public yaw constants (CS2/Apex/TF2/Quake 0.022, Valorant 0.07, OW2/CoD 0.0066, Fortnite 0.005555 per %, plus custom), outputting new sens, cm/360, in/360, eDPI and multiplier. (e) **Tools page**: eDPI, cm/360, FOV converter, crosshair generator (canvas preview, randomise, export), polling-rate tester (pointerrawupdate), DPI analyzer (pointer lock), double-click tester.
> **Accept when:** CS2 1.2 @800 → Valorant 0.377 / 43.3 cm, all tools work on touch and mouse, and personal bests persist in localStorage.

## Phase 3: SEO & content
> Generate **72 programmatic pages** `convert/{a}-to-{b}-sensitivity.html`, each with a unique title, meta description, multiplier, quick table, how-to and reverse link, plus an index page. Write guides (the 4 pillars, sensitivity method, 10-minute warm-up, crosshair placement, setup checklist, grips, leading targets, darts, archery, dominant-eye test) and the **Aiming Off** pillar page (SVG diagram, calculator offset = d·tan θ, steps, mistakes, related techniques, videos, FAQ). Add JSON-LD (WebSite, Organization, WebApplication, FAQPage), canonical URLs, Open Graph and Twitter cards, `sitemap.xml`, `robots.txt` and `manifest.webmanifest`.
> **Accept when:** every page has a unique title and description and the sitemap lists all of them.

## Phase 4: Monetisation
> Add `.ad-slot` placeholders (below tools, between guide sections, a 300×250 sidebar) that render AdSense `<ins>` units when `ADSENSE_CLIENT` is set in `tools/build.py`, and otherwise show **house ads** selling sponsorship (linking to web.works/contact). Never place ads inside the game area. Add `ads.txt`, a consent banner (Accept all / Essential only) and an **Advertise** media-kit page with packages (tool sponsorship, contest title sponsor, video, sponsored guides, display, newsletter, affiliate) and a lead form. Add a lite YouTube embed component (thumbnail first, youtube-nocookie iframe on click) and a Videos page.
> **Accept when:** with no client ID, house ads show; with an ID, AdSense loads and respects "Essential only".

## Phase 5: Lead generation (dedicated, high-converting)
> Build `coaching.html` with a hero promise ("free aim assessment in 48 h"), a benefit checklist, stats, and a **3-step multi-step form** (game, rank, goal, weakness chips → region, budget, availability, notes → name, email, Discord, age and consent). Add secondary funnels: become a coach, teams/orgs proposal, clubs/ranges listing. Put a quick-assessment block on Home and Trainer, a sticky "Free Aim Assessment" CTA, and an exit-intent / third-play **lead-magnet modal** ("14-Day Aim Plan"). Prefill fields from the query string (e.g. `?game=Valorant`).
> **Accept when:** each form posts JSON to the relay with `_subject`, `_template=table`, a honeypot, page URL and timestamp, and a mailto fallback appears on failure.

## Phase 6: Community, contests, donations, hiring
> `contests.html`: monthly AimOff Open (Gridshot 60 s, Reaction Royale, Clip of the Month), a prize tier display, a leaderboard loaded from `data/leaderboard.json`, an entry form with proof URL, and **official rules** (no purchase necessary, skill-based, anti-cheat, deadlines, void where prohibited). `support.html`: donation tiers ($5/$15/$50/$150/custom) plus purpose (operations, prizes, marketing, hiring), a PayPal donate URL built at click time, a fund-allocation bar chart, and a pledge/in-kind form. `careers.html`: roles (coach, writer, video editor, community/contest manager, developer, partnerships) plus an application form.
> **Accept when:** a donation opens PayPal with the amount and purpose, and contest entries prefill from trainer results.

## Phase 7: Legal & trust
> Privacy Policy (forms via FormSubmit, localStorage, AdSense cookie disclosure with opt-out links, GA4, YouTube nocookie, PayPal, children, GDPR/CCPA/PIPEDA rights), Terms, a **Disclaimer / Trademark & Copyright** page, About (story, values, roadmap), Contact (topic select including a copyright concern; a protected email button; web.works/contact for domain enquiries), and a custom 404.

## Phase 8: Deploy on GitHub Pages (free)
> Push to `WEBWORKSA1/aimoff-com` (public). A GitHub Action regenerates the HTML and images from `tools/` on every push. Settings → Pages → Deploy from branch `main` / root. Include `.nojekyll`. Use relative links so the site works at `webworksa1.github.io/aimoff-com/` and on the custom domain. To go live on AimOff.com: add a `CNAME` file containing `aimoff.com`, set DNS A records to 185.199.108.153 / .109.153 / .110.153 / .111.153 plus `www` CNAME → `webworksa1.github.io`, then tick "Enforce HTTPS". Submit the first form once and click FormSubmit’s activation email.

## Phase 9: Growth & expansion (next sprints)
> 1) Apply to AdSense once there are 20–30 indexed pages and real traffic, then set `ADSENSE_CLIENT` and update `ads.txt`. 2) Add GA4 and Search Console, and submit the sitemap. 3) Launch a YouTube channel: weekly 60-second drill Shorts and contest highlights. 4) Add a WebGL 3D trainer with FOV presets. 5) Add global leaderboards via a free backend (Supabase or Firebase) with anti-cheat heuristics. 6) Build a pro-settings database with affiliate gear links. 7) Localise into ES, PT-BR, TR and HI. 8) Add a premium ad-free tier and a Discord bot. 9) Do outreach to aim-training communities and creators, and sell contest title sponsorships.
