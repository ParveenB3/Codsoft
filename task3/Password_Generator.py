import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import string
import random
import pyperclip


def generate_password(length, characters):
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def generate_custom_password():
    try:
        length = int(simpledialog.askstring("Input", "Enter the password length: "))
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return None
        include_letters = messagebox.askyesno("Question", "Include letters? (y/n):")
        include_numbers = messagebox.askyesno("Question", "Include numbers? (y/n): ")
        include_special = messagebox.askyesno("Question", "Include symbols? (y/n): ")
        characters = ""
        if include_letters:
            characters = string.ascii_uppercase + string.ascii_lowercase + characters
        if include_numbers:
            characters = string.digits + characters
        if include_special:
            characters = string.punctuation + characters
        if not characters:
            messagebox.showerror(
                "Error",
                "No character set selected\nPlease select atleast one character.",
            )
            return None
        password = "".join(random.choice(characters) for _ in range(length))
        return password
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
        return None


def check_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Very Strong"
    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_special):
        return "Strong"
    else:
        return "Weak"


def save_password_to_file():
    password = simpledialog.askstring("Input", "Enter the password to save\n(ctrl+V): ")
    file_name = simpledialog.askstring("Input", "Enter the file name (i.e., abc.txt): ")
    try:
        with open(file_name, "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Success", f"Password saved to {file_name}  successfully!")
    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occured while saving the password: {e}"
        )


def copy_to_clipboard(password):
    try:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard")
    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occured while copying the clipboard: {e}"
        )


def main():
    while True:
        try:
            choice = int(
                simpledialog.askstring(
                    "Password Generator",
                    "1. Generate a Password\n2. Generate Custom Password\n3. Save password to File\n4. Exit \n Enter your choice: ",
                )
            )
            if choice == 1:
                try:
                    sub_choice = int(
                        simpledialog.askstring(
                            "Input",
                            "\nSelect the password type you want?\n1. Weak (only letters)\n2. Strong (letters and numbers)\n3. very strong (letters, numbers and special characters)",
                        )
                    )
                    length = 12
                    if sub_choice not in [1, 2, 3]:
                        messagebox.showerror(
                            "Error", "Invalid choice. Please select 1,2 or 3."
                        )
                        continue
                    messagebox.showinfo("Info", f"Length of the password is {length}")
                    if sub_choice == 1:
                        characters = string.ascii_lowercase
                        password_type = "Weak"
                    elif sub_choice == 2:
                        characters = (
                            string.ascii_uppercase
                            + string.ascii_lowercase
                            + string.digits
                        )
                        password_type = "Strong"
                    else:
                        characters = (
                            string.ascii_uppercase
                            + string.ascii_lowercase
                            + string.digits
                            + string.punctuation
                        )
                        password_type = "Very Strong"
                    password = generate_password(length, characters)
                    messagebox.showinfo(
                        "Password", f"Your {password_type} password is: {password}"
                    )
                    include_password = messagebox.askyesno(
                        "Question", "Want to Copy the Password ? (y/n): "
                    )
                    if include_password:
                        pyperclip.copy(password)
                        messagebox.showinfo("Success", "Password copied to clipboard")
                    if not include_password:
                        continue
                except (ValueError, TypeError):
                    messagebox.showerror(
                        "Error", "Invalid choice. Please select 1,2 or 3."
                    )
                    continue

            elif choice == 2:
                password = generate_custom_password()
                if password:
                    messagebox.showinfo(
                        "Password", f"Your Custom password is: {password} "
                    )
                    messagebox.showinfo(
                        "Strength",
                        f"Strength of Password is: {check_strength(password)}",
                    )
                    include_password = messagebox.askyesno(
                        "Question", "Want to Copy the Password ? (y/n): "
                    )
                    if include_password:
                        pyperclip.copy(password)
                        messagebox.showinfo("Success", "Password copied to clipboard")
                    if not include_password:
                        continue

            elif choice == 3:
                save_password_to_file()
            elif choice == 4:
                messagebox.showinfo(
                    "Exiting", "Exiting Password Generator...\n\tSee you soon\t"
                )
                break
            else:
                messagebox.showerror("Error", "Invalid Choice! Please try again.")
        except ValueError:
            messagebox.showerror(
                "Error", "Invalid input! Please enter a number between 1 to 5."
            )


if __name__ == "__main__":
    main()
