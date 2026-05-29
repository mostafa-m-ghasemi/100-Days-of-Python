
import random

choices = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
if 0 <= user_choice <= 2:
    print(f"You chose {choices[user_choice]}")
computer_choice = random.randint(0,2)
print(f"Computer chose {choices[computer_choice]}")
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif computer_choice < user_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Draw!")
