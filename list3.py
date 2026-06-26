L=[4,5,1,3,76,17,12,3]
print("orginal list : ",L)

count=0

for i in L:
    count+=i

avg=count/len(L)

print("sum : ",count)
print("average : ",avg)

L.sort()

print("the smallest element is ",L[0])
print("the largest element is ",L[-1])