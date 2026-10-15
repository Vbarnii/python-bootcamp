

print("This is a program which shows the even numbers from 1 to 100!")

#range_max = 100
number = 1

# One solution with while loop:
#while number <= range_max:
#    if (number % 2 == 0):
#        print(number)
#    number += 1


# Another solution with for loop:

for number in range(0, 100, 2):
    print(number)