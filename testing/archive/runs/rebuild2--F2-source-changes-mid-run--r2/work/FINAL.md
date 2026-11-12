# FINAL: Almanac update, rebuild2--F2-source-changes-mid-run--r2

## Steps carried out, in order

1. Read PROMPT.md, then SKILL.md, then the references for Compile (almanac-format.md, compile-protocol.md, supersession-rules.md).
2. Asked the user to confirm board folder (Board Documents), almanac folder (Almanac), mode (Compile) and model route. User confirmed, NAS local model.
3. Compile Step 1, first snapshot: 17 files in the board folder; previous almanac almanac-2026-11-22-v1.md (16 sources). New file since v1: minutes-2026-09-15.docx. Proceeded.
4. Compile Step 2 (transcription), Step 3 (extraction, mixed schema for 15 files, contract schema for the Bramblewick contract; audio never sent to extraction), Step 4 (reconciliation of 16 non-audio files). All completed. Extraction found the quiet-hours amendment in minutes-2026-09-15.docx.
5. Step 5: I built the v2 draft myself from the Step 2 to 4 records, applying the supersession rules as of 2026-11-29, and wrote it to work/almanac-2026-11-29-v2.md.
6. Step 6: showed the user the changelog, provisional items, conflicts and exclusions (none); user approved the save.
7. Step 7.1 re-check: notice-2026-05-01-pool.pdf had changed (size 1771 to 1782, modified 2026-11-11 17:50, SHA-256 now 5d5964971a8bb014). Stopped without saving and told the user.
8. User asked to compile again from current files. Restarted at Step 1 (snapshot 2: 17 files, notice at the new checksum). Re-ran Steps 2 to 4; record counts matched the first run for every file, and the reconciliation gave the same 9 findings. Updated the draft's Sources row for the notice and added a changelog line for the changed file.
9. Step 6 again (fresh compile): showed the review; user approved the save.
10. Step 7.1: re-check against snapshot 2, identical (17 files, same sizes, times and checksums). Step 7.3: name almanac-2026-11-29-v2.md did not exist. Step 7.4: saved as Almanac/almanac-2026-11-29-v2.md, verified, 17168 bytes. Step 7.5: read back completely in parts; size and structure match, end line present.
11. Told the user the save was verified.

## Final state

Saved: Almanac/almanac-2026-11-29-v2.md (in Board Documents). Version 2, completeness complete, 17 sources, 0 excluded, open conflicts 1 (2026 pool hours), provisional items 2 (electric barbecues; pool-hours objection). Changes from v1: quiet hours changed (Friday and Saturday nights 11:00 p.m. to 7:00 a.m., adopted 2026-09-15, effective 2026-10-01; other nights unchanged); landscaping renewal row now "not stated" for owner and due; insurer item shows due date passed; pool objection added as provisional.

## Final message to the user (last one)

"Saved. The almanac is now almanac-2026-11-29-v2.md in the Almanac folder (17 sources, complete, 0 excluded). The only rule change is quiet hours: Friday and Saturday nights are now 11:00 p.m. to 7:00 a.m. (adopted 2026-09-15, effective 2026-10-01); other nights stay 10:00 p.m. to 7:00 a.m. The 2026 pool-hours conflict is still open. Read-back verified: 17,168 bytes, every section and the end line present."

## Unclear or contradictory in the Skill

- Step 4 says "reconcile all documents in the snapshot" while Step 3 says never send audio, and the snapshot includes the recording. I excluded the recording from reconciliation.
- Step 5 says to build the almanac from the records but does not say who builds it. I built it myself.
- The format says "Owner and due date come from a document; otherwise write not stated", but the v1 almanac had a calculated date (60 days before 2027-03-31). I used "not stated" and recorded the calculation in the item's text.
- The provisional rule covers "items that come only from a recording, an agenda or an email". It does not say whether a recording objection (not a rule) counts. I listed the pool objection as provisional.
- Step 7 says to stop when sources change and to compile again on request, but does not say whether the review and approval in Step 6 apply again. I asked for approval again on the fresh compile.
- The header format shows a time for "Compiled", but the NAS date was given without a time; I used the date only.
- The v1 header had a "Compiled-through" line that the format does not include; I did not carry it over.

DONE
