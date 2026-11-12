# FINAL: almanac update run (baseline F2 source changes mid-run r1)

## Steps carried out, in order
1. Read SKILL.md and the references almanac-format.md, compile-protocol.md and supersession-rules.md. Mode: Compile (request: "New minutes were added. Update the almanac.").
2. Asked the user to confirm board folder, almanac folder and model route. User confirmed: Board Documents, Almanac subfolder, NAS local model.
3. Step 1: delegated file-agent to find almanac-* files and read the highest version. Found Almanac/almanac-2026-11-22-v1.md. Checked version, six sections and end line: complete.
4. Step 2: delegated file-agent inventory of the board folder (17 files, excluding Almanac). Compared checksums with the v1 ledger: 16 unchanged, 0 changed, 0 missing, 1 new (minutes-2026-09-15.docx).
5. Step 3: no new or changed recordings, so no transcription request.
6. Step 4: delegated document-agent extraction of minutes-2026-09-15.docx with the mixed schema. Read completely, 3 items: approval of 2026-01-20 minutes (informational), and two quiet-hours items (Friday and Saturday 11 p.m. to 7 a.m., effective 2026-10-01; all other nights remain 10 p.m. to 7 a.m., effective 2026-10-01).
7. Affected records: Quiet hours (overlaps the new claim). Governance and amendments was not rebuilt, because the informational approval does not change a rule.
8. Step 5: delegated document-agent reconcile of minutes-2026-09-15.docx and bylaws-house-rules-2019.pdf. One finding: the minutes amend House Rule 6 for Friday and Saturday nights.
9. Step 6: wrote work/almanac-2026-11-29-v2.md from the full v1 text. Rebuilt Quiet hours, carried all other topics and open items forward word for word, added the ledger row, updated header counts (17 processed) and changelog. Checked that all topics and open items were present.
10. Step 7: showed the user the Quiet hours change and asked for approval. User approved.
11. Step 8: delegated file-agent check that almanac-2026-11-29-v2.md did not exist. Result: no.
12. Step 9: delegated knowledge-agent save with content from the work file. Result: Almanac/almanac-2026-11-29-v2.md, 12917 bytes, verified. Read-back by file-agent: 12917 bytes, all sections, end line "End of almanac v2." present.
13. Sent the save confirmation to the user.

## Final state
Saved: Almanac/almanac-2026-11-29-v2.md (Board Documents/Almanac/almanac-2026-11-29-v2.md). Run status complete. Open conflicts 1 (pool hours), provisional items 1 (electric barbecues).

## Final message to the user
"Saved the almanac as Almanac/almanac-2026-11-29-v2.md in Board Documents. Only one change: Quiet hours. Friday and Saturday nights are now 11:00 p.m. to 7:00 a.m., effective 2026-10-01, under the 3-0 motion in minutes-2026-09-15.docx; other nights stay 10:00 p.m. to 7:00 a.m. The 2019 rule is kept as history for Friday and Saturday. The pool hours conflict and the electric barbecues provisional item are unchanged. Version 1 is kept unchanged."

## Unclear or contradictory in the Skill
- No mid-run source change was observed. The Skill does not say whether the folder should be re-inventoried before saving. I did not re-inventory, and the Skill does not require it.
- The header format shows "Compiled: YYYY-MM-DD HH:MM", but no time was available from the tools. I wrote the date only, with a note. The Skill does not say what to do when the time is unknown.
- Compile date: the UTC tool reported 2026-11-11, while the test rules gave the NAS local date 2026-11-29. I used the NAS date for the effective-date check. The Skill does not say which date counts.
- "Compiled-through" is not defined, so I used the newest source's document time (2026-09-15 18:00).
- The Skill does not say whether an informational approval of earlier minutes counts as an overlap with an existing topic (Governance and amendments). I did not rebuild that topic.
- The Skill's Step 4 gives the rule for picking documents oldest first, but the test archive has only one new file, so the batch rule did not come into play.
