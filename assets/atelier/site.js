(() => {
  const button = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#navigation');
  if (!button || !nav) return;
  function close(restoreFocus = false) {
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-label', 'メニューを開く');
    nav.classList.remove('is-open');
    if (restoreFocus) button.focus();
  }
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'メニューを閉じる' : 'メニューを開く');
    nav.classList.toggle('is-open', open);
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => close()));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') close(true);
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.site-header') && button.getAttribute('aria-expanded') === 'true') close();
  });
  window.matchMedia('(min-width:761px)').addEventListener('change', () => close());
})();
