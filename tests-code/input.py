print("Hello Michael" + input("Hello world"))
input("What is your name? ")
print(len(input("Enter your name")))

name = input("Enter your name ")
length = len(name)
print(f"Your name has {length} Characters")

a = input("a:")
b = input("b:")

c = a
a = b
b = c

print(a)
print(b)

print("Welcome to the band name generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's the name of your pet\n")

print("Your Band Name is:", city + " " + pet)