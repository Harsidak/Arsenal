# Analytical Geometry Summary

This document provides a rigorous geometric perspective on the core linear algebra concepts that underpin modern Machine Learning and Deep Learning algorithms.

---

## 1. Vector Spaces, Subspaces, and Linear Independence

| Concept | What It Is | Why You Need It in ML/DL |
| :--- | :--- | :--- |
| **Vector space** | A set closed under addition and scalar multiplication. | Your feature space $\mathbb{R}^d$; embeddings (word, token, image) live here. |
| **Subspace** | A subset of a vector space that is itself a vector space (closed under linear combinations). | The column space of your data matrix (representing the space of all "reachable" linear predictions). |
| **Linear independence** | No vector in the set can be written as a linear combination of the others. | Detecting redundant features; rank deficiency in datasets. |
| **Basis** | A minimal spanning set for a vector space or subspace. | Feature selection; dimensionality reduction (coordinate system representation). |
| **Dimension** | The cardinality (size) of any basis for the space. | The intrinsic complexity of your data manifold. |

> [!IMPORTANT]
> **ML Application (Multicollinearity):** 
> If your design matrix $X$ has linearly dependent columns (features), $X^\top X$ is singular (not invertible). This is the classic multicollinearity problem in regression, which blows up the variance of estimator coefficients. It is resolved by dropping redundant features or adding L2 regularization (Ridge).

---

## 2. Inner Products, Norms, and Distances

| Concept | Formula / Definition | ML/DL Application |
| :--- | :--- | :--- |
| **Inner product** | $\langle x,y\rangle$ | Measures similarity. The dot product is the computational engine of attention mechanisms:<br>$$\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$ |
| **Norm** | $\|x\|=\sqrt{\langle x,x \rangle}$ | L2 regularization (weight decay): $\mathcal{L}_{\text{total}} = \mathcal{L} + \lambda\|w\|^2$. Also critical for tracking gradient magnitudes and normalization layers (LayerNorm, BatchNorm). |
| **Distance** | $d(x,y)=\|x-y\|$ | Used in KNN, clustering, contrastive loss formulations (e.g., SimCLR), and reconstruction error in autoencoders. |
| **Angle** | $\cos\theta=\frac{\langle x,y\rangle}{\|x\|\|y\|}$ | Cosine similarity for comparing embeddings, semantic search, and information retrieval. |

> [!TIP]
> **Key Insight:** The inner product is not just "multiply and sum." It is the geometric lens through which your model measures alignment. In self-attention, the query-key dot product literally asks: *"how much does this token point in the direction of that token?"*

---

## 3. Orthogonality and Orthogonal Projection

| Concept | Formula / Property | ML/DL Application |
| :--- | :--- | :--- |
| **Orthogonal** | $\langle x,y\rangle=0$ | Principal Component Analysis (PCA): principal components are forced to be orthogonal. Residuals in regression are orthogonal to the column space. |
| **Projection onto subspace $U$** | $\pi_U(x)=B(B^\top B)^{-1} B^\top x$ | Linear regression. The predicted values $\hat{y}$ are the orthogonal projection of target $y$ onto the column space of design matrix $X$. |
| **Orthogonal complement** | $U^\perp =\{x \mid \langle x,u\rangle=0 \;\forall u\in U\}$ | The error/residual space. In least squares, the residual vector $y-\hat{y} \in (\operatorname{col}(X))^\perp$. |

### The Linear Regression Connection (Critical Geometric Intuition)
1. You have a data matrix $X$ and targets $y$.
2. The linear model $\hat{y} = Xw$ can only produce vectors that lie in the column space $\operatorname{col}(X)$.
3. If $y \notin \operatorname{col}(X)$, no exact solution to $Xw = y$ exists.
4. The least-squares solution $\hat{w}$ is the one where $X\hat{w}$ is the **orthogonal projection** of $y$ onto $\operatorname{col}(X)$.
5. The normal equations:
   $$X^\top X \hat{w} = X^\top y \iff X^\top (y - X\hat{w}) = 0$$
   are exactly the condition that the residual vector $y - X\hat{w}$ is orthogonal to the column space of $X$. This is the geometric definition of "best fit."

```
        y (Target)
       /|
      / |  Residual (y - Xw) is orthogonal to col(X)
     /  |
    /___v______ col(X)
  Origin   Xw (Orthogonal Projection)
```

---

## 4. Projection Matrices

| Property | Formula | Meaning |
| :--- | :--- | :--- |
| **Idempotency** | $P^2 = P$ | Projecting a vector that has already been projected onto the subspace does nothing. |
| **Symmetry** | $P=P^\top$ | The projection is orthogonal (preserves angles relative to the boundary). |
| **Rank** | $\operatorname{rank}(P)=\operatorname{dim}(U)$ | Represents the degrees of freedom of the projection space (model). |

> [!NOTE]
> **ML Application (Leverage Scores):** 
> In statistics, the "hat matrix" $H=X(X^\top X)^{-1} X^\top$ is the projection matrix onto the column space of $X$. The diagonal entries $h_{ii}$ are the leverage scores. They measure how much influence each training data point has on its own prediction. High leverage ($h_{ii} \approx 1$) flags potential outliers or highly influential data points.

---

## 5. Orthonormal Bases and Gram-Schmidt

| Concept | What It Does | ML/DL Application |
| :--- | :--- | :--- |
| **Orthonormal Basis (ONB)** | A basis where all vectors are unit length ($\|v_i\|=1$) and pairwise orthogonal ($\langle v_i, v_j \rangle = 0 \;\forall i \neq j$). | Numerical stability; decorrelated features. |
| **Gram-Schmidt Process** | An algorithm to convert any arbitrary basis into an orthonormal basis. | Generates the QR decomposition ($X = QR$), which is used in:<br>- Numerically stable least-squares solvers.<br>- Orthogonal initialization of neural networks.<br>- Householder reflections in linear algebra libraries. |

> [!TIP]
> **Why we care about QR Decomposition:** 
> Computing $(X^\top X)^{-1}$ directly is numerically unstable when $X$ is ill-conditioned (i.e., has high condition number). Factorizing $X = QR$ (where $Q$ is orthogonal and $R$ is upper-triangular) allows solving $X^\top Xw = X^\top y$ using back-substitution ($Rw = Q^\top y$) without ever computing the unstable product $X^\top X$.

---

## 6. Affine Spaces

| Concept | Definition | ML/DL Application |
| :--- | :--- | :--- |
| **Affine subspace** | $L=x_0 + U$ (a translated vector subspace). | Every linear model with a bias term: $y = w^\top x + b$. The set of all predictions is an affine subspace, not a vector subspace (unless $b=0$). |
| **Affine hyperplane** | $\{x \mid w^\top x+b=0\}$ | Support Vector Machine (SVM) decision boundary. The distance from any point $x$ to this hyperplane is:<br>$$\text{Distance} = \frac{|w^\top x + b|}{\|w\|}$$ |
| **Projection onto affine space** | $x_0 + \pi_U(x-x_0)$ | Centered PCA: you translate the data to the origin ($\mu=0$), perform the orthogonal projection, and translate back. |

---

## 7. Orthogonal Transformations and Rotations

| Property | Rotation Matrix $R$ | ML/DL Application |
| :--- | :--- | :--- |
| **Length Preservation** | $R^\top R = I$ | Preserves lengths and angles during transformation. Critical for spatial data augmentation (e.g., rotating images without altering features). |
| **Orientation Preservation** | $\det(R) = +1$ | Used in 3D computer vision, robotics, and pose estimation. |
| **Eigenvalues** | Eigenvalues lie on the unit circle in $\mathbb{C}$. | Indicates no stretching or shrinking of vectors. The orthogonal matrices $U$ and $V$ in Singular Value Decomposition ($A = U\Sigma V^\top$) act as pure rotations/reflections. |

### The Singular Value Decomposition (SVD) Connection
Every matrix $A \in \mathbb{R}^{m \times n}$ factors into SVD form: $A = U\Sigma V^\top$, where $U$ and $V$ are orthogonal matrices (rotations/reflections), and $\Sigma$ is diagonal (stretching). 
*   **PCA:** The columns of $V$ represent the principal components (axes of maximum variance).
*   **Low-Rank Approximation:** Truncating $\Sigma$ to keep only the largest $k$ singular values yields the optimal rank-$k$ approximation of $A$ (Eckart-Young-Mirsky Theorem).
*   **Pseudoinverse:** $A^+ = V\Sigma^+ U^\top$ yields the minimum-norm least-squares solution to linear systems.
*   **Numerical Stability:** Because orthogonal matrices $U$ and $V$ have a condition number of exactly $1$, multiplying by them does not amplify numerical rounding errors.

---

## 8. The Cauchy-Schwarz Inequality

$$\langle x,y\rangle^2 \le \langle x,x\rangle \langle y,y\rangle \iff |\langle x,y\rangle| \le \|x\|\|y\|$$

| Application | How It Is Used |
| :--- | :--- |
| **Proving Bounds** | Mathematically guarantees that correlation coefficients (Pearson/Spearman) lie strictly within $[-1, 1]$. |
| **Kernel Methods** | Mercer's theorem for SVM kernels relies on positive semi-definiteness, which is fundamentally constrained by Cauchy-Schwarz. |
| **Optimization** | Used to derive the maximum of $w^\top x$ subject to the norm constraint $\|x\| \le c$ (the optimizer points in the direction of $w$, yielding $c\|w\|$). |
| **Generalization Bounds** | Used in PAC-Bayesian and statistical learning theory to separate target complexity terms from hypothesis complexity. |

---

## 9. The Normal Equations (The Mathematical Bridge)

$$A^\top A x = A^\top b$$

This fundamental equation connects geometry directly to optimization. It appears identically in:
*   **Linear Regression:** Analytical solution for parameters $w = (X^\top X)^{-1}X^\top y$.
*   **Weighted Least Squares:** Replacing data inner products with $X^\top W X$.
*   **Ridge Regression:** Adding the L2 diagonal penalty: $(X^\top X + \lambda I)w = X^\top y$.
*   **Newton's Optimization Method:** The quadratic approximation using the Hessian.
*   **Gauss-Newton Algorithm:** Solving non-linear least squares.
*   **Kalman Filtering:** Recursive least squares formulations.

The underlying geometric meaning remains constant: **project the target vector onto the column space spanned by your data.**

---

## Summary Checklist: What to Internalize

| # | Concept | Verification |
| :--- | :--- | :--- |
| **1** | Can you compute $B(B^\top B)^{-1} B^\top x$ by hand? | Project a 3D vector onto a 2D plane spanned by two basis vectors. |
| **2** | Can you derive the normal equation from orthogonality? | Start from the residual definition: $A^\top (b - Ax) = 0$. |
| **3** | Can you run the Gram-Schmidt process? | Orthogonalize two simple linearly independent vectors. |
| **4** | Can you spot a non-inner-product? | Check the symmetry and positive definiteness of the metric matrix $A$ in $\langle x,y\rangle_A = x^\top A y$. |
| **5** | Can you explain why PCA is a projection? | Prove that $XX^\top$ or $X^\top X$ eigenvectors span the projection subspace that maximizes variance. |
