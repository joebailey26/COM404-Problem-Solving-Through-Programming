def run():
  print("Please enter a character to display...")
  character = str(input())
  print("Please enter total number of characters...")
  total = int(input())
  print("Please enter a whole number...")
  num = int(input())
  for count in range(1, total+1, 1):
    if count % num == 0:
      print(character, end="")
    else:
      print("-", end="")
 
#Run the program
run()
