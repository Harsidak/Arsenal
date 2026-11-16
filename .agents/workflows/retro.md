---
description: Weekly review from git history and your diary: what shipped, what repeated, what to cut
---

When the user types `/retro [days]` (default 7), shift context to **@vanguard**. This replaces a MISTAKES file: mistakes live in the user's diary, and this command reads them.

### Execution Sequence:

1. Gather evidence:
   - `git log --since="<days> days ago" --stat --pretty=format:"%h %ad %s" --date=short`
   - Ask the user to paste this period's diary entries (or give a path). Wait. If they have none, say so and continue from git alone. Never invent diary content.
2. Report the ground truth, no sugarcoating:
   - **Shipped** — problems solved, notes written, Lab work, with counts from git.
   - **Planned vs done** — compare against any plan the user pastes; list what was dropped.
   - **Repeated mistakes** — group the diary mistakes by root cause (missed observation, implementation bug, edge case, complexity, planning). A cause that appears twice is a pattern; name it.
   - **Weak tags / topics** — from solves, upsolves and quiz scores.
3. **@adversary** gets one pass: the week's most flattering story the user is telling themselves, and what the data says instead.
4. Decide, in order: ONE thing to stop, ONE thing to start, ONE habit to keep. A repeated mistake gets a concrete countermeasure the user can check next week.
5. Output a paste-ready block for the diary and a seed for the next `/plan`. Do not write to the diary yourself.
