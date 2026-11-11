"""Per-run workload: expert calls, documents sent to extraction, failed calls, user messages, almanac size."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
rows = []
for r in json.loads((ROOT / "runs" / "index.json").read_text()):
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
(ROOT / "results" / "metrics.json").write_text(json.dumps(rows, indent=1))
print(f"{'run':<50} calls fail docs user bytes")
for x in rows:
    print(f"{x['run']:<50} {x['expert_calls']:>5} {x['failed_calls']:>4} {x['docs_extracted']:>4} {x['user_messages']:>4} {x['newest_almanac_bytes']:>6}")
