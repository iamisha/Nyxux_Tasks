# 1. To-Do List Initialization:
def initialize_todo_list():
    todo_list = []
    return todo_list

# 2. Help Message
def display_help_message():
    print("Available commands:")
    print("add -> add a task to the to-do list.")
    print("complete -> mark a task as complete.")
    print("view all -> view the current tasks in the to-do list.")
    print("view complete -> view all the completed tasks in the to-do list.")
    print("delete -> Delete the todo-list and and take it to the bin if it's not permanent.")
    print("view incomplete -> view all the incomplete tasks in the to-do list.")
    print("view bin -> View all the tasks that are deleted and are not currently in bin.")
    print("restore -> restore the deleted task from the bin.")
    print("clear bin -> delete all the to-dos that arre presented in the bin.")
    print("help -> display all the help message.")
    print("exit -> exit the program.")

# 3. Task Addition
def add_task(todo_list):
    while True:
        task_description = input("Enter task description: ")
        if task_description in [task[0] for task in todo_list]:
            print("Task already exists. Please enter a unique task.")
        else:
            todo_list.append((task_description, False))
            break

# 4. Task Completion
def complete_task(todo_list):
    while True:
        task_number = input("Enter task number to mark as complete: ")
        try:
            task_index = int(task_number) - 1 # indices in list starts from zero
            if task_index < 0 or task_index >= len(todo_list):
                print("Invalid task number. Please enter a valid task number.")
            else:
                todo_list[task_index] = (todo_list[task_index][0], True)
                break
        except ValueError:
            print("Task number should be a valid integer. Please enter a valid task number.")

# 5. All to-do List view
def view_all_tasks(todo_list):
    for index, task in enumerate(todo_list): # enumerate(used to get both the index and corresponding task in each iteration.)
        status = "Incomplete" if not task[1] else "Completed"
        print(f"{index + 1}. {task[0]} ({status})")

# 6. Completed to-do list view
def view_completed_tasks(todo_list):
    completed_tasks = [task for task in todo_list if task[1]]
    if not completed_tasks:
        print("No completed tasks found.")
        return
    for index, task in enumerate(completed_tasks):
        print(f"{index + 1}. {task[0]} (Completed)")

# 7. Delete to-do
def delete_task(todo_list, bin_list):
    while True:
        task_number = input("Enter task number to delete: ")
        try:
            task_index = int(task_number) - 1
            if task_index < 0 or task_index >= len(todo_list):
                print("Invalid task number. Please enter a valid task number.")
            else:
                confirmation = input("Do you want to delete it permanently? (yes/no): ")
                if confirmation.lower() == "yes":
                    del todo_list[task_index]
                else:
                    bin_list.append(todo_list.pop(task_index))
                break
        except ValueError:
            print("Task number should be a valid integer. Please enter a valid task number.")

# 8. Incomplete to-do list view
def view_incomplete_tasks(todo_list):
    incomplete_tasks = [task for task in todo_list if not task[1]]
    if not incomplete_tasks:
        print("No incomplete tasks found.")
        return
    for index, task in enumerate(incomplete_tasks):
        print(f"{index + 1}. {task[0]} (Incomplete)")

# 9. Invalid options entered 
def invalid_option():
    print("Invalid option. Please enter a valid command.")

# 10. View bin
def view_bin(bin_list):
    if not bin_list:
        print("Bin is empty.")
        return
    for index, task in enumerate(bin_list):
        print(f"{index + 1}. {task[0]} (Deleted)")

# 11. Restore deleted to-do
def restore_from_bin(todo_list, bin_list):
    while True:
        task_number = input("Enter task number to restore: ")
        try:
            task_index = int(task_number) - 1
            if task_index < 0 or task_index >= len(bin_list):
                print("Invalid task number. Please enter a valid task number.")
            else:
                todo_list.append(bin_list.pop(task_index))
                break
        except ValueError:
            print("Task number should be a valid integer. Please enter a valid task number.")

# 12. Clear bin command
def clear_bin(bin_list):
    confirmation = input("Are you sure you want to clear the bin? (yes/no): ")
    if confirmation.lower() == "yes":
        bin_list.clear()
        print("Bin cleared.")
    else:
        print("Bin not cleared.")

def main():
    todo_list = initialize_todo_list()
    bin_list = []
    display_help_message()

    while True:
        command = input("Enter command: ")

        if command == "add":
            add_task(todo_list)
        elif command == "complete":
            complete_task(todo_list)
        elif command == "view all":
            view_all_tasks(todo_list)
        elif command == "view complete":
            view_completed_tasks(todo_list)
        elif command == "delete":
            delete_task(todo_list, bin_list)
        elif command == "view incomplete":
            view_incomplete_tasks(todo_list)
        elif command == "view bin":
            view_bin(bin_list)
        elif command == "restore":
            restore_from_bin(todo_list, bin_list)
        elif command == "clear bin":
            clear_bin(bin_list)
        elif command == "help":
            display_help_message()
        elif command == "exit":
            confirmation = input("Are you sure you want to exit? (yes/no): ")
            if confirmation.lower() == "yes":
                break
        else:
            invalid_option()

    print("Thank you for using the to-do list manager.")

if __name__ == "__main__":
    main()