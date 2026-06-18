# 📐 Linear Mappings

> [!NOTE] Source Context
> This concept builds directly upon [[Vector Spaces]] and [[Linear Independence]], and is adapted from [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]]. In AI systems and 3D computer graphics (such as rendering AR overlays in Project ONYX), **Linear Mappings** are the mathematical operators that transform vectors (rotate, scale, project) while preserving the linear structure of the space.

---

## 1. The Intuitive Picture: Graphing Paper Transformation
Imagine you have a piece of graphing paper with a drawing on it. A **Linear Mapping** is any way you can stretch, squash, rotate, or flip that paper, provided you obey two absolute, unbreakable physical laws:

```
  Rule 1: The Origin Anchor                    Rule 2: Parallel Grid Lines
  (The origin [0,0] cannot move)               (Lines must remain straight and parallel)

          y                                            y
          ▲                                            ▲
          │    o (Origin stays)                        │   /  /  /  / (Slanted but parallel)
   ───────o───────► x                           ──────/──/──/──/──► x
          │                                          /  /  /  /
          │                                         /  /  /  /
```

1.  **The Origin cannot move**: The center point $\vec{0} = [0, 0, 0]$ must stay exactly where it is. If you shift the entire paper two inches to the left, you just broke the law. (That is called a *translation*, and it is an affine mapping, not a linear mapping!).
2.  **Grid lines must remain perfectly straight and parallel**: You can stretch the paper so the squares turn into long rectangles or slanted diamonds (shearing), but you cannot bend, curve, twist, or warp the paper.

---

## 2. The Formal Definition (The Two Rules)
If we call our mapping function $L: \mathcal{V} \rightarrow \mathcal{W}$ (where $\mathcal{V}$ and $\mathcal{W}$ are vector spaces), it must pass these two mathematical tests to be officially crowned "Linear":

### Ⅰ. Additivity (The "No Surprises" Rule)
*   **The Formula**:
    $$L(\vec{u} + \vec{v}) = L(\vec{u}) + L(\vec{v})$$
*   **🧠 What it means**: Adding two vectors together and then transforming them yields the exact same coordinate as transforming each vector individually first, and then adding them together.
*   **👶 The 5yo Explanation**: If you walk 2 steps right ($\vec{u}$) and then 3 steps up ($\vec{v}$), and then zoom in on your position by $2\times$, it's the exact same as zooming in on your individual steps first, and then walking them.

### Ⅱ. Homogeneity (The Scaling Rule)
*   **The Formula**:
    $$L(c \cdot \vec{v}) = c \cdot L(\vec{v})$$
*   **🧠 What it means**: Scaling a vector and then transforming it is identical to transforming the vector first and then scaling the resulting vector by the same amount.
*   **👶 The 5yo Explanation**: Stretching a path by $5$ and then taking the shortcut is the same as taking the shortcut first and then stretching the end result by $5$.

---

## 3. The Grand Reveal: Matrices ARE Linear Maps
This is the biggest **"Aha!"** moment in linear algebra:

> [!IMPORTANT]
> **A Matrix is just the source code for a Linear Map.**
> Up until now, you may have thought of matrices as just grids of numbers or databases of vectors. But in reality, when you multiply a vector by a matrix ($A\vec{x} = \vec{b}$), you are physically applying a Linear Map to that vector. The matrix $A$ is the instruction manual that tells the vector exactly how to stretch, rotate, or shear.

*   **Rotation Matrix**: Multiply your 3D avatar coordinate by it, and the avatar spins.
*   **Scaling Matrix**: Multiply by it, and the avatar grows or shrinks.
*   **Projection Matrix**: Flattens a 3D object coordinate perfectly onto your 2D smart glasses screen (Project **ONYX** HUD rendering).

---

## 4. Classifications of Mappings

```
      Injective (1-to-1)             Surjective (Onto)             Bijective (Perfect Pairing)
        (No Collisions)               (No Wasted Space)                (Perfect Invertible)

      Inputs        Outputs         Inputs        Outputs            Inputs        Outputs
       ┌───┐         ┌───┐           ┌───┐         ┌───┐              ┌───┐         ┌───┐
       │ A ├────────►│ 1 │           │ A ├────────►│ 1 │              │ A ├────────►│ 1 │
       │ B ├────────►│ 2 │           │ B ├───┐     └───┘              │ B ├────────►│ 2 │
       │ C ├───┐     │ 3 │           │ C ├───┴────►│ 2 │              │ C ├────────►│ 3 │
       └───┘   └────►└───┘           └───┘         └───┘              └───┘         └───┘
                     (4 is empty)                                     (Perfect 1-to-1 match)
```

### Ⅰ. Injective (The "No Collisions" Rule)
*   **Also known as**: One-to-One ($1$-to-$1$).
*   **🧠 What it means**: No two inputs map to the exact same output. Every input gets its own unique target.
    $$L(\vec{x}) = L(\vec{y}) \implies \vec{x} = \vec{y}$$
*   **👶 The 5yo Explanation**: A group of kids throw darts. No two kids hit the exact same spot. (Some spots on the board might not get hit at all, which is fine).
*   **💻 The Engineering Reality**: **No Information Loss.** If a mapping is injective, you can perfectly trace any output back to its source. If your AI's sensor mapping is injective, you can guarantee that different physical states (inputs) never produce duplicate readings (collisions).

### Ⅱ. Surjective (The "No Wasted Space" Rule)
*   **Also known as**: Onto.
*   **🧠 What it means**: The mapping spans the entire target space. Every element in the output space is mapped to by at least one input.
    $$\forall \vec{y} \in \mathcal{W}, \exists \vec{x} \in \mathcal{V} \text{ such that } L(\vec{x}) = \vec{y}$$
*   **👶 The 5yo Explanation**: Every single spot on the dartboard gets hit by at least one dart. (It is fine if multiple kids hit the same spot, as long as the whole board is covered).
*   **💻 The Engineering Reality**: **Reachability & Spanning.** If you build a robotic arm with 3 joints, and the mathematical mapping of its joint angles is surjective for a 3D box workspace, the arm can physically reach every single millimeter inside that box. There are no "dead zones."

### Ⅲ. Bijective (The "Perfect Pairing")
*   **Also known as**: One-to-One Correspondence.
*   **🧠 What it means**: The mapping is both injective and surjective. There is a perfect, unique pairing between every input and every output.
*   **👶 The 5yo Explanation**: A perfect game of musical chairs with exactly 10 kids and 10 chairs. Every kid gets exactly one chair, and no chairs are left empty.
*   **💻 The Engineering Reality**: **Perfect Invertibility.** If a mapping is bijective, its matrix representation is invertible ($A^{-1}$ exists). You can map your data forward, and then safely run the inverse matrix to pull the data backward without losing a single bit of information.

---

## 5. Connecting It All Together: GL Group, Rank, & Invertibility
If you have a square matrix $A \in \mathbb{R}^{n \times n}$ representing a linear map:

*   **If it is NOT Injective**: It collapses space. For example, it squashes a 3D room flat onto a 2D sheet of paper. Data is destroyed, its Rank is less than $n$, its determinant is zero ($\det(A) = 0$), and it is **singular** (non-invertible).
*   **If it is NOT Surjective**: It cannot cover the target space. There are areas in the target space that cannot be reached by any input.
*   **If it is BIJECTIVE**: It has **Full Rank** ($n$), its determinant is non-zero ($\det(A) \neq 0$), and it belongs to the **General Linear Group** $GL_n(\mathbb{R})$. This is the holy grail because it guarantees you can reverse the map at zero cost.

---

## 🕹️ Interactive Mapping Visualizer

To help you visualize how matrices transform grid space, and to see injectivity, surjectivity, and sine-wave warping in real-time:

> [!TIP] Live Mapping Playground
> * **Interactive Web Application**: [[linear-mapping-visualizer.html]]
> * **How to run**: Open the file in your browser to adjust sliders (rotation, scale, shear, translation) and toggle presets to see what is (and isn't) a linear mapping.
> 
> * **To Embed Directly inside Obsidian**: Paste this HTML block in your editor:
> 
> ```html
> <iframe src="linear-mapping-visualizer.html" width="100%" height="820px" style="border:none; border-radius:12px; background:#080c14; box-shadow: 0 8px 24px rgba(0,0,0,0.4);"></iframe>
> ```

---

**Related Notes**:
*   [[Vector Spaces]]
*   [[Linear Independence]]
*   [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]]
