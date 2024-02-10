Task = []
Complete = []
while True:
    
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Tasks as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("")
    Choice = int(input("Enter Your Choice : "))
    if Choice == 1:
        task = input("Enter the task : ")
        Task.append(task)
        print(f"Task '{task}' added successfully")
    elif Choice == 2:
        if len(Task) == 0:
            print("No task to Display")
        else:
            for i in Task:
                print(i)
    elif Choice == 3:
        if len(Task) == 0:
            print("No task to Mark as Complete")
        else:
            for i in Task:
                print(i)
            mark = input("Enter the task to mark as Complete : ")
            if mark not in Task:
                print("This task is not in the to-do list")
            else:
                c = Task.index(mark)
                d = Task.pop(c)
                print(f"Task '{mark}' marked as Completed")
                Complete.append(d)
                for i in Complete:
                    print(f"Task Completed {i}")
    elif Choice == 4:
        if len(Task) == 0:
            print("No task to remove")
        else:
            for i in Task:
                print(i)
            remove = input("Enter the task to remove : ")
            Task.remove(remove)
            print(f"this task '{remove}' is removed")
    elif Choice == 5:
        print("Exiting Program")
        break
    else:
        print("Invalid Choice , Please Enter valid choice")