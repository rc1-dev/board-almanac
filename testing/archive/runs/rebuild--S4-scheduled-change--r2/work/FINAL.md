# FINAL: almanac run rebuild--S4-scheduled-change--r2

## Steps in order

1. Read PROMPT.md and SKILL.md. Read compile-protocol.md, supersession-rules.md, almanac-format.md (Compile) and ask-and-lint.md (Ask).
2. Confirmed inputs with the user: board folder "Board Documents", almanac folder "Almanac" inside it, mode Compile then Ask, model route NAS local model. User confirmed.
3. Compile Step 1 (file-agent snapshot): 18 source files plus 2 existing almanacs (v1 2026-11-22, v2 2026-11-29). Newest almanac v2 found. Not empty, so compile continued. Under the 60-file limit.
4. Compile Step 2 (knowledge-agent): transcribed board-meeting-2026-06-18.m4a. Three items: electric barbecues lean (no vote), insurer action item, pool-hours objection.
5. Compile Step 3 (document-agent): two batches. Mixed schema for 16 non-contract documents, contract schema for contract-bramblewick-landscaping-2024.pdf. All files completed and read completely.
6. Compile Step 4 (document-agent reconciliation): 17 files sent (all non-audio documents). Audio excluded, since recordings are never sent to document extraction (compile-protocol.md). 11 findings returned, including the parking 48h to 24h scheduled change and the pool hours conflict.
7. Compile Step 5: built the almanac myself from the returned records, as the Skill's build step asks. Wrote work/almanac-2026-12-01-v3.md. Changelog against v2: Parking scheduled change added; Vendor contracts status changed from adopted to incomplete; minutes-2026-11-10.docx is the new source.
8. Compile Step 6: showed the changelog, conflict (pool hours), provisional items (electric barbecues, pool-hours objection) and exclusions (none) to the user. User approved.
9. Compile Step 7: re-ran snapshot; file list and checksums matched the Step 1 snapshot. Name check: almanac-2026-12-01-v3.md did not exist. Save via knowledge-agent: saved as Almanac/almanac-2026-12-01-v3.md, 16173 bytes, verified. Read-back by file-agent: whole file, size 16173, reached "End of almanac v3."
10. Ask (A2): first document-agent call failed with "no almanac file supplied" when the almanac path was given only as --files. The retry passed it as --path and --files; it returned the almanac text, not an answer. The answer was composed from the almanac text.
11. Sent the review summary, the approval request and then the final answer to the user through the user channel. User replied "Yes, please continue."

## Final state

- Saved: Almanac/almanac-2026-12-01-v3.md (verified, 16173 bytes, read back completely).
- Almanac version 3, compiled 2026-12-01, 18 processed, 0 excluded, complete, 1 open conflict (pool hours 2026 season), 2 provisional items (electric barbecues; pool-hours objection in recording).

## Final message to user (summary)

Saved as Almanac/almanac-2026-12-01-v3.md. Answer: a guest car can stay in guest parking for up to 24 hours on January 5, 2027. The change takes effect 2027-01-01 (minutes-2026-11-10.docx, 3-0). Until then the rule is 48 hours (since 2025-10-01). No open conflicts or provisional items on this topic. Almanac v3, compiled 2026-12-01, so the 24-hour rule is the current one for January 5, 2027.

## Unclear or contradictory in the Skill

- Compile Step 4 says "all documents in the snapshot", but the Skill's protocol says recordings never go to document extraction. Unclear whether the reconciliation should include audio. I excluded the audio file.
- The Ask step names the question as "supplied in this request", but the delegate interface has no question field. I put the question in the instruction text. The Ask step also says the document expert answers, but the expert returned the almanac text with a note that the answer must be composed from it, so the answer was composed by the orchestrator. The result did not match the Ask step's expectation.
- The delegate command returned "no almanac file supplied" for --files alone; --path was needed for the Ask step. The Skill does not say which option carries the file.
- The almanac format asks for the whole topic list in fixed order, but does not say whether topics with no records (Special assessments, Waste and recycling, Insurance) must be present. I left them out, as v2 did.
- The format example header includes a time (e.g. 14:05). The NAS did not return a compile time, so the header says only the date.
- Pool hours: the 2019 bylaws give 9 a.m. to 9 p.m. for the season, and the 2025 minutes give 8 a.m. to 10 p.m. for the 2026 season. The documents do not say whether the minutes replaced the bylaws rule. The Skill's rules do not settle this, so I recorded it as a conflict with the 2019 rule as history only.
- Vendor contracts: the Skill's status vocabulary includes "incomplete", but it does not define when to use it. I used it because no successor contract is documented and the renewal effect is not decided by the documents.
- Ask answer: the freshness check was based on the snapshot just taken, which matched the new ledger. No separate Ask A1 call was run after the save.
