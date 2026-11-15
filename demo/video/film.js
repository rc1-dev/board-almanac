// Film the Almanac demo page as a sequence of held shots.
// Usage: node film.js <docs/index.html> <out-dir> [fonts-dir]
// Writes <out-dir>/NN.jpg and <out-dir>/shots.json ({file, seconds}).
// fonts-dir (optional): a node_modules/@fontsource folder, used when Google Fonts is unreachable.
//
// Each page shot is framed as the page above a caption band, so captions never cover the page.
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const [page_, out, fontsDir] = process.argv.slice(2);
const URL_ = "file://" + path.resolve(page_);
const GRAPHIC = path.resolve(path.dirname(page_), "search-vs-almanac.svg");
fs.mkdirSync(out, { recursive: true });

const FONT_CSS = fontsDir ? [
  "ibm-plex-sans/400.css", "ibm-plex-sans/500.css", "ibm-plex-sans/600.css", "ibm-plex-sans/400-italic.css",
  "ibm-plex-sans-condensed/500.css", "ibm-plex-sans-condensed/600.css", "ibm-plex-sans-condensed/700.css",
  "ibm-plex-mono/400.css", "ibm-plex-mono/500.css",
  "source-serif-4/400.css", "source-serif-4/600.css", "source-serif-4/400-italic.css"
].map(f => "file://" + path.resolve(fontsDir, f)) : [];
const fontLinks = FONT_CSS.map(h => `<link rel="stylesheet" href="${h}">`).join("");

// Frame: 1280 x 720 CSS px at 1.5x = 1920 x 1080. The page fills the top PAGE_H px; the caption band the rest.
const FRAME_W = 1280, FRAME_H = 720, PAGE_H = 612;
// The page is filmed at a narrower width so its text is larger in the frame.
const VIEW_W = 1120, VIEW_H = Math.round(PAGE_H * VIEW_W / FRAME_W);

const BASE_CSS = `
  :root { --paper:#0e1418; --ink:#e1e9ed; --muted:#97a8b3; --accent:#62b8cd; }
  html,body { margin:0; height:100%; background:var(--paper); color:var(--ink); font-family:"IBM Plex Sans",system-ui,sans-serif; }
`;
const CARD_CSS = BASE_CSS + `
  body { display:grid; place-items:center; }
  .card { width: 1040px; }
  .eyebrow { font: 500 15px "IBM Plex Mono", monospace; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }
  h1 { font: 700 96px/1 "IBM Plex Sans Condensed", sans-serif; margin: 14px 0 0; }
  .sub { font: 400 34px/1.3 "Source Serif 4", Georgia, serif; margin: 18px 0 0; }
  .for { font-size: 24px; color: var(--muted); margin: 14px 0 0; }
  .lines { margin-top: 30px; display:grid; gap: 16px; font-size: 27px; line-height:1.35; }
  .lines div { border-left: 4px solid var(--accent); padding-left: 18px; }
  .foot { margin-top: 40px; font: 400 17px "IBM Plex Mono", monospace; color: var(--muted); }
  .graphic { width: 1120px; } .graphic img { width: 100%; display:block; border-radius: 14px; }
  .graphic .eyebrow { margin-bottom: 14px; }
  .gwrap { position: relative; }
  .cover { position:absolute; left:49%; top:0.4%; right:0.3%; bottom:7%; background:#fff; border-top-right-radius: 13px; }
`;
const FRAME_CSS = BASE_CSS + `
  .shot { position:absolute; left:0; top:0; width:${FRAME_W}px; height:${PAGE_H}px; display:block; }
  .band { position:absolute; left:0; top:${PAGE_H}px; width:${FRAME_W}px; height:${FRAME_H - PAGE_H}px;
          display:flex; align-items:center; justify-content:center; box-sizing:border-box; padding:0 70px;
          border-top: 3px solid var(--accent); }
  .band p { margin:0; font: 500 23px/1.4 "IBM Plex Sans", system-ui, sans-serif; color:#f2f6f8; text-align:center; text-wrap: balance; }
`;
const html = (css, body) => `<!doctype html><html><head><meta charset="utf-8">${fontLinks}<style>${css}</style></head><body>${body}</body></html>`;
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");

let n = 0;
const shots = [];

(async () => {
  const browser = await chromium.launch();
  const p = await (await browser.newContext({ viewport: { width: VIEW_W, height: VIEW_H }, deviceScaleFactor: 1920 / VIEW_W, colorScheme: "light" })).newPage();
  const f = await (await browser.newContext({ viewport: { width: FRAME_W, height: FRAME_H }, deviceScaleFactor: 1.5 })).newPage();
  p.on("pageerror", e => console.error("pageerror", e.message));
  f.on("pageerror", e => console.error("pageerror", e.message));
  const tmp = path.join(out, "tmp"); fs.mkdirSync(tmp, { recursive: true });

  async function frame(doc, seconds) {
    const file = String(++n).padStart(2, "0") + ".jpg";
    const hf = path.join(tmp, "frame.html"); fs.writeFileSync(hf, doc);
    await f.goto("file://" + hf, { waitUntil: "load" });
    await f.evaluate(() => document.fonts.ready);
    await f.waitForTimeout(150);
    await f.screenshot({ path: path.join(out, file), type: "jpeg", quality: 92 });
    shots.push({ file, seconds });
  }
  const cardShot = (inner, seconds) => frame(html(CARD_CSS, `<div class="card">${inner}</div>`), seconds);
  async function cue(text, seconds) {
    await p.waitForTimeout(250);
    const png = path.join(tmp, `page${n + 1}.png`);
    await p.screenshot({ path: png });
    await frame(html(FRAME_CSS, `<img class="shot" src="file://${png}"><div class="band"><p>${esc(text)}</p></div>`), seconds);
  }
  async function open(hash) {
    await p.goto(URL_ + "#" + hash, { waitUntil: "load" });
    await p.evaluate((css) => {
      css.forEach(h => { const l = document.createElement("link"); l.rel = "stylesheet"; l.href = h; document.head.appendChild(l); });
    }, FONT_CSS);
    await p.evaluate(() => document.fonts.ready);
  }
  const toPanel = (extra = 0) => p.evaluate(x => { const h = document.querySelector("header.top"); window.scrollTo(0, h.offsetTop + h.offsetHeight + x); }, extra);
  const scrollTo = (sel, offset = 70) => p.evaluate(([s, o]) => { const el = document.querySelector(s); const nav = document.querySelector("nav.steps"); window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - nav.offsetHeight - o); }, [sel, offset]);

  // 1. Title and problem
  await cardShot(`<div class="eyebrow">UGREEN Hackathon 2026 · Skill: almanac</div><h1>Almanac</h1>
    <p class="sub">Which rule applies now, since when, and on whose authority?</p>
    <p class="for">A versioned, cited rulebook for HOA, condo and club associations</p>
    <div class="foot">A Skill for the UGREEN AI NAS · replay on synthetic data</div>`, 5.5);
  await cardShot(`<div class="eyebrow">The problem</div>
    <div class="lines"><div>An association's rules are spread across years of bylaws, minutes, notices, contracts and recordings.</div>
    <div>Later decisions replace earlier ones, notices contain errors, and proposals fail.</div>
    <div>A search returns every version and leaves the reader to decide which one applies.</div></div>`, 8);
  // The search first, then the almanac beside it.
  const graphic = (cover) => `<div class="graphic"><div class="eyebrow">The monthly fee in the test archive</div>
    <div class="gwrap"><img src="file://${GRAPHIC}">${cover ? '<div class="cover"></div>' : ""}</div></div>`;
  await cardShot(graphic(true), 6);
  await cardShot(graphic(false), 9);

  // 2. The fee, in the demo
  await open("almanac"); await p.evaluate(() => { window.demo.go("almanac"); window.demo.setVersion("v1", true); window.demo.topic("fee"); });
  await toPanel(-8);
  await cue("Almanac records the fee in force, the vote that set it and its effective date, quoting the minutes.", 6);
  await scrollTo("#topic .timeline", 20);
  await cue("The $235 proposal was never adopted, and the $230 notice was corrected by the board. $240 has applied since March 1, 2026.", 7.5);
  await p.evaluate(() => { window.demo.go("ask"); window.demo.ask("Q1"); }); await toPanel(-8);
  await cue("Questions are answered from the almanac. A search of the raw folder can return the corrected notice instead.", 7);

  // 3. A change that applies to part of a rule
  await p.evaluate(() => window.demo.go("update")); await toPanel(-8);
  await cue("New minutes change quiet hours on Friday and Saturday nights only. The next compile reads every document again and builds version 2 from them.", 7);
  await p.evaluate(() => { window.demo.go("almanac"); window.demo.setVersion("v2", true); window.demo.topic("quiet"); }); await toPanel(-8);
  await cue("Version 2 applies 11:00 p.m. to those two nights and keeps 10:00 p.m. for every other night, with the earlier rule recorded.", 7);

  // 4. A disagreement the documents do not resolve
  await p.evaluate(() => window.demo.topic("pool")); await toPanel(-8);
  await cue("When documents disagree and no later document settles it, the almanac quotes both and leaves the decision to the board. The 2019 hours still apply to other seasons.", 8);

  // 5. How it works
  await p.evaluate(() => window.demo.go("folder")); await toPanel(-8);
  await p.evaluate(() => window.demo.selectFile("board-meeting-2026-06-18.m4a"));
  await cue("The test archive holds 16 files from 2019 to 2026, including a meeting recording that ended without a vote.", 6);
  await p.evaluate(() => window.demo.go("compile")); await toPanel(-8);
  await p.evaluate(() => window.demo.run(0, -1));
  await cue("On the NAS, the Skill is designed to delegate every step of a compile to the UGOS agents.", 5);
  const stepCaps = {
    0: "The folder is listed with checksums. Every compile reads every document again, so a corrected or deleted file cannot leave an outdated rule behind.",
    2: "Decisions are extracted with a quotation and source file. A recording can only create provisional items.",
    3: "Sources are reconciled against each other, and disagreements are reported for the board to resolve.",
    5: "Before anything is saved, the user reviews each new or changed rule with its quotation.",
    6: "The folder is checked again before saving. If a file changed during the compile, nothing is saved.",
    7: "The new version is saved beside the old one and read back to confirm it is complete."
  };
  for (const i of [0, 2, 3, 5, 6, 7]) {
    await p.evaluate(i => window.demo.run(i + 1, i), i);
    await scrollTo(`#run > li:nth-child(${i + 1})`, 40);
    await cue(stepCaps[i], i === 0 ? 6.5 : 5);
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

  // 7. Close
  await cardShot(`<div class="eyebrow">UGREEN Hackathon 2026 · Skill: almanac</div><h1>Almanac</h1>
    <div class="lines"><div>Every rule is cited to a source document and quotation, and every version is kept on the NAS.</div>
    <div>Conflicts are reported for the board to resolve, and each change is reviewed before it is saved.</div></div>
    <div class="foot">github.com/rc1-dev/board-almanac · Replay on synthetic data; device results will follow NAS testing</div>`, 8);

  fs.writeFileSync(path.join(out, "shots.json"), JSON.stringify(shots, null, 1));
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log(shots.length, "shots,", shots.reduce((a, s) => a + s.seconds, 0).toFixed(1), "seconds");
  await browser.close();
})();
