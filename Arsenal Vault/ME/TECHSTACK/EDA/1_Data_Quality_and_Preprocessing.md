# Data Quality & Initial Preprocessing

Data quality assessment is the foundation of any robust machine learning pipeline. Downstream statistical tests, feature engineering, and neural network training assume the integrity of the input features.

---

## 1. Duplicate Analysis & Data Leakage

Duplicates are not just redundant rows; they represent a fundamental threat to model validation.

### The Threat of Data Leakage
If duplicate rows are present in the dataset before performing a train-test split:
1. The same data point can appear in both the training set and the validation/test set.
2. The model can "memorize" these samples, leading to artificially inflated performance metrics (optimism bias).
3. The validation set ceases to be an independent measure of generalization.

### Action Plan
*   **Detection:** Query duplicate rows using hashing or row-wise comparison:
    $$\text{Duplicates} = \{x_i \mid \exists x_j \text{ such that } x_i = x_j, i \neq j\}$$
*   **Mitigation:** Remove duplicate rows immediately after data loading, prior to split generation.

---

## 2. Missing Value Diagnostics

Missing data is not merely "empty space"—the *pattern of missingness* carries structural information about the data collection process.

### Classification of Missingness
1.  **Missing Completely at Random (MCAR):**
    The probability of missingness is completely independent of both observed and unobserved data:
    $$P(M \mid Y_{\text{obs}}, Y_{\text{mis}}) = P(M)$$
    *Implication:* Safe to drop or use simple imputation.
2.  **Missing at Random (MAR):**
    The missingness depends systematically on observed covariates, but not on the missing values themselves:
    $$P(M \mid Y_{\text{obs}}, Y_{\text{mis}}) = P(M \mid Y_{\text{obs}})$$
    *Implication:* Dropping leads to bias. Multiple Imputation or predictive imputation (MICE) is required.
3.  **Missing Not at Random (MNAR):**
    The probability of missingness depends directly on the value of the missing variable itself:
    $$P(M \mid Y_{\text{obs}}, Y_{\text{mis}}) \neq P(M \mid Y_{\text{obs}})$$
    *Implication:* Highly problematic. Requires modeling the missingness mechanism or adding indicator variables ($M_i \in \{0, 1\}$) to capture the semantic meaning of the absence.

---

## 3. Memory Optimization & Datatypes

For large datasets, memory layout directly impacts computation time (CPU cache misses, GPU memory boundaries).

### String vs. Categorical Representation
*   **Object Dtype:** Standard Python strings are stored as individual objects in memory, leading to high overhead due to pointer dereferencing.
*   **Category Dtype:** Maps unique string values to compact integer codes under the hood:
    $$\mathcal{C}: S \to \mathbb{N}$$
    *Benefit:* Reduces memory consumption by $\approx 70\%$, speeds up groupings, and signals downstream libraries to treat the column as a factor.

---

## 4. Temporal Feature Representation

Raw time representations (e.g., `"06:30"`) are categorical strings. They cannot be fed directly to numerical models, and treating them as simple ordinal values loses crucial cyclical structures.

### Continuous Minutes Conversion
Convert time strings into continuous scalar values representing the minutes elapsed since midnight:
$$t_{\text{minutes}} = H \times 60 + M$$
*   **Wake-up habit range:** $[0, 1440)$ minutes.
*   **Limitation:** It introduces a artificial boundary discontinuity at midnight (e.g., $1439$ min is geometrically close to $0$ min, but algebraically far).

### Cyclical Encoding (For Neural Networks)
To resolve midnight boundaries, map the continuous minutes to 2D unit circle coordinates:
$$x_{\text{sin}} = \sin\left(\frac{2\pi \cdot t_{\text{minutes}}}{1440}\right)$$
$$y_{\text{cos}} = \cos\left(\frac{2\pi \cdot t_{\text{minutes}}}{1440}\right)$$
This maps time to a continuous, closed topological loop preserving proximity.
