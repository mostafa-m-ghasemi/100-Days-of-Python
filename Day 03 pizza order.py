print("Welcome to the pizza order program1")

size = input("What size pizza do you want? s or m or l  ").lower()
pepperoni = input("Do you wanna extra pepperoni? y or n  ").lower()
cheese = input("Do you wanna extra cheese? y or n  ").lower()
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if cheese == "y":
    bill += 1

print(f"Your total bill is ${bill}")
