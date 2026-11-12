# FINAL: almanac compile, Board Documents (run rebuild3--S1-first-compile--r2)

## Steps carried out, in order

1. Confirmed inputs with the user: board folder "Board Documents", almanac folder "Almanac" inside it, mode Compile, model route NAS local model. User replied: "Yes. ... Please go ahead."
2. Step 1 snapshot (file-agent): 16 files listed with path, size, modified time and SHA-256. No almanac- files in the almanac folder, so this is a first compile. Board folder not empty, under the 60-file limit.
3. Step 2 transcription (knowledge-agent): transcribed board-meeting-2026-06-18.m4a. Returned 3 spoken items (1 proposal, 1 action item, 1 objection), all provisional. No failure.
4. Step 3 extraction (document-agent), two requests: contract-bramblewick-landscaping-2024.pdf with the contract schema (6 records, read completely); the other 14 text documents with the mixed schema (all read completely; 68 records in total). The audio file was not sent to extraction.
5. Step 4 reconciliation (document-agent) on the 15 non-audio documents: 8 findings (2 monthly-fee disagreements and correction, 4 amendments of house rules, 1 pool-hours disagreement, 1 fee amendment).
6. Step 5 build: wrote almanac-2026-11-22-v1.md in the scratch work folder (17,443 bytes). Built from the Step 2-4 records only.
7. Step 6 review: sent the changelog, each topic's rule with its quotation, the 1 conflict, the incomplete topic, the 2 provisional items and the exclusions (none) to the user. User replied: "Approved. Please save it."
8. Step 7 check, save and verify:
   1. Re-ran the Step 1 snapshot: 16 files, sizes, modification times and checksums identical to the first snapshot. Nothing changed.
   2. Almanac folder: created by file-agent with gateway approval ("created": true).
   3. Name check: almanac-2026-11-22-v1.md does not exist ("exists": "no").
   4. Save (knowledge-agent): saved to Almanac/almanac-2026-11-22-v1.md, 17443 bytes, verified true (workflow approval granted).
   5. Read-back (file-agent): size 17443, read completely in parts; contains every section and topic, with Version 1 in the header and "End of almanac v1." as the last line.

## Final state

Saved: Almanac/almanac-2026-11-22-v1.md (verified; name and size match; read-back complete).
Completeness: complete. 16 processed, 0 excluded. Open conflicts: 1. Provisional items: 2. Vendor contracts topic marked incomplete.

## Final message given to the user

Review message (before approval): "Review before saving: almanac-2026-11-22-v1.md (first compile, no previous almanac, nothing saved yet). Built from 16 files: 15 documents and 1 recording ... Save almanac-2026-11-22-v1.md in the Almanac folder? Reply yes to save, or tell me which passage is misread ... Reply no to stop without saving." The full text is in <runs>/rebuild3--S1-first-compile--r2/work/review-message.txt.

There was no separate message after the save; the approval reply "Approved. Please save it." was the last user message.

## Things in the Skill that were unclear or contradictory

- Step 4 says "reconcile all documents in the snapshot", but the Compile protocol says recordings are never sent to document extraction. I read this as excluding the recording from reconciliation; the Skill does not say so explicitly.
- Step 1 asks for the almanac folder but leaves it to the user to confirm; the "Almanac" folder did not exist, and the Skill does not say whether the folder-creation step should run before or after the confirmation. I ran it after the user's approval, in Step 7.2.
- almanac-format.md gives the header line "Compiled: 2026-11-22 14:05" with a time. I have no clock for the NAS time, so I wrote the date only.
- The Sources ledger status values (processed, excluded) do not say how a recording that was transcribed but is provisional only should be recorded. I used "processed (transcribed; provisional only)".
- The extraction results do not say whether a rule came from Part A (bylaws) or Part B (house rules). For the Saturday work, pet, rental and parking rules I treated them as house rules, which the board can amend by majority vote. The Skill says to rank by provision, not by file, and I could not check the provision from the extraction alone.
- Rule 2 in supersession-rules.md says a notice that disagrees with an adopted resolution "does not replace it: record a conflict". For the pool hours I recorded a conflict, which follows that sentence; the bylaws-era rule is listed under Superseded for seasons other than 2026.
- The Step 6 instruction asks for each topic's rule with its quotation on a first compile; the almanac-format changelog has no first-version form. I wrote a first-version changelog entry.
- The Skill names the file with a version number and a Compiled timestamp, but gives no rule for topics with no effective date in the record (for example the EV charging and heat pump rules). I used the decision date and labelled it as such.
