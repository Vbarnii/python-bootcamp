

print("This is a vowel counter program!")

user_text = input("Please enter a text here: ")
counter = 0 


for vowels in user_text:
    if vowels == "a" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u":
        counter += 1

print(f"Text: {user_text}")
print(f"Vowels: {counter}")
