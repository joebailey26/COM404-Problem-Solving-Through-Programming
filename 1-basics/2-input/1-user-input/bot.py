# Read some user input
print("Please type your name")
name = input()
print("Hello", name + ".")
print("Please type your last name")
lname = input()
print("Hello", name, lname + ".")
print("Please type your profession")
prof = input()
print("Hello", name, lname + ".", "You are a", prof + ".")

# Alternatively you can do the following
print("Please type your name")
name = input()
print("Hello ", name, ".", sep="")
print("Please type your last name")
lname = input()
print("Hello ", name, " ", lname, ".", sep="")
print("Please type your profession")
prof = input()
print("Hello ", name, " ", lname, ". ", "You are a ", prof, ".", sep="")

# For fun
print("Please type your name")
name = input()
print("Hello ", name, ".", sep=":)")
