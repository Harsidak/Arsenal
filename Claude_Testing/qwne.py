"""
Linear Regression from Scratch
==============================
A robust and optimized implementation of Linear Regression with:
- Gradient Descent optimization
- Mean Squared Error (MSE) cost function
- L1/L2 Regularization
- Learning rate scheduling
- Early stopping
- Feature normalization
"""

import numpy as np
from typing import Tuple, Optional, List, Dict, Union
from dataclasses import dataclass
from enum import Enum


class RegularizationType(Enum):
    """Types of regularization supported."""
    NONE = "none"
    L1 = "l1"      # Lasso
    L2 = "l2"      # Ridge
    ELASTIC = "elastic"  # Elastic Net


class LearningRateSchedule(Enum):
    """Learning rate scheduling strategies."""
    CONSTANT = "constant"
    STEP_DECAY = "step_decay"
    EXPONENTIAL = "exponential"
    ADAPTIVE = "adaptive"


@dataclass
class TrainingConfig:
    """Configuration for training hyperparameters."""
    learning_rate: float = 0.01
    n_iterations: int = 1000
    batch_size: Optional[int] = None  # None = batch gradient descent
    regularization_type: RegularizationType = RegularizationType.NONE
    reg_lambda: float = 0.01  # Regularization strength
    alpha: float = 0.5  # Elastic net mixing parameter (0=L2, 1=L1)
    lr_schedule: LearningRateSchedule = LearningRateSchedule.CONSTANT
    lr_decay_rate: float = 0.95
    lr_decay_steps: int = 100
    patience: int = 50  # Early stopping patience
    min_delta: float = 1e-6  # Minimum change for early stopping
    verbose: bool = True


class FeatureNormalizer:
    """
    Handles feature normalization (Standardization).
    Stores parameters for consistent transformation.
    """

    def __init__(self):
        self.mean: Optional[np.ndarray] = None
        self.std: Optional[np.ndarray] = None
        self.is_fitted: bool = False

    def fit(self, X: np.ndarray) -> 'FeatureNormalizer':
        """Compute mean and std for each feature."""
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        # Prevent division by zero
        self.std[self.std == 0] = 1.0
        self.is_fitted = True
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Apply normalization using stored parameters."""
        if not self.is_fitted:
            raise ValueError("Normalizer not fitted. Call fit() first.")
        return (X - self.mean) / self.std

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """Fit and transform in one step."""
        return self.fit(X).transform(X)

    def inverse_transform(self, X: np.ndarray) -> np.ndarray:
        """Reverse the normalization."""
        if not self.is_fitted:
            raise ValueError("Normalizer not fitted.")
        return X * self.std + self.mean


class LinearRegressionScratch:
    """
    Linear Regression implemented from scratch with Gradient Descent.

    Features:
    - Batch, Mini-batch, and Stochastic Gradient Descent
    - L1, L2, and Elastic Net regularization
    - Learning rate scheduling
    - Early stopping
    - Feature normalization
    - Training history tracking
    """

    def __init__(self, config: Optional[TrainingConfig] = None):
        """Initialize the Linear Regression model."""
        self.config = config or TrainingConfig()
        self.weights: Optional[np.ndarray] = None
        self.bias: float = 0.0
        self.normalizer: Optional[FeatureNormalizer] = None
        self.training_history: Dict[str, List[float]] = {
            'cost': [],
            'val_cost': [],
            'learning_rate': []
        }
        self.is_fitted: bool = False
        self.n_features: int = 0

    def _initialize_parameters(self, n_features: int) -> None:
        """Initialize weights using He initialization."""
        self.n_features = n_features
        # He initialization for better convergence
        self.weights = np.random.randn(n_features) * np.sqrt(2.0 / n_features)
        self.bias = 0.0

    def _compute_cost(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute the cost function (MSE with regularization).

        Cost = (1/2n) * Σ(y_pred - y)² + regularization_term
        """
        n_samples = len(y)
        predictions = self._predict_raw(X)
        errors = predictions - y

        # Base MSE cost
        cost = (1 / (2 * n_samples)) * np.sum(errors ** 2)

        # Add regularization term
        cost += self._compute_regularization(n_samples)

        return float(cost)

    def _compute_regularization(self, n_samples: int) -> float:
        """Compute regularization penalty."""
        reg_type = self.config.regularization_type
        reg_lambda = self.config.reg_lambda

        if reg_type == RegularizationType.NONE or self.weights is None:
            return 0.0

        if reg_type == RegularizationType.L2:
            return (reg_lambda / (2 * n_samples)) * np.sum(self.weights ** 2)

        elif reg_type == RegularizationType.L1:
            return (reg_lambda / n_samples) * np.sum(np.abs(self.weights))

        elif reg_type == RegularizationType.ELASTIC:
            alpha = self.config.alpha
            l2_term = (reg_lambda / (2 * n_samples)) * np.sum(self.weights ** 2)
            l1_term = (reg_lambda * alpha / n_samples) * np.sum(np.abs(self.weights))
            return l1_term + l2_term

        return 0.0

    def _compute_gradients(self, X: np.ndarray, y: np.ndarray,
                          batch_indices: Optional[np.ndarray] = None) -> Tuple[np.ndarray, float]:
        """
        Compute gradients for weights and bias.

        For MSE: d(cost)/d(w) = (1/n) * X.T @ (predictions - y) + reg_gradient
        """
        if batch_indices is not None:
            X_batch = X[batch_indices]
            y_batch = y[batch_indices]
        else:
            X_batch = X
            y_batch = y

        n_samples = len(y_batch)
        predictions = self._predict_raw(X_batch)
        errors = predictions - y_batch

        # Base gradients
        dw = (1 / n_samples) * X_batch.T @ errors
        db = (1 / n_samples) * np.sum(errors)

        # Add regularization gradients
        dw += self._compute_regularization_gradient(n_samples)

        return dw, float(db)

    def _compute_regularization_gradient(self, n_samples: int) -> np.ndarray:
        """Compute gradient of regularization term."""
        reg_type = self.config.regularization_type
        reg_lambda = self.config.reg_lambda

        if reg_type == RegularizationType.NONE or self.weights is None:
            return np.zeros_like(self.weights)

        if reg_type == RegularizationType.L2:
            return (reg_lambda / n_samples) * self.weights

        elif reg_type == RegularizationType.L1:
            # Subgradient for L1
            return (reg_lambda / n_samples) * np.sign(self.weights)

        elif reg_type == RegularizationType.ELASTIC:
            alpha = self.config.alpha
            l2_grad = (reg_lambda / n_samples) * self.weights
            l1_grad = (reg_lambda * alpha / n_samples) * np.sign(self.weights)
            return l1_grad + l2_grad

        return np.zeros_like(self.weights)

    def _predict_raw(self, X: np.ndarray) -> np.ndarray:
        """Make predictions (internal, no normalization)."""
        return X @ self.weights + self.bias

    def _adjust_learning_rate(self, iteration: int) -> float:
        """Adjust learning rate based on schedule."""
        base_lr = self.config.learning_rate
        schedule = self.config.lr_schedule

        if schedule == LearningRateSchedule.CONSTANT:
            lr = base_lr

        elif schedule == LearningRateSchedule.STEP_DECAY:
            decay_steps = self.config.lr_decay_steps
            decay_rate = self.config.lr_decay_rate
            lr = base_lr * (decay_rate ** (iteration // decay_steps))

        elif schedule == LearningRateSchedule.EXPONENTIAL:
            decay_rate = self.config.lr_decay_rate
            lr = base_lr * (decay_rate ** iteration)

        elif schedule == LearningRateSchedule.ADAPTIVE:
            # Reduce LR if cost is not improving significantly
            if len(self.training_history['cost']) > 10:
                recent_costs = self.training_history['cost'][-10:]
                if max(recent_costs) - min(recent_costs) < self.config.min_delta * 10:
                    lr = base_lr * 0.5
                else:
                    lr = base_lr
            else:
                lr = base_lr
        else:
            lr = base_lr

        # Ensure minimum learning rate
        lr = max(lr, 1e-8)
        return lr

    def _check_early_stopping(self) -> bool:
        """Check if early stopping conditions are met."""
        if len(self.training_history['cost']) < self.config.patience + 1:
            return False

        recent_costs = self.training_history['cost'][-self.config.patience:]
        best_recent = min(recent_costs)
        current = self.training_history['cost'][-1]

        # If current cost is not significantly better than best recent
        return (best_recent - current) < self.config.min_delta

    def fit(self, X: np.ndarray, y: np.ndarray,
            X_val: Optional[np.ndarray] = None,
            y_val: Optional[np.ndarray] = None,
            use_normalization: bool = True) -> 'LinearRegressionScratch':
        """
        Train the linear regression model.

        Parameters:
        -----------
        X : np.ndarray
            Training features (n_samples, n_features)
        y : np.ndarray
            Target values (n_samples,)
        X_val : np.ndarray, optional
            Validation features for early stopping
        y_val : np.ndarray, optional
            Validation target values
        use_normalization : bool
            Whether to normalize features (recommended)

        Returns:
        --------
        self : LinearRegressionScratch
            Fitted model
        """
        # Input validation
        X = np.array(X, dtype=np.float64)
        y = np.array(y, dtype=np.float64).flatten()

        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must have the same number of samples")

        if X.shape[0] == 0 or X.shape[1] == 0:
            raise ValueError("X must have at least one sample and one feature")

        # Normalize features
        if use_normalization:
            self.normalizer = FeatureNormalizer()
            X_normalized = self.normalizer.fit_transform(X)
            if X_val is not None:
                X_val_normalized = self.normalizer.transform(X_val)
        else:
            self.normalizer = None
            X_normalized = X
            X_val_normalized = X_val

        # Initialize parameters
        self._initialize_parameters(X_normalized.shape[1])

        # Training loop
        n_samples = X_normalized.shape[0]
        batch_size = self.config.batch_size or n_samples  # Default to batch GD

        if self.config.verbose:
            print(f"Starting training for {self.config.n_iterations} iterations...")
            print(f"Samples: {n_samples}, Features: {self.n_features}")
            print(f"Batch size: {batch_size}, Initial LR: {self.config.learning_rate}")
            print("-" * 60)

        best_cost = float('inf')
        patience_counter = 0

        for iteration in range(self.config.n_iterations):
            # Adjust learning rate
            current_lr = self._adjust_learning_rate(iteration)
            self.training_history['learning_rate'].append(current_lr)

            # Mini-batch selection
            if batch_size < n_samples:
                indices = np.random.choice(n_samples, batch_size, replace=False)
            else:
                indices = None

            # Compute gradients
            dw, db = self._compute_gradients(X_normalized, y, indices)

            # Gradient descent update
            self.weights -= current_lr * dw
            self.bias -= current_lr * db

            # Compute cost every 10 iterations for efficiency
            if iteration % 10 == 0 or iteration == self.config.n_iterations - 1:
                cost = self._compute_cost(X_normalized, y)
                self.training_history['cost'].append(cost)

                # Validation cost
                if X_val_normalized is not None and y_val is not None:
                    val_cost = self._compute_cost(X_val_normalized, y_val)
                    self.training_history['val_cost'].append(val_cost)

                    # Early stopping based on validation cost
                    if val_cost < best_cost - self.config.min_delta:
                        best_cost = val_cost
                        patience_counter = 0
                    else:
                        patience_counter += 1
                else:
                    # Early stopping based on training cost
                    if self._check_early_stopping():
                        patience_counter += 1
                    else:
                        patience_counter = 0

                # Print progress
                if self.config.verbose and (iteration % 100 == 0 or iteration == self.config.n_iterations - 1):
                    val_msg = ""
                    if self.training_history['val_cost']:
                        val_msg = f", Val Cost: {self.training_history['val_cost'][-1]:.6f}"
                    print(f"Iter {iteration:4d} | Cost: {cost:.6f}{val_msg} | LR: {current_lr:.2e}")

                # Early stopping
                if patience_counter >= self.config.patience:
                    if self.config.verbose:
                        print(f"\nEarly stopping at iteration {iteration}")
                    break

        self.is_fitted = True

        if self.config.verbose:
            print("-" * 60)
            print("Training completed!")
            print(f"Final Cost: {self.training_history['cost'][-1]:.6f}")

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data.

        Parameters:
        -----------
        X : np.ndarray
            Features (n_samples, n_features)

        Returns:
        --------
        predictions : np.ndarray
            Predicted values (n_samples,)
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")

        X = np.array(X, dtype=np.float64)

        # Apply same normalization as training
        if self.normalizer is not None:
            X_normalized = self.normalizer.transform(X)
        else:
            X_normalized = X

        return self._predict_raw(X_normalized)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute R² (coefficient of determination) score.

        R² = 1 - SS_res / SS_tot

        Parameters:
        -----------
        X : np.ndarray
            Features
        y : np.ndarray
            True target values

        Returns:
        --------
        r2 : float
            R² score (1.0 is perfect, can be negative)
        """
        y = np.array(y).flatten()
        predictions = self.predict(X)

        ss_res = np.sum((y - predictions) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)

        if ss_tot == 0:
            return 1.0 if ss_res == 0 else 0.0

        return 1 - (ss_res / ss_tot)

    def mean_squared_error(self, X: np.ndarray, y: np.ndarray) -> float:
        """Compute Mean Squared Error."""
        y = np.array(y).flatten()
        predictions = self.predict(X)
        return float(np.mean((y - predictions) ** 2))

    def mean_absolute_error(self, X: np.ndarray, y: np.ndarray) -> float:
        """Compute Mean Absolute Error."""
        y = np.array(y).flatten()
        predictions = self.predict(X)
        return float(np.mean(np.abs(y - predictions)))

    def root_mean_squared_error(self, X: np.ndarray, y: np.ndarray) -> float:
        """Compute Root Mean Squared Error."""
        return np.sqrt(self.mean_squared_error(X, y))

    def get_coefficients(self) -> Tuple[np.ndarray, float]:
        """
        Get the learned coefficients.

        Returns:
        --------
        weights : np.ndarray
            Feature coefficients
        bias : float
            Intercept term
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted.")
        return self.weights.copy(), self.bias

    def get_training_history(self) -> Dict[str, List[float]]:
        """Get the training history for analysis."""
        return self.training_history.copy()


# ============================================================================
# Example Usage and Testing
# ============================================================================

def generate_sample_data(n_samples: int = 1000, n_features: int = 5,
                         noise: float = 0.1, random_seed: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate synthetic linear regression data."""
    np.random.seed(random_seed)

    X = np.random.randn(n_samples, n_features)

    # True coefficients
    true_weights = np.random.randn(n_features)
    true_bias = np.random.randn()

    # Generate y with some noise
    y = X @ true_weights + true_bias + noise * np.random.randn(n_samples)

    return X, y, np.concatenate([true_weights, [true_bias]])


def demo():
    """Demonstrate the Linear Regression implementation."""
    print("=" * 70)
    print("LINEAR REGRESSION FROM SCRATCH - DEMO")
    print("=" * 70)
    print()

    # Generate sample data
    X, y, true_params = generate_sample_data(n_samples=1000, n_features=5, noise=0.1)

    # Split data
    split_idx = int(0.8 * len(X))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    print(f"Features: {X.shape[1]}")
    print()

    # Configuration 1: Basic Gradient Descent
    print("-" * 70)
    print("CONFIG 1: Basic Gradient Descent")
    print("-" * 70)

    config1 = TrainingConfig(
        learning_rate=0.1,
        n_iterations=1000,
        verbose=True
    )

    model1 = LinearRegressionScratch(config1)
    model1.fit(X_train, y_train, X_test, y_test)

    print(f"\nTest R² Score: {model1.score(X_test, y_test):.4f}")
    print(f"Test MSE: {model1.mean_squared_error(X_test, y_test):.4f}")
    print()

    # Configuration 2: With L2 Regularization
    print("-" * 70)
    print("CONFIG 2: L2 Regularization (Ridge)")
    print("-" * 70)

    config2 = TrainingConfig(
        learning_rate=0.1,
        n_iterations=1000,
        regularization_type=RegularizationType.L2,
        reg_lambda=0.1,
        verbose=True
    )

    model2 = LinearRegressionScratch(config2)
    model2.fit(X_train, y_train, X_test, y_test)

    print(f"\nTest R² Score: {model2.score(X_test, y_test):.4f}")
    print(f"Test MSE: {model2.mean_squared_error(X_test, y_test):.4f}")
    print()

    # Configuration 3: Mini-batch Gradient Descent
    print("-" * 70)
    print("CONFIG 3: Mini-batch Gradient Descent")
    print("-" * 70)

    config3 = TrainingConfig(
        learning_rate=0.1,
        n_iterations=1000,
        batch_size=32,
        lr_schedule=LearningRateSchedule.STEP_DECAY,
        verbose=True
    )

    model3 = LinearRegressionScratch(config3)
    model3.fit(X_train, y_train, X_test, y_test)

    print(f"\nTest R² Score: {model3.score(X_test, y_test):.4f}")
    print(f"Test MSE: {model3.mean_squared_error(X_test, y_test):.4f}")
    print()

    # Configuration 4: With Early Stopping
    print("-" * 70)
    print("CONFIG 4: Early Stopping")
    print("-" * 70)

    config4 = TrainingConfig(
        learning_rate=0.1,
        n_iterations=5000,
        patience=100,
        min_delta=1e-7,
        verbose=True
    )

    model4 = LinearRegressionScratch(config4)
    model4.fit(X_train, y_train, X_test, y_test)

    print(f"\nTest R² Score: {model4.score(X_test, y_test):.4f}")
    print(f"Test MSE: {model4.mean_squared_error(X_test, y_test):.4f}")
    print()

    # Compare learned vs true parameters
    print("-" * 70)
    print("PARAMETER COMPARISON")
    print("-" * 70)

    learned_weights, learned_bias = model1.get_coefficients()

    print("\nTrue weights:")
    print(f"  {true_params[:-1]}")
    print("\nLearned weights:")
    print(f"  {learned_weights}")
    print(f"\nTrue bias: {true_params[-1]:.4f}")
    print(f"Learned bias: {learned_bias:.4f}")

    print()
    print("=" * 70)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    demo()
