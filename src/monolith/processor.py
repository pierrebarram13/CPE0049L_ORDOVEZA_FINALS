books = []

def borrow_book(book):
    books.append(book)
    print(f"Borrowed: {book}")

from database import borrowed_books

def borrow_book(book):
    borrowed_books.append(book)
    print(f"{book} borrowed successfully.")

def view_books():
    print("Borrowed Books:")
    for book in borrowed_books:
        print("-", book)