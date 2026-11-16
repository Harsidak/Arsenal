---
trigger: glob
description: Note format and linking conventions when creating or editing notes in Arsenal Vault/
globs: "Arsenal Vault/**/*.md"
---

# Vault Note Conventions

- Route to **@archivist** for structure, **@bookworm** for book notes.
- Valid Obsidian Markdown. At least one `[[wikilink]]` per note, preferably to notes that already exist (check before linking; no invented targets).
- Atomic: one concept per note, titled by the concept (`Span and Bases`, not `Chapter 2 notes`). If a note grows to cover two ideas, propose a split rather than doing it.
- Existing style: an H1 with an emoji, a `> [!NOTE] Source Context` callout naming the source and cross-references, numbered `##` sections, math in `$...$` / `$$...$$`. Match the neighbouring notes in the same folder.
- New notes go under `Arsenal Vault/ME/` in the matching topical folder; add a link from the nearest index note (`ME/ME.md` or the topic index) so the note is reachable.
- Do not edit the user's wording or reasoning. Structure, links and typos only, and show a diff for any change to an existing note.
- Never cite a source you have not been given or cannot verify. Unsourced claims are tagged `[Logical Assumption]`.
