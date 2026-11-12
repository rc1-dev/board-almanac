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
| Same path, same checksum, ledger status `processed` | Unchanged: skip |
| Same path, same checksum, ledger status `pending`, `failed` or `partial` | Process again: an unfinished or failed run never leaves a file behind |
| Ledger status `missing`, file is back in the folder | Process again, as for a changed file |
| In the ledger, not in the folder | Missing: mark the file `missing`; rebuild every record that cited it from the surviving evidence, keeping its claims only as history marked source missing |

Only files that need processing are sent to extraction. A routine update after one meeting extracts claims from one or two new files; the unchanged documents that those decisions amend are read again during reconciliation, and every other topic is carried forward.

## Evidence dependencies

The records to rebuild are the union of two sets: records that cite a changed or missing file, and records whose subject and scope overlap a claim from a new or changed document or recording. Unchanged sources alone never mean a record is current, because a new amendment can change a topic whose earlier sources are untouched.

Every topic and every open item depends on the files it cites. When a file changes or goes missing, every record that cites it is rebuilt from the original evidence that remains, even if the new extraction returns nothing for it. The previous almanac shows which files to look at; those surviving files are extracted again for the affected records, because the almanac itself is never evidence. A claim that a corrected document no longer contains is dropped. If no remaining source supports a rule, the topic is marked `incomplete` and the changelog says why, so an obsolete rule is never kept as current. Only topics whose cited sources are all unchanged are carried forward word for word.

## Reading the previous almanac

The previous almanac is read completely, in parts of 4,000 characters, before anything is compiled. The read is complete only if all six sections are present and the end line is reached. If not, the compile stops and saves nothing, because a new version built from part of the old one would silently drop rules.

## Batching

- Process at most 60 documents per run, the default extraction limit.
- Choose the batch oldest first by the date in the file name, or by modification time when the name has none. During compiling, order claims by the document date the extraction returned, so that later decisions are applied after the rules they replace.
- Send contracts in their own extraction request with the contract schema, and other documents with the mixed schema, because each request takes one schema.
- Send at most 60 files per reconcile request, the default limit, and split by topic when there are more.
- Recordings are transcribed in their own step and never sent to document extraction. Their spoken decisions are mapped to the same claim fields as document claims.
- If a source that an affected record needs is still pending at the end of a run, that record is marked `incomplete` rather than rebuilt from part of its evidence.
- If documents remain, mark the run `partial`, list the remaining files as `pending`, and tell the user to run compile again.

## Claim fields

Each extracted claim must carry:

| Field | Meaning |
|---|---|
| Topic | One of the topics in [the almanac format](almanac-format.md) |
| Subject | The specific thing within the topic, for example "dog weight limit" within Pets |
| Scope | What the claim applies to, for example "Friday and Saturday nights", "the 2026 season" or "all units" |
| Value | The rule, amount, time range or date in plain words |
| Status | adopted, proposed, failed, provisional or informational |
| Document type | bylaws, minutes, notice, contract, agenda, newsletter, email, transcript or other |
| Document date | The date the document states, not the file date |
| Effective date | Only if the document states one |
| Vote | The recorded result, for example 3-0, if any |
| Quote | Short verbatim words that support the claim |
| Source | The file path |

Extraction reports, per file, whether the file was read completely and how many items were found. A completed request is not proof of completeness: a file that was not read completely is marked `partial`, processed again next run, and its topics are marked `incomplete`. The per-topic review before saving is where a person checks what was found.

A claim without a quote is not compiled. It is listed in the changelog as "unverified, not compiled" so that a person can check it.

## Recordings

Meeting recordings are transcribed by the knowledge expert, which also lists each spoken decision, proposal, vote, objection and action item with a quote and the segment time. These items go through the same claim fields as documents, with the recording path and segment time as the source. Claims from a transcript:

- are always `provisional`;
- become `adopted` only when written minutes adopted later state the same decision;
- are never used to supersede a rule from bylaws, minutes or a contract.

## Document types that never set a rule on their own

- **Agenda**: lists proposals. A proposal is compiled as `proposed`, and only the minutes record whether it passed.
- **Newsletter**: informational. It can trigger a conflict entry if it states a rule that disagrees with adopted documents, but it never supersedes one.
- **Email**: evidence of an action (for example, that a notice was sent on a date), not of a rule change.

## Provenance

The previous almanac is state to update, never evidence. Reconciliation compares the new documents with the original source files cited for the affected topics, not with the almanac text, so an earlier conclusion can never support a new one. Every current rule, replaced rule and conflict in the new version cites an original document or recording.

## Building the new version

1. Start from the full previous almanac text, or from an empty almanac on the first run. Carry unchanged topics forward word for word.
2. For each claim, in document date order, apply [the supersession and conflict rules](supersession-rules.md).
3. Rebuild the At a glance table from the topic sections.
4. Update Open items: add new action items, and mark items done only when a document says they were done.
5. Update the Sources ledger and the header counts.
6. Write the changelog entry for this run.
7. Check the size limit in [the almanac format](almanac-format.md), and end the file with its end line.
8. Check that every topic and open item of the previous version is still present, or that the changelog says why it changed. If not, stop and save nothing.

## Saving

Before saving, confirm that the file name is free. A taken name means another version was saved after this compile began, so the compile stops without saving and starts again from the newest version. The version number is set once, in Step 6, and used in the file name, header, changelog entry and end line. After saving, accept the result only if the expert reports it completed and verified, the saved name is the one supplied, the file size matches the content size the save reported, and a complete read-back contains every section, topic and open item of the approved text with this version in every version field. Anything else is an unresolved save: name the file that was written and do not describe it as the new version. The interface offers no byte-for-byte comparison, so this confirms structure and size rather than every character.

## What the compile must never do

- Invent a value, date, vote or quote that no expert returned.
- Resolve a conflict by choosing the more common value or the more plausible one.
- Rewrite or delete an older almanac version.
- Cite the almanac itself as the source of a rule.
- Copy personal details of residents into the almanac.
