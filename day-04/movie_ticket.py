
print("This is a movie ticket program!")

age = int(input("Please enter your age: "))
is_student = input("Are you a student? yes/no: ")

if age >= 65 or is_student == "yes":
    print("This is a ticket with discount for students and seniors!")
elif age >= 18:
    print("This is an adult ticket!")
elif age >= 12:
    print("This is a teenager ticket!")
else: 
    print("This is a child ticket!")