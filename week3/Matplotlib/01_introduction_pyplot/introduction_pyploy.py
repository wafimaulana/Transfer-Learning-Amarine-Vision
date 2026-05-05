"""
    Penggunaan matplotlib dibagi menjadi 3 bagian utama, yaitu:
    1. Membuat data
    2. Membuat plot
    3. Menampilkan plot
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Membuat data
x = np.arange(0, 10)
y = np.arange(10, 0, -1)
y2 = x**2

print(x)
print(y)

# 2. Membuat plot
plt.grid()
plt.plot(x, y)
plt.plot(x, y2)
plt.show()

# 3. Menampilkan plot
plt.plot(x, y)
plt.show()