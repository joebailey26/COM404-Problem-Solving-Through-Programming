print("How many times would you like the robot printed?")

num_prints = int(input())

if num_prints > 10:
  num_prints = 10

for count in range(0,num_prints, 1):
  print(""" 
    (0 | 0)
       O 
      -O- 
       O 
      ! !
  """)
