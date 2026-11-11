# Almanac format

An almanac is one Markdown file per compile, rebuilt from the original documents and saved as `almanac-YYYY-MM-DD-vN.md` in the almanac folder. Older versions are never changed, so the folder is also the history.

Keep the whole file under 60,000 characters so it can be read completely in parts of 4,000 characters. If it would be longer, shorten quotes to the decisive words. Keep topics in the order of the topic list below and use the same field names in every version, so that versions can be compared field by field.

## Section order

The file has exactly these sections, in this order, followed by an end line. Section titles are fixed so that reads can be checked for completeness.

### 1. Header

The first lines of the file:

```text
# Almanac: Harbor View Condominium Association
Version: 7
Compiled: 2026-11-22 14:05
As of: 2026-11-22 (board local date)
Board folder: Board Documents
Sources: 18 processed, 0 excluded
Completeness: complete
Open conflicts: 1
Provisional items: 1
Model route: NAS local model
```

`Completeness` is `complete` when every file in the snapshot was processed, or `compiled with exclusions` when the user excluded files that could not be read. An almanac compiled with exclusions says in its header that the excluded files may contain decisions on any topic, and its answers never treat the absence of a rule or conflict as established.

### 2. At a glance

One line per topic, with the current value and any adopted change that has not yet taken effect, so that a reader or the local model can decide quickly where to look and whether the calendar has moved past a scheduled change.

```text
| Topic | Current rule | Since | Scheduled | Status |
|---|---|---|---|---|
| Monthly fee | $240 per unit | 2026-03-01 | none | adopted |
| Parking | Guest parking up to 48 hours | 2025-10-01 | Up to 24 hours from 2027-01-01 | adopted |
| Pool hours | 2026 season: 8:00 a.m. to 10:00 p.m. or 8:00 a.m. to 9:00 p.m.; other seasons: 9:00 a.m. to 9:00 p.m. | 2026 season; 2019-05-01 | none | conflict |
```

Status is one of `adopted`, `conflict`, `provisional` or `incomplete`. Scheduled shows an adopted change with its effective date, or `none`. A line never says more than its topic: if the topic says an outcome is not established, so does the line. A topic that no document mentions is left out.

### 3. Topics

One subsection per topic, using the topic list below. Each topic has these parts:

```text
## Pets

Current rule: Up to 2 pets per unit. Registration with management is required. No weight limit.
Effective: 2025-04-15
Set by: Board meeting minutes, 2025-04-15, motion carried 3-0
Evidence: minutes-2025-04-15.docx: "maximum of two (2) pets per unit ... the 35-pound limit for dogs is removed"

Superseded:
- 2019-05-01 to 2025-04-15: One pet per unit, dogs up to 35 lb. Source: bylaws-house-rules-2019.pdf: "one (1) pet per unit"

Scheduled: none
Open conflicts: none
Provisional: none
```

Rules for the parts:

- **Current rule** states the currently documented rule in plain words: what the adopted documents record, not a ruling on legal validity. If the topic is in conflict, state both values and say that the documents disagree.
- **Effective** is the effective date the extracted record gives, even if its quote does not show it; otherwise the decision date, labelled as such.
- **Set by** names the document type, its date and the vote if one is recorded. People are named by board role only.
- **Evidence** gives the file's path relative to the board folder and a verbatim quote of the decisive words. Mark omitted words with ... and add no punctuation of your own. Paths, not bare file names, keep two files with the same name in different subfolders apart.
- **Superseded** lists earlier rules for the same subject, newest first, each with its date range and source.
- **Scheduled** lists adopted changes whose effective date is after the board's local date at compile time, each with the date, the decision that set it and a quote. The current rule stays in force until that date. Ask and Lint compare the date with today, and a compile runs again once it has passed.
- **Open conflicts** lists disagreements that no document resolves, with both quotes.
- **Provisional** lists items that come only from a recording, an agenda or an email and are not confirmed by adopted minutes.

### 4. Open items

Action items with owner role, due date, status and source, and contract deadlines such as notice periods. Owner and due date come from a document; otherwise write `not stated`.

```text
| Item | Owner | Due | Status | Source |
|---|---|---|---|---|
| Send non-renewal notice to landscaping contractor | Secretary | 2026-01-30 | Sent 2026-02-02, after the due date | minutes-2025-09-10.pdf; email-2026-02-02-landscaping.txt |
```

### 5. Sources

The snapshot this version was built from: one row per file in the board folder, with its path relative to the board folder. The next compile compares it with the folder to decide whether anything changed.

```text
| File | Type | Document date | Size | Modified | SHA-256 (first 16) | Status |
|---|---|---|---|---|---|---|
| minutes-2025-04-15.docx | minutes | 2025-04-15 | 36846 | 2025-04-20 09:12 | 3f9c0a17b2d4e8c1 | processed |
```

Status is `processed`, or `excluded` with the reason and the note that the user approved the exclusion.

### 6. Changelog

Newest first. Each entry compares this version with the previous one, topic by topic, on rule, scope, effective date, authority and status, and lists every open item added, closed or dropped. Any difference in meaning is a change; only a difference in wording is not. The comparison is proposed for the user to review before saving.

```text
## v7, 2026-11-22
- Rebuilt from 18 files. New since v6: minutes-2026-09-15.docx.
- Changed: Quiet hours. Friday and Saturday nights now 11:00 p.m. to 7:00 a.m.; other nights unchanged at 10:00 p.m. to 7:00 a.m.
- No new conflicts. No exclusions.
```

### End line

The last line of the file is always:

```text
End of almanac v7.
```

with the version number. A read that does not reach this line is incomplete.
## Topic list for boards

Use these topic names when they fit, and add a new topic only when no existing one fits:

Monthly fee and budget; Special assessments; Pets; Renovations and work hours; Balconies and exterior fixtures; Quiet hours; Rentals and leasing; Parking; Electric vehicle charging; Pool and amenities; Waste and recycling; Insurance; Vendor contracts; Officers and elections; Governance and amendments.
