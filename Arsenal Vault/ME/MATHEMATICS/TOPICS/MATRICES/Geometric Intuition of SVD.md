# Geometric Intuition of SVD

> [!NOTE] Source Context & References
> **Primary Textbook:** *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — Chapter 4: Matrix Decompositions
> **Parent Category:** [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]] | [[MATHEMATICS]]
> **Related Notes:** [[TOPICS/MATRICES/Singular Value Decomposition|Singular Value Decomposition]], [[TOPICS/MATRICES/Eigenvectors and Eigenspectrum|Eigenvectors and Eigenspectrum]], [[TOPICS/MATRICES/Diagonalization|Diagonalization]], [[TOPICS/Analytical Geometry/Analytical Geometry Summary|Analytical Geometry Summary]]

Singular Value Decomposition (SVD) reveals the underlying geometry of linear operators. This note breaks down how SVD maps space, transforms unit spheres into hyper-ellipsoids, and illuminates the fundamental subspaces of linear algebra.

---

## 1. The Core Question

What does a matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ actually do to space?

A general linear transformation can:
1.  **Rotate or reflect** space.
2.  **Stretch** space along certain directions.
3.  **Squash** space along other directions (reducing dimensions).

SVD decomposes any complex linear transformation into three clean, geometrically transparent operations.

---

## 2. The Three-Step Picture

$$\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$$

| Step | Matrix | Action | Geometric Meaning |
| :--- | :--- | :--- | :--- |
| **1** | $\mathbf{V}^\top$ | Rotation / Reflection in input space $\mathbb{R}^n$ | Aligns the input axes with the "natural" principal directions of the transformation. |
| **2** | $\mathbf{\Sigma}$ | Scaling along coordinate axes | Stretches space by factors $\sigma_1, \sigma_2, \dots$ along those aligned directions. |
| **3** | $\mathbf{U}$ | Rotation / Reflection in output space $\mathbb{R}^m$ | Maps the scaled result into the final output coordinate system. |

> [!TIP]
> **Key Geometric Takeaway:** Every linear transformation, no matter how complex, is simply: **Rotate $\to$ Scale $\to$ Rotate**.

```
Input Space R^n                   Intermediate Space                   Output Space R^m
  [ Unit Sphere ]  ──( V^T )──>  [ Rotated Sphere ]  ──( Σ )──>  [ Scaled Ellipsoid ]  ──( U )──>  [ Rotated Ellipsoid ]
```

---

## 3. The Detailed Picture: What Happens to a Unit Sphere?

This is the canonical geometric intuition for SVD. Consider the unit sphere in $\mathbb{R}^n$:

$$\mathcal{S} = \{ \mathbf{x} \in \mathbb{R}^n \mid \|\mathbf{x}\| = 1 \}$$

When we apply $\mathbf{A}$ to every point on this sphere:

1.  **Step 1 ($\mathbf{V}^\top$):** Rotates the sphere. Because orthogonal transformations preserve lengths ($\|\mathbf{V}^\top \mathbf{x}\| = \|\mathbf{x}\| = 1$), $\mathcal{S}$ remains a unit sphere.
2.  **Step 2 ($\mathbf{\Sigma}$):** Scales each orthogonal axis by $\sigma_i$. The unit sphere is stretched into a **hyper-ellipsoid**:
    *   Semi-axis 1 has length $\sigma_1$
    *   Semi-axis 2 has length $\sigma_2$
    *   $\dots$
3.  **Step 3 ($\mathbf{U}$):** Rotates this hyper-ellipsoid into its final orientation in $\mathbb{R}^m$.

### Vector Mappings
*   The **singular values** $\sigma_i$ are the exact lengths of the hyper-ellipsoid's semi-axes.
*   The **right singular vectors** ($\mathbf{v}_i$, columns of $\mathbf{V}$) are the orthonormal directions in input space that map directly onto these axes.
*   The **left singular vectors** ($\mathbf{u}_i$, columns of $\mathbf{U}$) are the orthonormal directions of these axes in output space.

$$\mathbf{A} \mathbf{v}_i = \sigma_i \mathbf{u}_i$$

---

## 4. Concrete 2D Example

Let $\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$.

1.  Start with the unit circle in $\mathbb{R}^2$.
2.  Apply $\mathbf{A}$: The circle is mapped into an ellipse in $\mathbb{R}^2$.
    *   The major semi-axis has length $\sigma_1 \approx 3.62$.
    *   The minor semi-axis has length $\sigma_2 \approx 1.38$.
3.  Vector correspondences:
    *   $\mathbf{v}_1$: The direction in input space that gets stretched the **most**.
    *   $\mathbf{v}_2$: The direction in input space that gets stretched the **least** (perpendicular to $\mathbf{v}_1$).
    *   $\mathbf{u}_1$: The direction in output space where $\mathbf{v}_1$ lands (along the major axis).
    *   $\mathbf{u}_2$: The direction in output space where $\mathbf{v}_2$ lands (along the minor axis).

$$\mathbf{v}_1 \mapsto \sigma_1 \mathbf{u}_1, \quad \mathbf{v}_2 \mapsto \sigma_2 \mathbf{u}_2$$

---

## 5. The Rank-1 Decomposition View

$$\mathbf{A} = \sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^\top$$

Where $r = \operatorname{rank}(\mathbf{A})$. Each term $\sigma_i \mathbf{u}_i \mathbf{v}_i^\top$ is a rank-1 matrix. 

### Geometric Mechanics of Each Term:
1.  $\mathbf{v}_i^\top \mathbf{x}$: Projects the input vector $\mathbf{x}$ onto the 1D subspace spanned by $\mathbf{v}_i$.
2.  $\sigma_i$: Scales the projection by the singular value $\sigma_i$.
3.  $\mathbf{u}_i$: Embeds the scalar magnitude into output space along the direction $\mathbf{u}_i$.

Thus, $\mathbf{A}$ is a superposition of $r$ independent 1D "modes" or "channels". The singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r$ rank these modes by energy/importance. $\sigma_1$ represents the dominant mode of maximum stretch.

---

## 6. Low-Rank Approximation: Geometric Meaning

The rank-$k$ approximation ($k < r$) is given by:

$$\mathbf{A}_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^\top$$

### Geometrically:
*   You are replacing the $r$-dimensional hyper-ellipsoid with a lower $k$-dimensional hyper-ellipsoid.
*   **If $k=1$:** You replace a 2D ellipse with a line segment along its major axis ($2\sigma_1 \mathbf{u}_1$).
*   **If $k=2$ in 3D:** You flatten a 3D ellipsoid into a 2D flat ellipse on the plane spanned by $\mathbf{u}_1, \mathbf{u}_2$.

The squared Frobenius error:
$$\|\mathbf{A} - \mathbf{A}_k\|_F^2 = \sum_{i=k+1}^r \sigma_i^2$$
is the sum of squared lengths of the discarded semi-axes.

> [!NOTE]
> **Why PCA Works:** PCA keeps the principal directions of maximum variance (the long semi-axes of the data ellipsoid) and truncates short semi-axes (which correspond to small singular values / noise).

---

## 7. The Four Fundamental Subspaces (Geometrically)

SVD exposes the complete geometry of $\mathbf{A} \in \mathbb{R}^{m \times n}$ across the four fundamental subspaces of linear algebra:

| Subspace | Geometric Description | SVD Basis |
| :--- | :--- | :--- |
| **Column Space $\text{Im}(\mathbf{A})$** | All reachable output vectors in $\mathbb{R}^m$ | Spanned by $\mathbf{u}_1, \dots, \mathbf{u}_r$ (first $r$ left singular vectors) |
| **Row Space $\text{Im}(\mathbf{A}^\top)$** | All input directions in $\mathbb{R}^n$ that produce non-zero output | Spanned by $\mathbf{v}_1, \dots, \mathbf{v}_r$ (first $r$ right singular vectors) |
| **Null Space $\operatorname{ker}(\mathbf{A})$** | Input directions in $\mathbb{R}^n$ mapped to zero ($\mathbf{A}\mathbf{x} = \mathbf{0}$) | Spanned by $\mathbf{v}_{r+1}, \dots, \mathbf{v}_n$ (last $n-r$ right singular vectors) |
| **Left Null Space $\operatorname{ker}(\mathbf{A}^\top)$** | Output directions in $\mathbb{R}^m$ that cannot be reached | Spanned by $\mathbf{u}_{r+1}, \dots, \mathbf{u}_m$ (last $m-r$ left singular vectors) |

> [!IMPORTANT]
> **Key Insight:** Singular vectors provide simultaneous orthonormal bases for all four fundamental subspaces. The singular values $\sigma_1, \dots, \sigma_r$ quantify how much the row space is stretched into the column space.

```
Input Space R^n                                     Output Space R^m
┌─────────────────────────────────┐                 ┌─────────────────────────────────┐
│ Row Space Im(A^T)               │                 │ Column Space Im(A)              │
│ Span(v_1, ..., v_r)             │ ──( A=UΣV^T )─> │ Span(u_1, ..., u_r)             │
│                                 │   Strech σ_i    │                                 │
├─────────────────────────────────┤                 ├─────────────────────────────────┤
│ Null Space ker(A)               │                 │ Left Null Space ker(A^T)        │
│ Span(v_{r+1}, ..., v_n) ──> 0   │                 │ Span(u_{r+1}, ..., u_m)         │
└─────────────────────────────────┘                 └─────────────────────────────────┘
```

---

## 8. The Pseudoinverse Geometrically

The Moore-Penrose pseudoinverse is defined as:

$$\mathbf{A}^+ = \mathbf{V}_r \mathbf{\Sigma}_r^{-1} \mathbf{U}_r^\top$$

What does $\mathbf{A}^+$ do geometrically?
1.  **$\mathbf{U}_r^\top$:** Projects an output vector onto the reachable column space $\text{Im}(\mathbf{A})$, discarding unreachable components in $\operatorname{ker}(\mathbf{A}^\top)$.
2.  **$\mathbf{\Sigma}_r^{-1}$:** Scales along each axis by $\frac{1}{\sigma_i}$, exactly inverting the stretching.
3.  **$\mathbf{V}_r$:** Maps the result back to the row space in input space $\mathbb{R}^n$.

Geometrically, $\mathbf{A}^+$ inverts the linear map by reversing rotations and scaling factors while projecting away non-invertible null space components.

---

## The One-Sentence Geometric Summary

> **SVD reveals that every linear transformation is a rotation of input space, followed by independent stretching along orthogonal axes, followed by a rotation into output space — where singular values are stretch factors, right singular vectors are the input directions that stretch, and left singular vectors are where those directions land.**
