# Almanac format

An almanac is one Markdown file per compile run, saved as `almanac-YYYY-MM-DD-vN.md` in the almanac folder. Older versions are never changed, so the folder is also the history.

Keep the whole file under 60,000 characters so the local model can read it in a few parts. If it would be longer, shorten quotes to the decisive words and move superseded entries older than five years to a single line each.

## Section order

The file has exactly these sections, in this order. Section titles are fixed so that later runs can find them.

### 1. Header

The first lines of the file:

```text
# Almanac: Harbor View Condominium Association
Version: 7
Compiled: 2026-11-22 14:05
Compiled-through: 2026-09-15 18:40
Board folder: Board Documents
Sources: 18 processed, 0 failed, 0 pending
Open conflicts: 1
Provisional items: 1
Run status: complete
Model route: NAS local model
```

`Run status` is `complete` or `partial`. A partial run lists the number of files still pending in `Sources`.

### 2. At a glance

One line per topic, current value only, so that a reader or the local model can decide quickly where to look.

```text
| Topic | Current rule | Since | Status |
|---|---|---|---|
| Monthly fee | EUR 240 per unit | 2026-03-01 | adopted |
| Pets | Up to 2 per unit, registration required, no weight limit | 2025-04-15 | adopted |
| Pool hours | 08:00 to 22:00 or 08:00 to 21:00 | 2026 season | conflict |
```

Status is one of `adopted`, `conflict`, `provisional` or `incomplete`.

### 3. Topics

One subsection per topic, using the topic list below. Each topic has these parts:

```text
## Pets

Current rule: Up to 2 pets per unit. Registration with management is required. No weight limit.
Effective: 2025-04-15
Set by: Board meeting minutes, 2025-04-15, motion carried 3-0
Evidence: minutes-2025-04-15.docx: "maximum of two (2) pets per unit ... the 15 kg limit for dogs is removed"

Superseded:
- 2019-05-01 to 2025-04-15: One pet per unit, dogs up to 15 kg. Source: bylaws-house-rules-2019.pdf: "one (1) pet per unit"

Open conflicts: none
Provisional: none
```

Rules for the parts:

- **Current rule** states the rule in plain words. If the topic is in conflict, state both values and say that the documents disagree.
- **Effective** is the effective date if a document states one, otherwise the decision date, labelled as such.
- **Set by** names the document type, its date and the vote if one is recorded. People are named by board role only.
- **Evidence** gives the file name and a verbatim quote of the decisive words.
- **Superseded** lists earlier rules for the same subject, newest first, each with its date range and source.
- **Open conflicts** lists disagreements that no document resolves, with both quotes.
- **Provisional** lists items that come only from a recording, an agenda or an email and are not confirmed by adopted minutes.

### 4. Open items

Action items with owner role, due date, status and source, and contract deadlines such as notice periods.

```text
| Item | Owner | Due | Status | Source |
|---|---|---|---|---|
| Send non-renewal notice to landscaping contractor | Secretary | 2026-01-30 | Sent 2026-02-02, after the due date | minutes-2025-09-10.pdf; email-2026-02-02-landscaping.txt |
```

### 5. Sources

The ledger that makes incremental compiles possible. One row per file in the board folder.

```text
| File | Type | Document date | Modified | SHA-256 (first 16) | Status |
|---|---|---|---|---|---|
| minutes-2025-04-15.docx | minutes | 2025-04-15 | 2025-04-20 09:12 | 3f9c0a17b2d4e8c1 | processed |
```

Status is `processed`, `failed`, `pending` (not yet processed in a partial run) or `missing` (in the previous ledger but no longer in the folder).

### 6. Changelog

Newest first. Each entry lists what this run added, changed, superseded, marked as conflict, marked as provisional or left incomplete, and which files it processed.

```text
## v7, 2026-11-22
- Processed 1 new file: minutes-2026-09-15.docx
- Changed: Quiet hours. Friday and Saturday nights now 23:00 to 07:00; other nights unchanged at 22:00 to 07:00.
- No new conflicts.
```

## Topic list for boards

Use these topic names when they fit, and add a new topic only when no existing one fits:

Monthly fee and budget; Special assessments; Pets; Renovations and work hours; Balconies and exterior fixtures; Quiet hours; Rentals and leasing; Parking; Electric vehicle charging; Pool and amenities; Waste and recycling; Insurance; Vendor contracts; Officers and elections; Governance and amendments.
