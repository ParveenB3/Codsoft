import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def button_click(value):
    current = entry.get()

    if value == "C":
        entry.delete(0, tk.END)

    elif value == "Del":
        if current:
            entry.delete(len(current) - 1, tk.END)

    elif value == "%":
        try:
            if current and not current.endswith(("%", "+", "-", "*", "/", "x", "÷")):
                result = eval(current.replace("x", "*").replace("÷", "/") + "/100")
                entry.delete(0, tk.END)
                entry.insert(0, str(result))
            else:
                messagebox.showerror("Error", "Invalid use of '%'")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

    elif value == "+/-":
        try:
            if current:
                if current.startswith("-"):
                    entry.delete(0)
                else:
                    entry.insert(0, "-")
        except Exception:
            messagebox.showerror("Error", "Invalid Input")

    elif value == "=":
        try:
            result = eval(current.replace("x", "*").replace("÷", "/"))
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input")

    else:

        entry.insert(tk.END, value)


root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.configure(bg="#3d3d3d")
root.resizable(False, False)


entry = tk.Entry(
    root,
    font=("Helvetica", 16),
    justify="right",
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ("C", 1, 0),
    ("Del", 1, 1),
    ("%", 1, 2),
    ("÷", 1, 3),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("x", 2, 3),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("-", 3, 3),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("+", 4, 3),
    ("+/-", 5, 0),
    ("0", 5, 1),
    (".", 5, 2),
    ("=", 5, 3),
]


for text, row, col in buttons:
    btn = tk.Button(
        root,
        font=("Helvetica", 14),
        bg=(
            "#d7dbdd"
            if text not in ["=", "C", "÷", "x", "%", "-","+/-", "+", "Del"]
            else "orange"
        ),
        text=text,
        command=lambda t=text: button_click(t),
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.configure(bg="#f0f0f0")
root.mainloop()
