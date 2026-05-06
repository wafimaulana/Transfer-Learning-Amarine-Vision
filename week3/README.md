# Week 3 — NumPy & Matplotlib: Fondasi Analisis Data untuk Computer Vision

## 1. Latar Belakang

Sebelum memasuki dunia **Computer Vision** secara penuh, terdapat dua library fundamental yang wajib dikuasai:

* **NumPy** — untuk manipulasi array dan komputasi numerik secara efisien
* **Matplotlib** — untuk visualisasi data dan hasil analisis

Kedua library ini menjadi tulang punggung hampir seluruh ekosistem machine learning dan computer vision di Python. Pemahaman mendalam terhadap keduanya akan sangat membantu saat bekerja dengan dataset gambar, operasi matriks (seperti konvolusi), dan interpretasi hasil model.

---

## 2. Tujuan Pembelajaran

Setelah menyelesaikan Week 3, diharapkan mampu:

* Membuat, memanipulasi, dan melakukan operasi matematis pada array NumPy
* Memahami indexing, slicing, dan iterasi pada array multidimensi
* Melakukan operasi linear algebra seperti perkalian matriks, invers, dan determinan
* Membuat berbagai jenis visualisasi menggunakan Matplotlib
* Mengatur properti grafik seperti axis, label, title, teks, ticks, dan spines
* Mengombinasikan NumPy dan Matplotlib untuk analisis data visual

---

## 3. Struktur Repositori

```
week3/
├── README.md                          # Dokumentasi Week 3 (file ini)
│
├── numpy/                             # Materi NumPy
│   ├── 01_numpy_array/
│   │   └── numpy_array.py             # Pembuatan dan dasar array NumPy
│   ├── 02_aritmatika/
│   │   └── aritmatika.py              # Operasi aritmatika pada array
│   ├── 03_index_slicing_iterasi/
│   │   └── index_slicing.py           # Indexing, slicing, dan iterasi
│   ├── 04_perkalian_matrix/
│   │   └── perkalian_matrix.py        # Perkalian matriks (dot product)
│   ├── 05_manipulasi_matrix/
│   │   └── manipulasi_matrix.py       # Reshape, transpose, flatten
│   ├── 06_stacking_matrix/
│   │   └── stacking_matrix.py         # Hstack, vstack, concatenate
│   ├── 07_advance_array_create/
│   │   └── advance_array.py           # zeros, ones, linspace, arange, random
│   ├── 08_ordering/
│   │   └── ordering.py                # Sort, argsort, dan pengurutan array
│   ├── 09_perkalian_vektor/
│   │   └── perkalian_vektor.py        # Operasi vektor: dot, cross, norm
│   ├── 10_invers_determinan/
│   │   └── invers_determinan.py       # Invers matriks dan determinan
│   └── 11_persamaan_linear/
│       └── persamaan_linear.py        # Penyelesaian sistem persamaan linear
│
├── Matplotlib/                        # Materi Matplotlib
│   ├── 01_introduction_pyplot/
│   │   └── introduction_pyploy.py     # Pengenalan pyplot dan plot dasar
│   ├── 02_set_properti/
│   │   └── set_properti.py            # Warna, style, linewidth, marker
│   ├── 03_set_axis/
│   │   └── set_axis.py                # Pengaturan sumbu x dan y
│   ├── 04_label_title/
│   │   └── label_title.py             # Menambahkan label dan judul grafik
│   ├── 05_teks/
│   │   └── teks.py                    # Menambahkan teks dan anotasi
│   └── 06_ticks_spines/
│       └── teks.py                    # Kustomisasi ticks dan spines
│
└── numpy_matplotlib.ipynb             # Notebook ringkasan gabungan NumPy + Matplotlib
```

---

## 4. Materi NumPy

### 4.1 Numpy Array

NumPy array adalah struktur data utama dalam NumPy, jauh lebih efisien dibanding Python list biasa untuk operasi numerik.

```python
import numpy as np

# Membuat array 1D
a = np.array([1, 2, 3, 4, 5])

# Membuat array 2D (matriks)
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.shape)   # (5,)
print(b.shape)   # (2, 3)
print(b.dtype)   # int64
```

---

### 4.2 Operasi Aritmatika

NumPy mendukung operasi element-wise secara langsung tanpa perlu loop.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]
print(a ** 2)  # [1 4 9]
print(np.sqrt(a))  # [1. 1.41 1.73]
```

---

### 4.3 Indexing, Slicing & Iterasi

```python
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[0, 1])     # 20  → baris 0, kolom 1
print(arr[:, 1])     # [20 50 80] → semua baris, kolom 1
print(arr[1:, :2])   # [[40 50], [70 80]]

# Iterasi
for row in arr:
    print(row)
```

---

### 4.4 Perkalian Matriks

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Dot product (perkalian matriks sejati)
C = np.dot(A, B)
# atau: C = A @ B
print(C)
# [[19 22]
#  [43 50]]
```

---

### 4.5 Manipulasi Matriks

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.reshape(3, 2))  # Ubah bentuk menjadi 3x2
print(arr.T)              # Transpose
print(arr.flatten())      # Ubah menjadi array 1D
```

---

### 4.6 Stacking Matriks

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack([a, b]))          # [1 2 3 4 5 6]
print(np.vstack([a, b]))          # [[1 2 3], [4 5 6]]
print(np.concatenate([a, b]))     # [1 2 3 4 5 6]
```

---

### 4.7 Advanced Array Creation

```python
print(np.zeros((3, 3)))           # Matriks 0
print(np.ones((2, 4)))            # Matriks 1
print(np.eye(3))                  # Matriks identitas
print(np.linspace(0, 1, 5))      # [0. 0.25 0.5 0.75 1.]
print(np.arange(0, 10, 2))       # [0 2 4 6 8]
print(np.random.rand(3, 3))      # Matriks random 0–1
```

---

### 4.8 Ordering / Pengurutan

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2])

print(np.sort(arr))           # [1 1 2 3 4 5 9]
print(np.argsort(arr))        # Indeks pengurutan
print(arr[np.argsort(arr)])   # Sama dengan sort
```

---

### 4.9 Perkalian Vektor

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))        # 32 → dot product
print(np.cross(a, b))      # Cross product
print(np.linalg.norm(a))   # Panjang/magnitude vektor
```

---

### 4.10 Invers & Determinan

```python
A = np.array([[2, 1],
              [5, 3]])

print(np.linalg.det(A))    # Determinan: 1.0
print(np.linalg.inv(A))    # Matriks invers
```

---

### 4.11 Sistem Persamaan Linear

```python
# Menyelesaikan: 2x + y = 5, 5x + 3y = 14
A = np.array([[2, 1],
              [5, 3]])
b = np.array([5, 14])

x = np.linalg.solve(A, b)
print(x)  # [1. 3.] → x=1, y=3
```

---

## 5. Materi Matplotlib

### 5.1 Pengenalan Pyplot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

---

### 5.2 Set Properti Grafik

```python
plt.plot(x, y,
         color='royalblue',
         linewidth=2,
         linestyle='--',
         marker='o',
         markersize=5,
         label='sin(x)')

plt.legend()
plt.show()
```

---

### 5.3 Set Axis

```python
plt.plot(x, y)
plt.xlim(0, 2 * np.pi)
plt.ylim(-1.5, 1.5)
plt.axis('equal')   # Skala x dan y sama
plt.show()
```

---

### 5.4 Label & Title

```python
plt.plot(x, y)
plt.xlabel('Sudut (radian)', fontsize=12)
plt.ylabel('Nilai', fontsize=12)
plt.title('Grafik Fungsi Sinus', fontsize=14, fontweight='bold')
plt.show()
```

---

### 5.5 Teks & Anotasi

```python
plt.plot(x, y)

# Menambahkan teks di koordinat tertentu
plt.text(np.pi, 0, 'π', fontsize=14, color='red')

# Anotasi dengan panah
plt.annotate('puncak', xy=(np.pi/2, 1), xytext=(2, 0.8),
             arrowprops=dict(arrowstyle='->'))
plt.show()
```

---

### 5.6 Ticks & Spines

```python
fig, ax = plt.subplots()
ax.plot(x, y)

# Kustomisasi ticks
ax.set_xticks([0, np.pi, 2 * np.pi])
ax.set_xticklabels(['0', 'π', '2π'])

# Kustomisasi spines (bingkai grafik)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('gray')

plt.show()
```

---

## 6. Notebook Gabungan

File `numpy_matplotlib.ipynb` merupakan notebook lengkap yang menggabungkan seluruh materi NumPy dan Matplotlib dalam satu dokumen interaktif. Notebook ini mencakup:

* Contoh kode untuk setiap topik
* Penjelasan dan komentar dalam bahasa Indonesia
* Output visual langsung dari setiap cell
* Studi kasus sederhana yang mengombinasikan kedua library

Untuk membuka notebook:

```bash
# Aktifkan environment terlebih dahulu
conda activate TL-Amarine-Vision

# Buka Jupyter
jupyter notebook numpy_matplotlib.ipynb
```

---

## 7. Cara Menjalankan File Python

Pastikan environment sudah aktif dan library sudah terinstall:

```bash
conda activate TL-Amarine-Vision
pip install numpy matplotlib
```

Jalankan file individual:

```bash
# Contoh menjalankan salah satu file
python week3/numpy/01_numpy_array/numpy_array.py
python week3/Matplotlib/01_introduction_pyplot/introduction_pyploy.py
```

---

## 8. Referensi

* [NumPy Official Documentation](https://numpy.org/doc/)
* [Matplotlib Official Documentation](https://matplotlib.org/stable/contents.html)
* [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
* [Matplotlib Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
* [Scientific Python Lectures](https://lectures.scientific-python.org/)

---

## 9. Navigasi

| Navigasi       | Link                              |
| -------------- | --------------------------------- |
| ⬅ Kembali     | [Week 2](../week2/README.md)      |
| 🏠 Utama       | [README Utama](../README.md)      |
| ➡ Lanjut      | Week 4 (Coming Soon)              |

---

> **Catatan:** Seluruh kode dalam Week 3 ditulis menggunakan Python 3.10 di dalam environment `TL-Amarine-Vision`. Pastikan environment aktif sebelum menjalankan file apapun.
