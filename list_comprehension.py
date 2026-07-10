num1=int(input("enter a number : "))
odd_numbers=[i for i in range (num1) if i%2==1]
print("the odd numbers in your num range are : ",odd_numbers)

fruits=["apple","banana","orange","mango"]
capital_fruits=[i.capitalize() for i in fruits]
print("\n capitalized fruits : ",capital_fruits)