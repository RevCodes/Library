class Book:
    def __init__(self, title, author):
        
        self.title = title 
        self.author = author
        self.available = True

def __str__(self):
        return f"Books: {self.title}, Author:{self.author}, Availability: {self.available}"

class Members:
    def __init__(self, name, ID):

        self.name = name
        self.ID = ID
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.Book = []
        self.Members = []

    def add_book(self, Book):
        self.Book.append(Book)

    def register_member(self, Members):
        self.Members.append(Members)

    def borrow_book(self, Book, Members):
        if Book.available:
            Book.available = False
            Members.borrowed_books.append(Book)
            print(f"{Book.title} has been lent to {Members.name}")

        else: 
            print(f"Sorry{Book.title } is not available to borrow")

    def return_book(self, Book , Members):
        if Book in Members.borrowed_books:
            Book.avaliable = True
            Members.borrowed_books.remove(Book)
            print(f"{Book.title} has been returned by {Members.name}")
        else:
            print(f"{Members.name} did not borrow {Book.title}")

book1 = Book("The Cat in the Hat", "Dr Seuss")
book2 = Book("Refactoring", "Kent Beck")

member1 = Members("Enrique", 101)
member2 = Members("Steve", 102)

library = Library()

library.add_book(book1)
library.add_book(book2)

library.register_member(member1)
library.register_member(member2)

library.borrow_book(book1, member1)

library.borrow_book(book2, member2)

library.return_book(book1, member1)

library.return_book(book1, member2)