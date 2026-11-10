"""Build the synthetic Harbor View board folder used to validate the almanac Skill.

Everything here is fictional. People appear by board role only.
Output:
  corpus/Board Documents/      files present at the first compile
  corpus/add-later/            the file added for the incremental-compile edge case
Run: python3 build_corpus.py
"""
import os
from pathlib import Path

from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

HERE = Path(__file__).resolve().parent
BOARD = HERE / "corpus" / "Board Documents"
LATER = HERE / "corpus" / "add-later"
ASSOC = "Harbor View Condominium Association"

# Each document: (filename, title, [paragraphs])
DOCS = [
    ("bylaws-house-rules-2019.pdf", f"{ASSOC} - Bylaws and House Rules", [
        "Adopted by the unit owners on May 1, 2019. Effective May 1, 2019.",
        "PART A - BYLAWS",
        "Article 1. The Association is governed by a board of three directors: a President, a Treasurer and a Secretary. A quorum is two directors.",
        "Article 2. Monthly common charges are set by the board in the annual budget and take effect on the date the board states.",
        "Article 3. Amendments. These Bylaws (Part A) may be amended only by a two-thirds (2/3) vote of unit owners at an annual meeting. The House Rules (Part B) may be amended by a majority vote of the board.",
        "PART B - HOUSE RULES",
        "Rule 4. Pets. Each unit may keep one (1) pet. Dogs may not exceed 35 pounds. All pets must be registered with management.",
        "Rule 5. Renovations. Renovation and construction work is permitted Monday to Friday, 8:00 a.m. to 5:00 p.m. No work is permitted on Saturdays, Sundays or holidays.",
        "Rule 6. Quiet hours. Quiet hours are 10:00 p.m. to 7:00 a.m. every night.",
        "Rule 7. Balconies. No fixtures, appliances or equipment may be mounted on balconies or exterior walls without written board approval. Barbecues and open flames are prohibited on balconies.",
        "Rule 8. Leasing. Units may not be leased for a term of less than six (6) months.",
        "Rule 9. Parking. Each unit has one assigned space. Guest vehicles may stay in guest parking for no more than 72 hours.",
        "Rule 10. Pool. The pool is open 9:00 a.m. to 9:00 p.m. daily during the season, June 1 to September 15.",
    ]),
    ("minutes-2024-01-18.pdf", "Board meeting minutes - January 18, 2024", [
        "Present: President, Treasurer, Secretary. Quorum present. Minutes approved at the meeting of June 12, 2024.",
        "1. Budget 2024. Motion: the monthly common charge is set at $210 per unit, effective March 1, 2024. Motion carried 3-0.",
        "2. Landscaping. Motion: award the landscaping contract to Bramblewick Grounds LLC on the terms of the attached agreement, for the period April 1, 2024 to March 31, 2026. Motion carried 3-0.",
        "3. Action: Treasurer to send the 2024 budget to all owners by February 15, 2024.",
    ]),
    ("contract-bramblewick-landscaping-2024.pdf", "Landscaping Services Agreement", [
        f"Between {ASSOC} (the Client) and Bramblewick Grounds LLC (the Contractor). Signed January 25, 2024.",
        "1. Term. This agreement runs from April 1, 2024 to March 31, 2026.",
        "2. Fee. The Client pays the Contractor $1,450 per month.",
        "3. Renewal. This agreement renews automatically for successive one-year terms unless either party gives written notice of non-renewal at least sixty (60) days before the end of the current term.",
        "4. Price on renewal. On each renewal the monthly fee may increase by no more than four percent (4%).",
        "5. Scope. Lawn care, hedges, seasonal planting and leaf removal for all common grounds.",
    ]),
    ("minutes-2024-06-12.docx", "Board meeting minutes - June 12, 2024", [
        "Present: President, Treasurer, Secretary. Quorum present. Minutes of January 18, 2024 approved 3-0.",
        "1. Renovation hours. Motion: amend House Rule 5 to permit renovation work on Saturdays from 9:00 a.m. to 1:00 p.m., effective July 15, 2024. Work on Sundays and holidays remains prohibited. Weekday hours are unchanged. Motion carried 3-0.",
        "2. Pets. The board adopted a pet registration form for use by management. No change to the pet rule.",
        "3. Action: Secretary to publish a notice of the new renovation hours by July 1, 2024.",
    ]),
    ("notice-2024-07-01-renovation-hours.pdf", "Notice to residents - Renovation hours", [
        "Dated July 1, 2024.",
        "From July 15, 2024, renovation work is permitted Monday to Friday 8:00 a.m. to 5:00 p.m. and Saturday 9:00 a.m. to 1:00 p.m. No work on Sundays or holidays.",
    ]),
    ("minutes-2024-11-07.pdf", "Board meeting minutes - November 7, 2024", [
        "Present: President, Treasurer, Secretary. Quorum present.",
        "1. Heat pumps. Several owners asked to install heat pump outdoor units on balconies. Discussion of load and noise. The item was tabled.",
        "2. Action: Secretary to obtain a structural engineer's opinion on balcony load and noise by January 31, 2025.",
    ]),
    ("agenda-2025-01-23.pdf", "Board meeting agenda - January 23, 2025", [
        "1. Approval of previous minutes.",
        "2. Engineer's opinion on balcony heat pumps.",
        "3. Budget 2025: proposed monthly common charge of $235 per unit from March 1, 2025.",
        "4. Heat pump policy.",
    ]),
    ("minutes-2025-01-23.pdf", "Board meeting minutes - January 23, 2025", [
        "Present: President, Treasurer, Secretary. Quorum present. Minutes of November 7, 2024 approved 3-0.",
        "1. The Secretary presented the structural engineer's opinion, received January 15, 2025.",
        "2. Budget 2025. The proposed charge of $235 was amended. Motion: the monthly common charge is set at $225 per unit, effective March 1, 2025. Motion carried 3-0.",
        "3. Heat pumps. Motion: heat pump outdoor units are permitted on balconies with written board approval, provided they are floor-mounted and not attached to the railing, and have a rated sound level of no more than 60 dB(A). Motion carried 2-1.",
    ]),
    ("notice-2025-02-10-fees.pdf", "Notice to residents - Common charges 2025", [
        "Dated February 10, 2025.",
        "From March 1, 2025 the monthly common charge will be $230 per unit.",
    ]),
    ("minutes-2025-04-15.docx", "Board meeting minutes - April 15, 2025", [
        "Present: President, Treasurer, Secretary. Quorum present. Minutes of January 23, 2025 approved 3-0.",
        "1. Correction. The Treasurer reported that the notice of February 10, 2025 stating $230 was in error. The adopted charge is $225 per unit. A correction was sent to all owners.",
        "2. Pets. Motion: amend House Rule 4 so that each unit may keep a maximum of two (2) pets; the 35-pound limit for dogs is removed; registration with management is still required. Effective immediately. Motion carried 3-0.",
        "3. Leasing. Motion: amend House Rule 8 so that the minimum lease term is thirty (30) days. Effective immediately. Motion carried 2-1.",
        "4. Leasing. Motion: permit leases of seven (7) days or more. Motion failed 1-2.",
    ]),
    ("minutes-2025-09-10.pdf", "Board meeting minutes - September 10, 2025", [
        "Present: President, Treasurer, Secretary. Quorum present. Minutes of April 15, 2025 approved 3-0.",
        "1. Officers. The Treasurer resigned. The board appointed a new Treasurer to serve until the next annual meeting. Motion carried 3-0.",
        "2. Pool. Motion: for the 2026 season the pool is open 8:00 a.m. to 10:00 p.m. daily. Motion carried 3-0.",
        "3. Parking. Motion: amend House Rule 9 so that guest vehicles may stay in guest parking for no more than 48 hours. Effective October 1, 2025. Motion carried 3-0.",
        "4. Landscaping. Motion: the Association will not renew the Bramblewick Grounds agreement at the end of its term. The Secretary is to send written notice of non-renewal by January 30, 2026. Motion carried 3-0.",
    ]),
    ("newsletter-2025-12.pdf", "Harbor View News - December 2025", [
        "Holiday party in the community room on December 13. Pets welcome!",
        "Many of you have asked whether charges will rise to $250 next year. The board will discuss the 2026 budget in January.",
        "The pool is closed for the winter.",
    ]),
    ("minutes-2026-01-20.pdf", "Board meeting minutes - January 20, 2026", [
        "Present: President, Treasurer, Secretary. Quorum present. Minutes of September 10, 2025 approved 3-0.",
        "1. Budget 2026. Motion: the monthly common charge is set at $240 per unit, effective March 1, 2026. Motion carried 3-0.",
        "2. Electric vehicle charging. Motion: owners may install an electric vehicle charger in their assigned parking space with written board approval, installed by a licensed electrician at the owner's cost. Motion carried 3-0.",
    ]),
    ("email-2026-02-02-landscaping.txt", None, [
        "From: secretary@harborview.example",
        "To: office@bramblewick.example",
        "Date: February 2, 2026",
        "Subject: Notice of non-renewal - landscaping agreement",
        "",
        f"Please accept this message as written notice that {ASSOC} will not renew the Landscaping Services Agreement that ends on March 31, 2026.",
        "",
        "Secretary, on behalf of the Board",
    ]),
    ("notice-2026-05-01-pool.pdf", "Notice to residents - Pool season 2026", [
        "Dated May 1, 2026.",
        "The pool opens on June 1, 2026. Hours: 8:00 a.m. to 9:00 p.m. daily.",
    ]),
]

LATER_DOCS = [
    ("minutes-2026-09-15.docx", "Board meeting minutes - September 15, 2026", [
        "Present: President, Treasurer, Secretary. Quorum present. Minutes of January 20, 2026 approved 3-0.",
        "1. Quiet hours. Motion: amend House Rule 6 so that quiet hours on Friday and Saturday nights are 11:00 p.m. to 7:00 a.m. Quiet hours on all other nights remain 10:00 p.m. to 7:00 a.m. Effective October 1, 2026. Motion carried 3-0.",
    ]),
]


def write_pdf(path, title, paras):
    styles = getSampleStyleSheet()
    story = [Paragraph(title, styles["Title"]), Spacer(1, 8)]
    for p in paras:
        style = styles["Heading3"] if p.startswith("PART ") else styles["BodyText"]
        story.append(Paragraph(p, style))
        story.append(Spacer(1, 4))
    doc = SimpleDocTemplate(str(path), pagesize=A4, title=title, author=ASSOC)
    doc.build(story)


def write_docx(path, title, paras):
    d = Document()
    d.core_properties.title = title
    d.core_properties.author = ASSOC
    d.add_heading(title, level=1)
    for p in paras:
        d.add_paragraph(p)
    d.save(str(path))


def write_any(folder, name, title, paras):
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    if name.endswith(".pdf"):
        write_pdf(path, title, paras)
    elif name.endswith(".docx"):
        write_docx(path, title, paras)
    else:
        path.write_text("\n".join(paras) + "\n", encoding="utf-8")
    return path


def main():
    for name, title, paras in DOCS:
        write_any(BOARD, name, title, paras)
    for name, title, paras in LATER_DOCS:
        write_any(LATER, name, title, paras)
    for folder in (BOARD, LATER):
        for f in sorted(folder.iterdir()):
            print(f"{f.relative_to(HERE)}  {f.stat().st_size} bytes")


if __name__ == "__main__":
    os.chdir(HERE)
    main()
