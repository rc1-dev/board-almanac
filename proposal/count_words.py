"""Count the words in the ten proposal answers, the way a strict reader would.

The rules limit "the ten substantive responses" to 500 English words in total.
Disclosures (third-party licenses and similar) are excluded. The rules do not say
whether the question headings count, so this script reports both, and the
submission should stay under 500 even with the headings included.

Methods reported:
  whitespace   - split on whitespace (what most word counters do)
  hyphen-split - also split on hyphens and slashes, so "ug-filesystem" counts as 2
                 (the strictest plausible reading)

Usage:
  python3 count_words.py                 # count the answers in proposal.py
  python3 count_words.py --pdf FILE.pdf  # count the rendered PDF between item 1 and the disclosures
"""
import re
import subprocess
import sys
from pathlib import Path


def words(text, split_hyphens=False):
    toks = text.split()
    if split_hyphens:
        toks = [t for tok in toks for t in re.split(r"[-/‐-—]", tok)]
    # a token counts as a word if it has at least one letter or digit
    return [t for t in toks if re.search(r"[A-Za-z0-9]", t)]


def answer_texts():
    sys.path.insert(0, str(Path(__file__).parent))
    import proposal  # noqa: E402
    out = []
    for heading, blocks in proposal.ITEMS:
        parts = []
        for b in blocks:
            parts.extend(b[1] if isinstance(b, tuple) else [b])
        out.append((heading, " ".join(parts)))
    return out


def report(items):
    tot = {"ws": 0, "hy": 0, "head_ws": 0, "head_hy": 0}
    print(f"{'item':<28}{'answer':>8}{'+heading':>10}{'hyphen-split':>14}")
    for heading, text in items:
        a, h = len(words(text)), len(words(heading))
        ah = len(words(text, True))
        hh = len(words(heading, True))
        tot["ws"] += a; tot["hy"] += ah; tot["head_ws"] += h; tot["head_hy"] += hh
        print(f"{heading[:27]:<28}{a:>8}{a + h:>10}{ah + hh:>14}")
    print("-" * 60)
    print(f"{'TOTAL answers only':<28}{tot['ws']:>8}")
    print(f"{'TOTAL with headings':<28}{tot['ws'] + tot['head_ws']:>18}")
    print(f"{'TOTAL with headings, strict':<28}{tot['hy'] + tot['head_hy']:>32}")
    worst = tot["hy"] + tot["head_hy"]
    print("\nLimit 500:", "OK" if worst <= 500 else f"OVER by {worst - 500} (strictest count)")
    return worst


def pdf_items(path):
    t = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True, check=True).stdout
    a, b = t.index("1. What"), t.index("Third-party")
    body = t[a:b]
    parts = re.split(r"(?m)^(\d+\. [A-Z][^\n]*)$", body)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--pdf":
        sys.exit(0 if report(pdf_items(sys.argv[2])) <= 500 else 1)
    sys.exit(0 if report(answer_texts()) <= 500 else 1)
