import numpy as np

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9], 
                   [10, 11, 12]])

print("Matrix size: {}".format(matrix.shape))  # output: 4 rows, 3 columns


# Transpose matrix
transpose_matrix = np.transpose(matrix)
print("\nTranspose Matrix:\n{}".format(transpose_matrix))
print("Transpose matrix size: {}".format(transpose_matrix.shape))  # output: 3 rows, 4 columns


# Reshape matrix
reshaped_matrix = np.reshape(matrix, (6, 2))  # change matrix to 6 rows and 2 columns
print("\nReshaped Matrix (6x2):\n{}".format(reshaped_matrix))
print("Reshaped matrix size: {}".format(reshaped_matrix.shape))  # output: 6 rows, 2 columns


# Flatten matrix
flattened_matrix = np.ravel(matrix)  # convert matrix to 1D array
print("\nFlattened Matrix:\n{}".format(flattened_matrix))
print("Flattened matrix size: {}".format(flattened_matrix.shape))  # output: 12 elements in 1 dimension


# Resize matrix
resized_matrix = np.resize(matrix, (6, 2))  # change matrix size to 6 rows and 2 columns
print("\nResized Matrix (6x2):\n{}".format(resized_matrix))
print("Resized matrix size: {}".format(resized_matrix.shape))  # output: 6 rows, 2 columns