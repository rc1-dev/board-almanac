# Readme

## What it is

Almanac compiles a board folder (bylaws, minutes, notices, contracts and meeting recordings) into a cited, versioned rulebook saved as Markdown files on the NAS, and answers questions from it.

## Setup

1. Put the board documents in one shared folder on the NAS.
2. Install the Skill.
3. Ask: "Compile the almanac for the Board Documents folder." Confirm the board folder, the almanac folder and the model route.
4. Approve creating the almanac folder, if it does not exist, and saving the first version.

## Everyday use

- "What is the current rule on pets?"
- "How has the monthly fee changed since 2024?"
- "Check the almanac" for conflicts, overdue items and coming deadlines.
- "Update the almanac" after adding new minutes.

## What it changes on the NAS

It creates the almanac folder once, if needed, and adds one new Markdown file per compile run. It never changes, moves or deletes board documents or older almanac versions. Each save asks for approval.

## Removal

Uninstall the Skill. To remove its output, delete the almanac folder yourself; the board documents are untouched.

## Privacy

Board documents are processed by the NAS experts and, by default, the NAS local model. Nothing is sent to a third-party model unless the user explicitly authorizes it for a run. The almanac records people by board role, and leaves out residents' private matters.

## Limits

The Skill reports what the documents say. It is not legal advice, does not judge whether votes or notices were valid, and records conflicts instead of resolving them. Scanned documents and recordings depend on extraction and transcription quality on the device.

## Disclosure

- Written for the UGREEN AI NAS hackathon. The workflow was designed and written during the hackathon.
- AI assistance: Claude (Anthropic) was used to help draft and check the Skill files and test materials.
- Third-party components: none bundled. The Skill uses only NAS experts named in the capability evidence section of SKILL.md.
- The official Skill kit checker was used to check the package.
- Test data is synthetic and fictional.
