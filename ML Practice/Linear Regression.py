import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sympy as sp

x = np.array([1, 2, 3, 4, 5])
y = np.array([50, 55, 65, 70, 75])

# Calculate the mean of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate the slope (m) and intercept (b) of the line
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator
b = y_mean - m * x_mean

# Print the slope and intercept
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Plot the data points and the regression line
plt.scatter(x, y, color='blue', label='Data Points')
regression_line = m * x + b
plt.plot(x, regression_line, color='red', label='Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()

