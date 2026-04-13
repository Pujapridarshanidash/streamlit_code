import random
print("welcome to Rock_paper_sessior!")
print("Type rock,paper,or scissors to play.Type quit to exit")
choices=["rock","paper","scissors"]
while True:
    user_choice=input("\n your choice:").lower()
    if user_choice=="quit":
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("invalid choice! please type rock,paper,or scissors")
        continue
    computer_choice=random.choice(choices)
    print(f"computer chose:{computer_choice}")
    if user_choice==computer_choice:
        print("its a tie!")
    elif(
        (user_choice=="rock"and computer_choice=="scissors")or
        (user_choice=="paper" and computer_choice=="rock")or
        (user_choice=="scissors"and computer_choice=="paper")      
        ):
        print("You win!")
    else:
        print("You lose!")
    