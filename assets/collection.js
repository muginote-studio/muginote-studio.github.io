(() => {
  const controls = document.querySelector('.gallery-controls');
  const form = document.querySelector('#collection-search');
  const search = document.querySelector('#shop-search');
  const region = document.querySelector('#region-filter');
  const clear = document.querySelector('#clear-filters');
  const status = document.querySelector('#filter-status');
  const empty = document.querySelector('#gallery-empty');
  const cards = [...document.querySelectorAll('.gallery-card')];
  const buttons = [...document.querySelectorAll('[data-filter]')];
  if (!controls || !form || !search || !region || !clear || !status || !empty) return;

  const normalize = value => String(value).normalize('NFKC').toLocaleLowerCase('ja').replace(/\s+/g, ' ').trim();
  const entries = cards.map(card => ({card, text: normalize(card.dataset.search || card.textContent)}));
  let category = 'all';

  function update() {
    const terms = normalize(search.value).split(' ').filter(Boolean);
    let count = 0;
    entries.forEach(({card, text}) => {
      const visible = (category === 'all' || card.dataset.category === category)
        && (region.value === 'all' || card.dataset.region === region.value)
        && terms.every(term => text.includes(term));
      card.hidden = !visible;
      if (visible) count++;
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === category)));
    status.textContent = `${count}件 / ${cards.length}件のデザイン`;
    empty.hidden = count !== 0;
  }

  form.addEventListener('submit', event => event.preventDefault());
  search.addEventListener('input', update);
  search.addEventListener('search', update);
  region.addEventListener('change', update);
  buttons.forEach(button => button.addEventListener('click', () => {
    category = button.dataset.filter;
    update();
  }));
  clear.addEventListener('click', () => {
    category = 'all';
    search.value = '';
    region.value = 'all';
    update();
    search.focus();
  });
  controls.hidden = false;
  update();
})();
