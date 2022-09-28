year = int(input("What year do you want to check?\n"))
if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# print(2020 / 4) # must pass
# print(2020 /100) # must fail
# print(2020 / 400) # must fail
