import numpy as np

number_one = np.array([ _ for _ in range(1,5)])
number_two = np.array([ _ for _ in range(6,10)])

print(f"Number One : {number_one}")
print(f"Number Two : {number_two}")

# adder
adder_number = number_one + number_two
print(f"Adder : {adder_number}")

# substractor
substractor_number = number_one - number_two
print(f"Substractor : {substractor_number}")

# multiplier
multiplier_number = number_one * number_two
print(f"Multiplier : {multiplier_number}")

# divider
divider_number = number_one / number_two
print(f"Divider : {divider_number}")

# power
power_number = number_one ** 2
print(f"Power : {power_number}")

# floor division
floor_number = number_one // 2
print(f"Floor Division : {floor_number}")