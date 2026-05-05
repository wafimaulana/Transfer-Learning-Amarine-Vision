import numpy as np

multidimensi_number_one = np.array([[1,2],[3,4],[5,6]])
multidimensi_number_two = np.array([[7,8],[9,10],[11,12]])

print(f"Array multidimensi number one : \n{multidimensi_number_one}")
print(f"Array multidimensi number two : \n{multidimensi_number_two}")

# adder
adder_multidimensi = multidimensi_number_one + multidimensi_number_two
print(f"Adder multidimensi : \n{adder_multidimensi}")

# substractor
substractor_multidimensi = multidimensi_number_one - multidimensi_number_two
print(f"Substractor multidimensi : \n{substractor_multidimensi}")

# multiplier
multiplier_multidimensi = multidimensi_number_one * multidimensi_number_two
print(f"Multiplier multidimensi : \n{multiplier_multidimensi}")

# divider
divider_multidimensi = multidimensi_number_one / multidimensi_number_two
print(f"Divider multidimensi : \n{divider_multidimensi}")

# power
power_multidimensi = multidimensi_number_one ** 2
print(f"Power multidimensi : \n{power_multidimensi}")

# floor division
floor_multidimensi = multidimensi_number_one // 2
print(f"Floor division multidimensi : \n{floor_multidimensi}")