# Matrix Diagonalization

> [!NOTE] Source Context & References
> **Primary Textbook:** *Mathematics for Machine Learning* (Deisenroth, Faisal, Ong) — Chapter 4: Matrix Decompositions
> **Parent Category:** [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]] | [[MATHEMATICS]]
> **Related Notes:** [[TOPICS/MATRICES/Eigenvectors and Eigenspectrum|Eigenvectors and Eigenspectrum]], [[TOPICS/MATRICES/Diagonalization|Diagonalization]], [[TOPICS/MATRICES/Singular Value Decomposition|Singular Value Decomposition]], [[TOPICS/Linear Algebra/Linear Mappings|Linear Mappings]]

Diagonalization is one of the most powerful tools in linear algebra. It transforms a complex, coupled linear operator into a simple, decoupled set of scalar operations by switching to the matrix's natural coordinate system (its eigenbasis).

---

## 1. What is Diagonalization?

A square matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ is **diagonalizable** if it can be factorized as:

$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$$

Where:
*   $\mathbf{D} = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$ is a diagonal matrix containing the **eigenvalues** of $\mathbf{A}$.
*   $\mathbf{P} = [\mathbf{v}_1 \; \mathbf{v}_2 \; \cdots \; \mathbf{v}_n]$ is an invertible modal matrix whose columns are the corresponding **linearly independent eigenvectors**.

---

## 2. Why Do We Need to Diagonalize?

Diagonalization means writing $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$. Here is why this form is pure power:

### Reason 1: Matrix Powers Become Trivial
Computing raw matrix powers $\mathbf{A}^k = \underbrace{\mathbf{A} \cdot \mathbf{A} \cdots \mathbf{A}}_{k \text{ times}}$ takes $\mathcal{O}(k \cdot n^3)$ operations. But using the diagonalized form:

$$\mathbf{A}^k = (\mathbf{P}\mathbf{D}\mathbf{P}^{-1})(\mathbf{P}\mathbf{D}\mathbf{P}^{-1}) \cdots (\mathbf{P}\mathbf{D}\mathbf{P}^{-1}) = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$$

Where raising $\mathbf{D}$ to power $k$ requires raising only its diagonal entries to $k$:

$$\mathbf{D}^k = \begin{bmatrix} \lambda_1^k & 0 & \dots & 0 \\ 0 & \lambda_2^k & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n^k \end{bmatrix}$$

Instead of $\mathcal{O}(n^3)$ matrix multiplications per step, raising $\mathbf{D}$ to a power takes $\mathcal{O}(n)$ scalar exponentiations.

> [!NOTE]
> **ML Applications:** 
> *   **Markov Chains & PageRank:** Transition probability matrices $\mathbf{T}$ are exponentiated to find long-term stationary distributions ($\lim_{k \to \infty} \mathbf{T}^k$).
> *   **Graph Diffusion & Random Walks:** Modeling $k$-step information propagation across network nodes.
> *   **Recurrent Neural Networks (RNNs):** Analyzing vanishing or exploding gradients across time steps $t$ via $\mathbf{W}_h^t$.

---

### Reason 2: Arbitrary Matrix Functions & Exponentials
Just as with powers, any analytic function $f(\mathbf{A})$ defined by a Taylor series can be evaluated directly on the diagonal entries:

$$f(\mathbf{A}) = \mathbf{P} f(\mathbf{D}) \mathbf{P}^{-1} = \mathbf{P} \begin{bmatrix} f(\lambda_1) & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & f(\lambda_n) \end{bmatrix} \mathbf{P}^{-1}$$

For example, the **matrix exponential** $e^{\mathbf{A}} = \sum_{k=0}^{\infty} \frac{\mathbf{A}^k}{k!}$ becomes:
$$e^{\mathbf{A}} = \mathbf{P} \operatorname{diag}\left(e^{\lambda_1}, e^{\lambda_2}, \dots, e^{\lambda_n}\right) \mathbf{P}^{-1}$$

> [!NOTE]
> **ML Applications:** 
> *   **Continuous-Time State Space Models (SSMs / S4 / Mamba):** Solving continuous linear ODEs $\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t)$ relies on $e^{\mathbf{A}t}$.
> *   **Neural ODEs & Diffusion Models:** Continuous time feature flows and noise schedules.

---

### Reason 3: Decoupling Linear Systems
Consider a system of coupled differential or difference equations:
$$\mathbf{x}_{k+1} = \mathbf{A}\mathbf{x}_k$$

In the original standard basis, each component of $\mathbf{x}_{k+1}$ depends on all components of $\mathbf{x}_k$. By transforming variables to the eigenbasis $\mathbf{z}_k = \mathbf{P}^{-1}\mathbf{x}_k$:
$$\mathbf{P}\mathbf{z}_{k+1} = \mathbf{A}\mathbf{P}\mathbf{z}_k \implies \mathbf{z}_{k+1} = \mathbf{P}^{-1}\mathbf{A}\mathbf{P}\mathbf{z}_k = \mathbf{D}\mathbf{z}_k$$

Now the system is completely **decoupled**:
$$z_{1, k+1} = \lambda_1 z_{1, k}, \quad z_{2, k+1} = \lambda_2 z_{2, k}, \quad \dots \quad z_{n, k+1} = \lambda_n z_{n, k}$$

Each dimension evolves independently as a simple 1D scalar dynamic.

---

### Reason 4: Natural Coordinates & Variance Maximization
Diagonalization rotates your coordinate axes to align with the intrinsic geometric modes of the transformation. Off-diagonal elements represent cross-variable coupling or correlation. Diagonalizing zeros out off-diagonal interactions, leaving only pure scaling along orthogonal axes.

---

## 3. Conditions for Diagonalizability

Not every square matrix can be diagonalized.

| Condition | Criterion | Status |
| :--- | :--- | :--- |
| **General Necessary & Sufficient** | $\mathbf{A}$ has $n$ linearly independent eigenvectors. | Fully Diagonalizable ($\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$) |
| **Sufficient Condition** | $\mathbf{A}$ has $n$ distinct eigenvalues ($\lambda_i \neq \lambda_j$). | Guaranteed Diagonalizable |
| **Symmetric Matrices** | $\mathbf{A} = \mathbf{A}^\top$ (Real Symmetric). | **Orthogically Diagonalizable:** $\mathbf{A} = \mathbf{Q}\mathbf{D}\mathbf{Q}^\top$ where $\mathbf{Q}^\top = \mathbf{Q}^{-1}$ |
| **Defective Matrices** | Geometric multiplicity $<$ Algebraic multiplicity for any $\lambda_i$. | **Not Diagonalizable** (Requires Jordan Form) |

---

## 4. Step-by-Step Diagonalization Algorithm

To diagonalize an $n \times n$ matrix $\mathbf{A}$:

1.  **Find Eigenvalues:** Solve the characteristic polynomial $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ for roots $\lambda_1, \dots, \lambda_n$.
2.  **Find Eigenvectors:** For each $\lambda_i$, solve the homogeneous linear system $(\mathbf{A} - \lambda_i\mathbf{I})\mathbf{v}_i = \mathbf{0}$ to find independent basis vectors for the null space.
3.  **Construct Matrices:**
    *   Form modal matrix $\mathbf{P} = [\mathbf{v}_1 \; \mathbf{v}_2 \; \dots \; \mathbf{v}_n]$.
    *   Form diagonal matrix $\mathbf{D} = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$.
4.  **Invert Modal Matrix:** Compute $\mathbf{P}^{-1}$ (or simply $\mathbf{P}^\top$ if $\mathbf{P}$ is orthogonal).

---

## 5. Where Diagonalization Appears Across ML / DL

| ML / DL Domain | Role of Diagonalization |
| :--- | :--- |
| **Principal Component Analysis (PCA)** | Diagonalizes the sample covariance matrix $\mathbf{\Sigma} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^\top$. The diagonal entries $\lambda_i$ give feature variances; columns of $\mathbf{Q}$ give orthogonal feature projections. |
| **Spectral Graph Theory & GNNs** | Diagonalizes the Graph Laplacian $\mathbf{L} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^\top$ to define Fourier transforms on graphs and graph convolutions ($g_\theta * x = \mathbf{U} g_\theta(\mathbf{\Lambda}) \mathbf{U}^\top x$). |
| **Modern State Space Models (Mamba/S4)** | Diagonalizes state transition matrices $\mathbf{A}$ to turn $\mathcal{O}(N L)$ sequence updates into $\mathcal{O}(L \log L)$ parallel FFT convolutions. |
| **Matrix Whitening & Decorrelation** | Zero-phase component analysis (ZCA) uses $\mathbf{\Sigma}^{-1/2} = \mathbf{P}\mathbf{D}^{-1/2}\mathbf{P}^\top$ to decorrelate features while preserving scale. |

---

## The One-Sentence Takeaway
> **Diagonalization uncouples complex matrix interactions into independent 1D scalar operations along the eigenbasis, turning $\mathcal{O}(n^3)$ matrix powers and differential systems into trivial $\mathcal{O}(n)$ elementwise calculations.**
