import numpy as np

number = np.floor(np.random.rand(2,5)*10)
print(number)

print("Value max from number = ", number.max())
print("Value min from number = ", number.min())
print("Value position of max from number = ", number.argmax())
print("Value position of min from number = ", number.argmin())

print("========================================================")
print("Sorting value number = ", np.sort(number))
print("Sorting value position number = ", np.argsort(number))