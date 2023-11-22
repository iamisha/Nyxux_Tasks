lib_invent = []


def display_help():
    print("LMS\nAvailable commands:\nadd -> Add a book\nremove -> Remove a book\ndisplay -> Display books\nexit -> Exit program")


def add_book():
    try:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")

        for book in lib_invent:
            if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
                print("Error: This book is already in the inventory.")
                return

        lib_invent.append({"title": title, "author": author})
        print(f"Book '{title}' by {author} added to the inventory.")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_book():
    try:
        title_to_remove = input("Enter the title of the book to remove: ")

        for book in lib_invent:
            if book["title"].lower() == title_to_remove.lower():
                lib_invent.remove(book)
                print(f"Book '{title_to_remove}' removed from the inventory.")
                return

        print(f"Book '{title_to_remove}' not found in the inventory.")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_books():
    try:
        if not lib_invent:
            print("The inventory is empty.")
        else:
            print("\nCurrent Books in the Inventory:")
            for book in lib_invent:
                print(f"Title: {book['title']}, Author: {book['author']}")
            print()
    except Exception as e:
        print(f"An error occurred: {e}")


def confirm_exit():
    try:
        return input("Are you sure you want to exit? (yes/no): ").lower() == 'yes'
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


while True:
    try:
        display_help()
        user_command = input("Enter a command: ").lower()

        if user_command == 'add':
            add_book()
        elif user_command == 'remove':
            remove_book()
        elif user_command == 'display':
            display_books()
        elif user_command == 'exit':
            if confirm_exit():
                print("Exiting the program. Thank you!")
                break
            else:
                print("Continuing...")
        else:
            print("Invalid command. Please enter a valid command.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
