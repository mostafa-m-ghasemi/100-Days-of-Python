import random
from day14data import data

def profile():
    random_number = random.randint(0, 49)
    name = data[random_number]["name"]
    country = data[random_number]["country"]
    description = data[random_number]["description"]
    followers = data[random_number]["follower_count"]
    compare = f"{name}, a {description}, from {country}."
    return compare, followers

def higher_lower():
    profile_a, followers_a = profile()
    profile_b, followers_b = profile()
    if profile_a == profile_b:
        profile_b, followers_b = profile()

    score = 0
    correct = True
    while correct:
        if score > 0:
            print("\n" * 10)
            print(f"Your score is ******  {score}  ******")
        print(f"Compare A : {profile_a}")
        print("********** VS **********")
        print(f"Compare B : {profile_b}")

        a_or_b = input("Who do you think has more followers A or B? ").lower()
        if a_or_b == "a" and followers_a >= followers_b:
            score += 1
            print("********** PERFECT **********")
            profile_b, followers_b = profile()
        elif a_or_b == "b" and followers_b >= followers_a:
            score += 1
            print("********** PERFECT **********")
            profile_a, followers_a = profile()
        elif a_or_b == "a" and followers_a <= followers_b:
            print("********** YOU LOST **********")
            print(f"***your total score is ****  {score}  ***")
            correct = False
            play_again = input("Would you like to play again? 'y' or 'n' :   ").lower()
            if play_again == "y":
                higher_lower()
            else:
                print("See you next time!")
        elif a_or_b == "b" and followers_b <= followers_a:
            print("********** YOU LOST **********")
            print(f"***your total score is ****  {score}  ***")
            correct = False
            play_again = input("Would you like to play again? 'y' or 'n' :   ").lower()
            if play_again == "y":
                higher_lower()
            else:
                print("See you next time!")

higher_lower()



