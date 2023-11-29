import os
import datetime

class ReportGeneration:
    def __init__(self, book_manager, member_manager):
        self.book_manager = book_manager
        self.member_manager = member_manager

    def generate_timestamp(self):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        return timestamp

    def create_directory(self, directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

    def generate_book_inventory_report(self):
        timestamp = self.generate_timestamp()
        directory_name = f"reports/book_inventory_{timestamp}"
        self.create_directory(directory_name)

        file_path = os.path.join(directory_name, "book_inventory_report.txt")

        with open(file_path, 'w') as file:
            file.write("Book Inventory Report\n")
            file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for book_id, book_info in self.book_manager.book_inventory.items():
                file.write(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity: {book_info['quantity']}\n")

        print(f"Book inventory report generated at: {file_path}")

    def generate_member_borrowing_report(self):
        timestamp = self.generate_timestamp()
        directory_name = f"reports/member_borrowing_{timestamp}"
        self.create_directory(directory_name)

        file_path = os.path.join(directory_name, "member_borrowing_report.txt")

        with open(file_path, 'w') as file:
            file.write("Member Borrowing Report\n")
            file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for member in self.member_manager.members_list:
                file.write(f"Member ID: {member['member_id']}, Name: {member['name']}\n")
                # Add more information about member borrowing history if needed

        print(f"Member borrowing report generated at: {file_path}")

    def display_sorting_options(self):
        print("\nSorting Options:")
        print("1. Sort Books by Title")
        print("2. Sort Books by Author")
        print("3. Sort Books by Quantity")
        print("4. Go Back")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sorted_books = sorted(self.book_manager.book_inventory.items(), key=lambda x: x[1]['title'])
            for book_id, book_info in sorted_books:
                print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")
        elif choice == '2':
            sorted_books = sorted(self.book_manager.book_inventory.items(), key=lambda x: x[1]['author'])
            for book_id, book_info in sorted_books:
                print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")
        elif choice == '3':
            sorted_books = sorted(self.book_manager.book_inventory.items(), key=lambda x: x[1]['quantity'], reverse=True)
            for book_id, book_info in sorted_books:
                print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")
        elif choice == '4':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

