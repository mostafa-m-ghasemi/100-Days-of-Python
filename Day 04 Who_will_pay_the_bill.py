import random
import time
count = int(input("How many people are you there? "))
people = []
for i in range(1, count + 1):
    name = input(f"Enter the name {i}: ")
    people.append(name)
will_pay = random.choice(people)
print("Picking a name ....")
time.sleep(3)
print(f"{will_pay} will pay the bill")
