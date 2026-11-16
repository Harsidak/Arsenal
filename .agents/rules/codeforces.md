---
trigger: glob
description: Conventions when working on CP solutions in CodeForces/ or templates in DSA/
globs: "CodeForces/**, DSA/**"
---

# CP & DSA Conventions

- Route to **@grandmaster**. The hint ladder in rule 7 of `arsenal.md` applies without exception.
- Solutions are standalone single files: C, C++ or Python, no build system. One folder per contest round; older problems live in `CodeForces/SOLVED/`, named by problem id (`1352.c`, `1613A.c`).
- Compile check: `g++ -O2 -std=c++17 file.cpp -o out` or `gcc file.c -o out`. Never commit binaries (`*.exe`, `*.out`, `*.o` are gitignored).
- Judge every solution on three things, in order: correctness on edge cases (n=1, max constraints, overflow), time/memory complexity against the stated limits, then clarity.
- Reusable ideas belong in `DSA/<topic_snake_case>/`; `DSA/template.cpp` is the fast-I/O template. Propose template changes, don't make them silently.
- Never rewrite the user's accepted solution just to make it "cleaner". Suggest, with a diff.
