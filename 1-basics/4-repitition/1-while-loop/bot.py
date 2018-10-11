print("How many times would you like the robot printed?")

num_prints = int(input())
MAX_ROBOTS = 10
count = 0

if num_prints < MAX_ROBOTS:
  while(count < num_prints):
    print(""" 
    (0 | 0)
       O 
      -O- 
       O 
      ! !
    """)
    count = count + 1
else:
  while(count < MAX_ROBOTS):
    print(""" 
    (0 | 0)
       O 
      -O- 
       O 
      ! !
    """)
    count = count + 1
