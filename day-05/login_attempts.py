

print("This is a program to limit the login attempts! (login checker v3)")

current_username = "admin"
current_password = "python123"



max_attempts = 3
counter = 1

while counter <= max_attempts:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if counter == 3:
        print("Account locked!")
        break
    elif username == current_username and password == current_password:
        print("Access granted!")
        break
    else:
        print(f"Invalid credentials you have {max_attempts - counter} tries left!")
        
    counter += 1
