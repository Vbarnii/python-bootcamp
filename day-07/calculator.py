

print("================================")
print("      PYTHON CALCULATOR v2")
print("================================")


while True:
    
    print("================================")
    print("1 - Addition ")
    print("2 - Subtraction ")
    print("3 - Multiplication ")
    print("4 - Division ")
    print("5 - Floor division ")
    print("6 - Modulo ")
    print("7 - Power ")
    print("0 - Exit ")
    print("================================")

    choice = input("Choose one of the points above: ")

    if choice == "0":
        break
    elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":
        
        first_number = float(input("First number: "))
        second_number = float(input("Second number: "))
        
        if choice == "1":
            
            result = (first_number + second_number)
            print(f"The result: {result} ")
        if choice == "2":
                    
            result = (first_number - second_number)
            print(f"The result: {result} ")
        if choice == "3":
                    
            result = (first_number * second_number)
            print(f"The result: {result} ")
        if choice == "4":
                    
            result = (first_number / second_number)
            print(f"The result: {result} ")
        if choice == "5":
                    
            result = (first_number // second_number)
            print(f"The result: {result} ")
        if choice == "6":
                    
            result = (first_number % second_number)
            print(f"The result: {result} ")
        if choice == "7":
                    
            result = (first_number ** second_number)
            print(f"The result: {result} ")

    else:
        print("Invalid operation. Please try again.")