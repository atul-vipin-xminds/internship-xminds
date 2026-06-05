class LibraryItem:
    def __init__(self, title):
        self._title = title
        self._available = True

    def display_info(self):
        print("Library Item")


class Book(LibraryItem):
    count = 0      # Static variable

    def __init__(self, book_id, title, author):
        super().__init__(title)
        self.__book_id = book_id
        self._author = author
        self._borrowed_by = None

        Book.count += 1

    def get_book_id(self):
        return self.__book_id

    def display_info(self):
        status = "Available" if self._available else "Issued"

        print("Book ID:", self.__book_id)
        print("Title:", self._title)
        print("Author:", self._author)
        print("Status:", status)

        if self._borrowed_by:
            print("Borrowed By:", self._borrowed_by)


class Member:
    count = 0      # Static variable

    def __init__(self, name):
        self.__name = name

        Member.count += 1

    def get_name(self):
        return self.__name


class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book):
        for b in self.__books:
            if b.get_book_id() == book.get_book_id():
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


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Register Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Members")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")

        library.add_book(Book(book_id, title, author))

    elif choice == "2":
        name = input("Member Name: ")

        library.add_member(Member(name))

    elif choice == "3":
        book_id = input("Book ID: ")
        member_name = input("Member Name: ")

        library.issue_book(book_id, member_name)

    elif choice == "4":
        book_id = input("Book ID: ")

        library.return_book(book_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_members()

    elif choice == "7":
        break

    else:
        print("Invalid choice.")