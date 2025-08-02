class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                print(f"\nChecked out: {book}")
                return
    def return_book(self,book):
        self._books.append(book)
        

    def list_available_books(self):

        for book in self._books:
            print(f"{book}")



