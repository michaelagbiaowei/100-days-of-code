height_in_meter = input("Enter your height in meter\n") # 0.3048 meter == 1 foot
weight_in_kg = input("Enter your weight in kg:\n")
value_of_height = float(height_in_meter)
value_of_weight = int(weight_in_kg)

result_of_BMI = round(value_of_weight // (value_of_height * value_of_height), 2)
a = result_of_BMI
# print(int(result_of_BMI))
print(f" Your BMI is: {result_of_BMI}")

if result_of_BMI < 18.5:
    print("You are underweight")
elif result_of_BMI > 18.5 and result_of_BMI < 25:
    print("You have a normal weight")
elif result_of_BMI > 25 and result_of_BMI < 30:
    print("You are overweight")
elif result_of_BMI > 30 and result_of_BMI < 35:
    print("You are obese")
else:
    print("You are clinically obese")
