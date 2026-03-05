class Book:
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
        return f"Title: {self.title} | author: {self.author} | status: {self.read}"
