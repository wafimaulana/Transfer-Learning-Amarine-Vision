import numpy as np

matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
matrix_b = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# perkailian dot
dot_product = np.dot(matrix_a, matrix_b)
print("Dot Product:\n", dot_product)

# perkalian cross
cross_product = np.cross(matrix_a, matrix_b)
print("Cross Product:\n", cross_product)