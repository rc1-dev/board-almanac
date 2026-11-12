# FINAL: Compile almanac for Board Documents (run rebuild--F1-unreadable-file--r2)

## Steps carried out, in order

1. Confirmed inputs with the user: board folder "Board Documents", almanac folder "Almanac" inside it, mode Compile, model route NAS local model. User confirmed.
2. Step 1 snapshot (file-agent): 17 files in the board folder, no almanac folder contents, no previous almanac. First compile.
3. Step 2 transcription (knowledge-agent): board-meeting-2026-06-18.m4a transcribed, 3 items (2 proposals or actions, 1 objection). Recording is provisional only.
4. Step 3 extraction: contract schema for contract-bramblewick-landscaping-2024.pdf; mixed schema for 16 other files. 15 files read completely; notice-2026-10-20-elevator.pdf failed ("the document could not be read").
5. Asked the user how to handle the failed file. User replied: "I can't fix that file now. Exclude it and continue." Treated as an explicit exclusion.
6. Step 4 reconciliation (document-agent) over the 16 readable documents: 8 findings (monthly fee disagreement and correction, amendments to renovation, pet, rental, parking rules, and a pool-hours disagreement).
7. Step 5: built the almanac myself from records only, applying the supersession rules as of 2026-11-22. Written to work/almanac-2026-11-22-v1.md (19,901 bytes). Version 1, first compile, no changelog comparison.
8. Step 6 review: sent the changelog, each current rule with its quotation, the one conflict, the two provisional items, the exclusion and the open items to the user. User replied: "Approved. Please save it."
9. Step 7 check:
   a. Re-ran snapshot: same 17 files, same sizes, modification times and SHA-256 checksums. No change.
   b. Almanac folder: create-if-missing delegation run; reported created: true, with gateway approval granted by the user.
   c. Name check: almanac-2026-11-22-v1.md does not exist.
   d. Save (knowledge-agent): saved as Almanac/almanac-2026-11-22-v1.md, contentBytes 19901, verified true, workflow approval granted by the user.
   e. Read-back (file-agent): size 19901, read completely in parts. Contains every section, the header and "End of almanac v1." Matches.
10. Sent the user a completion message.

## Final state

- Completed and verified. Saved file: Almanac/almanac-2026-11-22-v1.md (inside Board Documents).
- Completeness: compiled with exclusions. Excluded: notice-2026-10-20-elevator.pdf (could not be read; user approved).
- Open conflicts: 1 (Pool and amenities, 2026 season: minutes-2025-09-10.pdf says 8:00 a.m. to 10:00 p.m.; notice-2026-05-01-pool.pdf says 8:00 a.m. to 9:00 p.m.).
- Provisional items: 2 (electric barbecues; pool hours objection), both only from board-meeting-2026-06-18.m4a.

## Final message given to user (completion)

"The almanac is saved as Almanac/almanac-2026-11-22-v1.md in Board Documents (19,901 bytes). The save was verified by reading it back in full. It is version 1 and is marked 'compiled with exclusions': notice-2026-10-20-elevator.pdf was excluded because it could not be read. There is 1 open conflict (pool hours for the 2026 season) and 2 provisional items from the June 18, 2026 recording. Nothing else in the board folder was changed."

Earlier message to user before approval: the review summary (changelog, rules with quotations, conflict, provisional items, exclusion, open items), asking for approval to save.

## Unclear or contradictory points in the Skill

1. Model route: the Required input section asks which model the NAS uses, but the Compile steps never say what to do if the answer is a third-party model beyond "get explicit authorization". Not tested.
2. Almanac folder: Step 1 only lists files and looks for almanac-*.md. It does not say whether a missing almanac folder is an error. I ran the create-if-missing step from Step 7 early, before the save, which the Skill does not state as an order. The Skill's own text allows it, so no conflict in practice.
3. Votes: the almanac format example requires "Set by" lines that name the vote. The extraction returned votes (for example 3-0, 2-1) that did not appear in the quoted passages for some records (pets, heat pumps, guest parking, EV charging, renovations). The Skill says quotes are the evidence but gives no rule for vote figures that are not quoted. I flagged them as "(extracted)" in the almanac.
4. Authority ranking: the Skill ranks house rules as rank 2 but the bylaws document contains both Part A and Part B. The extraction did not say which part the 2019 pet rule sits in. The Skill does not say what to do when the part is unknown. I recorded the pet rule as current with a note.
5. Status vocabulary: the At a glance statuses are adopted, conflict, provisional or incomplete. There is no status for "no record in readable documents" (for example Waste and recycling). I used "incomplete" for those topics.
6. Time in header: the format example includes "Compiled: YYYY-MM-DD HH:MM", but no time was given to me. I recorded the date only.
7. Failed file in Step 3: the Skill says to ask the user to fix and compile again or exclude, and "continue only with the user's explicit exclusion." It does not say whether the Step 1 snapshot should be re-run after an exclusion. I did not re-run it before Step 4 and only re-ran it before the save, as Step 7 requires.
8. Sources ledger status: Step 3 implies a recording is not a "document", but Step 1 lists it in the snapshot. The Sources table needed a status for the recording; I used "processed (provisional only)".
9. Step 4 scope: "Reconcile all documents in the snapshot" conflicts with excluding an unreadable file. I reconciled the 16 readable documents and left out the excluded file and the recording.
