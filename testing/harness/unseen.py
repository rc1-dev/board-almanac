"""The unseen scenario: a small tennis club, not mentioned anywhere in the Skill.

It combines a correction, a partial amendment, a failed motion and a notice that
contradicts the adopted rules. Written by Claude, who also wrote the Skill, so it is
not fully independent; see the results report.
"""
import sys
from pathlib import Path
import os  # noqa: E402
sys.path.insert(0, os.path.join(os.environ.get("ALMANAC_REPO", "/home/claude/board-almanac"), "validation"))
try:
    from build_corpus import write_any  # noqa: E402  (only needed to regenerate unseen/board)
except ImportError:
    write_any = None
from records import R  # noqa: E402

CLUB = "Maple Court Tennis Club"
DOCS = [
 ("club-rules-2022.pdf", f"{CLUB} - Club Rules", [
   "Adopted at the members' meeting of March 1, 2022. Effective March 1, 2022.",
   "Rule 1. Court booking. A member may book a court for no more than two hours per day.",
   "Rule 2. Guests. Each guest pays a fee of $10 per visit.",
   "Rule 3. Court hours. Courts are open from 7:00 a.m. to 9:00 p.m. every day.",
   "Rule 4. Amendments. These rules may be amended by a majority vote of the committee.",
 ]),
 ("committee-minutes-2024-03-05.docx", "Committee meeting minutes - March 5, 2024", [
   "Present: Chair, Treasurer, Secretary, Courts Officer. Quorum present.",
   "1. Guest fee. Motion: the guest fee is raised to $15 per visit, effective April 1, 2024. Motion carried 3-1.",
   "2. Weekend booking. Motion: amend Rule 1 so that on Saturdays and Sundays a member may book a court for no more than 90 minutes per day. Weekday booking is unchanged. Effective April 1, 2024. Motion carried 4-0.",
   "3. Court hours. Motion: extend court hours to 10:00 p.m. Motion failed 2-2.",
 ]),
 ("notice-2024-03-20.txt", None, [
   "Notice to members",
   "Dated March 20, 2024.",
   "From April 1, 2024 the guest fee is $12 per visit.",
   "Courts are now open from 7:00 a.m. to 10:00 p.m.",
 ]),
 ("committee-minutes-2024-06-11.docx", "Committee meeting minutes - June 11, 2024", [
   "Present: Chair, Treasurer, Secretary, Courts Officer. Quorum present. Minutes of March 5, 2024 approved 4-0.",
   "1. Correction. The Secretary reported that the notice of March 20, 2024 misstated the guest fee. The adopted guest fee is $15 per visit.",
 ]),
]

RECORDS = {
 "club-rules-2022.pdf": [
  R("Governance and amendments", "adoption of club rules", "club", "Adopted at members' meeting", "adopted", "bylaws", "2022-03-01", "Adopted at the members' meeting of March 1, 2022. Effective March 1, 2022.", eff="2022-03-01"),
  R("Court booking", "daily booking limit", "every day", "No more than two hours per day", "adopted", "bylaws", "2022-03-01", "A member may book a court for no more than two hours per day.", eff="2022-03-01"),
  R("Guest fees", "guest fee", "per visit", "$10", "adopted", "bylaws", "2022-03-01", "Each guest pays a fee of $10 per visit.", eff="2022-03-01"),
  R("Court hours", "court opening hours", "every day", "7:00 a.m. to 9:00 p.m.", "adopted", "bylaws", "2022-03-01", "Courts are open from 7:00 a.m. to 9:00 p.m. every day.", eff="2022-03-01"),
  R("Governance and amendments", "rule amendment threshold", "club rules", "Majority vote of the committee", "adopted", "bylaws", "2022-03-01", "These rules may be amended by a majority vote of the committee.", eff="2022-03-01"),
 ],
 "committee-minutes-2024-03-05.docx": [
  R("Governance and amendments", "attendance and quorum", "meeting", "Quorum present", "informational", "minutes", "2024-03-05", "Present: Chair, Treasurer, Secretary, Courts Officer. Quorum present."),
  R("Guest fees", "guest fee", "per visit", "$15", "adopted", "minutes", "2024-03-05", "the guest fee is raised to $15 per visit, effective April 1, 2024. Motion carried 3-1.", eff="2024-04-01", vote="3-1"),
  R("Court booking", "weekend booking limit", "Saturdays and Sundays", "No more than 90 minutes per day", "adopted", "minutes", "2024-03-05", "on Saturdays and Sundays a member may book a court for no more than 90 minutes per day. Weekday booking is unchanged.", eff="2024-04-01", vote="4-0"),
  R("Court hours", "extend court hours to 10:00 p.m.", "every day", "Motion failed", "failed", "minutes", "2024-03-05", "extend court hours to 10:00 p.m. Motion failed 2-2.", vote="2-2"),
 ],
 "notice-2024-03-20.txt": [
  R("Guest fees", "guest fee", "per visit", "$12 from April 1, 2024", "informational", "notice", "2024-03-20", "From April 1, 2024 the guest fee is $12 per visit.", eff="2024-04-01"),
  R("Court hours", "court opening hours", "every day", "7:00 a.m. to 10:00 p.m.", "informational", "notice", "2024-03-20", "Courts are now open from 7:00 a.m. to 10:00 p.m."),
 ],
 "committee-minutes-2024-06-11.docx": [
  R("Governance and amendments", "approval of previous minutes", "meeting", "Minutes of March 5, 2024 approved 4-0", "informational", "minutes", "2024-06-11", "Minutes of March 5, 2024 approved 4-0.", vote="4-0"),
  R("Guest fees", "correction of March 20 notice", "per visit", "Notice misstated the fee; adopted fee is $15", "adopted", "minutes", "2024-06-11", "the notice of March 20, 2024 misstated the guest fee. The adopted guest fee is $15 per visit."),
 ],
}

RECONCILE = [
 {"type": "disagreement", "topic": "Guest fees", "a": ["committee-minutes-2024-03-05.docx", "the guest fee is raised to $15 per visit, effective April 1, 2024."], "b": ["notice-2024-03-20.txt", "From April 1, 2024 the guest fee is $12 per visit."]},
 {"type": "correction", "topic": "Guest fees", "a": ["committee-minutes-2024-06-11.docx", "the notice of March 20, 2024 misstated the guest fee. The adopted guest fee is $15 per visit."], "b": ["notice-2024-03-20.txt", "From April 1, 2024 the guest fee is $12 per visit."]},
 {"type": "amendment", "topic": "Guest fees", "a": ["committee-minutes-2024-03-05.docx", "the guest fee is raised to $15 per visit, effective April 1, 2024."], "b": ["club-rules-2022.pdf", "Each guest pays a fee of $10 per visit."]},
 {"type": "amendment", "topic": "Court booking", "a": ["committee-minutes-2024-03-05.docx", "on Saturdays and Sundays a member may book a court for no more than 90 minutes per day."], "b": ["club-rules-2022.pdf", "A member may book a court for no more than two hours per day."]},
 {"type": "disagreement", "topic": "Court hours", "a": ["club-rules-2022.pdf", "Courts are open from 7:00 a.m. to 9:00 p.m. every day."], "b": ["notice-2024-03-20.txt", "Courts are now open from 7:00 a.m. to 10:00 p.m."]},
]


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "unseen" / "board"
    for name, title, paras in DOCS:
        write_any(out, name, title, paras)
    print(sorted(p.name for p in out.iterdir()))
