import numpy as np

# Matriks koefisien
A = np.array([[3, 2, 1], 
              [1, 4, 2],
              [2, 1, 3]])

# Matriks hasil
B = np.array([50, 60, 55])

# Menyelesaikan SPLTV (bukan SPLDV)
solusi = np.linalg.solve(A, B)
print(solusi)

# menyimpan solusi ke dalam x, y, dan z
x, y, z = solusi

print(f"Berat Sensor A (RGB Camera)      = {x} gram")
print(f"Berat Sensor B (Depth Sensor)    = {y} gram")
print(f"Berat Sensor C (IMU)             = {z} gram")
nilai = x**2 - 10**y + z + 2**z
print(f"Nilai dari x^2 - 10^y + z + 2^z = {nilai}")