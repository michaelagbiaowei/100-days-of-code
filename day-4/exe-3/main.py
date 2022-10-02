row_1 = ["👩‍🦯", "🕺", "👨‍🦯"]
row_2 = ["👩‍🦼", "🏃‍♂️", "🤳"]
row_3 = ["🏃‍♀️", "🧜‍♂️", "💅"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

inPut = int(input("Where is the Treasure\n"))
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
