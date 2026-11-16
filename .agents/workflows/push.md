---
description: Stage everything, commit with the given message, and push to origin master
---

When the user types `/push <message>`, run exactly this. No persona, no commentary beyond the report.

1. If `<message>` is empty, stop and ask for it. Do not invent one.
2. Run `git branch --show-current`. If it is not `master`, stop and say so. Never push another branch from here.
3. Run `git status --short`. Show the user a one-line summary: N modified, N new, N deleted.
4. **Deletion check (File Safety, rule 4).** If any line starts with ` D` or `D `, list those paths and ask ONE question: "These deletions will be committed. Proceed?" Wait for a yes. If none, skip this step.
5. Run, in order, stopping at the first failure:
   - `git add -A`
   - `git commit -m "<message>"` (use the message verbatim; add nothing)
   - `git push origin master`
6. Report the commit hash, the file count, and the push result.

Never use `--force`, `--no-verify` or `--amend`. If the push is rejected, report the exact error and stop; suggest `git pull --rebase origin master` but do not run it unprompted.

Note: `git add -A` also stages untracked files. `.agents/protocol.md`, `*.csv`, `*.pth` and the other `.gitignore` entries stay out.
