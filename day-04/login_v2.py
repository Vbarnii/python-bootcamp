
print("This is a login checker program! (Version 2)")

current_username = "admin"
current_password = "python123"

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == current_username and password == current_password:
    print("Access granted!")
else:
    print("Invalid credentials!")
