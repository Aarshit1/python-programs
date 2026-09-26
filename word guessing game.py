import random

name=input("your name : ")
print("good luck ",name)

words=[
    "cancer","red", "python", "game", "word", "elegant", "equivocate",
    "simple", "word2", "password", "burger", "mathematics"
]

word=random.choice(words)

print("\nguess the words")

guesses=''
turns=12

while turns>0:
    failed=0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed+=1

    print()

    if failed==0:
        print("you win")
        print("the word is : ",word)
        break

    guess=input("guess a word : ").lower()

    if len(guess)!=1:
        print("enter a single character")
        continue

    if guess in guesses:
        print("you already guessed that character")
        continue

    guesses += guess

    if guess not in word:
        turns-=1
        print("wrong")
        print("you have ",turns,"more guesses")

        if turns==0:
            print("you lose")
            print("the word was ",word)