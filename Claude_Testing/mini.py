"""
Linear Regression Implementation from Scratch
==============================================
A clean, robust implementation of Linear Regression using only NumPy and Pandas.
No scikit-learn, TensorFlow, PyTorch, or Keras.
"""

import numpy as np
import pandas as pd
from typing import Tuple, Optional


class LinearRegression:
    """
    Linear Regression model implemented from scratch using NumPy.

    Supports:
    - Simple linear regression (single feature)
    - Multiple linear regression (multiple features)
    - Polynomial regression (via feature expansion)
    - L2 regularization (Ridge)
    - Gradient descent and Normal Equation solvers
    """

    def __init__(
        self,
        learning_rate: float = 0.01,
        n_iterations: int = 1000,
        regularization: float = 0.0,
        solver: str = "gradient_descent",
        early_stopping: bool = True,
        tol: float = 1e-6
    ):
        """
        Initialize the Linear Regression model.

        Args:
            learning_rate: Step size for gradient descent
            n_iterations: Maximum number of iterations
            regularization: L2 regularization strength (Ridge)
            solver: "gradient_descent" or "normal_equation"
            early_stopping: Stop if loss stops improving
            tol: Minimum improvement threshold for early stopping
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.regularization = regularization
        self.solver = solver
        self.early_stopping = early_stopping
        self.tol = tol

        self.weights: Optional[np.ndarray] = None
        self.bias: Optional[float] = None
        self.loss_history: list = []

    def _add_bias(self, X: np.ndarray) -> np.ndarray:
        """Add bias term to feature matrix."""
        return np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

    def _normalize(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Normalize features for gradient descent solver.
        Returns normalized X, mean, and std for later denormalization.
        """
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        std[std == 0] = 1  # Avoid division by zero
        X_normalized = (X - mean) / std
        return X_normalized, mean, std

    def _compute_loss(self, X: np.ndarray, y: np.ndarray) -> float:
        """Compute Mean Squared Error with L2 regularization."""
        n_samples = X.shape[0]
        predictions = self._predict_raw(X)
        loss = (1 / (2 * n_samples)) * np.sum((predictions - y) ** 2)
        if self.regularization > 0:
            loss += (self.regularization / (2 * n_samples)) * np.sum(self.weights[1:] ** 2)
        return loss

    def _predict_raw(self, X: np.ndarray) -> np.ndarray:
        """Raw prediction without denormalization."""
        return np.dot(X, self.weights) + self.bias

    def fit_gradient_descent(self, X: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """Fit using batch gradient descent."""
        n_samples, n_features = X.shape

        # Normalize for gradient descent
        X_norm, self._mean, self._std = self._normalize(X)

        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Add bias to X for unified computation
        X_norm = self._add_bias(X_norm)

        # Gradient descent
        self.loss_history = []
        for i in range(self.n_iterations):
            predictions = np.dot(X_norm, self.weights) + self.bias
            errors = predictions - y

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X_norm.T, errors)
            db = (1 / n_samples) * np.sum(errors)

            # Apply L2 regularization to weights (not bias)
            if self.regularization > 0:
                dw[1:] += (self.regularization / n_samples) * self.weights[1:]

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Track loss
            loss = self._compute_loss(X_norm[:, 1:], y)
            self.loss_history.append(loss)

            # Early stopping
            if self.early_stopping and i > 0:
                if abs(self.loss_history[-2] - loss) < self.tol:
                    print(f"Early stopping at iteration {i}")
                    break

        return self

    def fit_normal_equation(self, X: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """
        Fit using the Normal Equation (analytical solution).
        Includes regularization for numerical stability.
        """
        X_with_bias = self._add_bias(X)

        # Add regularization for numerical stability (pseudo-inverse)
        if self.regularization > 0:
            n_features = X_with_bias.shape[1]
            regularization_matrix = self.regularization * np.eye(n_features)
            regularization_matrix[0, 0] = 0  # Don't regularize bias
            XTX = np.dot(X_with_bias.T, X_with_bias) + regularization_matrix
        else:
            XTX = np.dot(X_with_bias.T, X_with_bias)

        # Solve using pseudo-inverse for numerical stability
        try:
            XTX_inv = np.linalg.pinv(XTX)
            self.weights = np.dot(XTX_inv, np.dot(X_with_bias.T, y))
        except np.linalg.LinAlgError:
            # Fallback to SVD-based solution
            U, S, Vt = np.linalg.svd(X_with_bias, full_matrices=False)
            self.weights = np.dot(Vt.T, np.dot(U.T, y) / S)

        self.bias = self.weights[0]
        self.weights = self.weights[1:]

        return self

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """
        Fit the linear regression model to the data.

        Args:
            X: Feature matrix of shape (n_samples, n_features)
            y: Target values of shape (n_samples,)

        Returns:
            self
        """
        X = np.asarray(X, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        if y.ndim == 0:
            y = y.reshape(-1, 1)

        if self.solver == "gradient_descent":
            self.fit_gradient_descent(X, y)
        elif self.solver == "normal_equation":
            self.fit_normal_equation(X, y)
        else:
            raise ValueError(f"Unknown solver: {self.solver}")

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions.

        Args:
            X: Feature matrix of shape (n_samples, n_features)

        Returns:
            Predictions of shape (n_samples,)
        """
        X = np.asarray(X, dtype=np.float64)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        if self.weights is None:
            raise RuntimeError("Model not fitted. Call fit() first.")

        # Normalize using stored statistics (gradient descent)
        if hasattr(self, "_mean") and hasattr(self, "_std"):
            X = (X - self._mean) / self._std

        return np.dot(X, self.weights) + self.bias

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute R² coefficient of determination.

        Args:
            X: Feature matrix
            y: True target values

        Returns:
            R² score
        """
        predictions = self.predict(X)
        y = np.asarray(y).flatten()

        ss_res = np.sum((y - predictions) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)

        if ss_tot == 0:
            return 0.0

        return 1 - (ss_res / ss_tot)

    def get_coefficients(self) -> Tuple[np.ndarray, float]:
        """Return learned weights and bias."""
        if self.weights is None:
            raise RuntimeError("Model not fitted. Call fit() first.")
        return self.weights.copy(), self.bias


class DataLoader:
    """Utility class for loading and preprocessing data."""

    @staticmethod
    def load_csv(filepath: str) -> pd.DataFrame:
        """Load data from CSV file."""
        return pd.read_csv(filepath)

    @staticmethod
    def train_test_split(
        X: np.ndarray,
        y: np.ndarray,
        test_size: float = 0.2,
        random_state: Optional[int] = None
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Split data into train and test sets.

        Args:
            X: Feature matrix
            y: Target vector
            test_size: Proportion of data for testing
            random_state: Random seed for reproducibility

        Returns:
            X_train, X_test, y_train, y_test
        """
        if random_state is not None:
            np.random.seed(random_state)

        n_samples = X.shape[0]
        indices = np.random.permutation(n_samples)
        test_count = int(n_samples * test_size)

        test_indices = indices[:test_count]
        train_indices = indices[test_count:]

        return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

    @staticmethod
    def standardize(X_train: np.ndarray, X_test: np.ndarray
                    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Standardize features using training set statistics.

        Returns:
            Standardized X_train, X_test, mean, std
        """
        mean = np.mean(X_train, axis=0)
        std = np.std(X_train, axis=0)
        std[std == 0] = 1

        X_train_scaled = (X_train - mean) / std
        X_test_scaled = (X_test - mean) / std

        return X_train_scaled, X_test_scaled, mean, std


def demo():
    """Demonstrate the Linear Regression implementation."""
    print("=" * 60)
    print("Linear Regression from Scratch - Demo")
    print("=" * 60)

    # Generate synthetic data
    np.random.seed(42)
    n_samples = 200

    # Features: size, bedrooms, age
    X = np.random.rand(n_samples, 3) * 100
    X[:, 0] = X[:, 0] * 5 + 1  # Size: 1-600 sqft
    X[:, 1] = np.floor(X[:, 1] * 4) + 1  # 1-5 bedrooms
    X[:, 2] = np.random.rand(n_samples) * 50  # Age: 0-50 years

    # Target: House price (in thousands)
    # True relationship: price = 50 + 0.3*size + 10*bedrooms - 0.5*age + noise
    y = 50 + 0.3 * X[:, 0] + 10 * X[:, 1] - 0.5 * X[:, 2]
    y += np.random.randn(n_samples) * 5  # Add Gaussian noise

    print("\n1. Dataset Summary")
    print("-" * 40)
    print(f"   Samples: {n_samples}")
    print(f"   Features: {X.shape[1]}")
    print(f"   Feature names: ['size', 'bedrooms', 'age']")

    # Split data
    X_train, X_test, y_train, y_test = DataLoader.train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Standardize
    X_train, X_test, _, _ = DataLoader.standardize(X_train, X_test)

    print(f"\n2. Train/Test Split")
    print("-" * 40)
    print(f"   Training samples: {X_train.shape[0]}")
    print(f"   Test samples: {X_test.shape[0]}")

    # Train with Gradient Descent
    print("\n3. Training with Gradient Descent")
    print("-" * 40)

    model_gd = LinearRegression(
        learning_rate=0.1,
        n_iterations=2000,
        regularization=0.01,
        solver="gradient_descent",
        early_stopping=True,
        tol=1e-8
    )

    model_gd.fit(X_train, y_train)

    train_score_gd = model_gd.score(X_train, y_train)
    test_score_gd = model_gd.score(X_test, y_test)

    print(f"   Final loss: {model_gd.loss_history[-1]:.4f}")
    print(f"   Train R²: {train_score_gd:.4f}")
    print(f"   Test R²: {test_score_gd:.4f}")

    weights, bias = model_gd.get_coefficients()
    print(f"   Coefficients: {weights}")
    print(f"   Bias: {bias:.4f}")

    # Train with Normal Equation
    print("\n4. Training with Normal Equation")
    print("-" * 40)

    model_ne = LinearRegression(
        regularization=0.01,
        solver="normal_equation"
    )

    model_ne.fit(X_train, y_train)

    train_score_ne = model_ne.score(X_train, y_train)
    test_score_ne = model_ne.score(X_test, y_test)

    print(f"   Train R²: {train_score_ne:.4f}")
    print(f"   Test R²: {test_score_ne:.4f}")

    weights_ne, bias_ne = model_ne.get_coefficients()
    print(f"   Coefficients: {weights_ne}")
    print(f"   Bias: {bias_ne:.4f}")

    # Comparison Summary
    print("\n5. Comparison Summary")
    print("-" * 40)
    print(f"   {'Method':<20} {'Train R²':<12} {'Test R²':<12}")
    print(f"   {'-'*44}")
    print(f"   {'Gradient Descent':<20} {train_score_gd:<12.4f} {test_score_gd:<12.4f}")
    print(f"   {'Normal Equation':<20} {train_score_ne:<12.4f} {test_score_ne:<12.4f}")

    # Predictions demo
    print("\n6. Sample Predictions")
    print("-" * 40)
    sample_indices = [0, 5, 10]
    print(f"   {'Actual':<12} {'Predicted':<12} {'Error':<12}")
    print(f"   {'-'*36}")
    for idx in sample_indices:
        pred = model_ne.predict(X_test[idx:idx+1])[0]
        actual = y_test[idx]
        error = actual - pred
        print(f"   {actual:<12.2f} {pred:<12.2f} {error:<12.2f}")

    # Feature importance
    print("\n7. Feature Importance (by coefficient magnitude)")
    print("-" * 40)
    feature_names = ['size', 'bedrooms', 'age']
    importance = np.abs(weights_ne)
    sorted_idx = np.argsort(importance)[::-1]
    for rank, idx in enumerate(sorted_idx, 1):
        print(f"   {rank}. {feature_names[idx]}: {importance[idx]:.4f}")

    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    demo()
