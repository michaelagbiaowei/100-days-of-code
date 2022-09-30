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
test_list = [1, 4, 5, 2, 7]

# printing original list
print("Original list is : " + str(test_list))

# using random.randint() to
# get a random number
rand_idx = random.randint(0, len(test_list)-1)
random_num = test_list[rand_idx]

# printing random number
print("Random selected number is : " + str(random_num))
