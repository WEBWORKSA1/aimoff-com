/* AimOff.com — site-wide behaviour (no framework, GitHub Pages friendly). */
(function () {
  'use strict';

  /* ---------- Contact routing (address is never written in plain text) ---------- */
  var _p = ['bW9jLmxp', 'YW1nQDFh', 'c2tyb3diZXc='];
  function inbox() { try { return atob(_p.join('')).split('').reverse().join(''); } catch (e) { return ''; } }
  window.AIMOFF = window.AIMOFF || {};
  var CFG = window.AIMOFF;

  // Any element with [data-mail] opens the mail client only when clicked.
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-mail]');
    if (!a) return;
    e.preventDefault();
    var subj = a.getAttribute('data-mail') || 'AimOff.com enquiry';
    window.location.href = 'mai' + 'lto:' + inbox() + '?subject=' + encodeURIComponent(subj);
  });

  /* ---------- Theme ---------- */
  var root = document.documentElement;
  function setTheme(t) { root.setAttribute('data-theme', t); try { localStorage.setItem('aimoff-theme', t); } catch (e) {} }
  try { var saved = localStorage.getItem('aimoff-theme'); if (saved) root.setAttribute('data-theme', saved); } catch (e) {}
  document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
    b.addEventListener('click', function () { setTheme(root.getAttribute('data-theme') === 'light' ? 'dark' : 'light'); });
  });

  /* ---------- Mobile nav ---------- */
  var burger = document.querySelector('.burger'), links = document.querySelector('.nav-links');
  if (burger && links) burger.addEventListener('click', function () {
    var open = links.classList.toggle('open'); burger.setAttribute('aria-expanded', open);
  });

  /* ---------- Year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Prefill fields from query string (?game=valorant&score=123) ---------- */
  var qs = new URLSearchParams(location.search);
  qs.forEach(function (v, k) {
    document.querySelectorAll('[name="' + CSS.escape(k) + '"]').forEach(function (f) {
      if (f.type === 'radio' || f.type === 'checkbox') { if (f.value === v) f.checked = true; }
      else if (f.tagName === 'SELECT') { if ([].some.call(f.options, function (o) { return (o.value || o.text) === v; })) f.value = v; }
      else if (f.type !== 'hidden' && !f.value) f.value = v;
    });
  });

  /* ---------- Forms -> inbox via FormSubmit AJAX endpoint ---------- */
  function endpoint() { return 'https://formsubmit.co/ajax/' + inbox(); }
  document.querySelectorAll('form.js-form').forEach(function (form) {
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var hp = form.querySelector('[name="_honey"]');
      if (hp && hp.value) return; // bot
      var data = {};
      new FormData(form).forEach(function (v, k) {
        if (k === '_honey') return;
        data[k] = data[k] ? data[k] + ', ' + v : v;
      });
      data._subject = '[AimOff.com] ' + (form.getAttribute('data-subject') || 'Website enquiry');
      data._template = 'table';
      data._captcha = 'false';
      data.page = location.href;
      data.submitted = new Date().toISOString();
      var btn = form.querySelector('[type="submit"]');
      if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = 'Sending…'; }
      fetch(endpoint(), { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
        .then(function () {
          if (msg) { msg.className = 'form-msg ok'; msg.textContent = form.getAttribute('data-success') || 'Thanks! Your message is in. We reply within 1–2 business days.'; }
          form.reset();
          if (typeof window.gtag === 'function') window.gtag('event', 'generate_lead', { form: form.getAttribute('data-subject') });
        })
        .catch(function () {
          if (msg) {
            msg.className = 'form-msg err';
            msg.innerHTML = 'Could not send right now. <a href="#" data-mail="' + (form.getAttribute('data-subject') || 'AimOff.com enquiry') + '">Click here to email us instead</a>.';
          }
        })
        .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; } });
    });
  });

  /* ---------- Multi-step forms ---------- */
  document.querySelectorAll('[data-steps]').forEach(function (form) {
    var steps = form.querySelectorAll('.step'), bars = form.querySelectorAll('.steps span'), i = 0;
    function show(n) {
      i = n;
      steps.forEach(function (s, k) { s.classList.toggle('on', k === n); });
      bars.forEach(function (b, k) { b.classList.toggle('on', k <= n); });
    }
    form.addEventListener('click', function (e) {
      if (e.target.matches('[data-next]')) {
        var ok = true;
        steps[i].querySelectorAll('input,select,textarea').forEach(function (f) { if (!f.checkValidity()) { ok = false; f.reportValidity(); } });
        if (ok) show(Math.min(i + 1, steps.length - 1));
      }
      if (e.target.matches('[data-prev]')) show(Math.max(i - 1, 0));
    });
    show(0);
  });

  /* ---------- Ads: AdSense when configured, otherwise sponsor house ads ---------- */
  var meta = document.querySelector('meta[name="google-adsense-account"]');
  var client = meta ? meta.content : '';
  var consent = null; try { consent = localStorage.getItem('aimoff-consent'); } catch (e) {}
  var houseAds = [
    ['Your brand here', 'Reach gamers who train their aim every day. Sponsor a tool, contest or video.'],
    ['Sponsor the AimOff Open', 'Put your gear in front of competitive players. Prize-pool partnerships open.'],
    ['Advertise on AimOff', 'Banner, newsletter and contest packages for gaming & esports brands.']
  ];
  document.querySelectorAll('.ad-slot').forEach(function (slot, n) {
    if (client && consent !== 'essential') {
      // No ad-unit ID on this slot: remove the placeholder and let AdSense Auto ads place ads.
      if (!slot.getAttribute('data-slot')) { slot.remove(); return; }
      slot.classList.add('has-ad');
      slot.innerHTML = '<div style="width:100%"><span class="ad-label">Advertisement</span><ins class="adsbygoogle" style="display:block" data-ad-client="' + client +
        '" data-ad-slot="' + (slot.getAttribute('data-slot') || '') + '" data-ad-format="auto" data-full-width-responsive="true"></ins></div>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    } else {
      var h = houseAds[n % houseAds.length];
      slot.innerHTML = '<a class="house-ad" href="https://web.works/contact" target="_blank" rel="noopener"><span class="ad-label">Sponsored space</span><b>' + h[0] + '</b> — ' + h[1] + '</a>';
    }
  });

  /* ---------- Cookie / consent banner ---------- */
  var ck = document.getElementById('cookie');
  if (ck && !consent) ck.hidden = false;
  document.querySelectorAll('[data-consent]').forEach(function (b) {
    b.addEventListener('click', function () {
      try { localStorage.setItem('aimoff-consent', b.getAttribute('data-consent')); } catch (e) {}
      if (ck) ck.hidden = true;
    });
  });

  /* ---------- Lite YouTube embeds (fast pages, no tracking until click) ---------- */
  document.querySelectorAll('.yt[data-id]').forEach(function (el) {
    var id = el.getAttribute('data-id');
    el.innerHTML = '<img loading="lazy" alt="' + (el.getAttribute('data-title') || 'Video') + '" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg">';
    el.setAttribute('role', 'button'); el.setAttribute('tabindex', '0');
    function play() {
      el.classList.add('playing');
      el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (el.getAttribute('data-title') || 'Video') +
        '" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
    }
    el.addEventListener('click', play);
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter') play(); });
  });

  /* ---------- Donations (PayPal donate link built at click time) ---------- */
  var amount = 15;
  document.querySelectorAll('.tier').forEach(function (t) {
    t.addEventListener('click', function () {
      document.querySelectorAll('.tier').forEach(function (x) { x.classList.remove('on'); });
      t.classList.add('on'); amount = t.getAttribute('data-amount');
      var c = document.getElementById('custom-amount'); if (c) c.value = amount;
    });
  });
  document.querySelectorAll('[data-donate]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      var c = document.getElementById('custom-amount');
      var amt = (c && c.value) ? c.value : (b.getAttribute('data-donate') || amount);
      var purpose = (document.getElementById('donate-purpose') || {}).value || 'General support';
      var url = 'https://www.paypal.com/donate/?business=' + encodeURIComponent(inbox()) +
        '&amount=' + encodeURIComponent(amt) + '&currency_code=USD&no_recurring=0&item_name=' + encodeURIComponent('AimOff.com — ' + purpose);
      window.open(url, '_blank', 'noopener');
    });
  });

  /* ---------- Lead-magnet modal (shown once, after engagement) ---------- */
  var modal = document.getElementById('lead-modal');
  function openModal() { if (modal) { modal.hidden = false; try { sessionStorage.setItem('aimoff-modal', '1'); } catch (e) {} } }
  if (modal) {
    var seen = null; try { seen = sessionStorage.getItem('aimoff-modal'); } catch (e) {}
    if (!seen) {
      setTimeout(openModal, 45000);
      document.addEventListener('mouseout', function (e) { if (!e.relatedTarget && e.clientY < 5) { try { if (!sessionStorage.getItem('aimoff-modal')) openModal(); } catch (x) {} } });
    }
    modal.addEventListener('click', function (e) { if (e.target === modal || e.target.matches('.close')) modal.hidden = true; });
  }
  window.AIMOFF.openLeadModal = openModal;

  /* ---------- Reveal on scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }); }, { threshold: .12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });

  /* ---------- Share helper ---------- */
  window.AIMOFF.share = function (text) {
    var url = location.origin + location.pathname;
    if (navigator.share) { navigator.share({ title: 'AimOff', text: text, url: url }).catch(function () {}); }
    else if (navigator.clipboard) { navigator.clipboard.writeText(text + ' ' + url); alert('Result copied — paste it anywhere!'); }
  };

  /* ---------- Local leaderboard store ---------- */
  window.AIMOFF.store = {
    get: function (k, d) { try { var v = localStorage.getItem('aimoff-' + k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem('aimoff-' + k, JSON.stringify(v)); } catch (e) {} }
  };
})();
