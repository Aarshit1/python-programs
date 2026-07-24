class employees:

    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructor called")

def CreateObj():
    print("creating object")
    obj=employees()
    print("function end")
    return obj

print("calling CreateObj function")
obj=CreateObj()
print("program end")