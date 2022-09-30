# # num_char = len(input("What is your name "))
# # # print("Your name has" + num_char + "characters")
# # # print(type(num_char))

# # #TYPE CONVERSION OR TYPE CASTING
# # #This is knowm as changing data from one data type to another

# # new_num_char = str(num_char)
# # print("Your name has " + new_num_char + " characters")
# #===================================================================
# # a = 123
# # print(type(123))

# # a = str(123)
# # print(type(a))

# # a = float(123)
# # print(type(a))

# # print(70 + float("100.5"))

# # # print(str(70) + str(100))
# # #===============================================================

inPut = input("Type a two digit number:\n")
value1 = inPut[0]
value2 = inPut[1]
result1 = int(value1)
result2 = int(value2)
outPut = result1 + result2
print(outPut)

# inPut = input("Enter any two didgits\n")
# results = int(inPut[0]) + int(inPut[1])
# print(results)

inPut = input("Enter any two digits\n")
print(int(inPut[0]) + int(inPut[1]))