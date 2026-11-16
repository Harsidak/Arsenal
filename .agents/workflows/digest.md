---
description: Convert a finished book into vault knowledge and practice
---

When the user types `/digest <book-title>`, orchestrate via `.agents/agents.md`.

### Execution Sequence:

1. Shift context to **@bookworm**. Interview the user: what stuck, what felt wrong, what they disagree with. Do not summarize chapters.
2. **@bookworm** extracts: three core principles, mental models, and one technique applicable this week in `Lab/` or `CodeForces/`. *(Wait for user approval of the extraction. Revise on feedback until they type "Approved".)*
3. **@archivist** creates atomic notes in `Arsenal Vault/ME/BOOKS/` and the matching topical folder, each with ≥2 wikilinks to existing notes, and updates the book index. Show a diff for any existing note.
4. HANDOFF to **@vanguard**: schedule the "apply it this week" action item for the next `/plan`.
