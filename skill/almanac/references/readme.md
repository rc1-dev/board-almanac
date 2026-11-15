# Readme

## What it is

Almanac compiles a board folder (bylaws, minutes, notices, contracts and meeting recordings) into a cited, versioned rulebook saved as Markdown files on the NAS, and answers questions from it.

## Setup

1. Put the board documents in one shared folder on the NAS.
2. Install the Skill.
3. Ask: "Compile the almanac for the Board Documents folder." Confirm the board folder, the almanac folder and the model route.
4. Approve creating the almanac folder, if it does not exist, and saving the first version.

## Everyday use

Once the first version is saved, anyone with access can ask about the rules in plain language. For example:

- "What is the current rule on pets?"
- "How has the monthly fee changed since 2024?"

Two other requests keep the almanac useful:

- "Check the almanac" lists open conflicts, overdue items and coming deadlines.
- "Update the almanac", after new minutes are added, compiles a new version.

## What it changes on the NAS

It creates the almanac folder once, if needed, and adds one new Markdown file per compile run, rebuilt from the original documents. It never asks a UGOS agent to change, move or delete board documents or older almanac versions. Before each save it checks that the file name is free, and after saving it reads the file back. Each save asks for approval after a review of every changed rule.

## Removal

Uninstall the Skill. To remove its output, delete the almanac folder yourself; the board documents are untouched.

## Privacy

Board documents are read by the UGOS agents on the NAS: file-agent, document-agent and knowledge-agent. The intended setting is the NAS local model. Model routing is a UGOS setting that the Skill cannot change: it asks which model the NAS uses, and if that is a third-party model it asks for explicit authorization before reading any document. The almanac records people by board role, and leaves out residents' private matters.

## Limits

The Skill reports what the documents say. It is not legal advice, does not judge whether votes or notices were valid, and records conflicts instead of resolving them. Scanned documents and recordings depend on extraction and transcription quality on the device. This version supports up to 60 source files per compile as a conservative design limit. Every compile re-reads all documents, so a larger folder takes longer to compile.

## Disclosure

- Written for the UGREEN AI NAS hackathon. The workflow was designed and written during the hackathon.
- AI assistance: Claude (Anthropic) was used to help draft and check the Skill files and test materials.
- Third-party components: none bundled. The Skill uses only the UGOS agents named in the capability evidence section of SKILL.md.
- The package passes the static check of the official UGREEN skill kit (version 0.7.7).
- Test data is synthetic and fictional.
