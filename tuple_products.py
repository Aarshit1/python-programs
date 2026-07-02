tup1=(4,3,2,2,-1,18)
tup2=(2,4,8,8,3,2,9)
product1=1
product2=1

for i in tup1:
    product1*=i

for j in tup2:
    product2*=j

print("product of first tuple : ",product1)
print("product of second tuple : ",product2)