#NUMBER MANIPUATION
print(10 / 3)
print(round(10 / 3))
print(round(10 / 3, 2))
print(3 // 3)

score = 10
score -= 2
score -= 2
print(score)

#F-STRING MANIPULATION
point = 2
height = 1.7
isWinning = True

print(f"Your point is {point}\nYour height is {height}\nisWinning: {isWinning}")


inputAge = input("What is your current age?\n")
age = int(inputAge)
year = 90 - age
day = year * 365
week = year * 52
months = year * 12

print(f"You have\n{day} days\n{week} weeks\n{months} months\nand {year} years left")

print("Welcome to the tip calculator")
input_total_bill = input("What was the total bill?\n")
bill = float(input_total_bill)
input_percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
percentage_tip = int(input_percentage_tip)
input_split_bill = input("How many people are to split the bill?\n")
spilt_bill = int(input_split_bill)

cal_1 = ((percentage_tip / 100) * bill)
cal_2 = (cal_1 + bill)
cal_3 = (round(cal_2 / spilt_bill, 2))

print(f"Each person should pay: {cal_3}")
