
print("This is an access checker program!")

age = int(input("Please enter your age: "))
has_ticket = input("Has ticket? yes/no: ")

if age >= 18 and has_ticket == "yes":
    print("Access granted!")
else:
    print("Access denied!")