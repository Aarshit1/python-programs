import random

low=int(input("enter a low number : "))
high=int(input("enter a high number : "))

rndm=random.randint(low,high)

chance=5
guess=0

while guess<chance :
    guess=guess+1
    guessuser=int(input("enter your guess : "))

    if guessuser==rndm:
        print("Correct!")
        break
    elif guess>=chance and guessuser!=rndm:
        print("Boo!")
    elif guessuser>rndm:
        print("too high")
    elif guessuser<rndm:
        print("too low")
    