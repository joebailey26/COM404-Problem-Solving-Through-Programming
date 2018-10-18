def one(word):
  print("*" * (len(word) + 10))
  print("*", word, "*")
  print("*" * (len(word) + 10))

def two(word):
  print(word.lower())

def three(word):
  print(word.upper())

def four(word):
  print(word, "|", word[::-1])

def five(word):
  print("How many times do you want me to display the word?")
  count = int(input())
  for count in range(0,count, 1):
    if count % 2  == 0:
      print (word.upper())
    else:
      print (word.lower())
    count = count - 1

def run():
  print("Please enter a word")
  word = str(input())
  print("What do you want me to do?")
  print("1) Display in a Box")
  print("2) Display Lower-case")
  print("3) Display Upper-case")
  print("4) Display Mirrored")
  print("5) Repeat")
  option = int(input())
  if option == 1:
    one(word)
  elif option == 2:
    two(word)
  elif option == 3:
    three(word)
  elif option == 4:
    four(word)
  elif option == 5:
    five(word)
  else:
    print("Please try again")

run()
