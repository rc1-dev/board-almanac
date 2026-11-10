# Compile protocol

This reference explains the compile steps in [SKILL.md](../SKILL.md) in more detail. It adds no new NAS actions.

## Why compile instead of searching every time

A board folder is small in bytes but large in history: one rule may be set in the 2019 bylaws, changed in 2024 minutes, announced with a typo in a 2025 notice, and corrected again in 2025. A search over raw files returns all four statements and leaves the reader, or a small local model, to work out which one is current. Compiling does that work once, carefully, when a file arrives, and stores the result with its evidence. Later questions read a short, reconciled file instead of the whole folder.

## Incremental compile

The Sources ledger in the newest almanac records every processed file with its checksum and modification time. On the next run:

| Inventory result | Action |
|---|---|
| File not in the ledger | New: extract and reconcile |
| Same path, different checksum | Changed: extract again, then reconcile; treat the old claims from this file as replaced by the new ones |
| Same path, same checksum | Unchanged: skip |
| In the ledger, not in the folder | Missing: keep its claims, mark the file `missing`, and list affected topics as `incomplete` in the changelog |

Only new and changed files are sent to extraction, so a routine update after one meeting processes one or two files.

## Batching

- Process at most 60 documents per run, the extraction limit used in Step 4.
- Process the oldest document date first, so that later decisions are compiled after the rules they replace.
- If documents remain, mark the run `partial`, list the remaining files as `pending`, and tell the user to run compile again.

## Claim fields

Each extracted claim must carry:

| Field | Meaning |
|---|---|
| Topic | One of the topics in [the almanac format](almanac-format.md) |
| Subject | The specific thing within the topic, for example "dog weight limit" within Pets |
| Value | The rule, amount, time range or date in plain words |
| Status | adopted, proposed, failed, provisional or informational |
| Document type | bylaws, minutes, notice, contract, agenda, newsletter, email, transcript or other |
| Document date | The date the document states, not the file date |
| Effective date | Only if the document states one |
| Vote | The recorded result, for example 3-0, if any |
| Quote | Short verbatim words that support the claim |
| Source | The file path |

A claim without a quote is not compiled. It is listed in the changelog as "unverified, not compiled" so that a person can check it.

## Recordings

Meeting recordings are transcribed by the knowledge expert. Claims from a transcript:

- are always `provisional`;
- become `adopted` only when written minutes adopted later state the same decision;
- are never used to supersede a rule from bylaws, minutes or a contract.

## Document types that never set a rule on their own

- **Agenda**: lists proposals. A proposal is compiled as `proposed`, and only the minutes record whether it passed.
- **Newsletter**: informational. It can trigger a conflict entry if it states a rule that disagrees with adopted documents, but it never supersedes one.
- **Email**: evidence of an action (for example, that a notice was sent on a date), not of a rule change.

## Building the new version

1. Start from the previous almanac text, or from an empty almanac on the first run.
2. For each claim, in document date order, apply [the supersession and conflict rules](supersession-rules.md).
3. Rebuild the At a glance table from the topic sections.
4. Update Open items: add new action items, and mark items done only when a document says they were done.
5. Update the Sources ledger and the header counts.
6. Write the changelog entry for this run.
7. Check the size limit in [the almanac format](almanac-format.md).

## What the compile must never do

- Invent a value, date, vote or quote that no expert returned.
- Resolve a conflict by choosing the more common value or the more plausible one.
- Rewrite or delete an older almanac version.
- Copy personal details of residents into the almanac.
