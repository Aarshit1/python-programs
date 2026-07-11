import random

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

password=""
newPassword=""

for i in range (10):
    password+=random.choice(characters)

print("your password is : ",password)
generate=input("\n do you want to re-generate your password?(y/n/yes/no) : ")

if generate=="y" or generate=="yes":
    for i in range(10):
        newPassword+=random.choice(characters)
    print("\n your new pasword is : ",newPassword)
elif generate=="n" or generate=="no":
    pass
else:
    print("\n invalid, you must write either of y, n, yes or no")