import numpy as np

# Matriks koefisien
A = np.array([[8, 1, 7], 
              [2, 4, 3],
              [1, 2, 1]])

# Matriks hasil
B = np.array([56, 20, 10])

# Menyelesaikan SPLTV (bukan SPLDV)
solusi = np.linalg.solve(A, B)
print(solusi)

# menyimpan solusi ke dalam x, y, dan z
x, y, z = solusi

print("x =", x)
print("y =", y)
print("z =", z)
nilai = x**2 - 10**y + z + 2**z
print("Nilai dari x^2 - 10^y + z + 2^z =", nilai)