from book_management import BookManagement  # Assuming the book_management module is in the same directory
from member_management import LibraryMember
from generate_reports import ReportGeneration
def main():
    book_manager = BookManagement()
    member_manager = LibraryMember()
    generate_reports = ReportGeneration(book_manager, member_manager)
    

    while True:
        print("\nLibrary Management System")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Generate Reports")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            manage_books(book_manager)
        elif choice == '2':
            manage_members(member_manager)  # You can create a similar function for managing members
        elif choice == '3':
             while True:
                print("\nReport Generation Menu")
                print("1. Generate Book Inventory Report")
                print("2. Generate Member Borrowing Report")
                print("3. Display Sorting Options for Books")
                print("4. Go Back")

                report_choice = input("Enter your choice (1-4): ")

                if report_choice == '1':
                    generate_reports.generate_book_inventory_report()
                elif report_choice == '2':
                    generate_reports.generate_member_borrowing_report()
                elif report_choice == '3':
                    generate_reports.display_sorting_options()
                elif report_choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def manage_books(book_manager):
    while True:
        print("\nBook Management Menu")
        print("1. Add New Book")
        print("2. Update Book Details")
        print("3. Remove Book")
        print("4. Display Book Inventory")
        print("5. Go Back")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))
            book_manager.add_book(book_id, title, author, quantity)
        elif choice == '2':
            book_id = int(input("Enter Book ID to update: "))
            title = input("Enter Updated Title (Press Enter to keep the current title): ")
            author = input("Enter Updated Author (Press Enter to keep the current author): ")
            quantity = int(input("Enter Updated Quantity (Press Enter to keep the current quantity): "))
            book_manager.update_book(book_id, title, author, quantity)
        elif choice == '3':
            book_id = int(input("Enter Book ID to remove: "))
            book_manager.remove_book(book_id)
        elif choice == '4':
            book_manager.display_inventory()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
def manage_members(member_manager):
    while True:
        print("\nMember Management Menu")
        print("1. Add New Member")
        print("2. Update Member Details")
        print("3. Remove Member")
        print("4. Display Members List")
        print("5. Go Back")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            contact = input("Enter Contact: ")
            member_manager.add_member(member_id, name, address, contact)
        elif choice == '2':
            member_id = int(input("Enter Member ID to update: "))
            name = input("Enter Updated Name (Press Enter to keep the current name): ")
            address = input("Enter Updated Address (Press Enter to keep the current address): ")
            contact = input("Enter Updated Contact (Press Enter to keep the current contact): ")
            member_manager.update_member(member_id, name, address, contact)
        elif choice == '3':
            member_id = int(input("Enter Member ID to remove: "))
            member_manager.remove_member(member_id)
        elif choice == '4':
            member_manager.display_members()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            
if __name__ == "__main__":
    main()
