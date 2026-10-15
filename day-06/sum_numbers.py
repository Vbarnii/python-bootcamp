

print("This is a program for summing numbers!")

user_number = int(input("Please enter a number: "))
total = 0

for number in range(1,user_number + 1):
    total += number

print(total)