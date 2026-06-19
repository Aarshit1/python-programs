import random

while True:
    user=input("enter your choice(rock/paper/scissors) : ")
    actions=["rock","paper","scissors"]
    computer=random.choice(actions)

    print("you chose", user, ", computer chose",computer)

    if computer==user:
        print("both chose ",user," its a tie")
    elif user=="rock":
        if computer=="scissors":
            print("you win")
        else:
            print("you lose")
    elif user=="paper":
        if computer=="rock":
            print("you win")
        else:
            print("you lose")
    elif user=="scissors":
        if computer=="paper":
            print("you win")
        else:
            print("you lose")
    else:
        print("invalid :/")

    again=input("\n play again?(y/n)")
    if again !="y":
        break
    elif again !="n":
        pass
    else:
        print("invalid")