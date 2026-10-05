
print("This is a working hours checker program!")

working_hours = int(input("Please enter a time value in hours: "))

if 8 <= working_hours < 18:
    print("The system is open!")
else:
    print("The system is closed!")