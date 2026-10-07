

print("This is a bmi calculator program!")

weight = float(input("Please enter your current weight in kg: "))
height = float(input("Please enter your current height in m: "))

bmi = (weight / (height ** 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")