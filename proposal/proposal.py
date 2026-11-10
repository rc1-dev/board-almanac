"""Round 1 proposal for the almanac Skill: source text, word count and HTML.

The 10 answers (with their short headings) count toward the 500-word limit.
The title block and the third-party and disclosure section are excluded by the rules.
Run: python3 proposal.py  -> proposal.html and a word count
"""
import html
import re
from pathlib import Path

TITLE = "Almanac"
SUBTITLE = "A living, cited rulebook for board documents on the UGREEN AI NAS"
META = "Track: Automate Your Workflow · Skill name: almanac · UGREEN Hackathon 2026, Round 1"
LINKS = "Source, demo and video: github.com/rc1-dev/board-almanac"

# (heading, [paragraphs or ("ul", [items])])
ITEMS = [
    ("1. What it does", [
        "Almanac compiles condo, HOA or club board documents on the NAS into a versioned, cited rulebook that answers \"what is the documented rule now, since when, says who?\"",
    ]),
    ("2. User and problem", [
        "Volunteer boards and managers of small associations, whose rules sit across years of minutes, notices and recordings. A new pet policy passes, yet residents quote the old one; a notice states the wrong fee; a failed motion is mistaken for a rule.",
    ]),
    ("3. Solution", [
        "Each compile applies explicit supersession rules and, after the user reviews every changed rule with its quote, saves a new Markdown version: per topic, the documented rule, effective date, vote, source quote, replaced rules, conflicts and action items.",
    ]),
    ("4. Core user flow", [
        "\"Compile the almanac for Board Documents\" → confirm folders → inventory, transcribe, extract, reconcile → review changed rules, approve save → almanac-2026-11-22-v1.md. \"Can I put a heat pump on my balcony?\" → conditions, vote, source, version. \"Check the almanac\" → conflicts, deadlines.",
    ]),
    ("5. Difference", [
        "File chat retrieves passages; each answer must work out which rule replaced which. Almanac settles this once, as files arrive: effective dates, failed motions, corrections, partial amendments (weekend-only quiet hours) and unresolved conflicts are explicit, never guessed. Answers come from one small reconciled file, which suits a local model.",
    ]),
    ("6. NAS capabilities", [
        ("ul", [
            "file-agent (ug-filesystem): previous almanac (1, Ask, Lint), checksummed inventory (2), name check and read-back (8, 9).",
            "knowledge-agent (ug-knowledge): transcription (3), saving versions (9).",
            "document-agent (ug-document): claim extraction (4), reconciliation (5), answers (Ask).",
            "Intended model: NAS local.",
        ]),
    ]),
    ("7. Technical approach", [
        "The parent Skill only delegates to these experts. Inputs: two folders, mode, model route. Permissions: reads plus approved folder creation and saves; nothing overwritten or deleted. A Sources ledger (checksum, status) drives resumable compiles, 60 documents per run. The previous almanac is read completely or the run stops; it is state, never evidence, so every rule cites an original quote.",
    ]),
    ("8. Status", [
        "Implemented: SKILL.md and six references; official checker (catalog 2.0.0): static-pass, 0 errors, 0 warnings. Validation kit: synthetic board folder, 20-question answer key, scorer. Pending NAS validation: runtime behaviour, accuracy, timing.",
    ]),
    ("9. Validation plan", [
        "Core 1, supersession: fee and pet rule. Pass: EUR 240 and two pets with dates, votes and citations; never the EUR 235 proposal or erroneous EUR 230 notice.",
        "Core 2, from the almanac: heat-pump conditions with the 2-1 vote and version; a gym question returns \"not covered\".",
        "Edge: add weekend quiet-hours minutes and recompile. Pass: only that file processed, weekdays unchanged, every other rule and the pool conflict preserved.",
        "All 20 questions also run against plain file chat.",
    ]),
    ("10. Limitations", [
        "Quality depends on on-device extraction, OCR and transcription; incomplete files are retried. Not legal advice. Model routing is a UGOS setting the Skill confirms but cannot enforce. Tested on synthetic data only.",
    ]),
]

DISCLOSURE = [
    ("Third-party components, licenses and data flows", [
        ("ul", [
            "Skill package: no bundled third-party code, models, libraries or external services. It uses only UGOS experts (file-agent, document-agent, knowledge-agent).",
            "Data flow: board files are read and processed by UGOS experts on the NAS; almanac versions are saved to a NAS folder the user confirms. The intended model is the NAS local model. Model routing is a UGOS setting: the Skill asks which model is used and requires explicit authorization before any document reaches a third-party model.",
            "Validation kit only (not in the Skill): reportlab 5.0.1 (BSD license) and python-docx 1.2.0 (MIT license) generate the synthetic test documents; the scorer uses the Python standard library.",
            "Checked with the official UGREEN skill kit 0.7.3 checker.",
            "AI assistance: Claude (Anthropic) helped draft and review the Skill files, test materials and this proposal.",
            "All test data is synthetic and fictional. The workflow was designed and written during the hackathon.",
        ]),
    ]),
]


def words(text):
    return len(re.findall(r"[A-Za-z0-9€][A-Za-z0-9€'’.,:/()%-]*", text))


def flatten(items):
    out = []
    for heading, body in items:
        out.append(heading)
        for b in body:
            if isinstance(b, tuple):
                out.extend(b[1])
            else:
                out.append(b)
    return out


CODE = re.compile(r"\b(ug-[a-z]+|[a-z]+-agent|almanac-2026-11-22-v1\.md|SKILL\.md)\b")


def fmt(text):
    t = html.escape(text, quote=False)
    return CODE.sub(r"<code>\1</code>", t)


def render(items, cls=""):
    parts = []
    for heading, body in items:
        parts.append(f'<section class="{cls}"><h2>{html.escape(heading)}</h2>')
        for b in body:
            if isinstance(b, tuple):
                parts.append("<ul>" + "".join(f"<li>{fmt(i)}</li>" for i in b[1]) + "</ul>")
            else:
                parts.append(f"<p>{fmt(b)}</p>")
        parts.append("</section>")
    return "\n".join(parts)


def main():
    counted = flatten(ITEMS)
    n = sum(words(t) for t in counted)
    per = [(h, sum(words(t) for t in flatten([(h, b)]))) for h, b in ITEMS]
    for h, c in per:
        print(f"{c:4d}  {h}")
    print(f"{n:4d}  TOTAL counted (limit 500)")
    print(f"{sum(len(t.split()) for t in counted):4d}  TOTAL by plain whitespace split")

    ws = sum(len(t.split()) for t in counted)
    css = Path(__file__).with_name("style.css").read_text(encoding="utf-8")
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Almanac - Round 1 proposal</title><style>{css}</style></head><body>
<header><h1>{TITLE}</h1><p class="sub">{html.escape(SUBTITLE)}</p><p class="meta">{html.escape(META)}</p><p class="meta"><a href="https://github.com/rc1-dev/board-almanac">{html.escape(LINKS)}</a></p></header>
<main>{render(ITEMS)}</main>
<footer>{render(DISCLOSURE, "disc")}</footer>
</body></html>"""
    Path(__file__).with_name("proposal.html").write_text(doc, encoding="utf-8")
    return n


if __name__ == "__main__":
    main()
