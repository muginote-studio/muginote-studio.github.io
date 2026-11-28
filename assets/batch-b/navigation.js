'use strict';
(() => {
  const button = document.querySelector('.menu-toggle');
  const nav = document.getElementById('site-nav');
  if (!button || !nav) return;
  document.documentElement.classList.add('js');
  const close = () => {
    nav.removeAttribute('data-open');
    button.setAttribute('aria-expanded', 'false');
  };
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    nav.toggleAttribute('data-open', open);
  });
  nav.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link) return;
    const wasOpen = button.getAttribute('aria-expanded') === 'true';
    close();
    if (!wasOpen) return;
    const href = link.getAttribute('href');
    const target = href && href.startsWith('#') ? document.getElementById(href.slice(1)) : null;
    if (target) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
      target.addEventListener('blur', () => target.removeAttribute('tabindex'), { once: true });
    } else {
      button.focus();
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') {
      close();
      button.focus();
    }
  });
  window.matchMedia('(max-width: 900px)').addEventListener('change', () => {
    const focusWasInside = nav.contains(document.activeElement);
    close();
    if (focusWasInside && window.matchMedia('(max-width: 900px)').matches) button.focus();
  });
})();
