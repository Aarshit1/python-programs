class parent:
    def __init__(self,eye_color,height):
        self.eye_color=eye_color
        self.height=height

    def showTraits(self):
        print("eye color : ",self.eye_color)
        print("height(cm) : ",self.height)

class kid(parent):
    def __init__(self,name,age,eye_color,height):
        self.name=name
        self.age=age
        super().__init__(eye_color,height)

    def showTraits(self):
        print("eye_color : ",self.eye_color)
        print("height(cm) : ",self.height)
        super().showTraits()

    def hobbies(self,hobby):
        print(self.name, "loves" , hobby)

child=kid("John",14,"brown",160)

child.showTraits()
child.hobbies("painting")

print("is kid a subclass of parent?", issubclass(kid,parent))