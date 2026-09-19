import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style('darkgrid')
sns.set_context("poster")


Vector = np.array([1, 2, 3])
Vector_1 = np.array([4, 5, 6])

sum = ((Vector @ Vector)*(Vector_1 @ Vector_1)) - (Vector @ Vector_1)**2

cross = abs(sum)
print(cross)
print(np.cross(Vector, Vector_1))