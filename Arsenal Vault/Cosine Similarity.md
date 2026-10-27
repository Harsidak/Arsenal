# Cosine Similarity

> [!NOTE] Context
> Measures directional alignment between vectors, ignoring length. Extends [[Inner product]] and [[Lengths and Distances]] for text embeddings, [[RAG]], and search. Reference: [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]].

---

## 1. Definition

For two non-zero vectors $u, v \in \mathbb{R}^d$:

$$S_C(u, v) = \frac{\langle u, v \rangle}{\lVert u \rVert_2 \lVert v \rVert_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum_{i=1}^d u_i^2} \sqrt{\sum_{i=1}^d v_i^2}} = \cos(\theta)$$

* **Range**: $[-1, 1]$.
* **$+1$ ($\theta = 0^\circ$)**: Pointing in the exact same direction.
* **$0$ ($\theta = 90^\circ$)**: Perpendicular (orthogonal, no linear relation).
* **$-1$ ($\theta = 180^\circ$)**: Pointing in the exact opposite direction.

---

## 2. Why We Use It

Standard dot product mixes two things:
1. **Direction** (what the vector represents)
2. **Length / Magnitude** (how big the numbers are, e.g., document word count)

Cosine similarity divides out the length, so only direction matters:
$$S_C(\alpha u, \beta v) = S_C(u, v) \quad \text{for any positive scalars } \alpha, \beta > 0$$

This is equivalent to normalizing both vectors to length 1 and taking their dot product:
$$\hat{u} = \frac{u}{\lVert u \rVert_2}, \quad \hat{v} = \frac{v}{\lVert v \rVert_2} \implies S_C(u, v) = \hat{u}^\top \hat{v}$$

---

## 3. Connection to Euclidean Distance

For unit vectors ($\lVert \hat{u} \rVert = \lVert \hat{v} \rVert = 1$):
$$\lVert \hat{u} - \hat{v} \rVert_2^2 = 2 - 2 S_C(u, v)$$

* Higher cosine similarity means smaller Euclidean distance on the unit sphere.
* In vector search databases, if vectors are normalized when stored, finding the closest cosine neighbor is identical to finding the closest Euclidean neighbor using fast matrix multiplication.

---

## 4. Cosine Distance

Often defined as:
$$D_C(u, v) = 1 - S_C(u, v)$$

* Ranges from $0$ (identical direction) to $2$ (opposite direction).
* **Note**: It violates the triangle inequality, so it is a pseudo-distance, not a true metric. True geometric distance along the sphere is the angle $\theta = \arccos(S_C(u, v))$.

---

## 5. When to Use & When Not to Use

* **Use when**:
  * Comparing embeddings (text, audio, image) where length depends on token count or volume, but direction carries the meaning.
  * Document search / [[RAG]].
* **Do not use when**:
  * Magnitude represents real physical value (e.g., speed, price, salary).
  * Uncentered ratings (like 1 to 5 stars) — center by subtracting user mean first (which turns it into Pearson correlation).

---

**Related Notes**:
* [[Inner product]]
* [[Lengths and Distances]]
* [[Norms]]
* [[RAG]]
* [[BOOK - MATHEMATICS FOR MACHINE LEARNING (Deisenroth)]]
