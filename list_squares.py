def square():
    num1=int(input("enter a starting range : "))
    num2=int(input("enter an end range : "))

    squares=[]
    odd=[]
    even=[]

    for i in range(num1,num2+1): #because python ignores end range(num2)
        sq=i**2
        squares.append(sq)

        if sq%2==0:
            even.append(sq)
        else:
            odd.append(sq)

    print("list with squares numbers from your range : ",squares)
    print("list of odd squares : ",odd)
    print("list of even squares : ",even)

square()