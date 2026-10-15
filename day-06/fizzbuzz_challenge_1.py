

print("This is a FizzBuzz challenge program!")

min_value = 1
max_value = 100

for i in range(min_value, max_value + 1):
    if (i % 5 == 0 and i % 3 == 0):
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
