# Demo video: captions and rebuild

The video has no narration. It opens with three title cards: the name, the problem, and the problem graphic (`docs/search-vs-almanac.svg`), shown first with only the search results and then with the almanac beside them. Each caption below is one held shot of the demo page (`docs/index.html`), filmed above a caption band so the caption never covers the page. `film.js` films the shots and `encode.sh` assembles them. After the fee history, the video shows a change to part of a rule and an unresolved conflict, then how a compile runs.

```bash
python3 demo/build_demo.py
node demo/video/film.js docs/index.html /tmp/shots [path/to/node_modules/@fontsource]
demo/video/encode.sh /tmp/shots demo/video/almanac-demo.mp4
```

## Captions

- Almanac records the fee in force, the vote that set it and its effective date, quoting the minutes.
- The $235 proposal was never adopted, and the $230 notice was corrected by the board. $240 has applied since March 1, 2026.
- Questions are answered from the almanac. A search of the raw folder can return the corrected notice instead.
- New minutes change quiet hours on Friday and Saturday nights only. The next compile reads every document again and builds version 2 from them.
- Version 2 applies 11:00 p.m. to those two nights and keeps 10:00 p.m. for every other night, with the earlier rule recorded.
- When documents disagree and no later document settles it, the almanac quotes both and leaves the decision to the board. The 2019 hours still apply to other seasons.
- The test archive holds 16 files from 2019 to 2026, including a meeting recording that ended without a vote.
- On the NAS, the Skill is designed to delegate every step of a compile to the UGOS agents.
- The folder is listed with checksums. Every compile reads every document again, so a corrected or deleted file cannot leave an outdated rule behind.
- Decisions are extracted with a quotation and source file. A recording can only create provisional items.
- Sources are reconciled against each other, and disagreements are reported for the board to resolve.
- Before anything is saved, the user reviews each new or changed rule with its quotation.
- The folder is checked again before saving. If a file changed during the compile, nothing is saved.
- The new version is saved beside the old one and read back to confirm it is complete.
- The heat-pump answer gives the conditions, the vote and the date.
- When the documents do not cover a question, the answer says so.
- Lint lists what needs attention: an open conflict, a late contract notice, a deadline in 69 days and items that were never voted on.
- The almanac itself is a plain Markdown file on the NAS, readable without any special software.
