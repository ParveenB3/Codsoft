---
### 1. To-Do List Application

#### Description
A GUI-based application to manage tasks efficiently. Built using the tkinter library.

#### Features:
- **Add Task:** Input a title, description, due date, time, priority (Low, Normal, High), and category (Work, Personal, or custom).
-**View Tasks:** Display tasks in a tabular format with the following columns:
 -Title
 -Description
 -Due Date & Time
 -Priority
 -Category
 -Status (Pending or Completed)
-Delete Task: Remove a task from the list.
-Mark as Completed: Update the status of a task.
-Search Tasks: Search by title or description.
-**Exit**

#### **Skills Learned**  
- **Programming**  
- Python basics and functions.  
- Data structures (lists, dictionaries).  
- File handling (JSON).  
- Error handling.  
- **GUI Development**  
- Tkinter widgets (`Button`, `Entry`, `Treeview`).  
- Event-driven programming.  
- Custom widgets (tkcalendar, spinboxes).  
- Dynamic UI updates.  
- **Data Management**  
- Task search, filter, and sorting.  
- Status management (Pending/Completed).  
- **Project Skills**  
- Problem-solving and modular coding.  
- Data persistence with JSON.  
- User-friendly interface design.  
  
#### How to Use:
-Run the Python script.
**Main menu options:**
-Input a Task: Open a window to add a new task.
-See Tasks: View all tasks in a table with options to delete, search, or mark as completed.
-Exit: Close the application.

#### Technologies Used:
-Tkinter: For GUI.
-tkcalendar: For date selection.
-JSON: For data persistence.
-Datetime: For handling dates and times.

---
### 2. Calculator

#### Description
A GUI-based calculator that performs basic arithmetic operations and additional functionalities such as percentage calculations, toggling positive/negative signs, and more.

#### Features
- Arithmetic operations: Addition, subtraction, multiplication, and division.
- Advanced functionalities: 
  - Percentage calculations (`%`).
  - Clear input (`C`) and delete last character (`Del`).
  - Toggle positive/negative signs (`+/-`).
- Clean and user-friendly interface.

#### Key Skills Learned
-Tkinter GUI Development: Learned to create a graphical user interface using the Tkinter library.
-Event Handling: Implemented button click events and associated functionality.
-Arithmetic Logic: Designed and implemented operations like addition, subtraction, multiplication, division, and percentages.
-Error Handling: Handled invalid inputs gracefully using message boxes.
-Responsive Design: Used grid_rowconfigure and grid_columnconfigure to ensure the calculator adapts to different window sizes.

---
### 3. Password Generator

#### Description
This program generates secure passwords based on the user's chosen strength and length.

#### Features:
- **Generate a Password**
  -Options:-Weak,Strong or Very Strong
  -Randomly generates passwords using uppercase, lowercase, numbers, and special characters.
  - copy password?
- **Generate Custom Password**
   - Enter the password length
      -include letters? -include numbers? -include specials?
      - copy password?
- **Save password to a file (ctrl+v)**
  -enter file name
- **Exit**

#### Key Skills learned
-Random Module Usage: Used Python's random module to generate secure passwords.
-String Manipulation: Utilized string methods to include letters, numbers, and special characters dynamically.
-Tkinter Dialogs: Worked with dialog boxes (messagebox, simpledialog) for user interactions.
-Clipboard Handling: Learned to copy text to the clipboard using the pyperclip library.
-Password Strength Evaluation: Developed logic to evaluate and classify password strength as weak, strong, or very strong.
-File Handling: Gained experience in saving data (passwords) to a file.
