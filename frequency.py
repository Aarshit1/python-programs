fruit_basket={"apple":3, "banana":4, "orange":2, "mango":2, "watermelon":1}
print("orginal dictionary : " + str(fruit_basket))

K=2

res=0
for keys in fruit_basket:
    if fruit_basket[keys]==K:
        res=res+1

print("frequency of K is : " + str(res))