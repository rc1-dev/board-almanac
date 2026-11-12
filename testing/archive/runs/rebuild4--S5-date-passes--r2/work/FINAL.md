# FINAL: "Update the almanac" (Compile mode)

## Steps carried out, in order

1. Confirmed inputs with the user: board folder "Board Documents", almanac folder "Almanac" inside it, NAS local model. User confirmed.
2. Read SKILL.md, then the Compile references: compile-protocol.md, almanac-format.md, supersession-rules.md.
3. Step 1 snapshot (file-agent, read only): 18 files in Board Documents (17 documents and 1 recording), excluding the Almanac folder. Found almanac-2026-11-22-v1.md, almanac-2026-11-29-v2.md and almanac-2026-12-01-v3.md; highest version is v3. Compared the snapshot with v3's Sources ledger: same 18 files, same checksums. Nothing new, changed or missing.
4. Freshness decision: no file changed, but v3 has a scheduled change (Parking: up to 24 hours from 2027-01-01) and the NAS date is 2027-01-02, so the scheduled date has passed. Per the Skill, the almanac is not current and a compile was needed.
5. Step 2 (knowledge-agent): transcribed board-meeting-2026-06-18.m4a. Results: a proposal to allow electric barbecues with no vote; an action item for the Secretary to ask the insurer by end of July; an objection that the pool notice says 9 p.m. rather than 10 p.m., deferred.
6. Step 3 (document-agent): contract schema for contract-bramblewick-landscaping-2024.pdf (6 records, read completely); mixed schema for the other 16 documents (all read completely; records per file reported). Audio was not sent.
7. Step 4 (document-agent): reconciliation over the 17 documents (audio excluded). Returned 11 findings: fee disagreement and correction ($225 vs $230, resolved by the 2025-04-15 minutes); $235 proposal amended; renovation Saturday hours amendment; pets amendment; rentals amendment; parking amendments (72, 48, then 24 hours); pool-hours disagreement (2026 minutes 10 p.m. vs 2026 notice 9 p.m.); quiet-hours amendment.
8. Step 5: wrote the v4 almanac from the records of Steps 2 to 4 (work/almanac-2027-01-02-v4.md). Applied supersession rules as of 2027-01-02. Pool-hours 2026 season kept as conflict. Vendor contracts kept incomplete. Parking now current. Changelog compared with v3.
9. Step 6: showed the user the changelog, the single conflict, the provisional items, the exclusions (none) and the incomplete topic, and asked for approval. User approved.
10. Step 7: (a) re-ran the Step 1 snapshot; all 18 files matched in size, modification time and SHA-256 prefix; (b) Almanac folder already exists, so no creation; (c) checked that almanac-2027-01-02-v4.md does not exist: "no"; (d) knowledge-agent saved Almanac/almanac-2027-01-02-v4.md, verified true, 16,611 bytes; (e) file-agent read it back completely in parts: 16,611 bytes, all sections and the end line present.
11. Sent the user the save confirmation. The user replied "Yes, please continue."

## Final state

- Saved: Almanac/almanac-2027-01-02-v4.md (version 4, complete, 18 sources, 0 excluded).
- Open conflicts: 1 (2026 season pool hours).
- Provisional items: 2 (electric barbecues proposal; pool-hours objection). The insurer action item is listed under Open items as provisional.
- Incomplete: Vendor contracts (landscaping). Renewal or end not established; the notice was sent 2026-02-02, after the 2026-01-30 deadline.

## Final message given to the user

Approval request listing the changelog (Parking changed from scheduled to current; provisional items 1 to 2; no open items added, closed or dropped), the single conflict, provisional items, no exclusions, and the incomplete landscaping topic. Then, after approval: "Saved and verified: Almanac/almanac-2027-01-02-v4.md (16,611 bytes, read back completely; all sections and the end line "End of almanac v4." present). ..." (summary as above).

## Unclear or contradictory points in the Skill

- Step 4 says "Reconcile all documents in the snapshot" but Step 3 says never send audio. I sent only the 17 documents to reconciliation and excluded the recording. The Skill does not say which applies to Step 4.
- The Compile header format requires "Compiled: YYYY-MM-DD HH:MM", but the request gives no clock time. I wrote the date with "(time not recorded)".
- The almanac folder is named "the almanac folder the user confirmed", but the delegate command has no option for it. The file-agent resolved "Almanac" from the board folder context. The expert was not given an explicit path for it.
- The Skill says a compile is needed when a scheduled date has passed, but the Step 1 rule says "report that the almanac is current" when no file has changed and no scheduled date has passed. Both rules were applied; the scheduled date had passed, so the compile went ahead.
- Owner and due date must come from a document, otherwise "not stated". The next landscaping notice date (2027-01-30) is derived from the 60-day clause and is not stated in any document. I labelled it as derived.
- The 2019 bylaws give pool hours for the June 1 to September 15 season. It is not explicit whether the 2026 season minutes override those hours or sit alongside them. I kept only the 2026 season as a conflict and left other seasons under the 2019 rule.
- For the heat pump rule, the decision date and effective date are not distinguished. I recorded the decision date and labelled it as such.
- Step 7 verification compares size and modification time, plus SHA-256 prefix for the snapshot recheck. The Skill's own note says byte-level comparison is not possible in this interface.
- The NAS date (2027-01-02) differs from the UTC date in the system prompt (2026-11-11). I used the NAS date, as the test rules instruct.
