# Compile protocol

This reference explains the Compile steps in [SKILL.md](../SKILL.md). It adds no new NAS actions.

## Why every compile is a rebuild

One rule may be set in the 2019 bylaws, changed in 2024 minutes, misstated in a 2025 notice and corrected later. Each compile reads every original document again and builds the almanac from what they say. Nothing is carried over from the previous almanac except its version number and, for the changelog, its At a glance table and Open items. A corrected or deleted document therefore cannot leave an outdated rule behind, and an amendment is always read together with the rule it amends.

Rebuilding takes longer, because every compile re-reads the whole folder. This version supports up to 60 source files per compile as a conservative design limit; the capacity that works in practice will be measured on the NAS.

## When to compile

A compile is needed when a file in the board folder is new, changed or missing compared with the Sources ledger of the newest almanac, or when a scheduled change in that almanac has reached its effective date. Otherwise the almanac is current.

## Snapshot

Step 1 records every source file with its path relative to the board folder, size, modification time and SHA-256 checksum. This snapshot becomes the Sources ledger. Before saving, Step 7 lists the files again; if anything differs, the compile stops, because the almanac would mix two states of the folder. A new compile starts again at Step 1 and reads every document. A file changed in the short time between this check and the save would still not be detected.

## Claim records

Each extracted record carries:

| Field | Meaning |
|---|---|
| Topic | One of the topics in [the almanac format](almanac-format.md) |
| Subject | The specific matter within the topic, for example "dog weight limit" within Pets |
| Scope | What it applies to, for example "Friday and Saturday nights", "the 2026 season" or "all units" |
| Value | The rule, amount, time range or date in plain words |
| Status | adopted, proposed, failed or informational |
| Document type and date | As stated in the document, not the file date |
| Effective date and vote | Only if stated |
| Quote | Verbatim, at most 30 words |
| Source | The file path |

A record without a quote is not used. Keep records compact: the build step needs every record from every document at once.

## Recordings

Recordings are transcribed by the knowledge agent and never sent to document extraction. Spoken decisions become records with the recording path and segment time as source. They are always provisional, never replace an adopted rule, and become adopted only when written minutes adopt the same decision.

## Documents that never set a rule

An agenda lists proposals. A newsletter is informational, though it can reveal a conflict. An email is evidence of an action, such as when a notice was sent, not of a rule.

## Unreadable files and exclusions

A file that fails or is not read completely blocks the compile until the user either fixes it or explicitly excludes it. An excluded file is listed in the Sources ledger as excluded, with the reason. The almanac is then marked "compiled with exclusions" and states that the excluded files may contain decisions on any topic, because their contents are unknown. Its answers never treat the absence of a rule or a conflict as established.

## Building the almanac

1. Group the records by topic, subject and scope.
2. Apply [the supersession rules](supersession-rules.md) in document date order, as of the board's local date.
3. Record adopted changes with a later effective date as scheduled.
4. Write every section of the almanac in the fixed topic order, with the Sources ledger from the snapshot and the end line.
5. Compare each topic's rule, scope, effective date and status with the previous At a glance table, and the open items with the previous Open items section, to write the changelog. Any difference in meaning is a change; only a difference in wording is not. The comparison is at summary level: a change only in a topic's authority or evidence, such as a corrected vote count, appears in the new topic but is not detected as a change.

## Saving

The version number is one above the previous version and appears in the file name, header, changelog entry and end line. Before saving, the snapshot is checked and the file name must be free; a taken name means another version was saved meanwhile, so the compile stops. After saving, the file is read back completely. The save counts only if it was verified, the name and size match, and every section and topic is present with this version number. The interface offers no byte-for-byte comparison, so this confirms structure and size rather than every character.

## What a compile never does

- Use the previous almanac as evidence for a rule.
- Invent a value, date, vote or quote that no expert returned.
- Resolve a conflict by choosing the more common or more plausible value.
- Overwrite, move or delete any file.
- Copy residents' personal details into the almanac.
