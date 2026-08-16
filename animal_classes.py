from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass


class human(animal):
    def move(self):
        print("I can walk and run")

class snake(animal):
    def move(self):
        print("I can crawl")

class bat(animal):
    def move(self):
        print("I can fly")

class whale(animal):
    def move(self):
        print("i can swim")

obj1=human()
obj1.move()

obj3=snake()
obj3.move()

obj1=bat()
obj1.move()

obj4=whale()
obj4.move()