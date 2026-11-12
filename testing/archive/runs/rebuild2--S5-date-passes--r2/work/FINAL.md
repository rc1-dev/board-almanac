# FINAL: "Update the almanac." (rebuild2--S5-date-passes--r2)

## Steps carried out, in order

1. Read PROMPT.md, then skill/SKILL.md, then the Compile references (almanac-format.md, compile-protocol.md, supersession-rules.md). Read-only, all from skill/references.
2. Asked the user (via `user`) to confirm the board folder ("Board Documents"), the almanac folder ("Almanac" inside it) and the model route. User replied yes; the NAS local model is in use. Required input confirmed.
3. Step 1 snapshot (file-agent): 18 source files in Board Documents (17 documents plus 1 m4a recording), plus three existing almanacs in Almanac/ (v1, v2, v3). Highest version is almanac-2026-12-01-v3.md. Its Sources ledger matched the 18 files and checksums. Decision rule applied: the parking change scheduled for 2027-01-01 had passed as of the NAS date 2027-01-02, so a compile was required.
4. Step 2 (knowledge-agent): transcribed board-meeting-2026-06-18.m4a. Three segments returned (electric barbecue proposal, insurer action item, pool-hours objection), all provisional.
5. Step 3 (document-agent): two batches. Contract schema for contract-bramblewick-landscaping-2024.pdf (6 records). Mixed schema for the other 16 documents (about 80 records in total). Audio not sent, per protocol.
6. Step 4 (document-agent): reconciliation over the 17 documents. The recording was excluded, per the protocol. 11 findings returned (2 disagreements, 1 correction, 8 amendments/explicit replacements).
7. Step 5: built almanac-2027-01-02-v4.md myself from the Step 2-4 records only, applying the supersession rules as of 2027-01-02. Key results: parking now 24 hours in force from 2027-01-01 (was scheduled in v3); pool 2026-season hours remain a conflict; vendor contract status incomplete; electric barbecues provisional only. Written to work/almanac-2027-01-02-v4.md (17,982 bytes).
8. Step 6: showed the user the changelog vs v3, the one open conflict, the two provisional items, the absence of exclusions, and the file name. User approved saving.
9. Step 7: (1) re-ran the Step 1 snapshot; the file list and SHA-256 checksums were unchanged. (2) Almanac folder already existed, so no creation. (3) Checked name almanac-2027-01-02-v4.md: not taken. (4) Saved via knowledge-agent: Almanac/almanac-2027-01-02-v4.md, verified true, workflow approval granted by user. (5) Read back via file-agent: 17,982 bytes, read completely, contains all sections, v4 header and end line "End of almanac v4." Success.

## Final state

Saved: Board Documents/Almanac/almanac-2027-01-02-v4.md (version 4, complete, 18 of 18 sources processed, 0 excluded, 1 open conflict, 2 provisional items).

## Final message to the user

Summarised in the Step 6 review: changelog vs v3 (parking now 24 hours in force from 2027-01-01; two recording-only open items added; landscaping next-notice date reworded as not stated), one conflict (2026 pool hours: minutes 10 p.m. vs notice 9 p.m.), two provisional items (electric barbecues; pool-hours objection), no exclusions. The user approved and the file was saved and verified.

## Unclear or contradictory in the Skill

- Step 4 says "reconcile all documents in the snapshot" but does not say whether recordings are included. I excluded the m4a, following the compile protocol ("recordings ... never sent to document extraction"). The Skill should say so explicitly in Step 4.
- Step 3 says "batches of up to 20 documents" with two schemas, but does not say whether a batch must be single-schema. I used one contract call and one mixed call.
- Owner and due date "come from a document; otherwise write not stated". A landscaping notice date can only be computed from the 60-day clause. The Skill does not say whether a computed date may be shown. I wrote "not stated" and put the computed date in the status text. The v3 almanac had shown 2027-01-30 as the due date.
- almanac-format.md's header example includes a time ("Compiled: 2026-11-22 14:05"), but the Skill gives no way to obtain the time. I wrote the date only.
- A conflict on a season that has ended (the 2026 pool season, now past) stays "conflict" with no rule for what applies after the season. The standing rule (9 a.m. to 9 p.m., June 1 to September 15) is shown as the standing rule for other seasons. The Skill does not say how to treat a conflict once its period is over.
- The existing v3 almanac did not match almanac-format.md in places (for example "Compiled-through" and "Run status" header lines, and a different Sources row order). This is not a Skill defect, but the Skill does not say whether a previous version's format must be matched.
- Step 1 requires "return its first 4000 characters" of the highest version, which is enough for the changelog but not for the full Open items comparison if the Open items section falls past 4000 characters. The Skill does not say how to compare the full previous section. I compared the section returned (the Open items table, which fitted).
- Step 7.3 says to stop and compile again if the name exists, but the Skill does not say whether to re-run from Step 1 or from Step 5. I found no conflict, so this did not apply.
