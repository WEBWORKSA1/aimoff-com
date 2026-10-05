"""Page bodies for AimOff.com: content, lead-gen, community, legal."""
AD = '<div class="ad-slot" data-slot="">Advertisement</div>'
SIDE_AD = '<div class="ad-slot" data-slot="" style="min-height:250px">Advertisement</div>'
HP = '<input class="hp" name="_honey" tabindex="-1" autocomplete="off">'
GAME_OPTS = ''.join(f'<option>{g}</option>' for g in ['Valorant', 'Counter-Strike 2', 'Apex Legends', 'Fortnite', 'Overwatch 2', 'Call of Duty', 'Marvel Rivals', 'Rainbow Six Siege', 'Other'])

def faq(qas):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qas)

def faq_schema(qas):
    return [{'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qas]}]

# ---------------- GUIDES ----------------
GUIDES = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Aim academy</span><h1>Aim Guides</h1>
<p>Practical, no-fluff guides to aiming better in games and beyond, from sensitivity and crosshair placement to darts and archery fundamentals.</p></div></section>
<section><div class="container layout"><article class="prose">
<div class="toc"><b>On this page</b><a href="#pillars">1. The 4 pillars of aim</a><a href="#sensitivity">2. Finding your sensitivity</a><a href="#warmup">3. The 10-minute warm-up</a><a href="#crosshair-placement">4. Crosshair placement</a><a href="#setup">5. Setup & gear checklist</a><a href="#grip">6. Mouse grip styles</a><a href="#leading">7. Leading moving targets</a><a href="#darts">8. Darts aiming basics</a><a href="#archery">9. Archery aiming methods</a><a href="#eye">10. Dominant-eye test</a></div>

<h2 id="pillars">1. The 4 pillars of aim</h2>
<p>Almost every aiming situation breaks down into four skills. Train them separately, then together.</p>
<ul><li><b>Flicking:</b> a fast, ballistic movement to a target followed by a click. Train with <a href="{{R}}train.html?mode=flick">Flick</a> and <a href="{{R}}train.html?mode=gridshot">Gridshot</a>.</li>
<li><b>Tracking:</b> keeping the crosshair on a moving target. Train with <a href="{{R}}train.html?mode=tracking">Tracking</a>. Smoothness beats speed.</li>
<li><b>Target switching:</b> moving between several targets efficiently. Gridshot with three active targets trains choosing the nearest next target.</li>
<li><b>Micro-adjustment:</b> tiny corrections at the end of a flick. Train with <a href="{{R}}train.html?mode=precision">Precision</a>.</li></ul>
<div class="callout"><b>Rule of thumb:</b> accuracy first, then speed. If accuracy drops below about 85% in Gridshot, slow down until it recovers.</div>

<h2 id="sensitivity">2. Finding your sensitivity (3-step method)</h2>
<ol><li><b>Start from a range.</b> Tactical shooters: 35–60 cm/360. Battle royale: 25–40 cm. Hero shooters: 20–35 cm. Use the <a href="{{R}}sensitivity-converter.html">converter</a> to see where you are now.</li>
<li><b>Bracket it.</b> Play 3 Tracking runs at your sensitivity, at +15% and at −15%. Keep the one with the highest average score.</li>
<li><b>Freeze it for 3 weeks.</b> Constant changes reset your muscle memory. Change sensitivity only if your scores clearly plateau.</li></ol>
<p>Then convert that exact cm/360 into every game you play, so your hand learns one distance.</p>
{AD}
<h2 id="warmup">3. The 10-minute warm-up</h2>
<div class="table-wrap"><table><thead><tr><th>Minutes</th><th>Drill</th><th>Focus</th></tr></thead><tbody>
<tr><td>0–2</td><td>Gridshot 60s ×2</td><td>Get the hand moving, relaxed grip</td></tr><tr><td>2–5</td><td>Tracking 60s ×3</td><td>Smooth, no jerks</td></tr>
<tr><td>5–8</td><td>Flick 60s ×3</td><td>Commit to one motion, then correct</td></tr><tr><td>8–10</td><td>Precision 60s ×2</td><td>Slow down, 90%+ accuracy</td></tr></tbody></table></div>
<p>Log your Sunday 60-second scores. Most players see their personal bests rise for 4–8 weeks before the first plateau.</p>

<h2 id="crosshair-placement">4. Crosshair placement</h2>
<p>The best flick is the one you never need. Keep your crosshair at <b>head height</b> and on the <b>edge of the next angle</b> an enemy can appear from. When you clear corners, move the crosshair along the wall edge (“slicing the pie”) so targets appear right on it. Good placement turns aim duels into reaction tests, and you can train reaction too: <a href="{{R}}reaction-test.html">test it here</a>.</p>

<h2 id="setup">5. Setup & gear checklist</h2>
<ul><li>Turn off OS mouse acceleration (Windows: “Enhance pointer precision”).</li><li>Use 400–1600 DPI and set speed in-game rather than by pushing DPI very high.</li>
<li>Use a polling rate of 1000 Hz or more (<a href="{{R}}tools.html#mouse">test yours</a>).</li><li>Turn on the highest monitor refresh rate in your OS display settings. Many 144/240 Hz screens ship running at 60 Hz.</li>
<li>Use a large mousepad (at least 45 cm wide) for low sensitivity and a control surface for precision.</li><li>Lighter mice (about 50–70 g) reduce fatigue for flicking, though grip matters more than grams.</li></ul>

<h2 id="grip">6. Mouse grip styles</h2>
<p><b>Palm:</b> the whole hand rests on the mouse. Stable, good for tracking and low sensitivity. <b>Claw:</b> arched fingers with the palm touching the back. A balance of speed and control. <b>Fingertip:</b> only the fingertips touch. The fastest micro-adjustments, but less stable. Pick a mouse shape that fits your grip and hand length.</p>

<h2 id="leading">7. Leading moving targets</h2>
<p>When a projectile is slow or the target is far away, you must aim off: aim ahead of where the target is. The required lead is <i>target speed × projectile travel time</i>. In games with hitscan weapons there is no lead, but in games with projectiles (rockets, arrows, grenades) leading is the whole skill. Practise it in Tracking by aiming slightly ahead of the target’s direction of travel.</p>
{AD}
<h2 id="darts">8. Darts aiming basics</h2>
<ul><li><b>Stance:</b> lead foot forward and pointing at the board, weight mostly on the front foot. Keep the body still and let only the arm move.</li>
<li><b>Grip:</b> hold the dart with 2–4 fingers, firmly enough to control it but without tension.</li>
<li><b>Aim line:</b> line up your dominant eye, the dart and the target in one line.</li>
<li><b>Release & follow-through:</b> the same speed every throw, with the arm finishing pointed at the target.</li>
<li><b>Aiming off:</b> if a cluster lands consistently low-left, adjust your aim point rather than your throw. Fix the mechanics later in practice.</li></ul>

<h2 id="archery">9. Archery aiming methods</h2>
<ul><li><b>Sight aiming:</b> a pin or sight marks the aim point for each distance. The most precise method.</li>
<li><b>Gap shooting:</b> you learn the visual gap between arrow point and target at each distance.</li>
<li><b>Instinctive:</b> both eyes open, focused on the target, with the brain doing the maths. This takes lots of repetition.</li>
<li><b>String walking:</b> changing your hand position on the string to change the arrow’s angle.</li>
<li><b>Wind:</b> archers “aim off” into a crosswind by a consistent amount learned from practice groups.</li></ul>
<p class="muted small">Always follow your range’s safety rules and get coaching from a certified instructor.</p>

<h2 id="eye">10. Dominant-eye test (30 seconds)</h2>
<ol><li>Extend both arms and make a small triangle with your thumbs and forefingers.</li><li>With both eyes open, frame a distant object inside the triangle.</li><li>Close your left eye. If the object stays framed, your right eye is dominant. If it jumps out, your left eye is dominant.</li></ol>
<p>Line up targets with your dominant eye in darts, archery and real-world aiming. It also explains why some players prefer their crosshair slightly off-centre on a screen.</p>
</article>
<aside class="sidebar">{SIDE_AD}<div class="card"><h3>Get the 14-Day Aim Plan</h3><p class="muted small">This guide as a daily routine, emailed to you free.</p><button class="btn btn-primary btn-block" onclick="AIMOFF.openLeadModal()">Send it to me</button></div>
<div class="card"><h3>Want to write for AimOff?</h3><p class="muted small">We pay creators and coaches for guides and videos.</p><a class="btn btn-secondary btn-block" href="{{R}}careers.html">Join the team</a></div></aside>
</div></section>'''

# ---------------- AIMING OFF ----------------
AO_FAQ = [
    ('What is aiming off in orienteering?', 'Aiming off means deliberately setting your bearing a few degrees to one side of a target that sits on a line feature, such as a path junction on a stream. When you reach the line feature you know which way to turn, instead of guessing.'),
    ('How many degrees should I aim off?', 'More than your expected compass error. Most walkers and runners have ±3–7° of error, so 8–10° works well. The calculator shows the sideways offset this creates over your leg distance.'),
    ('Is aiming off the same as an attack point?', 'No. An attack point is an easy-to-find feature near the control that you navigate to first. A catching feature stops you if you overshoot. Aiming off works with a line feature you know you will hit.'),
    ('Does aiming off apply to shooting and archery?', 'The phrase is also used for deliberately aiming to one side of a target to allow for wind or for a moving target. The principle is the same: plan for error instead of hoping it will not happen.'),
]
AIMING_OFF = f'''<section class="page-hero"><div class="container"><span class="eyebrow">The idea behind our name</span><h1>Aiming Off: Hit the Target by Aiming to One Side</h1>
<p>Aiming off is a classic navigation technique. You deliberately aim slightly to one side of your target, so that when you hit a line feature you know exactly which way to turn. It is the best example of a principle that runs through all of AimOff: <b>smart aim beats lucky aim.</b></p></div></section>
<section><div class="container layout"><article class="prose">
<figure class="card" style="margin:0 0 20px"><svg viewBox="0 0 640 300" width="100%" role="img" aria-label="Diagram showing aiming off to one side of a target on a river">
<rect width="640" height="300" fill="none"/><path d="M20 70 C 160 40, 300 100, 420 60 S 620 70, 630 50" stroke="#3aa0ff" stroke-width="10" fill="none" stroke-linecap="round"/>
<text x="500" y="40" fill="#3aa0ff" font-size="16" font-family="Inter">River (line feature)</text>
<circle cx="330" cy="82" r="13" fill="none" stroke="#ff4d6d" stroke-width="4"/><text x="300" y="120" fill="#ff4d6d" font-size="15" font-family="Inter">Target (bridge)</text>
<circle cx="320" cy="270" r="8" fill="#22e3c4"/><text x="335" y="276" fill="#22e3c4" font-size="15" font-family="Inter">You</text>
<line x1="320" y1="270" x2="330" y2="95" stroke="#93a1bf" stroke-dasharray="6 6" stroke-width="2"/>
<line x1="320" y1="270" x2="250" y2="78" stroke="#22e3c4" stroke-width="3"/>
<path d="M250 78 C 280 84, 300 86, 316 84" stroke="#ffc145" stroke-width="3" fill="none" marker-end="url(#a)"/>
<defs><marker id="a" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#ffc145"/></marker></defs>
<path d="M300 210 L 270 85 M 340 210 L 380 85" stroke="#93a1bf" stroke-opacity=".35" stroke-width="1.5"/>
<text x="20" y="200" fill="#93a1bf" font-size="14" font-family="Inter">Dashed = direct bearing. Error cone means you</text><text x="20" y="218" fill="#93a1bf" font-size="14" font-family="Inter">might hit the river left OR right of the bridge.</text>
<text x="20" y="250" fill="#22e3c4" font-size="14" font-family="Inter">Solid = aim off left → you KNOW to turn right.</text></svg></figure>

<h2>Why it works</h2><p>No compass bearing is perfect. Over 500 m, a 5° error puts you about 44 m left <i>or</i> right of the target, and on arrival you do not know which. By aiming off by more than your error, say 10°, you guarantee you hit the line feature on one known side. Then you follow it (a “handrail”) straight to the target.</p>

<h2>Aiming-off calculator</h2>
<form class="tool" id="ao-form" onsubmit="return false"><div class="grid g3">
<div class="field"><label for="ao-dist">Leg distance (m)</label><input id="ao-dist" type="number" value="500"></div>
<div class="field"><label for="ao-ang">Aim-off angle (°)</label><input id="ao-ang" type="number" value="10"></div>
<div class="field"><label for="ao-err">Expected bearing error (± °)</label><input id="ao-err" type="number" value="5"></div></div>
<div class="hud"><div><b id="ao-off">—</b><span>Sideways offset at the line</span></div><div><b id="ao-cone">—</b><span>Uncertainty without aiming off</span></div></div>
<p id="ao-verdict" class="small"></p><p class="muted small">Offset = distance × tan(angle). Pace-count the offset back along the line feature.</p></form>

<h2>Step by step</h2><ol><li>Identify a <b>line feature</b> that runs across your route and passes through or near the target: a stream, wall, fence, path or ridge.</li>
<li>Take the direct bearing, then <b>add or subtract 8–10°</b> towards the side that gives the easiest or safest walk.</li>
<li>Travel on the new bearing, counting paces.</li><li>When you hit the line feature, <b>turn towards the target</b>. You already know the direction.</li><li>Follow the line feature, using a <b>catching feature</b> beyond the target as a backstop.</li></ol>

<h2>Common mistakes</h2><ul><li>Aiming off by less than your error, which brings back the 50/50 guess.</li><li>Choosing a line feature that bends sharply near the target.</li><li>Forgetting that the offset grows with distance. Re-check it with the calculator.</li><li>Not having a catching feature, so you walk straight past the target along the line.</li></ul>
{AD}
<h2>Related techniques</h2><div class="grid g3"><div class="card"><h3>Handrails</h3><p class="muted small">Linear features you follow, such as paths, streams and fences.</p></div><div class="card"><h3>Attack points</h3><p class="muted small">An obvious feature near the control to navigate from precisely.</p></div><div class="card"><h3>Catching features</h3><p class="muted small">Something beyond the target that tells you that you have overshot.</p></div></div>

<h2>Watch: aiming off explained</h2><div class="grid g2"><div class="yt" data-id="PbIoD1gzyeg" data-title="Orienteering Techniques: Aiming Off"></div><div class="yt" data-id="oneUIiYkwHg" data-title="Aiming Off — Think Fast, Run Hard, Go Orienteering"></div></div>
<p class="muted small">Videos are embedded through YouTube and belong to their creators.</p>

<h2>Aiming off beyond navigation</h2><p>In target sports, “aiming off” means holding to one side of the mark to allow for wind or a moving target. In games, it is <a href="{{R}}guides.html#leading">leading</a> a target with a projectile weapon. The mindset is the same: <b>expect error, then put it where it helps you.</b></p>
<h2>FAQ</h2>{faq(AO_FAQ)}
</article><aside class="sidebar">{SIDE_AD}<div class="card"><h3>Outdoor & navigation brands</h3><p class="muted small">Sponsor this guide, which ranks for navigation-skills searches.</p><a class="btn btn-secondary btn-block" href="{{R}}advertise.html">Sponsor</a></div>
<div class="card"><h3>Clubs & instructors</h3><p class="muted small">Get listed and receive student enquiries.</p><a class="btn btn-primary btn-block" href="{{R}}coaching.html#partners">List your club</a></div></aside>
</div></section>'''

# ---------------- VIDEOS ----------------
VIDS = [
    ('Aim fundamentals', [('__yon0pWnxc', 'How to Improve at FPS Aiming (EP01)'), ('GMZ1kD1edgE', 'How to Master Your Aim in FPS Games'), ('ZOgniZrFsQ8', '5 Quick Tips to Improve Your Aim in Any FPS'), ('FpILIqeyZ1Y', '10 FPS Aim Tips in 9 Minutes'), ('jPZXbW4wz_A', '5 Quick Tips to Improve Your Aim at Any FPS'), ('I-ocJ0BxecU', 'A Trick to Improve Your Aim in Any FPS')]),
    ('Navigation: aiming off & handrails', [('PbIoD1gzyeg', 'Orienteering Techniques: Aiming Off'), ('P8ng2nXrWmA', 'Orienteering Techniques: Aiming Off'), ('kOXhT1uEgM0', 'Aiming Off When Navigating'), ('1teTcMsXFnQ', 'Orienteering Techniques: Handrails')]),
]
VIDEOS = '''<section class="page-hero"><div class="container"><span class="eyebrow">Watch & learn</span><h1>Video Library</h1>
<p>Hand-picked tutorials on aim, settings and navigation. Videos load only when you click, so the page stays fast. Creators: want to be featured or partner on a series? <a href="{R}advertise.html#creators">Get in touch</a>.</p></div></section>
<section><div class="container">''' + ''.join(
    f'<h2 class="mt">{cat}</h2><div class="grid g3">' + ''.join(f'<div><div class="yt" data-id="{i}" data-title="{t}"></div><p class="small mt">{t}</p></div>' for i, t in vs) + '</div>' + AD
    for cat, vs in VIDS) + '''<div class="card mt"><h3>📺 AimOff on YouTube</h3><p class="muted">Our own channel will publish weekly drills, contest highlights and settings breakdowns. Subscribe through the newsletter to be notified at launch, and to monetise the channel through the YouTube Partner Program.</p></div>
<p class="muted small mt">All videos are embedded through YouTube’s official player (privacy-enhanced mode) and remain the property of their creators. Inclusion does not imply endorsement either way.</p></div></section>'''

# ---------------- COACHING (dedicated lead generation) ----------------
COACH_FAQ = [
    ('Is the assessment really free?', 'Yes. You get a written review and a 3-point improvement plan at no cost and with no obligation to buy anything.'),
    ('How are coaches vetted?', 'Coaches apply through AimOff with proof of rank or competitive history and teaching experience, then complete a trial assessment we review.'),
    ('How much does coaching cost?', 'Coaches set their own prices. Typical market rates are around US$20–60 per hour, and packages are discounted. You see the price before you book.'),
    ('Which games are covered?', 'Valorant, Counter-Strike 2, Apex Legends, Fortnite, Overwatch 2, Call of Duty, Marvel Rivals and Rainbow Six Siege, with others on request.'),
]
COACHING = f'''<section class="hero"><div class="container hero-grid"><div>
<span class="eyebrow">Free aim assessment · 48-hour turnaround</span><h1>Rank up faster with a <span style="color:var(--accent)">vetted aim coach</span></h1>
<p class="lead">Tell us where you are stuck. A coach reviews your AimOff scores, sensitivity and setup, then sends you a personalised 3-point fix plan free. Book paid sessions only if you want them.</p>
<ul class="checks"><li>Free written assessment, with no card required</li><li>Matched by game, role, region and budget</li><li>Coaches for 8+ competitive shooters</li><li>Your details are never sold or shared outside your coach match</li></ul>
<div class="stats"><div><b>2 min</b>to apply</div><div><b>48 h</b>assessment</div><div><b>$0</b>to start</div></div></div>

<form class="card js-form" id="assess" data-steps data-subject="LEAD: Coaching assessment request" data-success="You're matched! Expect your free assessment by email within 48 hours.">{HP}
<input type="hidden" name="form" value="coaching-assessment">
<div class="steps"><span></span><span></span><span></span></div>
<div class="step"><h3>1 · Your game</h3>
<div class="field"><label for="c-game">Main game</label><select id="c-game" name="game" required><option value="">Choose…</option>{GAME_OPTS}</select></div>
<div class="row"><div class="field"><label for="c-rank">Current rank</label><input id="c-rank" name="rank" placeholder="e.g. Platinum 1" required></div><div class="field"><label for="c-goal">Goal rank</label><input id="c-goal" name="goal" placeholder="e.g. Diamond"></div></div>
<div class="field"><label>Biggest weakness</label><div class="chips">{''.join(f'<label><input type="checkbox" name="weakness" value="{w}"><span>{w}</span></label>' for w in ['Flicks', 'Tracking', 'Crosshair placement', 'Game sense', 'Consistency', 'Nerves / clutch'])}</div></div>
<button class="btn btn-primary btn-block" type="button" data-next>Next →</button></div>
<div class="step"><h3>2 · Your plan</h3>
<div class="row"><div class="field"><label for="c-region">Region</label><select id="c-region" name="region"><option>North America</option><option>Europe</option><option>Asia</option><option>Oceania</option><option>South America</option><option>Middle East / Africa</option></select></div>
<div class="field"><label for="c-budget">Budget per month</label><select id="c-budget" name="budget"><option>Free assessment only</option><option>Under $50</option><option>$50–150</option><option>$150–300</option><option>$300+</option></select></div></div>
<div class="field"><label for="c-avail">Availability</label><select id="c-avail" name="availability"><option>Weekday evenings</option><option>Weekends</option><option>Flexible</option></select></div>
<div class="field"><label for="c-notes">Anything else? (scores, sens, goals)</label><textarea id="c-notes" name="notes" placeholder="e.g. Gridshot 68, 0.35 sens at 800 DPI, want to hit Immortal by season end"></textarea></div>
<div style="display:flex;gap:8px"><button class="btn btn-secondary" type="button" data-prev>← Back</button><button class="btn btn-primary" style="flex:1" type="button" data-next>Next →</button></div></div>
<div class="step"><h3>3 · Where to send it</h3>
<div class="row"><div class="field"><label for="c-name">Name</label><input id="c-name" name="name" required></div><div class="field"><label for="c-email">Email</label><input id="c-email" type="email" name="email" required></div></div>
<div class="field"><label for="c-discord">Discord (optional)</label><input id="c-discord" name="discord" placeholder="username"></div>
<label class="check"><input type="checkbox" name="age_ok" value="yes" required> I am 16+ or have a parent/guardian’s permission.</label>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my assessment and coaching offers.</label>
<div style="display:flex;gap:8px" class="mt"><button class="btn btn-secondary" type="button" data-prev>← Back</button><button class="btn btn-primary" style="flex:1" type="submit">Get my free assessment</button></div>
<div class="form-msg" role="status"></div></div></form>
</div></section>
<section class="section alt"><div class="container"><h2 class="center">How it works</h2><div class="grid g4 mt">
<div class="card"><div class="ico">1</div><h3>Apply</h3><p class="muted small">Two minutes. Tell us your game, rank and goal.</p></div>
<div class="card"><div class="ico">2</div><h3>Get matched</h3><p class="muted small">We pick a coach for your game, role and region.</p></div>
<div class="card"><div class="ico">3</div><h3>Free assessment</h3><p class="muted small">You receive a written 3-point fix plan within 48 hours.</p></div>
<div class="card"><div class="ico">4</div><h3>Level up</h3><p class="muted small">Book sessions if you like, or train solo with AimOff.</p></div></div></div></section>
<section class="section"><div class="container grid g3">
<div class="card" id="become-coach"><h3>🎓 Become an AimOff coach</h3><p class="muted small">Get paid student leads. Proof of rank or competitive history required.</p>
<form class="js-form" data-subject="Coach application" data-success="Application received. We’ll be in touch within a week.">{HP}<input type="hidden" name="form" value="coach-application">
<div class="field"><input name="name" placeholder="Name / handle" required aria-label="Name"></div><div class="field"><input type="email" name="email" placeholder="Email" required aria-label="Email"></div>
<div class="field"><select name="game" aria-label="Game">{GAME_OPTS}</select></div><div class="field"><input name="proof" placeholder="Peak rank + profile link" required aria-label="Peak rank"></div>
<div class="field"><input name="rate" placeholder="Hourly rate (USD)" aria-label="Rate"></div><button class="btn btn-primary btn-block" type="submit">Apply to coach</button><div class="form-msg"></div></form></div>
<div class="card" id="teams"><h3>🛡️ Teams & orgs</h3><p class="muted small">Need tryouts, scrim partners, team aim programmes or a bootcamp? We will build a plan.</p>
<form class="js-form" data-subject="LEAD: Team / org enquiry" data-success="Thanks! We’ll send a proposal within 2 business days.">{HP}<input type="hidden" name="form" value="team-enquiry">
<div class="field"><input name="org" placeholder="Team / organisation" required aria-label="Organisation"></div><div class="field"><input type="email" name="email" placeholder="Email" required aria-label="Email"></div>
<div class="field"><input name="players" type="number" placeholder="Number of players" aria-label="Players"></div><div class="field"><textarea name="needs" placeholder="What do you need?" aria-label="Needs"></textarea></div>
<button class="btn btn-primary btn-block" type="submit">Request proposal</button><div class="form-msg"></div></form></div>
<div class="card" id="partners"><h3>🏹 Clubs, ranges & instructors</h3><p class="muted small">Orienteering clubs, archery ranges and darts leagues: get listed and receive enquiries from AimOff readers.</p>
<form class="js-form" data-subject="LEAD: Club / instructor listing" data-success="Thanks! We’ll confirm your listing shortly.">{HP}<input type="hidden" name="form" value="club-listing">
<div class="field"><input name="club" placeholder="Club / business name" required aria-label="Club"></div><div class="field"><select name="type" aria-label="Type"><option>Orienteering / navigation</option><option>Archery</option><option>Darts</option><option>Esports venue / LAN</option><option>Other</option></select></div>
<div class="field"><input name="location" placeholder="City, country" required aria-label="Location"></div><div class="field"><input type="email" name="email" placeholder="Email" required aria-label="Email"></div>
<button class="btn btn-primary btn-block" type="submit">Get listed</button><div class="form-msg"></div></form></div>
</div></section>
<section class="section alt"><div class="container" style="max-width:860px"><h2 class="center">Coaching FAQ</h2>{faq(COACH_FAQ)}</div></section>'''

# ---------------- CONTESTS ----------------
CONTESTS = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Free entry · skill-based</span><h1>The AimOff Open: Monthly Aim Contests</h1>
<p>Every month we pick a benchmark. Post your best score with proof, climb the board, and win prizes funded by sponsors and supporters. No purchase is necessary.</p></div></section>
<section><div class="container layout"><div>
<div class="grid g3"><div class="card"><span class="tag">This month</span><h3>Gridshot 60s</h3><p class="muted small">Highest normalised score in the AimOff Trainer, Gridshot mode, 60 seconds, medium targets.</p><a class="btn btn-primary btn-sm" href="{{R}}train.html?mode=gridshot">Practise now</a></div>
<div class="card"><span class="tag">Side event</span><h3>Reaction Royale</h3><p class="muted small">Lowest 5-try average on the Reaction Time Test, with a screen recording required.</p><a class="btn btn-secondary btn-sm" href="{{R}}reaction-test.html">Practise</a></div>
<div class="card"><span class="tag hot">Creators</span><h3>Clip of the Month</h3><p class="muted small">Best in-game aim clip (max 30 seconds), judged by the AimOff team.</p></div></div>
<h2 class="mt">Prizes</h2><div class="grid g3"><div class="card center"><div class="big-result" style="color:var(--gold)">🥇</div><h3>1st place</h3><p class="muted small">Sponsored gear prize + Featured Player spotlight</p></div><div class="card center"><div class="big-result">🥈</div><h3>2nd place</h3><p class="muted small">Gift card + free coaching session</p></div><div class="card center"><div class="big-result">🥉</div><h3>3rd place</h3><p class="muted small">Free coaching session + AimOff badge</p></div></div>
<p class="muted small mt">Prizes are confirmed and announced at the start of each month once sponsors and the supporter fund are allocated. <a href="{{R}}advertise.html#contest">Sponsor a prize →</a></p>
{AD}
<h2>Leaderboard</h2><div class="table-wrap"><table class="lb"><thead><tr><th>#</th><th>Player</th><th>Score</th><th>Verified</th></tr></thead><tbody id="lb-body"><tr><td colspan="4" class="muted">Season leaderboard opens with the first verified entries. Be the first name on the board.</td></tr></tbody></table></div>
<h2 class="mt" id="enter">Enter the contest</h2>
<form class="card js-form" data-subject="CONTEST ENTRY" data-success="Entry received! We’ll verify it and update the leaderboard within 72 hours.">{HP}<input type="hidden" name="form" value="contest-entry">
<div class="row"><div class="field"><label for="ce-name">Player name / handle</label><input id="ce-name" name="player" required></div><div class="field"><label for="ce-email">Email</label><input id="ce-email" type="email" name="email" required></div></div>
<div class="row"><div class="field"><label for="ce-mode">Event</label><select id="ce-mode" name="mode"><option value="gridshot">Gridshot 60s</option><option value="reaction">Reaction Royale</option><option value="flick">Flick</option><option value="tracking">Tracking</option><option value="precision">Precision</option><option value="clip">Clip of the Month</option></select></div>
<div class="field"><label for="ce-score">Score</label><input id="ce-score" name="score" required></div></div>
<div class="field"><label for="ce-proof">Proof link (screen recording / screenshot / clip URL)</label><input id="ce-proof" name="proof" type="url" placeholder="https://" required></div>
<div class="row"><div class="field"><label for="ce-country">Country</label><input id="ce-country" name="country"></div><div class="field"><label for="ce-social">Social / Discord (optional)</label><input id="ce-social" name="social"></div></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I have read and accept the contest rules below, and I am 18+ or have a parent/guardian’s consent.</label>
<button class="btn btn-gold btn-block mt" type="submit">Submit entry</button><div class="form-msg" role="status"></div></form>
<h2 class="mt">Official rules (summary)</h2><div class="prose small"><ol>
<li><b>No purchase necessary.</b> Entry is free. Donations or purchases do not improve your chances.</li><li>This is a skill contest: winners are decided by verified score or, for clips, by published judging criteria (difficulty 40%, execution 40%, entertainment 20%).</li>
<li>One account per person. Scripts, macros, aim assists, cheats or edited proof lead to disqualification.</li><li>Entries close on the last day of each month at 23:59 UTC. Winners are announced within 7 days and must reply within 14 days.</li>
<li>Prizes are non-transferable and may be substituted with equal value. Winners are responsible for any taxes. Void where prohibited by law.</li><li>By entering you allow AimOff to display your handle, score and submitted clip on the site and social channels.</li>
<li>AimOff may amend or cancel a contest if circumstances beyond its control arise; any changes will be posted on this page.</li></ol></div>
</div>
<aside class="sidebar"><div class="card"><h3>Fund the prize pool</h3><p class="muted small">Supporters fund prizes for the community.</p><a class="btn btn-gold btn-block" href="{{R}}support.html?purpose=Contest+prizes">Donate to prizes</a></div>{SIDE_AD}
<div class="card"><h3>Brands</h3><p class="muted small">Title-sponsor a monthly Open: logo, prize placement and newsletter feature.</p><a class="btn btn-secondary btn-block" href="{{R}}advertise.html#contest">Sponsor a month</a></div></aside>
</div></section>
<script>
fetch('{{R}}data/leaderboard.json').then(function(r){{return r.json()}}).then(function(d){{
 if(!d.entries||!d.entries.length)return;
 document.getElementById('lb-body').innerHTML=d.entries.map(function(e,i){{return '<tr><td>'+(i+1)+'</td><td>'+e.player+'</td><td>'+e.score+'</td><td>'+(e.verified?'✅':'⏳')+'</td></tr>'}}).join('');
}}).catch(function(){{}});
</script>'''

# ---------------- SUPPORT / DONATE ----------------
SUPPORT = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Keep AimOff free</span><h1>Support AimOff</h1>
<p>AimOff is free for everyone. Donations go directly into running the site, monthly prize pools, promotion, and hiring the coaches, creators and developers who build new tools.</p></div></section>
<section><div class="container layout"><div>
<div class="card"><h2>Choose an amount</h2>
<div class="tiers mt"><div class="tier" data-amount="5"><b>$5</b><span class="muted small">Supporter</span></div><div class="tier on" data-amount="15"><b>$15</b><span class="muted small">Prize booster</span></div><div class="tier" data-amount="50"><b>$50</b><span class="muted small">Contest backer</span></div><div class="tier" data-amount="150"><b>$150</b><span class="muted small">Champion</span></div></div>
<div class="row mt"><div class="field"><label for="custom-amount">Amount (USD)</label><input id="custom-amount" type="number" min="1" value="15"></div>
<div class="field"><label for="donate-purpose">Direct my support to</label><select id="donate-purpose" name="purpose"><option>General support</option><option>Ongoing operations</option><option>Contest prizes</option><option>Promotions & marketing</option><option>Hiring talent</option></select></div></div>
<button class="btn btn-gold btn-block" data-donate>❤ Donate securely with PayPal</button>
<p class="muted small mt">You will be taken to PayPal’s secure checkout, where cards are also accepted. AimOff never sees your payment details. Donations are voluntary support, not tax-deductible charitable gifts, and give no contest advantage.</p></div>
<h2 class="mt">Where your support goes</h2>
<div class="grid g2">
<div class="card"><h3>⚙️ Ongoing operations: 35%</h3><div class="bar"><i style="width:35%"></i></div><p class="muted small mt">Domains, tools, testing devices, moderation and keeping every tool free.</p></div>
<div class="card"><h3>🏆 Contests & prizes: 25%</h3><div class="bar"><i style="width:25%"></i></div><p class="muted small mt">Monthly AimOff Open prize pools and community events.</p></div>
<div class="card"><h3>📣 Promotions & marketing: 20%</h3><div class="bar"><i style="width:20%"></i></div><p class="muted small mt">Growing the community, creator collabs and tournament promotion.</p></div>
<div class="card"><h3>🧑‍💻 Hiring talent: 20%</h3><div class="bar"><i style="width:20%"></i></div><p class="muted small mt">Paying coaches, writers, video editors and developers for new features.</p></div></div>
{AD}
<h2>Other ways to help</h2><div class="grid g3"><div class="card"><h3>Share a score</h3><p class="muted small">Every shared result brings new players.</p><a href="{{R}}train.html">Play & share →</a></div>
<div class="card"><h3>Sponsor</h3><p class="muted small">Brands can fund a tool, a video or a prize.</p><a href="{{R}}advertise.html">Packages →</a></div>
<div class="card"><h3>Join the team</h3><p class="muted small">Coaches, creators and developers wanted.</p><a href="{{R}}careers.html">Open roles →</a></div></div>
<h2 class="mt">Pledge or in-kind support</h2><form class="card js-form" data-subject="Support pledge / in-kind offer" data-success="Thank you! We’ll reach out to arrange the details.">{HP}<input type="hidden" name="form" value="pledge">
<div class="row"><div class="field"><label for="p-name">Name / company</label><input id="p-name" name="name" required></div><div class="field"><label for="p-email">Email</label><input id="p-email" name="email" type="email" required></div></div>
<div class="field"><label for="p-offer">What would you like to offer?</label><select id="p-offer" name="offer"><option>Monthly recurring support</option><option>Gear for prizes</option><option>Services (design, dev, video)</option><option>Promotion / shout-out</option><option>Other</option></select></div>
<div class="field"><label for="p-msg">Details</label><textarea id="p-msg" name="message"></textarea></div><button class="btn btn-primary" type="submit">Send pledge</button><div class="form-msg"></div></form>
</div><aside class="sidebar">{SIDE_AD}<div class="card"><h3>Transparency</h3><p class="muted small">We publish a short funding update in the newsletter each quarter.</p></div></aside></div></section>'''

# ---------------- ADVERTISE ----------------
ADVERTISE = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Media kit</span><h1>Advertise & Sponsor on AimOff</h1>
<p>Reach players who actively train their aim: competitive gamers, aspiring pros and gear enthusiasts. Every package is clearly labelled as sponsored. For domain acquisition or partnership enquiries, <a href="https://web.works/contact" target="_blank" rel="noopener">contact the owner here</a>.</p></div></section>
<section><div class="container"><div class="grid g4">
<div class="card"><span class="tag">Tools</span><h3>Tool sponsorship</h3><p class="muted small">“Presented by” branding on the Aim Trainer, Sensitivity Converter or CPS Test, plus a contextual product card.</p></div>
<div class="card" id="contest"><span class="tag hot">Contests</span><h3>Title-sponsor the Open</h3><p class="muted small">Name the monthly contest, supply the prize, and get logo placement, a newsletter feature and social posts.</p></div>
<div class="card" id="creators"><span class="tag">Video</span><h3>Creator & video</h3><p class="muted small">Integrated segments in AimOff videos and creator collaborations on our video library.</p></div>
<div class="card"><span class="tag">Content</span><h3>Sponsored guides</h3><p class="muted small">Gear reviews and how-tos, clearly disclosed, with tracked affiliate links.</p></div></div>
<div class="grid g3 mt"><div class="card"><h3>Display</h3><p class="muted small">Direct-sold banner placements (300×250, 728×90, sticky mobile) that replace programmatic ads.</p></div><div class="card"><h3>Newsletter</h3><p class="muted small">A dedicated or shared slot in the weekly drill email.</p></div><div class="card"><h3>Affiliate partnerships</h3><p class="muted small">Mice, mousepads, monitors, chairs, coaching platforms, and outdoor or archery gear.</p></div></div>
{AD}
<h2 class="mt">Request the media kit</h2>
<form class="card js-form" data-subject="LEAD: Advertising / sponsorship enquiry" data-success="Thanks! The media kit and rate card are on the way.">{HP}<input type="hidden" name="form" value="advertise">
<div class="row"><div class="field"><label for="a-name">Name</label><input id="a-name" name="name" required></div><div class="field"><label for="a-company">Company / brand</label><input id="a-company" name="company" required></div></div>
<div class="row"><div class="field"><label for="a-email">Work email</label><input id="a-email" name="email" type="email" required></div><div class="field"><label for="a-site">Website</label><input id="a-site" name="website" type="url" placeholder="https://"></div></div>
<div class="field"><label>Interested in</label><div class="chips">{''.join(f'<label><input type="checkbox" name="interest" value="{x}"><span>{x}</span></label>' for x in ['Tool sponsorship', 'Contest sponsorship', 'Display ads', 'Video / creator', 'Sponsored content', 'Newsletter', 'Affiliate', 'Domain / site acquisition', 'Partnership'])}</div></div>
<div class="row"><div class="field"><label for="a-budget">Budget (monthly)</label><select id="a-budget" name="budget"><option>Under $500</option><option>$500–2,000</option><option>$2,000–10,000</option><option>$10,000+</option></select></div><div class="field"><label for="a-start">Start date</label><input id="a-start" name="start" type="month"></div></div>
<div class="field"><label for="a-msg">Goals & notes</label><textarea id="a-msg" name="message"></textarea></div>
<button class="btn btn-primary" type="submit">Request media kit</button><div class="form-msg"></div></form></div></section>'''

# ---------------- CAREERS ----------------
ROLES = [('Aim / game coach (freelance)', 'Coach players in your game. Paid per session through student leads.'),
         ('Content writer: gaming & aim', 'Write guides, gear explainers and settings breakdowns. Paid per article.'),
         ('Video editor / YouTube creator', 'Edit drill videos, Shorts and contest highlights. Paid per video.'),
         ('Community & contest manager', 'Run the monthly Open, verify entries and moderate the community. Part-time.'),
         ('Front-end / game developer', 'Build new trainer modes, a 3D trainer, leaderboards and PWA features. Contract.'),
         ('Partnerships & sponsorship sales', 'Bring in gear brands and contest sponsors. Commission-based.')]
CAREERS = '''<section class="page-hero"><div class="container"><span class="eyebrow">We’re hiring talent</span><h1>Careers & Talent</h1>
<p>AimOff is growing. We work with freelancers and part-timers worldwide, remote-first, and pay for results.</p></div></section>
<section><div class="container"><div class="grid g3">''' + ''.join(f'<div class="card"><h3>{t}</h3><p class="muted small">{d}</p><a href="#apply" onclick="document.getElementById(\'role\').value=\'{t}\'">Apply →</a></div>' for t, d in ROLES) + f'''</div>
<h2 class="mt" id="apply">Apply</h2><form class="card js-form" data-subject="Talent application" data-success="Application received. We review applications weekly.">{HP}<input type="hidden" name="form" value="talent">
<div class="row"><div class="field"><label for="t-name">Name</label><input id="t-name" name="name" required></div><div class="field"><label for="t-email">Email</label><input id="t-email" name="email" type="email" required></div></div>
<div class="row"><div class="field"><label for="role">Role</label><select id="role" name="role">{''.join(f'<option>{t}</option>' for t, _ in ROLES)}<option>Other</option></select></div><div class="field"><label for="t-loc">Location / time zone</label><input id="t-loc" name="location"></div></div>
<div class="field"><label for="t-port">Portfolio / profile links</label><input id="t-port" name="portfolio" placeholder="https://"></div>
<div class="field"><label for="t-why">Why you, in a few lines</label><textarea id="t-why" name="message" required></textarea></div>
<button class="btn btn-primary" type="submit">Send application</button><div class="form-msg"></div></form></div></section>'''

# ---------------- ABOUT / CONTACT ----------------
ABOUT = '''<section class="page-hero"><div class="container"><span class="eyebrow">About</span><h1>About AimOff</h1>
<p>AimOff is a free, independent aim-training hub. We build fast browser tools that measure and improve aim, and we write practical guides for gamers and other people who aim, from orienteers to darts players.</p></div></section>
<section><div class="container prose" style="max-width:860px">
<h2>Our principle: smart aim beats lucky aim</h2><p>The name comes from <a href="{R}aiming-off.html">aiming off</a>, the navigator’s technique of deliberately aiming to one side so you never miss your target. We apply the same idea to training: measure, find the error, then correct it on purpose.</p>
<h2>What we believe</h2><ul><li><b>Free core tools, forever.</b> They are funded by ads, sponsors and supporters.</li><li><b>Fast and private.</b> There is no account to sign up for, and your scores stay on your device unless you submit them.</li><li><b>Honest content.</b> Sponsored items are labelled, and affiliate links are disclosed.</li><li><b>Community first.</b> Contests are free to enter and judged on skill.</li></ul>
<h2>Roadmap</h2><ul><li>3D WebGL trainer with game FOV presets</li><li>Global leaderboards and benchmark seasons</li><li>Pro-style settings database</li><li>Mobile app (PWA) and Discord bot</li><li>More conversion pairs and game-specific guides</li></ul>
<p><a class="btn btn-primary" href="{R}contact.html">Contact us</a> <a class="btn btn-secondary" href="https://web.works/contact" target="_blank" rel="noopener">Domain / partnership enquiries</a></p></div></section>'''

CONTACT = f'''<section class="page-hero"><div class="container"><span class="eyebrow">Get in touch</span><h1>Contact AimOff</h1>
<p>Questions, feedback, bug reports, press or partnerships: send us a message and we reply within 1–2 business days. For interest in buying this website or domain name, or in sponsorship, advertising or partnership, you can also use <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p></div></section>
<section><div class="container layout"><form class="card js-form" data-subject="Contact form" data-success="Message sent! We’ll get back to you soon.">{HP}<input type="hidden" name="form" value="contact">
<div class="row"><div class="field"><label for="ct-name">Name</label><input id="ct-name" name="name" required></div><div class="field"><label for="ct-email">Email</label><input id="ct-email" name="email" type="email" required></div></div>
<div class="field"><label for="ct-topic">Topic</label><select id="ct-topic" name="topic"><option>General question</option><option>Bug report</option><option>Feature request</option><option>Coaching</option><option>Contest</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Website / domain acquisition</option><option>Press</option><option>Copyright / trademark concern</option></select></div>
<div class="field"><label for="ct-msg">Message</label><textarea id="ct-msg" name="message" required></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that AimOff may use these details to reply to me.</label>
<button class="btn btn-primary mt" type="submit">Send message</button><div class="form-msg" role="status"></div></form>
<aside class="sidebar"><div class="card"><h3>Prefer email?</h3><p class="muted small">Open your mail app with one click. Our address is protected from spam bots.</p><a class="btn btn-secondary btn-block" href="#" data-mail="AimOff.com enquiry">✉ Email us</a></div>
<div class="card"><h3>Business & domain</h3><p class="muted small">Interested in this website, the domain name, sponsorship, advertising or a partnership?</p><a class="btn btn-gold btn-block" href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div></aside></div></section>'''

# ---------------- LEGAL ----------------
PRIVACY = '''<section class="page-hero"><div class="container"><h1>Privacy Policy</h1><p class="muted">Last updated: October 2026</p></div></section>
<section><div class="container prose" style="max-width:860px">
<p>AimOff.com (“AimOff”, “we”) respects your privacy. This policy explains what we collect and why.</p>
<h2>Information you give us</h2><p>When you submit a form (contact, coaching, contest, newsletter, careers, sponsorship) we receive the details you enter. Form submissions are delivered to us by FormSubmit (formsubmit.co), a form-processing service. We use these details only to respond, to provide the service you asked for (for example matching you with a coach), and, if you opted in, to send our newsletter. We do not sell personal information.</p>
<h2>Information stored on your device</h2><p>Scores, personal bests, history, theme and consent choices are stored in your browser’s local storage. They never leave your device unless you submit them.</p>
<h2>Advertising & cookies</h2><p>We may use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your previous visits to this and other websites. Google’s use of advertising cookies lets it and its partners serve ads based on your visits. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">aboutads.info</a>. See <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses data from partner sites</a>. Visitors in the EEA, UK and Switzerland are shown a consent message, and you can choose “Essential only”.</p>
<h2>Analytics</h2><p>We may use Google Analytics to understand aggregate usage, such as pages visited and device type. IP addresses are not stored in identifiable form by GA4.</p>
<h2>Embedded content</h2><p>Videos use YouTube’s privacy-enhanced mode (youtube-nocookie.com) and load only when you click play. Donations are processed by PayPal under its own privacy policy.</p>
<h2>Children</h2><p>AimOff is a general-audience site. Users under 16 should get a parent’s or guardian’s permission before submitting any form. We do not knowingly collect personal information from children under 13.</p>
<h2>Your rights</h2><p>You can ask us to access, correct or delete the personal information you submitted. Use the <a href="{R}contact.html">contact page</a>. Residents of the EU/UK (GDPR), California (CCPA/CPRA) and Canada (PIPEDA) have additional rights, which we honour.</p>
<h2>Changes</h2><p>We will update this page if our practices change.</p></div></section>'''

TERMS = '''<section class="page-hero"><div class="container"><h1>Terms of Use</h1><p class="muted">Last updated: October 2026</p></div></section>
<section><div class="container prose" style="max-width:860px">
<p>By using AimOff.com you agree to these terms.</p>
<h2>Use of the site</h2><p>The tools and content are provided free for personal, non-commercial use. Do not attempt to disrupt the site, scrape it at scale, or submit false contest results.</p>
<h2>No warranty</h2><p>Tools such as sensitivity conversions, reaction and CPS measurements are provided “as is” for entertainment and training. Results depend on your hardware and browser and may not be exact. Always verify settings in-game.</p>
<h2>Health</h2><p>Take regular breaks. Stop if you feel pain in your hand, wrist or eyes. Fast-clicking techniques can cause strain.</p>
<h2>Contests</h2><p>Contests are governed by the rules on the Contests page. No purchase is necessary.</p>
<h2>Coaching & third parties</h2><p>Coaches are independent and are not employees of AimOff. Any paid arrangement is between you and the coach. Links to third-party sites are provided for convenience, and we are not responsible for their content.</p>
<h2>Intellectual property</h2><p>Original content, code and design are © AimOff.com. Trademarks belong to their owners. See the <a href="{R}disclaimer.html">Disclaimer</a>.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, AimOff is not liable for indirect or consequential losses arising from use of the site.</p>
<h2>Contact</h2><p>Questions? <a href="{R}contact.html">Contact us</a>.</p></div></section>'''

DISCLAIMER = '''<section class="page-hero"><div class="container"><h1>Disclaimer, Trademark & Copyright Notice</h1></div></section>
<section><div class="container prose" style="max-width:860px">
<h2>Trademark disclosure</h2><p>“AimOff” is the name of this independent website and is derived from the generic English phrase “aim off”, a long-established term in land navigation, orienteering and target sports. AimOff.com claims no exclusive rights in the descriptive phrase “aim off” and is <b>not affiliated with, endorsed by, sponsored by or connected to</b> any business, product, application, team or organisation that uses the same or a similar name. Any resemblance is coincidental.</p>
<p>Game titles, publisher names, hardware brands and other marks referenced on this site, including Counter-Strike, Valorant, Apex Legends, Overwatch, Call of Duty, Fortnite, Team Fortress, Titanfall, Quake, Marvel Rivals and Rainbow Six, are trademarks or registered trademarks of their respective owners. They are used solely to identify compatibility (nominative fair use). AimOff is not endorsed by, or affiliated with, any game publisher. No publisher logos or game assets are used.</p>
<h2>Copyright</h2><p>All original text, tools, source code, graphics and layouts on AimOff.com are © AimOff.com, all rights reserved, unless stated otherwise. Embedded YouTube videos are owned by their respective creators and are displayed using YouTube’s official embed functionality in line with YouTube’s Terms of Service. Fonts are served by Google Fonts under the SIL Open Font License.</p>
<h2>Copyright or trademark concerns</h2><p>If you believe content on this site infringes your rights, please use the <a href="{R}contact.html?topic=Copyright+%2F+trademark+concern">contact form</a> and select “Copyright / trademark concern”. Include the URL, a description of the work and your contact details. We review and act on valid notices promptly.</p>
<h2>Affiliate & advertising disclosure</h2><p>AimOff may earn money from display advertising (including Google AdSense), sponsorships and affiliate links. Sponsored content is labelled. Earning a commission never changes our test results.</p>
<h2>General disclaimer</h2><p>Information on this site is for general and educational purposes. Navigation guidance does not replace proper training and safety equipment in the outdoors. Archery and darts information does not replace instruction from a qualified coach.</p></div></section>'''

NOTFOUND = '''<section class="hero center"><div class="container"><div class="big-result" style="color:var(--hot)">404</div><h1>You aimed off a little too far.</h1>
<p class="muted">That page doesn’t exist, but your next personal best might.</p><div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="{R}index.html">Home</a><a class="btn btn-secondary" href="{R}train.html">Aim Trainer</a></div></div></section>'''

PAGES2 = [
    dict(path='guides.html', title='Aim Guides — Sensitivity, Warm-up, Crosshair Placement, Darts & Archery | AimOff',
         desc='Practical aim guides: the 4 pillars of aim, finding your sensitivity, a 10-minute warm-up, crosshair placement, setup checklist, grip styles, darts and archery aiming basics.', body=GUIDES, active='guides.html'),
    dict(path='aiming-off.html', title='Aiming Off: Navigation Technique Explained + Calculator | AimOff',
         desc='What aiming off means in orienteering and navigation, why it works, how many degrees to use, with a free aiming-off calculator, diagram, videos and FAQ.',
         body=AIMING_OFF, active='aiming-off.html', scripts=['tools.js'], schema=faq_schema(AO_FAQ)),
    dict(path='videos.html', title='Aim Training & Navigation Video Library | AimOff', desc='Hand-picked videos on FPS aim fundamentals, sensitivity and the aiming-off navigation technique.', body=VIDEOS, active='videos.html'),
    dict(path='coaching.html', title='Free Aim Assessment & Coaching — Valorant, CS2, Apex, Fortnite | AimOff',
         desc='Get a free aim assessment from a vetted coach within 48 hours. Valorant, CS2, Apex, Fortnite, Overwatch 2, Call of Duty and more. Coaches, teams and clubs welcome.',
         body=COACHING, schema=faq_schema(COACH_FAQ), sticky=False),
    dict(path='contests.html', title='AimOff Open — Free Monthly Aim Contests with Prizes', desc='Enter the free monthly AimOff Open aim contest. Submit your score with proof, climb the leaderboard and win sponsored prizes. No purchase necessary.', body=CONTESTS, active='contests.html'),
    dict(path='support.html', title='Support AimOff — Donate to Keep Aim Tools Free', desc='Donate to AimOff to fund operations, monthly contest prizes, promotion and hiring creators and developers. Secure PayPal checkout.', body=SUPPORT),
    dict(path='advertise.html', title='Advertise & Sponsor — AimOff Media Kit', desc='Sponsor AimOff tools, contests, videos and guides. Reach competitive gamers who train their aim daily. Request the media kit.', body=ADVERTISE),
    dict(path='careers.html', title='Careers & Talent — Coaches, Creators, Developers | AimOff', desc='Join AimOff as a coach, writer, video editor, community manager, developer or partnerships lead. Remote, freelance and part-time roles.', body=CAREERS),
    dict(path='about.html', title='About AimOff — Smart Aim Beats Lucky Aim', desc='AimOff is a free, independent aim-training hub with browser tools, guides and contests for gamers and anyone who aims.', body=ABOUT),
    dict(path='contact.html', title='Contact AimOff', desc='Contact AimOff for questions, feedback, coaching, contests, sponsorship, partnerships or domain enquiries.', body=CONTACT),
    dict(path='privacy.html', title='Privacy Policy | AimOff', desc='How AimOff handles form submissions, local storage, cookies, advertising and analytics.', body=PRIVACY),
    dict(path='terms.html', title='Terms of Use | AimOff', desc='Terms of use for AimOff.com tools, content, contests and coaching.', body=TERMS),
    dict(path='disclaimer.html', title='Disclaimer, Trademark & Copyright Notice | AimOff', desc='Trademark and copyright disclosure for AimOff.com, plus the affiliate and advertising disclosure.', body=DISCLAIMER),
    dict(path='404.html', title='Page not found | AimOff', desc='Page not found.', body=NOTFOUND, noindex=True),
]
