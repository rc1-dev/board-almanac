// Film the Board Almanac demo page as a sequence of held shots.
// Usage: node film.js <docs/index.html> <out-dir> [fonts-dir]
// Writes <out-dir>/NN.jpg and <out-dir>/shots.json ({file, seconds}).
// fonts-dir (optional): a node_modules/@fontsource folder, used when Google Fonts is unreachable.
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const [page_, out, fontsDir] = process.argv.slice(2);
const URL_ = "file://" + path.resolve(page_);
fs.mkdirSync(out, { recursive: true });

const FONT_CSS = fontsDir ? [
  "ibm-plex-sans/400.css", "ibm-plex-sans/500.css", "ibm-plex-sans/600.css", "ibm-plex-sans/400-italic.css",
  "ibm-plex-sans-condensed/500.css", "ibm-plex-sans-condensed/600.css", "ibm-plex-sans-condensed/700.css",
  "ibm-plex-mono/400.css", "ibm-plex-mono/500.css",
  "source-serif-4/400.css", "source-serif-4/600.css", "source-serif-4/400-italic.css"
].map(f => "file://" + path.resolve(fontsDir, f)) : [];

const CARD_CSS = `
  :root { --paper:#0e1418; --ink:#e1e9ed; --muted:#97a8b3; --accent:#62b8cd; --rule:#273540; }
  html,body { margin:0; height:100%; background:var(--paper); color:var(--ink); }
  body { display:grid; place-items:center; font-family:"IBM Plex Sans",system-ui,sans-serif; }
  .card { width: 1040px; }
  .eyebrow { font: 500 15px "IBM Plex Mono", monospace; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }
  h1 { font: 700 84px/1 "IBM Plex Sans Condensed", sans-serif; margin: 14px 0 0; }
  .sub { font: 400 34px/1.3 "Source Serif 4", Georgia, serif; margin: 16px 0 0; }
  .lines { margin-top: 34px; display:grid; gap: 14px; font-size: 25px; line-height:1.35; }
  .lines div { border-left: 4px solid var(--accent); padding-left: 16px; }
  .foot { margin-top: 40px; font: 400 17px "IBM Plex Mono", monospace; color: var(--muted); }
`;

const card = (inner) => `<!doctype html><html><head><meta charset="utf-8">${FONT_CSS.map(h => `<link rel="stylesheet" href="${h}">`).join("")}<style>${CARD_CSS}</style></head><body><div class="card">${inner}</div></body></html>`;

const CAPTION_CSS = `#cap{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);max-width:1100px;width:calc(100% - 80px);
  background:rgba(12,18,22,.92);color:#f2f6f8;font:500 21px/1.38 "IBM Plex Sans",system-ui,sans-serif;padding:13px 22px;border-radius:8px;
  box-shadow:0 6px 24px rgba(0,0,0,.25);z-index:99;text-align:center} #cap:empty{display:none}`;

let n = 0;
const shots = [];

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1.5, colorScheme: "light" });
  const p = await ctx.newPage();
  p.on("pageerror", e => console.error("pageerror", e.message));

  async function snap(seconds) {
    const file = String(++n).padStart(2, "0") + ".jpg";
    await p.waitForTimeout(250);
    await p.screenshot({ path: path.join(out, file), type: "jpeg", quality: 92 });
    shots.push({ file, seconds });
  }
  async function cardShot(inner, seconds) {
    const cf = path.join(out, "card.html"); fs.writeFileSync(cf, card(inner));
    await p.goto("file://" + cf, { waitUntil: "load" });
    await p.evaluate(() => document.fonts.ready);
    await snap(seconds);
  }
  async function open(hash) {
    await p.goto(URL_ + "#" + hash, { waitUntil: "load" });
    await p.evaluate((css) => {
      css.forEach(h => { const l = document.createElement("link"); l.rel = "stylesheet"; l.href = h; document.head.appendChild(l); });
    }, FONT_CSS);
    await p.addStyleTag({ content: CAPTION_CSS });
    await p.evaluate(() => { const c = document.createElement("div"); c.id = "cap"; document.body.appendChild(c); });
    await p.evaluate(() => document.fonts.ready);
  }
  const caption = (t) => p.evaluate(t => { document.getElementById("cap").textContent = t; }, t);
  const toPanel = (extra = 0) => p.evaluate(x => { const h = document.querySelector("header.top"); window.scrollTo(0, h.offsetTop + h.offsetHeight + x); }, extra);
  const scrollTo = (sel, offset = 70) => p.evaluate(([s, o]) => { const el = document.querySelector(s); const nav = document.querySelector("nav.steps"); window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - nav.offsetHeight - o); }, [sel, offset]);
  const cue = async (text, seconds) => { await caption(text); await snap(seconds); };

  // 1. Title and problem
  await cardShot(`<div class="eyebrow">UGREEN Hackathon 2026 · Skill: almanac</div><h1>Board Almanac</h1>
    <p class="sub">Which rule applies now, since when, and on whose authority?</p>
    <div class="foot">A Skill for the UGREEN AI NAS · replay on synthetic data</div>`, 5.5);
  await cardShot(`<div class="eyebrow">The problem</div>
    <div class="lines"><div>A board's rules are spread across years of bylaws, minutes, notices, contracts and recordings.</div>
    <div>Later decisions replace earlier ones, notices contain errors, and deadlines are missed.</div>
    <div>A search returns every version and leaves the reader to decide which one applies.</div></div>`, 9);

  // 2. Outcome first: one fee, three figures
  await open("folder"); await toPanel(-8);
  await p.evaluate(() => window.demo.selectFile("notice-2025-02-10-fees.pdf"));
  await cue("This board's documents give three different monthly fees: $230 in a notice, $235 on an agenda and $240 in the latest minutes.", 7);
  await p.evaluate(() => { window.demo.go("almanac"); window.demo.setVersion("v1", true); window.demo.topic("fee"); });
  await toPanel(-8);
  await cue("Almanac records which one is in force, who set it and when, quoting the minutes.", 6);
  await scrollTo("#topic .timeline", 20);
  await cue("The $235 proposal was never adopted, and the $230 notice was corrected by the board. $240 has applied since March 1, 2026.", 7.5);
  await p.evaluate(() => { window.demo.go("ask"); window.demo.ask("Q1"); }); await toPanel(-8);
  await cue("Questions are answered from the almanac. A search of the raw folder can return the corrected notice instead.", 7);

  // 3. A change that applies to part of a rule
  await p.evaluate(() => window.demo.go("update")); await toPanel(-8);
  await cue("New minutes change quiet hours on Friday and Saturday nights only. The next compile extracts that file, rechecks the bylaws it amends, and carries the other topics forward.", 7);
  await p.evaluate(() => { window.demo.go("almanac"); window.demo.setVersion("v2", true); window.demo.topic("quiet"); }); await toPanel(-8);
  await cue("Version 2 applies 11:00 p.m. to those two nights and keeps 10:00 p.m. for every other night, with the earlier rule recorded.", 7);

  // 4. A disagreement the documents do not resolve
  await p.evaluate(() => window.demo.topic("pool")); await toPanel(-8);
  await cue("When documents disagree and nothing resolves it, the almanac quotes both and leaves the decision to the board.", 6.5);

  // 5. How it works
  await p.evaluate(() => window.demo.go("folder")); await toPanel(-8);
  await p.evaluate(() => window.demo.selectFile("board-meeting-2026-06-18.m4a"));
  await cue("The test archive holds 16 files from 2019 to 2026, including a meeting recording that ended without a vote.", 6);
  await p.evaluate(() => window.demo.go("compile")); await toPanel(-8);
  await p.evaluate(() => window.demo.run(0, -1));
  await cue("On the NAS, the Skill is designed to delegate every step of a compile to the UGOS agents.", 6);
  const stepCaps = {
    1: "The folder is inventoried with checksums, so later compiles process only new or changed files.",
    3: "Decisions are extracted with a quotation and source file. A recording can only create provisional items.",
    4: "Sources are reconciled against each other, and disagreements are reported for the board to resolve.",
    6: "The user reviews each changed rule and its quotation before anything is saved.",
    8: "The new version is saved beside the old one and read back to confirm it is complete."
  };
  for (const i of [1, 3, 4, 6, 8]) {
    await p.evaluate(i => window.demo.run(i + 1, i), i);
    await scrollTo(`#run > li:nth-child(${i + 1})`, 120);
    await cue(stepCaps[i], 5);
  }

  // 6. More answers and the lint report
  await p.evaluate(() => { window.demo.go("ask"); window.demo.ask("Q5"); }); await toPanel(-8);
  await cue("The heat-pump answer gives the conditions, the vote and the date.", 5);
  await p.evaluate(() => window.demo.ask("Q16"));
  await cue("When the documents do not cover a question, the answer says so.", 5);
  await p.evaluate(() => window.demo.go("lint")); await toPanel(-8);
  await cue("Lint lists what needs attention: an open conflict, a late contract notice, a deadline in 69 days and items that were never voted on.", 7.5);
  await p.evaluate(() => { window.demo.go("almanac"); window.demo.setVersion("v2", true); window.demo.topic("fee"); document.querySelector("details.mdfile").open = true; });
  await scrollTo("details.mdfile", 10);
  await cue("The almanac itself is a plain Markdown file on the NAS, readable without any special software.", 5);

  // 8. Close
  await cardShot(`<div class="eyebrow">UGREEN Hackathon 2026 · Skill: almanac</div><h1>Board Almanac</h1>
    <div class="lines"><div>Every rule is cited to a source document and quotation, and every version is kept on the NAS.</div>
    <div>Conflicts are reported for the board to resolve, and each change is reviewed before it is saved.</div></div>
    <div class="foot">github.com/rc1-dev/board-almanac · Replay on synthetic data; device results will follow NAS testing</div>`, 8);

  fs.writeFileSync(path.join(out, "shots.json"), JSON.stringify(shots, null, 1)); fs.rmSync(path.join(out, "card.html"), { force: true });
  console.log(shots.length, "shots,", shots.reduce((a, s) => a + s.seconds, 0).toFixed(1), "seconds");
  await browser.close();
})();
