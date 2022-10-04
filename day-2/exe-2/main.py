weight_in_kg = input("Enter your weight in kg:\n")
height_in_meter = input("Enter your height in meter\n") # 0.3048 meter == 1 foot

value_of_weight = int(weight_in_kg)
value_of_height = float(height_in_meter) 

result_of_BMI = (value_of_weight / (value_of_height * value_of_height))

round_num = round(result_of_BMI)
print(f"Your BMI is {round_num}")
