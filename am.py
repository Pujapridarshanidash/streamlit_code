import random

num = random.randint(1, 10)
guess = int(input("Please guess your number between 1 and 10: "))

if num == guess:
    print("You are right!")
else:
    print(f"Sorry, you are wrong. The correct number was {num}.")