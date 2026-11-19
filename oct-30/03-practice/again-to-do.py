

    
tasks = []

def completed_tasks():
    if choice == 


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "completed": False})
        print(tasks)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        task_no = int(input("Enter task number to complete: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Thank you! Goodbye.")
        break


    else:
        print("Invalid choice. Please try again.")
