# Singular Value Decomposition (SVD)

> [!NOTE] Source Context & References
> **Primary Textbook:** *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — Chapter 4: Matrix Decompositions
> **Parent Category:** [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]] | [[MATHEMATICS]]
> **Related Notes:** [[Geometric Intuition of SVD|Geometric Intuition of SVD]], [[Eigenvectors and Eigenspectrum|Eigenvectors and Eigenspectrum]], [[Diagonalization|Diagonalization]], [[Cholesky Decomposition|Cholesky Decomposition]], [[Analytical Geometry Summary|Analytical Geometry Summary]]

Singular Value Decomposition (SVD) is the universal matrix decomposition. It generalizes eigendecomposition to non-square, non-symmetric matrices of any rank.

---

## 1. The Core Problem

Eigendecomposition ($\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$) only works for square matrices ($n \times n$). However, in Machine Learning, your data matrix $\mathbf{X} \in \mathbb{R}^{m \times n}$ is almost never square ($m$ samples, $n$ features, typically $m \neq n$). 

SVD resolves this fundamental limitation by generalizing matrix diagonalization to any rectangular matrix.

---

## 2. Definition

For any real matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ (of any shape and rank), there exists a factorization:

$$\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$$

Where:
*   $\mathbf{U} \in \mathbb{R}^{m \times m}$ is an **orthogonal matrix** ($\mathbf{U}^\top\mathbf{U} = \mathbf{I}_m$). Columns $\mathbf{u}_i$ are called **left singular vectors**.
*   $\mathbf{V} \in \mathbb{R}^{n \times n}$ is an **orthogonal matrix** ($\mathbf{V}^\top\mathbf{V} = \mathbf{I}_n$). Columns $\mathbf{v}_i$ are called **right singular vectors**.
*   $\mathbf{\Sigma} \in \mathbb{R}^{m \times n}$ is a **rectangular diagonal matrix** containing non-negative real singular values sorted in descending order:
    $$\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_{\min(m,n)} \ge 0$$

---

## 3. The Compact (Reduced) SVD

If $\operatorname{rank}(\mathbf{A}) = r \le \min(m, n)$, only the first $r$ singular values are strictly positive ($\sigma_r > 0$, $\sigma_{r+1} = \dots = 0$). We can drop the zero singular values and write the **Compact SVD**:

$$\mathbf{A} = \mathbf{U}_r \mathbf{\Sigma}_r \mathbf{V}_r^\top$$

Where:
*   $\mathbf{U}_r \in \mathbb{R}^{m \times r}$ has $r$ orthonormal columns.
*   $\mathbf{\Sigma}_r \in \mathbb{R}^{r \times r} = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$ is strictly positive diagonal.
*   $\mathbf{V}_r \in \mathbb{R}^{n \times r}$ has $r$ orthonormal columns.

> [!TIP]
> Compact SVD is the form used in computational libraries. The full matrices $\mathbf{U}$ and $\mathbf{V}$ contain extra orthonormal basis vectors that are multiplied by zero singular values in full SVD, wasting memory.

---

## 4. Connection to Eigendecomposition

SVD on $\mathbf{A} \in \mathbb{R}^{m \times n}$ is intimately connected to the eigendecomposition of the square symmetric matrices $\mathbf{A}^\top\mathbf{A}$ and $\mathbf{A}\mathbf{A}^\top$:

| Attribute | Eigendecomposition of $\mathbf{A}^\top\mathbf{A}$ | Eigendecomposition of $\mathbf{A}\mathbf{A}^\top$ | SVD of $\mathbf{A}$ |
| :--- | :--- | :--- | :--- |
| **Matrix** | $\mathbf{A}^\top\mathbf{A} \in \mathbb{R}^{n \times n}$ | $\mathbf{A}\mathbf{A}^\top \in \mathbb{R}^{m \times m}$ | $\mathbf{A} \in \mathbb{R}^{m \times n}$ |
| **Eigenvectors** | $\mathbf{V}$ (Right singular vectors) | $\mathbf{U}$ (Left singular vectors) | Both $\mathbf{U}$ and $\mathbf{V}$ |
| **Eigenvalues** | $\lambda_i = \sigma_i^2$ | $\lambda_i = \sigma_i^2$ | Singular values $\sigma_i = \sqrt{\lambda_i}$ |
| **Matrix Type** | Symmetric, positive semi-definite | Symmetric, positive semi-definite | General (any shape/rank) |

### Mathematical Proof Sketch
Starting from SVD $\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$:
$$\mathbf{A}^\top\mathbf{A} = (\mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top)^\top (\mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top) = \mathbf{V}\mathbf{\Sigma}^\top \mathbf{U}^\top \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top = \mathbf{V}(\mathbf{\Sigma}^\top\mathbf{\Sigma})\mathbf{V}^\top = \mathbf{V}\mathbf{\Sigma}^2\mathbf{V}^\top$$

This is precisely the orthogonal eigendecomposition of $\mathbf{A}^\top\mathbf{A}$. The eigenvectors are the columns of $\mathbf{V}$, and the eigenvalues are $\lambda_i = \sigma_i^2$.
Similarly, $\mathbf{A}\mathbf{A}^\top = \mathbf{U}\mathbf{\Sigma}^2\mathbf{U}^\top$.

---

## 5. Why SVD Is More General Than Eigendecomposition

| Feature | Eigendecomposition ($\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$) | SVD ($\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$) |
| :--- | :--- | :--- |
| **Non-square matrices ($m \neq n$)?** | ❌ No | ✅ Yes |
| **Non-symmetric matrices?** | ❌ No (yields complex eigenvalues) | ✅ Yes |
| **Values always real & non-negative?** | ❌ No (eigenvalues can be negative/complex) | ✅ Yes ($\sigma_i \ge 0$) |
| **Vectors always orthonormal?** | ❌ No (requires symmetric matrix) | ✅ Yes ($\mathbf{U}^\top\mathbf{U}=\mathbf{I}$, $\mathbf{V}^\top\mathbf{V}=\mathbf{I}$) |
| **Numerical Stability** | ⚠️ Less stable (squaring condition number) | ✅ Highly stable |

> [!IMPORTANT]
> SVD is the gold standard of numerical linear algebra. If a computation can be framed using SVD, it generally should be.

---

## 6. Key Properties & Matrix Norms

| Property | Formula / Statement | Meaning in ML |
| :--- | :--- | :--- |
| **Rank** | $\operatorname{rank}(\mathbf{A}) = \text{number of } \sigma_i > 0$ | The effective intrinsic dimensionality of the matrix. |
| **Frobenius Norm** | $\|\mathbf{A}\|_F^2 = \sum_{i=1}^r \sigma_i^2 = \operatorname{tr}(\mathbf{A}^\top\mathbf{A})$ | Total "energy" or variance contained in the matrix. |
| **Spectral Norm** | $\|\mathbf{A}\|_2 = \sigma_1$ (largest singular value) | Maximum stretching factor under linear transformation. |
| **Condition Number** | $\kappa(\mathbf{A}) = \frac{\sigma_1}{\sigma_r}$ | Measures matrix ill-conditioning (sensitivity to numerical perturbations). |
| **Moore-Penrose Pseudoinverse** | $\mathbf{A}^+ = \mathbf{V}_r \mathbf{\Sigma}_r^{-1} \mathbf{U}_r^\top$ | Generalizes matrix inverse to non-square and rank-deficient matrices. |
| **Best Low-Rank Approximation** | $\mathbf{A}_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^\top$ | Optimal rank-$k$ matrix minimizing $\|\mathbf{A} - \mathbf{A}_k\|_F$ and $\|\mathbf{A} - \mathbf{A}_k\|_2$. |

---

## 7. The Eckart-Young-Mirsky Theorem (Low-Rank Approximation)

**Theorem:** The optimal rank-$k$ approximation ($k < r$) to $\mathbf{A}$ under both the Frobenius norm and the spectral norm is obtained by truncating the SVD to the top-$k$ singular values:

$$\mathbf{A}_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^\top = \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^\top$$

**Approximation Error:**
$$\|\mathbf{A} - \mathbf{A}_k\|_F^2 = \sum_{i=k+1}^r \sigma_i^2$$
$$\|\mathbf{A} - \mathbf{A}_k\|_2 = \sigma_{k+1}$$

> [!NOTE]
> **Significance:** This is not just a heuristic approximation—it is **provably optimal**. No other rank-$k$ matrix in $\mathbb{R}^{m \times n}$ is closer to $\mathbf{A}$.

---

## 8. Where SVD Appears in ML/DL

| Application | How SVD Is Used |
| :--- | :--- |
| **Principal Component Analysis (PCA)** | Center data $\mathbf{X}$. SVD of $\mathbf{X} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$: right singular vectors $\mathbf{V}$ are principal components; $\frac{\sigma_i^2}{m-1}$ are feature variances. |
| **Latent Semantic Analysis (LSA)** | SVD of term-document frequency matrix to extract latent semantic concepts in NLP. |
| **Collaborative Filtering** | Low-rank SVD factorization of sparse user-item rating matrices (Netflix Prize benchmark). |
| **Image & Model Compression** | Truncate SVD to top-$k$ singular values to compress images or deep learning weight matrices. |
| **Spectral Normalization (GANs)** | Divide weight matrix $\mathbf{W}$ by its top singular value $\sigma_1(\mathbf{W})$ to enforce a 1-Lipschitz constraint. |
| **Data Whitening** | $\mathbf{X}_{\text{white}} = \mathbf{U} \mathbf{\Sigma}^{-1} \mathbf{U}^\top \mathbf{X}$ decorrelates features and standardizes variances. |
| **Pseudoinverse & Least Squares** | Solves overdetermined/underdetermined systems $\mathbf{X}\mathbf{w} = \mathbf{y}$ via $\mathbf{w} = \mathbf{X}^+\mathbf{y} = \mathbf{V}_r \mathbf{\Sigma}_r^{-1} \mathbf{U}_r^\top \mathbf{y}$. |

---

## 9. The Truncated SVD Algorithm

In practice, full SVD ($\mathcal{O}(\min(mn^2, m^2n))$) is rarely computed for large datasets. Instead, **Truncated SVD** computes only the top-$k$ singular components:

*   **Algorithms:** Randomized SVD (Halko et al.) or Lanczos iteration.
*   **Computational Complexity:** $\mathcal{O}(mnk)$ instead of $\mathcal{O}(mn^2)$.
*   **Implementations:** `scipy.sparse.linalg.svds` or `sklearn.decomposition.TruncatedSVD`.

---

## 10. SVD vs. Eigendecomposition for PCA

| Approach | Algorithm Steps | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Eigendecomposition** | Compute covariance $\mathbf{\Sigma} = \frac{1}{m} \mathbf{X}^\top\mathbf{X}$, then eigendecompose $\mathbf{\Sigma}$. | Directly yields covariance eigenvalues. | Computing $\mathbf{X}^\top\mathbf{X}$ costs $\mathcal{O}(mn^2)$ and **squares the condition number** ($\kappa(\mathbf{X}^\top\mathbf{X}) = \kappa(\mathbf{X})^2$). |
| **SVD** | Center $\mathbf{X}$, then compute SVD directly: $\mathbf{X} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$. | Highly numerically stable; avoids squaring condition number; works seamlessly when $m < n$. | Slightly higher flop count for small $n$. |

> [!TIP]
> **Rule of Thumb:** Always use SVD for PCA. It avoids loss of numerical precision and works reliably when feature count exceeds sample count ($n > m$).

---

## The One-Sentence Summary

> **SVD is the universal matrix factorisation that decomposes any matrix into orthogonal rotations and a diagonal scaling, generalizing eigendecomposition to non-square and non-symmetric matrices to serve as the computational engine for PCA, low-rank approximation, pseudoinverses, and spectral regularization in deep learning.**
