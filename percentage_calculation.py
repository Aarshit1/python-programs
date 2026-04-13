print("Enter the marks obtanined in each subjec")

maths=int(input("Enter your marks : "))
science=int(input("Enter your marks : "))
english=int(input("Enter your marks : "))
social=int(input("Enter your marks : "))

sum=maths+science+english+social
print("The sum of all your mark is ",sum)

perc=(sum/400)*100

print("Your obtained percentage is ",perc)