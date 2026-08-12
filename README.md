# password_login_system
A beginner-friendly Python login system that allows up to three password attempts. It demonstrates while loops, conditional statements, counters, user input, and break statements to control program flow.
# Python Password Login System

## 📌 Overview

The **Python Password Login System** is a beginner-friendly program that allows a user to enter a password and provides a maximum of three attempts to log in successfully.

If the correct password is entered, the login is successful. After three incorrect attempts, the password is locked.

## ✨ Features

- Password verification
- Maximum of 3 login attempts
- Displays login success or failure
- Locks the password after 3 failed attempts
- Uses a counter to track attempts

## 🛠️ Concepts Practiced

- `while` loop
- `if-else` statements
- `input()`
- Variables
- Comparison operators
- Counters
- `break` statement
- Conditional decision-making

## 💻 Source Code

```python
attempts = 1

while attempts <= 3:
    password = input("Enter your password: ")

    if password == "python123":
        print("Login successful")
        break
    else:
        print("Login failed")
        attempts += 1

if attempts > 3:
    print("Password locked")
```

## ▶️ Example

### Successful Login

```text
Enter your password: python123
Login successful
```

### Failed Login

```text
Enter your password: hello
Login failed

Enter your password: abc123
Login failed

Enter your password: test
Login failed
Password locked
```

## 📂 Project Structure

```text
Python-Password-Login-System/
│
├── password_login_system.py
└── README.md
```

## 🎯 Learning Objective

This project helps beginners understand how `while` loops, counters, conditional statements, and `break` can work together to create a simple login system.

---

⭐ Part of my Python learning journey and beginner programming practice.
