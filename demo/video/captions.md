# Demo video: captions and rebuild

The video has no narration. Each caption below is one held shot of the demo page (`docs/index.html`). `film.js` films the shots and `encode.sh` assembles them. The video opens with outcomes (the fee history, a change to part of a rule, an unresolved conflict) and then shows how a compile runs.

```bash
python3 demo/build_demo.py
node demo/video/film.js docs/index.html /tmp/shots [path/to/node_modules/@fontsource]
demo/video/encode.sh /tmp/shots demo/video/almanac-demo.mp4
```

## Captions

- This board's documents give three different monthly fees: $230 in a notice, $235 on an agenda and $240 in the latest minutes.
- Almanac records which one is in force, who set it and when, quoting the minutes.
- The $235 proposal was never adopted, and the $230 notice was corrected by the board. $240 has applied since March 1, 2026.
- Questions are answered from the almanac. A search of the raw folder can return the corrected notice instead.
- New minutes change quiet hours on Friday and Saturday nights only. The next compile processes that file and skips the 16 unchanged ones.
- Version 2 applies 11:00 p.m. to those two nights and keeps 10:00 p.m. for every other night, with the earlier rule recorded.
- When documents disagree and nothing resolves it, the almanac quotes both and leaves the decision to the board.
- The test archive holds 16 files from 2019 to 2026, including a meeting recording that ended without a vote.
- On the NAS, the Skill is designed to delegate every step of a compile to the UGOS agents.
- The folder is inventoried with checksums, so later compiles process only new or changed files.
- Decisions are extracted with a quotation and source file. A recording can only create provisional items.
- Sources are reconciled against each other, and disagreements are reported for the board to resolve.
- The user reviews each changed rule and its quotation before anything is saved.
- The new version is saved beside the old one and read back to confirm it is complete.
- The heat-pump answer gives the conditions, the vote and the date.
- When the documents do not cover a question, the answer says so.
- Lint lists what needs attention: an open conflict, a late contract notice, a deadline in 69 days and items that were never voted on.
- The almanac itself is a plain Markdown file on the NAS, readable without any special software.
