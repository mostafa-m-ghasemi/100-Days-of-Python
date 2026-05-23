try:
    age = int(input("What is your age? "))
except ValueError:
    print("Please enter a numerical number!")
    age = int(input("What is your age? "))
if age >= 18:
    print("You can drive!")
else:
    print("You can not drive!")