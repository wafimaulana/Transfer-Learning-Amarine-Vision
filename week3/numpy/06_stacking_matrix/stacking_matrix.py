import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

aMat = np.zeros((2, 3))
bMat = np.ones((2, 3))

# Stacking arrays (combining arrays)

c = np.hstack((a, b))
d = np.vstack((a, b))

cMat = np.hstack((aMat, bMat))
dMat = np.vstack((aMat, bMat))

print("Array a:", a)
print("Array b:", b)

print("\nResult of Horizontal Stacking (a and b):", c)
print("Result of Vertical Stacking (a and b):\n", d)

print("\nArray aMat:\n", aMat)
print("Array bMat:\n", bMat)

print("\nResult of Horizontal Stacking (aMat and bMat):\n", cMat)
print("Result of Vertical Stacking (aMat and bMat):\n", dMat)