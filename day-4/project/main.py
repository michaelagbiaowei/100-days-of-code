import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

all = [rock, paper, scissors]

ram = random.choice(all)
# print(ram)

inPut = input("What do you choose::: 0 for rock, 1 for paper or 2 for scissors\n")

if inPut == "0" and ram != rock: 
    print(f"you choose::: {all[0]}\nComputer choose::: {ram}\nYou WINNN")
elif inPut == "2" and ram == paper:
    print(f"you choose::: {all[2]}\nComputer choose::: {ram}\nYou WINNN")
elif inPut != "0" and ram == rock:
    print(f"you choose::: {all[0]}\nComputer choose::: {ram}\nYou LOOSE") 
elif inPut == "1" and ram != paper:
    print(f"you choose::: {all[0]}\nComputer choose::: {ram}\nYou LOOSE")
else:
    print("DRAW")
