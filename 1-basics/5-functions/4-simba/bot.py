def roar(num_roars):
  print("Simba says:")
  for count in range(0, num_roars, 1):
    print("Roar!")
  if num_roars < 3:
    print("Cough! Cough!  \n")
  else:
    print("ROAR!!!")
  
# The following are calls to the function for testing purposes
roar(1)
roar(3)
