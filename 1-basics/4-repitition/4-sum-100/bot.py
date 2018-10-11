print("The sum of the first 100 numbers is")

numbers = sum(range(0,101))

print(numbers)

#alternate method 

count = 0
sum_result = 0

for count in range (0,101,1):
  sum_result = count +sum_result

print("The sum of the first 100 numbers is:", sum_result)
