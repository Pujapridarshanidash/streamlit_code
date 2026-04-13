import random

print("Welcome to the Dice Rolling simulator!")

while True:
    roll=input("\n press enter to roll the dice(or type 'quit' to exit) :")
    if roll.lower()=="quit":
        print("Thanks for playing!")
        break
    
    # die1=random.randient(1,6)
    # die2=random.randient(1,6)
    
    # print(f"you rolled:{die1} and {die2}")
    
    print("You rolled:" , random.randint(1,6))