---
description: Read-only health report on the vault: missing wikilinks, broken links, orphans
---

When the user types `/lint-vault`, shift context to **@archivist**. This command never edits or deletes anything.

### Execution Sequence:

1. Run `python .agents/scripts/lint_vault.py` from the repo root (use `uv run python` if Python is not on PATH).
2. Report the script's findings in four lists, most important first:
   - **No wikilinks** — violates the rule that every note has at least one.
   - **Broken links** — `[[Target]]` with no matching note title.
   - **Orphans** — notes nothing links to, so they are not retrievable.
   - **Empty or near-empty notes.**
3. For each list, propose the fix (which link to add, which index to link from). Do not apply any of it. Any change goes through the diff rule (rule 4) in a follow-up the user approves.
4. Link detection is a heuristic (aliases, headings and anchors are stripped; embeds count). If a result looks wrong, say so and flag it `[Logical Assumption]` rather than asserting it.
5. HANDOFF to **@vanguard** only if the user wants the clean-up scheduled.
