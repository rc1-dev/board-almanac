# Almanac validation kit

This folder holds the test material for the `almanac` Skill. It is not part of the Skill package. The archive describes a fictional 48-unit building, Harbor View Condominium Association, between 2019 and 2026. All content is synthetic, and people appear by board role only.

The archive is designed to exercise the cases that make board rules hard to follow: a fee set three times, a notice that states the wrong fee and is later corrected, a proposal that was amended before adoption, a failed motion, an amendment that applies only to some nights, a notice that contradicts the minutes, a contract notice sent after its deadline, and a recorded discussion that ended without a vote.

| File | Purpose |
|---|---|
| `build_corpus.py` | Generates the board folder (`corpus/Board Documents`, 15 PDF, Word and text files) and the file added later for the update test (`corpus/add-later/minutes-2026-09-15.docx`). Requires `reportlab` and `python-docx`. |
| `recording-script-2026-06.md` | A short board discussion to be read aloud and recorded on the NAS during device testing. |
| `answer_key.json` | Twenty questions, each with the facts an answer must contain, statements it must not make, and the sources it must cite. Eighteen are asked after the first compile and two after the update. |
| `score.py` | Scores a file of answers against the key, using only the Python standard library: `python3 score.py answers.jsonl [--phase initial] [--recording]`. |
| `expected-almanac-v1.md` | A hand-written reference for a correct first compile of the 15 files and the recording. |
| `expected-almanac-v2.md` | The same reference after the update. |
| `selftest/gold_answers.jsonl` | Hand-written reference answers. They score 20 of 20, which confirms that the key and the scorer agree. |
| `selftest/raw_search_example.jsonl` | Hand-written examples of the mistakes a search over the raw folder tends to make. They illustrate the failure cases and are not measured results. |

## Procedure for device testing

1. Copy `corpus/Board Documents` to the NAS, record the script and add the audio file to the folder.
2. Run a compile and compare the result with `expected-almanac-v1.md`.
3. Ask the eighteen initial questions, save the answers as JSON Lines, and score them with `--phase initial --recording`.
4. Ask the same questions through plain file chat over the raw folder and score those answers the same way.
5. Add `corpus/add-later/minutes-2026-09-15.docx` to the board folder and compile again. Confirm that claims were extracted only from the new minutes, that the quiet-hours rule was rechecked against the bylaws, that a new version was saved beside the first, and that every other rule is unchanged. Then ask the two update questions with `--phase after_update`.
6. Record run times, approval prompts and any files that failed.

All results will be reported as measured on the device.
