# Bivariate & Multivariate Analysis

While univariate analysis profiles variables in isolation, bivariate and multivariate analysis investigate relationships, dependencies, and redundancies between features.

---

## 1. Linear vs. Monotonic Correlation

Correlation measures the strength and direction of association between two variables. Choosing the correct correlation metric is critical to avoid drawing false conclusions.

### Pearson Product-Moment Correlation ($r$)
Measures the strength of a **linear** relationship between two continuous variables.

$$r = \frac{\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^N (x_i - \bar{x})^2 \sum_{i=1}^N (y_i - \bar{y})^2}}$$

*   **Assumptions:** Linearity, homoscedasticity, continuous scale, normal distribution, and no outliers.
*   **Pitfalls:**
    1.  **Outlier Sensitivity:** A single extreme outlier can inflate a weak correlation ($r \approx 0 \to 0.9$) or destroy a strong one.
    2.  **Linear Limitation:** A perfect quadratic relationship ($y = x^2$) centered at $x=0$ yields $r \approx 0$, failing to detect the relationship.

### Spearman's Rank Correlation ($\rho$)
Measures the strength of a **monotonic** relationship (consistently increasing or decreasing, not necessarily linear).

$$\rho = 1 - \frac{6 \sum d_i^2}{N(N^2 - 1)}$$

Where $d_i = \operatorname{rank}(x_i) - \operatorname{rank}(y_i)$.

*   **Process:** Converts raw numerical values to ordinal ranks, then computes Pearson's correlation on those ranks.
*   **When to Use:**
    1.  Skewed distributions or non-normal features (e.g., calorie intake, alcohol consumption).
    2.  Presence of outliers (ranks bound the influence of extreme values; a massive outlier simply becomes rank $N$).
    3.  Ordinal categorical data.

### Comparison Summary
*   **Pearson:** Checks for straight-line relationships. Use only when data is normally distributed and clean.
*   **Spearman:** Checks if $Y$ increases when $X$ increases, regardless of the rate. Use as the default robust metric for skewed data.

---

## 2. Multicollinearity & Variance Inflation Factor (VIF)

Multicollinearity occurs when two or more independent features are highly correlated with each other, meaning they carry redundant information.

### The Threat of Multicollinearity
In linear models:
$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \epsilon$$
If $x_1$ and $x_2$ are highly collinear, the model's estimate of their individual coefficients ($\beta_1, \beta_2$) becomes highly unstable. Small perturbations in the training data cause massive shifts in coefficient values, destroying model interpretability and inflating standard errors.

### Variance Inflation Factor (VIF)
VIF measures how much the variance of an estimated regression coefficient is increased due to collinearity. For feature $j$, we run an ordinary least squares regression predicting $x_j$ using all other independent features.

$$\operatorname{VIF}_j = \frac{1}{1 - R_j^2}$$

Where $R_j^2$ is the coefficient of determination of that auxiliary regression.

### VIF Interpretation Scale
*   **$\operatorname{VIF} = 1$:** No collinearity.
*   **$1 < \operatorname{VIF} < 5$:** Moderate collinearity (Acceptable range).
*   **$5 \le \operatorname{VIF} < 10$:** High collinearity (Warning zone; consider dropping or combining).
*   **$\operatorname{VIF} \ge 10$:** Severe collinearity (Action required; coefficients are highly unstable).

### Mitigation Strategies
1.  **Drop Feature:** Remove the feature with the highest VIF (e.g., if you have `Weight_kg`, `Height_cm`, and `BMI`, drop weight and height since BMI captures their relationship).
2.  **Feature Interaction / Compression:** Use Principal Component Analysis (PCA) to project collinear features onto orthogonal axes.
3.  **L2 Regularization (Ridge Regression):** Adds a penalty to the loss function ($\lambda \sum \beta^2$) to force coefficients to remain stable despite collinearity.
