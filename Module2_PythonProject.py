import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password are correct (you can replace this with your own authentication logic)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Portal")

# Create and place widgets
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)

entry_username = tk.Entry(root)
entry_username.pack(pady=10)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")  # Show '*' for password
entry_password.pack(pady=10)

btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
