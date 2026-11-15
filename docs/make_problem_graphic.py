"""Draw docs/search-vs-almanac.svg: what a search of the archive returns for the
monthly fee, beside what the almanac records. Every figure, file name and
quotation comes from validation/build_corpus.py.
Run: python3 docs/make_problem_graphic.py
"""
from html import escape
from pathlib import Path

W, H = 1200, 650
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
INK, MUTED, RULE, ACCENT = "#1d2a31", "#5b6b75", "#d9e1e5", "#1f5f74"
WARN, WARN_BG = "#a64b1c", "#fbeee6"

# Search results, in the jumbled order a keyword search might return them.
SEARCH = [
    ("$230", "notice-2025-02-10-fees.pdf", "the monthly common charge will be $230 per unit"),
    ("$235", "agenda-2025-01-23.pdf", "proposed monthly common charge of $235 per unit"),
    ("$250", "newsletter-2025-12.pdf", "whether charges will rise to $250 next year"),
    ("$225", "minutes-2025-01-23.pdf", "the monthly common charge is set at $225 per unit"),
    ("$240", "minutes-2026-01-20.pdf", "the monthly common charge is set at $240 per unit"),
    ("$210", "minutes-2024-01-18.pdf", "the monthly common charge is set at $210 per unit"),
    ("$230", "minutes-2025-04-15.docx", "the notice of February 10, 2025 stating $230 was in error"),
]

# The almanac's history for the same topic, by document date, newest first.
HISTORY = [
    ("Dec 2025", "$250", "A newsletter question; sets nothing", MUTED),
    ("Feb 2025", "$230", "Notice in error; corrected Apr 15, 2025", WARN),
    ("Jan 2025", "$225", "In force Mar 2025 to Feb 2026", MUTED),
    ("Jan 2025", "$235", "Proposed on an agenda; never adopted", MUTED),
    ("Jan 2024", "$210", "In force Mar 2024 to Feb 2025", MUTED),
]


def t(x, y, s, size=14, weight=400, fill=INK, family=SANS, anchor="start", style="", extra=""):
    st = f' font-style="{style}"' if style else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}{extra}>{escape(s)}</text>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'role="img" aria-labelledby="title desc">',
         '<title id="title">Search returns every version; Almanac records which one applies</title>',
         '<desc id="desc">A search for the monthly fee in the validation archive returns seven documents '
         'giving $210, $225, $230, $235, $240 and $250. The almanac records that $240 has applied since '
         'March 1, 2026, set by the board minutes of January 20, 2026, and explains each other figure.</desc>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="#ffffff" stroke="{RULE}"/>']

    # Left: the search
    lx, top = 36, 96
    # The almanac side sits on a tinted panel so it reads as the answer.
    rx, rw = 680, 484
    o.append(f'<rect x="{rx - 22}" y="22" width="{rw + 44}" height="{H - 76}" rx="12" fill="#eef5f7" stroke="{ACCENT}" stroke-width="2"/>')
    o.append(t(lx, 56, "Search the archive", 22, 700, INK))
    o.append(t(lx, 80, "Every document that mentions the fee", 15, 400, MUTED))
    o.append(t(rx, 56, "Ask Almanac", 22, 700, ACCENT))
    o.append(t(rx, 80, "The rule that applies, with its source", 15, 400, MUTED))
    o.append(f'<rect x="{lx}" y="{top + 16}" width="540" height="40" rx="8" fill="#f4f7f8" stroke="{RULE}"/>')
    o.append(f'<circle cx="{lx + 22}" cy="{top + 35}" r="7" fill="none" stroke="{MUTED}" stroke-width="2"/>'
             f'<line x1="{lx + 27}" y1="{top + 40}" x2="{lx + 33}" y2="{top + 46}" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>')
    o.append(t(lx + 46, top + 42, "monthly common charge", 17, 500, INK))
    o.append(t(lx + 528, top + 42, "7 results", 13, 400, MUTED, anchor="end"))
    y = top + 92
    for amount, fname, quote in SEARCH:
        o.append(f'<line x1="{lx}" y1="{y - 26}" x2="{lx + 540}" y2="{y - 26}" stroke="{RULE}"/>')
        o.append(t(lx + 4, y + 2, amount, 22, 700, INK))
        o.append(t(lx + 78, y - 6, fname, 13, 500, ACCENT, MONO))
        o.append(t(lx + 78, y + 14, f"“{quote}”", 13.5, 400, MUTED, style="italic"))
        y += 60
    o.append(t(lx, y - 8, "Which one applies today?", 18, 600, WARN))

    # Arrow
    ax, ay = 598, 336
    o.append(t(ax + 24, ay - 14, "compile", 12, 500, ACCENT, MONO, anchor="middle"))
    o.append(f'<line x1="{ax}" y1="{ay}" x2="{ax + 34}" y2="{ay}" stroke="{ACCENT}" stroke-width="3"/>'
             f'<path d="M{ax + 34} {ay - 9} L{ax + 48} {ay} L{ax + 34} {ay + 9} Z" fill="{ACCENT}"/>')

    # Right: the almanac
    o.append(f'<rect x="{rx}" y="{top + 16}" width="{rw}" height="164" rx="10" fill="#ffffff" stroke="{ACCENT}" stroke-width="1.5"/>')
    o.append(t(rx + 22, top + 46, "Monthly fee", 15, 600, ACCENT))
    o.append(f'<rect x="{rx + rw - 104}" y="{top + 31}" width="84" height="22" rx="11" fill="{ACCENT}"/>')
    o.append(t(rx + rw - 62, top + 47, "IN FORCE", 11.5, 700, "#ffffff", MONO, anchor="middle"))
    o.append(t(rx + 22, top + 92, "$240 per unit per month", 30, 700, INK))
    o.append(t(rx + 22, top + 122, "Since March 1, 2026. Set by the board minutes of", 15, 400, INK))
    o.append(t(rx + 22, top + 143, "January 20, 2026, motion carried 3-0.", 15, 400, INK))
    o.append(t(rx + 22, top + 166, "“the monthly common charge is set at $240 per unit”", 13, 400, MUTED, style="italic"))

    o.append(t(rx, top + 222, "The other figures", 15, 600, INK))
    y = top + 258
    for when, amount, note, colour in HISTORY:
        o.append(f'<line x1="{rx}" y1="{y - 24}" x2="{rx + rw}" y2="{y - 24}" stroke="#c9dbe1"/>')
        o.append(t(rx, y, when, 13, 500, MUTED, MONO))
        o.append(t(rx + 92, y, amount, 17, 700, MUTED))
        o.append(f'<line x1="{rx + 91}" y1="{y - 6}" x2="{rx + 135}" y2="{y - 6}" stroke="{MUTED}" stroke-width="1.5"/>')
        if colour == WARN:
            o.append(f'<rect x="{rx + 150}" y="{y - 17}" width="{rw - 150}" height="24" rx="5" fill="{WARN_BG}"/>')
        o.append(t(rx + 160, y, note, 14.5, 500 if colour == WARN else 400, colour))
        y += 44
    o.append(t(rx, y + 8, "Each line cites its source file and quotation.", 13, 400, MUTED))

    o.append(t(W / 2, H - 18, "Synthetic validation archive: Harbor View Condominium Association (fictional)",
               12, 400, MUTED, anchor="middle"))
    o.append("</svg>")
    out = Path(__file__).with_name("search-vs-almanac.svg")
    out.write_text("\n".join(o) + "\n", encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    main()
