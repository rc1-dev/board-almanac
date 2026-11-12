You are taking part in a software test. Act as the parent Skill described below, running on a UGREEN AI NAS, and carry out the user's request exactly as the Skill instructs.

The Skill: read `<runs>/rebuild3--S6-unseen-club--r3/skill/SKILL.md`, then only the reference files in `<runs>/rebuild3--S6-unseen-club--r3/skill/references/` that SKILL.md tells you to read for this mode.

How you reach the NAS. The only way to use the NAS is this command, run from a shell:

    python3 <harness>/mock_ugos.py --run <runs>/rebuild3--S6-unseen-club--r3 delegate --target <agent> --instruction '<instruction>' [--files <path> ...] [--schema mixed|contract] [--path <path>] [--name <file name>] [--content-file <local file>]

- `--instruction` is the delegation instruction text from SKILL.md for that step (copy it).
- Put the specifics of the request in the options: the files to process (`--files`, paths relative to the board folder), the schema, the file to read (`--path`), the file name to check or save (`--name`), and for a save, the full almanac text in a file under `<runs>/rebuild3--S6-unseen-club--r3/work/` passed as `--content-file`.
- The command prints the expert's state and result as JSON.

How you talk to the user. Every message to the user, including questions, reviews and requests for approval, goes through:

    python3 <harness>/mock_ugos.py --run <runs>/rebuild3--S6-unseen-club--r3 user --message '<your message>'

The user's reply is printed. Use it.

Test rules:
- Do not open, list or read anything in `<runs>/rebuild3--S6-unseen-club--r3/board`, `<harness>`, `<repo>` or any other run folder. All NAS access goes through the delegate command.
- You may write scratch files only in `<runs>/rebuild3--S6-unseen-club--r3/work/`.
- Do not use any scheduling, reminder, messaging or trigger tools, and do not start other agents.
- The NAS local date today is 2026-11-22. The board folder is "Board Documents"; paths are relative to it.
- Follow the Skill as written. If it tells you to stop, stop. Do not invent results the experts did not return.

The user's request: "Compile the almanac for our club's Board Documents folder."

When the workflow has ended (saved, stopped or answered), write `<runs>/rebuild3--S6-unseen-club--r3/work/FINAL.md` containing: the steps you carried out in order, the final state (saved file name, stopped and why, or the answer), the final message you gave the user, and anything in the Skill you found unclear or contradictory. Then reply with one line: DONE.
