print("Welcome to the rollercoaster height check")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is pay $7")
    else:
        bill= 12
        print("Adult ticket is $12")

    wants_photo = input("Do you want a photo taken? Y or N\n").lower()
    if wants_photo == "Y":
            # bill = bill + 3
        bill += 3
        print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

#====================================================================================
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
#===========================================================================================

print("Welcome to the love calculator")
name_1 = input("What is your name?\n")
name_2 = input("What is their name?\n")

lower_case_1 = name_1.lower()
count_t = lower_case_1.count("t")
count_r = lower_case_1.count("r")
count_u = lower_case_1.count("u")
count_e = lower_case_1.count("e")

lower_case_2 = name_2.lower()
count_l = lower_case_2.count("l")
count_o = lower_case_2.count("o")
count_v = lower_case_2.count("v")
count_ee = lower_case_2.count("e")

count_1 = (count_t + count_r + count_u + count_e)
count_2 = (count_l + count_o + count_v + count_ee)

total_counts = int(f"{count_1}{count_2}")
# # print(total_counts)

if total_counts < 10 or total_counts > 90:
    print(f"You are {total_counts}% matched\nYou go together like coke and mentos")
elif total_counts > 40 and total_counts < 50:
    print(f"You are {total_counts}% matched\nYou are alright together")
else:
    print(f"Your percentage is {total_counts}%\nYou are undefined!")

#===================================================================================

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island\nYour mission is to find the Treasure.")
stage_1 = input("You are in a cross road. Where do you want to go?\nType 'left' or 'right'\n").lower()
if stage_1 == "left":
    lake = input("You have come to a lake.\nThere is an Island in the midlle of the lake.\nType 'wait' to wait for a boat\nType 'swim' to swim across.\n").lower()
    if lake == "wait":
        arrive = input("You have arrive at the Island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and blue. Which color do you choose?\n").lower()
        if arrive == "yellow":
            print("You have found the Treasure!!!")
        else:
            print("You lose! Game Over")
    else:
        print("You lose! Game Over")
else:
    print("You lose! Game Over")           