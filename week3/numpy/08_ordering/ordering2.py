import numpy as np

dtype = [('nama', 'U10'), ('umur', int), ('ipk', float)]

data = [('Budi', 20, 3.5), ('Andi', 21, 3.8), ('Citra', 19, 3.9)]

arr = np.array(data, dtype=dtype)
print(arr)

print("========================================================")
print("Sorting berdasarkan umur")
print(np.sort(arr, order='umur'))