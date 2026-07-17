class Dog:
    species="Dog"

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

Max=Dog("Golden Retriever","Golden Brown")
Trix=Dog("Labrador Retriever","White")

print("Max is a {} and {} in color".format(Max.breed, Max.color))
print("Trix is a {} and {}".format(Trix.breed, Trix.color))