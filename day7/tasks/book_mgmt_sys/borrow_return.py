
from datetime import datetime
from error_handling import CustomError
from book_management import Book, BookManagement

def borrow_book(member, book, quantity):
    if book.isbn not in BookManagement.inventory:
        raise CustomError("Invalid ISBN")

    if BookManagement.inventory[book.isbn].quantity < quantity:
        raise CustomError("Not enough copies available")

    BookManagement.inventory[book.isbn].quantity -= quantity
    transaction_time = datetime.now()


def return_book(member, book, quantity):
    if book.isbn not in BookManagement.inventory:
        raise CustomError("Invalid ISBN")

    BookManagement.inventory[book.isbn].quantity += quantity
    transaction_time = datetime.now()
    
