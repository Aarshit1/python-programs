class India():
    def capital(self):
        print("Capital of India is New Delhi")

    def language(self):
        print("Hindi is the primary language of India")

    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Capital of USA is Washington")

    def language(self):
        print("English is the primary language of USA")

    def type(self):
        print("USA is a developed country")

obj_ind=India()
obj_usa=USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()