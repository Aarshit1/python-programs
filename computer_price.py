class Computer:

    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice=price

obj=Computer()
obj.sell()

obj.__maxprice=1000
obj.sell()

obj.setMaxPrice(1000)
obj.sell()