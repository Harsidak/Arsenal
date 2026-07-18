# Eigenvectors and Eigenspectrum

> [!NOTE] Source Context & References
> **Primary Textbook:** *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — Chapter 4: Matrix Decompositions
> **Parent Category:** [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]] | [[MATHEMATICS]]
> **Related Notes:** [[TOPICS/MATRICES/Determinants and Trace|Determinants and Trace]], [[TOPICS/MATRICES/Diagonalization|Diagonalization]], [[TOPICS/Linear Algebra/Symmetric, Definite and Positive Matrices|Symmetric, Definite and Positive Matrices]]

This note places **eigenvectors and eigenspectra** on the mathematical landscape, building on the concepts of traces, determinants, and projections.

---

## 1. The Core Question

A square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ represents a linear transformation. Most vectors get both **stretched** and **rotated** when $\mathbf{A}$ acts on them.

**The Eigenvalue Question:** Are there special vectors that only get stretched, with zero rotation?

---

## 2. Definition

A non-zero vector $\mathbf{v} \in \mathbb{R}^n$ is an **eigenvector** of $\mathbf{A}$ with **eigenvalue** $\lambda \in \mathbb{R}$ (or $\mathbb{C}$) if:

$$\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$$

**Geometric Meaning:** $\mathbf{v}$ is a direction that the linear mapping $\mathbf{A}$ leaves unchanged (up to scaling). The eigenvalue $\lambda$ tells you by how much $\mathbf{v}$ is stretched ($|\lambda| > 1$), shrunk ($|\lambda| < 1$), or flipped ($\lambda < 0$).

---

## 3. The Eigenspectrum

The **spectrum** of $\mathbf{A}$ is the set of all eigenvalues:
$$\text{spec}(\mathbf{A}) = \{\lambda_1, \lambda_2, \dots, \lambda_n\}$$

For real matrices, eigenvalues can be:
*   **Real:** The eigenvector lies in $\mathbb{R}^n$.
*   **Complex Conjugate Pairs:** $\lambda = a \pm bi$. Geometrically, this means the matrix performs a rotation in a 2D plane.

---

## 4. How to Find Eigenvalues: The Characteristic Equation

Rearranging the definition:
$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v} \implies (\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$$

For a non-zero solution $\mathbf{v}$ to exist, the matrix $(\mathbf{A} - \lambda\mathbf{I})$ must be singular (non-invertible):
$$\det(\mathbf{A} - \lambda\mathbf{I}) = 0$$

This is the **characteristic polynomial**. Its roots are the eigenvalues of $\mathbf{A}$.

**Example (For a $2 \times 2$ matrix):**
$$\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$
$$\det(\mathbf{A} - \lambda\mathbf{I}) = (a-\lambda)(d-\lambda) - bc = \lambda^2 - (a+d)\lambda + (ad-bc) = 0$$
$$\lambda^2 - \text{tr}(\mathbf{A})\lambda + \det(\mathbf{A}) = 0$$

Notice how the trace and determinant appear directly as coefficients of the characteristic polynomial. This generalizes to $n \times n$ matrices.

---

## 5. Key Properties (The Ones That Matter)

| Property | Statement | Why It Matters |
| :--- | :--- | :--- |
| **Trace = Sum** | $\text{tr}(\mathbf{A}) = \sum_{i=1}^n \lambda_i$ | Total "expansion" of the transformation. |
| **Determinant = Product** | $\det(\mathbf{A}) = \prod_{i=1}^n \lambda_i$ | Volume scaling. If any $\lambda_i = 0$, the matrix collapses space (singular). |
| **Invertibility** | $\mathbf{A}$ invertible $\iff \forall \lambda_i \neq 0$ | Non-singular matrices have full rank. |
| **Powers** | $\mathbf{A}^k\mathbf{v} = \lambda^k\mathbf{v}$ | Applying a matrix $k$ times to an eigenvector is computationally cheap. |
| **Inverse** | If $\mathbf{A}$ is invertible, $\mathbf{A}^{-1}\mathbf{v} = \lambda^{-1}\mathbf{v}$ | Eigenvalues invert, eigenvectors stay the same. |
| **Similarity Invariance** | $\mathbf{A}$ and $\mathbf{P}^{-1}\mathbf{AP}$ have the same spectrum | The spectrum is a property of the linear map, not the basis. |

---

## 6. Diagonalization: The Payoff

If $\mathbf{A}$ has $n$ linearly independent eigenvectors, we can form the modal matrix $\mathbf{P}$:
$$\mathbf{P} = [\mathbf{v}_1 \; \mathbf{v}_2 \; \cdots \; \mathbf{v}_n]$$

Then, $\mathbf{A}$ can be factorized as:
$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$$

Where $\mathbf{D} = \text{diag}(\lambda_1, \dots, \lambda_n)$ is a diagonal matrix containing the eigenvalues.

**Why this is powerful:**
*   **Matrix Powers:** $\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$ (exceedingly cheap to compute).
*   **Matrix Functions:** $f(\mathbf{A}) = \mathbf{P}f(\mathbf{D})\mathbf{P}^{-1}$ (e.g., matrix exponential $e^{\mathbf{A}}$).
*   **Decoupled Systems:** The eigenbasis decouples multi-variable linear dynamical systems into independent 1D modes.

> [!WARNING]
> **Defective Matrices:** If $\mathbf{A}$ does not have $n$ linearly independent eigenvectors, it cannot be diagonalized. In this case, you must use **Jordan normal form**. This is rare for symmetric matrices, which are always diagonalizable.

### 6.1 Defective Matrices: Definition & Implications

#### The Correct Definition
A square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ is **defective** if it possesses **fewer than $n$ linearly independent eigenvectors**.

#### Algebraic vs. Geometric Multiplicity

##### Algebraic Multiplicity
*   **Definition:** The number of times $\lambda$ appears as a root of the characteristic polynomial $\det(\mathbf{A}-\lambda\mathbf{I})=0$.
*   **What It Is:** A property of the characteristic polynomial itself. It counts how many times the eigenvalue is "listed" as a root.
*   **Example:**
    $$\mathbf{A}=\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$$
    Characteristic polynomial:
    $$\det(\mathbf{A}-\lambda\mathbf{I}) = \det\begin{bmatrix} 2-\lambda & 1 \\ 0 & 2-\lambda \end{bmatrix} = (2-\lambda)^2 = 0$$
    The root $\lambda=2$ appears twice. Thus, the algebraic multiplicity of $\lambda=2$ is **2**.

##### Geometric Multiplicity
*   **Definition:** The dimension of the eigenspace associated with $\lambda$ (the number of linearly independent eigenvectors associated with $\lambda$).
*   **What It Is:** A property of the matrix operator's kernel: $\operatorname{dim}(\operatorname{null}(\mathbf{A} - \lambda\mathbf{I}))$.

#### Visual Comparison Matrix

An $n \times n$ matrix always has $n$ eigenvalues counting algebraic multiplicity, but it is defective if any eigenvalue's geometric multiplicity is strictly less than its algebraic multiplicity.

| Matrix | Eigenvalues & Algebraic Mult. | Eigenvectors & Geometric Mult. | Defective? |
| :--- | :--- | :--- | :--- |
| $\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$ | $\lambda_1=2$ (mult. 1)<br>$\lambda_2=3$ (mult. 1) | Two independent eigenvectors:<br>$(1,0)^\top$ and $(0,1)^\top$ (both geom. mult. 1) | **No** |
| $\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$ | $\lambda=2$ (mult. 2) | Only one independent eigenvector:<br>$(1,0)^\top$ (geom. mult. 1) | **Yes** ($1 < 2$) |
| $\begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$ | $\lambda=2$ (mult. 2) | Two independent eigenvectors:<br>any basis (geom. mult. 2) | **No** ($2 = 2$) |

The second matrix is defective because $\lambda = 2$ has algebraic multiplicity 2, but geometric multiplicity 1. The third is not defective because, despite the repeated eigenvalue, we still obtain two linearly independent eigenvectors (geometric multiplicity 2).

#### Why Defective Matrices Matter

| Consequence | Explanation |
| :--- | :--- |
| **Not Diagonalizable** | You cannot write $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ because the modal matrix $\mathbf{P}$ would need $n$ independent columns to be invertible. |
| **Need Jordan Form** | The matrix must be factored into Jordan normal form: $\mathbf{A} = \mathbf{P}\mathbf{J}\mathbf{P}^{-1}$ where $\mathbf{J}$ has $1$s on the superdiagonal. |
| **Unstable Powers** | Matrix powers $\mathbf{A}^k$ grow with a polynomial factor (e.g. terms like $k\lambda^k$), rather than pure exponential scaling. |
| **Rare in ML** | Symmetric matrices (covariances, Hessians, graph Laplacians) are mathematically guaranteed to never be defective. |

---

## 7. Symmetric Matrices: The Special Case

If $\mathbf{A} = \mathbf{A}^\top$ (symmetric), then:

| Property | Consequence |
| :--- | :--- |
| **Real Eigenvalues** | All eigenvalues are real numbers ($\lambda_i \in \mathbb{R}$); no complex numbers. |
| **Orthogonal Eigenvectors** | Eigenvectors corresponding to distinct eigenvalues are orthogonal: $\langle \mathbf{v}_i, \mathbf{v}_j \rangle = 0$ for $\lambda_i \neq \lambda_j$. |
| **Always Diagonalizable** | No defective cases. |
| **Orthonormal Eigenbasis** | Can choose an orthonormal eigenbasis. The modal matrix $\mathbf{P}$ is orthogonal: $\mathbf{P}^{-1} = \mathbf{P}^\top$. |

This is the foundation of the **Spectral Theorem**, which underlies PCA, SVD, and quadratic forms.

---

## 8. Where Eigenvectors and Spectra Appear in ML/DL

| Application | Role of Eigenvalues/Eigenvectors |
| :--- | :--- |
| **PCA** | The eigenvectors of the covariance matrix $\mathbf{\Sigma}$ are the principal components (directions of maximum variance). The eigenvalues correspond to the variance explained along those components. |
| **Spectral Clustering** | The eigenvectors of the graph Laplacian matrix reveal the community/cluster structure of the graph. |
| **PageRank** | The stationary probability distribution of a Markov chain is the dominant eigenvector of the transition probability matrix. |
| **Stability Analysis** | In Recurrent Neural Networks (RNNs) and dynamical systems, the eigenvalues of the Jacobian matrix determine whether perturbations grow ($|\lambda| > 1$) or decay ($|\lambda| < 1$). |
| **Hessian Analysis** | The eigenvalues of the Hessian matrix $\nabla^2 \mathcal{L}$ describe local loss curvature. Negative eigenvalues indicate saddle points; a large condition number ($\lambda_{\max}/\lambda_{\min}$) indicates an ill-conditioned optimization landscape. |
| **Spectral Normalization** | Used in GANs to stabilize training by bounding the Lipschitz constant of the networks. This is achieved by dividing weight matrices by their spectral norm $\sigma_{\max}(\mathbf{W})$. |
| **Graph Neural Networks** | Spectral GNNs define convolutions directly on the graph spectrum (using the eigenvalues of the graph Laplacian). |

---

## 9. The Spectral Decomposition (For Symmetric Matrices)

$$\mathbf{A} = \sum_{i=1}^n \lambda_i \mathbf{v}_i \mathbf{v}_i^\top$$

Each term $\lambda_i \mathbf{v}_i \mathbf{v}_i^\top$ is a rank-1 matrix. It represents an orthogonal projection onto the direction of $\mathbf{v}_i$, scaled by $\lambda_i$.

**Interpretation:** The matrix $\mathbf{A}$ is a linear superposition of independent "modes," each acting along its own orthogonal direction.

This is the mathematical engine behind:
*   **Low-Rank Approximation:** Keeping only the terms with the largest $|\lambda_i|$.
*   **Spectral Filtering:** Removing noise by zeroing out small eigenvalues.
*   **Matrix Completion:** Reconstructing missing values using low-rank spectral constraints.

---

## 10. The Dominant Eigenvalue and Power Iteration

For many ML applications, you only need the **largest (dominant)** eigenvalue and its corresponding eigenvector.

**Power Iteration Algorithm:** Start with a random vector $\mathbf{x}_0$, and iterate:
$$\mathbf{x}_{k+1} = \frac{\mathbf{A}\mathbf{x}_k}{\|\mathbf{A}\mathbf{x}_k\|}$$

This algorithm converges to the eigenvector of the largest-magnitude eigenvalue, assuming the eigenvalue is unique and $\mathbf{x}_0$ has a non-zero component along that eigenvector.

*   **Used In:** Large-scale PCA (when $n \gg d$), PageRank computation, and Spectral Normalization.

---

## The One-Sentence Summary
> **Eigenvectors are the directions that a linear transformation leaves invariant; eigenvalues are the scaling factors. The spectrum encodes the fundamental geometry of the transformation, and symmetric matrices guarantee real eigenvalues with orthogonal eigenvectors — the mathematical bedrock of PCA, spectral methods, and optimization curvature analysis.**
