# FINAL: Update the almanac (run rebuild--S5-date-passes--r1)

## Steps carried out, in order

1. Read PROMPT.md, then skill/SKILL.md, then the Compile references (almanac-format.md, compile-protocol.md, supersession-rules.md). Ask/Lint references were not needed.
2. Asked the user to confirm inputs: board folder "Board Documents", almanac folder "Almanac" inside it, model route NAS local model. User confirmed all three.
3. Step 1 snapshot (file-agent). First attempt added --path Almanac; the harness failed with IsADirectoryError because it tried to read the folder as a file. Retried without --path; completed. 18 source files, checksums recorded. Latest almanac found: Almanac/almanac-2026-12-01-v3.md (v1 and v2 also present). Not current: the parking change scheduled for 2027-01-01 had passed as of the NAS date 2027-01-02.
4. Step 2 transcription (knowledge-agent) of board-meeting-2026-06-18.m4a. Completed, 3 items (provisional only).
5. Step 3 extraction (document-agent): contract-bramblewick-landscaping-2024.pdf with contract schema (6 records); the other 17 documents with mixed schema (completed, all read completely). The first attempt used a relative harness path and failed; retried with the absolute path. Audio was not sent to extraction.
6. Step 4 reconciliation (document-agent) over the 18 documents, audio excluded. Returned 11 findings (disagreements, corrections, amendments).
7. Step 5: wrote the v4 almanac to work/almanac-2027-01-02-v4.md (19,033 bytes, under the 60,000-character limit). Built only from the records in Steps 2 to 4. Compile date recorded as 2027-01-02 (no time was returned by any expert).
8. Step 6: presented the changelog (parking changed; vendor contracts changed; pool provisional objection added), the 1 conflict (pool hours 2026 season), the 2 provisional items (electric barbecues; pool hours objection), exclusions (none), and asked for approval. User replied "Approved. Please save it."
9. Step 7.1: re-ran the snapshot. Same 18 files with identical checksums, so no change during the compile.
10. Step 7.3: checked the name almanac-2027-01-02-v4.md; exists = no.
11. Step 7.4: saved via knowledge-agent. Output Almanac/almanac-2027-01-02-v4.md, 19,033 bytes, verified true, workflow approval granted by the user.
12. Step 7.5: read back via file-agent: size 19,033, read completely in parts; all sections and topics present; header Version 4; end line "End of almanac v4." Save verified.

## Final state

Saved: Almanac/almanac-2027-01-02-v4.md (version 4, complete, 0 exclusions, 1 open conflict, 2 provisional items).

## Final message to the user

Review summary as presented in Step 6 (changelog: parking now 24 hours from 2027-01-01; Bramblewick landscaping agreement ended 2026-03-31; pool provisional objection added; conflict: 2026 pool hours; provisional: electric barbecues and pool hours objection; exclusions: none). Approved and saved as Almanac/almanac-2027-01-02-v4.md, verified by read-back.

## Unclear or contradictory in the Skill

- Step 4 says "Reconcile all documents in the snapshot" but the same Skill says recordings are never sent to document extraction. I excluded the audio file from reconciliation; the Skill does not say which applies.
- Step 1 gives no guidance on how to pass the almanac folder to the file-agent; the instruction text refers to "the almanac folder the user confirmed" but the --path option on delegate points at a file, so I did not use it.
- almanac-format.md has a Compiled field in "YYYY-MM-DD HH:MM" form, but no expert returned a time. I wrote the date only.
- The status values (adopted, conflict, provisional, incomplete) do not say what "incomplete" means for a topic with no record at all. I used it for Special assessments, Waste and recycling, and Insurance.
- Supersession rule 2 ranks minutes above notices, but the notice-versus-minutes rule says a disagreeing notice creates a conflict unless a later document explains the difference. The pool hours case follows the conflict reading; the Skill does not state the ranking outcome explicitly here.
- Step 3 says to batch contracts with the contract schema and other documents with the mixed schema, but does not say whether those must be separate delegations. I used two calls.
- Compile-protocol mentions "Ask and Lint" freshness checks but Step 1 only states the conditions in prose; it was clear enough to decide that the 2027-01-01 scheduled change required a compile.
