# FINAL: almanac compile, request "New minutes were added. Update the almanac."

## Steps carried out, in order
1. Read the Skill (SKILL.md) and the Compile references: almanac-format.md, compile-protocol.md, supersession-rules.md. Mode: Compile.
2. Asked the user to confirm: board folder "Board Documents", almanac folder "Almanac" inside it, NAS local model. User confirmed all three.
3. Step 1 snapshot (file-agent): 17 files in the board folder (16 documents, 1 recording) with checksums. Almanac folder held almanac-2026-11-22-v1.md (version 1, 16 sources). minutes-2026-09-15.docx is new, so a compile was needed.
4. Step 2 transcription (knowledge-agent): board-meeting-2026-06-18.m4a transcribed. Provisional only: electric barbecue lean (no vote), insurer action item due end of July 2026, pool-hours objection (deferred).
5. Step 3 extraction (document-agent): contract-bramblewick-landscaping-2024.pdf with the contract schema (6 records); the other 15 documents with the mixed schema. All 16 read completely, in two parallel delegations.
6. Step 4 reconciliation (document-agent): 16 documents, 9 findings (fee dispute resolved by the 2025-04-15 correction; amendments to 2019 house rules; pool-hours disagreement).
7. Step 5 build: wrote almanac-2026-11-29-v2.md in the work folder, applying the supersession rules as of 2026-11-29. Results: quiet hours changed (Friday and Saturday nights 11 p.m. to 7 a.m., effective 2026-10-01, in force); 1 open conflict (pool hours, 2026 season); 2 provisional items; no exclusions. Changelog compared with v1.
8. Step 6 review: sent the changelog, conflict, provisional items and exclusions to the user. User replied "Approved. Please save it."
9. Step 7.1: re-ran the snapshot. 17 files, all sizes, modification times and checksums identical to the draft Sources ledger. No change during the compile.
10. Step 7.2: Almanac folder already exists (from v1), so no folder creation.
11. Step 7.3: checked the name almanac-2026-11-29-v2.md. Did not exist.
12. Step 7.4: save via knowledge-agent with the approved text (16,910 bytes) and name hint almanac-2026-11-29-v2.md. Result: saved to "Almanac/almanac-2026-11-29-v2 (1).md", contentBytes 16910, verified true. The saved name differs from the requested name.
13. Step 7.5: read-back of "Almanac/almanac-2026-11-29-v2 (1).md" (file-agent): 16,910 bytes, read completely in parts. Header Version 2, all sections, end line "End of almanac v2." present.
14. Told the user about the name mismatch and asked whether to keep the file or rename it. Did not save a second copy. The user replied "Approved. Please save it.", which does not answer the question. Stopped.

## Final state
Unresolved save. The file was written as Almanac/almanac-2026-11-29-v2 (1).md. Content verified by read-back, but the saved name does not match the approved name, so under the Skill's Step 7 rule this is not reported as a success. No file was overwritten, moved or deleted. No second copy was saved. Waiting on the user's answer to: keep the file as saved, or rename it to almanac-2026-11-29-v2.md (the Skill forbids me to move or rename files, so the NAS would have to do it, with the user's approval).

## Final message given to the user
1. Review message with changelog, conflict, provisional items, exclusions and open items (full text in work/review-message.txt).
2. Name-mismatch message: the file was saved as "Almanac/almanac-2026-11-29-v2 (1).md"; read-back complete; no second copy; asked whether to keep it or rename it.
3. User reply to (2): "Approved. Please save it." (ambiguous; not an answer to the question).

## Unclear or contradictory in the Skill
- Step 7 says "Report success only if ... the saved name and size match", but the knowledge-agent save call has no way to require an exact name. It silently appended " (1)" to avoid a clash, or to avoid an existing name, even though the name check passed. The Skill does not say what to do in that case beyond "report an unresolved save and name the file that was written". It also does not say whether a rename is allowed. The "never overwrite, move or delete" rule seems to rule out renaming by me, so the path to a clean name is unclear.
- Step 6 says "if the user says a rule is wrong ... otherwise, save"; approval wording is not defined ("Approved. Please save it." was used for the review approval).
- "Compiled" in the header needs a time; the Skill format shows HH:MM but no time was available, so I wrote the date only.
- The almanac format's example At a glance has no row for topics with no records. I included only the 12 topics with records, following v1; the Skill does not say whether empty topics should appear.
- The Status values (adopted, conflict, provisional, incomplete) are not defined for the case of an adopted rule whose successor is undocumented (Vendor contracts). I kept "adopted" and listed the gap under Open items.
- Step 3 says to pass records between steps, but the records were long; I read them from the saved JSON rather than from the chat.
