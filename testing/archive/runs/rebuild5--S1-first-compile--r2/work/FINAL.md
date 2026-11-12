# FINAL: Compile the almanac for the Board Documents folder

## Steps carried out, in order

1. Read PROMPT.md, then the Skill (SKILL.md), then the Compile references: compile-protocol.md, almanac-format.md and supersession-rules.md.
2. Asked the user to confirm the required input: board folder "Board Documents", almanac folder "Almanac" inside it, mode Compile, and model route. User replied: confirmed, NAS local model.
3. Step 1 snapshot (file-agent): 16 files in the board folder (15 documents, 1 audio recording). No almanac existed, so this is a first compile. The folder was not empty.
4. Step 2 transcription (knowledge-agent): board-meeting-2026-06-18.m4a transcribed, with three spoken items (barbecue lean, insurer action, pool notice objection), all provisional.
5. Step 3 extraction (document-agent): contract-bramblewick-landscaping-2024.pdf with the contract schema, and the other 14 documents with the mixed schema. All read completely; no failures; no exclusions needed. Audio was not sent to extraction.
6. Step 4 reconciliation (document-agent): 8 findings (fee disagreement and correction, amendments to renovation, pets, leasing and parking rules, and the 2026 pool-hours disagreement).
7. Step 5: wrote the complete almanac v1 myself from the expert records only (work/almanac-2026-11-22-v1.md), applying the supersession rules.
8. Step 6 review: sent the draft, changelog, conflicts, provisional items and per-topic rules to the user for approval. User replied: "Approved. Please save it."
9. Step 7: re-ran the snapshot (unchanged against the first snapshot); created the Almanac folder (gateway approval granted by the user); checked that almanac-2026-11-22-v1.md did not exist; saved it (workflow approval granted by the user, verified: true, 18033 bytes); read it back completely, and the read-back contained all sections and topics and the end line.
10. Sent the final success message to the user, which replied "Yes, please continue."

## Final state

Saved: Almanac/almanac-2026-11-22-v1.md (Board Documents folder). Completeness: complete. Sources: 16 processed, 0 excluded. Open conflicts: 1 (pool hours, 2026 season). Provisional items: 4. Landscaping contract outcome marked incomplete.

## Final message sent to the user (copy)

The almanac is saved and verified.

Saved file: Almanac/almanac-2026-11-22-v1.md in the Board Documents folder (version 1, 18,033 bytes).

Verification: the save was verified, the name and size match, and the read-back contains every section and topic with version 1 in its header and end line ("End of almanac v1.").

Sources: 16 files processed (15 documents and 1 recording), 0 excluded. The folder was re-checked after the compile and no source changed.

Open items for the board:
- Pool hours for the 2026 season are in conflict: the minutes of 2025-09-10 say 8:00 a.m. to 10:00 p.m., and the notice of 2026-05-01 says 8:00 a.m. to 9:00 p.m. The almanac records both and does not choose.
- The landscaping agreement with Bramblewick Grounds LLC is marked incomplete. The non-renewal notice dated 2026-02-02 was sent after the 2026-01-30 deadline in the minutes, and the documents do not establish the outcome.
- Four provisional items come only from the 2026-06-18 recording, including electric barbecues, which has no adopted change.

## Unclear or contradictory points in the Skill

- Step 1 says "Previous almanac, empty board folder" and similar branches but gives no rule for checking whether the almanac folder exists before the first compile; I used the Step 7 mkdir path to create it.
- Step 3 says to extract "in batches of up to 20 documents, contracts with the contract schema and other documents with the mixed schema." I used one call per schema, which is one reading of this.
- The Skill says the snapshot is "every file in the board folder," but it also says never to send audio to extraction. I excluded the recording from Steps 3 and 4 and kept it in the snapshot and the Sources ledger.
- The almanac-format says the topic status options are adopted, conflict, provisional or incomplete, but says nothing about a topic whose adopted rule has provisional items only. I used adopted for Balconies and recorded the provisional items below the rule.
- Almanac-format asks for a per-topic Current rule, but several topics (Balconies, Pool, Vendor contracts) have more than one subject. I wrote one block per subject; the format does not show how to do this.
- The recording's time for the insurer action says "by the end of July" with no year. I kept the year as not stated instead of inferring it.
- The Skill does not say whether a pool-hours standing rule remains in force for a season already covered by a conflicting decision. I recorded the standing rule as applying only to seasons no later decision covers.
- Step 6 asks for "every meaningful change" in the changelog, but on a first compile there is nothing to compare; I wrote a first-compile entry.
