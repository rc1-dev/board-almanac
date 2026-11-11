"""Create one run folder per (version, scenario, repeat)."""
import hashlib, json, os, re, shutil, subprocess, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = Path(os.environ.get("ALMANAC_REPO", "/home/claude/board-almanac"))  # only needed to set up runs
CORPUS = REPO / "validation" / "corpus"
BOARD_SRC = CORPUS / "Board Documents"
ADV = CORPUS / "adversarial"
UNSEEN = ROOT / "unseen" / "board"
HERE_DIR = Path(__file__).resolve().parent

APPROVE = "Approved. Please save it."
CONFIRM = ("Yes. The board folder is 'Board Documents' (paths are relative to it), the almanac folder is 'Almanac' inside it, "
           "and the NAS is set to use its local model. Please go ahead.")
SAVE_Q = ["approve saving", "approve the save", "save almanac-", "saving almanac-", "reply yes to save", "save this version", "misread", "which passage"]
REPLIES = [
    {"all": ["exclude"], "any": ["fix", "replace", "which do you choose", "or exclude"], "none": SAVE_Q,
     "reply": "I can't fix that file now. Exclude it and continue."},
    {"all": ["model"], "any": ["board folder", "almanac folder", "model route", "which model"], "none": SAVE_Q, "reply": CONFIRM},
    {"any": ["approve", "approval", "save this", "shall i save", "should i save", "confirm saving", "ok to save", "go ahead and save", "reply 'save'", "reply \"save\"", "want me to save", "may i save", "reply yes to save"], "reply": APPROVE},
    {"any": [" (1).md"], "reply": "Leave that file as it is. I will check it myself."},
    {"any": ["new compile", "compile again", "start again", "restart the compile"], "reply": "Yes, compile again from the current files."},
    {"any": ["empty"], "reply": "Yes, that is the right folder."},
]


def skill_files(version):
    out = ROOT / "candidates" / version / "almanac"
    if out.exists():
        return out
    out.mkdir(parents=True)
    ref = {"rebuild": "8a5473e", "rebuild2": "3f37702", "rebuild3": "bafceeb", "rebuild4": "97fdfc7", "rebuild5": "9f08a78", "baseline": "main"}[version]
    names = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", ref, "skill/almanac"], capture_output=True, text=True, check=True).stdout.split()
    for n in names:
        data = subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:{n}"], capture_output=True, check=True).stdout
        dst = out / Path(n).relative_to("skill/almanac")
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
    return out


def doc_mtime(name):
    m = re.search(r"(\d{4})-(\d{2})(?:-(\d{2}))?", name)
    if not m:
        return datetime.datetime(2026, 11, 1, 12)
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3) or 15)
    return datetime.datetime(y, mo, d, 18, 0)


def put(board, src, name=None):
    dst = board / (name or src.name)
    shutil.copy2(src, dst)
    t = doc_mtime(dst.name).timestamp()
    os.utime(dst, (t, t))


def fill_ledger(text, board):
    def row(m):
        cells = [c.strip() for c in m.group(0).strip().strip("|").split("|")]
        f = board / cells[0]
        if not f.exists():
            return m.group(0)
        st = f.stat()
        cells[3] = str(st.st_size)
        cells[4] = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")
        cells[5] = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
        return "| " + " | ".join(cells) + " |"
    return re.sub(r"^\| [^|]+\.(?:pdf|docx|txt|m4a) \|[^\n]*$", row, text, flags=re.M)


def seed(board, version_text, name, compiled):
    d = board / "Almanac"; d.mkdir(exist_ok=True)
    t = version_text.replace("Compiled: (set at compile)", f"Compiled: {compiled}").replace(
        "Compiled-through: (latest modification time of the files processed)", f"Compiled-through: {compiled}")
    t = re.sub(r"<!--.*?-->\n*", "", t, flags=re.S)
    (d / name).write_text(fill_ledger(t, board), encoding="utf-8")


def v3_text(v2):
    t = v2.replace("Version: 2", "Version: 3").replace("Sources: 17 processed", "Sources: 18 processed")
    t = t.replace("| Parking | Guest parking up to 48 hours | 2025-10-01 | none | adopted |", "| Parking | Guest parking up to 48 hours | 2025-10-01 | Up to 24 hours from 2027-01-01 | adopted |")
    t = t.replace("Superseded:\n- 2019-05-01 to 2025-10-01: Guest parking up to 72 hours.",
                  "Scheduled: from 2027-01-01, guest vehicles up to 24 hours. Set by board minutes, 2026-11-10, motion carried 3-0. Evidence: minutes-2026-11-10.docx: \"guest vehicles may stay in guest parking for no more than 24 hours. Effective January 1, 2027.\"\n\nSuperseded:\n- 2019-05-01 to 2025-10-01: Guest parking up to 72 hours.")
    t = t.replace("| minutes-2026-09-15.docx | minutes | 2026-09-15 | | | | processed |", "| minutes-2026-09-15.docx | minutes | 2026-09-15 | | | | processed |\n| minutes-2026-11-10.docx | minutes | 2026-11-10 | | | | processed |")
    t = t.replace("## Changelog\n\n", "## Changelog\n\n## v3\n- Added minutes-2026-11-10.docx. Parking: change to 24 hours scheduled from 2027-01-01; 48 hours remains current.\n\n")
    return t.replace("End of almanac v2.", "End of almanac v3.")


def base_board(board, with_amendment=False):
    for p in sorted(BOARD_SRC.iterdir()):
        put(board, p)
    rec = board / "board-meeting-2026-06-18.m4a"
    rec.write_bytes(b"ID3 synthetic placeholder for the June 2026 board meeting recording\n")
    t = doc_mtime(rec.name).timestamp(); os.utime(rec, (t, t))
    if with_amendment:
        put(board, CORPUS / "add-later" / "minutes-2026-09-15.docx")


V1 = (REPO / "validation" / "expected-almanac-v1.md").read_text()
V2 = (REPO / "validation" / "expected-almanac-v2.md").read_text()

SCENARIOS = {
 "S1-first-compile": dict(today="2026-11-22", request="Compile the almanac for the Board Documents folder."),
 "S2-weekend-amendment": dict(today="2026-11-29", request="New minutes were added. Update the almanac."),
 "S3-corrected-minutes": dict(today="2026-12-01", request="The April 2025 minutes were corrected and replaced. Update the almanac."),
 "S4-scheduled-change": dict(today="2026-12-01", request="New minutes were added. Update the almanac, then tell me how long a guest car can stay in guest parking on January 5, 2027."),
 "S5-date-passes": dict(today="2027-01-02", request="Update the almanac."),
 "S6-unseen-club": dict(today="2026-11-22", request="Compile the almanac for our club's Board Documents folder."),
 "F1-unreadable-file": dict(today="2026-11-22", request="Compile the almanac for the Board Documents folder."),
 "F2-source-changes-mid-run": dict(today="2026-11-29", request="New minutes were added. Update the almanac.",
                                    mutate_after_extract_calls={"count": 1, "file": "notice-2026-05-01-pool.pdf", "append": "\n% revised\n"}),
 "F3-malformed-reply-and-injection": dict(today="2026-11-29", request="New documents were added. Update the almanac.", reconcile_malformed_once=True),
 "F4-unexpected-save-name": dict(today="2026-11-29", request="New minutes were added. Update the almanac.", save_rename=True),
}


def build_board(sid, board):
    board.mkdir(parents=True)
    if sid == "S6-unseen-club":
        for p in sorted(UNSEEN.iterdir()):
            put(board, p)
        return
    if sid in ("S1-first-compile",):
        base_board(board); return
    if sid == "F1-unreadable-file":
        base_board(board); put(board, ADV / "failed-file" / "first-run" / "notice-2026-10-20-elevator.pdf"); return
    if sid in ("S2-weekend-amendment", "F2-source-changes-mid-run", "F4-unexpected-save-name", "F3-malformed-reply-and-injection"):
        base_board(board)
        seed(board, V1, "almanac-2026-11-22-v1.md", "2026-11-22 10:00")
        put(board, CORPUS / "add-later" / "minutes-2026-09-15.docx")
        if sid == "F3-malformed-reply-and-injection":
            put(board, ADV / "injected-instructions" / "notice-2026-10-12-laundry.txt")
        return
    base_board(board, with_amendment=True)
    seed(board, V1.replace("| minutes-2026-09-15.docx", "| x"), "almanac-2026-11-22-v1.md", "2026-11-22 10:00")
    seed(board, V2, "almanac-2026-11-29-v2.md", "2026-11-29 10:00")
    if sid == "S3-corrected-minutes":
        put(board, ADV / "corrected-minutes" / "minutes-2025-04-15.docx")
    if sid in ("S4-scheduled-change", "S5-date-passes"):
        put(board, ADV / "scheduled-change" / "minutes-2026-11-10.docx")
    if sid == "S5-date-passes":
        seed(board, v3_text(V2), "almanac-2026-12-01-v3.md", "2026-12-01 10:00")


def main(plan, only=None, index="index.json"):
    runs = []
    tpl = (HERE_DIR / "orchestrator_prompt.md").read_text()
    for version, repeats in plan.items():
        sk = skill_files(version)
        for sid, cfg in SCENARIOS.items():
            if only and sid not in only:
                continue
            for r in range(1, repeats + 1):
                rd = ROOT / "runs" / f"{version}--{sid}--r{r}"
                if rd.exists():
                    shutil.rmtree(rd)
                build_board(sid, rd / "board")
                (rd / "work").mkdir()
                shutil.copytree(sk, rd / "skill")
                scn = {"id": sid, "version": version, "repeat": r, "today": cfg["today"], "request": cfg["request"],
                       "user_replies": REPLIES, "default_reply": "Yes, please continue."}
                for k in ("mutate_after_extract_calls", "reconcile_malformed_once", "save_rename"):
                    if k in cfg:
                        scn[k] = cfg[k]
                (rd / "scenario.json").write_text(json.dumps(scn, indent=1))
                (rd / "PROMPT.md").write_text(tpl.format(run=str(rd.resolve()), harness=str(HERE_DIR / "mock_ugos.py"), harness_dir=str(HERE_DIR),
                                                       today=scn["today"], request=scn["request"]))
                runs.append(str(rd))
    (ROOT / "runs" / index).write_text(json.dumps(runs, indent=1))
    print(len(runs), "runs")


if __name__ == "__main__":
    if sys.argv[1:] == ["final"]:
        main({"rebuild5": 3}, only={"S1-first-compile"}, index="index-final-s1.json")
        main({"rebuild5": 2}, only={"S2-weekend-amendment", "F3-malformed-reply-and-injection"}, index="index-final-upd.json")
    elif sys.argv[1:] == ["retest4"]:
        main({"rebuild4": 2}, only={"S1-first-compile", "S2-weekend-amendment", "S5-date-passes", "F3-malformed-reply-and-injection"}, index="index-retest4.json")
    elif sys.argv[1:] == ["retest3"]:
        main({"rebuild3": 3}, only={"S6-unseen-club", "S1-first-compile"}, index="index-retest3.json")
    elif sys.argv[1:] == ["retest"]:
        main({"rebuild2": 2}, only={"S1-first-compile", "S2-weekend-amendment", "S5-date-passes", "S6-unseen-club",
                                    "F2-source-changes-mid-run", "F3-malformed-reply-and-injection"}, index="index-retest.json")
    else:
        main({"rebuild": 2, "baseline": 1})
