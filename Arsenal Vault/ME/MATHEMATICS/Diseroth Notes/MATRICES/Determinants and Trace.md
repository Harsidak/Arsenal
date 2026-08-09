# Determinants and Trace

> [!NOTE] Source Context & References
> **Primary Textbook:** *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — Chapter 4: Matrix Decompositions
> **Parent Category:** [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]] | [[MATHEMATICS]]
> **Related Notes:** [[Eigenvectors and Eigenspectrum|Eigenvectors and Eigenspectrum]], [[Diagonalization|Diagonalization]], [[Cholesky Decomposition|Cholesky Decomposition]], [[Analytical Geometry Summary|Analytical Geometry Summary]]

This note places **traces** and **determinants** on the mathematical landscape, exploring their definitions, first-principles geometry, properties, and direct applications in Machine Learning and Deep Learning.

---

# 1. Traces: The Infinitesimal Scaling

## Definition
For a square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$:
$$\text{tr}(\mathbf{A}) = \sum_{i=1}^{n} a_{ii}$$

The sum of the diagonal entries.

---

## Why This Definition? (The First-Principles Question)
You might ask: why care about the sum of diagonal entries? The answer emerges from what the trace actually measures.

**Geometric Meaning:** The trace represents the **infinitesimal change in volume** under the flow of a linear vector field. More concretely, if you flow a small volume element along the vector field defined by $\mathbf{x}' = \mathbf{A}\mathbf{x}$, the rate at which that volume grows or shrinks is exactly $\text{tr}(\mathbf{A})$.

---

## Key Properties (Memorize These)

| Property | Formula / Property | Why It Matters |
| :--- | :--- | :--- |
| **Linearity** | $\text{tr}(\mathbf{A} + \mathbf{B}) = \text{tr}(\mathbf{A}) + \text{tr}(\mathbf{B})$ | Simplifies expectations and variances of random matrix variables. |
| **Scalar Multiplication** | $\text{tr}(c\mathbf{A}) = c \cdot \text{tr}(\mathbf{A})$ | Self-explanatory scaling behavior. |
| **Cyclic Invariance** | $\text{tr}(\mathbf{ABC}) = \text{tr}(\mathbf{BCA}) = \text{tr}(\mathbf{CAB})$ | **Critical.** Lets you cyclicly reorder matrix products inside a trace. The matrices do not need to commute, but their cyclic order must be preserved. |
| **Transpose** | $\text{tr}(\mathbf{A}^\top) = \text{tr}(\mathbf{A})$ | The diagonal is invariant under transposition. |
| **Similarity Invariance** | $\text{tr}(\mathbf{P}^{-1}\mathbf{AP}) = \text{tr}(\mathbf{A})$ | Shows that the trace is basis-independent; it is a property of the operator itself. |
| **Eigenvalue Connection** | $\text{tr}(\mathbf{A}) = \sum_{i=1}^{n} \lambda_i$ | The trace equals the sum of the eigenvalues (counting algebraic multiplicity). |

---

## The Eigenvalue Connection: Why It Works
If $\mathbf{A}$ has eigenvalues $\lambda_1, \dots, \lambda_n$ (counting multiplicity), then:
$$\text{tr}(\mathbf{A}) = \sum_{i=1}^{n} \lambda_i$$

**Why?** The characteristic polynomial of $\mathbf{A}$ is:
$$\det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^n - \text{tr}(\mathbf{A})\lambda^{n-1} + \dots + (-1)^n \det(\mathbf{A})$$

The coefficient of $\lambda^{n-1}$ is $-\text{tr}(\mathbf{A})$. However, this polynomial can also be factored directly using its roots (the eigenvalues):
$$(\lambda - \lambda_1)(\lambda - \lambda_2)\cdots(\lambda - \lambda_n) = \lambda^n - \left(\sum_{i=1}^n \lambda_i\right)\lambda^{n-1} + \dots$$

Matching the coefficients of $\lambda^{n-1}$ yields: $\text{tr}(\mathbf{A}) = \sum \lambda_i$.
Because eigenvalues are basis-independent, the trace is a **spectral invariant**.

---

## Where Traces Appear in ML/DL

| Application | How the Trace Appears |
| :--- | :--- |
| **Frobenius Norm** | $\|\mathbf{A}\|_F^2 = \text{tr}(\mathbf{A}^\top\mathbf{A}) = \sum_{i,j} a_{ij}^2$ (standard matrix norm squared). |
| **Covariance Matrices** | $\text{tr}(\mathbf{\Sigma}) = \sum \sigma_i^2 = \text{total variance}$ of the dataset. |
| **PCA** | The proportion of variance explained by the top $k$ principal components is: $\frac{\sum_{i=1}^k \lambda_i}{\text{tr}(\mathbf{\Sigma})}$. |
| **Matrix Calculus** | Fundamental derivative rules: $\frac{\partial}{\partial \mathbf{X}} \text{tr}(\mathbf{AX}) = \mathbf{A}^\top$. |
| **Information Theory** | The KL divergence between two multivariate Gaussians $\mathcal{N}(\boldsymbol{\mu}_1, \mathbf{\Sigma}_1)$ and $\mathcal{N}(\boldsymbol{\mu}_2, \mathbf{\Sigma}_2)$ contains a $\text{tr}(\mathbf{\Sigma}_2^{-1}\mathbf{\Sigma}_1)$ scaling term. |
| **Neural Regularization** | The Nuclear Norm (inducing low-rank matrices) is $\|\mathbf{A}\|_* = \text{tr}(\sqrt{\mathbf{A}^\top\mathbf{A}})$, which is the sum of singular values. |

---

## The Matrix Calculus Rule (Critical for Backpropagation)
$$\frac{\partial}{\partial \mathbf{X}} \text{tr}(\mathbf{AX}) = \mathbf{A}^\top$$

More generally:
$$\frac{\partial}{\partial \mathbf{X}} \text{tr}(\mathbf{AXB}) = \mathbf{A}^\top\mathbf{B}^\top$$

This is the workhorse of deriving gradients in matrix form. Instead of expanding equations into individual scalar components, you manipulate traces.

**Example (Gradient of L2/Frobenius Regularization):**
$$\mathcal{R}(\mathbf{X}) = \|\mathbf{X}\|_F^2 = \text{tr}(\mathbf{X}^\top\mathbf{X})$$
Using differentials:
$$d\,\text{tr}(\mathbf{X}^\top\mathbf{X}) = \text{tr}(d(\mathbf{X}^\top\mathbf{X})) = \text{tr}((d\mathbf{X})^\top\mathbf{X} + \mathbf{X}^\top d\mathbf{X}) = 2\,\text{tr}(\mathbf{X}^\top d\mathbf{X})$$
$$\implies \frac{\partial}{\partial \mathbf{X}} \text{tr}(\mathbf{X}^\top\mathbf{X}) = 2\mathbf{X}$$

---

# 2. Determinants: The Volume Scaler

## Definition
For a square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$, the determinant $\det(\mathbf{A})$ maps the matrix to a scalar:
$$\det(\mathbf{A}) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n a_{i, \sigma(i)}$$
(where $S_n$ is the set of all permutations of $\{1, \dots, n\}$).

---

## Why This Definition? (First-Principles Geometry)

**Geometric Meaning:** The determinant measures the **signed volume scaling factor** of the transformation.
If you take a unit hypercube in $\mathbb{R}^n$ and apply the transformation $\mathbf{A}$, the volume of the resulting parallelotope is exactly $|\det(\mathbf{A})|$.
*   **$\det(\mathbf{A}) > 0$:** The transformation preserves the orientation of space.
*   **$\det(\mathbf{A}) < 0$:** The transformation reverses the orientation of space (e.g., a reflection).
*   **$\det(\mathbf{A}) = 0$:** The transformation collapses space into a lower dimension. This is why $\det(\mathbf{A}) = 0 \iff \mathbf{A}$ is singular (non-invertible).

```
     3D Space           Linear Map A          Collapsed 2D Plane
      ┌───┐                 ───>                   / / /
      │   │ (Volume = V)                          / / /  (Volume = 0)
      └───┘                                      / / / 
   det(A) > 0                                  det(A) = 0
```

---

## Key Properties (Memorize These)

| Property | Formula | Why It Matters |
| :--- | :--- | :--- |
| **Product Rule** | $\det(\mathbf{AB}) = \det(\mathbf{A})\det(\mathbf{B})$ | Allows decomposing complex transformations. |
| **Transpose** | $\det(\mathbf{A}^\top) = \det(\mathbf{A})$ | Transposing does not alter volume scaling. |
| **Inverse** | $\det(\mathbf{A}^{-1}) = \frac{1}{\det(\mathbf{A})}$ | Inverting scales volume by the reciprocal factor. |
| **Scalar Scaling** | $\det(c\mathbf{A}) = c^n \det(\mathbf{A})$ | Scaling an $n$-dimensional space by $c$ changes volume by $c^n$. |
| **Eigenvalue Product** | $\det(\mathbf{A}) = \prod_{i=1}^n \lambda_i$ | The product of all eigenvalues. |
| **Similarity Invariance** | $\det(\mathbf{P}^{-1}\mathbf{AP}) = \det(\mathbf{A})$ | Basis-independent spectral invariant. |

---

## Where Determinants Appear in ML/DL

### 1. Probability Density Normalization (Multivariate Gaussian)
The probability density function of a multivariate Gaussian $\mathcal{N}(\boldsymbol{\mu}, \mathbf{\Sigma})$ is:
$$p(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n \det(\mathbf{\Sigma})}} \exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top \mathbf{\Sigma}^{-1} (\mathbf{x}-\boldsymbol{\mu})\right)$$
*   **Geometric Role:** The term $\det(\mathbf{\Sigma})$ acts as the normalization factor. It measures the "total volume" of the covariance ellipsoid. High determinant $\implies$ high uncertainty/spread.

### 2. Generative Modeling: Normalizing Flows (Change of Variables)
In generative modeling, Normalizing Flows map simple distributions $p_Z(\mathbf{z})$ to complex data distributions $p_X(\mathbf{x})$ via bijective functions $\mathbf{x} = f(\mathbf{z})$.
The probability density changes according to:
$$p_X(\mathbf{x}) = p_Z(f^{-1}(\mathbf{x})) \cdot \left| \det \mathbf{J}_{f^{-1}}(\mathbf{x}) \right| = p_Z(f^{-1}(\mathbf{x})) \cdot \left| \det \left( \frac{\partial f^{-1}(\mathbf{x})}{\partial \mathbf{x}} \right) \right|$$
*   **Geometric Role:** The determinant of the Jacobian matrix $\mathbf{J}$ scales the density to account for how much local space is stretched or compressed by the transformation. Modern flow models (like RealNVP) are designed to have triangular Jacobians so that computing this determinant is efficient ($\mathcal{O}(n)$ product of diagonal elements).

### 3. Optimization & Log-Determinant Gradients
In maximum likelihood estimation (MLE) of covariance matrices, we often maximize terms involving the log-determinant:
$$\mathcal{L}(\mathbf{\Sigma}) = -\ln\det(\mathbf{\Sigma}) - \text{tr}(\mathbf{\Sigma}^{-1}\mathbf{S})$$
Applying matrix calculus:
$$\frac{\partial}{\partial \mathbf{X}} \ln \det(\mathbf{X}) = \mathbf{X}^{-\top}$$

---

# 3. The Log-Det Relationship (The Bridge)

For a symmetric positive definite matrix $\mathbf{X}$ (or using matrix exponentials generally):
$$\det(e^{\mathbf{A}}) = e^{\text{tr}(\mathbf{A})} \iff \ln \det(\mathbf{X}) = \text{tr}(\ln \mathbf{X})$$

This fundamental identity connects the product of eigenvalues (determinant) to the sum of eigenvalues (trace) via the logarithm. It is heavily exploited in Gaussian Graphical Models and variational inference to compute expensive determinant operations using trace properties.

---

## The One-Sentence Summary
> **The trace is the sum of eigenvalues (governing infinitesimal volume change and matrix calculus), while the determinant is the product of eigenvalues (governing absolute volume scaling and invertibility); they are bridged by the identity $\ln \det(\mathbf{X}) = \text{tr}(\ln \mathbf{X})$.**
