# Board Almanac

Board Almanac is a Skill for the UGREEN AI NAS. It compiles the document archive of a condo association, homeowners' association or club board into a versioned, cited rulebook, and answers questions about which rule currently applies, since when, and on whose authority.

It was written for the UGREEN Hackathon 2026 (track: Automate Your Workflow). The Skill is named `almanac`.

## The problem

A board's rules are rarely kept in one place. They are set in bylaws, changed in meeting minutes, announced in notices, constrained by contracts and sometimes discussed in recorded meetings. Over the years, later decisions replace earlier ones, a notice occasionally states the wrong figure, and a proposal that failed can be mistaken for one that passed. Anyone trying to answer a simple question, such as how many pets a unit may keep, has to read the whole history and work out which statement is still in force.

## The approach

Almanac does that work once, when documents arrive, and keeps the result. Each compile produces a Markdown file in an almanac folder on the NAS. For every topic, the file records the currently documented rule, its effective date, the vote or document that established it, a quotation from the source, the rules it replaced and the period each applied, and any conflict the documents leave unresolved. Older versions are never modified, so the folder also serves as an audit trail.

The rules for deciding which statement is current are written out explicitly in [the supersession rules](skill/almanac/references/supersession-rules.md). A later adopted decision replaces an earlier one only for the same subject and scope, so an amendment that changes quiet hours on Friday and Saturday nights leaves the other nights untouched. Failed motions and agenda proposals never change a rule. A notice that contradicts the minutes is recorded as a conflict unless a later document corrects it. When nothing resolves a disagreement, the almanac quotes both statements and leaves the decision to the board.

Questions are answered from the newest almanac rather than from the raw archive. Each answer gives the rule, its source and the almanac version it came from, and says so plainly when the almanac does not cover the question.

## How a compile runs

The Skill delegates every step to the UGOS agents (`file-agent`, `document-agent` and `knowledge-agent`) and never calls a command-line tool directly.

1. The previous almanac is read in full. If any section is missing, the run stops without saving.
2. The board folder is inventoried with checksums and compared with the ledger of processed files. Claims are extracted from new, changed, unfinished or previously failed files, up to 60 documents per run, and from unchanged files that support a record affected by a change. The documents a new decision amends are read again during reconciliation, and all other topics are carried forward.
3. Meeting recordings are transcribed. Anything decided only in a recording is marked provisional.
4. Decisions, rules, votes, effective dates, action items and contract terms are extracted, each with a quotation and its source file.
5. The new material is reconciled with the original documents behind the affected topics. The previous almanac is treated as state to update, never as evidence.
6. The supersession rules are applied and the new version is written, carrying unchanged topics forward exactly.
7. The user reviews each new or changed rule beside the rule it replaces, with its effective date and quotation, before anything is saved.
8. The file name is checked, the version is saved after approval, and the saved file is read back to confirm it is complete.

The Skill asks which model the NAS uses for document processing. The intended setting is the NAS local model, and a third-party model is used only with the user's explicit authorization. Model routing itself is a UGOS setting that the Skill can confirm but not change. People are recorded by board role, and residents' private matters are left out.

The almanac reports what the documents record. It does not give legal advice or judge whether a vote or notice was valid.

## Demo

An interactive demo is available at [rc1-dev.github.io/board-almanac](https://rc1-dev.github.io/board-almanac/) (source in [`docs/index.html`](docs/index.html)). It walks through the board folder, the compile run, the resulting almanac with the history of each rule, answers to sample questions, an incremental update and the lint report. A captioned video of the same walkthrough is in [`demo/video/almanac-demo.mp4`](demo/video/almanac-demo.mp4).

Both replay the expected behavior on the synthetic test archive. The delegation text is quoted from `SKILL.md`, and the answers are the reference answers from the validation kit. Results from a real NAS will follow the hackathon's device testing.

## Status

The Skill (`SKILL.md` and six reference files) is complete and passes the official kit checker for capability catalog 2.0.0 with no errors or warnings ([result](docs/checker-result.json)). The validation kit contains a synthetic archive for a fictional 48-unit building, a 20-question answer key and a scorer. Runtime behavior on a UGREEN AI NAS has not yet been tested.

## Repository layout

| Path | Contents |
|---|---|
| `skill/almanac/` | The Skill package: `SKILL.md` and six reference files |
| `validation/` | Synthetic archive and its generator, answer key, scorer, expected almanac versions and recording script ([details](validation/README.md)) |
| `demo/` | Demo page source and build script, and the video with its filming scripts |
| `docs/` | Built demo page for GitHub Pages, and the checker result |
| `proposal/` | Round 1 proposal source and PDF |
| `scripts/package.sh` | Builds `dist/almanac.zip` and runs the official checker |

## Running the validation kit

```bash
pip install reportlab python-docx        # only needed to regenerate the archive
python3 validation/build_corpus.py       # writes validation/corpus/
python3 validation/score.py validation/selftest/gold_answers.jsonl --recording
```

The reference answers in `validation/selftest/` are written by hand. They confirm that the answer key and scorer agree, and serve as the standard that output from the NAS will be measured against.

## Building

```bash
python3 demo/build_demo.py                                  # rebuilds docs/index.html
UGREEN_KIT=/path/to/uliya-skill-kit scripts/package.sh      # builds and checks the Skill package
```

The UGREEN skill kit is not included in this repository and can be downloaded from the hackathon resources.

## Disclosure

The workflow was designed and written during the UGREEN Hackathon 2026. Claude (Anthropic) assisted with drafting and reviewing the Skill files, test materials, proposal and documentation. The Skill bundles no third-party code, models or services. The validation generator uses reportlab (BSD license) and python-docx (MIT license). All test data is synthetic and fictional, and people appear by board role only.
