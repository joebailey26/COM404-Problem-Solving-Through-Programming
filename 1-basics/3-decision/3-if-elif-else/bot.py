#Read direction from user
print("What direction do you want to move?")
print("1) Forward")
print("2) Backwards")
print("3) Left")
print("4) Right")

direction = int(input())

if direction == 1:
  print("I am moving up")
elif direction == 2:
  print("I am moving down")
elif direction == 3:
  print("I am moving left")
elif direction == 4:
  print("I am moving right")
else:
  print("I don't know which way you are going!")
