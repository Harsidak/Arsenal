# Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) is a rigorous diagnostic process designed to understand the underlying structure, quality, and relationships within a dataset. Rather than simply plotting charts, an elite EDA pipeline establishes statistical validation and profiles the data to make mathematically sound decisions for preprocessing, feature engineering, and modeling.

---

## The Core EDA Pipeline

This vault contains detailed notes on each phase of a production-grade EDA pipeline:

1. **[[EDA/1_Data_Quality_and_Preprocessing|Data Quality & Preprocessing]]**
   * Detecting data leakage from duplicates.
   * Diagnosing patterns of missingness (MCAR, MAR, MNAR).
   * Memory optimization (Category type mapping).
   * Cyclical time encoding ($sin$/$cos$ transforms).

2. **[[EDA/2_Univariate_Statistical_Profiling|Univariate Statistical Profiling]]**
   * Central tendency (Mean, Median, Mode, and robust Trimmed Mean).
   * Measures of dispersion (Variance, Bessel's correction, IQR, MAD, and CV).
   * Tukey's IQR outlier fences.
   * Distribution shape analysis (Skewness & Kurtosis).

3. **[[EDA/3_Univariate_Visual_Diagnostics|Univariate Visual Diagnostics]]**
   * Diagnostic value of Density (KDE) and Box plots.
   * Quantile-Quantile (Q-Q) plots for normality check.
   * Hexbin plots to resolve overplotting in large datasets ($N > 10,000$).
   * Architectural implications on Neural Networks (activation saturation and gradient explosion).

4. **[[EDA/4_Bivariate_and_Multivariate_Analysis|Bivariate & Multivariate Analysis]]**
   * Linear (Pearson) vs. Monotonic (Spearman Rank) correlation.
   * Multicollinearity issues and Variance Inflation Factor (VIF).
   * Regularization and PCA compression.

5. **[[EDA/5_Statistical_Testing_and_Effect_Sizes|Statistical Testing & Effect Sizes]]**
   * The Sample Size Paradox of $p$-values.
   * Standardized effect sizes (Cohen's $d$, Cramér's $V$).
   * Non-parametric alternatives (Mann-Whitney U, Kruskal-Wallis) for skewed distributions.

6. **[[EDA/6_Feature_Transformation_and_Scaling|Feature Transformation & Scaling]]**
   * Box-Cox and Yeo-Johnson power transformations.
   * Scaling methods (Standard, MinMax, Robust).
   * Dense semantic embeddings vs. One-Hot encoding for categorical data.
