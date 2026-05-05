import numpy as np
import random

matrix_a = np.array([[random.randint(1, 3) for _ in range(2)] for _ in range(2)])
matrix_b = np.array([[random.randint(1, 3) for _ in range(2)] for _ in range(2)])

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# Perform matrix multiplication
c1 = matrix_a.dot(matrix_b)

c2 = np.dot(matrix_a, matrix_b)

is_equal = np.array_equal(c1, c2)

print(f"\nResult of matrix multiplication A and B (method 1):\n{c1}")
print(f"\nResult of matrix multiplication A and B (method 2):\n{c2}")
print(f"\nDo both methods produce the same array? {is_equal}")