class LibraryItem:
    def __init__(self, title):
        self._title = title
        self._available = True

    def display_info(self):
        print("Library Item")
