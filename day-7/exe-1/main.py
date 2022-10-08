import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a Letter\n").lower()

for n in chosen_word:
    if n == guess:
        print("Right")
    else:
        print("Wrong")
