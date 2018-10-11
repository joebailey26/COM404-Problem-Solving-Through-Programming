import math
print("I will work out the factorial of your number.")
print("What is your number?")
number = int(input())
factorial = math.factorial(number)
print(factorial)

#alternate method

print("What is your number?")
n = int(input())
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
      
print ("The factorial of", n, "is: ",end="") 
print (fact) 
