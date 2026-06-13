try:
    a=int(input("enter a number : "))
    print("you entered : ",a)
except ValueError as ex:
    print("exception : ",ex)