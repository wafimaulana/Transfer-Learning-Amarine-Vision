import numpy as np

# 1. Create Vector
# a. Vector 1-D
oneDimension_int = np.array([0,1,2,3,4])
oneDimension_float = np.array([0,2.3,10,2])
oneDimension_mix = np.array(["Sharleen",12,0.12])
print(f"Create 1-D Vector {oneDimension_int} type : {oneDimension_int.dtype}")
print(f"Create 1-D Vector {oneDimension_float} type : {oneDimension_float.dtype}")
print(f"Create 1-D Vector {oneDimension_mix} type : {oneDimension_mix.dtype}")
# b. Vector 2-D (Matriks)
twoDimension_int = np.array([[1,2],
                            [3,4],
                            [5,6]])
twoDimension_float = np.array([[1.1,2],[3.3,4],[5.2,6]])
twoDimension_mix = np.array([["Sharleen",12],[13,0.12]])
print(f"Create 2-D Vector {twoDimension_int} type : {twoDimension_int.dtype}")
print(f"Create 2-D Vector {twoDimension_float} type : {twoDimension_float.dtype}")
print(f"Create 2-D Vector {twoDimension_mix} type : {twoDimension_mix.dtype}")

# 2. Attribute of numpy
print(f"Shape of Numpy : {twoDimension_int.shape}") # (3,2) -> 3 rows, 2 columns
print(f"Dimension of Numpy : {twoDimension_int.ndim}")
print(f"Datatype of Numpy : {twoDimension_mix.dtype}")
print(f"Total Elements of Numpy : {twoDimension_mix.size}")
print(f"Size of each element : {twoDimension_mix.itemsize} bytes")

# 3. Create Vector with range
range_numpy = np.arange(1,10, 2.5) # start, end (exclusive), step
print(f"Create Vector with range : {range_numpy}")

# 3. Create vector with linspace(evenly spaced values)
linspace_numpy = np.linspace(1,10,5) # start, end (inclusive), number of elements
print(f"Create Vector with linspace : {linspace_numpy}")

# 4. Array multidimensi/matrix
matrix_numpy = np.array([[i for i in range(1, 4)], [i for i in range(1,4)], [i for i in range(1,4)]])
print(f"Create Matrix with list comprehension (3-Dimension) : {matrix_numpy}")

# 5. Array with zeroes and ones
zero_numpy = np.zeros((3,2)) # shape (rows, columns)
ones_numpy = np.ones((3,2)) # shape (rows, columns)
print(f"Create Array with zeroes : {zero_numpy}")
print(f"Create Array with ones : {ones_numpy}")

# 6. Matrix identity
numpy_identity = np.identity(3) # numpy identity just have one param
numpy_eye = np.eye(3,4) # numpy eye have two param (rows, columns)
print(f"Create Matrix Identity : {numpy_identity}")
print(f"Create Matrix Eye : {numpy_eye}")

