import math

print("What shape do you want to work out the volume for?")
print("1) Cylinder")
print("2) Cone")
shape = float(input())

print("What is the height? (cm)")
height = float(input())

print("What is the radius? (cm)")
radius = float(input())

if shape == 1:
  volume = (math.pi*radius**2*height)
  print("The volume of the Cylinder is", str(round(volume, 2))+"cm2")
elif shape == 2:
  volume = (math.pi*radius**2*height)/3
  print("The volume of the Cone is", str(round(volume, 2))+"cm2")
else:
  print("Please try again...")
