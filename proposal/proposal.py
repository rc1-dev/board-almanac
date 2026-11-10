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
        "Volunteer board members and managers of condo, HOA and club associations. Rules build up over years of minutes, notices and recordings, and later decisions replace earlier ones, so residents quote repealed rules and mistake failed motions for policy.",
    ]),
    ("3. Solution", [
        "Almanac compiles the archive into a Markdown rulebook on the NAS. Each topic records the documented rule, its effective date, the authorizing vote or document, a supporting quotation, replaced rules and open conflicts. Versions are saved only after the user reviews the changes.",
    ]),
    ("4. Core user flow", [
        "The Skill inventories the folder, transcribes recordings, extracts and reconciles decisions, and saves a version once the user approves. Members can then ask whether a heat pump may go on a balcony and receive the conditions, vote and source.",
    ]),
    ("5. Difference", [
        "File chat retrieves passages per question and leaves each answer to decide which version applies. Almanac decides once, as documents arrive, with explicit rules for effective dates, failed motions, corrections, partial amendments and conflicts, and answers from one reconciled file.",
    ]),
    ("6. NAS capabilities", [
        ("ul", [
            "file-agent (ug-filesystem): previous almanac (step 1), checksummed inventory (2), checks around saving (8, 9).",
            "knowledge-agent (ug-knowledge): transcription (3), saving each version (9).",
            "document-agent (ug-document): extraction (4), reconciliation (5), answers.",
            "Intended model: the NAS local model.",
        ]),
    ]),
    ("7. Technical approach", [
        "The parent Skill only delegates to these agents. Inputs are the two folders, the mode and the model setting. It reads files and needs approval to create the folder or save; it never overwrites or deletes. A ledger of checksums and processing states makes compiles incremental and resumable, up to 60 documents per run. The previous almanac is read in full or the run stops, and every rule cites an original document.",
    ]),
    ("8. Status", [
        "SKILL.md and six references are complete and pass the official checker (catalog 2.0.0) without errors or warnings. A synthetic archive, answer key and scorer are ready; runtime accuracy and timing await NAS testing.",
    ]),
    ("9. Validation plan", [
        "Core case 1, supersession: the fee and pet-rule answers give $240 and two pets with dates, votes and citations, never the $235 proposal or the erroneous $230 notice.",
        "Core case 2, answering from the almanac: a heat-pump question returns the conditions, 2-1 vote and version; a gym question is reported as not covered.",
        "Edge case: minutes changing only weekend quiet hours are added. The recompile extracts the new minutes, rechecks the bylaws they amend, and preserves weekday hours, every other rule and the open pool conflict. All 20 questions also go to plain file chat.",
    ]),
    ("10. Limitations", [
        "Accuracy depends on on-device extraction, OCR and transcription. The almanac is not legal advice. Model routing is a UGOS setting the Skill confirms but cannot enforce. Testing so far is synthetic.",
    ]),
]

DISCLOSURE = [
    ("Third-party components, licenses and data flows", [
        ("ul", [
            "The Skill bundles no third-party code, models, libraries or external services. It uses only the UGOS agents file-agent, document-agent and knowledge-agent.",
            "Board files are read and processed by UGOS agents on the NAS, and almanac versions are saved to a NAS folder the user confirms. The intended model is the NAS local model. Model routing is a UGOS setting; the Skill asks which model is in use and requires explicit authorization before any document is sent to a third-party model.",
            "The validation kit, which is not part of the Skill, uses reportlab 5.0.1 (BSD license) and python-docx 1.2.0 (MIT license) to generate synthetic test documents. Its scorer uses only the Python standard library.",
            "The package was checked with the official UGREEN skill kit 0.7.3.",
            "Claude (Anthropic) assisted with drafting and reviewing the Skill files, test materials and this proposal.",
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
