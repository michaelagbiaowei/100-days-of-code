# #PEMDAS
# parentheses = ()
# exponents = 3 ** 3
# multiplication = 3 * 3
# division = 3 /3
# addition = 3 + 3
# subtraction = 3 -3

#multiplicaton, division, addition, and subtraction are on thesame level of priority

weight_in_kg = input("Enter your weight in kg:\n")
height_in_meter = input("Enter your heightin meter\n")

value_of_weight = int(weight_in_kg)
value_of_height = float(height_in_meter)

result_of_BMI = (value_of_weight / (value_of_height * value_of_height))

print(int(result_of_BMI))
print(round(result_of_BMI))

