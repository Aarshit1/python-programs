my_set={1,2,3}
print(my_set)

my_set={1.0,"Hello",(1,2,3)}
print(my_set)

my_set={1,2,2,3,2,2}
print(my_set)

my_set=set([1,2,3,2])
print(my_set, "\n")

num_set=set([1,2,3,4,5])
print("original set : ",num_set)
num_set.pop()
print("after removing last element : ",num_set)