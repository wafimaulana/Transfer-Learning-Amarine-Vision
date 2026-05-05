import numpy as np
import matplotlib.pyplot as plt

"""
    1. Membuat data
    2. Membuat plot
    3. Menampilkan plot
"""

# Fungsi Sinus & Cosinus
# f(x) = a sin(kx + b) + c
# f(x) = a cos(kx + b) + c
def sinus(a, k, b, c, x):
    return a * np.sin(k * x + b) + c

def cosinus(a, k, b, c, x):
    return a * np.cos(k * x + b) + c


# Membuat Data (HALUS)
x = np.linspace(0, 360, 1000)   
y_sin = sinus(a=2, k=np.pi/180, b=0, c=0, x=x)
y_cos = cosinus(a=2, k=np.pi/180, b=0, c=0, x=x)


# Membuat Plot
plt.figure(figsize=(9, 5))

plt.plot(
    x, y_sin,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Sinus"
)

plt.plot(
    x, y_cos,
    color="blue",
    linestyle="-",
    linewidth=2,
    label="Cosinus"
)


# Axis & Spines
plt.axis([0, 360, -3, 3])
ax = plt.gca()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.spines['left'].set_color('#444444')
ax.spines['bottom'].set_color('#444444')


# Ticks
ax.tick_params(
    axis='both',
    which='major',
    direction='in',
    length=6,
    width=1.2,
    colors='#333333',
    labelsize=12
)

ax.tick_params(
    axis='both',
    which='minor',
    direction='in',
    length=3,
    width=1,
    colors='#666666'
)

ax.minorticks_on()

plt.yticks([-2, -1, 0, 1, 2])
plt.xticks(
    [0, 90, 180, 270, 360],
    [r'${0}^\circ$', r'${90}^\circ$', r'${180}^\circ$', r'${270}^\circ$', r'${360}^\circ$']
)


# Grid
ax.grid(True, which='major', linestyle='--', linewidth=0.6, alpha=0.6)
ax.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.4)



# Judul & Label
judul = "Grafik Sinus dan Cosinus"
rumus = r"$f(x) = a \sin(kx + b) + c$ dan $f(x) = a \cos(kx + b) + c$"

plt.title(judul + "\n" + rumus, fontsize=16, pad=20)
plt.xlabel("Sumbu X (Derajat)", fontsize=14, color="purple", labelpad=15)
plt.ylabel("Sumbu Y", fontsize=14, color="purple", labelpad=15)

plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
