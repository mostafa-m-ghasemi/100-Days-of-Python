import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    """ Checks if the answer is correct. Returns the number of turns"""
    if guess > answer:
        print("Your guess is ***too high***")
        return turns - 1
    elif guess < answer:
        print("Your guess is ***too low***")
        return turns - 1
    else:
        print("Your guess is correct")

def set_difficulty():
    level = input("What is the difficulty? easy or hard:  ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("*****Welcome to the Number Guessing Game*****")
    print("I'm Thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses! You lose!")
            return
        elif guess != answer:
            print("guess again")

game()


