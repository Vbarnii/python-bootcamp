

print("This is a character counter program!")

user_text = input("Please enter a text here: ")
counter = 0

for character in user_text:
    counter += 1

print(f"The given text contains {counter} letters")
