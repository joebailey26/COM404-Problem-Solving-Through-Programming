DAYS_IN_YEAR = 365.25

#Read age from user
print("How many years old are you?")
age_years = int(input())

#Calculate age in years
age_days = age_years * DAYS_IN_YEAR

#Display result
print("You are", round(age_days, 2), "days old.")
