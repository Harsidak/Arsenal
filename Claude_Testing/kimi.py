import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class LinearRegression:
    """
    Linear Regression implementation using Gradient Descent.
    Uses only NumPy and Pandas (no scikit-learn, torch, tensorflow, or keras).
    """

    def __init__(self, learning_rate=0.01, n_iterations=1000, tolerance=1e-6):
        """
        Initialize Linear Regression model.

        Parameters:
        -----------
        learning_rate : float
            The step size for gradient descent (default: 0.01)
        n_iterations : int
            Maximum number of iterations for gradient descent (default: 1000)
        tolerance : float
            Minimum change in cost to continue iterations (default: 1e-6)
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.tolerance = tolerance
        self.weights = None
        self.bias = None
        self.cost_history = []
        self.weights_history = []

    def _initialize_parameters(self, n_features):
        """
        Initialize weights and bias to small random values or zeros.

        Parameters:
        -----------
        n_features : int
            Number of features in the dataset
        """
        # Initialize with small random values for better convergence
        np.random.seed(42)
        self.weights = np.random.randn(n_features) * 0.01
        self.bias = 0.0

    def _compute_hypothesis(self, X):
        """
        Compute the linear hypothesis: h(x) = X @ w + b

        Parameters:
        -----------
        X : np.ndarray
            Input features of shape (m, n)

        Returns:
        --------
        np.ndarray
            Predicted values of shape (m,)
        """
        return np.dot(X, self.weights) + self.bias

    def _compute_cost(self, y_pred, y_true):
        """
        Compute the Mean Squared Error (MSE) cost function.

        Cost = (1/2m) * sum((y_pred - y_true)^2)

        The 1/2 factor is for easier derivative calculation.

        Parameters:
        -----------
        y_pred : np.ndarray
            Predicted values
        y_true : np.ndarray
            Actual values

        Returns:
        --------
        float
            The cost value
        """
        m = len(y_true)
        cost = (1 / (2 * m)) * np.sum(np.square(y_pred - y_true))
        return cost

    def _compute_gradients(self, X, y_pred, y_true):
        """
        Compute gradients of the cost function with respect to weights and bias.

        dw = (1/m) * X^T @ (y_pred - y_true)
        db = (1/m) * sum(y_pred - y_true)

        Parameters:
        -----------
        X : np.ndarray
            Input features of shape (m, n)
        y_pred : np.ndarray
            Predicted values
        y_true : np.ndarray
            Actual values

        Returns:
        --------
        tuple
            (dw, db) gradients for weights and bias
        """
        m = len(y_true)
        error = y_pred - y_true

        # Compute gradients
        dw = (1 / m) * np.dot(X.T, error)
        db = (1 / m) * np.sum(error)

        return dw, db

    def _update_parameters(self, dw, db):
        """
        Update weights and bias using gradient descent.

        w = w - learning_rate * dw
        b = b - learning_rate * db

        Parameters:
        -----------
        dw : np.ndarray
            Gradient of weights
        db : float
            Gradient of bias
        """
        self.weights = self.weights - self.learning_rate * dw
        self.bias = self.bias - self.learning_rate * db

    def fit(self, X, y, verbose=True):
        """
        Train the linear regression model using gradient descent.

        Parameters:
        -----------
        X : np.ndarray or pd.DataFrame
            Training features of shape (m, n)
        y : np.ndarray or pd.Series
            Target values of shape (m,)
        verbose : bool
            Whether to print training progress

        Returns:
        --------
        self
        """
        # Convert inputs to numpy arrays
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, (pd.Series, pd.DataFrame)):
            y = y.values

        # Ensure y is 1D array
        y = y.ravel()

        # Get number of samples and features
        m, n = X.shape

        # Initialize parameters
        self._initialize_parameters(n)

        # Store initial weights
        self.weights_history.append(self.weights.copy())

        if verbose:
            print(f"Training Linear Regression...")
            print(f"Samples: {m}, Features: {n}")
            print(f"Learning Rate: {self.learning_rate}")
            print(f"Max Iterations: {self.n_iterations}")
            print("-" * 50)

        # Gradient Descent
        for i in range(self.n_iterations):
            # Forward pass: compute predictions
            y_pred = self._compute_hypothesis(X)

            # Compute cost
            cost = self._compute_cost(y_pred, y)
            self.cost_history.append(cost)

            # Backward pass: compute gradients
            dw, db = self._compute_gradients(X, y_pred, y)

            # Update parameters
            self._update_parameters(dw, db)
            self.weights_history.append(self.weights.copy())

            # Print progress
            if verbose and i % 100 == 0:
                print(f"Iteration {i}: Cost = {cost:.6f}")

            # Check for convergence
            if i > 0 and abs(self.cost_history[i-1] - cost) < self.tolerance:
                if verbose:
                    print(f"Converged at iteration {i}")
                break

        if verbose:
            print("-" * 50)
            print(f"Final Cost: {self.cost_history[-1]:.6f}")
            print(f"Final Weights: {self.weights}")
            print(f"Final Bias: {self.bias:.6f}")

        return self

    def predict(self, X):
        """
        Make predictions using the trained model.

        Parameters:
        -----------
        X : np.ndarray or pd.DataFrame
            Input features

        Returns:
        --------
        np.ndarray
            Predicted values
        """
        if self.weights is None or self.bias is None:
            raise ValueError("Model has not been trained yet. Call fit() first.")

        if isinstance(X, pd.DataFrame):
            X = X.values

        return self._compute_hypothesis(X)

    def score(self, X, y):
        """
        Calculate R-squared score.

        Parameters:
        -----------
        X : np.ndarray or pd.DataFrame
            Input features
        y : np.ndarray or pd.Series
            True target values

        Returns:
        --------
        float
            R-squared score
        """
        if isinstance(y, (pd.Series, pd.DataFrame)):
            y = y.values
        y = y.ravel()

        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2

    def get_cost_history(self):
        """Return the cost history from training."""
        return self.cost_history

    def get_params(self):
        """Return the learned parameters."""
        return {
            'weights': self.weights,
            'bias': self.bias
        }

    def plot_cost_history(self):
        """Plot the cost function over iterations."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.cost_history, 'b-', linewidth=2)
        plt.title('Cost Function vs. Iterations', fontsize=14)
        plt.xlabel('Iteration', fontsize=12)
        plt.ylabel('Cost (MSE)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.show()


class FeatureScaler:
    """
    Feature scaling using Standardization (Z-score normalization).
    Required for gradient descent to converge faster.
    """

    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, X):
        """Calculate mean and std for scaling."""
        if isinstance(X, pd.DataFrame):
            X = X.values
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        # Avoid division by zero
        self.std[self.std == 0] = 1
        return self

    def transform(self, X):
        """Scale features."""
        if isinstance(X, pd.DataFrame):
            X = X.values
        return (X - self.mean) / self.std

    def fit_transform(self, X):
        """Fit and transform in one step."""
        return self.fit(X).transform(X)

    def inverse_transform(self, X_scaled):
        """Reverse the scaling."""
        return X_scaled * self.std + self.mean


def generate_sample_data(n_samples=100, noise=10, random_seed=42):
    """
    Generate sample linear regression data for testing.

    Parameters:
    -----------
    n_samples : int
        Number of samples to generate
    noise : float
        Amount of noise to add
    random_seed : int
        Random seed for reproducibility

    Returns:
    --------
    tuple
        (X, y) features and target
    """
    np.random.seed(random_seed)

    # Generate random features
    X = np.random.randn(n_samples, 2)

    # True parameters
    true_weights = np.array([3.5, -2.0])
    true_bias = 5.0

    # Generate target with noise
    y = X @ true_weights + true_bias + np.random.randn(n_samples) * noise

    return X, y, true_weights, true_bias


# Example usage and testing
if __name__ == "__main__":
    print("=" * 60)
    print("LINEAR REGRESSION WITH GRADIENT DESCENT")
    print("=" * 60)

    # Generate sample data
    print("\n1. Generating Sample Data...")
    X, y, true_w, true_b = generate_sample_data(n_samples=200, noise=5)
    print(f"   True Weights: {true_w}")
    print(f"   True Bias: {true_b}")

    # Split into train and test
    split_idx = int(0.8 * len(X))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    # Feature scaling (important for gradient descent)
    print("\n2. Scaling Features...")
    scaler = FeatureScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train model
    print("\n3. Training Model...")
    model = LinearRegression(
        learning_rate=0.1,
        n_iterations=1000,
        tolerance=1e-8
    )
    model.fit(X_train_scaled, y_train)

    # Make predictions
    print("\n4. Making Predictions...")
    y_pred_train = model.predict(X_train_scaled)
    y_pred_test = model.predict(X_test_scaled)

    # Calculate metrics
    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)

    print(f"\n   Training R² Score: {train_score:.4f}")
    print(f"   Testing R² Score: {test_score:.4f}")

    # Calculate MSE manually
    train_mse = np.mean((y_train - y_pred_train) ** 2)
    test_mse = np.mean((y_test - y_pred_test) ** 2)
    print(f"   Training MSE: {train_mse:.4f}")
    print(f"   Testing MSE: {test_mse:.4f}")

    # Show learned parameters
    params = model.get_params()
    print(f"\n   Learned Weights: {params['weights']}")
    print(f"   Learned Bias: {params['bias']:.6f}")

    # Plot cost history
    print("\n5. Plotting Cost History...")
    model.plot_cost_history()

    # Example with pandas DataFrame
    print("\n" + "=" * 60)
    print("EXAMPLE WITH PANDAS DATAFRAME")
    print("=" * 60)

    # Create DataFrame
    df = pd.DataFrame({
        'Feature_1': np.random.randn(100),
        'Feature_2': np.random.randn(100),
        'Target': None
    })
    df['Target'] = 2.5 * df['Feature_1'] + (-1.5) * df['Feature_2'] + 3.0 + np.random.randn(100) * 0.5

    X_df = df[['Feature_1', 'Feature_2']]
    y_df = df['Target']

    # Train model
    model2 = LinearRegression(learning_rate=0.1, n_iterations=500)
    model2.fit(X_df, y_df)

    print(f"\n   Final R² Score: {model2.score(X_df, y_df):.4f}")
    print(f"   Final Cost: {model2.get_cost_history()[-1]:.6f}")

    print("\n" + "=" * 60)
    print("TRAINING COMPLETE!")
    print("=" * 60)
