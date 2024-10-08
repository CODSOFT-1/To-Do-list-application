import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Initialize the tasks list
tasks = []

# Function to update the task list display
def update_task_list():
    task_list.delete(0, tk.END)  # Clear the listbox
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        task_list.insert(tk.END, f"{i+1}. {task['task']} - [{status}]")

# Function to add a new task
def add_task():
    task = entry_task.get()
    if task:
        tasks.append({"task": task, "done": False})
        entry_task.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a task as done
def mark_task_done():
    try:
        selected_task_index = task_list.curselection()[0]
        tasks[selected_task_index]["done"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear the task list
def clear_tasks():
    tasks.clear()
    update_task_list()

# Creating the widgets
label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

task_list = tk.Listbox(frame, height=10, width=35, font=("Helvetica", 12))
task_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

entry_task = tk.Entry(root, width=35, font=("Helvetica", 12))
entry_task.pack(pady=10)

# Buttons for interacting with the to-do list
btn_add_task = tk.Button(root, text="Add Task", width=20, command=add_task)
btn_add_task.pack(pady=5)

btn_mark_done = tk.Button(root, text="Mark Task as Done", width=20, command=mark_task_done)
btn_mark_done.pack(pady=5)

btn_delete_task = tk.Button(root, text="Delete Task", width=20, command=delete_task)
btn_delete_task.pack(pady=5)

btn_clear_tasks = tk.Button(root, text="Clear All Tasks", width=20, command=clear_tasks)
btn_clear_tasks.pack(pady=5)

# Run the application
root.mainloop()
