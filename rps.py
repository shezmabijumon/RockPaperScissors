import random

options=("rock","paper","scissors")
player=None
running=True

while running:
    computer=random.choice(options)
    player=input("enter a choice(rock,paper,scissors):")

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player==computer:
        print("its a tie")
    elif player=="rock" and computer=="scissors":
        print("you win")
    elif player=="paper" and computer=="rock":
        print("you win")
    elif player=="scissors" and computer=="paper":
        print("you win")
    else:
        print("you lose")
    
    if not input("play again?(y/n): ").lower()=='y':
        break

print("thanks for playing")