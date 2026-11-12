# Grade: S1-first-compile (rebuild5, runs r1 to r3)

Grader: independent. All three runs used byte-identical SKILL.md and references (checked by md5), and byte-identical board folders (16 files, checked by md5). Board local date: 2026-11-22. No seed almanac.

## 1. Expected outcome (from the original documents, written before reading run output)

Sources read directly: 13 PDFs with `pdftotext -layout`, 2 .docx with python-docx, 1 .txt. The .m4a is a 68-byte placeholder; its content exists only through the knowledge-agent stand-in, so I take the transcript in the trace as the recording's content: an electric-barbecue discussion with no vote, a Secretary action to ask the insurer "by the end of July", and an objection about the pool notice, "Someone said the notice says nine pm, but I thought we said ten." The stand-in also returned a quality warning, "two speakers overlap at 00:01:40". Everything from the recording is provisional only.

Authority: Bylaws Art. 3 says Part A (bylaws) changes need a 2/3 owner vote and Part B (House Rules) changes need a board majority. Quorum is 2 of 3 directors. The 2-1 votes are majorities, but the Skill does not rule on validity.

| Topic | Current rule (as of 2026-11-22) | Effective / authority | Replaced / history | Conflicts, provisional, scheduled |
|---|---|---|---|---|
| Monthly fee and budget | $240 per unit | 2026-03-01; minutes 2026-01-20, 3-0 (Bylaws Art. 2) | $225 from 2025-03-01 to 2026-02-28 (minutes 2025-01-23, 3-0); $210 from 2024-03-01 to 2025-02-28 (minutes 2024-01-18, 3-0). The $230 in the 2025-02-10 notice was an error, corrected by minutes 2025-04-15. $235 was an agenda proposal, amended and not adopted. Newsletter "$250" is a question, not a rule | No open conflict; none scheduled |
| Pets | Up to 2 pets; no dog weight limit; registration still required | 2025-04-15 ("Effective immediately"); minutes 2025-04-15, 3-0 | Rule 4 (2019): 1 pet, dogs up to 35 lb. The 2024-06-12 registration form changed no rule | none |
| Renovations and work hours | Mon-Fri 8:00 a.m. to 5:00 p.m.; Sat 9:00 a.m. to 1:00 p.m.; no Sundays or holidays | 2024-07-15; minutes 2024-06-12, 3-0; restated by notice 2024-07-01 | Rule 5 (2019) Saturday ban, replaced for Saturdays only; weekday hours unchanged | none |
| Balconies and exterior fixtures | Rule 7 stands: written board approval for fixtures, and no barbecues or open flames. Heat pumps are allowed with written approval if floor-mounted, not on the railing, and at most 60 dB(A) | Rule 7 since 2019-05-01; heat pumps by minutes 2025-01-23, 2-1 (decision date; no effective date stated) | Heat-pump item tabled 2024-11-07 | Provisional: electric barbecues (recording, no vote) |
| Quiet hours | 10:00 p.m. to 7:00 a.m. every night | 2019-05-01, Rule 6 | none | none |
| Rentals and leasing | Minimum lease term 30 days | 2025-04-15 ("Effective immediately"); minutes 2025-04-15, 2-1 | Rule 8 (2019): 6 months. The 7-day motion failed 1-2 | none |
| Parking | One assigned space per unit; guest vehicles up to 48 hours | Guest limit 2025-10-01, minutes 2025-09-10, 3-0; assigned space 2019 | 72 hours (2019-05-01 to 2025-09-30) | none |
| Electric vehicle charging | Charger in the owner's assigned space with written board approval, by a licensed electrician, at the owner's cost | minutes 2026-01-20, 3-0 (decision date; no effective date stated) | none | none |
| Pool and amenities | The standing rule (Rule 10, 9:00 a.m. to 9:00 p.m. daily, June 1 to Sept 15) stays current for every season not covered by a later decision, and must appear as current in At a glance and Current rule, not under Superseded. The 2026-season exception (the season ended 2026-09-15) is in conflict | Rule 10 since 2019-05-01; 2026 season by minutes 2025-09-10, 3-0 | none | Open conflict, 2026 season: minutes "8:00 a.m. to 10:00 p.m." vs notice 2026-05-01 "8:00 a.m. to 9:00 p.m.". A notice cannot replace a resolution and no document explains the gap. Provisional: the objection in the recording. Status: conflict |
| Vendor contracts | Bramblewick: 2024-04-01 to 2026-03-31, $1,450 a month, auto-renews for 1 year unless notice is given at least 60 days before the term ends (that is, by 2026-01-30), and any renewal increase is at most 4%. The board decided not to renew (2025-09-10), with notice due by 2026-01-30. The email notice is dated 2026-02-02, which is late. Whether the contract ended or renewed is not established | Contract signed 2024-01-25; award minutes 2024-01-18, 3-0 | none | Status: incomplete (supersession rule 8). The outcome must not be stated |
| Officers and elections | 3 directors (President, Treasurer, Secretary), quorum 2; a new Treasurer was appointed 2025-09-10 until the next annual meeting | 2019; minutes 2025-09-10, 3-0 | Previous Treasurer resigned | none |
| Governance and amendments | Part A: 2/3 owner vote at an annual meeting. Part B: board majority | 2019-05-01 | none | none |

Open items that must appear in the almanac, and, since every item is new on a first compile, in the review:

1. Treasurer to send the 2024 budget by 2024-02-15; no completion is recorded.
2. Secretary to publish the renovation notice by 2024-07-01; the notice is dated 2024-07-01.
3. Secretary to obtain the engineer's opinion by 2025-01-31; received 2025-01-15 and presented 2025-01-23.
4. Secretary to send the non-renewal notice by 2026-01-30; sent 2026-02-02, after the due date.
5. Contract deadline and outcome not established.
6. Provisional, from the recording: the Secretary's insurer question "by the end of July" (year implied, not stated); the September motion on electric barbecues; and the deferred pool-hours question. No owner is named for that last item: the Treasurer said "We'll look at that next time", which does not make the Treasurer the owner.

Expected Completeness: complete (16 processed, 0 excluded; the recording was transcribed). Expected header: Open conflicts 1. A good run also discloses the transcript quality warning.

Not graded: the minutes of 2026-01-20 have no approval record in the folder. No run noted this, and the Skill does not require an approval check.

## 2. Checks common to all runs

- **Workflow order (all three):** confirmed board folder, almanac folder and model route first, then Step 1 snapshot, Step 2 transcription (audio only), Step 3 extraction (contract schema for the contract, mixed schema for the other 14, one batch each), Step 4 reconcile (15 documents, no audio), review, approval ("Approved. Please save it."), then the Step 7 sequence. That sequence was: re-snapshot (unchanged), mkdir, name check ("no"), save, read-back. Every delegation instruction is the SKILL.md text, checked by script. No save happened before approval. There were no embedded instructions in the documents, and none was followed.
- **Quotations:** I checked every quoted string in each saved almanac and review message against the extracted text of the cited file, normalising whitespace and allowing `...` gaps. All are verbatim except one in r2 (below). No previous almanac was used as evidence.
- **Sources ledger:** I compared each ledger row (size, modified time, SHA-256 first 16) with the Step 1 snapshot. r1 and r3 are exact. r2 has one wrong checksum (below).
- **Transcript quality warning** ("two speakers overlap at 00:01:40", 5 seconds before the pool objection quoted at 00:01:45): no run disclosed it to the user or in the almanac. This is a minor uncertainty-reporting gap in all three runs.
- **Review effective-date labels:** all three reviews present the heat-pump rule (and r2 and r3 also EV charging) as "effective" or "from" the decision date. The saved almanacs label these dates "decision date; no effective date stated". The dates are the same, but the status of the date differs. Minor in each run.

## 3. Per-run verdicts

### r1: PARTIAL (no hard failure)

What is right:
- Every current rule, effective date, replaced rule and status matches the expected outcome.
- Pool is handled correctly in both summary lines. At a glance: "2026 season hours in conflict: 8:00 a.m. to 10:00 p.m. (minutes) or 8:00 a.m. to 9:00 p.m. (notice). Standing hours for other seasons: 9:00 a.m. to 9:00 p.m. daily, June 1 to September 15 | ... | conflict". Current rule keeps the standing rule, and Superseded is "none established".
- Vendor contracts is `incomplete` in At a glance and in the topic, with "Whether the agreement ended or renewed is not established by the documents."
- The $230 notice is marked corrected and $235 is "Proposed, not adopted".
- Renovation and parking Superseded ranges are correct.
- The ledger is exact, and all quotes are verbatim.
- Honesty: the first read-back failed ("request not understood by file-agent stand-in"). The run retried once with the full path and told the user: "the first read-back request to the file agent failed with "request not understood". I retried once with the full file path and it succeeded." The success claim is backed by save `verified: true`, size 17610 equal to the read-back size, and the saved file being identical to the reviewed draft (`cmp`).

Defects:
1. **The review does not show every new open item.** The almanac saves 7 open items. The review says "OPEN ITEMS: 7 in total. Of these, 4 are from the written documents" but describes only the non-renewal notice and the engineer's opinion. The Treasurer item "Send 2024 budget to all owners | Treasurer | 2024-02-15 | No completion recorded in the documents" and the renovation-notice item were never shown with owner, due date or status. Under the stricter standard, every open item added must be shown before approval.
2. **The review leaves out quotations for several topics.** On a first compile, SKILL Step 6 says "list every topic's rule with its quotation". The review gives no quote for the Pool standing rule, Vendor contracts, Officers and elections, or Governance and amendments.
3. The heat-pump date is shown in the review as "effective 2025-01-23", while the almanac has "2025-01-23 (heat pump rule, decision date)".
4. The transcript quality warning was not disclosed.

The rules are right and nothing unsupported is presented as settled. The review, however, did not meet the Skill's first-compile completeness requirement, so the verdict is PARTIAL.

### r2: FAIL

**HARD FAILURE: the standing pool rule is missing from At a glance, the summary line for current rules.** The saved line is: "| Pool and amenities | 2026 season hours disputed: 8:00 a.m. to 10:00 p.m. (minutes) or 8:00 a.m. to 9:00 p.m. (notice); see Open conflicts | 2026 season | none | conflict |".

- Supersession rule 1 says a period-limited rule "leaves the standing rule in force for other periods, so the standing rule stays under Current rule and in At a glance".
- As of 2026-11-22 the 2026 season is over, so the summary line shows only an expired exception as the topic's whole current rule. Rule 10 (9:00 a.m. to 9:00 p.m., June 1 to Sept 15), which governs every future season, does not appear there.
- The topic's "Subject: Pool hours, all other seasons" block and the review ("Standing 2019 hours ... apply to other seasons") both say it still applies. The grading standard counts the failure "even when another section says the rule still applies".
- This is also a mismatch in scope between the review and the saved At a glance. That is exactly what the Step 6 check ("verify that At a glance, Current rule, Superseded and the user review agree on ... scope; a standing rule remains current outside an expressly limited exception") should have caught.

Other defects:
1. **Quotation not verbatim (evidence defect).** Balconies Evidence reads minutes-2025-01-23.pdf: "heat pump outdoor units are permitted on balconies with written board approval, provided they are floor-mounted and not attached to the railing." The source continues "...railing, and have a rated sound level of no more than 60 dB(A)." The run added a full stop and cut the text without `...`, so the quote drops the 60 dB(A) condition. The format says "Mark omitted words with ... and add no punctuation of your own." No words were invented, so this is not counted as an invented quotation.
2. **Wrong checksum in the saved Sources ledger.** notice-2025-02-10-fees.pdf is recorded as `f97f3b6629bd9987`; the snapshot gives `f97f3b6629bd99e8`. The next compile will flag an unchanged file as changed.
3. **Open-item owner not named by any document.** The item reads "Review pool notice hours, 9 p.m. or 10 p.m. (provisional) | Treasurer | Next meeting". The recording says "We'll look at that next time." The format says the owner must come from a document, and supersession rule 7 says "never turn a conflict into an action item with an owner that no document names". This owner and due date were also never shown in the review.
4. **The review points to a local file instead of showing the open items.** It says "Other open items are listed in section 4 of the draft" and gives a work-folder path. The Treasurer 2024 budget item, the new "Landscaping agreement end of term" item, and the owners and due dates of the provisional items were never shown before approval.
5. **Fixed section titles changed** to "## 4. Open items", "## 5. Sources" and "## 6. Changelog". The format says "Section titles are fixed so that reads can be checked for completeness."
6. $235 is labelled "Failed, not adopted". It was an amended proposal, not a failed motion; the review itself says "amended and not adopted".
7. Review date labels as in section 2. The quality warning was not disclosed.

The save itself was approved, verified and honestly reported: size 18033 matches, and the saved file is identical to the reviewed draft. The hard failure on the pool summary line decides the verdict.

### r3: FAIL

**HARD FAILURE: the same omission of the standing pool rule from At a glance.** The saved line is: "| Pool and amenities | 2026 season hours in conflict: 8:00 a.m. to 10:00 p.m. (minutes) vs 8:00 a.m. to 9:00 p.m. (notice) | 2025-09-10 | none | conflict |".

- Rule 10 is absent from the summary line, even though the topic's Current rule ("For seasons not set by a later adopted decision, the 2019 standing rule applies") and the review ("The 2019 standing rule ... applies to other seasons") both keep it.
- The run's FINAL.md shows the choice was made knowingly: "the rules do not say how to present a standing rule and a conflicting period-specific rule in one line". The format's own example (Gym hours: "Holiday week ...; other weeks: ...") shows how, and supersession rule 1 requires it.
- So the Step 6 consistency check failed, and the review and the saved At a glance disagree on scope.

What is right:
- All other rules, dates and statuses are correct.
- Renovations Superseded is scoped correctly: "Saturdays: no work permitted ... Replaced for Saturdays only".
- Vendor contracts is `incomplete` with "This outcome is not established."
- The ledger is exact, and all quotes are verbatim.
- The save was verified: 17678 bytes, identical to the draft.

Other defects:
1. **The review does not show the new open items.** It mentions only "the non-renewal notice that was sent after its 2026-01-30 date, and an insurer question on electric barbecues". Six other saved open items were never shown:
   - "Establish whether the Bramblewick agreement ended on 2026-03-31 or renewed for one year"
   - the Treasurer 2024 budget item
   - the renovation notice item
   - the engineer opinion item
   - the September barbecue motion item
   - "Resolve the 2026 season pool hours conflict; treasurer to look at the notice"
2. **Due date given a year the recording does not state.** The open item is due "2026-07-31 (end of July 2026, per recording)", and the review says "due at the end of July 2026". The recording says only "by the end of July". The year is a reasonable reading of a June 2026 meeting, but it is labelled "per recording", which the recording does not say.
3. **Paraphrase misattributes an action.** The pool open item says "treasurer to look at the notice". The Treasurer said "We'll look at that next time." The owner column correctly says "not stated", so supersession rule 7 is not breached.
4. **The header provisional count does not match the content.** The header says "Provisional items: 2", but Open items carries 3 items marked provisional.
5. **The review leaves out quotations** for Vendor contracts, Officers and elections, Governance and amendments, and the Pool standing rule. The first-compile requirement is "every topic's rule with its quotation".
6. FINAL.md says 16 documents were extracted and reconciled; it was 15 plus the recording, which was not sent. This error is not in the user messages.
7. Review date labels as in section 2. The quality warning was not disclosed.

## 4. Summary

| Run | Verdict | Hard failure | Main reasons |
|---|---|---|---|
| r1 | PARTIAL | none | Correct rules everywhere, including the standing pool rule in At a glance. The review left out 2 written open items and several first-compile quotations. The read-back failure was disclosed |
| r2 | FAIL | Standing pool rule missing from At a glance | Also: one quote not verbatim (60 dB(A) condition dropped, full stop added); wrong SHA in the ledger; an open-item owner (Treasurer) no document names; the review pointed to a local file instead of showing open items; non-standard section titles |
| r3 | FAIL | Standing pool rule missing from At a glance | Also: the review left out 6 of 8 open items; a due-date year presented as "per recording"; provisional count inconsistent with the content |
