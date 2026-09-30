
print("This is a time converter program!")

total_seconds = int(input("Please enter an integer number in seconds! "))

one_hour_in_seconds = 3600
one_minute_in_seconds = 60

hours = (total_seconds // one_hour_in_seconds) 
minutes = ((total_seconds - one_hour_in_seconds) % one_minute_in_seconds)
seconds = (((total_seconds -  one_hour_in_seconds) - minutes * one_minute_in_seconds) % 60)

print(f"The entered value is: {hours} hour(s) {minutes} minute(s) {seconds} second(s)")