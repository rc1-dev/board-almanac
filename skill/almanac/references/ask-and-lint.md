# Ask, lint and status

## Answer format for ask

Every answer from the almanac has these parts, in this order:

1. **Answer**: the currently documented rule in one or two sentences. It reports what the documents record, not legal advice.
2. **Since and source**: the effective date and the document that set it, with the vote if recorded.
3. **History**: earlier rules for the same subject, only if they help, for example "Before Apr 15, 2025: one pet per unit."
4. **Open conflicts or provisional items** on the same topic, quoted. If the documents disagree, say so first and give both statements instead of a single answer.
5. **Almanac version**: for example "From almanac v7, compiled through Sep 15, 2026."

Example:

```text
Yes. You can install a heat pump outdoor unit on your balcony with written board approval.
It must be floor-mounted, not on the railing, and rated at 60 dB or less.
Set by board minutes of Jan 23, 2025, motion carried 2-1, replacing the 2019 rule that
banned all exterior fixtures without approval.
From almanac v7, compiled through Sep 15, 2026.
```

## When the almanac does not cover the question

Say "The almanac does not cover this." Do not answer from general knowledge. Offer:

- to compile, if files have changed since the last version; or
- to search the raw board folder with the document expert, only if the user asks, and label that answer "uncompiled and unverified".

## Freshness warning

Count the board files that are not in the almanac's Sources ledger or whose size or modification time differs from it, and the ledger files that are no longer in the folder. If the count is above zero, add: "N board files are new, changed or missing since this almanac was compiled. The answer may be out of date. Say compile to update it." This is a quick check that compares size and modification time, not content, so a file changed without any change to either would not be counted. A compile confirms every change by checksum, and the user can ask for that definitive check at any time.

## Scheduled changes

Before answering, compare today's date with every scheduled effective date in the At a glance table. If a scheduled change has taken effect since the compile, it is the current rule: answer with it, cite the decision that adopted it, and say that the almanac was compiled before it took effect. For a question about a particular date, answer from the effective dates and history recorded for that topic as of that date. Dates use the board's local calendar.

## Exclusions

If the almanac was compiled with exclusions, say so in every answer and name the excluded files. Never state that no rule or no conflict exists on a topic, because an excluded file may contain one.

## Coverage

Ask the document expert to read the whole almanac, not a preview, and to say whether it did. If it did not, read the file completely and answer from the topic's own section.

## Lint checks

Lint reads the newest almanac and the inventory of changed files. It reports, in this order:

1. **Scheduled changes now in force**: adopted changes whose effective date has passed since the compile.
2. **Open conflicts**, with both quotes.
3. **Provisional items** that no adopted minutes confirm yet.
4. **Overdue action items**: due date passed and no document shows them done.
5. **Late actions**: done after their due date, for example a contract notice sent after the notice deadline.
6. **Coming effective dates** within 90 days.
7. **Contract deadlines** within 90 days, such as renewal notice periods.
8. **Files changed since the last compile**, by count and name.
9. **Exclusions**: files excluded from the compile, and the reminder that they may affect any topic.

If every check is empty, report "Lint found no issues" with the almanac version.

## Status

Report the newest almanac file name, version, compiled time, compiled-through time, source count, open conflicts, provisional items and the number of board files changed since.
