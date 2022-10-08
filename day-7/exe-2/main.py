import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# print(chosen_word)

empty_list = []

for n in chosen_word:
    empty_list += "_"
print(empty_list)


guess = input("Guess a Letter\n").lower()

con = list(chosen_word)

repl_chr = "_"
ret_chr = guess
res = [i if i == ret_chr else repl_chr for i in con]

print(res)
