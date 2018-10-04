print("Where should I look?")
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
