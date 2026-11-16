---
description: Active-recall exam on one of your own vault notes (Socratic, graded against the note)
---

When the user types `/quiz <note-or-topic>`, run a closed-book exam on their own notes. Nothing is written to any file.

### Execution Sequence:

1. Find the note in `Arsenal Vault/`: match the title, otherwise search the vault for the topic. If several match, list them and ask which one. Read the note and the notes it links to.
2. Pick the examiner: **@grandmaster** for CP, DSA and algorithm notes; **@researcher** for math, ML and research notes. Do not show the note's content to the user.
3. Ask questions ONE at a time, 5 total, escalating:
   1. Recall — define or state it.
   2. Why — why is it true / why does it work.
   3. Apply — a small concrete problem or example.
   4. Connect — how it relates to a linked note (name the link).
   5. Break it — an edge case or a counterexample to a tempting wrong claim.
4. After each answer, the user must answer in their own words first. Then grade it **against the note's text**: correct / partial / missing, with the exact line quoted. If the note itself looks wrong or incomplete, say so and flag it `[Logical Assumption]`; do not silently "correct" it.
5. Never give the answer before the user attempts. If they say "skip", mark it missing and move on.
6. Close with a score out of 5, the weak points as a list of `[[note]]` names to re-read, and a paste-ready diary line: `Quiz: <note> — x/5 — weak: …`.
7. HANDOFF to **@vanguard** only if the score is below 3: schedule a re-quiz in 2 days.
