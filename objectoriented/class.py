class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Example usage
book = Book("WINGS OF WIRE", "DR.ADBUL KALAM", 180)
print(book)  # Output: 'WINGS OF WIRE' by DR.ADBUL KALAM, 180 pages
