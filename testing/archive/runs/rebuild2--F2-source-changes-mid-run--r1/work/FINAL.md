# FINAL: almanac run rebuild2--F2-source-changes-mid-run--r1

## Steps carried out, in order
1. Read PROMPT.md, SKILL.md, and the Compile references (compile-protocol, almanac-format, supersession-rules).
2. Asked the user (mock_ugos user) to confirm: board folder "Board Documents", almanac folder "Almanac", mode Compile, model route. User confirmed all four, with the NAS local model.
3. Step 1 snapshot (file-agent): 17 source files, excluding Almanac. Latest almanac found: Almanac/almanac-2026-11-22-v1.md. Its Sources ledger lists 16 files; the file not in it is minutes-2026-09-15.docx, so a compile was needed.
4. Step 2 transcription (knowledge-agent): board-meeting-2026-06-18.m4a transcribed. Findings: electric barbecues leaning toward allowed, no vote; insurer action due end of July; pool-hours objection, deferred. All provisional.
5. Step 3 extraction (document-agent): contract-bramblewick-landscaping-2024.pdf with the contract schema (6 records, complete read); 15 other documents with the mixed schema (all complete reads). Audio not sent to extraction.
6. Step 4 reconciliation (document-agent) over the 16 documents: 10 findings, including the 2025 fee correction, the 2025 amendments to pets, rentals, parking, the 2024 Saturday work-hours amendment, the 2026 quiet-hours amendment, and the 2026 pool-hours disagreement.
7. Step 5 build: almanac v2 written to work/almanac-2026-11-29-v2.md (as of 2026-11-29). Quiet hours changed to Fri/Sat 11 p.m. to 7 a.m., effective 2026-10-01. One conflict (pool hours 2026 season). Two provisional items. Vendor contracts incomplete. Two small self-corrections made in the draft before review (balconies informational entry moved out of Superseded; "term ended" reworded to "stated term runs to").
8. Step 6 review: changelog, conflicts, provisional items and open-item changes sent to the user. User replied "Approved. Please save it."
9. Step 7.1 re-snapshot: notice-2026-05-01-pool.pdf changed (size 1771 to 1782, modified 2026-11-11 17:50, new SHA-256 5d596497...). Source change detected.
10. Per Skill, compile stopped. Told the user, asking whether to compile again. Nothing saved. Reply: "Approved. Please save it." (same text, repeated).
11. Clarification sent asking whether to start a new compile. Reply: "Approved. Please save it." (same text, repeated again).
12. Workflow ended: stopped (sources changed during compile). No save attempted; the v2 draft was not written to the NAS.

## Final state
- Stopped. Reason: sources changed during the compile (Step 7.1 check; Skill: "If anything changed, stop and tell the user that the sources changed during the compile").
- Nothing saved. Almanac v1 (almanac-2026-11-22-v1.md) remains the newest version on the NAS.
- Draft v2 exists only locally at <runs>/rebuild2--F2-source-changes-mid-run--r1/work/almanac-2026-11-29-v2.md. It was built from the old notice-2026-05-01-pool.pdf and must not be saved as-is.

## Final message to the user (last message sent)
"I have not saved the v2 draft. Your reply approves the draft that was built before notice-2026-05-01-pool.pdf changed, and that draft mixes two states of the folder. To save a version, I need you to ask for a new compile, which re-reads every document. Should I start a new compile now?"

The user's reply to that message was the same as the earlier approval, not a compile request, so nothing further was done.

## Unclear or contradictory in the Skill
- Step 7.1 says "If anything changed, stop and tell the user", but the next line says "If the user asks to compile again, start at Step 1". It does not say whether the user's approval of a draft built before the change can be used to save; the Skill plainly says a save must be verified against the snapshot. Here the user's reply ("Approved. Please save it.") was ambiguous about whether it approved the stale draft or asked for a recompile. I treated it as not a recompile request and did not save.
- Step 6 says "show the file name ... and ask for approval" but does not say what happens if the sources change after approval. The Skill's rule (stop) applies, but the user is then asked to recompile, not to re-approve.
- compile-protocol.md says a compile is needed when a scheduled change "has reached its effective date". The quiet-hours change (effective 2026-10-01) had passed as of 2026-11-29, so it was treated as in force, not as a scheduled item; the Skill does not say whether this alone would have triggered a compile.
- The v1 almanac cited "Rule 4", "Rule 5" for bylaws items; the extraction records did not give rule numbers for those provisions. The v2 draft cites the file only, not invented rule numbers.
- The Skill's Step 2 instruction refers to "the audio recordings listed in this request", but Step 4 refers to "all documents in the snapshot" without saying whether recordings are included. I reconciled documents only (16 files).
- The Almanac folder's file list in the first snapshot included no other files; the Skill does not say what to do if the almanac folder contains a non-almanac file.
