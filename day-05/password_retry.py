

print("This is a password checker program with while loop!")

correct_password = "python123"

#password = input("Please enter your password: ")

#while password != correct_password:
#    print("Your password is incorrect!")
#    password = input("Please enter your password: ")

#print("Access granted!")

while True:
    password = input("Please enter your password: ")
    print("Your password is incorrect!")

    if password == correct_password:
        break

print("Access granted!")