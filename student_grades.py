sum=0
grade_book={"John":76,"Emma":89,"Jack":66,"Ivan":79,"Lisa":92}

for value in grade_book.values():
    sum+=value

avg=sum/len(grade_book)
print("average : ",avg)

print("Highest Score : ",max(grade_book.values()),"\nLowest Score : ",min(grade_book.values()))

score=input("enter the student's name : ")

print(grade_book.get(score))