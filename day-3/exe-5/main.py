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
