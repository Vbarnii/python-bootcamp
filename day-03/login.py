
print("This is a login checker program!")

current_username = "admin"
current_password = "python123"

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == current_username:
    if password == current_password:
        print("Acces granted!")
    else:
        print("Wrong password!")
else:
    print("Unknown user")


