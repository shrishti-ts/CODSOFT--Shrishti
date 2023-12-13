#SHRISHTI SINGH
#CODSOFT Task 1 to-do list

# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append({'task': task, 'completed': False})

# Function to view tasks
def view_tasks():
    if not tasks:
        print("There is no tasks to display.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            status = "✓" if task['completed'] else " "
            print(f"{i + 1}. [{status}] {task['task']}")

# Function to mark a task as completed
def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index.")

# Main loop for the application to work properly
while True:
    print("\n Options:")
    print("1. Add a task: ")
    print("2. View tasks: ")
    print("3. Mark a task as completed: ")
    print("4. Delete a task: ")
    print("5. Quit: ")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
        print("Task added.")
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task index to mark as completed: ")) - 1
        mark_completed(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task index to delete: ")) - 1
        delete_task(task_index)
    elif choice == '5':
        print("Bye,work finished!")
        break
    else:
        print("Invalid choice. Please try again.")