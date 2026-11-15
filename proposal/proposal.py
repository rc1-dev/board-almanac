"""Round 1 proposal for the almanac Skill: source text and HTML.

The 10 answers (with their short headings) count toward the 500-word limit.
The title block and the third-party and disclosure section are excluded by the rules.
Run: python3 proposal.py  -> proposal.html (prints a word count to the console only)
"""
import html
import re
from pathlib import Path

TITLE = "Almanac"
SUBTITLE = "A versioned, cited rulebook for HOA and condo association records on the UGREEN AI NAS"
META = "Rajeev Chawla · Track: Automate Your Workflow · Skill name: almanac · UGREEN Hackathon 2026, Round 1"
LINKS = "Source, demo and video: github.com/rc1-dev/board-almanac"

# (heading, [paragraphs or ("ul", [items])])
ITEMS = [
    ("1. What the Skill does", [
        "Almanac turns an HOA or condo board's archive on the NAS into a versioned, cited rulebook: which rule applies now, since when, and on whose authority.",
    ]),
    ("2. User and problem", [
        "Users: volunteer boards and managers of HOA, condo and club associations. Rules are spread across years of minutes, notices, recordings and corrections. One archive can hold a proposed $235 fee, a notice wrongly saying $230 and the vote setting $240. Search finds all three; which governs?",
    ]),
    ("3. Solution", [
        "A Markdown rulebook on the NAS recording, for each topic, the current rule, scope, effective date, authorizing vote or document, a quotation, replaced rules, scheduled changes and open conflicts.",
    ]),
    ("4. Core user flow", [
        "A board member points Almanac at the board folder and asks it to compile. It reads every document and recording, shows the proposed changes with quotations, and saves it once approved. Members can then ask questions and get the rule, vote and source.",
    ]),
    ("5. Difference", [
        "Search finds what documents say; Almanac reconstructs which decisions still apply. Hosted HOA platforms, such as HOALife and HOA Hub, answer questions from uploaded governing documents. Almanac instead reconciles decisions across minutes, notices, recordings and corrections. With the UGOS local model, documents need not go to a hosted AI service.",
    ]),
    ("6. NAS capabilities", [
        ("ul", [
            "file-agent (ug-filesystem): snapshot and checks before saving.",
            "knowledge-agent (ug-knowledge): transcription and saving.",
            "document-agent (ug-document): extraction, reconciliation and answers.",
        ]),
    ]),
    ("7. Technical approach", [
        "The Skill only delegates to these agents. Each compile rebuilds the rulebook from every original document, so a corrected or deleted document leaves no outdated rule. A compile after a scheduled date makes that change current. Saving needs approval, never overwrites, and is cancelled if a file changes mid-run.",
    ]),
    ("8. Status", [
        "Implemented: the Skill, which follows the Uliya Skill Development Standard and passes the skill kit's static check, and a validation kit. In 64 simulated runs with a small stand-in model, the checks found no save without approval or obeyed instructions hidden in documents. Pending NAS validation: accuracy and run time.",
    ]),
    ("9. Validation plan", [
        "On the NAS, Almanac will compile the validation kit's synthetic condo archive, including the fee history above.",
        ("ul", [
            "Core test 1: when asked the monthly fee, it should answer $240 with the vote and minutes, not $235 or $230.",
            "Core test 2: when asked about balcony heat pumps, it should give the conditions and 2-1 vote; for gym hours, which no document covers, it should say so.",
            "Edge case: after new minutes change quiet hours on Friday and Saturday only, version 2 should change those nights and keep 10:00 p.m. on others.",
        ]),
    ]),
    ("10. Limitations", [
        "Answer quality depends on the NAS's document reading, OCR and transcription. In simulations, the model sometimes treated a partial change, such as new Saturday hours, as ending the whole rule. The review before saving shows each change beside the earlier rule, but some reviews were incomplete. One compile handles up to 60 files.",
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
