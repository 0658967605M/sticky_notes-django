# ===== Importing external modules ===========
'''This is the section where you will import modules'''
from datetime import date, datetime
import os
# ==== Login Section ====
'''Here you will write code that will allow a user to login using while loops
'''


users = {}
if not os.path.exists('user.txt'):
    open('user.txt', 'a').close()

with open('user.txt', 'r') as f:
    for line in f:
        if not line.strip():
            continue
        parts = [x.strip() for x in line.strip().split(',', 1)]  # split only on first comma
        if len(parts) < 2:
            continue
        users[parts[0]] = parts[1]
        

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")
        continue


# ====== Function Section ======
# Functions for registering a user and not duplicating the username


def reg_user():
    new_username = input("Enter a new username: ")
    if new_username in users:
        print("Username already exists. Please choose another.")
        return
    if not new_username:
        print("Username cannot be empty.")
        return
    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm your password: ")
    if not new_password:
        print("Password cannot be empty.")
        return
    if new_password == confirm_password:
        need_newline = os.path.getsize('user.txt') > 0
        with open('user.txt', 'a', encoding='utf-8') as f:
            if need_newline:
                f.write("\n")
            f.write(f"{new_username}, {new_password}\n")
        print("User registered successfully!")
    else:
        print("Passwords do not match. Please try again.")
  


# Function for adding a task to task.txt file


def add_task():
    task_username = input("Enter the username of the person assigned to the task: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    current_date = input("Enter the current date (YYYY-MM-DD): ")
    task_due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    need_newline = os.path.getsize('tasks.txt') > 0
    with open('tasks.txt', 'a', encoding='utf-8') as f:
        if need_newline:
            f.write("\n")
        f.write(f"{task_username}, {task_title}, {task_description}, {current_date}, {task_due_date}, No\n")
    print("Task added successfully!")
    if not task_username:
        print("Assigned username cannot be empty.")
        return
    if task_username not in users:
        print("Warning: username does not exist in user list. Use reg_user to add them first.")
        confirm = input("Continue anyway? (y/n): ").lower()
        if confirm != 'y':
            return
    if not task_title:
        print("Title cannot be empty.")
        return
    if not task_description:
        print("Description cannot be empty.")
        return
    try:
        due_dt = datetime.strptime(task_due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

# Function to view all tasks in task.txt file


def view_all():
    with open('tasks.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) < 6:
                continue
            task_username, task_title, task_description, date_assigned, task_due_date, task_complete = parts
            print(f"Task: {task_title}\nAssigned to: {task_username}\nDate assigned: {date_assigned}\nDue date: {task_due_date}\nTask complete? {task_complete}\nTask description: {task_description}\n")


# Function to view only completed tasks


def view_completed():
    with open('tasks.txt', 'r') as f:
        found = False
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) < 6:
                continue
            task_username, task_title, task_description, date_assigned, task_due_date, task_complete = parts
            if task_complete.lower() == "yes":
                found = True
                print(f"Task: {task_title}\nAssigned to: {task_username}\nDate assigned: {date_assigned}\nDue date: {task_due_date}\nTask complete? {task_complete}\nTask description: {task_description}\n")
        if not found:
            print("No completed tasks found.")


# Function to view tasks assigned to the logged-in user


def view_mine():
    user_tasks = []
    with open('tasks.txt', 'r') as f:
        all_lines = f.readlines()
    for idx, line in enumerate(all_lines):
        parts = line.strip().split(', ')
        if len(parts) < 6:
            continue
        task_username, task_title, task_description, date_assigned, task_due_date, \
            task_complete = parts
        if task_username == username:
            user_tasks.append({
                "index": idx,
                "raw": line,
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": task_due_date,
                "date_assigned": date_assigned,
                "complete": task_complete
            })
    with open('tasks.txt', 'r') as f:
        all_lines = f.readlines()
    user_tasks = []
    for idx, line in enumerate(all_lines):
        parts = line.strip().split(', ')
        if len(parts) < 6:
            continue
        task_username, task_title, task_description, date_assigned, task_due_date, \
            task_complete = parts
        if task_username == username:
            user_tasks.append({
                "index": idx,
                "raw": line,
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": task_due_date,
                "date_assigned": date_assigned,
                "complete": task_complete
            })
    if not user_tasks:
        print("No tasks assigned to you.")
    else:
        for i, task in enumerate(user_tasks, 1):
            print(f"Task {i}:")
            print(f"  Title: {task['title']}")
            print(f"  Description: {task['description']}")
            print(f"  Date assigned: {task['date_assigned']}")
            print(f"  Due date: {task['due_date']}")
            print(f"  Task complete? {task['complete']}\n")
      
        selection = input("Enter the task number to select, or -1 to return to the main menu: ")
        if selection == "-1":
            return
        else:
            print("Invalid number. Try again or -1 to return to main menu.")
        try:
            selection = int(selection)
            if 1 <= selection <= len(user_tasks):
                selected_task = user_tasks[selection - 1]
                print("Selected Task:")
                print(f"Title: {selected_task['title']}")
                print(f"Description: {selected_task['description']}")
                print(f"Due date: {selected_task['due_date']}")
                print(f"Task complete? {selected_task['complete']}\n")
 
                action = input("Enter 'c' to mark as complete or 'e' to edit the task: ").lower()
                if action == 'c':
                    # update that specific line by index
                    parts = all_lines[selected_task["index"]].strip().split(', ')
                    if len(parts) >= 6:
                        parts[5] = "Yes"
                        all_lines[selected_task["index"]] = ", ".join(parts) + "\n"
                        with open('tasks.txt', 'w') as f:
                            f.writelines(all_lines)
                    print("Task marked as complete.")
                elif action == 'c':
                    if selected_task['complete'] == "Yes":
                        print("Cannot edit a completed task.")
                    else:
                        parts = all_lines[selected_task["index"]].strip().split(', ')
                        if len(parts) >= 6:
                            parts[5] = "Yes"
                            all_lines[selected_task["index"]] = ", ".join(parts) + "\n"
                            with open('tasks.txt', 'w') as f:
                                f.writelines(all_lines)
                    print("Task marked as complete.")
                elif action == 'c':
                    if selected_task['complete'] == "Yes":
                        print("Cannot edit a completed task.")
                elif action == 'e':
                    if selected_task['complete'] == "No":
                        edit_choice = input("Edit (u)sername, (d)ue date, or (b)oth? ").lower()
                        new_username = selected_task['username']
                        new_due_date = selected_task['due_date']
                        if edit_choice == 'u' or edit_choice == 'b':
                            new_username = input("Enter new username: ")
                        if edit_choice == 'd' or edit_choice == 'b':
                            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                        new_line = f"{new_username}, {selected_task['title']}, {selected_task['description']}, {selected_task['date_assigned']}, {new_due_date}, No\n"
                        new_lines = []
                        for line in all_lines:
                            if line == selected_task["raw"]:
                                new_lines.append(new_line)
                            else:
                                new_lines.append(line)
                            if not new_username:
                                print("Username cannot be empty. Edit cancelled.")
                                return
                            if new_username not in users:
                                print("Username not found. Use reg_user to add them first.")
                                confirm = input("Continue anyway? (y/n): ").lower()
                                if confirm != 'y':
                                    return
                            new_username = new_username.strip()
                            new_due_date = new_due_date.strip()
                            try:
                                datetime.strptime(new_due_date, "%Y-%m-%d")
                            except ValueError:
                                print("Invalid date format. Edit cancelled.")
                                return
                       # reconstruct line and save
                        parts = all_lines[selected_task["index"]].strip().split(', ')
                        if len(parts) >= 6:
                            parts[0] = new_username
                            parts[4] = new_due_date
                            parts[5] = "No"
                            all_lines[selected_task["index"]] = ", ".join(parts) + "\n"
                            with open('tasks.txt', 'w') as f:
                                f.writelines(all_lines)
                        print("Task updated.")
                else:
                    print("Invalid action.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")
# ...existing code...



# Function to delete a task


def delete_task():
    with open('tasks.txt', 'r') as f:
        all_lines = f.readlines()
    for i, line in enumerate(all_lines, 1):
        parts = line.strip().split(', ')
        if len(parts) < 6:
            continue
        task_username, task_title, task_description, date_assigned, task_due_date, task_complete = parts
        print(f"{i}. Task: {task_title}, Assigned to: {task_username}, Due date: {task_due_date}, Complete: {task_complete}")
    selection = input("Enter the task number to delete, or -1 to return to the main menu: ")
    if selection == "-1":
        return
    try:
        selection = int(selection)
        if 1 <= selection <= len(all_lines):
            confirm = input(f"Are you sure you want to delete task {selection}? (y/n): ").lower()
            if confirm == 'y':
                del all_lines[selection - 1]
                with open('tasks.txt', 'w') as f:
                    f.writelines(all_lines)
                print("Task deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")


# Function to generate task overview report


def generate_task_overview():
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    today = datetime.today()
    with open('tasks.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) < 6:
                continue
            _, _, _, date_assigned, due_date, complete = parts
            total_tasks += 1
            if complete == "Yes":
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                try:
                    due = datetime.strptime(due_date, "%Y-%m-%d")
                    if due < today:
                        overdue_tasks += 1
                except ValueError:
                    pass
    percent_incomplete = (uncompleted_tasks / total_tasks * 100) if total_tasks else 0
    percent_overdue = (overdue_tasks / total_tasks * 100) if total_tasks else 0
    with open('task_overview.txt', 'w') as f:
        f.write(f"Total tasks: {total_tasks}\n")
        f.write(f"Completed tasks: {completed_tasks}\n")
        f.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        f.write(f"Overdue tasks: {overdue_tasks}\n")
        f.write(f"Percentage incomplete: {percent_incomplete:.2f}%\n")
        f.write(f"Percentage overdue: {percent_overdue:.2f}%\n")


# Function to generate user overview report


def generate_user_overview():
    users = []
    with open('user.txt', 'r') as f:
        for line in f:
            username = line.strip().split(',')[0]
            users.append(username)
    tasks = []
    with open('tasks.txt', 'r') as f:
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) < 6:
                continue
            task = {
                "username": parts[0],
                "due_date": parts[4],
                "complete": parts[5]
            }
            tasks.append(task)
    total_users = len(users)
    total_tasks = len(tasks)
    with open('user_overview.txt', 'w') as f:
        f.write(f"Total users registered: {total_users}\n")
        f.write(f"Total tasks generated: {total_tasks}\n\n")
        for user in users:
            user_tasks = [t for t in tasks if t["username"] == user]
            num_user_tasks = len(user_tasks)
            percent_assigned = (num_user_tasks / total_tasks * 100) if total_tasks else 0
            completed = [t for t in user_tasks if t["complete"] == "Yes"]
            num_completed = len(completed)
            percent_completed = (num_completed / num_user_tasks * 100) if num_user_tasks else 0
            uncompleted = [t for t in user_tasks if t["complete"] == "No"]
            num_uncompleted = len(uncompleted)
            percent_uncompleted = (num_uncompleted / num_user_tasks * 100) if num_user_tasks else 0
            overdue = 0
            today = datetime.today()
            for t in uncompleted:
                try:
                    due = datetime.strptime(t["due_date"], "%Y-%m-%d")
                    if due < today:
                        overdue += 1
                except ValueError:
                    continue
            percent_overdue = (overdue / num_user_tasks * 100) if num_user_tasks else 0
            f.write(f"User: {user}\n")
            f.write(f"  Total tasks assigned: {num_user_tasks}\n")
            f.write(f"  Percentage of all tasks assigned: {percent_assigned:.2f}%\n")
            f.write(f"  Percentage completed: {percent_completed:.2f}%\n")
            f.write(f"  Percentage incomplete: {percent_uncompleted:.2f}%\n")
            f.write(f"  Percentage overdue: {percent_overdue:.2f}%\n\n")
    print("User overview report generated as 'user_overview.txt'.")

# ====== Menu Section ======
# Present the menu to the user and
# make sure that the user input is converted to lower case.

while True:
    if username == "admin":
        menu = input('''Select an option:
r - register a user
a - add task
va - view all tasks
vc - view completed tasks
vm - view my tasks
to - generate task overview
uo - generate user overview
del - delete a task
gr - generate both reports
ds - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select an option:
a - add task
va - view all tasks
vc - view completed tasks
vm - view my tasks
e - exit
: ''').lower()


# '''This code block will add a new user to the user.txt file'''

    if menu == 'r' and username == "admin":
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vc':
        view_completed()
    elif menu == 'vm':
        view_mine()
    elif menu == 'del' and username == "admin":
        delete_task()
    elif menu == 'to' and username == "admin":
        generate_task_overview()
        print("Task overview report generated as 'task_overview.txt'.")
    elif menu == 'uo' and username == "admin":
        generate_user_overview()
        print("User overview report generated as 'user_overview.txt'.")
    elif menu == 'gr' and username == "admin":
        generate_task_overview()
        generate_user_overview()
        print("Both reports generated: 'task_overview.txt' and 'user_overview.txt'.")
    elif menu == 'ds' and username == "admin":
        try:
            with open('task_overview.txt', 'r') as f:
                print("\nTask Overview Report:")
                print(f.read())
        except FileNotFoundError:
            print("Task overview report not found.")
        try:
            with open('user_overview.txt', 'r') as f:
                print("User Overview Report:")
                print(f.read())
        except FileNotFoundError:
            print("User overview report not found.")
        # auto-generate missing reports
        if not os.path.exists('task_overview.txt') or not os.path.exists('user_overview.txt'):
            print("Reports not found — generating now...")
            generate_task_overview()
            generate_user_overview()
        # display reports
        with open('task_overview.txt', 'r') as f:
            print("\nTask Overview Report:")
            print(f.read())
        with open('user_overview.txt', 'r') as f:
            print("\nUser Overview Report:")
            print(f.read())
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
        continue
