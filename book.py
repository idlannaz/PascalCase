class Book:

    total_books_count = 0

    def __init__(self, author: str, title: str):

        self.author = author
        self.title = title
        Book.total_books_count += 1

    def get_info(self) -> str:

        return f"Title: {self.title}, Author: {self.author}"

    @classmethod
    def total_books(cls) -> int:

        return cls.total_books_count

    @staticmethod
    def is_valid_title(title: str) -> bool:

        return isinstance(title, str) and len(title.strip()) > 0


if __name__ == "__main__":
    book1 = Book("Barney Stinson", "Bro Code")
    book2 = Book("Sam Austen", "Meow: A Novel")

    print(book1.get_info())
    print(book2.get_info())

    print(Book.is_valid_title("Bro Code"))
    print(Book.is_valid_title("Meow: A Novel"))

    print(Book.total_books())
