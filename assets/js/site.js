// ShiftFlow marketing site: phone mockups, navigation and reveal-on-scroll.
// No dependencies.
(function () {
  'use strict';

  // The employee app Home screen is written once, as a <template>, and drawn
  // into every phone that asks for it.
  document.querySelectorAll('[data-clone]').forEach(function (el) {
    var tpl = document.getElementById(el.getAttribute('data-clone'));
    if (tpl && tpl.content) el.appendChild(tpl.content.cloneNode(true));
  });

  // Each mockup is laid out at 250px wide and scaled to whatever size its
  // phone frame is drawn at, so the hero phone and the card phone match.
  var screens = document.querySelectorAll('.phone__screen');
  function fit(el) { el.style.setProperty('--s', String(el.clientWidth / 250)); }
  screens.forEach(fit);
  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(function (entries) { entries.forEach(function (e) { fit(e.target); }); });
    screens.forEach(function (el) { ro.observe(el); });
  }

  // Navigation: solid once scrolled, toggle on small screens.
  var nav = document.getElementById('nav');
  var toggle = document.getElementById('navToggle');
  function onScroll() { nav.classList.toggle('is-scrolled', window.scrollY > 24); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
  document.querySelectorAll('#navLinks a').forEach(function (a) {
    a.addEventListener('click', function () {
      nav.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });

  // Reveal sections as they scroll into view.
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Partner logos open in a new tab; drop focus after a mouse click so no ring is left behind.
  document.querySelectorAll('.partner a').forEach(function (a) {
    a.addEventListener('click', function (e) { if (e.detail > 0) a.blur(); });
  });

  // Custom dropdown for <select data-enhance>. The native select stays in the form
  // (hidden) so the value is submitted and the page still works without JavaScript.
  var CHEV = '<svg class="select__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>';
  var TICK = '<svg class="select__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';
  function iconSvg(id) {
    return id && document.getElementById(id)
      ? '<svg class="select__ico" viewBox="0 0 24 24" aria-hidden="true"><use href="#' + id + '"/></svg>' : '';
  }
  var uid = 0;
  document.querySelectorAll('select[data-enhance]').forEach(function (sel) {
    var n = ++uid;
    var wrap = document.createElement('div');
    wrap.className = 'select';
    sel.parentNode.insertBefore(wrap, sel);

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'select__btn';
    btn.id = 'select-btn-' + n;
    btn.setAttribute('aria-haspopup', 'listbox');
    btn.setAttribute('aria-expanded', 'false');
    var labelId = sel.getAttribute('aria-labelledby');
    btn.setAttribute('aria-labelledby', (labelId ? labelId + ' ' : '') + btn.id);

    var list = document.createElement('ul');
    list.className = 'select__list';
    list.id = 'select-list-' + n;
    list.setAttribute('role', 'listbox');
    list.tabIndex = -1;
    if (labelId) list.setAttribute('aria-labelledby', labelId);
    btn.setAttribute('aria-controls', list.id);

    var opts = [];
    Array.prototype.forEach.call(sel.options, function (o, i) {
      if (o.disabled && !o.value) return; // the "Choose one" placeholder
      var li = document.createElement('li');
      li.className = 'select__opt';
      li.id = list.id + '-' + i;
      li.setAttribute('role', 'option');
      li.dataset.index = String(i);
      li.innerHTML = iconSvg(o.dataset.icon) + '<span></span>' + TICK;
      li.querySelector('span').textContent = o.text;
      list.appendChild(li);
      opts.push(li);
    });

    wrap.appendChild(btn);
    wrap.appendChild(list);
    wrap.appendChild(sel);
    sel.tabIndex = -1;
    sel.setAttribute('aria-hidden', 'true');

    var active = -1;
    function sync() {
      var o = sel.options[sel.selectedIndex];
      var empty = !o || !o.value && o.disabled;
      btn.classList.toggle('is-placeholder', empty);
      btn.innerHTML = (empty ? '' : iconSvg(o.dataset.icon)) + '<span class="select__val"></span>' + CHEV;
      btn.querySelector('.select__val').textContent = o ? o.text : '';
      opts.forEach(function (li) { li.setAttribute('aria-selected', String(Number(li.dataset.index) === sel.selectedIndex)); });
      if (!empty) wrap.classList.remove('is-invalid');
    }
    function setActive(i) {
      if (!opts.length) return;
      active = (i + opts.length) % opts.length;
      opts.forEach(function (li, j) { li.classList.toggle('is-active', j === active); });
      list.setAttribute('aria-activedescendant', opts[active].id);
      var li = opts[active];
      if (li.offsetTop < list.scrollTop) list.scrollTop = li.offsetTop - 6;
      else if (li.offsetTop + li.offsetHeight > list.scrollTop + list.clientHeight) list.scrollTop = li.offsetTop + li.offsetHeight - list.clientHeight + 6;
    }
    function open() {
      if (wrap.classList.contains('is-open')) return;
      var below = window.innerHeight - btn.getBoundingClientRect().bottom;
      wrap.classList.toggle('is-up', below < 340 && btn.getBoundingClientRect().top > below);
      wrap.classList.add('is-open');
      btn.setAttribute('aria-expanded', 'true');
      var cur = opts.findIndex(function (li) { return li.getAttribute('aria-selected') === 'true'; });
      setActive(cur < 0 ? 0 : cur);
      list.focus({ preventScroll: true });
    }
    function close(refocus) {
      if (!wrap.classList.contains('is-open')) return;
      wrap.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
      list.removeAttribute('aria-activedescendant');
      if (refocus) btn.focus();
    }
    function choose(i) {
      sel.selectedIndex = Number(opts[i].dataset.index);
      sel.dispatchEvent(new Event('change', { bubbles: true }));
      sync();
      close(true);
    }

    btn.addEventListener('click', function () { wrap.classList.contains('is-open') ? close(true) : open(); });
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); open(); }
    });
    list.addEventListener('click', function (e) {
      var li = e.target.closest('.select__opt');
      if (li) choose(opts.indexOf(li));
    });
    list.addEventListener('mousemove', function (e) {
      var li = e.target.closest('.select__opt');
      if (li && opts.indexOf(li) !== active) setActive(opts.indexOf(li));
    });
    var typed = '', typedAt = 0;
    list.addEventListener('keydown', function (e) {
      switch (e.key) {
        case 'ArrowDown': e.preventDefault(); setActive(active + 1); break;
        case 'ArrowUp': e.preventDefault(); setActive(active - 1); break;
        case 'Home': e.preventDefault(); setActive(0); break;
        case 'End': e.preventDefault(); setActive(opts.length - 1); break;
        case 'Enter': case ' ': e.preventDefault(); if (active >= 0) choose(active); break;
        case 'Escape': e.preventDefault(); close(true); break;
        case 'Tab': close(false); break;
        default:
          if (e.key.length === 1 && /\S/.test(e.key)) {
            var now = Date.now();
            typed = (now - typedAt > 700 ? '' : typed) + e.key.toLowerCase();
            typedAt = now;
            var hit = opts.findIndex(function (li) { return li.textContent.trim().toLowerCase().indexOf(typed) === 0; });
            if (hit >= 0) setActive(hit);
          }
      }
    });
    document.addEventListener('pointerdown', function (e) { if (!wrap.contains(e.target)) close(false); });
    if (sel.form) sel.form.addEventListener('reset', function () { setTimeout(sync, 0); });

    // Lets the form handler check the choice, since the hidden select cannot show the browser's bubble.
    wrap.validate = function () {
      var ok = !sel.required || !!sel.value;
      wrap.classList.toggle('is-invalid', !ok);
      if (!ok) btn.focus();
      return ok;
    };
    sync();
  });

  // Contact form: post to the BTree contact API (Cloudflare Worker) and show the result in place.
  // Add ?localapi to the page URL to post to `wrangler dev` instead of the live API.
  var LOCAL_API = 'http://localhost:8787/contact';

  // Email checks. The same format rule runs in the Worker, which also checks that the
  // domain can receive mail and is not a throwaway inbox.
  var EMAIL_RE = /^[a-z0-9.!#$%&'*+/=?^_`{|}~-]+@(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/i;
  var COMMON_DOMAINS = ['gmail.com', 'googlemail.com', 'outlook.com', 'hotmail.com', 'hotmail.co.uk', 'live.com', 'live.co.uk',
    'msn.com', 'yahoo.com', 'yahoo.co.uk', 'icloud.com', 'me.com', 'aol.com', 'btinternet.com', 'sky.com', 'virginmedia.com',
    'talktalk.net', 'protonmail.com', 'proton.me'];
  var TLD_TYPOS = { '.con': '.com', '.cmo': '.com', '.ocm': '.com', '.vom': '.com', '.xom': '.com', '.comm': '.com',
    '.co.uj': '.co.uk', '.co.ul': '.co.uk', '.co.k': '.co.uk', '.couk': '.co.uk', '.ukk': '.uk' };

  function emailFormatError(v) {
    if (!v) return 'Please enter your email address.';
    var local = v.split('@')[0];
    if (v.length > 254 || !EMAIL_RE.test(v) || local.length > 64 || v.indexOf('..') >= 0 || /^\.|\.$/.test(local)) {
      return 'Please enter a valid email address, like name@company.co.uk.';
    }
    return '';
  }
  function editDistance(a, b) {
    var prev = [], i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      var cur = [i];
      for (j = 1; j <= b.length; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      }
      prev = cur;
    }
    return prev[b.length];
  }
  // "name@gmial.com" -> "name@gmail.com". Only a suggestion; the visitor decides.
  function suggestEmail(v) {
    var at = v.lastIndexOf('@');
    if (at < 1) return '';
    var domain = v.slice(at + 1).toLowerCase();
    if (!domain || COMMON_DOMAINS.indexOf(domain) >= 0) return '';
    var fixed = domain;
    Object.keys(TLD_TYPOS).some(function (t) {
      if (fixed.slice(-t.length) === t) { fixed = fixed.slice(0, -t.length) + TLD_TYPOS[t]; return true; }
      return false;
    });
    var best = '', bestD = Infinity;
    COMMON_DOMAINS.forEach(function (c) { var d = editDistance(fixed, c); if (d < bestD) { bestD = d; best = c; } });
    if (best && bestD > 0 && bestD <= (fixed.length < 8 ? 1 : 2)) fixed = best;
    else if (best && bestD === 0) fixed = best;
    return fixed !== domain ? v.slice(0, at + 1) + fixed : '';
  }

  // Turnstile spam check, rendered by hand so its size fits the form: the normal and
  // flexible widgets need at least 300px, so narrow phones get the compact one.
  var turnstiles = document.querySelectorAll('.turnstile');
  function renderTurnstiles() {
    turnstiles.forEach(function (el) {
      if (el.dataset.widgetId) return;
      el.dataset.widgetId = window.turnstile.render(el, {
        // With ?localapi (local Worker), use Cloudflare's always-pass test key: the real key only works on btree.uk.
        sitekey: /[?&]localapi(=|&|$)/.test(location.search) ? '1x00000000000000000000AA' : el.dataset.sitekey,
        theme: 'dark',
        size: el.clientWidth < 300 ? 'compact' : 'flexible',
      });
    });
  }
  if (turnstiles.length) {
    var waited = 0;
    (function waitForTurnstile() {
      if (window.turnstile && window.turnstile.render) renderTurnstiles(); // ready() is not allowed with async api.js
      else if ((waited += 100) < 20000) setTimeout(waitForTurnstile, 100);
    })();
  }

  document.querySelectorAll('form[data-contact]').forEach(function (form) {
    var status = form.querySelector('.form__status');
    var button = form.querySelector('button[type="submit"]');
    var email = form.querySelector('input[name="email"]');
    function show(msg, kind) { status.textContent = msg; status.className = 'form__status is-' + kind; }
    // Validation is run by hand below, so the hidden select behind a custom dropdown
    // cannot silently block the submit.
    form.noValidate = true;
    form.addEventListener('change', function () { if (status.classList.contains('is-error')) show('', 'pending'); });

    // A message line under the email field, for errors and typo suggestions.
    var msg = document.createElement('p');
    msg.className = 'field__msg';
    msg.id = 'email-msg-' + Math.random().toString(36).slice(2, 8);
    msg.setAttribute('aria-live', 'polite');
    email.insertAdjacentElement('afterend', msg);
    email.setAttribute('aria-describedby', msg.id);

    // Appends "Did you mean <button>name@gmail.com</button>?" to the message line.
    function addSuggestion(suggestion, lead) {
      msg.appendChild(document.createTextNode(lead + 'Did you mean '));
      var fix = document.createElement('button');
      fix.type = 'button';
      fix.className = 'field__fix';
      fix.textContent = suggestion;
      fix.addEventListener('click', function () {
        email.value = suggestion;
        emailError('');
        email.focus();
        checkRemote(suggestion.toLowerCase());
      });
      msg.appendChild(fix);
      msg.appendChild(document.createTextNode('?'));
    }
    function emailError(text) {
      msg.className = 'field__msg' + (text ? ' is-error' : '');
      msg.textContent = text || '';
      email.setAttribute('aria-invalid', text ? 'true' : 'false');
      var suggestion = text && suggestEmail(email.value.trim());
      if (suggestion) addSuggestion(suggestion, ' ');
    }
    function emailHint(suggestion) {
      msg.className = 'field__msg is-hint';
      msg.textContent = '';
      email.setAttribute('aria-invalid', 'false');
      addSuggestion(suggestion, '');
    }

    // Ask the Worker whether the domain can receive email. Results are remembered per address.
    var useLocal = /[?&]localapi(=|&|$)/.test(location.search);
    var checkApi = (useLocal ? LOCAL_API : form.action).replace(/\/contact$/, '/check-email');
    var remote = {};
    function checkRemote(v) {
      if (remote[v] !== undefined) { if (remote[v]) emailError(remote[v]); return; }
      fetch(checkApi, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email: v }) })
        .then(function (res) { return res.json(); })
        .then(function (out) {
          remote[v] = out && out.ok === false && out.error ? out.error : '';
          if (remote[v] && email.value.trim().toLowerCase() === v) emailError(remote[v]);
        })
        .catch(function () { /* offline or blocked: the server checks again on submit */ });
    }
    function checkEmail(live) {
      var v = email.value.trim();
      if (v !== email.value) email.value = v;
      var err = emailFormatError(v);
      if (err) { emailError(err); return false; }
      var key = v.toLowerCase();
      if (remote[key]) { emailError(remote[key]); return false; }
      var suggestion = suggestEmail(v);
      if (suggestion) emailHint(suggestion); else emailError('');
      if (live) checkRemote(key);
      return true;
    }
    email.addEventListener('blur', function () { if (email.value.trim()) checkEmail(true); });
    email.addEventListener('input', function () { if (msg.classList.contains('is-error')) emailError(''); });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      // Custom dropdowns first: their hidden select cannot show the browser's own message.
      var bad = Array.prototype.find.call(form.querySelectorAll('.select'), function (w) { return w.validate && !w.validate(); });
      if (bad) { show('Please choose what you need help with.', 'error'); return; }
      if (!checkEmail(false)) { email.focus(); show('Please check your email address.', 'error'); return; }
      if (!form.reportValidity()) return;
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.turnstileToken = data['cf-turnstile-response'] || '';
      delete data['cf-turnstile-response'];
      data.page = location.pathname;
      if (!data.turnstileToken) { show('Please wait for the spam check to finish, then try again.', 'error'); return; }

      var api = /[?&]localapi(=|&|$)/.test(location.search) ? LOCAL_API : form.action;
      button.disabled = true;
      show('Sending…', 'pending');
      fetch(api, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (res) {
          return res.json().catch(function () { return {}; }).then(function (out) {
            if (!res.ok) { var er = new Error(out.error || 'Something went wrong.'); er.field = out.field; throw er; }
          });
        })
        .then(function () {
          form.reset();
          emailError('');
          form.classList.add('is-sent');
          show('Thank you. We have your message and will be in touch soon.', 'ok');
        })
        .catch(function (err) {
          if (err && err.field === 'email') {
            remote[email.value.trim().toLowerCase()] = err.message;
            emailError(err.message);
            email.focus();
            show('Please check your email address.', 'error');
          } else {
            var text = err && err.message && err.message !== 'Failed to fetch' ? err.message : 'We could not send your message.';
            show(text + ' Please try again, or email info@btree.uk.', 'error');
          }
          var ts = form.querySelector('.turnstile');
          if (window.turnstile && ts && ts.dataset.widgetId) window.turnstile.reset(ts.dataset.widgetId);
        })
        .then(function () { button.disabled = false; });
    });
  });

  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
