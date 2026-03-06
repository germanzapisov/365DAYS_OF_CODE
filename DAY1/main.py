class Book:
    """
    Represents a book with a title, author, and read status.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        read (bool): Whether the book has been read (default False).

    Methods:
        mark_read(): Marks the book as read.
        info(): Returns a formatted string with book information.
    """

    def __init__(self, title, author, read=False):
        self.__title = title
        self.__author = author
        self.__read = read

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def read(self):
        return self.__read

    def mark_read(self):
        self.__read = True

    def info(self):
        status = "read" if self.read else "unread"
        text = f"Title: {self.title} | author: {self.author} | status: {status}"
        return text

    def __str__(self):
        return self.info()


class Library:
    """
    This class allows you to add a book to the book library and retrieve it when needed.

    Attributes:
    books(list): List of books

    Methods:
    add_book(): Add a book to the list
    show_books(): Returns all books
    show_unread(): Returns unread books
    """

    def __init__(self, books=None):
        if books is None:
            books = []
        self.__books = books

    @property
    def books(self):
        return self.__books

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        return "All books:\n" + "\n".join([book.info() for book in self.books.copy()])

    def show_unread(self):
        return "Unread books:\n" + "\n".join(
            [book.info() for book in self.books if not book.read]
        )


if __name__ == "__main__":
    my_book = Book("War and Peace", "Leo Tolstoy")
    my_book_two = Book("Dead Souls", "Nikolai Gogol")
    my_library = Library()
    my_library.add_book(my_book)
    my_library.add_book(my_book_two)
    my_book.mark_read()
    print(my_library.show_books())
    print(my_library.show_unread())
