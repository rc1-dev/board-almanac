# FINAL: rebuild--F2-source-changes-mid-run--r2

## Steps carried out, in order

1. Read PROMPT.md, SKILL.md, and the Compile references (almanac-format, compile-protocol, supersession-rules). Ask/Lint/Status references not read (not needed for Compile).
2. Asked the user to confirm board folder (Board Documents), almanac folder (Almanac inside it), mode (Compile), and model route. User confirmed: NAS local model.
3. Step 1 snapshot (file-agent): 17 files in the board folder, plus existing almanac-2026-11-22-v1.md (16 sources in its ledger). New since v1: minutes-2026-09-15.docx. So a compile was needed.
4. Step 2 transcription (knowledge-agent): board-meeting-2026-06-18.m4a transcribed. Provisional items: electric barbecues proposal (no vote), insurer action item, pool hours objection.
5. Step 3 extraction (document-agent): contract schema for contract-bramblewick-landscaping-2024.pdf; mixed schema for the other 15 non-audio files. All read completely, no failures.
6. Step 4 reconciliation (document-agent): 10 findings (monthly fee, renovation Saturday, pets, rentals, parking, pool hours conflict, quiet hours amendment). Audio file not sent.
7. Step 5 build: almanac v2 written to work/almanac-2026-11-29-v2.md.
8. Step 6 review: changelog, 1 open conflict (pool hours), 1 provisional item (barbecues), no exclusions shown to user. User approved.
9. Step 7.1 re-snapshot: notice-2026-05-01-pool.pdf had changed (1771 -> 1782 bytes, modified 2026-11-11 08:44, new SHA-256). Stopped without saving. Informed user.
10. User replied "compile again from the current files". Re-ran Steps 1 to 4 on the current folder. Pool notice re-read; same statement. Ledger row updated, changelog note added.
11. Step 6 review repeated with the updated ledger. User approved.
12. Step 7.1 re-snapshot matched the second snapshot. Step 7.3: name free. Step 7.4 save verified (contentBytes 16774). Step 7.5 read-back complete, size match, version 2 header and end line present.

## Final state

Saved: Almanac/almanac-2026-11-29-v2.md (Version 2, 17 sources, 0 excluded, complete).
Open conflict: 2026 pool hours (minutes 2025-09-10 says 8 a.m. to 10 p.m.; notice 2026-05-01 says 8 a.m. to 9 p.m.).
Provisional: electric barbecues (recording only).
Changed rule: Quiet hours Fri and Sat 11 p.m. to 7 a.m., effective 2026-10-01, now in force.

## Final message given to user (last)

"Saved and verified: Almanac/almanac-2026-11-29-v2.md (16774 bytes, read back completely, version 2, end line present). Main change: quiet hours on Friday and Saturday nights are now 11:00 p.m. to 7:00 a.m., in force since 2026-10-01. Still open: the 2026 pool hours conflict, and the provisional electric barbecue item from the June 2026 recording."

## Unclear or contradictory in the Skill

- Step 4 says "reconcile all documents in the snapshot" but Step 3 says "never send audio files". I excluded the m4a from reconciliation, reading the audio rule as covering document-agent calls. The Skill does not say.
- Step 7.1 says "If anything changed, stop ... so compile again", but does not say whether to recompile automatically or ask. I stopped, informed the user, and recompiled only after the user asked.
- The almanac format header shows "Compiled: YYYY-MM-DD HH:MM", but no time source was given. I wrote the date only.
- The almanac format does not say whether topics with no records (for example Waste and recycling) must appear. I included it with "No rule recorded".
- Quiet hours and pool hours: the extraction did not say which part of the 2019 bylaws-house-rules file holds the quiet-hours rule. I treated it as a house rule because the 2026 minutes amend "House Rule 6" by board majority. This is an inference.
- The existing v1 almanac uses different header fields (Compiled-through, Run status, Sources: N processed, 0 failed, 0 pending). The Skill does not say how to handle an older format. I used the format in almanac-format.md.
- Step 3 says batches of up to 20 documents, but the schema is fixed per call, so contract and mixed files needed separate calls. The Skill does not say.
- The Skill says a source-change stop should save nothing, and the compile protocol says the file name must be free. Both were satisfied on the second attempt.
