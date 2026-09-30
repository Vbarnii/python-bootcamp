
print("This is a circle calculator!")

radius = float(input("Please provide a number for the radius of the circle! "))

pi = 3.14159

diameter = (2 * radius)
circumference = (2 * pi * radius)
area = (pi * radius ** 2)

print(f"The dieameter of the circle is: {diameter}")
print(f"The circumference of the circle is: {circumference}")
print(f"The area of the circle is: {area}")