# 🔢 Complex Numbers ($\mathbf{C}$)

> [!NOTE] Source Reference
> Sheldon Axler, *Linear Algebra Done Right* (Chapter 1.A). Cross-references: [[Vector Spaces]], [[BOOK - LINEAR ALGEBRA DONE RIGHT (Axler)]].

---

## 1. Formal Definition

A **complex number** is an ordered pair $(a, b)$, where $a, b \in \mathbf{R}$, customarily written as:
$$z = a + bi$$
where $i$ is the imaginary unit satisfying $i^2 = -1$.

The set of all complex numbers is denoted by $\mathbf{C}$:
$$\mathbf{C} = \{ a + bi : a, b \in \mathbf{R} \}$$

---

## 2. Fundamental Operations

For any two complex numbers $z_1 = a + bi$ and $z_2 = c + di$ with $a, b, c, d \in \mathbf{R}$:

### ➕ Addition
$$(a + bi) + (c + di) = (a + c) + (b + d)i$$
*   **Properties**: Commutative, associative, has additive identity $0 = 0 + 0i$, and every element has an additive inverse $-(a + bi) = (-a) + (-b)i$.

### ✖️ Multiplication
$$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$
*   **Properties**: Commutative, associative, distributive over addition, has multiplicative identity $1 = 1 + 0i$.
*   Every non-zero $z = a + bi$ has a unique multiplicative inverse:
    $$z^{-1} = \frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2}i$$

---

## 3. Role in Linear Algebra

In Sheldon Axler's *Linear Algebra Done Right*, $\mathbf{C}$ serves as the primary scalar field ($\mathbf{F} = \mathbf{C}$):
- **Fundamental Theorem of Algebra**: Every non-constant polynomial with complex coefficients has a root in $\mathbf{C}$.
- **Consequence for Operators**: Over $\mathbf{C}$, every linear operator on a finite-dimensional non-zero vector space has at least one **eigenvalue**. This guarantees upper-triangular matrix representations without needing determinants.

---

## 🔗 Related Notes
- [[Vector Spaces]] — Vector spaces over $\mathbf{F} = \mathbf{R}$ or $\mathbf{C}$
- [[Linear Independence]] — Independent directions in vector spaces
- [[Eigenvectors and Eigenspectrum]] — Spectral decomposition enabled by $\mathbf{C}$
