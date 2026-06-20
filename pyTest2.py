try:
    num1=float(input("enter a number : "))
    num2=float(input("enter another number : "))

    def add(a,b):
        return(a+b)

    def subtract(a,b):
        return(a-b)

    def multiply(a,b):
        return(a*b)

    def divide(a,b):
        return(a/b)

    ask=input("enter what calculation you want to perform (sum/difference/product/divide): ")

    if ask=="sum":
        print(add(num1,num2))
    elif ask=="difference":
        print(subtract(num1,num2))
    elif ask=="product":
        print(multiply(num1,num2))
    elif ask=="divide":
        print(divide(num1,num2))
    else:
        print("invalid operation")

except ValueError:
    print("enter a number, worng input")
except ZeroDivisionError:
    print("dividing by 0 is invalid!!!")