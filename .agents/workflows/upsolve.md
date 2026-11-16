---
description: Work a stuck or failed CP problem up the hint ladder, then re-solve it and log the post-mortem
---

When the user types `/upsolve <problem-id-or-file>`, orchestrate via `.agents/agents.md`. The hint ladder is rule 7 of `.agents/rules/arsenal.md`.

### Execution Sequence:

1. Shift context to **@grandmaster**. Locate the problem and any attempt in `CodeForces/`. Ask the user, and wait: what did you try, what is your current idea, and where exactly does it break (WA test, TLE, no idea)? No attempt means no hints — tell them to write one, even a wrong one.
2. Diagnose from their attempt, not from the editorial. Name the failure type: missed observation / wrong approach / implementation bug / complexity / edge case. Give **Tier 1** only. Stop.
3. Climb one tier per user request. Never jump. Give Tier 5 (full solution) only after the user types "reveal" at Tier 3 or higher.
4. After a reveal: the user closes the file and re-solves from blank, no peeking. **@grandmaster** checks it against edge cases and complexity.
5. **@adversary** gets one pass: break the accepted solution (max constraints, n=1, overflow, adversarial tests). Report what was tried, even if nothing broke.
6. Output a post-mortem block the user can paste into their diary:
   - Problem / tags / time spent / highest tier used
   - Failure type and the one-line root cause
   - The idea in one sentence
   - Template or technique to add to `DSA/`
7. **@archivist** files the solution in `CodeForces/` (show a diff if the file exists) and links the technique note in `Arsenal Vault/` if one exists.
8. HANDOFF to **@vanguard**: re-solve this problem cold in 3 days (put it in the `/plan` queue).
