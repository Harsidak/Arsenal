"""
GLM - Generalized Linear Model Implementation
A robust Linear Regression model built from scratch without ML libraries.

Features:
- Ordinary Least Squares (OLS) regression
- Gradient Descent optimization (Batch, Stochastic, Mini-batch)
- Regularization (L1/Lasso, L2/Ridge, Elastic Net)
- Feature scaling (Standardization, Normalization)
- Polynomial regression
- Statistical diagnostics (R-squared, Adjusted R-squared, MSE, MAE, RMSE)
- Hypothesis testing (t-tests, F-tests)
- Confidence and prediction intervals
- Cross-validation
- Residual analysis
- Multi-collinearity detection (VIF)
"""

import math
from typing import List, Tuple, Optional, Dict, Union
from dataclasses import dataclass
from enum import Enum


class OptimizationMethod(Enum):
    OLS = "ols"  # Closed-form solution
    BATCH_GD = "batch_gd"  # Batch Gradient Descent
    SGD = "sgd"  # Stochastic Gradient Descent
    MINI_BATCH_GD = "mini_batch_gd"  # Mini-batch Gradient Descent


class RegularizationType(Enum):
    NONE = "none"
    L1 = "l1"  # Lasso
    L2 = "l2"  # Ridge
    ELASTIC_NET = "elastic_net"


class ScalingType(Enum):
    NONE = "none"
    STANDARDIZATION = "standardization"  # z-score
    MIN_MAX = "min_max"  # 0-1 normalization


@dataclass
class ModelConfig:
    """Configuration for Linear Regression model."""
    optimization: OptimizationMethod = OptimizationMethod.OLS
    regularization: RegularizationType = RegularizationType.NONE
    alpha: float = 0.01  # Regularization strength
    l1_ratio: float = 0.5  # For Elastic Net
    learning_rate: float = 0.01
    max_iterations: int = 1000
    tolerance: float = 1e-6
    scaling: ScalingType = ScalingType.STANDARDIZATION
    polynomial_degree: int = 1
    fit_intercept: bool = True
    batch_size: int = 32  # For mini-batch GD


@dataclass
class ModelStatistics:
    """Statistical summary of the fitted model."""
    r_squared: float = 0.0
    adjusted_r_squared: float = 0.0
    mse: float = 0.0
    rmse: float = 0.0
    mae: float = 0.0
    f_statistic: float = 0.0
    f_p_value: float = 0.0
    residuals: List[float] = None
    standard_errors: List[float] = None
    t_statistics: List[float] = None
    p_values: List[float] = None
    confidence_intervals: List[Tuple[float, float]] = None
    vif: List[float] = None  # Variance Inflation Factor


class LinearRegression:
    """
    A robust Linear Regression implementation from scratch.

    Supports multiple optimization methods, regularization, and comprehensive
    statistical diagnostics.
    """

    def __init__(self, config: Optional[ModelConfig] = None):
        """Initialize the model with optional configuration."""
        self.config = config or ModelConfig()
        self.coefficients: List[float] = []
        self.intercept: float = 0.0
        self.n_features: int = 0
        self.n_samples: int = 0
        self._is_fitted: bool = False
        self._scaling_params: Dict = {}
        self.statistics: ModelStatistics = ModelStatistics()
        self._loss_history: List[float] = []

    def _validate_inputs(self, X: List[List[float]], y: List[float]) -> None:
        """Validate input data dimensions and types."""
        if not X or not y:
            raise ValueError("Input data cannot be empty")
        if len(X) != len(y):
            raise ValueError(f"X and y must have same number of samples. Got X: {len(X)}, y: {len(y)}")
        if any(len(row) == 0 for row in X):
            raise ValueError("Feature vectors cannot be empty")

        # Check all features have same dimension
        n_features = len(X[0])
        if not all(len(row) == n_features for row in X):
            raise ValueError("All feature vectors must have the same dimension")

    def _transpose(self, matrix: List[List[float]]) -> List[List[float]]:
        """Transpose a matrix."""
        if not matrix:
            return []
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

    def _matmul(self, A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
        """Matrix multiplication."""
        if not A or not B or len(A[0]) != len(B):
            raise ValueError("Invalid matrix dimensions for multiplication")

        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])

        result = [[0.0] * cols_B for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def _inverse(self, matrix: List[List[float]]) -> List[List[float]]:
        """
        Compute matrix inverse using Gauss-Jordan elimination.
        More numerically stable than naive approach.
        """
        n = len(matrix)
        if n == 0 or any(len(row) != n for row in matrix):
            raise ValueError("Matrix must be square")

        # Augment matrix with identity
        augmented = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]

        # Forward elimination with partial pivoting
        for col in range(n):
            # Find pivot
            max_row = max(range(col, n), key=lambda r: abs(augmented[r][col]))
            if abs(augmented[max_row][col]) < 1e-12:
                raise ValueError("Matrix is singular and cannot be inverted")

            # Swap rows
            augmented[col], augmented[max_row] = augmented[max_row], augmented[col]

            # Scale pivot row
            pivot = augmented[col][col]
            for j in range(2 * n):
                augmented[col][j] /= pivot

            # Eliminate column
            for i in range(n):
                if i != col:
                    factor = augmented[i][col]
                    for j in range(2 * n):
                        augmented[i][j] -= factor * augmented[col][j]

        # Extract inverse
        return [[augmented[i][j] for j in range(n, 2 * n)] for i in range(n)]

    def _scale_features(self, X: List[List[float]], fit: bool = True) -> List[List[float]]:
        """Scale features based on configuration."""
        if self.config.scaling == ScalingType.NONE:
            return X

        if fit:
            self._scaling_params = {'means': [], 'stds': [], 'mins': [], 'maxs': []}

        n_features = len(X[0])
        scaled = [[0.0] * n_features for _ in range(len(X))]

        for j in range(n_features):
            column = [X[i][j] for i in range(len(X))]

            if fit:
                mean = sum(column) / len(column)
                std = math.sqrt(sum((x - mean) ** 2 for x in column) / len(column))
                std = std if std > 1e-10 else 1.0
                min_val, max_val = min(column), max(column)
                range_val = max_val - min_val if max_val != min_val else 1.0

                self._scaling_params['means'].append(mean)
                self._scaling_params['stds'].append(std)
                self._scaling_params['mins'].append(min_val)
                self._scaling_params['maxs'].append(max_val)

            mean = self._scaling_params['means'][j]
            std = self._scaling_params['stds'][j]
            min_val = self._scaling_params['mins'][j]
            max_val = self._scaling_params['maxs'][j]
            range_val = max_val - min_val if max_val != min_val else 1.0

            for i in range(len(X)):
                if self.config.scaling == ScalingType.STANDARDIZATION:
                    scaled[i][j] = (X[i][j] - mean) / std
                else:  # MIN_MAX
                    scaled[i][j] = (X[i][j] - min_val) / range_val

        return scaled

    def _generate_polynomial_features(self, X: List[List[float]]) -> List[List[float]]:
        """Generate polynomial features up to specified degree."""
        if self.config.polynomial_degree <= 1:
            return X

        result = []
        for sample in X:
            new_features = list(sample)

            # Add polynomial terms (including interactions)
            for degree in range(2, self.config.polynomial_degree + 1):
                # Pure polynomial terms
                for j in range(len(sample)):
                    new_features.append(sample[j] ** degree)

                # Interaction terms for degree 2
                if degree == 2 and len(sample) > 1:
                    for i in range(len(sample)):
                        for j in range(i + 1, len(sample)):
                            new_features.append(sample[i] * sample[j])

            result.append(new_features)

        return result

    def _add_intercept(self, X: List[List[float]]) -> List[List[float]]:
        """Add intercept column (ones) to feature matrix."""
        return [[1.0] + row for row in X]

    def _compute_predictions(self, X: List[List[float]], coefficients: List[float]) -> List[float]:
        """Compute predictions for given features and coefficients."""
        return [sum(x[i] * coefficients[i] for i in range(len(coefficients))) for x in X]

    def _compute_loss(self, y_true: List[float], y_pred: List[float]) -> float:
        """Compute mean squared error loss."""
        mse = sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true))) / len(y_true)

        # Add regularization term
        if self.config.regularization != RegularizationType.NONE:
            reg_term = 0.0
            if self.config.regularization in [RegularizationType.L1, RegularizationType.ELASTIC_NET]:
                l1_term = sum(abs(c) for c in self.coefficients)
                reg_term += self.config.l1_ratio * self.config.alpha * l1_term
            if self.config.regularization in [RegularizationType.L2, RegularizationType.ELASTIC_NET]:
                l2_term = sum(c ** 2 for c in self.coefficients)
                reg_term += (1 - self.config.l1_ratio) * self.config.alpha * l2_term
            mse += reg_term

        return mse

    def _ols_fit(self, X: List[List[float]], y: List[float]) -> List[float]:
        """Fit using Ordinary Least Squares (closed-form solution)."""
        # Add intercept if needed
        if self.config.fit_intercept:
            X_design = self._add_intercept(X)
        else:
            X_design = X

        X_T = self._transpose(X_design)
        X_TX = self._matmul(X_T, X_design)

        # Add regularization to diagonal if specified
        if self.config.regularization == RegularizationType.L2:
            for i in range(len(X_TX)):
                X_TX[i][i] += self.config.alpha

        X_TX_inv = self._inverse(X_TX)

        y_col = [[yi] for yi in y]
        X_Ty = self._matmul(X_T, y_col)
        coefficients_col = self._matmul(X_TX_inv, X_Ty)

        return [row[0] for row in coefficients_col]

    def _gradient_descent(self, X: List[List[float]], y: List[float],
                          method: OptimizationMethod) -> List[float]:
        """Fit using gradient descent variants."""
        if self.config.fit_intercept:
            X_design = self._add_intercept(X)
        else:
            X_design = X

        n_features = len(X_design[0])
        n_samples = len(X_design)

        # Initialize coefficients
        coefficients = [0.0] * n_features
        self._loss_history = []

        for iteration in range(self.config.max_iterations):
            # Select samples based on method
            if method == OptimizationMethod.SGD:
                indices = [math.floor(math.random() * n_samples)]
            elif method == OptimizationMethod.MINI_BATCH_GD:
                batch_size = min(self.config.batch_size, n_samples)
                indices = [math.floor(math.random() * n_samples) for _ in range(batch_size)]
            else:  # BATCH_GD
                indices = list(range(n_samples))

            X_batch = [X_design[i] for i in indices]
            y_batch = [y[i] for i in indices]

            # Compute predictions and gradient
            predictions = self._compute_predictions(X_batch, coefficients)
            errors = [predictions[i] - y_batch[i] for i in range(len(y_batch))]

            # Gradient computation
            gradients = [0.0] * n_features
            for j in range(n_features):
                for i in range(len(X_batch)):
                    gradients[j] += X_batch[i][j] * errors[i]
                gradients[j] /= len(X_batch)

                # Add regularization gradient
                if self.config.regularization == RegularizationType.L1:
                    gradients[j] += self.config.alpha * (1 if coefficients[j] > 0 else -1)
                elif self.config.regularization == RegularizationType.L2:
                    gradients[j] += self.config.alpha * coefficients[j]
                elif self.config.regularization == RegularizationType.ELASTIC_NET:
                    gradients[j] += self.config.alpha * (
                        self.config.l1_ratio * (1 if coefficients[j] > 0 else -1) +
                        (1 - self.config.l1_ratio) * coefficients[j]
                    )

            # Update coefficients
            for j in range(n_features):
                coefficients[j] -= self.config.learning_rate * gradients[j]

            # Track loss
            full_predictions = self._compute_predictions(X_design, coefficients)
            loss = self._compute_loss(y, full_predictions)
            self._loss_history.append(loss)

            # Check convergence
            if len(self._loss_history) > 1 and abs(self._loss_history[-2] - self._loss_history[-1]) < self.config.tolerance:
                break

        return coefficients

    def _compute_statistics(self, X: List[List[float]], y: List[float]) -> None:
        """Compute comprehensive model statistics."""
        if self.config.fit_intercept:
            X_design = self._add_intercept(X)
            coeffs = [self.intercept] + self.coefficients
        else:
            X_design = X
            coeffs = self.coefficients

        n = len(y)
        p = len(coeffs)

        # Predictions and residuals
        predictions = self._compute_predictions(X_design, coeffs)
        residuals = [y[i] - predictions[i] for i in range(n)]
        self.statistics.residuals = residuals

        # MSE, RMSE, MAE
        self.statistics.mse = sum(r ** 2 for r in residuals) / n
        self.statistics.rmse = math.sqrt(self.statistics.mse)
        self.statistics.mae = sum(abs(r) for r in residuals) / n

        # R-squared
        y_mean = sum(y) / n
        ss_tot = sum((yi - y_mean) ** 2 for yi in y)
        ss_res = sum(r ** 2 for r in residuals)
        self.statistics.r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0

        # Adjusted R-squared
        self.statistics.adjusted_r_squared = 1 - (1 - self.statistics.r_squared) * (n - 1) / (n - p) if n > p else 0

        # Standard errors of coefficients
        X_TX = self._matmul(self._transpose(X_design), X_design)
        try:
            X_TX_inv = self._inverse(X_TX)
            mse = self.statistics.mse
            self.statistics.standard_errors = [math.sqrt(mse * X_TX_inv[j][j]) for j in range(p)]
        except:
            self.statistics.standard_errors = [float('inf')] * p

        # T-statistics and p-values
        self.statistics.t_statistics = []
        self.statistics.p_values = []
        self.statistics.confidence_intervals = []

        for j in range(p):
            if self.statistics.standard_errors[j] > 0:
                t_stat = coeffs[j] / self.statistics.standard_errors[j]
                self.statistics.t_statistics.append(t_stat)
                # Approximate p-value using t-distribution (simplified)
                p_val = self._t_distribution_pvalue(t_stat, n - p)
                self.statistics.p_values.append(p_val)
                # 95% confidence interval
                t_critical = 1.96  # Approximate for large samples
                margin = t_critical * self.statistics.standard_errors[j]
                self.statistics.confidence_intervals.append((coeffs[j] - margin, coeffs[j] + margin))
            else:
                self.statistics.t_statistics.append(0)
                self.statistics.p_values.append(1.0)
                self.statistics.confidence_intervals.append((coeffs[j], coeffs[j]))

        # F-statistic
        if self.statistics.mse > 0 and p > 1:
            explained_var = (ss_tot - ss_res) / (p - 1)
            unexplained_var = ss_res / (n - p)
            self.statistics.f_statistic = explained_var / unexplained_var if unexplained_var > 0 else 0
            self.statistics.f_p_value = self._f_distribution_pvalue(self.statistics.f_statistic, p - 1, n - p)

        # Variance Inflation Factor (VIF) for multicollinearity detection
        if p > 1:
            self.statistics.vif = self._compute_vif(X_design)

    def _t_distribution_pvalue(self, t_stat: float, df: int) -> float:
        """Approximate p-value for t-statistic using normal approximation."""
        # Simplified approximation
        z = abs(t_stat)
        # Approximate using standard normal for large df
        if df > 30:
            p = 2 * (1 - self._normal_cdf(z))
        else:
            p = 2 * (1 - self._normal_cdf(z * math.sqrt(df / (df - 2 + z ** 2))))
        return min(1.0, p)

    def _normal_cdf(self, x: float) -> float:
        """Approximate standard normal CDF."""
        # Abramowitz and Stegun approximation
        a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429
        sign = 1 if x >= 0 else -1
        x = abs(x) / math.sqrt(2)
        t = 1 / (1 + 0.2316419 * x)
        y = 1 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-x * x)
        return 0.5 * (1 + sign * y)

    def _f_distribution_pvalue(self, f_stat: float, df1: int, df2: int) -> float:
        """Approximate p-value for F-statistic."""
        # Simplified approximation
        if f_stat <= 0:
            return 1.0
        # Using normal approximation for large df
        if df1 > 4 and df2 > 4:
            z = (math.log(f_stat) - (1 - 2 / (9 * df2))) / math.sqrt(2 / (9 * df1) + 2 / (9 * df2))
            return 1 - self._normal_cdf(z)
        return 0.05  # Conservative default

    def _compute_vif(self, X: List[List[float]]) -> List[float]:
        """Compute Variance Inflation Factor for each feature."""
        vif = []
        n_features = len(X[0])

        for j in range(n_features):
            # Regress feature j on all other features
            X_j = [row[:j] + row[j + 1:] for row in X]
            y_j = [row[j] for row in X]

            try:
                if len(X_j[0]) > 0:
                    coeffs = self._ols_fit(X_j, y_j)
                    X_j_design = self._add_intercept(X_j) if self.config.fit_intercept else X_j
                    predictions = self._compute_predictions(X_j_design, coeffs)
                    y_mean = sum(y_j) / len(y_j)
                    ss_tot = sum((yi - y_mean) ** 2 for yi in y_j)
                    ss_res = sum((y_j[i] - predictions[i]) ** 2 for i in range(len(y_j)))
                    r_squared_j = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
                    vif.append(1 / (1 - r_squared_j) if r_squared_j < 1 else float('inf'))
                else:
                    vif.append(1.0)
            except:
                vif.append(1.0)

        return vif

    def fit(self, X: List[List[float]], y: List[float]) -> 'LinearRegression':
        """
        Fit the linear regression model to the training data.

        Args:
            X: Training features (n_samples x n_features)
            y: Target values (n_samples)

        Returns:
            self: The fitted model instance
        """
        self._validate_inputs(X, y)

        # Store original dimensions
        self.n_samples = len(X)
        self.n_features = len(X[0])

        # Generate polynomial features if needed
        X_processed = self._generate_polynomial_features(X)

        # Scale features
        X_scaled = self._scale_features(X_processed, fit=True)

        # Fit based on optimization method
        if self.config.optimization == OptimizationMethod.OLS:
            coefficients = self._ols_fit(X_scaled, y)
        elif self.config.optimization in [OptimizationMethod.BATCH_GD,
                                           OptimizationMethod.SGD,
                                           OptimizationMethod.MINI_BATCH_GD]:
            coefficients = self._gradient_descent(X_scaled, y, self.config.optimization)
        else:
            raise ValueError(f"Unknown optimization method: {self.config.optimization}")

        # Extract intercept and coefficients
        if self.config.fit_intercept:
            self.intercept = coefficients[0]
            self.coefficients = coefficients[1:]
        else:
            self.intercept = 0.0
            self.coefficients = coefficients

        # Update feature count after polynomial expansion
        self.n_features = len(self.coefficients)

        # Compute statistics
        self._compute_statistics(X_scaled, y)

        self._is_fitted = True
        return self

    def predict(self, X: List[List[float]]) -> List[float]:
        """
        Make predictions using the fitted model.

        Args:
            X: Features to predict (n_samples x n_features)

        Returns:
            Predicted values
        """
        if not self._is_fitted:
            raise ValueError("Model must be fitted before making predictions")

        # Process features
        X_processed = self._generate_polynomial_features(X)
        X_scaled = self._scale_features(X_processed, fit=False)

        # Make predictions
        predictions = []
        for sample in X_scaled:
            pred = self.intercept + sum(sample[j] * self.coefficients[j] for j in range(len(self.coefficients)))
            predictions.append(pred)

        return predictions

    def predict_interval(self, X: List[List[float]], confidence: float = 0.95) -> List[Tuple[float, float, float]]:
        """
        Compute prediction intervals.

        Returns list of (lower, prediction, upper) tuples.
        """
        if not self._is_fitted:
            raise ValueError("Model must be fitted first")

        predictions = self.predict(X)
        X_processed = self._generate_polynomial_features(X)
        X_scaled = self._scale_features(X_processed, fit=False)

        # Compute prediction interval width
        if self.config.fit_intercept:
            X_design = self._add_intercept(X_scaled)
        else:
            X_design = X_scaled

        try:
            X_TX_inv = self._inverse(self._matmul(self._transpose(X_design), X_design))
        except:
            # Fallback if inversion fails
            return [(p - 2 * self.statistics.rmse, p, p + 2 * self.statistics.rmse) for p in predictions]

        t_critical = 1.96  # Approximate 95% CI
        intervals = []

        for i, pred in enumerate(predictions):
            # Compute leverage
            x_row = X_design[i]
            leverage = 0
            for j in range(len(x_row)):
                for k in range(len(x_row)):
                    leverage += x_row[j] * X_TX_inv[j][k] * x_row[k]

            # Prediction interval width
            se_pred = math.sqrt(self.statistics.mse * (1 + leverage))
            margin = t_critical * se_pred
            intervals.append((pred - margin, pred, pred + margin))

        return intervals

    def cross_validate(self, X: List[List[float]], y: List[float],
                       k_folds: int = 5) -> Dict[str, float]:
        """
        Perform k-fold cross-validation.

        Returns dictionary of cross-validation metrics.
        """
        n = len(X)
        fold_size = n // k_folds

        mse_scores = []
        r2_scores = []
        mae_scores = []

        for fold in range(k_folds):
            # Split data
            start_idx = fold * fold_size
            end_idx = start_idx + fold_size if fold < k_folds - 1 else n

            X_test = X[start_idx:end_idx]
            y_test = y[start_idx:end_idx]
            X_train = X[:start_idx] + X[end_idx:]
            y_train = y[:start_idx] + y[end_idx:]

            # Train and evaluate
            model = LinearRegression(self.config)
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)

            # Compute metrics
            mse = sum((y_test[i] - predictions[i]) ** 2 for i in range(len(y_test))) / len(y_test)
            y_mean = sum(y_test) / len(y_test)
            ss_tot = sum((yi - y_mean) ** 2 for yi in y_test)
            r2 = 1 - (mse * len(y_test)) / ss_tot if ss_tot > 0 else 0
            mae = sum(abs(y_test[i] - predictions[i]) for i in range(len(y_test))) / len(y_test)

            mse_scores.append(mse)
            r2_scores.append(r2)
            mae_scores.append(mae)

        return {
            'mean_mse': sum(mse_scores) / k_folds,
            'std_mse': math.sqrt(sum((m - sum(mse_scores) / k_folds) ** 2 for m in mse_scores) / k_folds),
            'mean_r2': sum(r2_scores) / k_folds,
            'std_r2': math.sqrt(sum((r - sum(r2_scores) / k_folds) ** 2 for r in r2_scores) / k_folds),
            'mean_mae': sum(mae_scores) / k_folds,
            'fold_scores': {'mse': mse_scores, 'r2': r2_scores, 'mae': mae_scores}
        }

    def get_coefficients(self) -> Dict[str, float]:
        """Return model coefficients as dictionary."""
        result = {'intercept': self.intercept}
        for i, coef in enumerate(self.coefficients):
            result[f'feature_{i}'] = coef
        return result

    def summary(self) -> str:
        """Generate a comprehensive model summary."""
        if not self._is_fitted:
            return "Model not fitted yet."

        lines = [
            "=" * 70,
            "                    LINEAR REGRESSION MODEL SUMMARY",
            "=" * 70,
            f"\n{'Optimization Method:':<25} {self.config.optimization.value}",
            f"{'Regularization:':<25} {self.config.regularization.value}",
            f"{'Feature Scaling:':<25} {self.config.scaling.value}",
            f"{'Polynomial Degree:':<25} {self.config.polynomial_degree}",
            f"\n{'Number of Samples:':<25} {self.n_samples}",
            f"{'Number of Features:':<25} {self.n_features}",
            "\n" + "-" * 70,
            "                          COEFFICIENTS",
            "-" * 70,
            f"{'Feature':<15} {'Coef':>12} {'Std Err':>12} {'t-stat':>10} {'p-value':>10}",
            "-" * 70,
        ]

        # Intercept
        if self.config.fit_intercept:
            lines.append(f"{'Intercept':<15} {self.intercept:>12.4f} {self.statistics.standard_errors[0]:>12.4f} "
                        f"{self.statistics.t_statistics[0]:>10.4f} {self.statistics.p_values[0]:>10.4f}")

        # Feature coefficients
        offset = 1 if self.config.fit_intercept else 0
        for i in range(len(self.coefficients)):
            idx = i + offset
            if idx < len(self.statistics.standard_errors):
                lines.append(f"{'Feature_' + str(i):<15} {self.coefficients[i]:>12.4f} "
                            f"{self.statistics.standard_errors[idx]:>12.4f} "
                            f"{self.statistics.t_statistics[idx]:>10.4f} "
                            f"{self.statistics.p_values[idx]:>10.4f}")
            else:
                lines.append(f"{'Feature_' + str(i):<15} {self.coefficients[i]:>12.4f}")

        lines.extend([
            "\n" + "-" * 70,
            "                       MODEL STATISTICS",
            "-" * 70,
            f"{'R-squared:':<25} {self.statistics.r_squared:.6f}",
            f"{'Adjusted R-squared:':<25} {self.statistics.adjusted_r_squared:.6f}",
            f"{'MSE:':<25} {self.statistics.mse:.6f}",
            f"{'RMSE:':<25} {self.statistics.rmse:.6f}",
            f"{'MAE:':<25} {self.statistics.mae:.6f}",
            f"{'F-statistic:':<25} {self.statistics.f_statistic:.4f}",
            f"{'F p-value:':<25} {self.statistics.f_p_value:.6f}",
        ])

        # VIF if available
        if self.statistics.vif and len(self.statistics.vif) > 0:
            lines.extend([
                "\n" + "-" * 70,
                "               VARIANCE INFLATION FACTORS (VIF)",
                "-" * 70,
            ])
            for i, v in enumerate(self.statistics.vif):
                warning = " (high multicollinearity!)" if v > 10 else ""
                lines.append(f"{'Feature_' + str(i):<25} {v:.4f}{warning}")

        lines.append("\n" + "=" * 70)

        return "\n".join(lines)


# Example usage and demonstration
if __name__ == "__main__":
    import random

    print("=" * 70)
    print("          GLM - Linear Regression from Scratch Demo")
    print("=" * 70)

    # Generate synthetic data
    random.seed(42)
    n_samples = 200

    # True relationship: y = 3x1 + 2x2 - 1.5x3 + 5 + noise
    X = [[random.uniform(-5, 5) for _ in range(3)] for _ in range(n_samples)]
    y = [3 * x[0] + 2 * x[1] - 1.5 * x[2] + 5 + random.gauss(0, 1) for x in X]

    # Split data (simple split)
    split_idx = int(0.8 * n_samples)
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    print("\n1. BASIC OLS REGRESSION")
    print("-" * 50)

    config1 = ModelConfig(
        optimization=OptimizationMethod.OLS,
        scaling=ScalingType.STANDARDIZATION
    )
    model1 = LinearRegression(config1)
    model1.fit(X_train, y_train)
    print(model1.summary())

    # Test predictions
    predictions1 = model1.predict(X_test)
    print(f"\nSample predictions (first 5):")
    for i in range(5):
        print(f"  Actual: {y_test[i]:.2f}, Predicted: {predictions1[i]:.2f}")

    print("\n\n2. RIDGE REGRESSION (L2)")
    print("-" * 50)

    config2 = ModelConfig(
        optimization=OptimizationMethod.OLS,
        regularization=RegularizationType.L2,
        alpha=0.1,
        scaling=ScalingType.STANDARDIZATION
    )
    model2 = LinearRegression(config2)
    model2.fit(X_train, y_train)
    print(model2.summary())

    print("\n\n3. GRADIENT DESCENT WITH LASSO")
    print("-" * 50)

    config3 = ModelConfig(
        optimization=OptimizationMethod.BATCH_GD,
        regularization=RegularizationType.L1,
        alpha=0.01,
        learning_rate=0.1,
        max_iterations=5000,
        scaling=ScalingType.STANDARDIZATION
    )
    model3 = LinearRegression(config3)
    model3.fit(X_train, y_train)
    print(model3.summary())

    print("\n\n4. POLYNOMIAL REGRESSION")
    print("-" * 50)

    config4 = ModelConfig(
        optimization=OptimizationMethod.OLS,
        polynomial_degree=2,
        scaling=ScalingType.STANDARDIZATION
    )
    model4 = LinearRegression(config4)
    model4.fit(X_train, y_train)
    print(f"Polynomial features created: {model4.n_features}")
    print(f"R-squared: {model4.statistics.r_squared:.6f}")

    print("\n\n5. CROSS-VALIDATION")
    print("-" * 50)

    cv_results = model1.cross_validate(X, y, k_folds=5)
    print(f"Mean MSE: {cv_results['mean_mse']:.4f} (+/- {cv_results['std_mse']:.4f})")
    print(f"Mean R²: {cv_results['mean_r2']:.4f} (+/- {cv_results['std_r2']:.4f})")
    print(f"Mean MAE: {cv_results['mean_mae']:.4f}")

    print("\n\n6. PREDICTION INTERVALS")
    print("-" * 50)

    intervals = model1.predict_interval(X_test[:5])
    print("95% Prediction Intervals (lower, predicted, upper):")
    for i, (lower, pred, upper) in enumerate(intervals):
        print(f"  Sample {i+1}: [{lower:.2f}, {pred:.2f}, {upper:.2f}] (actual: {y_test[i]:.2f})")

    print("\n\n" + "=" * 70)
    print("                    DEMO COMPLETE!")
    print("=" * 70)