#assigning different variables

name="Penguin"
age=15
is_student=True
weight=38.5

#printing different variables and their data types

print("Name : ",name)
print("datatype of name is ",type(name))

print("Age : ", age)
print("Datatype of age is ",type(age))

print("is_student : ", is_student)
print("Datatype of is_student is ",type(is_student))

print("Weight : ",weight)
print("Datatype of weight is ", type(weight))

#type casting to convert the datatypes of variables

print("\n After type casting...")
age=str(age)
print(age)
print("Datatype of age is ",type(age))

weight=int(weight)
print(weight)
print("Datatype of weight is ",type(weight))