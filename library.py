class LibraryItem:
    def __init__(self, title):
        self._title = title
        self._available = True

    def borrow(self):
        if self._available:
            self._available = False
            print("Borrowed successfully")
        else:
            print("Already borrowed")

    def display_info(self):      # Parent method
        print("Library Item")


class Book(LibraryItem):         # Inheritance
    def __init__(self, title, author, book_type):
        super().__init__(title)
        self.author = author
        self.type = book_type

    def display_info(self):      # Polymorphism
        status = "Available" if self._available else "Borrowed"

        print("Title:", self._title)
        print("Author:", self.author)
        print("Type:", self.type)
        print("Status:", status)


class Member:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        print(self.name, "is borrowing", book._title)
        book.borrow()


# Objects
book1 = Book("ABC", "XYZ", "Book")
book2 = Book("PQR", "LMN", "Magazine")

member1 = Member("atul")

print("Book 1:")
book1.display_info()

print("\nBook 2:")
book2.display_info()

print("\nBorrowing Book 1...")
member1.borrow_book(book1)

print("\nUpdated Book 1 Details:")
book1.display_info()