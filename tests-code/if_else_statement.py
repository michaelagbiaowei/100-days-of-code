# # print("Welcome to the rollercoaster height check")
# # height = int(input("What is your height in cm?\n"))

# # if height >= 120:
# #     print("You can ride the rollercoaster")
# # else:
# #     print("Sorry, you have to grow taller before you can ride.")
# #=========================================================================

odd_even = int(input("What number do you want to check?\n"))
if odd_even % 2 == 0:
    print("This is an even number")
else:
    print("This ia an odd number")

# #=======================================================================
# #NESTED IF STATEMENTS AND ELIF STATEMENTS
# print("Welcome to the rollercoaster height check")
# height = int(input("What is your height in cm?\n"))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?\n"))
#     if age <= 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#============================================================================
height_in_meter = input("Enter your height in meter\n")
weight_in_kg = input("Enter your weight in kg:\n")
value_of_height = float(height_in_meter)
value_of_weight = int(weight_in_kg)

result_of_BMI = round(value_of_weight // (value_of_height * value_of_height), 2)
a = result_of_BMI
# print(int(result_of_BMI))
print(f" Your BMI is: {result_of_BMI}")

if result_of_BMI < 18.5:
    print("They are underweight")
elif result_of_BMI > 18.5 and result_of_BMI < 25:
    print("They have a normal weight")
elif result_of_BMI > 25 and result_of_BMI < 30:
    print("They are overweight")
elif result_of_BMI > 30 and result_of_BMI < 35:
    print("They are obese")
else:
    print("They are clinically obese")
#======================================================================
year = int(input("What year do you want to check?\n"))
if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# print(2020 / 4) # must pass
# print(2020 /100) # must fail
# print(2020 / 400) # must fail