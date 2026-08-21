class library:

    def __init__(self,title,author,is_burrowed):
        self.title=title
        self.author=author
        self.is_burrowed=is_burrowed
        #return self.title, self.author, self.is_burrowed

    def burrow(self):
        print("\nbook name:",self.title)
        print("\nauthor:",self.author)
        print("\nyou burrowed a book")

    def return_book(self):
        print("\nyou returned a book")

book1=library("To kill a mockingbird","Harper Lee",False)
book1.burrow()
book1.return_book()

book2=library("Harry Potter","JK Rowling",False)
book2.burrow()
book2.return_book()

book3=library("The Alchemist","Paulo Coelho",False)
book3.burrow()
book3.return_book()
