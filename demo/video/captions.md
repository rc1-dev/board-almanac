# Demo video: shot list and captions

The video is silent with burnt-in captions. Each line is one held shot of the demo page (`docs/index.html`), filmed by `film.js` and encoded by `encode.sh`.

Rebuild:

```bash
python3 demo/build_demo.py
node demo/video/film.js docs/index.html /tmp/shots [path/to/node_modules/@fontsource]
demo/video/encode.sh /tmp/shots demo/video/almanac-demo.mp4
```

## Captions

- The board folder: 16 files from 2019 to 2026. Bylaws, minutes, notices, a contract, an email and a meeting recording.
- Some files are traps. This notice says the fee is EUR 230. The board adopted EUR 225.
- This notice says the pool closes at 21:00. The board minutes say 22:00.
- A recorded discussion with no vote. It must not change a rule.
- Compile, version 1. The Skill only delegates to UGOS experts: file-agent, document-agent and knowledge-agent.
- Each delegation shown here is quoted from SKILL.md. No CLI calls, no invented results.
- The almanac keeps one current rule per topic, with its source, its quote and every rule it replaced.
- EUR 235 was only proposed. EUR 230 was an error, corrected later. EUR 240 has been the rule since March 2026.
- When documents disagree and nothing resolves it, the almanac says so and quotes both.
- It is a plain Markdown file saved on the NAS. Readable without any AI.
- Ask: answers come only from the almanac, with the source file and the almanac version.
- A raw search can surface the wrong notice. Both answers are scored with the same answer key.
- Conditions, vote and date, straight from the compiled rule.
- Not in the documents? It says so, instead of inventing an answer.
- New minutes arrive. The next compile reads only the new file and skips the 16 unchanged ones.
- Only Friday and Saturday quiet hours changed. Version 2 is saved next to version 1; nothing is overwritten.
- The history shows exactly what was replaced, and what still applies on other nights.
- Lint finds what needs attention: an open conflict, a late contract notice, a deadline in 69 days and items never voted on.
- Step 1: look for the previous almanac. There is none, so this is a first compile.
- Step 2: inventory the folder with SHA-256 checksums. This ledger makes later updates incremental.
- Step 3: transcribe the recording on the NAS. What it says stays provisional.
- Step 4: extract claims. Every claim needs a verbatim quote and its source file.
- Step 5: reconcile. Disagreements are reported, never settled by guessing.
- Step 6: apply the supersession rules, topic by topic.
- Step 7: show the changelog and ask before saving anything.
- Step 8: create the Almanac folder, with approval.
- Step 9: save almanac v1 as a new file. Success only when the save is verified.
