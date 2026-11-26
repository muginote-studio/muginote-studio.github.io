'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const code = fs.readFileSync(__dirname + '/site.js', 'utf8');
function setup(mobile) {
  const callbacks = {};
  const attrs = {'aria-expanded': 'false'};
  const button = {textContent: 'メニュー', getAttribute: k => attrs[k], setAttribute: (k,v) => {attrs[k]=v;}, addEventListener: (k,fn) => {callbacks['button:'+k]=fn;}, focus: () => {button.focused=true;}};
  const nav = {hidden: false, addEventListener: (k,fn) => {callbacks['nav:'+k]=fn;}};
  const media = {matches: mobile, addEventListener: (k,fn) => {callbacks['media:'+k]=fn;}};
  const document = {querySelector: s => s==='.menu-toggle' ? button : nav, documentElement: {classList: {add: c => {callbacks.enhanced=c;}}}, addEventListener: (k,fn) => {callbacks['document:'+k]=fn;}};
  vm.runInNewContext(code, {document, window: {matchMedia: () => media}});
  return {button,nav,attrs,callbacks,media};
}
test('mobile menu starts collapsed; button opens and closes it', () => {
  const x=setup(true);assert.equal(x.nav.hidden,true);assert.equal(x.callbacks.enhanced,'enhanced');
  x.callbacks['button:click']();assert.equal(x.nav.hidden,false);assert.equal(x.attrs['aria-expanded'],'true');assert.equal(x.button.textContent,'閉じる');
  x.callbacks['button:click']();assert.equal(x.nav.hidden,true);assert.equal(x.attrs['aria-expanded'],'false');
});
test('mobile menu link closes navigation', () => {
  const x=setup(true);x.callbacks['button:click']();x.callbacks['nav:click']({target:{closest:()=>({})}});assert.equal(x.nav.hidden,true);
});
test('Escape closes navigation and restores focus', () => {
  const x=setup(true);x.callbacks['button:click']();x.callbacks['document:keydown']({key:'Escape'});assert.equal(x.nav.hidden,true);assert.equal(x.button.focused,true);
});
test('desktop navigation stays visible and responsive changes reset state', () => {
  const x=setup(false);assert.equal(x.nav.hidden,false);x.media.matches=true;x.callbacks['media:change']();assert.equal(x.nav.hidden,true);
  x.media.matches=false;x.callbacks['media:change']();assert.equal(x.nav.hidden,false);assert.equal(x.attrs['aria-expanded'],'false');
});
test('missing navigation exits without an error', () => {
  vm.runInNewContext(code,{document:{querySelector:()=>null}});
});
