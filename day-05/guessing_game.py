

print("This is a guessing game program!")

secret_number = 7

# Basic:
#while True:
#    user_number = int(input("Please enter a number: "))

#    if user_number > secret_number:
#        print("Too high")
#    elif user_number < secret_number:
#        print("Too low")
#    else:
#        print("Correct!")
#        break

# Improved with attempts:

max_attempts = 5
user_attempts = 1

while user_attempts <= max_attempts:
    user_number = int(input("Please enter a number: "))

    if user_attempts == max_attempts and user_number != secret_number:
        print("Game over!")
        break
    elif user_number > secret_number:
        print("Too high")
        print(f"You have {max_attempts - user_attempts} tries left!")
    elif user_number < secret_number:
        print("Too low")
        print(f"You have {max_attempts - user_attempts} tries left!")
    else:
        print("Correct, you found the secret number!")

    user_attempts += 1