// Prüft eine Hersteller-Produktseite mit echtem Browser (Shops sperren einfache Abrufe oft mit 429).
// Ausgabe: "<HTTP-Status> <finale URL>". Aufruf: node tools/awin-shopcheck.cjs URL
const path = require('path');
let pw;
for (const p of [process.env.PLAYWRIGHT_MODULE, path.join(process.env.HOME || '', '.local/lib/node_modules/@playwright/cli/node_modules/playwright'), 'playwright']) {
  if (!p) continue; try { pw = require(p); break; } catch (e) {}
}
(async () => {
  if (!pw) { console.log('0 kein-playwright'); return; }
  const b = await pw.chromium.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', headless: true, args: ['--no-sandbox', '--headless=new'] });
  try {
    const p = await (await b.newContext({ locale: 'de-DE' })).newPage();
    const r = await p.goto(process.argv[2], { waitUntil: 'domcontentloaded', timeout: 45000 });
    console.log((r ? r.status() : 0) + ' ' + p.url());
  } catch (e) { console.log('0 fehler'); } finally { await b.close(); }
})();
