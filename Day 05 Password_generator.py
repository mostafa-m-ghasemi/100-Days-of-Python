import random

def random_list(num, main_list):
    result = []
    for i in range(num):
        result.append(random.choice(main_list))
    return result


print("*********Welcome to Password Generator**********")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letter = int(input("How many letters would you like? "))
symbol = int(input("How many symbols would you like? "))
number = int(input("How many numbers would you like? "))
password_list = []

password_list += random_list(letter, letters)
password_list += random_list(symbol, symbols)
password_list += random_list(number, numbers)

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i

print(f"The password is: {password}")