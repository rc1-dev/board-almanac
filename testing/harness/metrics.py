"""Per-run workload: expert calls, documents sent to extraction, failed calls, user messages, almanac size.
Usage: python3 metrics.py [--json FILE] [run folder ...]   (default: every run in testing/archive/runs/)
"""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
args = sys.argv[1:]
out = None
if "--json" in args:
    k = args.index("--json")
    out = args[k + 1]
    del args[k:k + 2]
runs = args or sorted(str(p) for p in (ROOT / "archive" / "runs").glob("*--*") if p.is_dir())
rows = []
for r in runs:
    rd = Path(r)
    if not (rd / "trace.jsonl").exists():
        continue
    tr = [json.loads(l) for l in (rd / "trace.jsonl").read_text().splitlines()]
    d = [t for t in tr if t.get("kind") == "delegate"]
    ext = [f for t in d if t["target"] == "document-agent" and "extract" in t["instruction"].lower() for f in (t.get("files") or [])]
    alm = sorted((rd / "board" / "Almanac").glob("almanac-*.md"), key=lambda p: p.stat().st_mtime) if (rd / "board" / "Almanac").exists() else []
    rows.append({"run": rd.name, "expert_calls": len(d), "failed_calls": sum(t["state"] != "completed" for t in d),
                 "docs_extracted": len(ext), "user_messages": sum(t.get("kind") == "user" for t in tr),
                 "newest_almanac_bytes": alm[-1].stat().st_size if alm else 0})
if out:
    Path(out).write_text(json.dumps(rows, indent=1))
print(f"{'run':<50} calls fail docs user bytes")
for x in rows:
    print(f"{x['run']:<50} {x['expert_calls']:>5} {x['failed_calls']:>4} {x['docs_extracted']:>4} {x['user_messages']:>4} {x['newest_almanac_bytes']:>6}")
