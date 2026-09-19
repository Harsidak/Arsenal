# Feature Transformation & Scaling

Before training any machine learning model, numerical features must be scaled and transformed. This ensures numerical stability, accelerates gradient convergence, and allows distance-based metrics to operate correctly.

---

## 1. Skewness Reduction (Power Transformations)

Linear models and neural networks assume homoscedasticity and symmetric errors. Severely skewed features warp the loss landscape, creating valleys with unbalanced gradients.

### Box-Cox Transformation
A parametric power transformation that stabilizes variance and normalizes data.

$$y_i^{(\lambda)} = \begin{cases} \frac{y_i^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0 \\ \ln(y_i) & \text{if } \lambda = 0 \end{cases}$$

*   **Constraint:** Requires all input values to be strictly positive ($y_i > 0$).

### Yeo-Johnson Transformation
An extension of the Box-Cox transformation that allows for zero and negative values.

$$\psi(\lambda, y) = \begin{cases} \frac{(y + 1)^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0, y \ge 0 \\ \ln(y + 1) & \text{if } \lambda = 0, y \ge 0 \\ -\frac{(-y + 1)^{2 - \lambda} - 1}{2 - \lambda} & \text{if } \lambda \neq 2, y < 0 \\ -\ln(-y + 1) & \text{if } \lambda = 2, y < 0 \end{cases}$$

*   **Constraint:** None. Ideal for features that contain zeros (e.g., daily alcohol intake, step counts).
*   **Optimization:** The parameter $\lambda$ is estimated using maximum likelihood estimation to minimize skewness.

---

## 2. Scaling Methodologies

Numerical scaling maps feature values to a standardized range, preventing features with large magnitudes (e.g., income) from dominating features with small magnitudes (e.g., age).

### StandardScaler (Z-Score Normalization)
$$x' = \frac{x - \mu}{\sigma}$$
*   **Result:** Mean $= 0$, Standard Deviation $= 1$.
*   *Vulnerability:* Highly sensitive to outliers. If outliers exist, $\sigma$ is artificially inflated, compressing the standard variance of the normal data points.

### MinMaxScaler
$$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
*   **Result:** Maps data strictly to the interval $[0, 1]$.
*   *Vulnerability:* If an extreme outlier exists, $x_{\max}$ will be massive, compressing all non-outlier data points into a narrow range (e.g., $[0, 0.05]$).

### RobustScaler
$$x' = \frac{x - \operatorname{median}(x)}{\operatorname{IQR}}$$
*   **Result:** Scales data using statistics that are immune to outliers.
*   *Benefit:* Median and IQR are robust to extreme values. The outliers are scaled but they do not compress or distort the scaling of the rest of the dataset. **This is the standard choice when box plots reveal substantial outlier counts.**

---

## 3. Semantic Categorical Encoding

Traditional categorical encoding (e.g., One-Hot Encoding) is problematic when dealing with high-cardinality features or unstructured text columns.

### Limitations of One-Hot Encoding
1.  **Dimensionality Curse:** A categorical column with $K$ unique values adds $K-1$ columns to the dataset, leading to sparse matrices and memory bloat.
2.  **Loss of Semantic Meaning:** Every one-hot vector is orthogonal to every other one-hot vector. Geometrically, the distance between any two categories is identical:
    $$d(\mathbf{e}_a, \mathbf{e}_b) = \sqrt{2} \quad \forall a \neq b$$
    *Example:* The terms `"Active Gym Member"` and `"Casual Jogger"` are treated as being just as different from each other as `"Active Gym Member"` and `"Sedentary Office Worker"`.

### Sentence Transformer Encoding (Dense Vectors)
Convert categorical text into dense semantic vector embeddings (e.g., 384-dimensional space) using a pre-trained transformer model (like MiniLM).

$$\mathbf{v}_i = \operatorname{Transformer}(s_i) \in \mathbb{R}^{d}$$

*   **Benefit:** Captures semantic meaning and proximity. In the embedding space, the cosine similarity between related categories will be high:
    $$\cos(\theta) = \frac{\mathbf{v}_{\text{Active}} \cdot \mathbf{v}_{\text{Jogger}}}{\|\mathbf{v}_{\text{Active}}\| \|\mathbf{v}_{\text{Jogger}}\|} \approx 0.85$$
    Whereas:
    $$\cos(\theta) = \frac{\mathbf{v}_{\text{Active}} \cdot \mathbf{v}_{\text{Sedentary}}}{\|\mathbf{v}_{\text{Active}}\| \|\mathbf{v}_{\text{Sedentary}}\|} \approx 0.15$$
*   **Use Case:** Highly recommended for text-based categories or description fields in tabular datasets to preserve structural semantic relationships.
