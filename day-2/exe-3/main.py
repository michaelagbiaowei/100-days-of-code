inputAge = input("What is your current age?\n")
age = int(inputAge)
year = 90 - age
day = year * 365
week = year * 52
months = year * 12

print(f"You have\n{day} days\n{week} weeks\n{months} months\nand {year} years left")
