class IOstring:
    def __init__(self):
        self.str1=""

    def getString(self):
        self.str1=input("enter a string : ")

    def printString(self):
        self.str1=print("Uppercase string is : ",self.str1.upper())

str1=IOstring()

str1.getString()
str1.printString()