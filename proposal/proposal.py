"""Round 1 proposal for the almanac Skill: source text and HTML.

The 10 answers (with their short headings) count toward the 500-word limit.
The title block and the third-party and disclosure section are excluded by the rules.
Run: python3 proposal.py  -> proposal.html (prints a word count to the console only)
"""
import html
import re
from pathlib import Path

TITLE = "Almanac"
SUBTITLE = "A versioned, cited rulebook for board documents on the UGREEN AI NAS"
META = "Track: Automate Your Workflow · Skill name: almanac · UGREEN Hackathon 2026, Round 1"
LINKS = "Source, demo and video: github.com/rc1-dev/board-almanac"

# (heading, [paragraphs or ("ul", [items])])
ITEMS = [
    ("1. What the Skill does", [
        "Almanac turns a board's document archive on the NAS into a versioned, cited rulebook showing which rule applies, since when, and on whose authority.",
    ]),
    ("2. User and problem", [
        "Volunteer boards of condo, HOA and club associations. Rules accumulate over years of minutes, notices and recordings; later decisions replace earlier ones, so residents quote repealed rules and mistake failed motions for policy.",
    ]),
    ("3. Solution", [
        "The rulebook is a Markdown file kept on the NAS. Each topic records the documented rule, effective date, authorizing vote or document, a quotation, replaced rules, scheduled changes and open conflicts. Each version records what changed, with evidence, and is saved only after user review.",
    ]),
    ("4. Core user flow", [
        "The Skill snapshots the folder with checksums, transcribes recordings, extracts and reconciles decisions from every document, and saves a version after user approval. Members can then ask whether a balcony heat pump is allowed and get its conditions, vote and source.",
    ]),
    ("5. Difference", [
        "File chat retrieves passages and leaves each answer to decide which version applies; errors mean a refused Saturday renovation, a wrong fee or a missed contract deadline. Almanac decides once, with explicit rules for effective dates, scheduled changes, failed motions, corrections, partial amendments and conflicts.",
    ]),
    ("6. NAS capabilities", [
        ("ul", [
            "file-agent (ug-filesystem): checksummed snapshot (step 1), checks around saving (7).",
            "knowledge-agent (ug-knowledge): transcription (2), saving each version (7).",
            "document-agent (ug-document): extraction (3), reconciliation (4), answers.",
            "Intended model: the NAS local model.",
        ]),
    ]),
    ("7. Technical approach", [
        "The Skill takes two folders, a mode and the model setting. It only delegates to these agents, needs approval to create the folder or save, and never overwrites or deletes. Each compile rebuilds the almanac from every original document (up to 60), so a corrected or deleted document cannot leave an outdated rule behind. It recompiles when a scheduled change takes effect and saves nothing if a file changes mid-run.",
    ]),
    ("8. Status", [
        "SKILL.md and six references pass the official checker (catalog 2.0.0) cleanly. In 64 simulated runs with a small model playing the Skill, none saved without approval or followed instructions planted in a document; their results prompted four rounds of fixes. Device accuracy and timing await NAS testing.",
    ]),
    ("9. Validation plan", [
        "Core case 1, supersession: fee and pet answers give $240 and two pets with citations, never the $235 proposal or wrong $230 notice.",
        "Core case 2, answering: a heat-pump question returns conditions, 2-1 vote and version; a gym question is reported as not covered.",
        "Edge case: added minutes change weekend quiet hours only; version 2 keeps 10:00 p.m. on other nights, other rules and the pool conflict. File chat is scored on the same questions.",
    ]),
    ("10. Limitations", [
        "Accuracy depends on on-device extraction, OCR and transcription. Tests showed partial changes sometimes recorded as ending a whole rule; the pre-save review shows each change beside the replaced rule, and a planned fix has the document agent report which parts stay in force.",
    ]),
]

DISCLOSURE = [
    ("Third-party components, licenses and data flows", [
        ("ul", [
            "The Skill bundles no third-party code, models, libraries or external services. It uses only the UGOS agents file-agent, document-agent and knowledge-agent.",
            "Board files are read and processed by UGOS agents on the NAS, and almanac versions are saved to a NAS folder the user confirms. The intended model is the NAS local model. Model routing is a UGOS setting; the Skill asks which model is in use and requires explicit authorization before any document is sent to a third-party model.",
            "The validation kit, which is not part of the Skill, uses reportlab 5.0.1 (BSD license) and python-docx 1.2.0 (MIT license) to generate synthetic test documents. Its scorer uses only the Python standard library.",
            "The package was checked with the official UGREEN skill kit 0.7.3.",
            "Claude (Anthropic) assisted with drafting and reviewing the Skill files, test materials and this proposal, and Claude models played the Skill and graded the runs in the simulated tests.",
            "All test data is synthetic and fictional. The workflow was designed and written during the hackathon.",
            "The almanac reports what the documents record and is not legal advice.",
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
