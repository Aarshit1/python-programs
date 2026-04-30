print("Enter a numerator : ")
numN=int(input())
print("Enter a denominator : ")
numD=int(input())

if numN%numD==0 :
    print("\n"+str(numN)," is divisible by "+str(numD))
else :
    print("\n"+str(numN), " is not divisible by "+str(numD))