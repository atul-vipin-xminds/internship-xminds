from .library_item import LibraryItem


class Book(LibraryItem):
    count = 0

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
