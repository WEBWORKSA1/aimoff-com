/* AimOff tools: reaction, CPS, sensitivity converter, eDPI, cm/360, FOV, crosshair, mouse tests, aiming-off calculator. */
(function () {
  'use strict';
  var S = window.AIMOFF.store;
  var $ = function (id) { return document.getElementById(id); };

  /* ===== Game yaw table (degrees per mouse count at sensitivity 1) ===== */
  var GAMES = {
    cs2: ['Counter-Strike 2', 0.022], csgo: ['CS:GO', 0.022], valorant: ['Valorant', 0.07], apex: ['Apex Legends', 0.022],
    overwatch2: ['Overwatch 2', 0.0066], cod: ['Call of Duty (MW / Warzone / BO)', 0.0066], fortnite: ['Fortnite (X/Y %)', 0.005555],
    tf2: ['Team Fortress 2', 0.022], titanfall2: ['Titanfall 2', 0.022], quake: ['Quake Champions', 0.022], custom: ['Custom yaw…', 0.022]
  };
  window.AIMOFF.GAMES = GAMES;
  function cm360(yaw, sens, dpi) { return 360 / (yaw * sens * dpi) * 2.54; }

  /* ===== Reaction time ===== */
  var pad = $('react-pad');
  if (pad) {
    var state = 'idle', t0 = 0, timer = 0, runs = [], N = 5;
    var setPad = function (cls, html) { pad.className = 'react-pad ' + cls; pad.innerHTML = html; };
    var pct = function (ms) { // logistic approximation around a ~270 ms population median
      var z = (ms - 270) / 38; return Math.max(1, Math.min(99, Math.round(100 / (1 + Math.exp(1.7 * z)))));
    };
    var tier = function (ms) { return ms < 180 ? 'Superhuman' : ms < 210 ? 'Pro-level' : ms < 240 ? 'Elite' : ms < 280 ? 'Above average' : ms < 330 ? 'Average' : 'Warming up'; };
    var go = function () {
      if (state === 'idle' || state === 'res' || state === 'early') {
        state = 'wait'; setPad('wait', 'Wait for green…<span class="small" style="font-family:var(--font);font-weight:500">Attempt ' + (runs.length + 1) + ' of ' + N + '</span>');
        timer = setTimeout(function () { state = 'go'; t0 = performance.now(); setPad('go', 'CLICK!'); }, 1200 + Math.random() * 2800);
      } else if (state === 'wait') {
        clearTimeout(timer); state = 'early'; setPad('res', 'Too soon! 😅<span class="small" style="font-family:var(--font);font-weight:500">Click to try again</span>');
      } else if (state === 'go') {
        var ms = Math.round(performance.now() - t0); runs.push(ms);
        if (runs.length >= N) {
          var avg = Math.round(runs.reduce(function (a, b) { return a + b; }, 0) / runs.length), best = Math.min.apply(null, runs);
          var pb = S.get('pb-react', 9999); if (avg < pb) S.set('pb-react', avg);
          state = 'res';
          setPad('res', '<span class="big-result">' + avg + ' ms</span><span style="font-size:1rem;font-family:var(--font)">' + tier(avg) +
            ' · faster than ~' + pct(avg) + '% of people · best ' + best + ' ms</span><span class="small" style="font-family:var(--font);font-weight:500">Click to test again</span>');
          $('react-runs').textContent = runs.join(' · ') + ' ms';
          $('react-pb').textContent = Math.min(avg, pb === 9999 ? avg : pb) + ' ms';
          window.AIMOFF.lastReact = avg; runs = [];
        } else {
          state = 'res'; setPad('res', '<span class="big-result">' + ms + ' ms</span><span class="small" style="font-family:var(--font);font-weight:500">Click to keep going (' + runs.length + '/' + N + ')</span>');
        }
      }
    };
    pad.addEventListener('pointerdown', go);
    document.addEventListener('keydown', function (e) { if (e.code === 'Space' && document.activeElement.tagName !== 'INPUT') { e.preventDefault(); go(); } });
    var rpb = S.get('pb-react', 0); if (rpb && rpb !== 9999) $('react-pb').textContent = rpb + ' ms';
    var rs = $('react-share'); if (rs) rs.onclick = function () { window.AIMOFF.share('My reaction time is ' + (window.AIMOFF.lastReact || '?') + ' ms on AimOff. Can you beat it?'); };
  }

  /* ===== CPS test ===== */
  var cpsPad = $('cps-pad');
  if (cpsPad) {
    var dur = 5, clicks = 0, start = 0, running = false, done = false, iv = 0;
    var ranks = [[3, 'Sloth'], [5, 'Turtle'], [7, 'Rabbit'], [9, 'Cheetah'], [11, 'Falcon'], [14, 'Jitter Machine'], [99, 'Butterfly God']];
    var rankOf = function (c) { for (var i = 0; i < ranks.length; i++) if (c < ranks[i][0]) return ranks[i][1]; return 'Legend'; };
    var reset = function () { clicks = 0; running = false; done = false; clearInterval(iv); $('cps-count').textContent = 0; $('cps-live').textContent = '0.0'; $('cps-time').textContent = dur.toFixed(1);
      cpsPad.className = 'react-pad idle'; cpsPad.innerHTML = 'Click here to start<span class="small" style="font-family:var(--font);font-weight:500">' + dur + '-second test · or tap / press <kbd>Space</kbd></span>'; };
    var finish = function () {
      running = false; done = true; clearInterval(iv);
      var cps = clicks / dur, key = 'pb-cps-' + dur, pb = S.get(key, 0); if (cps > pb) S.set(key, cps);
      cpsPad.className = 'react-pad res';
      cpsPad.innerHTML = '<span class="big-result">' + cps.toFixed(2) + ' CPS</span><span style="font-size:1rem;font-family:var(--font)">' + clicks + ' clicks in ' + dur + 's · Rank: ' + rankOf(cps) + (cps > pb ? ' · New best!' : '') + '</span><span class="small" style="font-family:var(--font)">Wait a moment, then click to retry</span>';
      $('cps-pb').textContent = Math.max(cps, pb).toFixed(2); window.AIMOFF.lastCps = cps.toFixed(2);
      setTimeout(function () { done = false; }, 900);
    };
    var hit = function () {
      if (done) return;
      if (!running && clicks === 0) {
        running = true; start = performance.now(); cpsPad.className = 'react-pad go'; cpsPad.textContent = 'CLICK CLICK CLICK!';
        iv = setInterval(function () { var el = (performance.now() - start) / 1000; $('cps-time').textContent = Math.max(0, dur - el).toFixed(1);
          $('cps-live').textContent = (clicks / Math.max(el, .1)).toFixed(1); if (el >= dur) finish(); }, 50);
      } else if (!running) { reset(); return; }
      clicks++; $('cps-count').textContent = clicks;
    };
    cpsPad.addEventListener('pointerdown', function (e) { e.preventDefault(); hit(); });
    document.addEventListener('keydown', function (e) { if (e.code === 'Space' && !e.repeat && document.activeElement.tagName !== 'INPUT') { e.preventDefault(); hit(); } });
    $('cps-dur').addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return;
      this.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on'); dur = +b.getAttribute('data-v');
      $('cps-pb').textContent = S.get('pb-cps-' + dur, 0).toFixed(2); reset(); });
    var cs = $('cps-share'); if (cs) cs.onclick = function () { window.AIMOFF.share('I hit ' + (window.AIMOFF.lastCps || '?') + ' CPS on the AimOff click test!'); };
    var d0 = new URLSearchParams(location.search).get('t'); if (d0) { dur = +d0 || 5; }
    $('cps-pb').textContent = S.get('pb-cps-' + dur, 0).toFixed(2); reset();
  }

  /* ===== Sensitivity converter ===== */
  var conv = $('conv');
  if (conv) {
    var opts = Object.keys(GAMES).map(function (k) { return '<option value="' + k + '">' + GAMES[k][0] + '</option>'; }).join('');
    $('from-game').innerHTML = opts; $('to-game').innerHTML = opts;
    var q = new URLSearchParams(location.search);
    $('from-game').value = conv.getAttribute('data-from') || q.get('from') || 'cs2';
    $('to-game').value = conv.getAttribute('data-to') || q.get('to') || 'valorant';
    var yawOf = function (side) { var k = $(side + '-game').value; return k === 'custom' ? (+$(side + '-yaw').value || 0.022) : GAMES[k][1]; };
    var calc = function () {
      ['from', 'to'].forEach(function (s) { $(s + '-yaw-wrap').hidden = $(s + '-game').value !== 'custom'; });
      var fs = +$('from-sens').value, fd = +$('from-dpi').value, td = +$('to-dpi').value || fd;
      if (!fs || !fd) return;
      var fy = yawOf('from'), ty = yawOf('to');
      var ts = fs * fy * fd / (ty * td);
      var c = cm360(fy, fs, fd);
      $('to-sens').textContent = ts < 0.01 ? ts.toFixed(5) : ts.toFixed(3);
      $('o-cm').textContent = c.toFixed(1) + ' cm';
      $('o-in').textContent = (c / 2.54).toFixed(1) + ' in';
      $('o-edpi').textContent = Math.round(fs * fd * 100) / 100;
      $('o-mult').textContent = '×' + (fy / ty * fd / td).toFixed(4);
      var style = c > 45 ? 'Low sens — arm aiming, great for precise tac shooters.' : c > 28 ? 'Medium sens — balanced flicks & tracking.' : 'High sens — wrist/finger aiming, fast turns, harder micro-adjusts.';
      $('o-style').textContent = style;
    };
    conv.addEventListener('input', calc); conv.addEventListener('change', calc);
    $('swap').addEventListener('click', function () { var a = $('from-game').value; $('from-game').value = $('to-game').value; $('to-game').value = a;
      var s = $('to-sens').textContent; if (+s) $('from-sens').value = s; calc(); });
    calc();
  }

  /* ===== eDPI + cm/360 + FOV ===== */
  var ed = $('edpi-form');
  if (ed) { var f1 = function () { var v = (+$('e-sens').value) * (+$('e-dpi').value); $('e-out').textContent = v ? Math.round(v * 100) / 100 : '—'; }; ed.addEventListener('input', f1); f1(); }
  var cmf = $('cm-form');
  if (cmf) {
    var gsel = $('cm-game'); gsel.innerHTML = Object.keys(GAMES).filter(function (k) { return k !== 'custom'; }).map(function (k) { return '<option value="' + k + '">' + GAMES[k][0] + '</option>'; }).join('');
    var f2 = function () { var c = cm360(GAMES[gsel.value][1], +$('cm-sens').value, +$('cm-dpi').value); $('cm-out').textContent = isFinite(c) ? c.toFixed(1) + ' cm / 360°' : '—'; };
    cmf.addEventListener('input', f2); cmf.addEventListener('change', f2); f2();
  }
  var fov = $('fov-form');
  if (fov) {
    var f3 = function () {
      var ar = (+$('fov-w').value) / (+$('fov-h').value), v = +$('fov-v').value * Math.PI / 180;
      var h = 2 * Math.atan(Math.tan(v / 2) * ar) * 180 / Math.PI;
      var h43 = 2 * Math.atan(Math.tan(v / 2) * 4 / 3) * 180 / Math.PI;
      $('fov-out').textContent = isFinite(h) ? h.toFixed(2) + '° horizontal (' + h43.toFixed(2) + '° at 4:3)' : '—';
    };
    fov.addEventListener('input', f3); f3();
  }

  /* ===== Crosshair generator ===== */
  var xc = $('xh-canvas');
  if (xc) {
    var xctx = xc.getContext('2d');
    var drawX = function () {
      var c = { color: $('xh-color').value, len: +$('xh-len').value, th: +$('xh-th').value, gap: +$('xh-gap').value, dot: $('xh-dot').checked, ol: $('xh-ol').checked, t: $('xh-t').checked };
      var W = xc.width, H = xc.height, cx = W / 2, cy = H / 2;
      xctx.clearRect(0, 0, W, H);
      var bg = $('xh-bg').value; xctx.fillStyle = bg; xctx.fillRect(0, 0, W, H);
      var bars = [[cx - c.gap - c.len, cy - c.th / 2, c.len, c.th], [cx + c.gap, cy - c.th / 2, c.len, c.th], [cx - c.th / 2, cy + c.gap, c.th, c.len]];
      if (!c.t) bars.push([cx - c.th / 2, cy - c.gap - c.len, c.th, c.len]);
      if (c.dot) bars.push([cx - c.th / 2, cy - c.th / 2, c.th, c.th]);
      var sc = 4; // zoom for preview
      xctx.save(); xctx.translate(cx, cy); xctx.scale(sc, sc); xctx.translate(-cx, -cy);
      bars.forEach(function (b) {
        if (c.ol) { xctx.fillStyle = '#000'; xctx.fillRect(b[0] - 1, b[1] - 1, b[2] + 2, b[3] + 2); }
        xctx.fillStyle = c.color; xctx.fillRect(b[0], b[1], b[2], b[3]);
      });
      xctx.restore();
      $('xh-json').value = JSON.stringify(c);
    };
    document.getElementById('xh-form').addEventListener('input', drawX);
    $('xh-rand').addEventListener('click', function () {
      var cols = ['#00ff6a', '#22e3c4', '#ff2d55', '#ffe600', '#ffffff', '#00b3ff', '#ff00ea'];
      $('xh-color').value = cols[Math.floor(Math.random() * cols.length)]; $('xh-len').value = 1 + Math.floor(Math.random() * 8);
      $('xh-th').value = 1 + Math.floor(Math.random() * 3); $('xh-gap').value = Math.floor(Math.random() * 6);
      $('xh-dot').checked = Math.random() > .6; $('xh-t').checked = Math.random() > .85; drawX();
    });
    $('xh-copy').addEventListener('click', function () { navigator.clipboard && navigator.clipboard.writeText($('xh-json').value); this.textContent = 'Copied!'; });
    drawX();
  }

  /* ===== Polling-rate tester ===== */
  var pr = $('poll-area');
  if (pr) {
    var times = [], evName = ('onpointerrawupdate' in window) ? 'pointerrawupdate' : 'pointermove';
    pr.addEventListener(evName, function (e) {
      var evs = e.getCoalescedEvents ? e.getCoalescedEvents() : [e]; if (!evs.length) evs = [e];
      evs.forEach(function (x) { times.push(x.timeStamp); });
      var now = e.timeStamp; while (times.length && now - times[0] > 1000) times.shift();
      $('poll-out').textContent = times.length + ' Hz';
      var mx = S.get('poll-max', 0); if (times.length > mx) { S.set('poll-max', times.length); }
      $('poll-max').textContent = Math.max(mx, times.length) + ' Hz';
    });
  }

  /* ===== Double-click tester ===== */
  var dcb = $('dc-btn');
  if (dcb) {
    var last = { 0: 0, 2: 0 }, cnt = { 0: 0, 2: 0 }, dbl = { 0: 0, 2: 0 };
    dcb.addEventListener('contextmenu', function (e) { e.preventDefault(); });
    dcb.addEventListener('mousedown', function (e) {
      var b = e.button === 2 ? 2 : 0; cnt[b]++; var now = performance.now();
      if (now - last[b] < 80) dbl[b]++; last[b] = now;
      $('dc-out').textContent = 'Left clicks ' + cnt[0] + ' · suspicious doubles ' + dbl[0] + '  |  Right clicks ' + cnt[2] + ' · suspicious doubles ' + dbl[2];
    });
  }

  /* ===== DPI analyzer (pointer lock) ===== */
  var dpiBox = $('dpi-area');
  if (dpiBox) {
    var counts = 0, measuring = false;
    dpiBox.addEventListener('click', function () {
      if (!measuring) { counts = 0; measuring = true; dpiBox.requestPointerLock && dpiBox.requestPointerLock(); dpiBox.textContent = 'Move your mouse exactly the distance below to the RIGHT, then click again.'; }
      else { measuring = false; document.exitPointerLock && document.exitPointerLock();
        var inches = (+$('dpi-dist').value) / ($('dpi-unit').value === 'cm' ? 2.54 : 1);
        var dpi = Math.round(Math.abs(counts) / inches); $('dpi-out').textContent = dpi ? '≈ ' + dpi + ' DPI (counts: ' + Math.abs(counts) + ')' : 'No movement detected — try again';
        dpiBox.textContent = 'Click to start a new measurement'; }
    });
    document.addEventListener('mousemove', function (e) { if (measuring && document.pointerLockElement === dpiBox) counts += e.movementX; });
  }

  /* ===== Aiming-off calculator (navigation) ===== */
  var ao = $('ao-form');
  if (ao) {
    var f4 = function () {
      var d = +$('ao-dist').value, ang = +$('ao-ang').value, err = +$('ao-err').value, rad = Math.PI / 180;
      var off = d * Math.tan(ang * rad), cone = d * Math.tan(err * rad);
      $('ao-off').textContent = Math.round(off) + ' m';
      $('ao-cone').textContent = '± ' + Math.round(cone) + ' m';
      $('ao-verdict').textContent = ang > err ? '✅ Safe: your aim-off angle exceeds your expected bearing error, so you will hit the line feature on the known side.' :
        '⚠️ Increase the aim-off angle above ' + err + '° — with this setting you could end up on either side of the target.';
    };
    ao.addEventListener('input', f4); f4();
  }
})();
