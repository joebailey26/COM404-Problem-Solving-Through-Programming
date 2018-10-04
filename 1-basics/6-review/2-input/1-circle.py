import math
print("Please enter radius")
radius = float(input())
area = math.pi*(radius**2)
circumference = 2*math.pi*radius
print("Area is", round(area, 2))
print("Circumference is", round(circumference, 2))
