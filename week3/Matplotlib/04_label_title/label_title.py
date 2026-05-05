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


# Membuat Data
def sinus(a, k, b, c, x):
    return a * np.sin(k * x + b) + c

def cosinus(a, k, b, c, x):
    return a * np.cos(k * x + b) + c


# Membuat Plot
x = np.arange(0, 10, 0.1)
y_sin = sinus(a=2, k=1, b=0, c=0, x=x)
y_cos = cosinus(a=2, k=1, b=0, c=0, x=x)
plt.plot(x, y_sin, color="red", marker=".", label="Sinus", linestyle="--")
plt.plot(x, y_cos, color="blue", marker="s", label="Cosinus")



# Menampilkan Plot
judul = "Grafik Sinus dan Cosinus" 
rumus = r"$f(x) = a \sin(kx + b) + c$ dan $f(x) = a \cos(kx + b) + c$"



plt.grid()
plt.axis([0, 10, -2, 2]) 
plt.xticks([0, 2, 4, 6, 8, 10])
plt.title(judul + "\n" + rumus, fontsize=16, pad=20)
plt.xlabel("Sumbu X", fontsize=14, color="purple", labelpad=15)
plt.ylabel("Sumbu Y", fontsize=14, color="purple", labelpad=15)
plt.legend(loc="upper right", fontsize=12, shadow=True, borderpad=1)
plt.show()

