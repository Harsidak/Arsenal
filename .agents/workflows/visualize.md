---
description: Generate Manim Python code to animate and visualize a requested topic, including folder setup and rendering commands. Use when the user types /visualize <Topic> or asks to visualize something.
---

# Visualize with Manim

When the user types `/visualize <Topic>`, or asks to animate, draw or visualize a concept with Manim or Python, generate a `manim` script for it.

## Steps

1. **Understand the topic.** Pick the best visual representation (shapes, graphs, equations, transformations).
2. **Folder setup.** Provide commands for a dedicated, snake_case directory, e.g. `mkdir -p manim_projects/<topic_name_snake_case> && cd manim_projects/<topic_name_snake_case>`.
3. **Generate the code.** Write the complete `main.py`:
   - `from manim import *`
   - A class inheriting from `Scene` (or `ThreeDScene` / `MovingCameraScene` if needed)
   - Well-commented animations (`Create`, `Write`, `Transform`, ...)
4. **Render commands.**
   - Fast preview: `manim -pql main.py <ClassName>`
   - High quality: `manim -pqh main.py <ClassName>`

## Gotchas

- Use the community edition (`manim`), not the deprecated `manimlib`.
- Use raw strings (`r"..."`) for LaTeX and keep math formulas properly formatted.
- The repo's `.venv_manim/` is the local environment for this; it is gitignored.
