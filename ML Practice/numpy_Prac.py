import numpy as np
# from numpy import random
# # to create a numpy array 
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# transpose_matrix = np.array(list(zip(*matrix)))

# Matrix_90 = []
# for i in range(0,3):
#     Matrix_90.append(transpose_matrix[i][::-1])
# print(np.array(Matrix_90))

# numpy reshape
"""
"""
a = np.array(np.random.randint(3,3 *100, size=(3,3)))
a.round(a*100)
a.reshape(-1)
print(a)