from auth import login
from processor import borrow_book

login("Pierre", "1234")
borrow_book("Python Programming")

from auth import login
from processor import borrow_book, view_books

if login("admin", "password123"):
    borrow_book("Python Programming")
    borrow_book("Software Engineering")
    view_books()