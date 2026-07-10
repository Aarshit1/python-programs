numbers1=[1,2,3,4,5]
numbers2=[6,7,8,9,10]

result=map(lambda x,y : x+y , numbers1, numbers2) 

print("addition of two lists : ",list(result))

numbers=[1,2,3,4,5]

def sq(n):
    return n*n

square=map(sq, numbers)

print("square of the elements : ",list(square))