print("Welcome to the Python Pizza Deiveries!")
size = input("What size of pizza do you want? S, M, or L\n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N\n").upper()
extra_cheese = input("Do you want extra cheese? Y or N\n").upper()

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_small = 2
pepperoni_large = 3
cheese = 1 

if size == "S" and add_pepperoni == "Y" and extra_cheese =="Y":
    print(f" Your total bill is ${small_pizza + pepperoni_small + cheese}")
elif size == "S" and add_pepperoni == "Y" and extra_cheese =="N":
    print(f"Your total bil is {small_pizza + pepperoni_small}")
elif size == "S" and add_pepperoni == "N" and extra_cheese =="Y":
    print(f"Your total bill is ${small_pizza + cheese}")
elif size == "S" and add_pepperoni == "N" and extra_cheese =="N":
    print(f"Your total bil is {small_pizza}")

elif size == "M" and add_pepperoni == "Y" and extra_cheese =="Y":
    print(f"Your total bill is ${medium_pizza + pepperoni_small + cheese}")
elif size == "M" and add_pepperoni == "Y" and extra_cheese =="N":
    print(f"Your total bill is ${medium_pizza + pepperoni_small + cheese}")
elif size == "M" and add_pepperoni == "N" and extra_cheese =="Y":
    print(f"Your total bill is ${medium_pizza + pepperoni_small + cheese}")
elif size == "M" and add_pepperoni == "N" and extra_cheese =="":
    print(f"Your total bill is ${medium_pizza + pepperoni_small + cheese}")

elif size == "L" and add_pepperoni == "Y" and extra_cheese =="Y":
    print(f"Your total bill is ${large_pizza + pepperoni_small + cheese}")
elif size == "L" and add_pepperoni == "Y" and extra_cheese =="N":
    print(f"Your total bill is ${large_pizza + pepperoni_small + cheese}")
elif size == "L" and add_pepperoni == "N" and extra_cheese =="Y":
    print(f"Your total bill is ${large_pizza + pepperoni_small + cheese}")
else:
    print(f"Your total bill is ${large_pizza}")
