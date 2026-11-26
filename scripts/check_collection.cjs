const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'assets/collection.js'), 'utf8');
const collection = JSON.parse(fs.readFileSync(path.join(root, 'collections/index.json'), 'utf8'));
class Element {
  constructor(dataset = {}) { this.dataset = dataset; this.listeners = {}; this.hidden = true; this.value = ''; this.attributes = {}; this.textContent = ''; }
  addEventListener(type, fn) { (this.listeners[type] ||= []).push(fn); }
  setAttribute(name, value) { this.attributes[name] = value; }
  focus() { this.focused = true; }
  fire(type, event = {}) { (this.listeners[type] || []).forEach(fn => fn(event)); }
}
function setup() {
  const ids = ['.gallery-controls','#collection-search','#shop-search','#region-filter','#clear-filters','#filter-status','#gallery-empty'];
  const nodes = Object.fromEntries(ids.map(id => [id, new Element()]));
  nodes['#region-filter'].value = 'all';
  const cards = collection.map(row => { const e = new Element({category:row.category,region:row.region,search:`${row.name} ${row.place} ${row.slug}`});e.id=row.id;return e; });
  const buttons = ['all','tea','sweets','coffee','meal','bar','bakery'].map(filter => new Element({filter}));
  const document = {querySelector:s => nodes[s],querySelectorAll:s => s === '.gallery-card' ? cards : buttons};
  vm.runInNewContext(source, {document});
  return {nodes,cards,buttons,visible:() => cards.filter(c => !c.hidden).map(c => c.id)};
}
test('all 100 concepts are shown on startup', () => {
  const x = setup();assert.equal(x.visible().length,100);assert.equal(x.nodes['.gallery-controls'].hidden,false);
  assert.equal(x.nodes['#filter-status'].textContent,'100件 / 100件のデザイン');assert.equal(x.nodes['#gallery-empty'].hidden,true);
});
test('fullwidth case-insensitive store search finds mico', () => {
  const x=setup();x.nodes['#shop-search'].value='ＭＩＣＯ';x.nodes['#shop-search'].fire('input');assert.deepEqual(x.visible(),['CAFE-041']);
});
test('search combines multiple words and region', () => {
  const x=setup();x.nodes['#shop-search'].value='北海道 HOKI';x.nodes['#shop-search'].fire('input');assert.deepEqual(x.visible(),['CAFE-011']);
  x.nodes['#region-filter'].value='京都府';x.nodes['#region-filter'].fire('change');assert.equal(x.visible().length,0);assert.equal(x.nodes['#gallery-empty'].hidden,false);
});
test('Kyoto region includes an existing concept and a newly added concept', () => {
  const x=setup();x.nodes['#region-filter'].value='京都府';x.nodes['#region-filter'].fire('change');assert.deepEqual(x.visible(),['CAFE-009','CAFE-061']);
});
test('category selection updates accessible state and clear restores everything', () => {
  const x=setup(),bar=x.buttons.find(b=>b.dataset.filter==='bar');bar.fire('click');assert.equal(x.visible().length,5);assert.equal(bar.attributes['aria-pressed'],'true');
  x.nodes['#shop-search'].value='存在しないお店xyz';x.nodes['#shop-search'].fire('search');assert.equal(x.visible().length,0);
  x.nodes['#clear-filters'].fire('click');assert.equal(x.visible().length,100);assert.equal(x.nodes['#gallery-empty'].hidden,true);assert.equal(x.nodes['#shop-search'].focused,true);
  assert.equal(x.buttons.find(b=>b.dataset.filter==='all').attributes['aria-pressed'],'true');
});
test('form submission does not navigate and unrelated pages exit safely', () => {
  const x=setup();let prevented=false;x.nodes['#collection-search'].fire('submit',{preventDefault(){prevented=true;}});assert.equal(prevented,true);
  assert.doesNotThrow(()=>vm.runInNewContext(source,{document:{querySelector:()=>null,querySelectorAll:()=>[]}}));
});
