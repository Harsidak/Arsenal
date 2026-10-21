# Probability Mass Functions (PMF)

In [[Probability]], a **Probability Mass Function (PMF)** describes the probability distribution of a discrete [[Random Variables and Distributions|Random Variable]].

---

## 1. Mathematical Definition

Let $X$ be a discrete random variable defined on probability space $(\Omega, \mathcal{F}, P)$. The PMF of $X$, denoted $p_X$ or $P(X = x)$, is the function:
$$p_X(x) = P(X = x) = P(\{\omega \in \Omega : X(\omega) = x\})$$

### Axioms of a Valid PMF
For any valid PMF $p_X$:
1. **Non-negativity**:
   $$p_X(x) \ge 0 \quad \text{for all } x \in \mathbb{R}$$
2. **Total Mass Normalization**:
   $$\sum_{x \in \text{Support}(X)} p_X(x) = 1$$

The **Support** of $X$ is defined as the set of values where the PMF is strictly positive:
$$\text{Supp}(X) = \{x \in \mathbb{R} : p_X(x) > 0\}$$

---

## 2. Fundamental Discrete Distributions in Blitzstein Ch 3

### 1. Bernoulli Distribution: $X \sim \text{Bern}(p)$
The simplest non-trivial random variable. Models an indicator of success or failure.
* **Support**: $\{0, 1\}$
* **Parameter**: $p \in [0, 1]$
* **PMF**:
  $$p_X(x) = \begin{cases} p & \text{if } x = 1 \\ 1 - p & \text{if } x = 0 \end{cases} \quad \iff \quad p_X(x) = p^x (1-p)^{1-x} \quad \text{for } x \in \{0, 1\}$$
* **ML Connection**: Binary classification targets; outputs of a sigmoid neuron $\sigma(\mathbf{w}^T \mathbf{x} + b)$.

### 2. Binomial Distribution: $X \sim \text{Bin}(n, p)$
The number of successes in $n$ independent and identically distributed (i.i.d.) $\text{Bern}(p)$ trials.
* **Support**: $\{0, 1, 2, \dots, n\}$
* **Parameters**: $n \in \{1, 2, \dots\}$, $p \in [0, 1]$
* **PMF**:
  $$p_X(k) = P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
* **Deconstruction**:
  - $p^k (1-p)^{n-k}$: The probability of any *specific* sequence with $k$ successes and $n-k$ failures.
  - $\binom{n}{k}$: The number of distinct sequences of length $n$ containing exactly $k$ successes.

### 3. Hypergeometric Distribution: $X \sim \text{HGeom}(w, b, n)$
Sampling $n$ items **without replacement** from an urn containing $w$ white balls and $b$ black balls.
* **Support**: $\max(0, n - b) \le k \le \min(n, w)$
* **PMF**:
  $$p_X(k) = \frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$$
* **Key Distinction from Binomial**: Trials are *dependent* because the urn composition changes after every draw. When $w + b \gg n$, $\text{HGeom} \to \text{Bin}$ (Binomial approximation to Hypergeometric).

### 4. Geometric Distribution: $X \sim \text{Geom}(p)$
The number of failures before the 1st success in independent $\text{Bern}(p)$ trials (or in some conventions, the trial number of the 1st success).
* **Support**: $\{0, 1, 2, \dots\}$ (number of failures)
* **PMF**:
  $$p_X(k) = (1-p)^k p$$
* **Fundamental Property**: **Memorylessness**
  $$P(X \ge s + t \mid X \ge s) = P(X \ge t)$$

---

## 3. How to Compute Probabilities from a PMF

For any subset of values $B \subseteq \mathbb{R}$:
$$P(X \in B) = \sum_{x \in B} p_X(x)$$

---

## 🔗 Related Notes
- Preceding: [[Random Variables and Distributions]]
- Next: [[Cumulative Distribution Functions (CDF)]]
- Theoretical Core: [[Kolmogorov Axioms and Probability Spaces]]
- Root: [[Probability]]
