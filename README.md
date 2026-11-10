# Board Almanac

**A living, cited rulebook for board documents on the UGREEN AI NAS.**
UGREEN Hackathon 2026 entry · Track: Automate Your Workflow · Skill name: `almanac`

Condo associations, HOAs and clubs keep their rules in years of bylaws, meeting minutes, notices, contracts and recordings. Later votes quietly replace earlier ones, notices contain mistakes, and deadlines slip. Searching the folder returns every version of a rule and leaves people to guess which one is current.

Almanac compiles that folder into a versioned Markdown rulebook on the NAS and answers one question well: **what is the rule now, since when, and says who?**

## Demo

- **Interactive demo:** [rc1-dev.github.io/board-almanac](https://rc1-dev.github.io/board-almanac/) (source: [`docs/index.html`](docs/index.html)). Walk through the board folder, the compile run, the almanac with each rule's history, cited answers next to raw-search mistakes, an incremental update and lint.
- **Video (2:47, captioned):** [`demo/video/almanac-demo.mp4`](demo/video/almanac-demo.mp4)

Both are a **replay** on the synthetic test folder: the delegation text is quoted from `SKILL.md` and the answers are the test kit's reference answers. The Skill itself runs on a UGREEN AI NAS, and on-device results come after the NAS test day.

## How it works

```text
Board Documents/            almanac (compile)               Almanac/
  bylaws-2019.pdf     ─┐    1 read previous almanac          almanac-2026-11-22-v1.md
  minutes-*.pdf/docx   ├──▶ 2 inventory + SHA-256       ──▶  almanac-2026-11-29-v2.md
  notices, contract    │    3 transcribe recordings          (one new file per run;
  email, recordings   ─┘    4 extract cited claims             older versions kept)
                            5 reconcile against almanac
                            6 apply supersession rules
                            7 show changelog → approve → save
```

- **Compile once, answer many times.** Each compile reads only files that are new or changed since the last version (tracked in a Sources ledger of checksums), applies explicit [supersession and conflict rules](skill/almanac/references/supersession-rules.md), and saves a new version.
- **Every fact is cited.** Each topic records the current rule, effective date, the vote or document that set it, a verbatim quote, the rules it replaced, open conflicts and provisional items.
- **Conflicts are reported, not guessed.** If minutes say the pool closes at 22:00 and a later notice says 21:00, the almanac says the documents disagree and quotes both.
- **Four modes:** Compile, Ask (answers only from the newest almanac), Lint (conflicts, provisional decisions, late or overdue actions, coming deadlines) and Status.
- **Safe by design:** the parent Skill only delegates to UGOS experts (`file-agent`, `document-agent`, `knowledge-agent`); it never overwrites, moves or deletes files; each save needs approval; the NAS local model is the default; people are recorded by board role.

See [SKILL.md](skill/almanac/SKILL.md) for the full workflow and [the almanac format](skill/almanac/references/almanac-format.md) for what a compiled file looks like.

## Why not just file chat or RAG?

Retrieval finds passages that match a question. It cannot tell a 2019 rule from the 2025 vote that replaced it, a proposal from an adopted motion, or a notice with a typo from the corrected minutes. Almanac resolves those relationships once, when files arrive, and keeps the result, so answers come from one small reconciled file. That also suits a small on-device model.

## Status

| Item | State |
|---|---|
| Skill (`skill/almanac`) | Implemented. Official kit checker (catalog 2.0.0): `static-pass`, 0 errors, 0 warnings ([result](docs/checker-result.json)) |
| Validation kit (`validation/`) | Synthetic board folder, 20-question answer key, scorer; self-test 20/20 on hand-written reference answers |
| Runtime on a UGREEN AI NAS | **Pending.** Scheduled for the finalist NAS test day. No on-device results are claimed yet. |

## Repository layout

| Path | Contents |
|---|---|
| `skill/almanac/` | The Skill package: `SKILL.md` and six reference files |
| `validation/` | Synthetic corpus and generator, answer key, scorer, expected first almanac, recording script ([readme](validation/README.md)) |
| `proposal/` | Round 1 proposal source and rendered PDF |
| `demo/` | Demo page source (`template.html`, `build_demo.py`) and the video with its filming scripts |
| `docs/` | Built demo page (`index.html`, served by GitHub Pages) and checker output |
| `scripts/package.sh` | Builds `dist/almanac.zip` and runs the official checker |

## Try the validation kit

```bash
pip install reportlab python-docx        # only needed to regenerate the corpus
python3 validation/build_corpus.py       # writes validation/corpus/
python3 validation/score.py validation/selftest/gold_answers.jsonl --recording
python3 validation/score.py validation/selftest/raw_search_example.jsonl
```

## Rebuild the demo

```bash
python3 demo/build_demo.py               # writes docs/index.html from the repo's own files
```

## Build the Skill package

```bash
UGREEN_KIT=/path/to/uliya-skill-kit scripts/package.sh
```

The UGREEN skill kit is not included; download it from the hackathon resources.

## Disclosure

- The workflow was designed and written during the UGREEN Hackathon 2026.
- AI assistance: Claude (Anthropic) helped draft and review the Skill files, test materials, proposal and this README.
- The Skill bundles no third-party code, models or services. The validation generator uses reportlab (BSD) and python-docx (MIT).
- All test data is synthetic and fictional; people appear by board role only.
- Not legal advice. The Skill reports what documents say; it does not judge whether votes or notices were valid.
