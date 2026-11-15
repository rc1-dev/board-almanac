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
        "Users: volunteer boards and managers of HOA, condo and club associations. Rules are spread across years of minutes, notices and recordings. One archive can hold a proposed $235 fee, a notice wrongly saying $230 and the vote setting $240. Which governs?",
    ]),
    ("3. Solution", [
        "Almanac writes a Markdown rulebook on the NAS. For each topic, it gives the current rule, its scope and start date, the vote or document behind it, and a source quote. It also keeps replaced rules, scheduled changes and conflicts.",
    ]),
    ("4. Core user flow", [
        "A board member asks Almanac to compile the folder. It reads every document and recording and shows what changed, with quotes. Nothing is saved without approval. Members can ask questions and get the rule, vote and source.",
    ]),
    ("5. Difference", [
        "Boards use search or a hosted HOA platform. Search returns every document on a topic, leaving the reader to decide which applies. Hosted platforms such as HOALife and HOA Hub answer questions from uploaded documents, so a third party holds a copy. Almanac reconciles minutes, notices, recordings and corrections into the rule in force. With the NAS local model, records naming residents and disputes stay on the association's NAS.",
    ]),
    ("6. NAS capabilities", [
        ("ul", [
            "file-agent (ug-filesystem): snapshot and checks before saving.",
            "knowledge-agent (ug-knowledge): transcription and saving.",
            "document-agent (ug-document): extraction, comparison and answers.",
        ]),
    ]),
    ("7. Technical approach", [
        "The Skill only delegates to these agents. Each compile rebuilds the rulebook from every original document, so a corrected or deleted document leaves no outdated rule. Saving needs approval, never overwrites, and is cancelled if a file changes mid-run.",
    ]),
    ("8. Status", [
        "Implemented: the Skill, which follows the Uliya Skill Development Standard and passes the skill kit's static check, and a validation kit. In 64 simulated runs, the checks found no save without approval or obeyed instructions hidden in documents. Pending NAS validation: accuracy and run time.",
    ]),
    ("9. Validation plan", [
        "On the NAS, Almanac will compile the validation kit's fictional condo archive (2019 to 2026): 15 documents, a recording and a 23-question answer key.",
        ("ul", [
            "Core test 1: the monthly fee should be $240, citing the 2026 vote, not the $235 proposal or $230 notice.",
            "Core test 2: balcony heat pumps should be allowed with conditions, by a 2-1 vote. It should say no document covers Sunday gym hours.",
            "Edge case: after minutes change quiet hours for Friday and Saturday only, version 2 should change those nights and keep 10:00 p.m. on others.",
        ]),
    ]),
    ("10. Limitations", [
        "Results depend on how well UGOS agents read documents, scans and recordings. In simulations, a stand-in model sometimes treated a partial change, such as new Saturday hours, as ending the whole rule. The planned fix has the document agent state which parts still apply. One compile handles up to 60 files.",
    ]),
]

DISCLOSURE = [
    ("Third-party components, licenses and data flows", [
        ("ul", [
            "The Skill bundles no third-party code, models, libraries or external services. It uses only the UGOS agents file-agent, document-agent and knowledge-agent.",
            "Board files are read and processed by UGOS agents on the NAS, and almanac versions are saved to a NAS folder the user confirms. The intended model is the NAS local model. Model routing is a UGOS setting; the Skill asks which model is in use and requires explicit authorization before any document is sent to a third-party model.",
            "The validation kit, which is not part of the Skill, uses reportlab 5.0.1 (BSD license) and python-docx 1.2.0 (MIT license) to generate synthetic test documents. Its scorer uses only the Python standard library.",
            "The package passes the static check of the official UGREEN skill kit 0.7.7 (capability catalog 2.2.0).",
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
