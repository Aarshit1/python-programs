try:
    num1, num2=eval(input("enter two numbers seperated by a comma(,) : "))
    result=num1/num2
    print("result : ",result)
except ZeroDivisionError:
    print("dividing by zero is an error!!!")
except SyntaxError:
    print("comma is missing, enter values like : 3,4")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this WILL run no matter what")