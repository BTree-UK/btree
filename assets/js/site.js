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

  document.getElementById('year').textContent = String(new Date().getFullYear());
})();
