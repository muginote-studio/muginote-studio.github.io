(() => {
  'use strict';
  const button = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  if (!button || !nav) return;
  const narrow = window.matchMedia('(max-width: 680px)');
  const close = () => {
    button.setAttribute('aria-expanded', 'false');
    button.textContent = 'メニュー';
    nav.hidden = narrow.matches;
  };
  document.documentElement.classList.add('enhanced');
  close();
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    button.textContent = open ? '閉じる' : 'メニュー';
    nav.hidden = !open;
  });
  nav.addEventListener('click', (event) => {
    if (event.target.closest('a') && narrow.matches) close();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') {
      close();
      button.focus();
    }
  });
  if (narrow.addEventListener) narrow.addEventListener('change', close);
  else narrow.addListener(close);
})();
