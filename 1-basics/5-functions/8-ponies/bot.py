def sum_ages_of_friends(Applejack, Rainbowdash, Buttershine):
  total_age = Buttershine + Rainbowdash + Applejack
  print(total_age)
  
def calc_avg_age_of_friends(Applejack, Rainbowdash, Buttershine):
  avg_age = (Buttershine + Rainbowdash + Applejack) / 3
  print(avg_age)

def run():
  print("How old is Applejack?")
  Applejack = int(input())
  print("How old is Rainbowdash?")
  Rainbowdash = int(input())
  print("How old is Buttershine?")
  Buttershine = int(input())
  print("What do you want me to work out?")
  print("1. Sum")
  print("2. Average")
  work_out = int(input())
  if work_out == 1:
    sum_ages_of_friends(Applejack, Rainbowdash, Buttershine)
  elif work_out == 2:
    calc_avg_age_of_friends(Applejack, Rainbowdash, Buttershine)
  else:
    print("Please try again")

run()
