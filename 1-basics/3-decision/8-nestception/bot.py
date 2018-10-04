print("Where should I look for the battery?")
print("1) The Bedroom")
print("2) The Bathroom")
print("3) The Lab")
print("4) Somewhere else")

choice_one = int(input())

if choice_one == 1:
  print("Where should I look?")
  print("1) Under the bed")
  print("2) Somewhere else")
  choice_two = int(input())  
  if choice_two == 1:
    print("Found some socks but no battery")
  elif choice_two == 2:
    print("Found some mess but no battery")
  else:
    print("There's nothing here")
elif choice_one == 2:
  print("Where should I look?")
  print("1) In the sink")
  print("2) In the bath")
  choice_two = int(input())  
  if choice_two == 1:
    print("Found some hairs but no battery")
  elif choice_two == 2:
    print("Found some water but no battery")
  else:
    print("There's nothing here")
elif choice_one == 3:
  print("Where should I look?")
  print("1) On the desk")
  print("2) In the cupboard")
  choice_two = int(input())  
  if choice_two == 1:
    print("Found some bottles but no battery")
  elif choice_two == 2:
    print("Found the battery!")
  else:
    print("There's nothing here")
else:
  print("There's nothing here")
