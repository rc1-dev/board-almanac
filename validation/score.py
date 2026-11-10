"""Score answers against the Harbor View answer key. Standard library only.

Usage:
  python3 score.py answers.jsonl [--key answer_key.json] [--phase initial|after_update|all]
                   [--recording] [--json]

answers.jsonl has one JSON object per line: {"id": "Q1", "answer": "..."}.
An answer passes when every must_include entry matches, every must_cite entry
matches, and no must_not_include pattern matches. --recording also applies the
if_recording checks, for runs where the meeting recording was in the folder.
"""
import argparse
import json
import re
import sys
from pathlib import Path


def normalize(text):
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("’", "'")
    return re.sub(r"[ \t]+", " ", text)


def any_match(alternatives, text):
    return any(re.search(p, text, re.IGNORECASE | re.MULTILINE) for p in alternatives)


def score_one(q, answer, recording):
    text = normalize(answer)
    problems = []
    include = list(q.get("must_include", []))
    if recording and "if_recording" in q:
        include += q["if_recording"].get("must_include", [])
    for alts in include:
        if not any_match(alts, text):
            problems.append("missing: " + " | ".join(alts))
    for alts in q.get("must_cite", []):
        if not any_match([re.escape(a) for a in alts], text):
            problems.append("no citation: " + " | ".join(alts))
    for pat in q.get("must_not_include", []):
        if re.search(pat, text, re.IGNORECASE | re.MULTILINE):
            problems.append("forbidden: " + pat)
    return problems


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser()
    ap.add_argument("answers")
    ap.add_argument("--key", default=str(here / "answer_key.json"))
    ap.add_argument("--phase", default="all", choices=["initial", "after_update", "all"])
    ap.add_argument("--recording", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    key = json.loads(Path(args.key).read_text(encoding="utf-8"))
    answers = {}
    for n, line in enumerate(Path(args.answers).read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            row = json.loads(line)
            answers[row["id"]] = row.get("answer", "")

    results = []
    for q in key["questions"]:
        if args.phase != "all" and q["phase"] != args.phase:
            continue
        if q["id"] not in answers:
            results.append({"id": q["id"], "pass": False, "problems": ["no answer"]})
            continue
        problems = score_one(q, answers[q["id"]], args.recording)
        results.append({"id": q["id"], "pass": not problems, "problems": problems})

    passed = sum(r["pass"] for r in results)
    if args.json:
        print(json.dumps({"passed": passed, "total": len(results), "results": results}, indent=2))
    else:
        for r in results:
            mark = "PASS" if r["pass"] else "FAIL"
            print(f"{r['id']:>4}  {mark}  {'; '.join(r['problems'])}")
        print(f"\n{passed}/{len(results)} passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
