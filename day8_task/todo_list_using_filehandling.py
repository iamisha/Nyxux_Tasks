import os

# File paths
TODO_FILE = "todo_list.txt"
BIN_FILE = "bin_list.txt"

# 1. To-Do List Initialization:
def initialize_todo_list(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass
    with open(file_path, "r") as file:
        return [line.strip().split(",") for line in file.readlines()]

# 2. Help Message
def display_help_message():
    print("Available commands:")
    print("add -> add a task to the to-do list.")
    print("complete -> mark a task as complete.")
    print("view all -> view the current tasks in the to-do list.")
    print("view complete -> view all the completed tasks in the to-do list.")
    print("delete -> Delete the todo-list and take it to the bin if it's not permanent.")
    print("view incomplete -> view all the incomplete tasks in the to-do list.")
    print("view bin -> View all the tasks that are deleted and are not currently in bin.")
    print("restore -> restore the deleted task from the bin.")
    print("clear bin -> delete all the to-dos that are presented in the bin.")
    print("help -> display all the help message.")
    print("exit -> exit the program.")

# 3. Task Addition
def add_task(todo_list):
    while True:
        task_description = input("Enter task description: ")
        if any(task_description == task[0] for task in todo_list):
            print("Task already exists. Please enter a unique task.")
        else:
            with open(TODO_FILE, "a") as file:
                file.write(f"{task_description},False\n")
            break

# 4. Task Completion
def complete_task(todo_list):
    while True:
        task_number = input("Enter task number to mark as complete: ")
        try:
            task_index = int(task_number) - 1
            if 0 <= task_index < len(todo_list):
                todo_list[task_index] = (todo_list[task_index][0], "True")
                with open(TODO_FILE, "w") as file:
                    file.write("\n".join([",".join(task) for task in todo_list]))
                break
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Task number should be a valid integer. Please enter a valid task number.")

# 5. All to-do List view
def view_all_tasks(todo_list):
    for index, task in enumerate(todo_list):
        status = "Incomplete" if task[1] == "False" else "Completed"
        print(f"{index + 1}. {task[0]} ({status})")

# 6. Completed to-do list view
def view_completed_tasks(todo_list):
    completed_tasks = [task for task in todo_list if task[1] == "True"]
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
            if 0 <= task_index < len(todo_list):
                confirmation = input("Do you want to delete it permanently? (yes/no): ")
                if confirmation.lower() == "yes":
                    del todo_list[task_index]
                    with open(TODO_FILE, "w") as file:
                        file.write("\n".join([",".join(task) for task in todo_list]))
                else:
                    bin_list.append(todo_list.pop(task_index))
                    with open(TODO_FILE, "w") as file:
                        file.write("\n".join([",".join(task) for task in todo_list]))
                    with open(BIN_FILE, "a") as bin_file:
                        bin_file.write(",".join(bin_list[-1]) + "\n")
                break
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Task number should be a valid integer. Please enter a valid task number.")

# 8. Incomplete to-do list view
def view_incomplete_tasks(todo_list):
    incomplete_tasks = [task for task in todo_list if task[1] == "False"]
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
            if 0 <= task_index < len(bin_list):
                todo_list.append(bin_list.pop(task_index))
                with open(TODO_FILE, "w") as file:
                    file.write("\n".join([",".join(task) for task in todo_list]))
                with open(BIN_FILE, "w") as bin_file:
                    bin_file.write("\n".join([",".join(task) for task in bin_list]))
                break
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Task number should be a valid integer. Please enter a valid task number.")

# 12. Clear bin command
def clear_bin(bin_list):
    confirmation = input("Are you sure you want to clear the bin? (yes/no): ")
    if confirmation.lower() == "yes":
        bin_list.clear()
        with open(BIN_FILE, "w"):
            pass
        print("Bin cleared.")
    else:
        print("Bin not cleared.")

def main():
    todo_list = initialize_todo_list(TODO_FILE)
    bin_list = initialize_todo_list(BIN_FILE)
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
