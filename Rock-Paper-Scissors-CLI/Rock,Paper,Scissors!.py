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
attacks = [rock, paper, scissors]
choice = int(input("What do you choose? (Type 0 for Rock, 1 for Paper, 2 for Scissors):\n"))
comp_choice = random.randint(0,2)
if choice == comp_choice:
    print("Draw!")
elif choice == 0:   #If choice is Rock
    if comp_choice == 1:
        print("You Lost!😿")
    else:
        print("You Won!🎊")
elif choice == 1:   #If choice is Paper
    if comp_choice == 2:
        print("You Lost!😿")
    else:
        print("You Won!🎊")
elif choice == 2:   #If choice is Scissors
    if comp_choice == 0:
        print("You Lost!😿")
    else:
        print("You Won!🎊")
else:
    print("Error!! Please type within the provided range of inputs!")
print(f"Your Choice:{attacks[choice]}\nComputer's Choice:{attacks[comp_choice]}")