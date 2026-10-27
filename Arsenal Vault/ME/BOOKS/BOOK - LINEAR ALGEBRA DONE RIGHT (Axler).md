# 📘 Book Note: Linear Algebra Done Right (Sheldon Axler)

> *"Determinants are difficult, non-intuitive, and often obscure the geometric and algebraic truth of linear algebra."* — Sheldon Axler

- **Author**: Sheldon Axler
- **Subject**: Pure & Abstract Linear Algebra, Operator Theory
- **Vault Location**: [[Arsenal Vault/ME/1_FOUNDATIONS/01_MATHEMATICS/Linear Algebra]]

---

## 🧠 Three Core Principles

### 1. Coordinate-Free Operator Theory
- Linear maps and operators exist independently of coordinate axes or basis choices.
- Matrices are merely secondary book-keeping devices representing an operator with respect to chosen bases; proving theorems about operators directly avoids matrix algebra gymnastics.

### 2. Elimination of Determinants (Eigenvalues via Polynomials)
- Traditional linear algebra relies on $\det(A - \lambda I) = 0$ as a crutch to define eigenvalues.
- Axler proves the existence of eigenvalues over $\mathbf{C}$ directly using polynomial factorization and the Fundamental Theorem of Algebra on the minimal polynomial of an operator $T \in \mathcal{L}(V)$.

### 3. Geometric Decomposition (Direct Sums & Invariant Subspaces)
- The structure of an operator is illuminated by decomposing the parent space into a direct sum of invariant subspaces:
  $$V = U_1 \oplus U_2 \oplus \dots \oplus U_m$$
- On each subspace $U_j$, the operator $T$ acts simply (e.g., scaling or upper-triangular action).

---

## ⚡ Application This Week

- **In [[Lab/]] (Neural Network Representation & Low-Rank Projection)**:
  - Formulate embedding space projections coordinate-free: treat layer transformations $W: V \to W$ as operators, analyzing how subspace rank constraints collapse feature variance in low-rank adaptation (LoRA).
  - Verify that weight matrices $W \in \mathbb{R}^{d_{out} \times d_{in}}$ project input tokens strictly onto $\operatorname{span}(\text{columns}(W))$.

---

## 🔗 Connected Vault Notes
- [[Vector Spaces]] — Formal algebraic axioms and operator domain
- [[Linear Independence]] — Non-redundant representations and dimension
- [[Linear Mappings]] — Operators and homomorphisms between spaces
- [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]] — Computational counterpart to Axler's abstract theory
