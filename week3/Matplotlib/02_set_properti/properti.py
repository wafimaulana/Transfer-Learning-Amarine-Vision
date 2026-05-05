import numpy as np
import matplotlib.pyplot as plt

"""
    1. Membuat data
    2. Membuat plot
    3. Menampilkan plot
"""

# Mengimplementasikan sinus dan cosinus grafik
#1. Sinus : f(x) = asin(kx + b) + c
#2. Cosinus : f(x) = acos(kx + b) + c

def sinus(a, k, b, c, x):
    return a * np.sin(k * x + b) + c

def cosinus(a, k, b, c, x):
    return a * np.cos(k * x + b) + c

x = np.arange(0, 10, 0.1)
y_sin = sinus(a=2, k=1, b=0, c=0, x=x)
y_cos = cosinus(a=2, k=1, b=0, c=0, x=x)

plt.grid()
plt.plot(x, y_sin, color="red", marker=".", linestyle="--")
plt.plot(x, y_cos, color="blue", marker="s" )
plt.legend()
plt.show()

