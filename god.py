import random
print("Welcome to the Number Guessing Game! ")
print("iam thinking of a number between 1 and 100...")
secret_number=random.randint(1,100)
attempts=0
while True:
    guess=int(input("enter your guess:"))
    attempts+=1
    if guess<secret_number:
        print("Too low!")
    elif guess>secret_number:
        print("Too high!")
    else:
        print(f"Correct!The number was {secret_number}")
        print(f"you guessed it in {attempts}attempts")
        break