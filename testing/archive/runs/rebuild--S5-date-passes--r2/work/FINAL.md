# FINAL: Compile run, Harbor View almanac (request: "Update the almanac.")

## Steps carried out, in order

1. Read SKILL.md and the three references the Compile mode needs (almanac-format, compile-protocol, supersession-rules).
2. Asked the user to confirm inputs: board folder "Board Documents", almanac folder "Almanac" inside it, mode Compile, model route. User confirmed all four and said the NAS uses its local model.
3. Step 1 snapshot (file-agent, read only): 18 source files in Board Documents, plus the almanac folder listing. Highest existing version was almanac-2026-12-01-v3.md (v1, v2 and v3 present). The snapshot matched the v3 Sources ledger, but the scheduled change "Guest parking up to 24 hours from 2027-01-01" had passed against the NAS local date 2027-01-02, so a compile was required.
4. Step 2 transcription (knowledge-agent): board-meeting-2026-06-18.m4a transcribed. Three items: an electric barbecue proposal (no vote), an action for the Secretary to ask the insurer by end of July, and a deferred objection on pool hours. Recorded as provisional.
5. Step 3 extraction (document-agent): 16 documents with the mixed schema in one batch, and contract-bramblewick-landscaping-2024.pdf with the contract schema. All 17 read completely. Audio was not sent. Records were returned per file, with quotes.
6. Step 4 reconciliation (document-agent): 17 documents, no audio. Eleven findings: fee disagreements and correction, pool hours disagreement, and several later amendments of house rules (renovation hours, pets, rentals, parking twice, quiet hours).
7. Step 5 build: almanac v4 written from the Step 2 to 4 records only, with the supersession rules applied as of 2027-01-02. The guest parking 24-hour rule is now current. Pool hours remain a conflict. Two provisional items. Five open items. Changelog compared with v3 At a glance. Written to work/almanac-template.md and built into work/almanac-2027-01-02-v4.md (17,797 characters) with the Sources ledger generated from a second snapshot run.
8. Step 6 review: sent the changelog, conflict, provisional items, open items, exclusions (none), and one point to confirm (whether the pet and balcony provisions are house rules or bylaws, since the extraction did not say which Part of the 2019 document they sit in). User replied "Approved. Please save it."
9. Step 7 check and save:
   a. Snapshot recheck: 18 files, identical to Step 1 (same sizes, times and checksums).
   b. Name check for almanac-2027-01-02-v4.md: does not exist.
   c. Save (knowledge-agent): Almanac/almanac-2027-01-02-v4.md, 17,797 bytes, verified true.
   d. Read-back (file-agent): size 17,797, read completely in parts. Read-back text matches the local file exactly, contains all sections, 15 topic subsections, and the end line "End of almanac v4."

## Final state

Saved: Almanac/almanac-2027-01-02-v4.md (inside Board Documents). Save verified. Previous versions v1 to v3 were not changed.

Summary of v4:
- Changed: Parking (24-hour guest parking now in force since 2027-01-01). Vendor contracts (Bramblewick agreement ended 2026-03-31, not renewed; notice dated 2026-02-02 after the 2026-01-30 due date).
- Added empty sections: Special assessments, Waste and recycling, Insurance (no records, marked incomplete).
- Open conflict: pool hours for the 2026 season (minutes-2025-09-10.pdf vs notice-2026-05-01-pool.pdf).
- Provisional: electric barbecues (recording), pool-hours objection (recording).
- Open items: 5.

## Final message given to the user

The last message sent to the user was the review message at step 8 (the changelog, conflict, provisional items, open items, exclusions, and the Part A/B confirmation request), ending with: "Save v4 as almanac-2027-01-02-v4.md in the Almanac folder? Reply "approve" to save, or tell me which passage was misread." The user replied "Approved. Please save it." No further message was sent after the save, because the Skill does not specify one.

## Unclear or contradictory points in the Skill

- Step 4 says "Reconcile all documents in the snapshot" but Step 3 says never send audio files. I treated the rule as documents only and left the recording out of Step 4. The Skill does not say which applies.
- The almanac format asks for "Compiled: YYYY-MM-DD HH:MM", but the NAS did not return a time of day, so the header has the date only.
- Authority ranking (supersession rule 2) depends on which Part (A bylaws or B house rules) of the 2019 document a provision sits in, but the extraction returns only the file and the document type "bylaws" for every 2019 provision. Where the minutes cite a "House Rule" number, I treated the provision as house rule. For pets, balcony/fixture rules, rental minimum and pool hours, the Part is not stated in the records, so I flagged this to the user for confirmation rather than deciding it.
- Step 3's batch rule ("in batches of up to 20 documents") and the schema rule (contracts use the contract schema) together left it open whether one batch may mix schemas. I used two calls: one mixed batch of 16 and one contract call of 1.
- The Skill says "Scheduled" lists changes after the compile date, and the compile protocol says a compile runs again once a scheduled date has passed. It does not say how a topic whose scheduled change has just taken effect should be labelled in At a glance ("Since" date versus "Scheduled: none"). I used the effective date as "Since" and "none" for Scheduled.
- Topics with no records: the format says "one subsection per topic" and the topic list has 15 entries, but the Skill does not say whether empty topics should appear. I included them, marked incomplete, so that absence is not read as established.
- Status values (adopted, conflict, provisional, incomplete) do not say what to use for a topic with a provisional recording item but an adopted rule. I used adopted for the rule and listed the recording item under Provisional.
