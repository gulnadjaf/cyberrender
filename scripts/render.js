// Renders HTML slides to 1080x1350 PNGs. Input on stdin: [{"html": path, "png": path}, ...]
// Used by scripts/compose.py. Needs Playwright (global install is fine).
const path = require('path');
const { execSync } = require('child_process');

function loadPlaywright() {
  try { return require('playwright'); } catch (e) {
    return require(path.join(execSync('npm root -g').toString().trim(), 'playwright'));
  }
}

(async () => {
  const jobs = JSON.parse(require('fs').readFileSync(0, 'utf8'));
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const job of jobs) {
    await page.goto('file://' + job.html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: job.png, clip: { x: 0, y: 0, width: 1080, height: 1350 } });
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
