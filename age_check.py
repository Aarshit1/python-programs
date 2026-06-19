try:
    age = int(input("Enter your age : "))

except ValueError:
    print("invalid age")
except TypeError:
    print("enter your AGE")

else:
    # This block only runs if NO exception was raised
    if age < 0 or age > 100:
        print("age too high, enter your actual age")
    elif age > 0 and age < 100:
        if age % 2 == 0:
            print("your age is even")
        else:
            print("your age is odd")
    else:
        print("wrong input")