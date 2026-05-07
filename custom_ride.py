print("choose your ride : ")
print("1. Bike")
print("2. Car")

choice=int(input("enter your choice : "))

if choice==1 :
    print("what type of bike?")
    print("1. Scooter\n")
    print("2. Motorbike\n")

    choice2=int(input("enter your bike choice : "))
    if choice2==1 :
        print("you have chosen scooter")
    else :
        print("you have choosen motorbike")

elif choice==2 :
    print("what type of car?")
    print("1. Sedan")
    print("2. SUV")

    choice3=int(input("enter your car choice : "))
    if choice3==1:
        print("you have chosen Sedan")
    else:
        print("you have chosen SUV")

else :
    print("wrong choice")