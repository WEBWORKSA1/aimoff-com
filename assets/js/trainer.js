/* AimOff Trainer — 2D canvas aim trainer with 5 modes. */
(function () {
  'use strict';
  var cv = document.getElementById('arena'); if (!cv) return;
  var ctx = cv.getContext('2d');
  var ov = document.getElementById('overlay');
  var S = window.AIMOFF.store;
  var MODES = {
    gridshot:  { name: 'Gridshot',  desc: 'Three targets at once. Clear them as fast as you can.', size: 30, count: 3 },
    flick:     { name: 'Flick',     desc: 'One target, random spot. Snap to it and click.', size: 22, count: 1 },
    tracking:  { name: 'Tracking',  desc: 'Keep your crosshair on the moving target. No clicking.', size: 34, count: 1 },
    reflex:    { name: 'Reflex',    desc: 'Targets shrink and vanish. Hit them before they disappear.', size: 34, count: 1 },
    precision: { name: 'Precision', desc: 'Tiny targets. Accuracy matters more than speed.', size: 11, count: 1 }
  };
  var TIERS = ['Rookie', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Legend'];
  // score thresholds per mode for 60s (scaled for 30s)
  var THR = { gridshot: [0, 25, 45, 60, 75, 90, 105, 120], flick: [0, 20, 32, 42, 52, 62, 72, 82], tracking: [0, 30, 45, 55, 65, 75, 83, 90],
              reflex: [0, 15, 28, 40, 52, 62, 72, 82], precision: [0, 12, 20, 28, 36, 44, 52, 60] };

  var st = { mode: 'gridshot', dur: 60, scale: 1, color: '#22e3c4', running: false };
  var g = null, mouse = { x: -99, y: -99, in: false }, dpr = 1, W = 0, H = 0, raf = 0;

  function resize() {
    dpr = window.devicePixelRatio || 1;
    var r = cv.getBoundingClientRect(); W = r.width; H = r.height;
    cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  window.addEventListener('resize', resize); resize();

  function rnd(a, b) { return a + Math.random() * (b - a); }
  function rad() { var base = MODES[st.mode].size * st.scale * Math.max(.6, Math.min(1.4, W / 900)); return base; }
  function spawn() {
    var r = rad(), t = { x: rnd(r + 10, W - r - 10), y: rnd(r + 10, H - r - 10), r: r, born: performance.now(), vx: 0, vy: 0 };
    if (st.mode === 'gridshot') { // snap to a 5x4 grid like classic grid drills
      var cx = Math.floor(rnd(0, 5)), cy = Math.floor(rnd(0, 4));
      t.x = W * (.2 + cx * .15); t.y = H * (.2 + cy * .2);
      if (g.targets.some(function (o) { return Math.hypot(o.x - t.x, o.y - t.y) < 5; })) return spawn();
    }
    if (st.mode === 'tracking') { var sp = Math.max(W, 400) / 4; t.x = W / 2; t.y = H / 2; t.vx = rnd(-sp, sp); t.vy = rnd(-sp, sp) * .6; t.turn = 0; }
    if (st.mode === 'reflex') t.life = 1100;
    return t;
  }

  function start() {
    resize();
    g = { t0: performance.now(), last: performance.now(), hits: 0, shots: 0, score: 0, targets: [], ttk: [], onT: 0, total: 0 };
    for (var i = 0; i < MODES[st.mode].count; i++) g.targets.push(spawn());
    st.running = true; ov.hidden = true;
    cancelAnimationFrame(raf); raf = requestAnimationFrame(loop);
  }

  function end() {
    st.running = false;
    var acc = g.shots ? g.hits / g.shots * 100 : 0;
    var score;
    if (st.mode === 'tracking') score = Math.round(g.onT / Math.max(g.total, 1) * 100);
    else score = Math.round(g.hits * (0.5 + acc / 200) * (60 / st.dur) * 10) / 10; // normalised to a 60s run
    var ttk = g.ttk.length ? Math.round(g.ttk.reduce(function (a, b) { return a + b; }, 0) / g.ttk.length) : 0;
    var thr = THR[st.mode], tier = 0; for (var i = 0; i < thr.length; i++) if (score >= thr[i]) tier = i;
    var key = 'pb-' + st.mode, pb = S.get(key, 0), isPB = score > pb; if (isPB) S.set(key, score);
    var hist = S.get('history', []); hist.unshift({ m: st.mode, s: score, a: Math.round(acc), d: st.dur, t: Date.now() }); S.set('history', hist.slice(0, 50));
    renderHistory();
    var unit = st.mode === 'tracking' ? '% on target' : 'pts';
    ov.innerHTML = '<div class="small" style="opacity:.8">' + MODES[st.mode].name + ' · ' + st.dur + 's</div>' +
      '<div class="big-result">' + score + ' <span style="font-size:.35em">' + unit + '</span></div>' +
      '<div><span class="tag">' + TIERS[tier] + '</span>' + (isPB ? '<span class="tag hot">New personal best!</span>' : '<span class="tag">PB ' + pb + '</span>') + '</div>' +
      '<div class="small">Hits ' + g.hits + ' · Accuracy ' + acc.toFixed(1) + '%' + (ttk ? ' · Avg time-to-kill ' + ttk + ' ms' : '') + '</div>' +
      '<div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:8px">' +
      '<button class="btn btn-primary" id="again">Play again</button>' +
      '<button class="btn btn-secondary" id="shareBtn">Share</button>' +
      '<a class="btn btn-gold" href="contests.html?mode=' + st.mode + '&score=' + score + '&duration=' + st.dur + '#enter">Enter monthly contest</a></div>' +
      '<a href="coaching.html?game=&goal=Improve+aim" style="color:#9ff">Want a coach to fix your weak spots? Get a free assessment →</a>';
    ov.hidden = false;
    document.getElementById('again').onclick = start;
    document.getElementById('shareBtn').onclick = function () { window.AIMOFF.share('I scored ' + score + ' ' + unit + ' (' + TIERS[tier] + ') on AimOff ' + MODES[st.mode].name + '. Beat me:'); };
    updateHud(score, acc);
    var plays = S.get('plays', 0) + 1; S.set('plays', plays);
    if (plays === 3 && window.AIMOFF.openLeadModal) setTimeout(window.AIMOFF.openLeadModal, 1500);
  }

  function updateHud(score, acc) {
    var el = function (id) { return document.getElementById(id); };
    var left = st.running ? Math.max(0, st.dur - (performance.now() - g.t0) / 1000) : 0;
    el('h-time').textContent = left.toFixed(1);
    el('h-hits').textContent = g ? g.hits : 0;
    el('h-acc').textContent = (acc !== undefined ? acc : (g && g.shots ? g.hits / g.shots * 100 : 0)).toFixed(0) + '%';
    el('h-pb').textContent = S.get('pb-' + st.mode, 0);
    if (score !== undefined) el('h-score').textContent = score;
    else if (g) el('h-score').textContent = st.mode === 'tracking' ? Math.round(g.onT / Math.max(g.total, 1) * 100) + '%' : g.hits;
  }

  function loop(now) {
    var dt = Math.min(.05, (now - g.last) / 1000); g.last = now;
    if ((now - g.t0) / 1000 >= st.dur) { draw(now); end(); return; }
    if (st.mode === 'tracking') {
      var t = g.targets[0];
      t.turn -= dt; if (t.turn <= 0) { var sp = Math.max(W, 400) / 3.2; t.vx = rnd(-sp, sp); t.vy = rnd(-sp, sp) * .6; t.turn = rnd(.35, 1.2); }
      t.x += t.vx * dt; t.y += t.vy * dt;
      if (t.x < t.r || t.x > W - t.r) { t.vx *= -1; t.x = Math.max(t.r, Math.min(W - t.r, t.x)); }
      if (t.y < t.r || t.y > H - t.r) { t.vy *= -1; t.y = Math.max(t.r, Math.min(H - t.r, t.y)); }
      g.total += dt; if (mouse.in && Math.hypot(mouse.x - t.x, mouse.y - t.y) <= t.r) g.onT += dt;
    }
    if (st.mode === 'reflex') {
      g.targets = g.targets.map(function (t) { return (now - t.born > t.life) ? (g.shots++, spawn()) : t; });
    }
    draw(now); updateHud(); raf = requestAnimationFrame(loop);
  }

  function draw(now) {
    ctx.clearRect(0, 0, W, H);
    g.targets.forEach(function (t) {
      var r = t.r;
      if (st.mode === 'reflex') r = t.r * Math.max(.15, 1 - (now - t.born) / t.life);
      var on = st.mode === 'tracking' && Math.hypot(mouse.x - t.x, mouse.y - t.y) <= t.r;
      ctx.beginPath(); ctx.arc(t.x, t.y, r, 0, Math.PI * 2);
      var grd = ctx.createRadialGradient(t.x - r / 3, t.y - r / 3, r / 6, t.x, t.y, r);
      grd.addColorStop(0, on ? '#9dffcf' : '#ff8aa0'); grd.addColorStop(1, on ? '#20c76b' : '#ff2d55');
      ctx.fillStyle = grd; ctx.fill();
      ctx.beginPath(); ctx.arc(t.x, t.y, Math.max(2, r * .28), 0, Math.PI * 2); ctx.fillStyle = 'rgba(255,255,255,.85)'; ctx.fill();
    });
    if (mouse.in) { // crosshair
      ctx.strokeStyle = st.color; ctx.lineWidth = 2; var gap = 4, len = 9;
      ctx.beginPath();
      ctx.moveTo(mouse.x - gap - len, mouse.y); ctx.lineTo(mouse.x - gap, mouse.y);
      ctx.moveTo(mouse.x + gap, mouse.y); ctx.lineTo(mouse.x + gap + len, mouse.y);
      ctx.moveTo(mouse.x, mouse.y - gap - len); ctx.lineTo(mouse.x, mouse.y - gap);
      ctx.moveTo(mouse.x, mouse.y + gap); ctx.lineTo(mouse.x, mouse.y + gap + len);
      ctx.stroke(); ctx.fillStyle = st.color; ctx.fillRect(mouse.x - 1, mouse.y - 1, 2, 2);
    }
  }

  function pos(e) { var r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; mouse.in = true; }
  cv.addEventListener('pointermove', function (e) { pos(e); if (!st.running && g) draw(performance.now()); });
  cv.addEventListener('pointerleave', function () { mouse.in = false; });
  cv.addEventListener('pointerdown', function (e) {
    pos(e); if (!st.running || st.mode === 'tracking') return;
    g.shots++;
    for (var i = 0; i < g.targets.length; i++) {
      var t = g.targets[i], r = st.mode === 'reflex' ? t.r * Math.max(.15, 1 - (performance.now() - t.born) / t.life) : t.r;
      if (Math.hypot(mouse.x - t.x, mouse.y - t.y) <= r) {
        g.hits++; g.ttk.push(performance.now() - t.born); g.targets[i] = spawn(); return;
      }
    }
  });
  cv.addEventListener('contextmenu', function (e) { e.preventDefault(); });

  /* Controls */
  function seg(id, fn) {
    var box = document.getElementById(id);
    box.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      box.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on'); fn(b.getAttribute('data-v'));
      if (!st.running) intro();
    });
  }
  seg('seg-mode', function (v) { st.mode = v; });
  seg('seg-dur', function (v) { st.dur = +v; });
  seg('seg-size', function (v) { st.scale = +v; });
  var col = document.getElementById('xhair'); if (col) col.addEventListener('input', function () { st.color = col.value; });

  function intro() {
    cancelAnimationFrame(raf); st.running = false;
    ov.innerHTML = '<h2 style="margin:0">' + MODES[st.mode].name + '</h2><p style="margin:0;max-width:440px">' + MODES[st.mode].desc +
      '</p><button class="btn btn-primary" id="startBtn">Start · ' + st.dur + 's</button><div class="small" style="opacity:.75">Tip: press <kbd>Space</kbd> to start/restart</div>';
    ov.hidden = false; document.getElementById('startBtn').onclick = start;
    g = { hits: 0, shots: 0, targets: [], onT: 0, total: 0 }; updateHud(0, 0);
  }
  document.addEventListener('keydown', function (e) {
    if (e.code === 'Space' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); start(); }
    if (e.code === 'Escape' && st.running) { st.running = false; cancelAnimationFrame(raf); intro(); }
  });

  function renderHistory() {
    var tb = document.getElementById('history'); if (!tb) return;
    var h = S.get('history', []);
    tb.innerHTML = h.length ? h.slice(0, 10).map(function (r) {
      return '<tr><td>' + MODES[r.m].name + '</td><td>' + r.s + '</td><td>' + r.a + '%</td><td>' + r.d + 's</td><td>' + new Date(r.t).toLocaleDateString() + '</td></tr>';
    }).join('') : '<tr><td colspan="5" class="muted">No runs yet — your last 10 sessions will appear here.</td></tr>';
    var pbs = document.getElementById('pbs');
    if (pbs) pbs.innerHTML = Object.keys(MODES).map(function (k) { return '<div><b>' + S.get('pb-' + k, 0) + '</b><span>' + MODES[k].name + ' PB</span></div>'; }).join('');
  }
  var mq = new URLSearchParams(location.search).get('mode');
  if (mq && MODES[mq]) { st.mode = mq; document.querySelectorAll('#seg-mode button').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-v') === mq); }); }
  intro(); renderHistory();
})();
