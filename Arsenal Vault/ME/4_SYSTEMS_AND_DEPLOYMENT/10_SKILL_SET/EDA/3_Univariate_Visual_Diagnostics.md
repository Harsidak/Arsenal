# Univariate Visual Diagnostics

Visual analysis serves to detect patterns, outliers, and boundary anomalies that summary statistics alone cannot capture. This document details the diagnostic value of the standard EDA visualization toolkit and explains its implications for neural network training.

---

## 1. Density Plot (KDE - Kernel Density Estimate)

A KDE plot is a smooth, continuous estimate of the probability density function of a random variable. It is constructed by placing a kernel (typically a Gaussian) over each data point and summing them:

$$\hat{f}_h(x) = \frac{1}{N h} \sum_{i=1}^N K\left(\frac{x - x_i}{h}\right)$$

Where $K(\cdot)$ is the kernel function and $h$ is the bandwidth (the smoothing parameter).

### Diagnostic Value
*   **Modality:** Identifies if a distribution is unimodal (one peak) or multimodal (multiple peaks). Multimodality indicates distinct subpopulations in the data that may require segmentation or clustering.
*   **Skewness and Tail Behavior:** Displays the rate at which the distribution's tail decays.

### Implication for Neural Networks
*   **Activation Saturation:** Severely skewed input distributions force linear units or activation functions like ReLU ($\max(0, x)$) into saturation. If a feature's values are concentrated far in the positive or negative range, the neuron outputs either a constant linear scale or zero. This slows learning due to unbalanced gradient updates.
*   **Solution:** Transform skewed inputs to make them approximately symmetric before feeding them into neural architectures.

---

## 2. Box Plot (Tukey Boxplot)

A box plot summarizes the distribution using a five-number summary: Minimum, Q1 ($P_{25}$), Median ($P_{50}$), Q3 ($P_{75}$), and Maximum, along with flagged outliers.

```
       Outlier          Lower Whisker      Q1    Median   Q3      Upper Whisker      Outliers
          o ───────────────[    |    ]─────────────── o o o
                            ^   ^    ^
                            |   |    |
                           Q1  Med   Q3
```

### Diagnostic Value
*   **Symmetry:** If the median line is not centered inside the box, the data is skewed.
*   **Outlier Density:** Focuses directly on values exceeding $1.5 \times \text{IQR}$ fences.

### Implication for Neural Networks
*   **Exploding Gradients:** Neural network loss functions like Mean Squared Error (MSE) penalize errors quadratically:
    $$\mathcal{L} = \frac{1}{2} (y - \hat{y})^2 \implies \frac{\partial \mathcal{L}}{\partial w} = -(y - \hat{y}) \cdot x$$
    Extreme outlier values of $x$ propagate massive gradients back through the network, destabilizing weight matrices and causing numerical overflow.
*   **Solution:** Identify outliers in boxplots to apply robust scaling, clipping, or winsorization.

---

## 3. Q-Q Plot (Quantile-Quantile)

A Q-Q plot compares the empirical quantiles of your sample against the theoretical quantiles of a standard normal distribution $\mathcal{N}(0, 1)$.

$$\{ (F^{-1}_{\text{theoretical}}(p), F^{-1}_{\text{empirical}}(p)) \mid p \in (0, 1) \}$$

### Diagnostic Value
*   **Normality Check:** Points falling exactly along the $45^\circ$ reference line represent a perfectly normal distribution.
*   **S-Shape:** Deviations at the tails in an S-shape indicate heavy tails (kurtosis issue) or light tails.
*   **Curve:** A constant curve away from the reference line indicates skewness.

### Implication for Neural Networks
*   **Optimization Convergence:** Optimization algorithms (e.g., Adam, RMSprop, SGD with momentum) perform best when inputs are approximately normally distributed. Normalization ensures the loss landscape is spherical rather than elongated, allowing gradient descent to take a direct path to the minimum. Q-Q plots tell you if a simple Z-score standardizer is sufficient or if non-linear power transforms are required.

---

## 4. Hexbin Plot (2D Density)

Hexbin plots are a 2D extension of histograms. The plotting space is partitioned into a grid of regular hexagons, and the color of each hexagon represents the frequency of data points falling within that boundary.

### Diagnostic Value
*   **Overplotting Resolution:** Standard scatter plots suffer from overplotting when $N > 10,000$, collapsing into solid blocks of color. Hexbins preserve density variations in massive datasets.
*   **Non-linear Boundary Identification:** Highlights clustering, non-linear relationships (e.g., U-shape, sinusoidal patterns), and boundary limits.

### Feature Engineering Direction
*   If a hexbin plot reveals a curved relationship between two features, it indicates that a simple linear model will fail. This guides you to create polynomial features ($x^2, x^3$) or use non-linear kernels to capture the interaction.
