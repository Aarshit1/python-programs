import random
playing=True
number=random.randint(0,9)

print("I will select a random number between 0-9, try to guess it first try and win!")
print("restart the agme when you want to play agian after you win")

while playing:
    guess=int(input("Guess the number : "))
    if guess==number:
        print("\nyou win! restart to continue")
        break
    else:
        ("too bad, try again")