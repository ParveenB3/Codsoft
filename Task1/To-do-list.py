import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
from tkcalendar import Calendar
from datetime import datetime

import json

tasks = []
data_file = "tasks.json"


def load_tasks():
    global tasks
    try:
        with open(data_file, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    with open(data_file, "w") as file:
        json.dump(tasks, file, indent=4)


def open_calendar():
    def select_date():
        selected_date.set(calendar.get_date())
        calendar_window.destroy()

    calendar_window = Toplevel(root)
    calendar_window.title("Select Date")
    calendar = Calendar(calendar_window, date_pattern="yyyy-MM-dd")
    calendar.pack(pady=10)
    select_button = tk.Button(calendar_window, text="Select", command=select_date)
    select_button.pack(pady=5)


def open_clock():
    def select_time():
        selected_time.set(f"{hour_var.get()}:{minute_var.get()}:{second_var.get()}")
        clock_window.destroy()

    clock_window = Toplevel(root)
    clock_window.title("Select Time")

    hour_var = tk.StringVar(value="00")
    minute_var = tk.StringVar(value="00")
    second_var = tk.StringVar(value="00")

    tk.Label(clock_window, text="Hour").grid(row=0, column=0)
    tk.Label(clock_window, text="Minute").grid(row=0, column=1)
    tk.Label(clock_window, text="Second").grid(row=0, column=2)

    tk.Spinbox(clock_window, from_=0, to=23, textvariable=hour_var, width=5).grid(
        row=1, column=0
    )
    tk.Spinbox(clock_window, from_=0, to=59, textvariable=minute_var, width=5).grid(
        row=1, column=1
    )
    tk.Spinbox(clock_window, from_=0, to=59, textvariable=second_var, width=5).grid(
        row=1, column=2
    )

    select_button = tk.Button(clock_window, text="Select", command=select_time)
    select_button.grid(row=2, column=0, columnspan=3, pady=10)


def add_task():
    title = task_title_entry.get()
    description = task_description_entry.get()
    due_date = f"{selected_date.get()} {selected_time.get()}"
    priority = priority_var.get()
    category = category_var.get()

    if category == "Other":
        category = other_category_entry.get()

    if title and selected_date.get() and selected_time.get():
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "category": category,
            "completed": False,
        }
        tasks.append(task)
        update_task_list()
        save_tasks()
        task_title_entry.delete(0, tk.END)
        task_description_entry.delete(0, tk.END)
        other_category_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please input")


def delete_task():
    selected_item = task_tree.selection()
    if selected_item:
        index = task_tree.index(selected_item[0])
        tasks.pop(index)
        update_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")


def complete_task():
    selected_item = task_tree.selection()
    if selected_item:
        index = task_tree.index(selected_item[0])
        tasks[index]["completed"] = True
        update_task_list()
        save_tasks()
    else:
        messagebox.showwarning(
            "Selection Error", "Please select a task to mark as completed."
        )


def update_task_list(sorted_tasks=None):
    for item in task_tree.get_children():
        task_tree.delete(item)

    if not sorted_tasks:
        sorted_tasks = tasks

    for task in sorted_tasks:
        status = "Done" if task["completed"] else "Pending"
        task_tree.insert(
            "",
            tk.END,
            values=(
                task["title"],
                task["description"],
                task["due_date"],
                task["priority"],
                task["category"],
                status,
            ),
        )


def search_tasks():
    query = search_entry.get().lower()
    for item in task_tree.get_children():
        task_tree.delete(item)

    for task in tasks:
        if query in task["title"].lower() or query in task["description"].lower():
            status = "Done" if task["completed"] else "Pending"
            task_tree.insert(
                "",
                tk.END,
                values=(
                    task["title"],
                    task["description"],
                    task["due_date"],
                    task["priority"],
                    task["category"],
                    status,
                ),
            )


def open_add_task_window():
    main_menu.destroy()
    global root
    root = tk.Tk()
    root.title("Add Task")
    root.geometry("400x280")
    root.config(background="#0b545d")

    def go_back():
        root.destroy()
        open_main_menu()

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    input_frame.config(bg="#0b545d")

    task_title_label = tk.Label(
        input_frame, text="Task Title", bg="#0b545d", fg="white"
    )
    task_title_label.grid(row=0, column=0)

    global task_title_entry
    task_title_entry = tk.Entry(input_frame, width=35, bg="#eff1e4")
    task_title_entry.grid(row=0, column=1, padx=10)

    task_description_label = tk.Label(
        input_frame, text="Description", bg="#0b545d", fg="white"
    )
    task_description_label.grid(row=1, column=0)
    global task_description_entry
    task_description_entry = tk.Entry(input_frame, width=35, bg="#eff1e4")
    task_description_entry.grid(row=1, column=1, padx=10)

    calendar_button = tk.Button(
        input_frame, text="Select Date", command=open_calendar, bg="#0b545d", fg="white"
    )
    calendar_button.grid(row=2, column=0)
    global selected_date
    selected_date = tk.StringVar()
    selected_date_label = tk.Label(
        input_frame,
        textvariable=selected_date,
        width=30,
        anchor="w",
        relief="sunken",
        bg="#eff1e4",
    )
    selected_date_label.grid(row=2, column=1, padx=10)

    time_button = tk.Button(
        input_frame, text="Select Time", command=open_clock, bg="#0b545d", fg="white"
    )
    time_button.grid(row=3, column=0)
    global selected_time
    selected_time = tk.StringVar()
    selected_time_label = tk.Label(
        input_frame,
        textvariable=selected_time,
        width=30,
        anchor="w",
        bg="#eff1e4",
        relief="sunken",
    )
    selected_time_label.grid(row=3, column=1, padx=10)

    priority_label = tk.Label(input_frame, text="Priority", bg="#0b545d", fg="white")
    priority_label.grid(row=4, column=0)
    priority_frame = tk.Frame(input_frame, bg="#0b545d")
    priority_frame.grid(row=4, column=1, padx=10)

    global priority_var
    priority_var = tk.StringVar(value="Normal")
    priority_dropdown = tk.OptionMenu(
        input_frame, priority_var, "Low", "Normal", "High"
    )
    priority_dropdown.config(
        bg="#eff1e4", fg="black", highlightthickness=0, relief="flat"
    )
    priority_dropdown.grid(row=4, column=1, padx=10)

    priority_menu = priority_dropdown["menu"]
    priority_menu.config(bg="lightpink")

    category_label = tk.Label(input_frame, text="Category", bg="#0b545d", fg="white")
    category_label.grid(row=5, column=0)
    global category_var
    category_var = tk.StringVar(value="General")
    category_dropdown = tk.OptionMenu(
        input_frame, category_var, "Work", "Personal", "Other"
    )
    category_dropdown.config(
        bg="#eff1e4", fg="black", highlightthickness=0, relief="flat"
    )
    category_dropdown.grid(row=5, column=1, padx=10, pady=10)

    category_menu = category_dropdown["menu"]
    category_menu.config(bg="lightpink")

    global other_category_entry
    other_category_entry = tk.Entry(input_frame, width=30)
    other_category_entry.grid(row=6, column=1, padx=10)
    other_category_entry.grid_remove()

    def on_category_change(*args):
        if category_var.get() == "Other":
            other_category_entry.grid()
        else:
            other_category_entry.grid_remove()

    category_var.trace("w", on_category_change)

    add_button = tk.Button(
        input_frame, text="Add Task", command=add_task, bg="lightpink", fg="black"
    )
    add_button.grid(row=7, column=0, columnspan=2, pady=10)

    go_back_button = tk.Button(
        root, text="Go Back", command=go_back, bg="#eff1e4", fg="black"
    )
    go_back_button.pack(padx=10)

    root.mainloop()

#view task
def open_view_tasks_window():
    main_menu.destroy()
    global root
    root = tk.Tk()
    root.title("View Tasks")
    root.geometry("900x480")
    root.config(background="#283747")

    def go_back():
        root.destroy()
        open_main_menu()

    list_frame = tk.Frame(root)
    list_frame.pack(pady=10)

    global task_tree
    task_tree = ttk.Treeview(
        list_frame,
        columns=("Title", "Description", "Due Date", "Priority", "Category", "Status"),
        show="headings",
        height=15,
    )
    task_tree.pack(side=tk.LEFT, fill=tk.BOTH)

    for col in ("Title", "Description", "Due Date", "Priority", "Category", "Status"):
        task_tree.heading(
            col, text=col, command=lambda _col=col: sort_column(_col, False)
        )
        task_tree.column(col, width=150)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    task_tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_tree.yview)

    action_frame = tk.Frame(root)
    action_frame.config(bg="#283747")
    action_frame.pack(pady=10)

    complete_button = tk.Button(
        action_frame,
        text="Mark as Completed",
        command=complete_task,
        bg="Green",
        fg="white",
    )
    complete_button.grid(row=0, column=0, padx=10)

    delete_button = tk.Button(
        action_frame, text="Delete Task", command=delete_task, bg="Red", fg="black"
    )
    delete_button.grid(row=0, column=1, padx=10)

    global search_entry
    search_entry = tk.Entry(action_frame, width=34, bg="#f7dc6f")
    search_entry.grid(row=1, column=0, columnspan=2, pady=10)

    search_button = tk.Button(
        action_frame, text="Search", bg="#2c3e50", fg="white", command=search_tasks
    )
    search_button.grid(row=1, column=2, padx=10)

    go_back_button = tk.Button(
        root, text="Go Back", command=go_back, bg="lightblue", fg="black"
    )
    go_back_button.pack(pady=10)

    update_task_list()
    root.mainloop()


def sort_column(col, reverse):
    update_task_list(sort_by=col.lower().replace(" ", "_"), reverse=reverse)


def sort_column(col, reverse):
    if col == "Priority":
        priority_order = {"Low": 0, "Normal": 1, "High": 2}
        sorted_tasks = sorted(
            tasks, key=lambda x: priority_order[x["priority"]], reverse=reverse
        )
    elif col == "Due Date":
        sorted_tasks = sorted(
            tasks,
            key=lambda x: datetime.strptime(x["due_date"], "%Y-%m-%d %H:%M:%S"),
            reverse=reverse,
        )
    else:
        sorted_tasks = sorted(
            tasks, key=lambda x: x[col.lower().replace(" ", "_")], reverse=reverse
        )

    update_task_list(sorted_tasks=sorted_tasks)

#main
def open_main_menu():
    global main_menu
    main_menu = tk.Tk()
    main_menu.title("To-Do List App")
    main_menu.geometry("400x300")
    main_menu.config(background="#1abc9c")

    label = tk.Label(
        main_menu,
        text="A goal without an action plan is a daydream.\n\t\t~ Nathaniel Branden",
        font=("Helvetica", 14),
        wraplength=350,
        bg="#1abc9c",
        fg="white",
    )
    label.pack(pady=20)

    add_task_button = tk.Button(
        main_menu,
        text="Input a Task",
        width=20,
        command=open_add_task_window,
        bg="lightgreen",
    )
    add_task_button.pack(pady=10)

    view_tasks_button = tk.Button(
        main_menu,
        text="See Tasks",
        width=20,
        command=open_view_tasks_window,
        bg="lightgreen",
    )
    view_tasks_button.pack(pady=10)

    exit_button = tk.Button(
        main_menu,
        text="Exit",
        width=10,
        command=main_menu.destroy,
        bg="red",
        fg="white",
    )
    exit_button.pack(pady=20)

    main_menu.mainloop()


load_tasks()
open_main_menu()
