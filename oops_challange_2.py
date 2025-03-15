
class library:

    def __init__(self, book, book_price):
        
        self.book = book
        self.book_price = book_price

    #add book to the library
    def add_book(self, new_book):
        
        self.book = new_book
        print(f"book has been added {self.book}")

    #withdraw the book
    def withdraw(self, withdraw_book):

        if self.book == withdraw_book:
            self.book = self.book - withdraw_book

        print(f"{self.book} book has been withdraw")

    def __str__(self):
        return f"book id : {self.book} \n book price : {self.book_price}"

book1 = library(23, 'firfirey')

print(book1)

book1.add_book(45)

print(book1)

book1.withdraw(23)

