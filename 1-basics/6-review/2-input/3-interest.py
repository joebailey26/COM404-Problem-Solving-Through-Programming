#Read current amount from user
print("How much money do you have? (£)")
total = float(input())

#Read interest rate from user
print("What is your interest rate? (%)")
interest = float(input())

#Calculate total after interest
total_interest = total + (total*(interest/100))

#Print total after interest
print("Total after interest is", round(float(total_interest), 2))
