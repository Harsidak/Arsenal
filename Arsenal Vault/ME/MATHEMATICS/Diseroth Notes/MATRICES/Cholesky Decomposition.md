# Cholesky Decomposition

> [!NOTE] Source Context & References
> **Primary Textbook:** *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — Chapter 4: Matrix Decompositions
> **Parent Category:** [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]] | [[MATHEMATICS]]
> **Related Notes:** [[Determinants and Trace|Determinants and Trace]], [[Diagonalization|Diagonalization]], [[Singular Value Decomposition|Singular Value Decomposition]], [[Symmetric, Definite and Positive Matrices|Symmetric, Definite and Positive Matrices]]

This note places **Cholesky decomposition** on the mathematical landscape, connecting it to symmetric positive definite matrices, trace/determinant calculations, and deep learning applications.

---

## 1. What Cholesky Is

Given a symmetric, positive definite matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$, there exists a unique lower-triangular matrix $\mathbf{L}$ with positive diagonal entries ($l_{ii} > 0$) such that:

$$\mathbf{A} = \mathbf{L}\mathbf{L}^\top$$

**Lower-triangular means:** All entries above the main diagonal are zero.

$$\mathbf{L} = \begin{bmatrix} l_{11} & 0 & 0 & \dots & 0 \\ l_{21} & l_{22} & 0 & \dots & 0 \\ l_{31} & l_{32} & l_{33} & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ l_{n1} & l_{n2} & l_{n3} & \dots & l_{nn} \end{bmatrix}$$

---

## 2. Why Positive Definite Is Required

| Property | Why It Matters |
| :--- | :--- |
| **Symmetric ($\mathbf{A} = \mathbf{A}^\top$)** | Guarantees real eigenvalues and orthogonal eigenvectors. Without symmetry, $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$ is impossible because $\mathbf{L}\mathbf{L}^\top$ is inherently symmetric ($(\mathbf{L}\mathbf{L}^\top)^\top = \mathbf{L}\mathbf{L}^\top$). |
| **Positive Definite ($\mathbf{A} \succ 0$)** | All eigenvalues $\lambda_i > 0$, ensuring all pivots are positive, so the diagonal entries $l_{ii} = \sqrt{a_{ii} - \sum_{k=1}^{i-1} l_{ik}^2}$ are strictly real and positive. |

> [!WARNING]
> If $\mathbf{A}$ is only positive semi-definite ($\mathbf{A} \succeq 0$), some diagonal entries $l_{ii}$ become zero and the decomposition becomes non-unique. If $\mathbf{A}$ is indefinite, Cholesky fails completely (requires LDL decomposition or diagonal regularization $\mathbf{A} + \epsilon \mathbf{I}$).

---

## 3. How It Connects to What You Know

| Concept | Connection to Cholesky |
| :--- | :--- |
| **Eigendecomposition** | $\mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^\top$. Cholesky is significantly cheaper ($\frac{1}{3}n^3$ vs $\mathcal{O}(n^3)$ for eigendecomposition) but less informative. Eigendecomposition reveals the spectrum; Cholesky yields a triangular "square root." |
| **Singular Value Decomposition (SVD)** | $\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$. For symmetric positive definite $\mathbf{A}$, SVD reduces to eigendecomposition. Cholesky is much faster than SVD. |
| **Trace** | $\text{tr}(\mathbf{A}) = \text{tr}(\mathbf{L}\mathbf{L}^\top) = \sum_{i,j} l_{ij}^2 = \|\mathbf{L}\|_F^2$ (the sum of squares of all entries in $\mathbf{L}$). |
| **Determinant** | $\det(\mathbf{A}) = \det(\mathbf{L}\mathbf{L}^\top) = \det(\mathbf{L})^2 = \left(\prod_{i=1}^n l_{ii}\right)^2$. The square of the product of diagonal entries of $\mathbf{L}$. |

---

## 4. The "Square Root" Intuition

If $\mathbf{A}$ is positive definite, think of it as $\mathbf{A} = \mathbf{B}^2$ for some matrix $\mathbf{B}$. Cholesky finds a specific $\mathbf{B} = \mathbf{L}$ that is lower-triangular.

This is directly analogous to scalar algebra:
*   **Scalar:** $a > 0 \implies a = (\sqrt{a})^2 = \sqrt{a} \cdot \sqrt{a}$
*   **Matrix:** $\mathbf{A} \succ 0 \implies \mathbf{A} = \mathbf{L}\mathbf{L}^\top$

The triangular structure allows linear systems $\mathbf{A}\mathbf{x} = \mathbf{b}$ to be solved in $\mathcal{O}(n^2)$ time via forward substitution ($\mathbf{L}\mathbf{y} = \mathbf{b}$) followed by back substitution ($\mathbf{L}^\top\mathbf{x} = \mathbf{y}$).

---

## 5. Where Cholesky Appears in ML/DL

| Application | How Cholesky Is Used |
| :--- | :--- |
| **Multivariate Gaussian Sampling** | To sample $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{\Sigma})$, draw isotropic noise $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, then compute $\mathbf{x} = \boldsymbol{\mu} + \mathbf{L}\mathbf{z}$ where $\mathbf{\Sigma} = \mathbf{L}\mathbf{L}^\top$. This is the **Reparameterization Trick** in Variational Autoencoders (VAEs). |
| **Gaussian Processes (GPs)** | The kernel covariance matrix $\mathbf{K}$ is symmetric positive definite. Cholesky decomposes $\mathbf{K} = \mathbf{L}\mathbf{L}^\top$ for numerically stable marginal likelihood computation and posterior inference. |
| **Linear Regression (Normal Equations)** | Solving $(X^\top X)w = X^\top y$. Since $X^\top X$ is positive definite (assuming full rank), Cholesky is twice as fast as LU decomposition and far more stable than direct matrix inversion. |
| **Kalman Filtering** | The covariance measurement update step uses square-root Cholesky filtering to prevent loss of positive-definiteness due to floating-point truncation error. |
| **Newton's Method in Optimization** | Solves $\mathbf{H}\mathbf{d} = -\mathbf{g}$ for the search direction $\mathbf{d}$. If the Hessian $\mathbf{H} \succ 0$, Cholesky provides the optimal direction. |
| **Constrained Optimization / KKT Systems** | Block-Cholesky factorization is used to solve symmetric indefinite KKT systems efficiently. |

---

## 6. Why Cholesky Beats Eigendecomposition for Sampling

Suppose you want to draw samples from a multivariate Gaussian distribution $\mathcal{N}(\mathbf{0}, \mathbf{\Sigma})$.

### Eigendecomposition Approach
$$\mathbf{\Sigma} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^\top \implies \mathbf{x} = \mathbf{Q}\mathbf{\Lambda}^{1/2}\mathbf{z}$$
*   **Computational Cost:** Full eigendecomposition requires $\mathcal{O}(n^3)$ operations with high constant factors.

### Cholesky Approach
$$\mathbf{\Sigma} = \mathbf{L}\mathbf{L}^\top \implies \mathbf{x} = \mathbf{L}\mathbf{z}$$
*   **Computational Cost:** Cholesky factorization requires $\frac{1}{3}n^3$ operations — roughly **$3\times$ faster** than eigendecomposition. Once $\mathbf{L}$ is computed, generating each new sample requires only a fast matrix-vector multiplication ($\mathcal{O}(n^2)$).

---

## The One-Sentence Summary

> **Cholesky decomposition is the efficient, lower-triangular "square root" of a symmetric positive definite matrix; it is $3\times$ cheaper than eigendecomposition or SVD, and forms the computational backbone of Gaussian sampling, Gaussian processes, and positive-definite linear system solvers in optimization.**
