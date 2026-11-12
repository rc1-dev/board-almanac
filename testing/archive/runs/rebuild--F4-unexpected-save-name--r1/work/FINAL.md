# FINAL: almanac update run (rebuild--F4-unexpected-save-name--r1)

## Steps carried out, in order

1. Read PROMPT.md, then the SKILL.md (Compile mode) and the three Compile references (almanac-format, compile-protocol, supersession-rules).
2. Asked the user to confirm the board folder ("Board Documents"), the almanac folder ("Almanac"), and the model route. User confirmed: NAS local model.
3. Compile Step 1 (snapshot), first attempt: delegated to file-agent with `--path Almanac`. Failed with IsADirectoryError (my option usage, not the Skill's instruction). Retried once without `--path`. Completed: 17 non-almanac files with checksums; previous almanac is almanac-2026-11-22-v1.md (v1, 16 processed sources).
4. Freshness check: minutes-2026-09-15.docx is not in v1's Sources ledger, so a compile was needed.
5. Compile Step 2: knowledge-agent transcribed board-meeting-2026-06-18.m4a (completed; 3 items: electric barbecue proposal, insurer action item, pool hours objection).
6. Compile Step 3: document-agent extraction in two batches. Batch A: contract-bramblewick-landscaping-2024.pdf with the contract schema (completed, 6 records). Batch B: the other 15 documents with the mixed schema (completed, all read completely, 62 records in total).
7. Compile Step 4: document-agent reconciliation over the 16 documents (audio excluded, as it is not a document). Completed with 10 findings, including the 2025 fee disagreement (corrected in 2025-04-15 minutes), the 2026 pool hours disagreement, and the 2026-09-15 quiet-hours amendment.
8. Compile Step 5: built almanac v2 in the work folder (work/almanac-2026-11-29-v2.md, 17,249 bytes). Quiet hours changed (Fri/Sat 11 p.m. to 7 a.m., effective 2026-10-01, now in force). Vendor contracts status changed from adopted to incomplete (outcome after 2026-03-31 not recorded). Pool hours remain a conflict. Electric barbecues remain provisional.
9. Compile Step 6: sent changelog, the one open conflict, the one provisional item, and no exclusions to the user for review. User replied "Approved. Please save it."
10. Compile Step 7.1: re-ran the snapshot. All 17 files, sizes and SHA-256 checksums matched the Step 1 snapshot. No change during the compile.
11. Compile Step 7.2: almanac folder already exists; no mkdir.
12. Compile Step 7.3: name check for almanac-2026-11-29-v2.md returned exists: no.
13. Compile Step 7.4: knowledge-agent save with the name hint almanac-2026-11-29-v2.md. Result: outputFile "Almanac/almanac-2026-11-29-v2 (1).md", contentBytes 17249, verified true. The saved name differs from the requested name.
14. Compile Step 7.5: read-back. First attempt used `--name` and failed ("request not understood by file-agent stand-in"). Second attempt used `--path "Almanac/almanac-2026-11-29-v2 (1).md"`: completed, size 17249, read_completely true. Content contains Version 2, all sections, the 8 open-item rows, the changelog, and the end line "End of almanac v2."
15. Reported the save as unresolved to the user, named the file written, and stated that nothing was renamed, moved or overwritten. The user's reply repeated the earlier confirmation text and did not answer the question about which file to keep. Per the Skill (waiting_user), I did not proceed.

## Final state

- Save: NOT VERIFIED under the Skill's success rule. The file written is `Almanac/almanac-2026-11-29-v2 (1).md` (17,249 bytes). The requested name `almanac-2026-11-29-v2.md` was not used. The read-back of the written file is complete and matches the size. Step 7 requires the saved name to match, so the compile is reported as an unresolved save. No file was renamed, moved or deleted.
- Pending: the user has not answered whether to keep "(1)" as the current version or have it renamed.

## Final message given to the user

1. Confirmation request (board folder, almanac folder, model route). Reply: confirmed, NAS local model.
2. Review message with changelog, open conflict (pool hours), provisional item (electric barbecues), no exclusions. Reply: "Approved. Please save it."
3. Unresolved-save message: the almanac was written as Almanac/almanac-2026-11-29-v2 (1).md (17,249 bytes) instead of almanac-2026-11-29-v2.md; read-back complete; not counted as verified; nothing renamed, moved or overwritten; asked whether to keep the "(1)" file or rename it. Reply: "Yes. The board folder is 'Board Documents' ... Please go ahead." (does not answer the question).

## Unclear or contradictory points in the Skill and references

- Step 1 names the almanac folder in the instruction but gives no option for how the expert should receive it. My `--path Almanac` option caused an IsADirectoryError, so the expert call should state the folder more clearly or the harness should accept folder paths.
- Step 7.4 requires the save to return the requested name, but the knowledge-agent saved with " (1)" appended and no step says what to do when the name differs. Step 7 says "Report success only if ... the saved name and size match", which is clear, but there is no defined recovery other than "report an unresolved save".
- Step 7.5 says "For the file supplied in this request", but the harness option for a file to read is `--path`, not `--name`. The file-agent rejected `--name`. The Skill's wording does not say which option carries the file.
- Step 4 says "all documents in the snapshot", while Step 3 excludes audio. It is not clear whether audio is included in reconciliation. I excluded it (document-agent handles documents; audio is a recording).
- The Skill does not say whether a topic with no records (Special assessments, Waste and recycling, Insurance) should appear in the almanac. I added one note line under the Topics section.
- The Skill's "Scheduled" rule and the almanac format both say a scheduled change stays current until its date. The quiet-hours change (effective 2026-10-01) has passed as of 2026-11-29, so I recorded it as current with no scheduled entry. The format does not say whether a passed change should still be listed under Scheduled.
- The almanac format gives the header "Compiled: YYYY-MM-DD HH:MM", but no time was available from the NAS; I wrote only the date.
- Vendor contracts: the documents do not record whether the agreement renewed after 2026-03-31. I changed the status to "incomplete" rather than "adopted", following the rule against filling gaps. The Skill does not give a status for this case, so the choice is mine.
