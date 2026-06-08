from .models import Book, Library, Member


def run():
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
