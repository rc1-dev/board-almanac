# FINAL: almanac compile, Board Documents (run rebuild4--S1-first-compile--r1)

## Steps carried out, in order

1. Confirmed inputs with the user: board folder "Board Documents"; almanac folder "Almanac" inside it; model route NAS local model. User replied yes to all three.
2. Step 1 snapshot (file-agent, read only): 16 files in the board folder, no almanac-* files in Almanac, so this is a first compile. Board folder not empty. Under the 60-file limit.
3. Step 2 transcription (knowledge-agent): board-meeting-2026-06-18.m4a completed. Three provisional items (electric barbecues proposal, insurer action, pool-hours objection). Quality warning: overlapping speech at 00:01:40.
4. Step 3 extraction (document-agent): contract-bramblewick-landscaping-2024.pdf with contract schema (6 records). The other 14 documents with mixed schema, one batch. All 15 read completely, no failures, no exclusions.
5. Step 4 reconciliation (document-agent): 8 findings, covering the fee history ($225 vs $230 notice, corrected in April 2025), amendments to Saturday work, pets, leasing, parking, and the 2026 pool hours disagreement. Recording excluded from document extraction and reconciliation, as the protocol requires.
6. Step 5 build: wrote the complete almanac v1 by hand from the returned records only, in the almanac format. Saved a copy at work/almanac-2026-11-22-v1.md.
7. Step 6 review: sent changelog, every topic's rule with quotation, the open conflict, provisional items and exclusions (none) to the user, asked for approval. User replied "Approved. Please save it."
8. Step 7 check and save:
   - Re-ran snapshot: all 16 files unchanged (sizes, times, SHA-256 identical).
   - Almanac folder: file-agent reported it created (user gateway approval granted). Note: the Skill says create only if missing; the response said "created: true", so it was absent before.
   - Name check: almanac-2026-11-22-v1.md did not exist.
   - Save (knowledge-agent, workflow approval granted): Almanac/almanac-2026-11-22-v1.md, 18,798 bytes, verified true.
   - Read-back (file-agent, read only, in 4,000-character parts): size 18,798, read_completely true, contains header Version 1, all 12 topic sections, Sources table, Changelog, end line "End of almanac v1."
9. Sent the user a save confirmation. User replied "Yes, please continue."

## Final state

Saved: Almanac/almanac-2026-11-22-v1.md (relative to Board Documents). Compile succeeded; Step 7 verification passed.

Final message given to the user (review, then save confirmation):
- Review: changelog (first compile), each topic's current rule with quotation, open conflict (2026 pool hours: minutes 10:00 p.m. vs notice 9:00 p.m.), vendor contracts incomplete (landscaping outcome not established), provisional items (electric barbecues, pool-hours objection), 0 exclusions. Asked for approval to save almanac-2026-11-22-v1.md.
- Save confirmation: "Saved: Almanac/almanac-2026-11-22-v1.md (18,798 bytes, verified by read-back, version 1, complete with 16 sources and 0 exclusions). Open conflict: pool hours ... Incomplete: the landscaping contract outcome ..."

## Unclear or contradictory points in the Skill

1. Compiled-time header: the almanac format shows "Compiled: YYYY-MM-DD HH:MM" but the Skill gives no way to get the NAS time. I wrote the date only.
2. Step 1 "Sources" check: the Skill's list is "find Markdown files whose names start with almanac-", but the Almanac folder's existence is not checked in Step 1. Step 7.2 says create it only if missing, but the create delegation reported created: true, so it was missing. The Skill does not say what to do if it already exists in a different form.
3. Recordings and Step 4: "Reconcile all documents in the snapshot" could be read to include the audio file. The compile protocol says recordings never go to document extraction, so I left the recording out of reconciliation. The Skill should say this explicitly for Step 4.
4. Part A and Part B: the bylaws define house rules as Part B, but the extracted records do not say which part the pet, leasing, parking and renovation rules sit in. The minutes cite "House Rule N", so the house-rule amendment threshold (board majority) was applied as the governing authority. The almanac says this is not stated in the records. The Skill does not say what to do when a provision's part is unknown.
5. Effective date for the heat pump policy: no effective date is recorded, so the almanac uses the decision date labelled as such. The Skill allows this in its format rules but does not say how to treat "effective immediately" wording.
6. Pool hours for the 2026 season: the Skill's rule 2 says a notice does not replace an adopted resolution, and rule 7 makes this a conflict. The 2019 standing hours for the same season are replaced by the adopted minutes for the 2026 season only; the Skill does not say whether a period-specific minutes item replaces a standing rule that covers all seasons. I recorded the 2026 season as the conflict and the other seasons under the standing rule.
7. Open items: the Skill requires owner and due date from a document, otherwise "not stated". Spoken recording items have only "as spoken" values. I labelled them provisional.
8. Vendor contracts: the Skill says to mark the topic incomplete when an outcome depends on whether a notice deadline was met. I marked it incomplete and stated the outcome is not established. The 60-day deadline date (2026-01-30) comes from the minutes' stated due date, not from my own calculation.
