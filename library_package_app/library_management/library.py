from .book import Book
from .member import Member


class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book):
        for existing_book in self.__books:
            if existing_book.get_book_id() == book.get_book_id():
                print("Book ID already exists.")
                return

        self.__books.append(book)
        print("Book added.")

    def add_member(self, member):
        self.__members.append(member)
        print("Member registered.")

    def issue_book(self, book_id, member_name):
        for book in self.__books:
            if book.get_book_id() == book_id:
                if book._available:
                    book._available = False
                    book._borrowed_by = member_name
                    print("Book issued.")
                else:
                    print("Book already issued.")
                return

        print("Book not found.")

    def return_book(self, book_id):
        for book in self.__books:
            if book.get_book_id() == book_id:
                book._available = True
                book._borrowed_by = None
                print("Book returned.")
                return

        print("Book not found.")

    def display_books(self):
        for book in self.__books:
            book.display_info()
            print()

        print("Total Books:", Book.count)

    def display_members(self):
        for member in self.__members:
            print("Member:", member.get_name())

        print("Total Members:", Member.count)
