import os

def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Quit")

def view_todo_list():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("To-Do List is empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("To-Do List not found. Creating a new one.")

def add_task():
    task = input("Enter a new task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_task_done():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = f"[Done] {tasks[task_number - 1]}"
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            print("Quitting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
