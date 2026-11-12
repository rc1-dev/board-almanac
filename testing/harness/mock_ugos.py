"""Stand-in for the UGOS expert agents, for testing the almanac Skill without a NAS.

This is an external test tool. It is not part of the Skill package.

Usage:
  python3 mock_ugos.py --run RUN delegate --target AGENT --instruction TEXT
         [--files PATH ...] [--schema mixed|contract] [--path PATH] [--name NAME] [--content-file FILE]
  python3 mock_ugos.py --run RUN user --message-file FILE   (or --message TEXT)

RUN is a run folder holding board/ (the board folder), scenario.json and trace.jsonl.
Paths are relative to the board folder. Every call is appended to trace.jsonl.

The stand-in answers only for the files named in a request, reads the files on disk to
decide what they contain, and can inject failures listed in scenario.json.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import records as base  # noqa: E402
import unseen  # noqa: E402

AUDIO = {".m4a", ".mp3", ".wav"}
ALMANAC_DIR = "Almanac"


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def text_of(p: Path):
    try:
        if p.suffix == ".pdf":
            r = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True)
            if r.returncode != 0 or not r.stdout.strip():
                return None
            return r.stdout
        if p.suffix == ".docx":
            from docx import Document
            return "\n".join(par.text for par in Document(str(p)).paragraphs)
        if p.suffix in (".txt", ".md"):
            return p.read_text(encoding="utf-8")
    except Exception:
        return None
    return None


def contains(text, quote):
    t = norm(text).replace("’", "'")
    q = norm(quote).replace("’", "'")
    # tolerate line wrapping in PDF text
    return q in t or q.replace(" ", "") in t.replace(" ", "")


def all_records():
    out = {}
    for src in (base.RECORDS, base.EXTRA, unseen.RECORDS):
        for k, v in src.items():
            out.setdefault(k, []).extend(v)
    for k, v in base.VARIANTS.items():
        out.setdefault(k.split("#")[0], []).extend(v)
    return out


def all_pairs():
    return base.RECONCILE + unseen.RECONCILE


class Run:
    def __init__(self, run):
        self.dir = Path(run)
        self.board = self.dir / "board"
        self.scn = json.loads((self.dir / "scenario.json").read_text())
        self.state_path = self.dir / "state.json"
        self.state = json.loads(self.state_path.read_text()) if self.state_path.exists() else {"calls": 0, "extract_calls": 0, "reconcile_calls": 0}

    def save_state(self):
        self.state_path.write_text(json.dumps(self.state))

    def trace(self, entry):
        self.state["calls"] += 1
        entry["n"] = self.state["calls"]
        with open(self.dir / "trace.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")

    def resolve(self, rel):
        rel = rel.strip().lstrip("/")
        for prefix in ("Board Documents/", "board/"):
            if rel.startswith(prefix):
                rel = rel[len(prefix):]
        p = (self.board / rel).resolve()
        if not str(p).startswith(str(self.board.resolve())):
            raise ValueError("path outside the board folder")
        return p

    # ---------- file-agent ----------
    def inventory(self, with_hash):
        files = []
        for p in sorted(self.board.rglob("*")):
            if p.is_file() and ALMANAC_DIR not in p.relative_to(self.board).parts:
                st = p.stat()
                row = {"path": p.relative_to(self.board).as_posix(), "type": p.suffix.lstrip("."), "size": st.st_size,
                       "modified": __import__("datetime").datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")}
                if with_hash:
                    row["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
                files.append(row)
        return files

    def almanacs(self):
        d = self.board / ALMANAC_DIR
        if not d.exists():
            return []
        found = []
        for p in d.glob("almanac-*.md"):
            m = re.search(r"-v(\d+)\.md$", p.name)
            found.append((int(m.group(1)) if m else 0, p))
        return sorted(found)

    def file_agent(self, instr, a):
        il = instr.lower()
        if "create the almanac folder" in il:
            d = self.board / ALMANAC_DIR
            existed = d.exists()
            d.mkdir(exist_ok=True)
            return "completed", {"created": not existed, "approval": "gateway approval granted by the user"}
        if "check whether a file" in il:
            name = a.name or ""
            p = self.board / ALMANAC_DIR / name
            return "completed", {"name": name, "exists": "yes" if p.exists() else "no"}
        listing = ("list" in il and ("board folder" in il or "every file" in il))
        if a.path and (listing or self.resolve(a.path).is_dir()):
            a.path = None  # a folder given as --path: treat the request as being about that folder
        if a.path:
            p = self.resolve(a.path)
            if not p.exists():
                return "failed", {"error": f"not found: {a.path}"}
            t = p.read_text(encoding="utf-8", errors="replace")
            res = {"path": a.path, "size": p.stat().st_size}
            if "last 4000" in il:
                res["last_4000_characters"] = t[-4000:]
            else:
                res["parts"] = [t[i:i + 4000] for i in range(0, len(t), 4000)]
                res["read_completely"] = True
            return "completed", res
        res = {}
        if "list" in il and ("board folder" in il or "every file" in il):
            res["files"] = self.inventory(with_hash=("sha-256" in il or "checksum" in il))
        if "almanac-" in il:
            alms = self.almanacs()
            res["almanac_files"] = [{"path": p.relative_to(self.board).as_posix(), "size": p.stat().st_size} for _, p in alms]
            if alms:
                v, p = alms[-1]
                t = p.read_text(encoding="utf-8")
                res["highest_version_path"] = p.relative_to(self.board).as_posix()
                if "completely" in il:
                    res["parts"] = [t[i:i + 4000] for i in range(0, len(t), 4000)]
                else:
                    res["first_4000_characters"] = t[:4000]
                    for title in ("Sources", "Open items"):
                        if title.lower() in il:
                            m = re.search(rf"\n## {title}\n(.*?)(?=\n## |\Z)", t, re.S)
                            res[title.lower().replace(" ", "_") + "_section"] = (f"## {title}\n" + m.group(1)) if m else ""
            else:
                res["highest_version_path"] = None
        if not res:
            return "failed", {"error": "request not understood by file-agent stand-in"}
        return "completed", res

    # ---------- document-agent ----------
    def document_agent(self, instr, a):
        il = instr.lower()
        files = a.files or []
        if "reconcile" in il:
            self.state["reconcile_calls"] += 1
            if len(files) > 60:
                return "failed", {"error": "max-files is 60 by default; request had %d files" % len(files)}
            if self.scn.get("reconcile_malformed_once") and self.state["reconcile_calls"] == 1:
                return "completed", "<<partial stream>> {\"disagreements\": [ {\"topic\": \"Pool and amen"
            names = {Path(f).name: f for f in files}
            texts = {n: text_of(self.resolve(f)) for n, f in names.items()}
            found = []
            for pr in all_pairs():
                fa, qa = pr["a"]; fb, qb = pr["b"]
                if fa in names and fb in names and texts.get(fa) and texts.get(fb) and contains(texts[fa], qa) and contains(texts[fb], qb):
                    found.append({"type": pr["type"], "topic": pr["topic"], "statement_a": {"file": names[fa], "quote": qa}, "statement_b": {"file": names[fb], "quote": qb}})
            return "completed", {"findings": found}
        if "answer the question" in il:
            if not a.path:
                return "failed", {"error": "no almanac file supplied"}
            p = self.resolve(a.path)
            return "completed", {"whole_file_read": True, "almanac_text": p.read_text(encoding="utf-8"),
                                 "note": "Stand-in limitation: returns the almanac text; the answer must be composed from it."}
        if "extract" in il:
            self.state["extract_calls"] += 1
            if len(files) > 60:
                return "failed", {"error": "max-files is 60 by default"}
            recs = all_records()
            out = []
            fail = set(self.scn.get("extract_fail", [])); partial = set(self.scn.get("extract_partial", [])); zero = set(self.scn.get("extract_zero", []))
            for f in files:
                n = Path(f).name
                p = self.resolve(f)
                if p.suffix in AUDIO:
                    out.append({"file": f, "status": "failed", "error": "unsupported file type for document extraction (audio)"}); continue
                if not p.exists():
                    out.append({"file": f, "status": "failed", "error": "file not found"}); continue
                t = text_of(p)
                if n in fail or t is None:
                    out.append({"file": f, "status": "failed", "error": "the document could not be read"}); continue
                seen, rows = set(), []
                pinned = self.scn.get("record_set", {}).get(n)
                for r in (base.VARIANTS[f"{n}#{pinned}"] if pinned else recs.get(n, [])):
                    key = (r["subject"], r["quote"])
                    if key not in seen and contains(t, r["quote"]):
                        seen.add(key); rows.append(dict(r, file=f))
                if n in zero:
                    rows = []
                read_all = True
                if n in partial:
                    rows = rows[: max(1, len(rows) // 2)]; read_all = False
                out.append({"file": f, "status": "completed", "read_completely": read_all, "records_found": len(rows), "records": rows,
                            "schema_used": a.schema or "auto"})
            self.mutate_if_due()
            return "completed", {"results": out}
        return "failed", {"error": "request not understood by document-agent stand-in"}

    def mutate_if_due(self):
        m = self.scn.get("mutate_after_extract_calls")
        if m and self.state["extract_calls"] == m["count"] and not self.state.get("mutated"):
            p = self.resolve(m["file"])
            with open(p, "ab") as fh:
                fh.write(m.get("append", "\n").encode())
            self.state["mutated"] = True
            self.trace({"kind": "harness", "event": f"changed {m['file']} on disk after extraction call {m['count']}"})

    # ---------- knowledge-agent ----------
    def knowledge_agent(self, instr, a):
        il = instr.lower()
        if "transcribe" in il:
            out = []
            for f in a.files or []:
                n = Path(f).name
                if n in set(self.scn.get("transcribe_fail", [])) or n not in base.TRANSCRIPTS or not self.resolve(f).exists():
                    out.append({"file": f, "status": "failed", "error": "could not transcribe"}); continue
                out.append(dict(base.TRANSCRIPTS[n], file=f, status="completed", quality_warnings=["two speakers overlap at 00:01:40"]))
            return "completed", {"results": out}
        if "save" in il:
            if not a.content_file or not a.name:
                return "failed", {"error": "save needs content and a file name hint"}
            content = Path(a.content_file).read_text(encoding="utf-8")
            d = self.board / ALMANAC_DIR
            if not d.exists():
                return "failed", {"error": "almanac folder does not exist"}
            name = a.name
            if self.scn.get("save_rename"):
                name = name.replace(".md", " (1).md")
            p = d / name
            if p.exists():
                return "failed", {"error": f"{name} already exists; nothing was written"}
            p.write_text(content, encoding="utf-8")
            return "completed", {"outputFile": f"{ALMANAC_DIR}/{name}", "contentBytes": len(content.encode()), "verified": True,
                                 "approval": "workflow approval granted by the user"}
        return "failed", {"error": "request not understood by knowledge-agent stand-in"}

    # ---------- user ----------
    def user(self, msg):
        ml = msg.lower()
        for rule in self.scn.get("user_replies", []):
            if (all(k in ml for k in rule.get("all", [])) and (not rule.get("any") or any(k in ml for k in rule["any"]))
                    and not any(k in ml for k in rule.get("none", []))):
                return rule["reply"]
        return self.scn.get("default_reply", "Yes, please continue.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("delegate")
    d.add_argument("--target", required=True)
    d.add_argument("--instruction", required=True)
    d.add_argument("--files", nargs="*")
    d.add_argument("--schema")
    d.add_argument("--path")
    d.add_argument("--name")
    d.add_argument("--content-file")
    u = sub.add_parser("user")
    u.add_argument("--message")
    u.add_argument("--message-file")
    a = ap.parse_args()
    run = Run(a.run)
    if a.cmd == "user":
        if a.message_file:
            a.message = Path(a.message_file).read_text()
        if not a.message:
            sys.exit("user: give --message-file (preferred) or --message")
        reply = run.user(a.message)
        run.trace({"kind": "user", "message": a.message, "reply": reply})
        run.save_state()
        print(json.dumps({"user_reply": reply}, indent=1))
        return
    handler = {"file-agent": run.file_agent, "document-agent": run.document_agent, "knowledge-agent": run.knowledge_agent}.get(a.target)
    try:
        state, result = handler(a.instruction, a) if handler else ("failed", {"error": f"unknown agent {a.target}"})
    except Exception as e:  # report, never crash silently
        state, result = "failed", {"error": f"{type(e).__name__}: {e}"}
    summary = result if isinstance(result, str) else {k: (v if k not in ("parts", "almanac_text", "first_4000_characters", "sources_section", "last_4000_characters") else f"<{len(str(v))} chars>") for k, v in result.items()}
    if isinstance(summary, dict) and "results" in summary:
        summary["results"] = [{k: v for k, v in r.items() if k != "records"} | ({"records": len(r.get("records", []))} if "records" in r else {}) for r in summary["results"]]
    run.trace({"kind": "delegate", "target": a.target, "instruction": a.instruction, "files": a.files, "schema": a.schema,
               "path": a.path, "name": a.name, "content_file": a.content_file, "state": state, "result": summary})
    run.save_state()
    print(json.dumps({"state": state, "result": result}, indent=1))


if __name__ == "__main__":
    main()
