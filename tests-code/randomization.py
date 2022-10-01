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


# initializing list
# test_list = [1, 4, 5, 2, 7]

# # printing original list
# print("Original list is : " + str(test_list))

# # using random.randint() to
# # get a random number
# rand_idx = random.randint(0, len(test_list)-1)
# random_num = test_list[rand_idx]

# # printing random number
# print("Random selected number is : " + str(random_num))

# row_1 = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["b1", "b2", "b3"]]
# print(row_1[0][1])

row_1 = ["👩‍🦯", "🕺", "👨‍🦯"]
row_2 = ["👩‍🦼", "🏃‍♂️", "🤳"]
row_3 = ["🏃‍♀️", "🧜‍♂️", "💅"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

inPut = int(input("Where\n"))
if inPut == 11:
    map[0][0] = "❌"
    print("You are very close 👌")

elif inPut == 12:
    map[0][1] = "❌"
    print("Did you just pick!?\nYou are JOKER!!! 🤡")

elif inPut == 13:
    map[0][2] = "❌"
    print("I am so sorry\nYou loose😭")

elif inPut == 21:
    map[1][0] = "🥇"
    print("You just won a 🥇")
elif inPut == 22:
    map[1][1] = "❌"
    print("I am so sorry\nYou loose😭")

elif inPut == 23:
    map[1][2] = "❌"
    print("Shit!!! you are almost there 🥶") 

elif inPut == 31:
    map[2][0] = "❌"
    print("You are very close 👌") 
  
elif inPut == 32:
    map[2][1] = "❌"
    print("You are very close 👌")

else:
    map[2][2] = "❌"
    print("Did you just pick!?\nYou are JOKER!!! 🤡")