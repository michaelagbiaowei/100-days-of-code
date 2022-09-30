import random

print("Who's Paying...")
cards = input("Drop Your Cards Here\n")
names = cards.split(", ")
random_choice = random.randint(0, len(names)-1)
output = names[random_choice]
print(f" {output} Is going to pay for the meal today")
