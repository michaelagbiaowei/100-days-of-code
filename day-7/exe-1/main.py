import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a Letter\n").lower()

if guess in chosen_word:
    print("correct")
else:
    ("wrong")
