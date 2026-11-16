---
description: Take a concept from first principles to running code
---

When the user types `/deepdive <concept-or-paper>`, orchestrate via `.agents/agents.md`.

### Execution Sequence:

1. Shift context to **@researcher**. Demand the user state their current hypothesis about `<concept-or-paper>` first (rule 7). Then deliver the first-principles breakdown (what/when/why/where/how), with sources or `[Logical Assumption]` flags, and say what result would prove the idea wrong.
2. **@researcher** designs a minimal from-scratch implementation spec (no libraries beyond NumPy unless justified).
3. Shift context to **@craftsman**. Implement the spec in `Lab/` with logged config, seed, and a runnable verification test (`cd Lab && uv run python <file>`).
4. Run it. **@craftsman** reports honest results; **@researcher** interprets: does reality match theory? If not, diagnose why.
5. **@adversary** gets one pass on the result: seeds, baselines, leakage, a cheaper explanation. Report what was tried, even if nothing broke.
6. **@archivist** files the concept note in `Arsenal Vault/ME/` linking the paper, the Lab experiment, and related notes (show a diff for any existing note).
7. HANDOFF to **@vanguard**: schedule the follow-up experiment in the next `/plan`.
