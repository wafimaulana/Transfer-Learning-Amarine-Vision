from numpy import iterable
import numpy as np

# Create Matrix with data type specialiy
float_matrix = np.array(([ _ for _ in range(1,6)], [ _ for _ in range(1,6)]), dtype = float)
print(f"Output of floating matrix :\n {float_matrix}")

# matrix[x,y] : x is row, y is column

# Create array with function
def quadratic(row, column):
    return column**2

output_float_matrix = quadratic(float_matrix[0], float_matrix[1])
print(f"\nOutput of quadratic function :\n {output_float_matrix}")

# Create array with numpy fromfunction (like for each cell run function)
output_matrix_with_fromfunction = np.fromfunction(quadratic, (2,5), dtype=int)
print(f"\nOutput of fromfunction :\n {output_matrix_with_fromfunction}")

# create array ir matrix with use iterable
iterable = (x*2 for x in range(1,6))
output_matrix_with_iterable = np.fromiter(iterable, dtype=int)
print(f"\nOutput of iterable :\n {output_matrix_with_iterable}")

# multitype aray

data = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15),
]

multi_type_array = np.array(data)
print(f"\nOutput of multi type array :\n {multi_type_array}")
