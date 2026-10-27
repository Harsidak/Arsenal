# 🌐 Span and Bases

> [!NOTE] Source Context
> Sheldon Axler, *Linear Algebra Done Right* (Chapter 2: Finite-Dimensional Vector Spaces). Cross-references: [[Vector Spaces]], [[Vector Subspaces]], [[Linear Independence]], [[BOOK - LINEAR ALGEBRA DONE RIGHT (Axler)]].

---

## 1. Linear Combinations & Span

Let $v_1, v_2, \dots, v_m$ be a list of vectors in a vector space $V$ over a field $\mathbf{F}$ ($\mathbf{R}$ or $\mathbf{C}$).

### 🔹 Linear Combination
A **linear combination** of $(v_1, \dots, v_m)$ is any vector of the form:
$$a_1 v_1 + a_2 v_2 + \dots + a_m v_m$$
where $a_1, a_2, \dots, a_m \in \mathbf{F}$.

### 🔹 Span (Reachable Territory)
The **span** of $(v_1, \dots, v_m)$ is the set of *all* possible linear combinations:
$$\operatorname{span}(v_1, \dots, v_m) = \{ a_1 v_1 + \dots + a_m v_m : a_1, \dots, a_m \in \mathbf{F} \}$$

---

## 2. Axler's Smallest Subspace Theorem

> **Theorem**: The span of any list of vectors $(v_1, \dots, v_m)$ in $V$ is the **smallest subspace of $V$ containing $v_1, \dots, v_m$**.

### Why this is mathematically rigorous:
1. **It is a subspace**:
   - Setting all scalars $a_i = 0$ yields the zero vector $\vec{0} \in \operatorname{span}(v_1, \dots, v_m)$.
   - Sum of two linear combinations is another linear combination (closed under addition).
   - Scaling a linear combination produces another linear combination (closed under scalar multiplication).
2. **It is minimal**: Any subspace containing $v_1, \dots, v_m$ must, by the closure axioms of a vector space, contain all linear combinations of those vectors. Hence, no subspace containing the vectors can be smaller than their span.

### The Empty List Boundary
$$\operatorname{span}() = \{ \vec{0} \}$$
*Why not $\emptyset$?* Every subspace must contain the additive identity $\vec{0}$. The smallest subspace of any vector space is $\{\vec{0}\}$. Furthermore, an empty sum of vectors is defined algebraically as the identity element $\vec{0}$.

---

## 3. The Linear Dependence Lemma (Axler 2.21)

The workhorse engine of finite-dimensional linear algebra:

> If $(v_1, \dots, v_m)$ is **linearly dependent** in $V$, then there exists an index $j \in \{1, 2, \dots, m\}$ such that:
> 1. **$v_j \in \operatorname{span}(v_1, \dots, v_{j-1})$**: The $j$-th vector is redundant baggage trapped in the span of its predecessors.
> 2. **$\operatorname{span}(v_1, \dots, \widehat{v_j}, \dots, v_m) = \operatorname{span}(v_1, \dots, v_m)$**: Pruning $v_j$ from the list preserves the reachable territory without losing a single point.

### The Left-to-Right Scanner Proof:
Since the list is dependent, $\sum_{i=1}^m a_i v_i = \vec{0}$ with some non-zero scalars. Let $j$ be the largest index with $a_j \neq 0$. Then:
$$v_j = -\frac{a_1}{a_j}v_1 - \dots - \frac{a_{j-1}}{a_j}v_{j-1} \in \operatorname{span}(v_1, \dots, v_{j-1})$$

---

## 4. The Basis (The "Goldilocks" Balance)

A list of vectors $(v_1, \dots, v_n)$ in $V$ is a **basis** of $V$ if it satisfies two simultaneous criteria:
1. **Linearly Independent** (Zero waste / no redundancy).
2. **Spans $V$** (Zero gaps / full coverage of $V$).

```
            Spanning List                     Linearly Independent List
       (Covers space, has waste)               (Zero waste, has gaps)
                  ▲                                      ▲
                  │                                      │
          [Prune via Lemma]                       [Extend by v ∉ span]
                  │                                      │
                  └──────────────► BASIS ◄───────────────┘
                              (Just right)
```

### 🔑 Unique Representation Theorem
A list $(v_1, \dots, v_n)$ is a basis of $V$ **if and only if** every $v \in V$ can be uniquely written in the form:
$$v = c_1 v_1 + c_2 v_2 + \dots + c_n v_n$$
for unique scalars $c_1, \dots, c_n \in \mathbf{F}$.

### ⚖️ Minimal vs. Maximal Duality
- A basis is a **minimal spanning list**: Removing any single vector shrinks the span below $V$.
- A basis is a **maximal linearly independent list**: Appending any new vector makes the list linearly dependent.

---

## 🔗 Related Notes
- [[Vector Spaces]] — Vector space axioms and operator domain
- [[Vector Subspaces]] — Subspaces and direct sums
- [[Linear Independence]] — Formal zero-test and pivot analysis
- [[BOOK - LINEAR ALGEBRA DONE RIGHT (Axler)]] — Conceptual theoretical source
