---
description: Build a realistic plan for today or this week from evidence, with one non-negotiable
---

When the user types `/plan [day|week]` (default: day), shift context to **@vanguard**.

### Execution Sequence:

1. Gather evidence. Run `git log --since="7 days ago" --name-only --pretty=format:"%h %ad %s" --date=short` for what was actually shipped. Ask the user, and wait for answers:
   - How many hours are really available, and any fixed commitments or deadlines?
   - Paste yesterday's (or this week's) diary entry, or give its path. If they have none, say so and continue from git only. Never invent diary content.
2. Read the open queue: problems waiting for a cold re-solve (from earlier `/upsolve` handoffs), quizzes under 3/5, books awaiting `/digest`.
3. Build the plan from three blocks, sized to the stated hours with a 20% human-error buffer:
   - **CP** — one problem at the edge of their ability, or one overdue re-solve (**@grandmaster**).
   - **Lab / deep work** — one concrete deliverable, not "study" (**@researcher** / **@craftsman**).
   - **Vault** — one note written, linked or quizzed (**@archivist** / **@bookworm**).
   Drop a block rather than shrink it to nothing. Name what was cut and why.
4. Pick the ONE non-negotiable: the single item that must happen even if everything else collapses.
5. **@adversary** gets one pass on the plan: the most likely way it fails, and the fallback.
6. Output: the schedule, the non-negotiable, and ONE next action to start in the next 10 minutes. Remind the user why they are doing this.
7. For `week`: the same, plus a daily skeleton and one checkpoint on day 4.

The plan stays in chat. Do not write it to a file unless the user asks.
