

print("This is a factorial challenge program!")

user_input = int(input("Please enter a not negativ number: "))
result = 1

for number in range(1, user_input + 1):
    result *= number

print(f"{user_input}! = {result}")
