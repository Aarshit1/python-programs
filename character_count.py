string=input("enter anything : ")
char=input("enter a character : ")

i=0
count=0

while(i<len(string)):
    if (string [i]==char):
        count=count+1
    i=i+1

print("the total number number",char,"has occured :",count)