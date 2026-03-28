'''Write a Book class:

__init__ takes title, author, pages
__repr__ returns something that looks like valid Python: Book(title='Atomic Habits', author='James Clear', pages=320)
__str__ returns something human friendly: "Atomic Habits" by James Clear (320 pages)'''

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    def __str__(self):
        return f"'{self.title}' by '{self.author}' written in {self.pages}pages"
b = Book("Atomic Habits", "James Clear", 320)
print(b)        # use __str__
print(repr(b))  # use __repr__

books = [Book("Atomic Habits", "James Clear", 320), Book("Deep Work", "Cal Newport", 296)]
print(books)   