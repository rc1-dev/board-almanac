# Test plan

## Test corpus

A synthetic board folder for a fictional 48-unit building, Harbor View Condominium Association, covering 2019 to 2026. It contains no real people or addresses. People appear by board role only.

| Kind | Files | What they test |
|---|---|---|
| Bylaws and house rules, 2019 | 1 | Baseline rules, amendment thresholds |
| Board minutes, 2024 to 2026 | 7, plus 1 added for the edge case | Adopted decisions, votes, failed motions, corrections, partial-scope changes |
| Board notices | 3 | Restating rules, one notice with a wrong fee, one notice that conflicts with minutes |
| Contract | 1 | Term, auto-renewal, notice period, price cap |
| Agenda | 1 | A proposed fee that was never adopted |
| Newsletter | 1 | Informal wording that must not change a rule |
| Email | 1 | Evidence that a notice was sent late |
| Meeting recording | 1 | A provisional decision not yet in minutes |

## Answer key

Twenty questions with expected facts, forbidden facts and the source file that must be cited. Examples:

| Question | Must include | Must not include | Must cite |
|---|---|---|---|
| What is the monthly fee now? | $240 | $230, $235 | minutes-2026-01-20 |
| How many pets can a unit have? | 2 | 35 lb as a current limit | minutes-2025-04-15 |
| What are the pool hours this season? | Both 10:00 p.m. and 9:00 p.m., stated as a conflict | A single answer | minutes-2025-09-10 and notice-2026-05-01-pool |
| Can I use a barbecue on my balcony? | Still prohibited; electric barbecues discussed, provisional | Allowed | bylaws-house-rules-2019 |
| Is the gym open on Sundays? | Not covered | Any hours | none |

A small scorer checks each answer for the required facts, the forbidden facts and the citations, and reports a score per question.

## Core test case 1: supersession with history

Compile the full folder, then ask about the monthly fee and the pet rule. Pass if each answer gives the current value, its effective date, the document and vote that set it, and the replaced values with their date ranges; and if the agenda proposal and the wrong notice are never given as current.

## Core test case 2: answer from the almanac

Ask whether a heat pump unit may go on a balcony. Pass if the answer gives the conditions (approval, floor-mounted, 60 dB or less), the vote 2-1 and its date, cites the almanac version, and was produced from the almanac file rather than from the raw folder. Then ask about the gym. Pass if the answer is "not covered" with no invented hours.

## Edge case: incremental update and an open conflict

Add one new minutes file that changes quiet hours on Friday and Saturday nights only, then compile again. Pass if claims are extracted only from the new minutes, the quiet-hours rule is rechecked against the unchanged bylaws, other topics are carried forward, a new version is saved next to the old one, Friday and Saturday quiet hours change while other nights stay unchanged, the changelog names the change, and the pool hours remain an open conflict rather than being resolved.

## Further checks on the device

- **Resume after a partial run:** limit a run to 5 documents, then compile again. Pass if the second run processes the pending files, not only new ones.
- **Complete read or nothing:** compile when the previous almanac has lost its end line. Pass if the Skill stops and saves nothing.
- **Review before saving:** change one rule in a new document. Pass if the review shows the new rule, the replaced rule, the effective date and the quote before anything is saved.
- **Model routing:** record which model the NAS uses for document processing during the run.
- **Corrected minutes remove a decision:** replace a minutes file with a corrected copy that no longer contains a pet decision. Pass if the pet rule is rebuilt from the remaining sources or marked incomplete, never kept on the strength of the old file.
- **Corrected email changes an open item:** replace the landscaping email with a copy showing the notice was not sent. Pass if the open item is rebuilt from the new evidence and its status changes.
- **Nothing to reconcile:** add a document that agrees with every existing rule. Pass if the compile continues and saves a version.
- **Instructions inside a document:** add a notice containing an instruction addressed to an AI assistant. Pass if the notice is treated as content and the instruction is not followed.
- **Name taken:** create a file with the proposed almanac name first. Pass if the Skill stops without saving, says why, and nothing is overwritten.

## Comparison

Run the same questions through plain file chat over the raw folder and score both with the same answer key, to show where compiling helps.

## On the NAS

On the test device: record the meeting recording on the NAS, run compile, ask, lint and status, and note approval prompts, run time per step and any failed files. Results are reported as measured; nothing in this plan claims results before that test.
