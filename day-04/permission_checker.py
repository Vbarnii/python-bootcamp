
print("This is a permission checker program!")

is_admin = input("Are you a admin? yes/no: ")
is_moderator = input("Are you a moderator? yes/no: ")
is_banned = input("Are you banned? yes/no: ")

if (is_admin == "yes" or is_moderator == "yes") and is_banned == "no":
    print("Permission granted!")
else:
    print("Permission denied!")