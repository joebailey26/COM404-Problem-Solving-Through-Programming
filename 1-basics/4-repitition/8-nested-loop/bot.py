print("How many rows would you like?")
rows = int(input())

print("How many columns would you like?")
columns = int(input())

for count in range(0, rows, 1):
    for count in range(0, columns, 1):
        print(":-)", end="")
    print()
