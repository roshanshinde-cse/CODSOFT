# Task-01-ToDoList/todo.py

tasks = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task name: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def remove_task():
    view_tasks()
    num = int(input("Enter task number to remove: "))
    if 0 < num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f"Removed: {removed['title']}")
    else:
        print("Invalid number!")

def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark done: "))
    if 0 < num <= len(tasks):
        tasks[num - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid number!")

while True:
    show_menu()
    choice = input("Choose: ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
