import time


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

    def remove_book(self, book):
        self.books.remove(book)

    def show_books(self):
        return "All books:\n" + "\n".join([book.info() for book in self.books])

    def show_unread(self):
        return "Unread books:\n" + "\n".join(
            [book.info() for book in self.books if not book.read]
        )


def menu():
    """
    Runs the command-line interface (CLI) menu for managing the book library.

    The function continuously prompts the user to choose an action:
    - view all books
    - view unread books
    - add a new book
    - remove a book
    - mark a book as read

    The menu runs in an infinite loop until the program is terminated manually.
    It also handles invalid input using a ValueError exception.
    """

    while True:
        try:
            time.sleep(0.5)
            asc_menu = int(
                input(
                    """choice the: 
            1 - show all books
            2 - show unread books
            3 - add the book
            4 - remove the book
            5 - mark read
            6 - exit
            >>
            """.strip()
                )
            )
            if asc_menu == 1:
                (
                    print(my_library.show_books())
                    if my_library.books
                    else print("It's empty here..")
                )
            elif asc_menu == 2:
                print(my_library.show_unread())
            elif asc_menu == 3:
                try:
                    asc_menu_title = input("enter the book title: ")
                    asc_menu_author = input("enter the author of the book: ")
                    book = Book(asc_menu_title, asc_menu_author)
                    my_library.add_book(book)
                except KeyboardInterrupt:
                    print("\ngoodbye!")
                    break
            elif asc_menu == 4:
                try:
                    found = False
                    asc_remove = input("enter title to remove: ")
                    for book in my_library.books:
                        if book.title == asc_remove:
                            my_library.remove_book(book)
                            found = True
                            print("successfully!")
                            break
                    if not found:
                        print("not found..")
                except KeyboardInterrupt:
                    print("\ngoodbye!")
                    break

            elif asc_menu == 5:
                try:
                    asc_mark = input("Enter a title to mark the book: ")
                    for book in my_library.books:
                        if book.title == asc_mark:
                            book.mark_read()
                except KeyboardInterrupt:
                    print("\ngoodbye!")
                    break
            elif asc_menu == 6:
                print("goodbye!")
                break
            else:
                print("enter the correct integer!")
        except ValueError:
            print("enter the integer!")
        except KeyboardInterrupt:
            print("\ngoodbye!")
            break

if __name__ == "__main__":
    my_library = Library()
    menu()
