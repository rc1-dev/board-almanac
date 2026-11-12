# FINAL: almanac update, run rebuild4--S2-weekend-amendment--r2

## Steps carried out, in order

1. Read PROMPT.md, then SKILL.md, then the Compile references (compile-protocol.md, supersession-rules.md, almanac-format.md). Did not open the board folder, harness or other run folders directly.
2. Asked the user to confirm the inputs: board folder "Board Documents", almanac folder "Almanac" inside it, mode Compile, model route. User confirmed; NAS local model.
3. Step 1 (snapshot): delegated to file-agent. Found 17 source files plus almanac-2026-11-22-v1.md (the highest version). minutes-2026-09-15.docx is new against v1's Sources ledger, so a compile was needed.
4. Step 2 (recordings): delegated board-meeting-2026-06-18.m4a to knowledge-agent. Returned three items: electric barbecues proposal (no vote), an insurer action item, and a pool-hours objection.
5. Step 3 (extraction): delegated the contract (contract-bramblewick-landscaping-2024.pdf) with the contract schema, and the other 15 documents with the mixed schema. The recording was not sent to extraction. All 16 documents were read completely.
6. Step 4 (reconcile): delegated the 16 documents to document-agent. Returned 10 findings: the $225/$230 fee correction, the $235 amendment, the 2024-06-12 Saturday amendment, the 2025 pets, rentals and parking amendments, the 2026 pool hours disagreement, and the 2026-09-15 quiet-hours amendment.
7. Step 5 (build): wrote almanac-2026-11-29-v2.md to the scratch work folder from the Step 2 to 4 records only. Applied the supersession rules as of 2026-11-29. Quiet hours: Friday and Saturday changed to 11 p.m. to 7 a.m. from 2026-10-01 (already in force, nothing scheduled). Pool hours: kept as an open conflict. Vendor contracts: marked incomplete.
8. Step 6 (review): showed the user the changelog, the open conflict, the provisional items, the incomplete topic and the absence of exclusions. User approved the save.
9. Step 7 (check and save):
   a. Re-ran the snapshot: same 17 files, checksums identical to Step 1.
   b. Almanac folder already existed; no creation needed.
   c. Name check for almanac-2026-11-29-v2.md: not present.
   d. Saved via knowledge-agent: Almanac/almanac-2026-11-29-v2.md, 16,521 bytes, verified true, workflow approval granted by user.
   e. Read back completely in parts via file-agent: same size, all sections present, header says Version 2, end line "End of almanac v2."
10. Told the user the save succeeded and summarised the changes. User replied "Yes, please continue."

## Final state

- Saved: Almanac/almanac-2026-11-29-v2.md (inside Board Documents), verified.
- Completeness: complete, 17 processed, 0 excluded.
- Open conflicts: 1 (Pool and amenities, 2026 season closing time: minutes-2025-09-10.pdf says 10:00 p.m., notice-2026-05-01-pool.pdf says 9:00 p.m.).
- Provisional items: 2 (electric barbecues from the recording; pool hours objection from the recording).
- Incomplete topic: Vendor contracts (landscaping, Bramblewick). Non-renewal notice sent 2026-02-02 after the 2026-01-30 deadline; whether the agreement ended is not established.

## Final message given to the user

"Almanac v2 is saved as Almanac/almanac-2026-11-29-v2.md in Board Documents (16,521 bytes, read back and verified). What changed: Quiet hours are now 11:00 p.m. to 7:00 a.m. on Friday and Saturday nights, in force since 2026-10-01; other nights are unchanged. Still open: the 2026 pool closing time conflict (minutes say 10:00 p.m., the notice says 9:00 p.m.), and the landscaping contract outcome is not established, so that topic is marked incomplete. Provisional items from the June recording: electric barbecues (no vote taken) and the pool hours objection. Nothing was excluded."

## Unclear or contradictory points in the Skill

- Step 3 says to extract in batches of up to 20 documents, but also requires a contract schema for contracts and a mixed schema for the rest. A single batch cannot use both schemas, so I made two calls. The Skill does not say how to split batches by schema.
- Step 3 says "every document in the snapshot" and Step 4 says "all documents in the snapshot", but the snapshot also contains audio. I excluded audio from extraction and reconciliation, as the Skill's "never send audio files" rule requires, but "all documents" is ambiguous on whether a recording counts as a document.
- almanac-format.md asks for a "Compiled" time (YYYY-MM-DD HH:MM), but the NAS results gave no time of day for the compile. I wrote the date only.
- The Step 1 instruction says to return the almanac folder's "Open items" and "Sources" sections, and the Open items of v1 used a "Due" date of 2027-01-30 that the contract does not state. The format asks for owner and due date "from a document; otherwise write not stated". I did not carry that v1 entry forward, since the due date is derived, not stated.
- Whether a recording objection (not a rule) counts as a "provisional item" is not settled. The format says Provisional lists items that come only from a recording, which the objection does, so I counted it and noted the change in the changelog.
- Balconies has two effective dates (2025-01-23 for heat pumps, 2019-05-01 for fixtures and barbecues). The format expects one "Effective" line per topic, so I put both on the line.
- The recording gives the insurer action due "by the end of July" with no year; I wrote "by the end of July 2026" based on the meeting date.
- Step 2 says to transcribe recordings, and the compile protocol says recording decisions are always provisional, but the Skill does not say whether a recorded decision that an adopted minute later records should move out of Provisional. This did not arise here.
