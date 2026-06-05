def add(p,q):
    return p+q

def subtract(p,q):
    return p-q

def multiply(p,q):
    return p*q

def divide(p,q):
    return p/q

print("select the operation : ")
print("a. addition")
print("b. subtract")
print("c. multiply")
print("d. divide")

choice = input("enter your choice : a/b/c/d : ")

num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))

if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 'b':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 'd':
    print(num1, "/", num2, "=", divide(num1, num2))

else :
    print("invalid input")