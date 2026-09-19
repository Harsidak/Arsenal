# Statistical Testing & Effect Sizes

Statistical significance ($p$-values) is insufficient for making data-driven decisions in production pipelines. We must couple significance testing with effect size estimation and select tests based on the structural properties of our data.

---

## 1. The Limitation of $p$-values (The Sample Size Paradox)

A $p$-value measures the probability of observing a test statistic as extreme as, or more extreme than, the one calculated, assuming the null hypothesis ($H_0$) is true.

### The Sample Size Dependency
As the sample size ($N$) approaches infinity, the standard error of our estimator approaches zero:
$$\operatorname{SE} = \frac{\sigma}{\sqrt{N}} \to 0$$
Consequently, even a microscopic, practically meaningless difference between two groups will yield a statistically significant $p$-value ($p < 0.05$).

*   *Example:* If comparing sleep hours between two groups with $N = 100,000$, a difference of $1.2$ minutes ($0.02$ hours) will be highly statistically significant ($p < 0.001$), but holds zero practical or clinical relevance.
*   **Core Rule:** Never report $p$-values without reporting **Effect Sizes**, which measure the magnitude of the difference independent of sample size.

---

## 2. Standardized Effect Sizes

### Cohen's $d$ (Continuous Variables, Two Groups)
Quantifies the standardized difference between the means of two groups.

$$d = \frac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}}$$

Where the pooled standard deviation is:
$$s_{\text{pooled}} = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$$

| Cohen's $d$ Value | Effect Size | Practical Meaning |
| :--- | :--- | :--- |
| **$< 0.2$** | Negligible | The difference is practically unobservable. |
| **$0.2 - 0.5$** | Small | Subtle but statistically observable difference. |
| **$0.5 - 0.8$** | Medium | Clear difference, visible to a casual observer. |
| **$> 0.8$** | Large | Substantial difference; highly significant in practice. |

### Cramér's $V$ (Categorical Variables, Association Strength)
Quantifies the association strength between two nominal categorical variables, outputting a value in $[0, 1]$.

$$V = \sqrt{\frac{\chi^2}{N \times \min(k-1, r-1)}}$$

Where $\chi^2$ is the Pearson chi-square statistic, $k$ is the number of columns, and $r$ is the number of rows.

| Cramér's $V$ Value | Association Strength |
| :--- | :--- |
| **$< 0.1$** | Negligible association |
| **$0.1 - 0.3$** | Small association |
| **$0.3 - 0.5$** | Medium association |
| **$> 0.5$** | Large association |

---

## 3. Parametric vs. Non-Parametric Testing

Parametric tests assume specific underlying probability distributions (usually normal) and homogeneity of variance. Violating these assumptions invalidates the test's mathematical foundations.

### Mann-Whitney U Test (Non-Parametric Two-Group Comparison)
An alternative to the independent samples $T$-test.
*   **How it works:** Replaces raw values with their ranks across the combined dataset.
*   **Assumption Freedoms:** No assumption of normality; highly robust to extreme outliers (an outlier simply receives the highest rank).

### Kruskal-Wallis H Test (Non-Parametric Multi-Group Comparison)
An alternative to one-way ANOVA.
*   **How it works:** Extends the rank-based approach of the Mann-Whitney test to $3+$ groups.
*   **Hypothesis tested:** Evaluates whether the medians of the groups differ significantly.

### Decision matrix for statistical test selection:

| Data Type | Group Count | Normality / Outlier Condition | Parametric Test | Non-Parametric Test |
| :--- | :--- | :--- | :--- | :--- |
| **Continuous** | 2 Groups | Normal, no outliers | Independent $T$-Test | Mann-Whitney U Test |
| **Continuous** | 2 Groups | Skewed or has outliers | *Do not use* | **Mann-Whitney U Test** |
| **Continuous** | $3+$ Groups | Normal, no outliers | One-Way ANOVA | Kruskal-Wallis Test |
| **Continuous** | $3+$ Groups | Skewed or has outliers | *Do not use* | **Kruskal-Wallis Test** |
| **Categorical** | $2+$ Groups | All expected cell counts $\ge 5$ | Chi-Square Test ($\chi^2$) | Fisher's Exact Test |
