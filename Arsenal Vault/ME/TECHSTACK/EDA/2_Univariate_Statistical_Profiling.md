# Univariate Statistical Profiling

Univariate analysis is the study of a single variable's distribution. Before looking at interactions between features, we must establish a complete mathematical profile of each individual feature.

---

## 1. Central Tendency

Measures of central tendency locate the "center" of a distribution.

| Measure | Mathematical Definition | Robustness to Outliers | Notes |
| :--- | :--- | :--- | :--- |
| **Mean** ($\bar{x}$) | $$\bar{x} = \frac{1}{N} \sum_{i=1}^N x_i$$ | **Low** | Great for symmetric, normal-like distributions. |
| **Median** ($\tilde{x}$) | $$P_{50} = \text{Value at the 50th percentile}$$ | **High** | Ideal for skewed distributions (e.g., income, calorie intake). |
| **Mode** | $$\operatorname{argmax}_x \operatorname{count}(x)$$ | **High** | Primary measure for categorical features. |
| **Trimmed Mean** ($\bar{x}_{\alpha}$) | $$\bar{x}_{\alpha} = \frac{1}{N - 2k} \sum_{i=k+1}^{N-k} x_{(i)}$$ | **Medium-High** | Removes the top and bottom $\alpha\%$ (where $k = \alpha N$) to prevent outlier bias. |

### Decision Rule
*   If $\bar{x} \approx \tilde{x}$, the distribution is symmetric. Use the **Mean**.
*   If $\bar{x} \gg \tilde{x}$, the distribution is right-skewed. Use the **Median** as the typical value representation.

---

## 2. Dispersion & Spread

Measures of dispersion quantify the variability or "spread" of data points.

### Range
$$\text{Range} = X_{\max} - X_{\min}$$
*   *Vulnerability:* Highly unstable; a single outlier can double the range.

### Variance ($\sigma^2$) & Standard Deviation ($\sigma$)
$$\sigma^2 = \frac{1}{N - 1} \sum_{i=1}^N (x_i - \bar{x})^2$$
*   **Bessel's Correction ($N-1$):** We divide by $N-1$ rather than $N$ when calculating sample variance. Because the sample mean $\bar{x}$ is calculated from the same data, we lose one degree of freedom. Dividing by $N-1$ provides an *unbiased estimator* of the population variance.
*   *Limitation:* Since deviations are squared, standard deviation is highly sensitive to outliers.

### Interquartile Range (IQR)
$$\text{IQR} = Q_3 - Q_1 = P_{75} - P_{25}$$
*   *Benefit:* Captures the range of the middle $50\%$ of the data. Completely unaffected by outliers in the outer $50\%$.

### Median Absolute Deviation (MAD)
$$\text{MAD} = \operatorname{median}(|x_i - \operatorname{median}(X)|)$$
*   *Benefit:* The most robust measure of dispersion. More stable than standard deviation when outliers are present.

### Coefficient of Variation (CV)
$$\text{CV} = \frac{\sigma}{\bar{x}}$$
*   *Benefit:* Standardizes the variance relative to the mean. Allows you to compare the variability of features on completely different scales (e.g., age vs. income).

---

## 3. Percentiles & Outlier Detection

Percentiles ($P_k$) partition a sorted distribution into $100$ equal parts.

### Tukey's IQR Outlier Rule
Using the Interquartile Range, we construct statistical fences:
$$\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}$$
$$\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}$$
*   **The 1.5 multiplier:** For a standard normal distribution $\mathcal{N}(\mu, \sigma^2)$, Tukey's fences capture $\approx 99.3\%$ of the data. Values outside are considered outliers.
*   **Extreme Outliers:** Defined by a $3.0 \times \text{IQR}$ multiplier. These represent critical data anomalies.

---

## 4. Distribution Shape Metrics

We measure how much a distribution deviates from normality using Skewness and Kurtosis.

### Skewness
Measures the asymmetry of the distribution about its mean.
$$\text{Skewness} = \frac{\frac{1}{N} \sum (x_i - \bar{x})^3}{\left(\frac{1}{N} \sum (x_i - \bar{x})^2\right)^{3/2}}$$
*   **Symmetric:** $|Skew| < 0.5$ (No transformation needed).
*   **Moderate Skew:** $0.5 \le |Skew| < 1.0$ (Consider square root or mild log transformation).
*   **High Skew:** $|Skew| \ge 1.0$ (Requires strong transformation like Box-Cox or Yeo-Johnson to ensure model convergence).

### Kurtosis (Excess)
Measures the "tailedness" of the distribution relative to a normal distribution (excess kurtosis = Kurtosis - 3).
$$\text{Kurtosis}_{\text{excess}} = \frac{\frac{1}{N} \sum (x_i - \bar{x})^4}{\left(\frac{1}{N} \sum (x_i - \bar{x})^2\right)^2} - 3$$
*   **Leptokurtic ($> 0$):** Heavy tails, high peak. Indicates frequent extreme outliers.
*   **Platykurtic ($< 0$):** Thin tails, flat peak. Indicates outliers are rare.
