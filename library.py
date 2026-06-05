class LibraryItem:
    def __init__(self, title):
        self._title = title
        self._available = True

    def display_info(self):
        print("Library Item")


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
        self.borrowed_by = None

    def display_info(self):      # Polymorphism
        status = "Available" if self._available else "Issued"

        print("Title:", self._title)
        print("Author:", self.author)
        print("Status:", status)

        if self.borrowed_by:
            print("Borrowed By:", self.borrowed_by)


class Member:
    def __init__(self, name):
        self.name = name


books = []
members = []

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
        title = input("Title: ")
        author = input("Author: ")
        books.append(Book(title, author))
        print("Book added.")

    elif choice == "2":
        name = input("Member Name: ")
        members.append(Member(name))
        print("Member registered.")

    elif choice == "3":
        title = input("Book Title: ")
        member_name = input("Member Name: ")

        for book in books:
            if book._title == title:
                if book._available:
                    book._available = False
                    book.borrowed_by = member_name
                    print("Book issued.")
                else:
                    print("Book already issued.")
                break
        else:
            print("Book not found.")

    elif choice == "4":
        title = input("Book Title: ")

        for book in books:
            if book._title == title:
                book._available = True
                book.borrowed_by = None
                print("Book returned.")
                break
        else:
            print("Book not found.")

    elif choice == "5":
        for book in books:
            book.display_info()
            print()

    elif choice == "6":
        for member in members:
            print("Member:", member.name)

    elif choice == "7":
        break

    else:
        print("Invalid choice")