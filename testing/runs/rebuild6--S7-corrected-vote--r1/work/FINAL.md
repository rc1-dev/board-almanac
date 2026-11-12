# FINAL: almanac Compile, "The April 2025 minutes were corrected and replaced. Update the almanac."

## Steps carried out, in order

1. Read the Skill (SKILL.md), then the Compile references it names: almanac-format.md, compile-protocol.md, supersession-rules.md.
2. Sent the required-input confirmation to the user (board folder, almanac folder, mode Compile, model route). User replied: board folder "Board Documents", almanac folder "Almanac" inside it, NAS local model, go ahead.
3. Step 1 snapshot (file-agent). 17 source files, 2 existing almanacs (v1, v2). Newest is v2. The Sources ledger shows minutes-2025-04-15.docx changed (size 36856 to 36934, checksum differs), so the compile continued.
4. Step 2 (knowledge-agent): transcribed board-meeting-2026-06-18.m4a. Three spoken items: electric barbecue lean (proposal), insurer action item, pool-hours objection. Recorded as provisional.
5. Step 3 (document-agent): contract-bramblewick-landscaping-2024.pdf with the contract schema (6 records); the other 15 non-audio documents with the mixed schema (all read completely). Output was large; read in full from the saved tool result.
6. Step 4 (document-agent): reconciliation across the 16 non-audio documents. Nine findings (fee disagreement and correction, amendments to pets, lease, parking, quiet hours, renovation hours, and a pool hours disagreement between minutes and notice).
7. Step 5: read the three reference files, then built almanac v3 from Steps 2 to 4 only. Written to work/almanac-2026-12-01-v3.md.
8. Step 6: sent the review (changelog, the corrected pet-rule vote, conflict, provisional items, exclusions) and asked for approval. User replied "Approved. Please save it."
9. Step 7.1: re-ran the snapshot. All 17 checksums matched the first snapshot. No source changed during the compile.
10. Step 7.3: name check for almanac-2026-12-01-v3.md. Result: does not exist.
11. Step 7.4: saved via knowledge-agent to Almanac/almanac-2026-12-01-v3.md. Result: verified true, 18,408 bytes.
12. Step 7.5: read-back via file-agent in 4000-character parts. Size 18,408, read_completely true, header version 3, end line "End of almanac v3." present, all sections present.

## Final state

Saved: Almanac/almanac-2026-12-01-v3.md (inside Board Documents). Verified.

Conflicts: 1 (2026 pool hours: minutes 2025-09-10 say 8:00 a.m. to 10:00 p.m.; notice 2026-05-01 says 8:00 a.m. to 9:00 p.m.).
Provisional: 2 (electric barbecues; pool hours objection), both from the recording only.
Exclusions: none.
Completeness: complete.

## Copy of the messages sent to the user (via the user command)

Message 1 (inputs confirmation): asked to confirm board folder "Board Documents", almanac folder "Board Documents/Almanac", mode Compile, and the model route. Reply: "Yes. The board folder is 'Board Documents' (paths are relative to it), the almanac folder is 'Almanac' inside it, and the NAS is set to use its local model. Please go ahead."

Message 2 (review, Step 6): the full changelog, the single pet-rule evidence change (vote 3-0 to 2-1 in the corrected copy), the 2026 pool hours conflict, the two provisional items, no exclusions, and the request for approval to save almanac-2026-12-01-v3.md. Reply: "Approved. Please save it."

Message 3 (final, after save): "The almanac is updated and saved as Almanac/almanac-2026-12-01-v3.md in Board Documents. The save was verified: the read-back is complete, 18,408 bytes, and the end line reads "End of almanac v3." What changed: the corrected April 2025 minutes change the recorded vote on the pet rule from 3-0 to 2-1. The rule itself, its date and its status are unchanged. No rule changed in the almanac. Still open: the 2026 pool hours conflict between the adopted minutes and the notice, the landscaping contract outcome (not established by the documents), and the electric barbecue question (recording only)." Reply: "Yes, please continue."

## Things in the Skill that were unclear or contradictory

- Step 4 says "reconcile all documents in the snapshot", while Step 3 and the compile protocol say recordings are never sent to document extraction. I sent the 16 non-audio files to reconciliation and excluded the recording; the recording's items are already in the Step 2 results. The Skill does not say which applies to Step 4.
- The almanac format requires a "Compiled" time (YYYY-MM-DD HH:MM). The NAS gave only the local date (2026-12-01), so the header has the date with "(NAS local date)" and no time.
- The Step 6 review rule and the compile protocol disagree on changelog detection. The protocol says a change only in evidence (here, the corrected 2-1 vote) is not detected by the summary comparison, but Step 6 asks for every meaningful change. I disclosed it explicitly in both the changelog and the review message.
- Authority ranking (rule 2 in supersession-rules.md) depends on whether a provision is in Part A (bylaws) or Part B (house rules). The Step 3 extraction did not say which part the pool-hours and quiet-hours provisions are in, so the pool conflict is recorded as a conflict under rule 2's "notice does not replace adopted decision" clause without a ranking claim.
- The Skill's own examples use different figures (version 7, 18 files, 2025-04-15 minutes as 3-0 in a sample); these are illustrative and I did not copy them.
- The landscaping "next notice point" (2027-01-30) is a calculation from the 60-day clause, not stated in any document. The format says due dates come from a document, otherwise "not stated". I recorded it as "not stated" with the calculation labelled.
