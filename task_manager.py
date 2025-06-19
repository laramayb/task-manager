import json
import os

# File where tasks will be stored
TASKS_FILE = "tasks.json"

# Load tasks from a file (if it exists)
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file in JSON format
def save_tasks(tasks):
    with open("tasks.json", "w") as  file:
        json.dump(tasks, file, indent=4) # indent makes it look nicer

# Prints the list of tasks with their status (done or not)
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, tasks in enumerate(tasks, 1):
            if tasks["done"]:
                status = "✓"
            else:
                status = " "
            print(f"{i}. [{status}] {tasks['title']}")

# Add a new task to the list
def add_task(task): 
    title = input("Enter a new task: ")
    if not title.strip():
        print("Task title cannot be empty.")
        return
    new_task = {"title": title, "done": False}
    task.append(new_task)
    print(f'Task "{title}" added.')

# Delete a task from the list
def delete_task(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as complete
def complete_task(tasks):
    if not tasks:
        print("No tasks to complete.")
        return
    
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop that shows the menu and handles user input
def main():
    # first load any saved tasks
    tasks = load_tasks()

    while True: 
        print("\nTask Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Save & Quit")

        option = input("Choose an option: ") 

        if option == "1":
            list_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start program
if __name__ == "__main__":
    main()