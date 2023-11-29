class BookManagement:
    def __init__(self):
        self.book_inventory = {}

    def add_book(self, book_id, title, author, quantity):
        if book_id not in self.book_inventory:
            self.book_inventory[book_id] = {'title': title, 'author': author, 'quantity': quantity}
            print(f"Book '{title}' added to inventory.")
        else:
            print(f"Book with ID {book_id} already exists in inventory.")

    def update_book(self, book_id, title=None, author=None, quantity=None):
        if book_id in self.book_inventory:
            book = self.book_inventory[book_id]
            if title is not None:
                book['title'] = title
            if author is not None:
                book['author'] = author
            if quantity is not None:
                book['quantity'] = quantity
            print(f"Book details updated for ID {book_id}.")
        else:
            print(f"Book with ID {book_id} not found in inventory.")

    def remove_book(self, book_id):
        if book_id in self.book_inventory:
            removed_book = self.book_inventory.pop(book_id)
            print(f"Book '{removed_book['title']}' removed from inventory.")
        else:
            print(f"Book with ID {book_id} not found in inventory.")

    def display_inventory(self):
        print("\nBook Inventory:")
        for book_id, book_info in self.book_inventory.items():
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")

