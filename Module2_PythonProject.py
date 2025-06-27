import tkinter as tk
from tkinter import messagebox
import json
import os
import hashlib
from datetime import datetime

class ModernLoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modern Login Portal")
        self.root.geometry("450x550")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Initialize user data storage
        self.users_file = "users.json"
        self.load_users()
        
        # Login attempts tracking
        self.login_attempts = {}
        self.max_attempts = 3
        
        # Color scheme
        self.colors = {
            'bg': '#1a1a2e',
            'card': '#16213e',
            'accent': '#0f4c75',
            'button': '#3282b8',
            'button_hover': '#4a90c2',
            'text': '#ffffff',
            'text_secondary': '#a0a0a0',
            'error': '#e74c3c',
            'success': '#27ae60',
            'warning': '#f39c12'
        }
        
        self.create_ui()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.root.winfo_screenheight() // 2) - (550 // 2)
        self.root.geometry(f"450x550+{x}+{y}")
    
    def load_users(self):
        """Load existing users from JSON file"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r') as f:
                    self.users = json.load(f)
            else:
                # Default admin account for demo
                self.users = {
                    'admin': {
                        'email': 'admin@example.com',
                        'password': self.hash_password('password'),
                        'created_at': datetime.now().isoformat(),
                        'last_login': None
                    }
                }
                self.save_users()
        except:
            self.users = {
                'admin': {
                    'email': 'admin@example.com',
                    'password': self.hash_password('password'),
                    'created_at': datetime.now().isoformat(),
                    'last_login': None
                }
            }
    
    def save_users(self):
        """Save users to JSON file"""
        try:
            with open(self.users_file, 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            print(f"Failed to save user data: {str(e)}")
    
    def hash_password(self, password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_ui(self):
        """Create the user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        header_frame.pack(fill='x', pady=(0, 30))
        
        title = tk.Label(header_frame, text="Welcome Back",
                        font=('Segoe UI', 28, 'bold'),
                        fg=self.colors['text'],
                        bg=self.colors['bg'])
        title.pack()
        
        subtitle = tk.Label(header_frame, text="Sign in to your account",
                           font=('Segoe UI', 12),
                           fg=self.colors['text_secondary'],
                           bg=self.colors['bg'])
        subtitle.pack(pady=(5, 0))
        
        # Card frame
        card_frame = tk.Frame(main_frame, bg=self.colors['card'], relief='flat')
        card_frame.pack(fill='both', expand=True, pady=10)
        
        # Add subtle border effect
        border_frame = tk.Frame(card_frame, bg=self.colors['button'], height=3)
        border_frame.pack(fill='x')
        
        # Form container
        form_frame = tk.Frame(card_frame, bg=self.colors['card'])
        form_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Username field
        self.create_input_field(form_frame, "Username", "username_entry")
        
        # Password field
        self.create_input_field(form_frame, "Password", "password_entry", show="*")
        
        # Remember me checkbox
        self.remember_var = tk.BooleanVar()
        remember_frame = tk.Frame(form_frame, bg=self.colors['card'])
        remember_frame.pack(fill='x', pady=(10, 20))
        
        remember_check = tk.Checkbutton(remember_frame, text="Remember me",
                                       variable=self.remember_var,
                                       font=('Segoe UI', 9),
                                       fg=self.colors['text_secondary'],
                                       bg=self.colors['card'],
                                       selectcolor=self.colors['accent'],
                                       activebackground=self.colors['card'],
                                       activeforeground=self.colors['text'])
        remember_check.pack(side='left')
        
        # Forgot password link
        forgot_link = tk.Label(remember_frame, text="Forgot password?",
                              font=('Segoe UI', 9, 'underline'),
                              fg=self.colors['button'],
                              bg=self.colors['card'],
                              cursor='hand2')
        forgot_link.pack(side='right')
        forgot_link.bind('<Button-1>', lambda e: self.forgot_password())
        
        # Login button
        self.login_btn = tk.Button(form_frame, text="SIGN IN",
                                  font=('Segoe UI', 12, 'bold'),
                                  bg=self.colors['button'],
                                  fg=self.colors['text'],
                                  relief='flat',
                                  bd=0,
                                  padx=30,
                                  pady=12,
                                  cursor='hand2',
                                  command=self.handle_login)
        self.login_btn.pack(fill='x', pady=(10, 0))
        
        # Button hover effects
        self.login_btn.bind('<Enter>', lambda e: self.login_btn.config(bg=self.colors['button_hover']))
        self.login_btn.bind('<Leave>', lambda e: self.login_btn.config(bg=self.colors['button']))
        
        # Status label for messages
        self.status_label = tk.Label(form_frame, text="",
                                    font=('Segoe UI', 9),
                                    bg=self.colors['card'])
        self.status_label.pack(pady=(10, 0))
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        footer_frame.pack(fill='x', pady=(20, 0))
        
        footer_text = tk.Label(footer_frame, text="Don't have an account? ",
                              font=('Segoe UI', 10),
                              fg=self.colors['text_secondary'],
                              bg=self.colors['bg'])
        footer_text.pack(side='left')
        
        signup_link = tk.Label(footer_frame, text="Sign up here",
                              font=('Segoe UI', 10, 'underline'),
                              fg=self.colors['button'],
                              bg=self.colors['bg'],
                              cursor='hand2')
        signup_link.pack(side='left')
        signup_link.bind('<Button-1>', lambda e: messagebox.showinfo("Info", "Signup feature would be implemented in a separate module"))
        
        # Demo info
        demo_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        demo_frame.pack(fill='x', pady=(15, 0))
        
        demo_label = tk.Label(demo_frame, text="Demo Credentials: admin / password",
                             font=('Segoe UI', 9, 'italic'),
                             fg=self.colors['text_secondary'],
                             bg=self.colors['bg'])
        demo_label.pack()
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self.handle_login())
    
    def create_input_field(self, parent, label_text, attr_name, show=None):
        """Create a modern input field"""
        container = tk.Frame(parent, bg=self.colors['card'])
        container.pack(fill='x', pady=(0, 15))
        
        # Label
        label = tk.Label(container, text=label_text,
                        font=('Segoe UI', 10, 'bold'),
                        fg=self.colors['text'],
                        bg=self.colors['card'])
        label.pack(anchor='w', pady=(0, 5))
        
        # Entry field
        entry = tk.Entry(container,
                        font=('Segoe UI', 11),
                        bg=self.colors['accent'],
                        fg=self.colors['text'],
                        relief='flat',
                        bd=5,
                        show=show)
        entry.pack(fill='x', ipady=8)
        
        # Store reference to entry
        setattr(self, attr_name, entry)
        
        # Add focus effects
        entry.bind('<FocusIn>', lambda e: entry.config(bg='#1e3a5f'))
        entry.bind('<FocusOut>', lambda e: entry.config(bg=self.colors['accent']))
        
        return entry
    
    def show_status(self, message, color):
        """Show status message"""
        self.status_label.config(text=message, fg=color)
        self.root.after(3000, lambda: self.status_label.config(text=""))
    
    def forgot_password(self):
        """Handle forgot password"""
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showwarning("Info", "Please enter your username first, then click 'Forgot password?'")
            return
        
        if username in self.users:
            email = self.users[username].get('email', 'No email on file')
            messagebox.showinfo("Password Reset", 
                               f"Password reset instructions would be sent to:\n{email}\n\n"
                               f"(This is a demo - no actual email will be sent)")
        else:
            messagebox.showerror("Error", "Username not found!")
    
    def handle_login(self):
        """Handle login form submission"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        # Basic validation
        if not username or not password:
            self.show_status("Please enter both username and password!", self.colors['error'])
            return
        
        # Check login attempts
        if username in self.login_attempts and self.login_attempts[username] >= self.max_attempts:
            self.show_status(f"Account locked due to too many failed attempts!", self.colors['error'])
            messagebox.showerror("Account Locked", 
                               f"Too many failed login attempts for '{username}'.\n"
                               f"Account is temporarily locked for security.")
            return
        
        # Verify credentials
        if username in self.users:
            stored_password = self.users[username]['password']
            if stored_password == self.hash_password(password):
                # Successful login
                self.login_attempts[username] = 0  # Reset attempts
                
                # Update last login
                self.users[username]['last_login'] = datetime.now().isoformat()
                self.save_users()
                
                self.show_status("Login successful!", self.colors['success'])
                
                # Show success message with user info
                last_login = self.users[username].get('last_login')
                if last_login and last_login != datetime.now().isoformat():
                    try:
                        last_login_date = datetime.fromisoformat(last_login).strftime("%Y-%m-%d %H:%M:%S")
                        login_info = f"Last login: {last_login_date}"
                    except:
                        login_info = "Welcome back!"
                else:
                    login_info = "First time login!"
                
                messagebox.showinfo("Login Successful", 
                                   f"Welcome, {username}!\n\n"
                                   f"Email: {self.users[username].get('email', 'N/A')}\n"
                                   f"{login_info}")
                
                # Clear form on successful login
                self.clear_form()
                
                # Here you would typically open the main application window
                # For demo purposes, we'll just show a success message
                
            else:
                # Failed login
                self.login_attempts[username] = self.login_attempts.get(username, 0) + 1
                remaining = self.max_attempts - self.login_attempts[username]
                
                if remaining > 0:
                    self.show_status(f"Invalid password! {remaining} attempts remaining.", self.colors['error'])
                else:
                    self.show_status("Account locked due to too many failed attempts!", self.colors['error'])
                    messagebox.showerror("Account Locked", 
                                       f"Account '{username}' has been locked due to multiple failed login attempts.")
        else:
            # Username not found
            self.show_status("Username not found!", self.colors['error'])
            self.login_attempts[username] = self.login_attempts.get(username, 0) + 1
    
    def clear_form(self):
        """Clear all form fields"""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.remember_var.set(False)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernLoginApp()
    app.run()
