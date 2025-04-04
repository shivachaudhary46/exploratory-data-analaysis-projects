import random;

comp = ['s', 'w', 'g'];
random.SystemRandom().shuffle(comp);
print(comp);
comp.reverse();
comp1 = "".join(random.choices(comp));
print(comp1);

num_of_book = 0;
book = [];

while num_of_book >= len(book):
    newBook = input('enter the new book and enter exit for ending : ');
    book.append(newBook);
    num_of_book += 1
    if newBook == 'exit':
        num_of_book -= 1;
        book.pop();
        break;

print(book);
print(num_of_book);

# class library():

#     #decorator function
#     def decorator(function):
#         def decorated():
#             function();
#         return decorated

#     #takes function
#     @decorator
#     def main(self, newBook):
#         book = [];
#         num_of_book = 0;
#         while num_of_book >= len(book):
#             self.newBook = input('enter new book or enter exit to end: ');
#             book.append(newBook);
#             num_of_book += 1;
#             if newBook == 'exit':
#                 book.pop();
#                 num_of_book -= 1;
#                 break;

#     main();

#library management software 
class library():
    def __init__(self) -> None:
        self.books = []
        self.no_book = 0;

    def addBook(self, book):
        self.books.append(book);
        self.no_book = len(self.books);

    def showReslt(self):
        print(f'{self.no_book} book has been added in LIBRARY ');
        for index, book in enumerate(self.books, 1):
            print(index, book);
        

object1 = library();
user = int(input('how many book you want to add: '));

#to write book
for i in range(user):
    bookName = input('book name : ');   
    object1.addBook(bookName);

object1.showReslt();

#clear the cutter excersice 
#random name.png lai sequence name.png
import os;
