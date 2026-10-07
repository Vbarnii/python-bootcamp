
print("This is a grade checker program!")

grade = int(input("Please enter your score in order to get your current grade! "))

if grade < 60:
    print("F")
elif grade < 70:
    print("D")
elif grade < 80:
    print("C")
elif grade < 90:
    print("B")
else:
    print("A")