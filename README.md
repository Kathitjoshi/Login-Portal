# Modern Login Portal

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-1.0-orange.svg)
![Security](https://img.shields.io/badge/Security-SHA256-red.svg)

A modern, secure user authentication system built with Python and Tkinter, featuring a sleek dark theme UI with account lockout protection and session management.

## 🌟 Features

### 🔐 Security Features
- **Password Hashing**: SHA-256 encryption for secure authentication
- **Account Lockout**: Protection against brute force attacks (3 failed attempts)
- **Session Management**: User session tracking and last login timestamps
- **Secure Authentication**: Hashed password verification
- **Login Attempt Tracking**: Monitors and restricts failed login attempts

### 🎨 User Interface
- **Modern Dark Theme**: Professional dark UI with smooth animations
- **Responsive Design**: Clean, centered layout with proper spacing
- **Interactive Elements**: Hover effects and visual feedback
- **Status Messages**: Real-time login status and error messages
- **Remember Me**: Session persistence option
- **Keyboard Support**: Enter key login functionality

### 🔑 Authentication Features
- **User Login System**: Secure username/password authentication
- **Password Recovery**: Forgot password functionality (demo mode)
- **Account Management**: User profile and session information
- **Demo Credentials**: Built-in admin account for testing

## 📋 Requirements

- Python 3.6 or higher
- Tkinter (usually comes with Python)
- JSON support (built-in)
- Hashlib (built-in)
- DateTime (built-in)

## 🚀 Installation

1. **Download the login module:**
   ```bash
   # Save Module2_PythonProject.py to your desired directory
   ```

2. **Ensure Python is installed:**
   ```bash
   python --version
   ```

3. **No additional dependencies required** - uses only Python standard library

## 💻 Usage

### Running the Login Portal
```bash
python Module2_PythonProject.py
```

### Demo Credentials
- **Username**: `admin`
- **Password**: `password`

### Login Process
1. **Enter Username** (existing registered username)
2. **Enter Password** (corresponding password)
3. **Optional**: Check "Remember me" for session persistence
4. **Click "SIGN IN"** to authenticate
5. **Alternative**: Press Enter key to login



## 🔧 Configuration

### Color Scheme
```python
colors = {
    'bg': '#1a1a2e',           # Background
    'card': '#16213e',         # Card/Form background
    'accent': '#0f4c75',       # Input fields
    'button': '#3282b8',       # Primary buttons
    'button_hover': '#4a90c2',  # Button hover state
    'text': '#ffffff',         # Primary text
    'text_secondary': '#a0a0a0', # Secondary text
    'error': '#e74c3c',        # Error messages
    'success': '#27ae60',      # Success messages
    'warning': '#f39c12'       # Warning messages
}
```

### Security Settings
- **Maximum Login Attempts**: 3 (configurable via `max_attempts`)
- **Account Lockout**: Automatic after max attempts exceeded
- **Password Hashing**: SHA-256 algorithm
- **Session Tracking**: Last login timestamp recording

## 💾 Data Storage

User data structure in `users.json`:

```json
{
  "admin": {
    "email": "admin@example.com",
    "password": "hashed_password_string",
    "created_at": "2024-01-01T12:00:00.000000",
    "last_login": "2024-01-01T12:30:00.000000"
  }
}
```

## 🛡️ Security Features

### ✅ Current Security Measures
- **Brute Force Protection**: Account lockout after 3 failed attempts
- **Password Hashing**: SHA-256 secure password storage
- **Session Management**: Login timestamp tracking
- **Input Validation**: Basic username/password validation
- **Account Status Tracking**: Monitors login attempts per user

### 🔒 Authentication Flow
1. **Input Validation**: Checks for empty fields
2. **Account Status Check**: Verifies account isn't locked
3. **User Existence**: Confirms username exists
4. **Password Verification**: Compares hashed passwords
5. **Success Actions**: Updates last login, shows user info
6. **Failure Actions**: Increments attempt counter, shows warnings

### ⚠️ Security Limitations
Current implementation is suitable for demo/educational purposes. For production:
- **Use bcrypt/scrypt** instead of SHA-256
- **Implement rate limiting** beyond simple attempt counting
- **Add CAPTCHA** after failed attempts
- **Use database storage** instead of JSON files
- **Implement proper session tokens**
- **Add audit logging**

## 🎨 UI Components

### Form Elements
- **Username Input**: Clean, modern text field
- **Password Input**: Masked password entry
- **Remember Me Checkbox**: Session persistence option
- **Sign In Button**: Primary authentication action
- **Forgot Password Link**: Password recovery option

### Interactive Features
- **Hover Effects**: Button color changes on mouse over
- **Focus Effects**: Input field highlighting
- **Status Messages**: Real-time feedback with auto-hide
- **Keyboard Navigation**: Enter key support
- **Visual Feedback**: Success/error message coloring

## 🚀 Functionality

### Authentication Process
```python
def handle_login(self):
    # Input validation
    # Account lockout check
    # User verification
    # Password comparison
    # Success/failure handling
    # Session updates
```

### Password Recovery
- **Username-based recovery**: Enter username first
- **Email notification**: Shows registered email (demo)
- **Security consideration**: Doesn't reveal if username exists

### Account Lockout
- **Attempt Tracking**: Monitors failed logins per username
- **Automatic Lockout**: Triggers after max attempts
- **Security Message**: Informs user of lockout status
- **Reset Mechanism**: Successful login resets attempt counter

## 🛠️ Customization

### Changing Window Size
```python
self.root.geometry("450x550")  # width x height
```

### Modifying Max Attempts
```python
self.max_attempts = 5  # Change from default 3
```

### Updating Colors
```python
self.colors['button'] = '#your_preferred_color'
```

### Adding New Users Programmatically
```python
self.users['newuser'] = {
    'email': 'user@example.com',
    'password': self.hash_password('userpassword'),
    'created_at': datetime.now().isoformat(),
    'last_login': None
}
```

## 🐛 Troubleshooting

### Common Issues

1. **"users.json not found"**
   - File auto-generates with default admin account
   - Check directory write permissions

2. **Admin login not working**
   - Verify credentials: admin/password
   - Check if users.json was corrupted

3. **Account immediately locked**
   - Delete users.json to reset attempt counters
   - Or manually edit the file to remove attempt tracking

4. **Window positioning issues**
   - Modify center_window() for multi-monitor setups
   - Adjust geometry parameters

### Debug Tips
```python
# Add debug prints to track login flow
print(f"Login attempt for: {username}")
print(f"Attempts so far: {self.login_attempts.get(username, 0)}")
print(f"User exists: {username in self.users}")
```

## 🔄 Integration

### With Signup Module
- Both modules use the same `users.json` format
- Users created in signup portal can login here
- Shared password hashing algorithm ensures compatibility

### Database Migration
For production use, replace JSON storage:
```python
# Replace file operations with database queries
# Use SQLite, PostgreSQL, or other database systems
# Implement proper connection pooling and error handling
```

## 🚀 Future Enhancements

- **Multi-factor authentication (MFA)**
- **OAuth integration** (Google, Facebook, etc.)
- **Session token management**
- **Password reset via email**
- **Account recovery questions**
- **Login history tracking**
- **Device fingerprinting**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/login-enhancement`)
3. Commit your changes (`git commit -am 'Add new login feature'`)
4. Push to the branch (`git push origin feature/login-enhancement`)
5. Create a Pull Request

## 👨‍💻 Author

Modern Login Portal - Secure authentication made simple.

## 🙏 Acknowledgments

- Python Tkinter documentation
- Authentication security best practices
- Modern UI design principles

---

**⭐ If you find this login portal helpful, please consider giving it a star!**
