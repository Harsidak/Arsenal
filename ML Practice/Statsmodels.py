import statsmodels.api as sm
import pandas as pd
import numpy as np

# Generate sample data for linear regression
np.random.seed(42)  # For reproducibility
n = 100  # Number of observations

# Create independent variables
X1 = np.random.normal(0, 1, n)
X2 = np.random.normal(0, 1, n)

# Create dependent variable with some noise
# True relationship: y = 2 + 3*X1 + 1.5*X2 + error
y = 2 + 3*X1 + 1.5*X2 + np.random.normal(0, 0.5, n)

# Create DataFrame
data = pd.DataFrame({
    'X1': X1,
    'X2': X2,
    'y': y
})

print("Sample data:")
print(data.head())
print("\nData summary:")
print(data.describe())

# Prepare the data for statsmodels
# Add constant (intercept) to the independent variables
X = sm.add_constant(data[['X1', 'X2']])

# Fit the OLS model
model = sm.OLS(data['y'], X).fit()

# Print the model summary
print("\n" + "="*50)
print("LINEAR REGRESSION MODEL SUMMARY")
print("="*50)
print(model.summary())

# Print the coefficients
print("\nCoefficients:")
print(f"Intercept: {model.params['const']:.4f}")
print(f"X1 coefficient: {model.params['X1']:.4f}")
print(f"X2 coefficient: {model.params['X2']:.4f}")

# Make predictions on the same data (for demonstration)
predictions = model.predict(X)
print(f"\nR-squared: {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")

# Calculate and print some additional statistics
print(f"\nF-statistic: {model.fvalue:.4f}")
print(f"Prob (F-statistic): {model.f_pvalue:.4f}")

# Residual analysis
residuals = model.resid
print(f"\nResidual statistics:")
print(f"Mean residual: {residuals.mean():.6f}")
print(f"Residual standard deviation: {residuals.std():.6f}")


