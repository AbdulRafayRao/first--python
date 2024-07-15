import sys

def display_menu():
    print("To-Do List Application")
    print("======================")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("======================")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        view_todo_list(todo_list)
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_todo_list(todo_list)
            elif choice == 2:
                add_task(todo_list)
            elif choice == 3:
                remove_task(todo_list)
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
