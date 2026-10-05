
print("This is a secure access checker program!")

is_banned = input("Are you banned? yes/no: ")
is_admin = input("Are you a admin? yes/no: ")
is_adult = int(input("Please enter your age: "))
has_ticket = input("Dou you have a ticket? yes/no: ")

if is_banned == "no" and (is_admin == "yes" or (is_adult >= 18 and has_ticket == "yes")):
    print("Access granted!")
else:
    print("Access denied!")