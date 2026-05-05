import numpy as np
import random 

# Create a 5x5 matrix so all indices are valid
number = np.array([[random.randint(1,10) for _ in range(5)] for _ in range(5)])

print(f"Number:\n{number}")
print("=========================================================================")

# number[x, y] = x is row, y is column

# 1. Collect single values
print(f"Element at (row 0, col 1): {number[0,1]}") 
print(f"Last element (last row, last col): {number[-1,-1]}")

print("=========================================================================")

# 2. Collect multiple values (column slicing)
print(f"Rows 1 to 3 in column 0      : {number[1:4, 0]}")
print(f"Rows start to 2 in column 0  : {number[:3, 0]}")
print(f"Rows 3 to end in column 0    : {number[3:, 0]}")
print(f"Rows 3 to 0 (reverse) col 0  : {number[3::-1, 0]}")

print("=========================================================================")

# 3. Collect multiple values (row slicing)
print(f"Cols 1 to 2 in row 1         : {number[1, 1:3]}")
print(f"Cols start to 2 in row 1     : {number[1, :3]}")
print(f"Cols 3 to end in row 1       : {number[1, 3:]}")
print(f"Cols 3 to 0 (reverse) row 1  : {number[1, 3::-1]}")

print("=========================================================================")