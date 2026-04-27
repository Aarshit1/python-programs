print("enter marks obtained in five subjects")

mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

tot=mark1+mark2+mark3+mark4+mark5

avg=tot/5

if avg>=91 and avg<=100:
    print("your grade is A+")

elif avg>=81 and avg<=90:
    print("your grade is A")

elif avg>=71 and avg<=80:
    print("your grade is B+")

elif avg>=61 and avg<=70:
    print("your grade is B")

elif avg>=51 and avg<=60:
    print("your garde is C")

elif avg>=41 and avg<=50:
    print("your grade is D")

elif avg>=31 and avg<=40:
    print("you fail")

else:
    print("invalid")


