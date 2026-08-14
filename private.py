class myClass:

    __privateVar=27

    def privMeth(self):
        print("im inside class myClass")

    def hello(self):
        print("private variable value : ",myClass.__privateVar)

foo=myClass()
foo.hello()
foo.__privMeth