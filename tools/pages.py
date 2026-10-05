"""Page bodies for AimOff.com — core pages (home, trainer, tests, tools, conversions).
{R} is replaced with the relative path prefix to the site root."""
import json
from pages2 import PAGES2

AD = '<div class="ad-slot" data-slot="">Advertisement</div>'

def faq_schema(qas):
    return [{'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qas]}]

def faq_html(qas):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qas)

def tool_schema(name, url, desc):
    return [{'@context': 'https://schema.org', '@type': 'WebApplication', 'name': name, 'url': 'https://aimoff.com/' + url,
             'applicationCategory': 'GameApplication', 'operatingSystem': 'Any (web browser)', 'description': desc,
             'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}]

LEAD_BLOCK = '''<section class="section"><div class="container"><div class="lead-box split reveal">
<div><span class="eyebrow">Free · 15 minutes · No commitment</span><h2>Stuck at the same rank? Get a free aim assessment.</h2>
<ul class="checks"><li>A coach reviews your scores, sensitivity and setup</li><li>You get a written 3-point fix list within 48 hours</li><li>Matched to coaches for Valorant, CS2, Apex, Fortnite, OW2 and CoD</li><li>Pay nothing unless you choose to book sessions</li></ul>
<a class="btn btn-secondary" href="{R}coaching.html">See how coaching works →</a></div>
<form class="card js-form" data-subject="Lead: Free aim assessment (quick form)" data-success="Request received! A coach will email you within 48 hours.">
<input class="hp" name="_honey" tabindex="-1" autocomplete="off"><input type="hidden" name="form" value="quick-assessment">
<h3>Claim your free assessment</h3>
<div class="row"><div class="field"><label for="qa-n">Name</label><input id="qa-n" name="name" required></div>
<div class="field"><label for="qa-e">Email</label><input id="qa-e" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="qa-g">Main game</label><select id="qa-g" name="game" required><option value="">Choose…</option><option>Valorant</option><option>Counter-Strike 2</option><option>Apex Legends</option><option>Fortnite</option><option>Overwatch 2</option><option>Call of Duty</option><option>Other</option></select></div>
<div class="field"><label for="qa-r">Current rank</label><input id="qa-r" name="rank" placeholder="e.g. Gold 2"></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about coaching. Unsubscribe anytime.</label>
<button class="btn btn-primary btn-block mt" type="submit">Get my free assessment</button><div class="form-msg" role="status"></div></form>
</div></div></section>'''

HERO_SVG = '''<svg viewBox="0 0 400 400" width="100%" height="100%" aria-hidden="true">
<defs><radialGradient id="tg" cx="50%" cy="50%"><stop offset="0" stop-color="#ff8aa0"/><stop offset="1" stop-color="#ff2d55"/></radialGradient></defs>
<g opacity=".18" stroke="#93a1bf">''' + ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="400"/><line x1="0" y1="{x}" x2="400" y2="{x}"/>' for x in range(0, 401, 40)) + '''</g>
<circle cx="200" cy="200" r="150" fill="none" stroke="#22e3c4" stroke-opacity=".25" stroke-width="2"><animate attributeName="r" values="140;160;140" dur="4s" repeatCount="indefinite"/></circle>
<circle cx="200" cy="200" r="95" fill="none" stroke="#7c5cff" stroke-opacity=".4" stroke-width="2"/>
<circle cx="265" cy="150" r="26" fill="url(#tg)"><animate attributeName="cx" values="265;130;300;265" dur="6s" repeatCount="indefinite"/><animate attributeName="cy" values="150;260;250;150" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="120" cy="120" r="14" fill="url(#tg)" opacity=".8"/><circle cx="310" cy="300" r="10" fill="url(#tg)" opacity=".7"/>
<g stroke="#22e3c4" stroke-width="4"><line x1="200" y1="170" x2="200" y2="190"/><line x1="200" y1="210" x2="200" y2="230"/><line x1="170" y1="200" x2="190" y2="200"/><line x1="210" y1="200" x2="230" y2="200"/></g>
<text x="24" y="380" fill="#93a1bf" font-family="Space Grotesk, Inter, sans-serif" font-size="16">ACC 97.4%  ·  TTK 312ms  ·  GOLD</text></svg>'''

TOOLS = [
    ('train.html', '🎯', 'Aim Trainer', '5 modes: Gridshot, Flick, Tracking, Reflex, Precision. No download.', 'Most played'),
    ('reaction-test.html', '⚡', 'Reaction Time Test', 'Average of 5 tries, percentile and tier.', ''),
    ('cps-test.html', '🖱️', 'CPS Test', '1, 5, 10, 30 & 60-second click-speed tests.', ''),
    ('sensitivity-converter.html', '🔁', 'Sensitivity Converter', 'Move your exact aim between 10 games + cm/360.', 'Popular'),
    ('tools.html#crosshair', '✛', 'Crosshair Generator', 'Design, preview and save your crosshair.', ''),
    ('tools.html#mouse', '🖲️', 'Mouse Tests', 'DPI analyzer, polling-rate & double-click tester.', ''),
    ('tools.html#edpi', '🧮', 'eDPI & cm/360', 'Compare your sensitivity across setups.', ''),
    ('aiming-off.html', '🧭', 'Aiming-Off Calculator', 'The navigator’s trick for never missing a target.', 'Unique'),
]

def tool_cards(items):
    return ''.join(f'<a class="card link reveal" href="{{R}}{h}"><div class="ico">{i}</div>{f"<span class=tag>{t}</span>" if t else ""}<h3>{n}</h3><p class="muted small" style="margin:0">{d}</p></a>' for h, i, n, d, t in items)

HOME_FAQ = [
    ('Is AimOff free?', 'Yes. Every trainer, test and tool on AimOff is free and runs in your browser — no download, no account. Ads and sponsors keep it that way.'),
    ('Does a browser aim trainer actually help?', 'Yes, for the fundamentals. Flicking, tracking, target switching and click timing all carry over between games. Train 10–20 minutes a day before you play; consistency beats long sessions.'),
    ('What does "aim off" mean?', 'In navigation, aiming off means deliberately aiming slightly to one side of a target so you know which way to turn when you reach a line feature such as a stream or fence. In target sports it means aiming to one side to allow for wind or movement. AimOff is built around that idea: smart aim beats lucky aim.'),
    ('How do I convert my sensitivity between games?', 'Use our Sensitivity Converter: choose your current game, sensitivity and DPI, then pick the target game. We keep your exact cm/360, so the same hand movement turns you the same distance.'),
    ('Can I win prizes?', 'Yes. The monthly AimOff Open is a free-to-enter skill contest. Prizes are funded by sponsors and supporters. See the Contests page for rules.'),
]

INDEX = f'''<section class="hero"><div class="container hero-grid">
<div><span class="eyebrow">Free · Browser-based · No download</span>
<h1>Train your aim. <span style="color:var(--accent)">Measure everything.</span></h1>
<p class="lead">AimOff is a free aim-training gym: a 5-mode aim trainer, reaction and click-speed tests, a sensitivity converter for 10 games, crosshair and mouse tools, and coach-written guides. Warm up in 60 seconds, track your progress, and enter monthly contests for prizes.</p>
<div class="hero-actions"><a class="btn btn-primary" href="{{R}}train.html">▶ Start aim training</a><a class="btn btn-secondary" href="{{R}}reaction-test.html">Test reaction time</a></div>
<div class="stats"><div><b>5</b>trainer modes</div><div><b>10+</b>games supported</div><div><b>72</b>conversion guides</div><div><b>$0</b>forever</div></div></div>
<div class="hero-visual">{HERO_SVG}</div></div></section>
<section class="section" style="padding-top:8px"><div class="container"><div class="marquee">
<span>Valorant</span><span>Counter-Strike 2</span><span>Apex Legends</span><span>Fortnite</span><span>Overwatch 2</span><span>Call of Duty</span><span>TF2</span><span>Titanfall 2</span><span>Quake Champions</span></div>
<p class="center muted small mt">Compatible settings tools for these games. Not affiliated with any publisher.</p></div></section>
<section class="section alt"><div class="container"><div class="center mb"><h2>Everything you need to aim better</h2><p class="muted">Pick a tool. Each one saves your personal best on this device.</p></div>
<div class="grid g4">{tool_cards(TOOLS)}</div>{AD}</div></section>
<section class="section"><div class="container split">
<div class="reveal"><span class="eyebrow">How it works</span><h2>A 3-step routine top players use</h2>
<ol class="prose"><li><b>Set your sensitivity once.</b> Convert it to cm/360 and keep it the same in every game.</li>
<li><b>Warm up 10 minutes a day.</b> 2 min Gridshot → 3 min Tracking → 3 min Flick → 2 min Precision.</li>
<li><b>Measure weekly.</b> Run a 60-second benchmark each Sunday and watch your personal bests climb.</li></ol>
<a class="btn btn-primary" href="{{R}}guides.html#warmup">Get the full warm-up routine</a></div>
<div class="card reveal"><h3>This week’s challenge</h3><p class="muted">Score <b>75+</b> in 60-second Gridshot (Platinum tier) to qualify for the monthly AimOff Open shortlist.</p>
<div class="bar"><i style="width:62%"></i></div><p class="small muted mt">Entries are open all month. Prizes are funded by sponsors and supporters.</p>
<div style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn btn-gold btn-sm" href="{{R}}contests.html">View contest & prizes</a><a class="btn btn-secondary btn-sm" href="{{R}}train.html?mode=gridshot">Play Gridshot</a></div></div>
</div></section>
{LEAD_BLOCK}
<section class="section alt"><div class="container"><div class="center mb"><h2>Learn the skill, not just the drill</h2></div>
<div class="grid g3">
<a class="card link reveal" href="{{R}}guides.html#pillars"><span class="tag">Guide</span><h3>The 4 pillars of aim</h3><p class="muted small">Flicking, tracking, switching and micro-adjusting, and how to train each one.</p></a>
<a class="card link reveal" href="{{R}}guides.html#sensitivity"><span class="tag">Guide</span><h3>How to find your perfect sensitivity</h3><p class="muted small">cm/360 ranges by game and play style, plus a 3-step tuning method.</p></a>
<a class="card link reveal" href="{{R}}aiming-off.html"><span class="tag hot">Signature</span><h3>Aiming off: the navigator’s trick</h3><p class="muted small">Why aiming slightly to one side gets you to the target faster.</p></a>
<a class="card link reveal" href="{{R}}guides.html#crosshair-placement"><span class="tag">Guide</span><h3>Crosshair placement</h3><p class="muted small">Head height, pre-aiming angles and why less flicking means more kills.</p></a>
<a class="card link reveal" href="{{R}}guides.html#darts"><span class="tag">Beyond gaming</span><h3>Darts & archery aiming basics</h3><p class="muted small">Dominant eye, stance, release, and the same consistency principles.</p></a>
<a class="card link reveal" href="{{R}}videos.html"><span class="tag">Watch</span><h3>Video library</h3><p class="muted small">Hand-picked aim and navigation tutorials from creators worth following.</p></a>
</div>{AD}</div></section>
<section class="section"><div class="container grid g3">
<div class="card reveal"><div class="ico">🏆</div><h3>Monthly contests</h3><p class="muted">Free-entry skill contests with prizes from sponsors and supporters.</p><a href="{{R}}contests.html">Enter now →</a></div>
<div class="card reveal"><div class="ico">🤝</div><h3>Sponsor or advertise</h3><p class="muted">Reach players who train every day. Tool, contest and video sponsorships.</p><a href="{{R}}advertise.html">See packages →</a></div>
<div class="card reveal"><div class="ico">❤</div><h3>Support AimOff</h3><p class="muted">Donations fund servers, prize pools, marketing and new creators.</p><a href="{{R}}support.html">Chip in →</a></div>
</div></section>
<section class="section alt"><div class="container" style="max-width:860px"><h2 class="center">FAQ</h2>{faq_html(HOME_FAQ)}</div></section>'''

TRAIN = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Free aim trainer · no download</span>
<h1>Aim Trainer</h1><p>Five drills that build the core aiming skills used in every shooter: speed (Gridshot), snapping (Flick), smoothness (Tracking), reaction (Reflex) and control (Precision). Press <kbd>Space</kbd> to start and <kbd>Esc</kbd> to stop.</p></div></section>
<section><div class="container layout"><div>
<div class="tool">
<div class="toolbar">
<div class="seg" id="seg-mode"><button class="on" data-v="gridshot">Gridshot</button><button data-v="flick">Flick</button><button data-v="tracking">Tracking</button><button data-v="reflex">Reflex</button><button data-v="precision">Precision</button></div>
<div class="seg" id="seg-dur"><button data-v="30">30s</button><button class="on" data-v="60">60s</button></div>
<div class="seg" id="seg-size"><button data-v="0.75">S</button><button class="on" data-v="1">M</button><button data-v="1.3">L</button></div>
<label class="small" style="display:flex;align-items:center;gap:6px;margin:0">Crosshair <input id="xhair" type="color" value="#22e3c4" style="width:44px;padding:2px;height:34px"></label>
</div>
<div class="arena"><canvas id="arena" aria-label="Aim trainer arena"></canvas><div class="overlay" id="overlay"></div></div>
<div class="hud"><div><b id="h-score">0</b><span>Score</span></div><div><b id="h-time">0.0</b><span>Time left</span></div><div><b id="h-hits">0</b><span>Hits</span></div><div><b id="h-acc">0%</b><span>Accuracy</span></div><div><b id="h-pb">0</b><span>Personal best</span></div></div>
</div>
{AD}
<h2>Your personal bests</h2><div class="hud" id="pbs"></div>
<h3>Recent sessions</h3><div class="table-wrap"><table><thead><tr><th>Mode</th><th>Score</th><th>Accuracy</th><th>Length</th><th>Date</th></tr></thead><tbody id="history"></tbody></table></div>
<div class="prose mt">
<h2>How each mode trains you</h2>
<ul><li><b>Gridshot</b> builds raw speed and target acquisition: three targets on a grid, cleared as fast as you can.</li>
<li><b>Flick</b> trains fast, accurate snaps to a single random target. Watch your average time-to-kill drop.</li>
<li><b>Tracking</b> trains smooth, continuous aim on a target that changes direction. It is scored by the share of time your crosshair stays on it.</li>
<li><b>Reflex</b> combines reaction and precision: targets shrink and disappear if you are too slow.</li>
<li><b>Precision</b> uses tiny targets that punish overflicking. Slow down and be accurate first.</li></ul>
<h2>Tiers</h2><p>Every run is ranked from <b>Rookie → Bronze → Silver → Gold → Platinum → Diamond → Master → Legend</b>. Scores are normalised to a 60-second run, so 30s and 60s results are comparable.</p>
<div class="callout">Tip: browser trainers use your desktop cursor, so turn off Windows “Enhance pointer precision” for consistent results. See <a href="{{R}}guides.html#setup">setup guide</a>.</div>
</div></div>
<aside class="sidebar"><div class="card"><h3>Enter the AimOff Open</h3><p class="muted small">Post your best 60s Gridshot score and you could win this month’s prize.</p><a class="btn btn-gold btn-block" href="{{R}}contests.html">Contest details</a></div>
<div class="ad-slot" data-slot="" style="min-height:250px">Advertisement</div>
<div class="card"><h3>Plateaued?</h3><p class="muted small">Get a free coach review of your scores and setup.</p><a class="btn btn-primary btn-block" href="{{R}}coaching.html">Free assessment</a></div></aside>
</div></section>
{LEAD_BLOCK}'''

REACT_FAQ = [
    ('What is a good reaction time?', 'For a visual click test the average human score is roughly 250–280 ms. Under 200 ms is excellent and typical of trained competitive players; under 150 ms usually means you anticipated the signal.'),
    ('Why is my score different on another device?', 'Monitor refresh rate, input lag, mouse polling rate and browser load all add milliseconds. A 60 Hz screen can add up to ~16 ms compared with 240 Hz.'),
    ('Can I improve my reaction time?', 'Partly. Sleep, warm-ups, caffeine timing and hardware improvements help, and practice reduces decision time in games. Pure visual reaction has a biological floor around 100–150 ms.'),
]
REACT = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Human-benchmark style test</span><h1>Reaction Time Test</h1>
<p>Click (or press <kbd>Space</kbd>) the moment the box turns green. We average 5 attempts, then show your percentile and tier.</p></div></section>
<section><div class="container layout"><div>
<div class="tool"><div id="react-pad" class="react-pad idle" role="button" tabindex="0">Click to start<span class="small" style="font-family:var(--font);font-weight:500">Wait for green, then click as fast as you can</span></div>
<div class="hud"><div><b id="react-pb">—</b><span>Best average</span></div><div style="flex:1"><b id="react-runs" style="font-size:1rem">—</b><span>Last 5 attempts</span></div></div>
<button class="btn btn-secondary btn-sm" id="react-share">Share my result</button> <a class="btn btn-gold btn-sm" href="{{R}}contests.html?mode=reaction#enter">Submit to contest</a></div>
{AD}
<div class="prose"><h2>Reaction time benchmarks</h2>
<div class="table-wrap"><table><thead><tr><th>Average</th><th>Tier</th><th>What it means</th></tr></thead><tbody>
<tr><td>&lt; 180 ms</td><td>Superhuman</td><td>Exceptional, or you are anticipating</td></tr><tr><td>180–210 ms</td><td>Pro-level</td><td>Typical of trained esports players</td></tr>
<tr><td>210–240 ms</td><td>Elite</td><td>Very fast</td></tr><tr><td>240–280 ms</td><td>Above average</td><td>Better than most people</td></tr><tr><td>280–330 ms</td><td>Average</td><td>Normal human range</td></tr><tr><td>&gt; 330 ms</td><td>Warming up</td><td>Check your setup, sleep and focus</td></tr></tbody></table></div>
<h2>How to get a faster score</h2><ul><li>Use a wired mouse and the highest refresh rate your monitor supports.</li><li>Close heavy browser tabs. Background load adds jitter.</li><li>Rest your finger lightly on the button, and focus on the centre of the box rather than the edges.</li><li>Warm up with 2 minutes of <a href="{{R}}train.html?mode=reflex">Reflex mode</a>.</li></ul>
<h2>FAQ</h2>{faq_html(REACT_FAQ)}</div></div>
<aside class="sidebar"><div class="ad-slot" data-slot="" style="min-height:250px">Advertisement</div><div class="card"><h3>Next test</h3><a class="btn btn-primary btn-block" href="{{R}}cps-test.html">CPS Test →</a><a class="btn btn-secondary btn-block mt" href="{{R}}train.html">Aim Trainer →</a></div></aside>
</div></section>'''

CPS_FAQ = [
    ('What is a good CPS?', 'Most people click 6–7 times per second with normal clicking. 8–10 CPS is fast, and jitter or butterfly techniques can reach 12–20+ CPS.'),
    ('What is jitter clicking?', 'Tensing the forearm so the finger vibrates on the button, producing very fast clicks. Do it in short bursts and stop if you feel pain.'),
    ('What is butterfly clicking?', 'Alternating two fingers on the same button. It produces high CPS, but some game servers limit or flag very high click rates.'),
]
CPS = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Click speed test</span><h1>CPS Test</h1>
<p>How many clicks per second can you do? Choose a duration, then click the pad (or tap, or press <kbd>Space</kbd>) as fast as you can.</p></div></section>
<section><div class="container layout"><div><div class="tool">
<div class="toolbar"><div class="seg" id="cps-dur"><button data-v="1">1s</button><button class="on" data-v="5">5s</button><button data-v="10">10s</button><button data-v="30">30s</button><button data-v="60">60s</button></div></div>
<div id="cps-pad" class="react-pad idle" role="button" tabindex="0"></div>
<div class="hud"><div><b id="cps-live">0.0</b><span>Live CPS</span></div><div><b id="cps-count">0</b><span>Clicks</span></div><div><b id="cps-time">5.0</b><span>Time left</span></div><div><b id="cps-pb">0.00</b><span>Best CPS</span></div></div>
<button class="btn btn-secondary btn-sm" id="cps-share">Share my CPS</button></div>
{AD}
<div class="prose"><h2>CPS ranks</h2><div class="table-wrap"><table><thead><tr><th>CPS</th><th>Rank</th></tr></thead><tbody>
<tr><td>&lt;3</td><td>Sloth</td></tr><tr><td>3–5</td><td>Turtle</td></tr><tr><td>5–7</td><td>Rabbit</td></tr><tr><td>7–9</td><td>Cheetah</td></tr><tr><td>9–11</td><td>Falcon</td></tr><tr><td>11–14</td><td>Jitter Machine</td></tr><tr><td>14+</td><td>Butterfly God</td></tr></tbody></table></div>
<h2>Clicking techniques</h2><p><b>Regular clicking:</b> 6–8 CPS, sustainable. <b>Jitter clicking:</b> 10–14 CPS in bursts. <b>Butterfly clicking:</b> 12–20+ CPS with two fingers. <b>Drag clicking:</b> uses friction on the button, can exceed 20 CPS, and depends on the mouse.</p>
<div class="callout">Health note: stop and rest if you feel wrist or forearm pain. Fast clicking in short bursts is fine; grinding it for hours is not.</div>
<h2>FAQ</h2>{faq_html(CPS_FAQ)}</div></div>
<aside class="sidebar"><div class="ad-slot" data-slot="" style="min-height:250px">Advertisement</div><div class="card"><h3>Your mouse matters</h3><p class="muted small">Check polling rate and double-click faults.</p><a class="btn btn-primary btn-block" href="{{R}}tools.html#mouse">Mouse tests →</a></div></aside>
</div></section>'''

GAMES = {
    'cs2': ('Counter-Strike 2', 0.022), 'valorant': ('Valorant', 0.07), 'apex': ('Apex Legends', 0.022), 'overwatch2': ('Overwatch 2', 0.0066),
    'cod': ('Call of Duty', 0.0066), 'fortnite': ('Fortnite', 0.005555), 'tf2': ('Team Fortress 2', 0.022), 'titanfall2': ('Titanfall 2', 0.022),
    'quake': ('Quake Champions', 0.022), 'csgo': ('CS:GO', 0.022),
}

def converter_widget(frm='cs2', to='valorant'):
    return f'''<div class="tool" id="conv" data-from="{frm}" data-to="{to}">
<div class="grid g2"><div><h3>From</h3>
<div class="field"><label for="from-game">Game</label><select id="from-game"></select></div>
<div class="field" id="from-yaw-wrap" hidden><label for="from-yaw">Custom yaw (°/count)</label><input id="from-yaw" type="number" step="any" value="0.022"></div>
<div class="row"><div class="field"><label for="from-sens">Sensitivity</label><input id="from-sens" type="number" step="any" value="1.2"></div>
<div class="field"><label for="from-dpi">DPI</label><input id="from-dpi" type="number" value="800"></div></div></div>
<div><h3>To <button class="btn btn-secondary btn-sm" id="swap" type="button" style="float:right">⇄ Swap</button></h3>
<div class="field"><label for="to-game">Game</label><select id="to-game"></select></div>
<div class="field" id="to-yaw-wrap" hidden><label for="to-yaw">Custom yaw (°/count)</label><input id="to-yaw" type="number" step="any" value="0.022"></div>
<div class="field"><label for="to-dpi">DPI (leave equal unless changing mouse DPI)</label><input id="to-dpi" type="number" value="800"></div>
<div class="out"><span class="muted small">Your new sensitivity</span><br><b id="to-sens">—</b></div></div></div>
<div class="hud"><div><b id="o-cm">—</b><span>cm / 360°</span></div><div><b id="o-in">—</b><span>inches / 360°</span></div><div><b id="o-edpi">—</b><span>eDPI (source)</span></div><div><b id="o-mult">—</b><span>Multiplier</span></div></div>
<p class="muted small" id="o-style"></p>
<p class="small muted">Values use public hip-fire yaw constants (degrees per mouse count). Scoped/ADS multipliers differ per game, so check in-game. Fortnite uses the X/Y percentage scale.</p></div>'''

SENS_FAQ = [
    ('How does the sensitivity converter work?', 'Each game turns your view by a fixed angle per mouse count (its “yaw”), multiplied by your sensitivity. We match the degrees turned per centimetre of mouse movement between the two games, so your muscle memory transfers 1:1.'),
    ('What is cm/360?', 'The distance in centimetres you move your mouse to turn 360° in game. It is the only fully game-independent way to compare sensitivity.'),
    ('What is eDPI?', 'Effective DPI = in-game sensitivity × mouse DPI. It compares players in the same game only, because yaw differs between games.'),
    ('Does FOV change my sensitivity?', 'Hip-fire 360° distance does not change with FOV in most games, but how fast the screen appears to move does. For scoped aim, use the game’s ADS multiplier setting.'),
]
SENS = f'''<section class="page-hero"><div class="container"><span class="eyebrow">10 games · cm/360 accurate</span><h1>Sensitivity Converter</h1>
<p>Convert your mouse sensitivity between Valorant, CS2, Apex Legends, Overwatch 2, Call of Duty, Fortnite and more. It keeps your exact cm/360, so your aim feels identical.</p></div></section>
<section><div class="container layout"><div>{converter_widget()}{AD}
<div class="prose"><h2>Popular conversions</h2><div class="chips" style="margin-bottom:16px">''' + ''.join(
    f'<a class="tag" style="padding:8px 12px" href="{{R}}convert/{a}-to-{b}-sensitivity.html">{GAMES[a][0]} → {GAMES[b][0]}</a>'
    for a, b in [('cs2', 'valorant'), ('valorant', 'cs2'), ('apex', 'valorant'), ('valorant', 'apex'), ('fortnite', 'valorant'), ('valorant', 'fortnite'), ('overwatch2', 'valorant'),
                 ('cod', 'valorant'), ('cs2', 'apex'), ('apex', 'cod'), ('fortnite', 'cs2'), ('overwatch2', 'cs2')]) + f'''</div>
<p><a href="{{R}}convert/index.html">See all 72 game-to-game conversion pages →</a></p>
<h2>Typical cm/360 ranges</h2><div class="table-wrap"><table><thead><tr><th>Game type</th><th>Common range</th><th>Why</th></tr></thead><tbody>
<tr><td>Tactical shooters (Valorant, CS2)</td><td>35–60 cm</td><td>Precise one-taps; little need for 180° turns</td></tr>
<tr><td>Battle royale (Apex, Fortnite, Warzone)</td><td>25–40 cm</td><td>Mix of tracking and fast turns</td></tr>
<tr><td>Hero shooters (Overwatch 2)</td><td>20–35 cm</td><td>Fast movement and vertical fights</td></tr>
<tr><td>Arena (Quake)</td><td>25–45 cm</td><td>Heavy tracking at high speed</td></tr></tbody></table></div>
<p class="muted small">These are community-typical ranges, not rules. Find your own with the 3-step method in our <a href="{{R}}guides.html#sensitivity">sensitivity guide</a>.</p>
<h2>FAQ</h2>{faq_html(SENS_FAQ)}</div></div>
<aside class="sidebar"><div class="ad-slot" data-slot="" style="min-height:250px">Advertisement</div><div class="card"><h3>Test your new sens</h3><p class="muted small">Run 3 Tracking sessions to lock it in.</p><a class="btn btn-primary btn-block" href="{{R}}train.html?mode=tracking">Open trainer</a></div>
<div class="card"><h3>Gear brands</h3><p class="muted small">Sponsor this converter. It is one of our most-used tools.</p><a class="btn btn-secondary btn-block" href="{{R}}advertise.html">Sponsorship info</a></div></aside>
</div></section>'''

TOOLS_PAGE = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Free utilities</span><h1>Aim Tools</h1>
<p>Calculators and testers for dialling in your setup: eDPI, cm/360, FOV conversion, a crosshair generator, and mouse diagnostics (DPI analyzer, polling rate, double-click).</p>
<div class="chips"><a class="tag" href="#edpi">eDPI & cm/360</a><a class="tag" href="#fov">FOV</a><a class="tag" href="#crosshair">Crosshair</a><a class="tag" href="#mouse">Mouse tests</a></div></div></section>
<section><div class="container">
<h2 id="edpi">eDPI & cm/360 calculators</h2><div class="grid g2">
<form class="tool" id="edpi-form" onsubmit="return false"><h3>eDPI calculator</h3><div class="row"><div class="field"><label for="e-sens">In-game sensitivity</label><input id="e-sens" type="number" step="any" value="0.4"></div><div class="field"><label for="e-dpi">Mouse DPI</label><input id="e-dpi" type="number" value="800"></div></div><div class="out">eDPI: <b id="e-out">—</b></div></form>
<form class="tool" id="cm-form" onsubmit="return false"><h3>cm/360 calculator</h3><div class="field"><label for="cm-game">Game</label><select id="cm-game"></select></div><div class="row"><div class="field"><label for="cm-sens">Sensitivity</label><input id="cm-sens" type="number" step="any" value="1"></div><div class="field"><label for="cm-dpi">DPI</label><input id="cm-dpi" type="number" value="800"></div></div><div class="out"><b id="cm-out">—</b></div></form>
</div>{AD}
<h2 id="fov">FOV converter</h2><form class="tool" id="fov-form" onsubmit="return false"><div class="grid g3"><div class="field"><label for="fov-v">Vertical FOV (°)</label><input id="fov-v" type="number" step="any" value="73.74"></div><div class="field"><label for="fov-w">Aspect width</label><input id="fov-w" type="number" value="16"></div><div class="field"><label for="fov-h">Aspect height</label><input id="fov-h" type="number" value="9"></div></div><div class="out">Result: <b id="fov-out">—</b></div><p class="muted small">Formula: hFOV = 2·atan(tan(vFOV/2)·aspect). Use it to compare games that specify FOV differently.</p></form>
<h2 id="crosshair" class="mt">Crosshair generator</h2>
<div class="grid g2"><form class="tool" id="xh-form" onsubmit="return false">
<div class="row"><div class="field"><label for="xh-color">Colour</label><input id="xh-color" type="color" value="#00ff6a"></div><div class="field"><label for="xh-bg">Preview background</label><select id="xh-bg"><option value="#3a4a5c">Concrete</option><option value="#c9b38a">Sand</option><option value="#2c4a2a">Foliage</option><option value="#e8eefc">Sky</option><option value="#0b0f18">Night</option></select></div></div>
<div class="row"><div class="field"><label for="xh-len">Line length <span class="muted">(px)</span></label><input id="xh-len" type="range" min="0" max="12" value="4"></div><div class="field"><label for="xh-th">Thickness</label><input id="xh-th" type="range" min="1" max="5" value="2"></div></div>
<div class="field"><label for="xh-gap">Gap</label><input id="xh-gap" type="range" min="0" max="10" value="2"></div>
<div class="chips"><label class="check"><input type="checkbox" id="xh-dot"> Centre dot</label><label class="check"><input type="checkbox" id="xh-ol" checked> Outline</label><label class="check"><input type="checkbox" id="xh-t"> T-style</label></div>
<div class="field mt"><label for="xh-json">Your settings (save or share)</label><textarea id="xh-json" readonly style="min-height:70px"></textarea></div>
<button type="button" class="btn btn-secondary btn-sm" id="xh-rand">🎲 Randomize</button> <button type="button" class="btn btn-primary btn-sm" id="xh-copy">Copy settings</button></form>
<div class="tool"><canvas id="xh-canvas" width="480" height="320" style="width:100%;border-radius:12px"></canvas><p class="muted small">Preview at 4× zoom. Enter these values in your game’s crosshair menu. Pick a colour that contrasts with the map: green or cyan for most maps, magenta for foliage.</p></div></div>
{AD}
<h2 id="mouse" class="mt">Mouse tests</h2><div class="grid g3">
<div class="tool"><h3>Polling rate</h3><div id="poll-area" class="react-pad idle" style="aspect-ratio:4/3;font-size:1.1rem">Move your mouse in fast circles here</div><div class="hud"><div><b id="poll-out">0 Hz</b><span>Live</span></div><div><b id="poll-max">0 Hz</b><span>Peak</span></div></div><p class="muted small">Browsers can cap readings at your monitor refresh rate; Chromium browsers report the most accurate values.</p></div>
<div class="tool"><h3>DPI analyzer</h3><div class="row"><div class="field"><label for="dpi-dist">Distance</label><input id="dpi-dist" type="number" value="10"></div><div class="field"><label for="dpi-unit">Unit</label><select id="dpi-unit"><option value="cm">cm</option><option value="in">inches</option></select></div></div>
<div id="dpi-area" class="react-pad idle" style="aspect-ratio:4/2;font-size:1rem">Click to start, move the distance to the right, click again</div><div class="out"><b id="dpi-out">—</b></div></div>
<div class="tool"><h3>Double-click tester</h3><button id="dc-btn" class="react-pad idle" style="aspect-ratio:4/3;width:100%;border:0;font-size:1.1rem">Click here with left & right buttons</button><p class="small" id="dc-out">Clicks under 80 ms apart are flagged as possible switch chatter.</p></div>
</div></div></section>'''

def conv_values(a, b):
    na, ya = GAMES[a]; nb, yb = GAMES[b]
    m = ya / yb
    rows = ''.join(f'<tr><td>{s}</td><td>{s * m:.3f}</td><td>{360 / (ya * s * 800) * 2.54:.1f} cm</td></tr>' for s in ([0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.6, 0.8] if a == 'valorant' else [5, 6, 7, 8, 10, 12, 15] if a == 'fortnite' else [3, 4, 5, 6, 7, 8, 10, 12] if a in ('cod', 'overwatch2') else [0.8, 1, 1.2, 1.5, 1.8, 2, 2.5, 3, 4, 5]))
    return dict(a=a, b=b, na=na, nb=nb, ya=str(ya), yb=str(yb), m=f'{m:.4f}', rows=rows, nbplus=nb.replace(' ', '+'))

LIQUID = {k: '{{ page.%s }}' % k for k in ['a', 'b', 'na', 'nb', 'ya', 'yb', 'm', 'rows', 'nbplus']}

def conv_page(a, b, v=None):
    v = v or conv_values(a, b)
    a, b, na, nb, ya, yb, m, rows, nbplus = (v[k] for k in ['a', 'b', 'na', 'nb', 'ya', 'yb', 'm', 'rows', 'nbplus'])
    body = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Sensitivity conversion</span><h1>{na} to {nb} Sensitivity Converter</h1>
<p>Convert your {na} sensitivity to {nb} and keep the same cm/360. At equal DPI, multiply your {na} sensitivity by <b>{m}</b> to get your {nb} sensitivity.</p></div></section>
<section><div class="container layout"><div>{converter_widget(a, b)}{AD}
<div class="prose"><h2>{na} → {nb} quick table (800 DPI)</h2><div class="table-wrap"><table><thead><tr><th>{na} sens</th><th>{nb} sens</th><th>cm/360</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>How the {na} to {nb} conversion works</h2><p>{na} turns your view by {ya}° per mouse count at sensitivity 1; {nb} turns {yb}°. Dividing the two gives the multiplier {m}. If you change DPI as well, the converter above adjusts for it, so the physical distance per 360° stays identical.</p>
<h3>After converting</h3><ol><li>Set the new value in {nb} and turn off mouse acceleration.</li><li>Play 2–3 short sessions; small adjustments of ±5% are normal because FOV makes speed <i>feel</i> different.</li><li>Lock it in with 10 minutes of <a href="{{R}}train.html?mode=tracking">Tracking</a> and <a href="{{R}}train.html?mode=flick">Flick</a> drills.</li></ol>
<p class="muted small">Game names are trademarks of their owners; AimOff is not affiliated with them. Values are for hip-fire; verify scoped multipliers in-game.</p>
<p><a href="{{R}}convert/{b}-to-{a}-sensitivity.html">Reverse: {nb} → {na}</a> · <a href="{{R}}convert/index.html">All conversions</a></p></div></div>
<aside class="sidebar"><div class="ad-slot" data-slot="" style="min-height:250px">Advertisement</div><div class="card"><h3>Need a coach for {nb}?</h3><p class="muted small">Get a free assessment from a vetted coach.</p><a class="btn btn-primary btn-block" href="{{R}}coaching.html?game={nbplus}">Free assessment</a></div></aside>
</div></section>'''
    return dict(path=f'convert/{a}-to-{b}-sensitivity.html', title=f'{na} to {nb} Sensitivity Converter (cm/360 exact) | AimOff',
                desc=f'Convert {na} sensitivity to {nb} instantly. Multiplier {m} at equal DPI, quick table, cm/360 and eDPI. Free, accurate, no signup.',
                body=body, active='', scripts=['tools.js'], schema=tool_schema(f'{na} to {nb} sensitivity converter', f'convert/{a}-to-{b}-sensitivity.html', 'Free sensitivity converter'))

def conversion_pages():
    out = []
    keys = [k for k in GAMES if k != 'csgo']
    links = []
    for a in keys:
        for b in keys:
            if a != b:
                out.append(conv_page(a, b))
                links.append(f'<li><a href="{{R}}convert/{a}-to-{b}-sensitivity.html">{GAMES[a][0]} → {GAMES[b][0]}</a></li>')
    idx = f'''<section class="page-hero"><div class="container"><h1>All Sensitivity Conversions</h1><p>Every game-to-game conversion page, each with a quick table and the exact multiplier.</p></div></section>
<section><div class="container"><ul style="columns:3 240px;list-style:none;padding:0">{''.join(links)}</ul>{AD}</div></section>'''
    out.append(dict(path='convert/index.html', title='All Game Sensitivity Conversions | AimOff', desc='Index of 72 game-to-game mouse sensitivity conversions: Valorant, CS2, Apex, Overwatch 2, Call of Duty, Fortnite, TF2, Titanfall 2 and Quake.', body=idx))
    return out

PAGES = [
    dict(path='index.html', title='AimOff — Free Aim Trainer, Reaction Test, CPS Test & Sensitivity Converter',
         desc='Train your aim free in the browser: 5-mode aim trainer, reaction time test, CPS test, sensitivity converter for 10 games, crosshair & mouse tools, guides and monthly contests.',
         body=INDEX, schema=faq_schema(HOME_FAQ)),
    dict(path='train.html', title='Free Aim Trainer Online — Gridshot, Flick, Tracking, Reflex | AimOff',
         desc='Play a free browser aim trainer with 5 modes: Gridshot, Flick, Tracking, Reflex and Precision. Tiers, personal bests, history, and monthly contests. No download.',
         body=TRAIN, active='train.html', scripts=['trainer.js'], schema=tool_schema('AimOff Aim Trainer', 'train.html', 'Free 5-mode browser aim trainer')),
    dict(path='reaction-test.html', title='Reaction Time Test — Average, Percentile & Tier | AimOff',
         desc='Test your reaction time in milliseconds. 5-attempt average, percentile vs. the population, tier and tips to get faster. Free and instant.',
         body=REACT, scripts=['tools.js'], schema=faq_schema(REACT_FAQ) + tool_schema('Reaction Time Test', 'reaction-test.html', 'Free reaction time test')),
    dict(path='cps-test.html', title='CPS Test — Click Speed Test (1, 5, 10, 30, 60 Seconds) | AimOff',
         desc='Check your clicks per second with 1 to 60-second CPS tests. Live CPS, ranks from Sloth to Butterfly God, and jitter and butterfly clicking tips.',
         body=CPS, scripts=['tools.js'], schema=faq_schema(CPS_FAQ) + tool_schema('CPS Test', 'cps-test.html', 'Free click speed test')),
    dict(path='sensitivity-converter.html', title='Sensitivity Converter — Valorant, CS2, Apex, OW2, CoD, Fortnite | AimOff',
         desc='Convert mouse sensitivity between 10 games with exact cm/360. Includes eDPI, inches/360 and a multiplier. Valorant, CS2, Apex, Overwatch 2, Call of Duty, Fortnite and more.',
         body=SENS, scripts=['tools.js'], schema=faq_schema(SENS_FAQ) + tool_schema('Sensitivity Converter', 'sensitivity-converter.html', 'Game sensitivity converter')),
    dict(path='tools.html', title='Aim Tools — eDPI, cm/360, FOV, Crosshair Generator, Mouse Tests | AimOff',
         desc='Free aim tools: eDPI and cm/360 calculators, FOV converter, crosshair generator, DPI analyzer, polling rate tester and double-click tester.',
         body=TOOLS_PAGE, scripts=['tools.js']),
] + PAGES2
