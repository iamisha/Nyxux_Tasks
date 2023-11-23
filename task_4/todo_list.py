def initialize_todo_list():
    todo_list = []
    return todo_list

def display_help_message():
    print("Available commands:")
    print("add -> add a task to the to-do list.")
    print("complete -> mark a task as complete.")
    print("view all -> view the current tasks in the to-do list.")
    print("view complete -> view all the completed tasks in the to-do list.")
    print("view incomplete -> view all the incomplete tasks in the to-do list.")
    print("help -> display all the help message.")
    print("exit -> exit the program.")

def add_task(todo_list):
    while True:
        task_description = input("Enter task description: ")
        if task_description in [task[0] for task in todo_list]:
            print("Task already exists. Please enter a unique task.")
        else:
            todo_list.append((task_description, False))
            break

def complete_task(todo_list):
    while True:
        task_number = input("Enter task number to mark as complete: ")
        try:
            task_index = int(task_number) - 1
            if task_index < 0 or task_index >= len(todo_list):
                print("Invalid task number. Please enter a valid task number.")
            else:
                todo_list[task_index] = (todo_list[task_index][0], True)
                break
        except ValueError:
            print("Task number should be a valid integer. Please enter a valid task number.")

def view_all_tasks(todo_list):
    for index, task in enumerate(todo_list):
        status = "Incomplete" if not task[1] else "Completed"
        print(f"{index + 1}. {task[0]} ({status})")

def view_completed_tasks(todo_list):
    completed_tasks = [task for task in todo_list if task[1]]
    if not completed_tasks:
        print("No completed tasks found.")
        return
    for index, task in enumerate(completed_tasks):
        print(f"{index + 1}. {task[0]} (Completed)")

def view_incomplete_tasks(todo_list):
    incomplete_tasks = [task for task in todo_list if not task[1]]
    if not incomplete_tasks:
        print("No incomplete tasks found.")
        return
    for index, task in enumerate(incomplete_tasks):
        print(f"{index + 1}. {task[0]} (Incomplete)")

def invalid_option():
    print("Invalid option. Please enter a valid command.")

def main():
    todo_list = initialize_todo_list()
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
        elif command == "view incomplete":
            view_incomplete_tasks(todo_list)
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