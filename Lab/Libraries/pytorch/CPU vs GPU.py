import numpy as np
import torch as t
import time 

size = 10000

matrix1 = t.rand(size, size)
matrix2 = t.rand(size, size)

# measuring the time here 
start_time = time.time()
result = t.matmul(matrix1, matrix2)
cpu_time = time.time() - start_time

print(f"CPU time: {cpu_time:.6f} seconds")

Matrix_gpu_1 = matrix1.to('cuda')
Matrix_gpu_2 = matrix2.to('cuda')

start_time = time.time()
result = t.matmul(Matrix_gpu_1, Matrix_gpu_2)
gpu_time = time.time() - start_time

print(f"GPU time: {gpu_time:.6f} seconds")

# comparing results 

print(f"Speedup: {cpu_time / gpu_time:.2f}x faster on GPU")