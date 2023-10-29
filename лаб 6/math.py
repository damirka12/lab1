import math

# Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904

deg=float(input())
rad=deg*(math.pi/180)
print(rad)

# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

a=float(input())
b=float(input())
h=float(input())
S=(a+b)/2*h
print (S)

# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

sides=float(input())
l=float(input())
S=(sides*pow(l,2))/(4*math.tan(math.pi/sides))
print(S)

# Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

l=float(input())
h=float(input())
S=l*h
print (S)