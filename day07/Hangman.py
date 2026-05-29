import random
print("*" * 15, "Welcome to the Hangman!", "*" * 15)

word_list = ["strawberry", "raspberry", "cherry", "watermelon", "apple", "plum", "banana", "melon", "lemon", "pineapple", "apricot", "mango", "nectarian", "orange", "avocado", "grapes", "blueberry", "blackberry", "peach"]

lives = 6
chosen_word = random.choice(word_list)

placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)

correct_letters = []
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for i in chosen_word:
        if guess == i:
            display += i
            correct_letters.append(guess)
        elif i in correct_letters:
            display += i
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You lost 1 live and you have only {lives} lives.")
        if lives == 0:
            game_over = True
            print("*"*15, "You lose!", "*"*15)

    if "_" not in display:
        game_over = True
        print("*" * 15, "You win!", "*" * 15)

