const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const source = readFileSync('docs/assets/javascripts/popularity.js', 'utf8');
function setup(data, ok = true) {
  const makeElement = () => ({ hidden: true, isConnected: true, textContent: '', getAttribute: () => '../assets/analytics-stats.json' });
  let element = makeElement();
  let callback;
  const urls = [];
  const context = {
    document: { baseURI: 'http://localhost:8765/AIUserManual/chapter/', getElementById: () => element },
    window: { location: { origin: 'http://localhost:8765' } },
    document$: { subscribe: fn => { callback = fn; fn(); } }, URL,
    fetch: async url => { urls.push(url); return { ok, json: async () => data }; }
  };
  runInNewContext(source, context);
  return { urls, get element() { return element; }, navigate() { element.isConnected = false; element = makeElement(); callback(); } };
}
const settle = () => new Promise(resolve => setImmediate(resolve));
test('uses preview origin and reinitializes after instant navigation', async () => {
  const app = setup({ totalPageViews: 1234, updatedAt: '2026-09-11T10:00:00Z' });
  await settle();
  assert.equal(app.urls[0], 'http://localhost:8765/AIUserManual/assets/analytics-stats.json');
  assert.equal(app.element.hidden, false);
  assert.match(app.element.textContent, /1,234.*2026-09-11/);
  app.navigate();
  await settle();
  assert.equal(app.element.hidden, false);
  assert.equal(app.urls.length, 2);
});
test('zero is a valid count', async () => {
  const app = setup({ totalPageViews: 0 }); await settle();
  assert.equal(app.element.hidden, false);
  assert.match(app.element.textContent, /约 0 次/);
});
test('missing, malformed and negative values stay hidden', async () => {
  for (const value of [null, '', '12oops', -1, 1.5, undefined]) {
    const app = setup({ totalPageViews: value }); await settle();
    assert.equal(app.element.hidden, true);
    assert.equal(app.element.textContent, '');
  }
});
test('network failure hides optional statistics', async () => {
  const app = setup({}, false); await settle();
  assert.equal(app.element.hidden, true);
});
