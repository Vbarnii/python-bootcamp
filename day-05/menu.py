

print("This is a simple menu simulator program!")

menu_number_one = "Hello!"
menu_number_two = 42
menu_number_three = "Goodbye!"

while True:
    print("1 - Say hello")
    print("2 - Show number")
    print("3 - Quit")

    user_choice = int(input("Please enter a number in order to navigate in the menu: "))

    if user_choice == 1:
        print(menu_number_one)
    elif user_choice == 2:
        print(menu_number_two)
    else:
        print(menu_number_three)
        break
