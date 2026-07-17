class student:
    grade=10
    print("hello I'm a student of grade ",grade,"\n")

obj=student()
print(obj)

class Vehicle:

    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage

modelX=Vehicle(250,23)

print("\n model maxspeed : ",modelX.maxspeed)
print("model mileage : ",modelX.mileage)