"""Build the Board Almanac demo page from the repository's own files.

Reads the synthetic corpus text, SKILL.md delegate lines, expected almanac
versions, answer key, reference answers and scorer results, and writes:
  demo/almanac-demo.html   page body (for the claude.ai artifact)
  docs/index.html          full HTML document (for GitHub Pages)
Run: python3 demo/build_demo.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validation"))
import build_corpus  # noqa: E402

VAL = ROOT / "validation"


def doc_type(name):
    for prefix, t in [("bylaws", "bylaws"), ("minutes", "minutes"), ("notice", "notice"),
                      ("contract", "contract"), ("agenda", "agenda"), ("newsletter", "newsletter"),
                      ("email", "email"), ("board-meeting", "recording")]:
        if name.startswith(prefix):
            return t
    return "other"


def doc_date(name):
    m = re.search(r"(\d{4}-\d{2}(?:-\d{2})?)", name)
    return m.group(1) if m else ""


def recording_transcript():
    text = (VAL / "recording-script-2026-06.md").read_text(encoding="utf-8")
    body = text.split("---")[1]
    lines = [re.sub(r"\*\*(.+?):\*\*", r"\1:", l).strip() for l in body.strip().splitlines() if l.strip()]
    return lines


def files():
    out = []
    for name, title, paras in build_corpus.DOCS:
        out.append({"name": name, "type": doc_type(name), "date": doc_date(name),
                    "title": title or "Email", "paras": paras, "phase": 1})
    out.append({"name": "board-meeting-2026-06-18.m4a", "type": "recording", "date": "2026-06-18",
                "title": "Board meeting recording (transcript)", "paras": recording_transcript(), "phase": 1})
    for name, title, paras in build_corpus.LATER_DOCS:
        out.append({"name": name, "type": doc_type(name), "date": doc_date(name),
                    "title": title, "paras": paras, "phase": 2})
    if "bylaws" in out[0]["name"]:
        out[0]["date"] = "2019-05-01"
    for f in out:
        if f["name"].startswith("contract"):
            f["date"] = "2024-01-25"
    return out


def delegates():
    skill = (ROOT / "skill" / "almanac" / "SKILL.md").read_text(encoding="utf-8")
    found = re.findall(r"`(delegate --target (\S+) --instruction '([^`]*)')`", skill)
    return [{"agent": a, "instruction": i} for _, a, i in found]


def score(path, recording=False):
    cmd = [sys.executable, str(VAL / "score.py"), str(path), "--json"]
    if recording:
        cmd.append("--recording")
    res = json.loads(subprocess.run(cmd, capture_output=True, text=True, check=False).stdout)  # exit 1 means some answers failed
    return {r["id"]: r for r in res["results"]}


def jsonl(path):
    return {json.loads(l)["id"]: json.loads(l)["answer"]
            for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()}


def ask():
    key = json.loads((VAL / "answer_key.json").read_text(encoding="utf-8"))
    gold = jsonl(VAL / "selftest" / "gold_answers.jsonl")
    raw = jsonl(VAL / "selftest" / "raw_search_example.jsonl")
    gs = score(VAL / "selftest" / "gold_answers.jsonl", recording=True)
    rs = score(VAL / "selftest" / "raw_search_example.jsonl")
    out = []
    for q in key["questions"]:
        if q["phase"] not in ("initial", "after_update"):
            continue  # adversarial cases are described in the validation kit, not the demo
        i = q["id"]
        item = {"id": i, "q": q["question"], "phase": q["phase"], "almanac": gold[i],
                "almanacScore": gs[i]["pass"]}
        if i in raw:
            item["raw"] = raw[i]
            item["rawProblems"] = rs[i]["problems"]
        out.append(item)
    return out


def main():
    data = {
        "files": files(),
        "delegates": delegates(),
        "almanac": {
            "v1": (VAL / "expected-almanac-v1.md").read_text(encoding="utf-8"),
            "v2": (VAL / "expected-almanac-v2.md").read_text(encoding="utf-8"),
        },
        "ask": ask(),
    }
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    tpl = (ROOT / "demo" / "template.html").read_text(encoding="utf-8")
    body = tpl.replace("/*DATA*/null", blob)
    (ROOT / "demo" / "almanac-demo.html").write_text(body, encoding="utf-8")

    head_end = body.index("</style>") + len("</style>")
    head, rest = body[:head_end], body[head_end:]
    full = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            + head + "\n</head>\n<body>\n" + rest + "\n</body>\n</html>\n")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "index.html").write_text(full, encoding="utf-8")
    print("files", len(data["files"]), "delegates", len(data["delegates"]), "questions", len(data["ask"]),
          "bytes", len(full))


if __name__ == "__main__":
    main()
