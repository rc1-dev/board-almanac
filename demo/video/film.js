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
    <p class="sub">What is the rule now, since when, and says who?</p>
    <div class="foot">A Skill for the UGREEN AI NAS · replay on synthetic data</div>`, 5.5);
  await cardShot(`<div class="eyebrow">The problem</div>
    <div class="lines"><div>A condo board's rules live in years of bylaws, minutes, notices, contracts and recordings.</div>
    <div>Later votes quietly replace earlier ones. Notices contain errors. Deadlines slip.</div>
    <div>Search returns every version and leaves people guessing which one is current.</div></div>`, 9);

  // 2. Folder
  await open("folder"); await toPanel(-8);
  await cue("The board folder: 16 files from 2019 to 2026. Bylaws, minutes, notices, a contract, an email and a meeting recording.", 6);
  await p.evaluate(() => window.demo.selectFile("notice-2025-02-10-fees.pdf"));
  await cue("Some files are traps. This notice says the fee is EUR 230. The board adopted EUR 225.", 6);
  await p.evaluate(() => window.demo.selectFile("notice-2026-05-01-pool.pdf"));
  await cue("This notice says the pool closes at 21:00. The board minutes say 22:00.", 5.5);
  await p.evaluate(() => window.demo.selectFile("board-meeting-2026-06-18.m4a"));
  await cue("A recorded discussion with no vote. It must not change a rule.", 5);

  // 3. Compile
  await p.evaluate(() => window.demo.go("compile")); await toPanel(-8);
  await p.evaluate(() => window.demo.run(0, -1));
  await cue("Compile, version 1. The Skill only delegates to UGOS experts: file-agent, document-agent and knowledge-agent.", 6);
  const stepCaps = [
    "Step 1: look for the previous almanac. There is none, so this is a first compile.",
    "Step 2: inventory the folder with SHA-256 checksums. This ledger makes later updates incremental.",
    "Step 3: transcribe the recording on the NAS. What it says stays provisional.",
    "Step 4: extract claims. Every claim needs a verbatim quote and its source file.",
    "Step 5: reconcile. Disagreements are reported, never settled by guessing.",
    "Step 6: apply the supersession rules, topic by topic.",
    "Step 7: show each changed rule with its quote, and ask before saving anything.",
    "Step 8: create the Almanac folder, with approval.",
    "Step 9: save almanac v1 as a new file. Success only when the save is verified."
  ];
  for (let i = 0; i < 9; i++) {
    await p.evaluate(i => window.demo.run(i + 1, i), i);
    await scrollTo(`#run > li:nth-child(${i + 1})`, 120);
    await cue(stepCaps[i], i === 3 || i === 4 ? 5 : 4);
    if (i === 3) {
      await p.evaluate(() => { document.querySelector("#run > li:nth-child(4) details").open = true; });
      await scrollTo("#run > li:nth-child(4) details", 60);
      await cue("Each delegation shown here is quoted from SKILL.md. No CLI calls, no invented results.", 5.5);
    }
  }

  // 4. Almanac
  await p.evaluate(() => { window.demo.go("almanac"); window.demo.setVersion("v1", true); window.demo.topic("fee"); });
  await toPanel(-8);
  await cue("The almanac keeps one current rule per topic, with its source, its quote and every rule it replaced.", 6);
  await scrollTo("#topic .timeline", 20);
  await cue("EUR 235 was only proposed. EUR 230 was an error, corrected later. EUR 240 has been the rule since March 2026.", 7.5);
  await p.evaluate(() => window.demo.topic("pool")); await toPanel(-8);
  await cue("When documents disagree and nothing resolves it, the almanac says so and quotes both.", 6);
  await p.evaluate(() => { document.querySelector("details.mdfile").open = true; });
  await scrollTo("details.mdfile", 10);
  await cue("It is a plain Markdown file saved on the NAS. Readable without any AI.", 5);

  // 5. Ask
  await p.evaluate(() => { window.demo.go("ask"); window.demo.ask("Q1"); }); await toPanel(-8);
  await cue("Ask: answers come only from the almanac, with the source file and the almanac version.", 6);
  await cue("A raw search can surface the wrong notice. Both answers are scored with the same answer key.", 6);
  await p.evaluate(() => window.demo.ask("Q5"));
  await cue("Conditions, vote and date, straight from the compiled rule.", 5);
  await p.evaluate(() => window.demo.ask("Q16"));
  await cue("Not in the documents? It says so, instead of inventing an answer.", 5);

  // 6. Update
  await p.evaluate(() => window.demo.go("update")); await toPanel(-8);
  await cue("New minutes arrive. The next compile reads only the new file and skips the 16 unchanged ones.", 6);
  await cue("Only Friday and Saturday quiet hours changed. Version 2 is saved next to version 1; nothing is overwritten.", 6.5);
  await p.evaluate(() => { window.demo.go("almanac"); window.demo.setVersion("v2", true); window.demo.topic("quiet"); }); await toPanel(-8);
  await cue("The history shows exactly what was replaced, and what still applies on other nights.", 5.5);

  // 7. Lint
  await p.evaluate(() => window.demo.go("lint")); await toPanel(-8);
  await cue("Lint finds what needs attention: an open conflict, a late contract notice, a deadline in 69 days and items never voted on.", 7.5);

  // 8. Close
  await cardShot(`<div class="eyebrow">Board Almanac</div><h1>Compile once.<br>Answer many times.</h1>
    <div class="lines"><div>Every rule cited to a file and a quote. Every version kept on the NAS.</div>
    <div>Conflicts reported, never guessed. Every changed rule reviewed before it is saved.</div></div>
    <div class="foot">github.com/rc1-dev/board-almanac · Replay on synthetic data · On-device results after the NAS test day</div>`, 8);

  fs.writeFileSync(path.join(out, "shots.json"), JSON.stringify(shots, null, 1)); fs.rmSync(path.join(out, "card.html"), { force: true });
  console.log(shots.length, "shots,", shots.reduce((a, s) => a + s.seconds, 0).toFixed(1), "seconds");
  await browser.close();
})();
