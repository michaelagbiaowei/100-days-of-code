import random
# import my_module
# print(my_module.num)
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# dice_toss = random.randint(0, 1)
# if dice_toss == 0:
#     print("Tails")
# else:
#     print("Heads")

# lists_of_names = ["kdjshkjd", "bdjs", "jsjdg"]
# lists_of_names.append("hgaj") # add to the end of the list
# lists_of_names.extend(["jhgsjh", "shhsd", "shaj"])
# print(lists_of_names)

cards = input("Drop Your Cards Here\n")
split_cards = cards.split(", ")
randome_choice = random.choice(split_cards)
print(randome_choice)