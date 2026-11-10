# Demo video: captions and rebuild

The video has no narration. Each caption below is one held shot of the demo page (`docs/index.html`), in the order shown. `film.js` films the shots and `encode.sh` assembles them.

```bash
python3 demo/build_demo.py
node demo/video/film.js docs/index.html /tmp/shots [path/to/node_modules/@fontsource]
demo/video/encode.sh /tmp/shots demo/video/almanac-demo.mp4
```

## Captions

- The board folder holds 16 files from 2019 to 2026, including bylaws, minutes, notices, a contract, an email and a meeting recording.
- This notice states a fee of EUR 230. The fee the board adopted was EUR 225.
- This notice gives the pool closing time as 21:00. The board minutes say 22:00.
- This recording captures a discussion that ended without a vote, so it cannot change a rule.
- Compiling version 1. The Skill delegates every step to the UGOS agents.
- Step 1. The Skill looks for a previous almanac. None exists, so this is a first compile.
- Step 2. The folder is inventoried with checksums, which makes later compiles incremental.
- Step 3. The recording is transcribed on the NAS. Anything decided only there is marked provisional.
- Step 4. Decisions are extracted, each with a quotation and its source file.
- Step 5. The sources are reconciled, and disagreements are reported for the board to resolve.
- Step 6. The supersession rules are applied topic by topic.
- Step 7. The user reviews each changed rule and its quotation before anything is saved.
- Step 8. The almanac folder is created with the user's approval.
- Step 9. Version 1 is saved, then read back to confirm it is complete.
- The delegation text is quoted directly from SKILL.md.
- Each topic shows the documented rule, its source and quotation, and every rule it replaced.
- EUR 235 was proposed but never adopted, and the EUR 230 notice was corrected. EUR 240 has applied since March 2026.
- Where documents disagree and nothing resolves the difference, the almanac quotes both.
- The almanac is a plain Markdown file on the NAS, readable without any special software.
- Answers come from the almanac and cite the source file and almanac version.
- A search of the raw folder can return the wrong notice. Both answers are scored with the same answer key.
- The heat-pump answer gives the conditions, the vote and the date.
- When the documents do not cover a question, the answer says so.
- New minutes arrive. The next compile processes the new file and skips the 16 unchanged ones.
- Only Friday and Saturday quiet hours changed. Version 2 is saved beside version 1.
- The history shows what was replaced and what still applies on other nights.
- Lint lists what needs attention: an open conflict, a late contract notice, a deadline in 69 days and items that were never voted on.
