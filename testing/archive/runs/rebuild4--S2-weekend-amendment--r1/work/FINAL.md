# FINAL: almanac update, "New minutes were added. Update the almanac."

## Steps carried out, in order

1. Read PROMPT.md, then SKILL.md, then only the Compile references (almanac-format, compile-protocol, supersession-rules).
2. Asked the user to confirm the board folder (Board Documents), the almanac folder (Almanac inside it), the mode (Compile) and the model route. User confirmed: NAS local model.
3. Step 1 snapshot (file-agent): 17 source files (16 documents, 1 recording), plus the newest almanac, almanac-2026-11-22-v1.md. minutes-2026-09-15.docx was new and absent from v1's Sources ledger.
4. Step 2 (knowledge-agent): transcribed board-meeting-2026-06-18.m4a. Returned a barbecue proposal (no vote), an insurer action item and a deferred pool-hours objection.
5. Step 3 (document-agent): extraction in two calls. The contract went with the contract schema; the 15 other documents went with the mixed schema. All 16 documents were read completely. The audio was not sent to extraction.
6. Step 4 (document-agent): reconciliation of the 16 documents, audio excluded. Returned 9 findings: 3 fee items (resolved by the 2025-04-15 correction), 4 amendments to house rules, 1 pool-hours disagreement (minutes 2025-09-10 vs notice 2026-05-01), 1 quiet-hours amendment.
7. Step 5: built almanac-2026-11-29-v2.md locally from the Step 2 to 4 records, with supersession rules applied as of 2026-11-29. Written to work/almanac-2026-11-29-v2.md.
8. Step 6: sent the changelog, the open conflict, the provisional items and the incomplete topic to the user. User approved.
9. Step 7.1: re-ran the snapshot. All 17 files matched sizes, modification times and checksums.
10. Step 7.3: name check, almanac-2026-11-29-v2.md did not exist.
11. Step 7.4: saved via knowledge-agent. Result: Almanac/almanac-2026-11-29-v2.md, 16320 bytes, verified true.
12. Step 7.5: read back via file-agent in 5 parts, 16320 bytes, read_completely true. Header Version: 2, all 16 section titles present, end line "End of almanac v2." present. Joined text is byte-identical to the local copy.
13. Sent the final outcome message to the user, which the user acknowledged.

## Final state

Saved: Almanac/almanac-2026-11-29-v2.md (in the board folder "Board Documents"). Completeness: complete, 17 processed, 0 excluded. Open conflicts: 1 (2026 pool hours). Provisional items: 2. Status for vendor contracts: incomplete.

## Final message to the user (abbreviated)

Saved and verified: Almanac/almanac-2026-11-29-v2.md. Quiet hours changed to 11:00 p.m. to 7:00 a.m. on Friday and Saturday nights from 2026-10-01. Still open: the 2026 pool hours conflict, and the landscaping contract marked incomplete. Two provisional items come from the 2026-06-18 recording only.

## Unclear or contradictory in the Skill

- Step 1 says to confirm the model route before NAS work, but the Required input list does not say whether the route question must be asked when the user has already said "update the almanac". I asked it anyway, since the list requires it.
- Step 4 says "all documents in the snapshot", while Step 3 says audio is never sent to document extraction. I excluded the audio from reconciliation; the Skill does not say which applies to Step 4.
- Compile protocol says the Sources ledger and Open items are the only carry-over from the previous almanac, but the Step 5 instruction lists the previous At a glance table and Open items only for the changelog. Both readings were followed.
- The almanac format example shows a scheduled change for Parking ("Up to 24 hours from 2027-01-01"). v1 did not have it and no extracted document supports it, so v2 keeps Scheduled as none. The example is illustrative only.
- The almanac format does not say how a spoken relative date ("end of July") becomes a due date. I wrote "2026-07-31 (end of July 2026, as spoken)", as v1 had.
- The almanac format asks for a "Compiled" time, but the NAS did not return one. I wrote the date only.
- Step 5 says to compare the changelog with the previous At a glance table. When a superseded rule is partly overlapping a new one (pool 2026 season), rule 1 and rule 7 (conflict) pull in different directions. I kept the topic as a conflict with no superseded entry.
