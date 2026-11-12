# Test plan

## Test corpus

A synthetic board folder for a fictional 48-unit building, Harbor View Condominium Association, covering 2019 to 2026. It contains no real people or addresses. People appear by board role only.

| Kind | Files | What they test |
|---|---|---|
| Bylaws and house rules, 2019 | 1 | Baseline rules, amendment thresholds |
| Board minutes, 2024 to 2026 | 7, plus 1 added for the edge case | Adopted decisions, votes, failed motions, corrections, partial-scope changes |
| Board notices | 3 | Restating rules, one notice with a wrong fee, one notice that conflicts with minutes |
| Contract | 1 | Term, auto-renewal, notice period, price cap |
| Agenda | 1 | A proposed fee that was never adopted |
| Newsletter | 1 | Informal wording that must not change a rule |
| Email | 1 | Evidence that a notice was sent late |
| Meeting recording | 1 | A provisional decision not yet in minutes |

## Answer key

Twenty-three questions with expected facts, forbidden facts and the source file that must be cited. Examples:

| Question | Must include | Must not include | Must cite |
|---|---|---|---|
| What is the monthly fee now? | $240 | $230, $235 | minutes-2026-01-20 |
| How many pets can a unit have? | 2 | 35 lb as a current limit | minutes-2025-04-15 |
| What are the pool hours this season? | Both 10:00 p.m. and 9:00 p.m., stated as a conflict | A single answer | minutes-2025-09-10 and notice-2026-05-01-pool |
| Can I use a barbecue on my balcony? | Still prohibited; electric barbecues discussed, provisional | Allowed | bylaws-house-rules-2019 |
| Is the gym open on Sundays? | Not covered | Any hours | none |

A small scorer checks each answer for the required facts, the forbidden facts and the citations, and reports a score per question.

## Core test case 1: supersession with history

Compile the full folder, then ask about the monthly fee and the pet rule. Pass if each answer gives the current value, its effective date, the document and vote that set it, and the replaced values with their date ranges; and if the agenda proposal and the wrong notice are never given as current.

## Core test case 2: answer from the almanac

Ask whether a heat pump unit may go on a balcony. Pass if the answer gives the conditions (approval, floor-mounted, 60 dB or less), the vote 2-1 and its date, cites the almanac version, and was produced from the almanac file rather than from the raw folder. Then ask about the gym. Pass if the answer is "not covered" with no invented hours.

## Edge case: an amendment that changes part of a rule

Add minutes that change quiet hours on Friday and Saturday nights only, and compile again. Pass if the almanac is rebuilt from all documents, a new version is saved next to the old one, Friday and Saturday quiet hours change while other nights stay at 10:00 p.m., the changelog reports only that change, and the pool hours remain an open conflict.

## Adversarial cases

The validation kit contains six cases with expected outcomes: corrected minutes that remove a decision, a corrected email that changes an open item, a change adopted for a later effective date, a document that agrees with every rule, a document containing instructions addressed to an AI assistant, and a file that cannot be read. Further checks:

- **Exclusion:** the unreadable file stops the compile until the user fixes or excludes it. Pass if, after exclusion, the almanac is marked as compiled with exclusions and its answers never claim that no rule exists.
- **Sources change during a compile:** change a file between the snapshot and the save. Pass if the Skill stops without saving.
- **Name taken:** create a file with the proposed almanac name first. Pass if the Skill stops without saving and nothing is overwritten.
- **Model routing:** record which model the NAS uses for document processing.

## Device test plan

The NAS is available for one day, so the tests are ordered by priority and recorded as they go.

| Priority | Test | Purpose |
|---|---|---|
| P0 | Install, compile three core documents, ask two questions, save and reopen a version | The Skill runs end to end |
| P1 | Add the weekend amendment and compile again; compile the full archive; record demonstration footage | The central behavior on the real device |
| P2 | Adversarial cases, repeated runs, timings | Robustness and engineering evidence |

Record footage as soon as P0 and P1 succeed rather than at the end of the day.

## Checking answers

The scorer checks required facts, forbidden statements and citations with patterns. It is a regression aid and can accept an answer that is wrong in meaning, so every answer from the device is also checked by hand for the current value, effective date, vote, source and replaced rules.

## Comparison

Run the same questions through plain file chat over the raw folder and score both with the same answer key.
