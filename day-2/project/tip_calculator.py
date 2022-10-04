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

print(f"Each person should pay: ${cal_3}")

