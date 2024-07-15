import math

constant = math.log10(0.5)

base = input("Enter base (in Integers):")
height = input("Enter height (in Integers):")

area = int(constant) * int(base) * int(height) 

print("The area is:" + str(area))