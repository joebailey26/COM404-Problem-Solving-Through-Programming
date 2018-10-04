print("Please enter the first number")
first_number = int(input())

print("Please enter the second number")
second_number = int(input())

print("Please enter the third number")
third_number = int(input())

even = 0
odd = 0

if (first_number % 2 == 0):
  even = even + 1
else:
  odd = odd + 1

if (second_number % 2 == 0):
  even = even + 1
else:
  odd = odd + 1

if (third_number % 2 == 0):
  even = even + 1
else:
  odd = odd + 1

print("There were", even, "even numbers and", odd, "odd numbers")
