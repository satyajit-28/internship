'''
@Author:    satyajit 

@Goal:      To implement a menu driven to do list

@Date:      30th Oct 2026

'''
'''
def to_do_list():
    print("-" * 50)
    print("===== MY TO DO LIST =====")
    print("-" * 50)


    task = []
    print("1. Add new task \n2. View task \n3. Edit task \n4. Delete task \n5. Exit")
    
    choice = int(input("Enter option here: "))

    if choice == 1:
        new_task = input("Enter your task --> ")
        task.append(new_task)

        with open("to_do_list.txt", 'w') as file_handle:
            for t in task:
                file_handle.write(t + "\n")

        with open("to_do_list.txt", "r") as file_handle:
            r = file_handle.read()
            print(r)

     
        print("Task added successfully...!")
    
    
    elif choice == 2:
        with open("to_do_list.txt", "r") as file_handle:
            r = file_handle.read()
            print(r)


    elif choice == 3:
        with open("to_do_list.txt", 'w') as file_handle:
            r = file_handle.read()
'''
'''
def to_do_list():
    print("-" * 50)
    print("===== MY TO DO LIST =====")
    print("-" * 50)
    
    tasks = []

    while True:
        
        print("1. Add task \n2. View task \n3. Delete task \n4. Exit")
        
        choice = int(input("Enter option here: "))

    
        if choice == 1:
            new_task = input("Enter your task here --> ")
            tasks.append(new_task)
            print("Task added successfully...!")


        elif choice == 2:
            print("\n Your tasks")

            if len(tasks) < 0:
                print("You dont have any tasks..!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"Task No: {i}\nTask Info: {task} ")

        elif choice == 3:
            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                tasks.remove(task_number)
            else:
                print("Invalid task number")
        elif choice == 4:
            print("Thank you...!")
            break
    
        else:
            print("Invalid choice. Please try again.")

        
to_do_list()
                
'''




    
tasks = []

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
