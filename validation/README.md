# Almanac validation kit

Synthetic test material for the `almanac` Skill. Everything is fictional; people appear by board role only. This folder is not part of the Skill package.

| File | Purpose |
|---|---|
| `build_corpus.py` | Generates the board folder (`corpus/Board Documents`, 15 files: PDF, DOCX, TXT) and the edge-case file (`corpus/add-later/minutes-2026-09-15.docx`). Needs `reportlab` and `python-docx`. |
| `recording-script-2026-06.md` | Script to read aloud and record on the NAS on test day (provisional-decision test). |
| `answer_key.json` | 20 questions with required facts, forbidden facts and required citations. Phases: `initial` (18) and `after_update` (2). |
| `score.py` | Scorer, standard library only. `python3 score.py answers.jsonl [--phase initial] [--recording]` |
| `expected-almanac-v1.md` | Hand-written reference of a correct first compile, for reviewing real output. |
| `selftest/gold_answers.jsonl` | Hand-written correct answers. Scores 20/20; proves the key and scorer agree. |
| `selftest/raw_search_example.jsonl` | Hand-written examples of typical raw-search mistakes (stale fee, superseded pet rule, one side of a conflict, invented gym hours). Illustrative only; not a measured baseline. |

## Test-day procedure

1. Copy `corpus/Board Documents` to the NAS. Record the script and add the audio file.
2. Compile. Review the result against `expected-almanac-v1.md`.
3. Ask the 18 `initial` questions; save answers as JSONL; score with `--phase initial --recording`.
4. Ask the same questions with plain file chat over the raw folder; score the same way.
5. Copy `corpus/add-later/minutes-2026-09-15.docx` into the board folder, compile again, check that only that file was processed and a new version was saved, then ask Q9 and Q10 (`--phase after_update`).
6. Record run times, approval prompts and failed files.

Results are reported as measured on the device. No results are claimed before that run.
