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

    def display_info(self):  # Parent method
        print("Library Item")


class Book(LibraryItem):  # Inheritance
    def __init__(self, title, author, book_type):
        super().__init__(title)
        self.author = author
        self.type = book_type

    def display_info(self):  # Polymorphism (method overriding)
        status = "Available" if self._available else "Borrowed"

        print(f"Title: {self._title}")
        print(f"Author: {self.author}")
        print(f"Type: {self.type}")
        print(f"Status: {status}")


# Objects
book1 = Book("ABC", "XYZ", "Book")
book2 = Book("PQR", "LMN", "Magazine")

print("Book 1:")
book1.display_info()

print("\nBook 2:")
book2.display_info()

print("\nBorrowing Book 1...")
book1.borrow()

print("\nUpdated Book 1 Details:")
book1.display_info()