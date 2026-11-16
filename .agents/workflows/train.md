---
description: Run a focused competitive programming drill session
---

When the user types `/train [topic]`, orchestrate via `.agents/agents.md`. For a problem you already failed or got stuck on, use `/upsolve` instead.

### Execution Sequence:

1. Shift context to **@grandmaster**. Analyze the user's recent solve history in `CodeForces/` and `[topic]` (or pick their weakest tag if blank; ask for the diary line if the history is unclear). Select ONE problem at the edge of their ability and set a time box.
2. The user attempts the problem. **@grandmaster** gives hints up the ladder (rule 7) ONLY on request, one tier at a time. NEVER the full solution pre-attempt.
3. After the attempt (solve or fail), **@grandmaster** delivers a brutal post-mortem: complexity analysis, what a top competitor did differently, and which template in `DSA/` needs updating. If it failed, continue with `/upsolve`.
4. **@archivist** files the problem note in `CodeForces/` with `[[links]]` to the topic concept note in `Arsenal Vault/` where one exists.
5. HANDOFF to **@vanguard**: update the training queue and report whether the user's rating trajectory is on track.
