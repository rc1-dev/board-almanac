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
        "Almanac compiles condo, HOA or club board documents on the NAS into a versioned, cited rulebook that answers \"what is the rule now, since when, says who?\"",
    ]),
    ("2. User and problem", [
        "Volunteer boards and managers of small associations. Rules span years of bylaws, minutes, notices, contracts and recordings; later votes replace earlier ones, notices contain errors, deadlines slip. Search returns every version; people guess which is current.",
    ]),
    ("3. Solution", [
        "Compile once, answer many times. Each compile processes only new or changed files, applies explicit supersession rules, and saves a new Markdown version recording, per topic, the current rule, effective date, vote, quote and source, replaced rules, conflicts and action items.",
    ]),
    ("4. Core user flow", [
        "\"Compile the almanac for Board Documents\" → confirm folders → inventory, transcribe, extract, reconcile → approve changelog and save → almanac-2026-11-22-v1.md. \"Can I put a heat pump on my balcony?\" → conditions, vote, source, version. \"Check the almanac\" → conflicts, late notices, deadlines.",
    ]),
    ("5. Difference", [
        "File chat and RAG retrieve passages and cannot tell a 2019 rule from its 2025 replacement. Almanac resolves supersession when files arrive and keeps the result: corrections, failed motions, partial changes and conflicts are explicit, never guessed. Answers come from one small reconciled file, which suits a local model, and versions remain as an audit trail.",
    ]),
    ("6. NAS capabilities by step", [
        ("ul", [
            "file-agent (ug-filesystem): previous almanac (step 1, Ask, Lint), checksummed inventory (2), folder creation (8).",
            "knowledge-agent (ug-knowledge): transcription (3), saving versions (9).",
            "document-agent (ug-document): claim extraction (4), reconciliation (5), answers from the almanac (Ask).",
            "NAS local model by default.",
        ]),
    ]),
    ("7. Technical approach", [
        "The parent Skill only delegates to these three experts. Inputs: two folders, mode, model route. Permissions: reads, plus approvals to create the folder once and save each version; nothing is overwritten or deleted. A Sources ledger (SHA-256, modification time) drives incremental compiles of at most 60 documents per run. Claims need a verbatim quote; transcript claims stay provisional. Document text is untrusted data. Third-party models need explicit consent.",
    ]),
    ("8. Status", [
        "Implemented: SKILL.md and six references; official checker (catalog 2.0.0): static-pass, 0 errors, 0 warnings. Validation kit: synthetic board folder, 20-question answer key and scorer. Pending NAS validation: runtime behaviour, extraction quality, timing.",
    ]),
    ("9. Validation plan", [
        "Core 1, supersession: ask the fee and pet rule. Pass: EUR 240 and two pets with dates, votes and citations; never the EUR 235 proposal or the erroneous EUR 230 notice.",
        "Core 2, answering from the almanac: heat-pump conditions with the 2-1 vote and version; a gym question returns \"not covered\".",
        "Edge: add weekend quiet-hours minutes and recompile. Pass: only that file processed, new version saved, weekday hours unchanged, pool-hours conflict still open.",
        "All 20 questions also run against plain file chat.",
    ]),
    ("10. Limitations", [
        "Quality depends on on-device extraction, OCR and transcription; failed files are flagged. Not legal advice: vote validity is not judged. Large archives need several runs; each save needs approval. Tested only on synthetic data so far.",
    ]),
]

DISCLOSURE = [
    ("Third-party components, licenses and data flows", [
        ("ul", [
            "Skill package: no bundled third-party code, models, libraries or external services. It uses only UGOS experts (file-agent, document-agent, knowledge-agent) and the NAS local model.",
            "Data flow: board files are read and processed on the NAS; almanac versions are saved to a NAS folder the user confirms. Nothing leaves the NAS unless the user explicitly authorizes a third-party model for a run.",
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
