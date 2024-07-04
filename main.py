import json
import os
import datetime


def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            return json.load(f)
    else:
        return {}


def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)


def save_completed_task(task_name, completion_time):
    with open('completed_tasks.txt', 'a') as f:
        f.write(f"{task_name} - Completed at {completion_time}\n")


tasks = load_tasks()
n = len(tasks) + 1

print("Here is your to-do list:")

if len(tasks) == 0:
    print("Your do-do list is currently empty!")
else:
    for task_number, task_info in tasks.items():
        task_name = task_info[0]
        task_status = task_info[1]
        print(f"Task {task_number}: {task_name} ({task_status})")
    print("\n")


select = int(input("To add task enter 1\nTo remove task enter 2\nTo mark a task done enter 3\n Enter Here: "))

if select < 1 or select > 3:
    print("Invalid input")
else:
    if select == 1:
        addTask = input("Enter the task you want to add: ")
        tasks[n] = [addTask, "Pending"]
        n += 1
        print("Here is your to-do list:")
        for task_number, task_info in tasks.items():
            task_name = task_info[0]
            task_status = task_info[1]
            print(f"Task {task_number}: {task_name} ({task_status})")
        print("\n")
        save_tasks(tasks)  # Save the tasks dictionary
    elif select == 2:
        removeTask = int(
            input("Enter the task number that you want to remove: "))
        if 1 <= removeTask <= len(tasks):
            if str(removeTask) in tasks:
                del tasks[str(removeTask)]
                n -= 1  # Decrement n when a task is removed
                # Reassign task numbers
                new_tasks = {}
                n = 1
                for task in tasks.values():
                    new_tasks[n] = task
                    n += 1
                tasks = new_tasks
                print("Here is your to-do list:")
                if len(tasks) == 0:
                    print("Your do-do list is currently empty!")
                else:
                    for task_number, task_info in tasks.items():
                        task_name = task_info[0]
                        task_status = task_info[1]
                        print(f"Task {task_number}: {task_name} ({task_status})")
                    print("\n")
                save_tasks(tasks)  # Save the tasks dictionary
            else:
                print("Task number does not exist")
        else:
            print("Task number is out of range")
    elif select == 3:
        doneTask = int(input("Enter the task number that you want to mark as done: "))
        if 1 <= doneTask <= len(tasks):
            if str(doneTask) in tasks:
                task_name = tasks[str(doneTask)][0]
                tasks[str(doneTask)][1] = "Completed"
                completion_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_completed_task(task_name, completion_time)
                print("Here is your to-do list:")
                for task_number, task_info in tasks.items():
                    task_name = task_info[0]
                    task_status = task_info[1]
                    print(f"Task {task_number}: {task_name} ({task_status})")
                print("\n")
                save_tasks(tasks)  # Save the tasks dictionary
            else:
                print("Task number does not exist")
        else:
            print("Task number is out of range")


    # elif select == 4:
    #     pendingTask = int(input("Enter the task number that you want to mark as pending: "))
    #     if 1 <= pendingTask <= len(tasks):
    #         if str(pendingTask) in tasks:
    #             tasks[str(pendingTask)][1] = "Pending"
    #             print("Here is your to-do list:")
    #             for task_number, task_info in tasks.items():
    #                 task_name = task_info[0]
    #                 task_status = task_info[1]
    #                 print(f"Task {task_number}: {task_name} ({task_status})")
    #             print("\n")
    #             save_tasks(tasks)  # Save the tasks dictionary
    #         else:
    #             print("Task number does not exist")
    #     else:
    #         print("Task number is out of range")