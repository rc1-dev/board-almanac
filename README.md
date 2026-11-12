# Board Almanac

Board Almanac is a Skill for the UGREEN AI NAS. It compiles the document archive of a condo association, homeowners' association or club board into a versioned, cited rulebook, and answers questions about which rule currently applies, since when, and on whose authority.

It was written for the UGREEN Hackathon 2026 (track: Automate Your Workflow). The Skill is named `almanac`.

## The problem

A board's rules are rarely kept in one place. They are set in bylaws, changed in meeting minutes, announced in notices, constrained by contracts and sometimes discussed in recorded meetings. Over the years, later decisions replace earlier ones, a notice occasionally states the wrong figure, and a proposal that failed can be mistaken for one that passed. In the validation archive, an agenda proposes a monthly fee of $235, a notice wrongly states $230 and a later vote sets $240. A search for the fee finds all three. Anyone trying to answer a simple question, such as the current fee or how many pets a unit may keep, has to read the whole history and work out which statement still governs.

## The approach

Search finds what documents say; Almanac reconstructs which decisions still apply. It does that work in a compile and keeps the result. Each compile produces a Markdown file in an almanac folder on the NAS. For every topic, the file records the currently documented rule, its scope, its effective date, the vote or document that established it, a quotation from the source, the rules it replaced and the period each applied, any change scheduled for a later date, and any conflict the documents leave unresolved. Each version also has a changelog of what changed since the previous one, and the user reviews it before the version is saved. The changelog compares each topic's summary (rule, scope, effective date and status) and the open items; a change only to a topic's authority or evidence, such as a corrected vote count, appears in the topic but is not flagged as a change. Older versions are never modified, so the folder also serves as an audit trail.

The rules for deciding which statement is current are set out in [the supersession rules](skill/almanac/references/supersession-rules.md). A later adopted decision replaces an earlier one only for the same subject and scope, so an amendment that changes quiet hours on Friday and Saturday nights leaves the other nights untouched. Failed motions and agenda proposals never change a rule. A notice that contradicts the minutes is recorded as a conflict unless a later document corrects it. When nothing resolves a disagreement, the almanac quotes both statements and leaves the decision to the board.

Adopted changes that take effect later are recorded as scheduled, and a question about a date after the change gets the new rule. Almanac has no background scheduler. When the user next runs a compile after that date, it proceeds even if no file has changed, and the saved version makes the new rule current.

Questions are answered from the newest almanac rather than from the raw archive. Each answer gives the rule, its source and the almanac version it came from, and says so plainly when the almanac does not cover the question.

## How a compile runs

The Skill delegates every step to the UGOS agents (`file-agent`, `document-agent` and `knowledge-agent`) and never calls a command-line tool directly.

1. The board folder is listed with checksums. The newest almanac supplies only its version number and, for the changelog, its summary table and open items. If nothing has changed and no scheduled change has taken effect, the almanac is reported as current.
2. Meeting recordings are transcribed. Anything decided only in a recording is marked provisional.
3. Every document is read again, up to 60 files per compile. Decisions, rules, votes, effective dates, action items and contract terms are extracted, each with a quotation and its source file. A file that cannot be read stops the compile until the user fixes it or explicitly excludes it, and an almanac built without it is marked as compiled with exclusions.
4. The documents are reconciled against each other, and every disagreement is reported rather than decided.
5. The supersession rules are applied and the whole almanac is written again from these records. Because nothing is carried over from the previous version, a corrected or deleted document cannot leave an outdated rule behind.
6. Before approval, the Skill checks that the summary table, each topic and the review agree. The user then reviews each new or changed rule beside its previous summary value, with the new rule's effective date and quotation, and every change to an open item.
7. The folder is checked again, and if any file changed during the compile, nothing is saved. Otherwise the version is saved after approval under a new name and read back to confirm that it is complete.

The Skill asks which model the NAS uses for document processing. The intended setting is the NAS local model, and a third-party model is used only with the user's explicit authorization. Model routing itself is a UGOS setting that the Skill can confirm but not change. People are recorded by board role, and residents' private matters are left out.

The almanac reports what the documents record. It does not give legal advice or judge whether a vote or notice was valid.

## Existing tools

Hosted HOA platforms such as HOALife and HOA Hub answer questions from an association's uploaded governing documents. [HOALife](https://www.hoalife.com/features/ai-features) offers an AI chat that draws on an HOA's governing documents. HOA Hub answers residents' questions with [EasyAsk](https://www.hoahub.app/features/easyask/), and its [document hub](https://www.hoahub.app/features/documents/) compares an uploaded amendment with the governing document and keeps a version history.

Almanac instead reconciles decisions across the board's whole archive on the NAS, including minutes, notices, recordings and corrections. It records which motions passed or failed, when each change takes effect and where documents disagree, and the user reviews each version before it is saved. With the UGOS local model, the documents need not go to a hosted AI service.

## Demo

An interactive demo is available at [rc1-dev.github.io/board-almanac](https://rc1-dev.github.io/board-almanac/) (source in [`docs/index.html`](docs/index.html)). It walks through the board folder, the compile run, the resulting almanac with the history of each rule, answers to sample questions, an update and the lint report. A captioned video of the same walkthrough is in [`demo/video/almanac-demo.mp4`](demo/video/almanac-demo.mp4).

Both replay the expected behavior on the synthetic test archive. The delegation text is quoted from `SKILL.md`, and the answers are the reference answers from the validation kit. Results from a real NAS will follow the hackathon's device testing.

## Status

The Skill (`SKILL.md` and six reference files) is complete. It follows the Uliya Skill Development Standard and passes the skill kit's static check for capability catalog 2.0.0 with no errors or warnings ([result](docs/checker-result.json)). The validation kit contains a synthetic archive for a fictional 48-unit building, six adversarial cases, a 23-question answer key and a scorer. Runtime behavior on a UGREEN AI NAS has not yet been tested.

Before device testing, the Skill was exercised in 64 simulated runs, with a small model playing the Skill against stand-in agents ([method and results](testing/README.md)). No run saved without approval or followed an instruction hidden in a document, and the results led to the current design: a full rebuild on every compile, a compile when a scheduled change takes effect, and a check of the folder before saving.

One weakness remains. A change to part of a rule, or to one period, is sometimes treated as ending the parts that did not change. For example, a pool-hours decision for the 2026 season can hide the standing rule for later seasons. The review before saving shows each changed rule beside the one it replaces, so the user can catch this. The planned fix is to have the document agent report which parts of an earlier rule stay in force.

Answer quality on the device will depend on how well the NAS reads documents, recognizes scanned text and transcribes recordings. One compile handles up to 60 files.

## Repository layout

| Path | Contents |
|---|---|
| `skill/almanac/` | The Skill package: `SKILL.md` and six reference files |
| `validation/` | Synthetic archive and its generator, answer key, scorer, expected almanac versions and recording script ([details](validation/README.md)) |
| `demo/` | Demo page source and build script, and the video with its filming scripts |
| `docs/` | Built demo page for GitHub Pages, and the checker result |
| `testing/` | Simulated-test harness, the unseen club archive, and the runs, checks and grades of the final round ([details](testing/README.md)) |
| `proposal/` | Round 1 proposal source and PDF |
| `scripts/package.sh` | Builds `dist/almanac.zip` and runs the skill kit's static check on it |

## Running the validation kit

```bash
pip install reportlab python-docx        # only needed to regenerate the archive
python3 validation/build_corpus.py       # writes validation/corpus/
python3 validation/score.py validation/selftest/gold_answers.jsonl --recording
```

The reference answers in `validation/selftest/` are written by hand. They confirm that the answer key and scorer agree, and serve as the standard that output from the NAS will be measured against. The kit also contains six adversarial cases with their expected outcomes, including corrected minutes and a change adopted for a later effective date. The generated archive is byte-for-byte reproducible and its checksums are recorded.

## Building

```bash
python3 demo/build_demo.py                                  # rebuilds docs/index.html
UGREEN_KIT=/path/to/uliya-skill-kit scripts/package.sh      # builds and checks the Skill package
```

The UGREEN skill kit is not included in this repository and can be downloaded from the hackathon resources.

## Disclosure

The workflow was designed and written during the UGREEN Hackathon 2026. Claude (Anthropic) assisted with drafting and reviewing the Skill files, test materials, proposal and documentation, and Claude models played the Skill and graded the runs in the simulated tests. The Skill bundles no third-party code, models or services. The validation generator uses reportlab (BSD license) and python-docx (MIT license). All test data is synthetic and fictional, and people appear by board role only.
