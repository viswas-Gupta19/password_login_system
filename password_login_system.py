# Python Password Login System

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
