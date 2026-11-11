

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
    print("8 - Last Record ")
    print("0 - Exit ")
    print("================================")

    choice = input("Choose one of the points above: ")
    lastRecord = 0

    if choice == "0":
        break
    elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":
        
        first_number = float(input("First number: "))
        second_number = float(input("Second number: "))
        
        
        if choice == "1":
            
            result = (first_number + second_number)
            print(f"The result: {result} ")
        elif choice == "2":
                    
            result = (first_number - second_number)
            print(f"The result: {result} ")
        elif choice == "3":
                    
            result = (first_number * second_number)
            print(f"The result: {result} ")
        elif choice == "4":
            if second_number != 0:
                result = (first_number / second_number)
                print(f"The result: {result} ")
            else:
                print("Cannot divide by zero. ")
        elif choice == "5":
            if second_number != 0:
                result = (first_number // second_number)
                print(f"The result: {result} ")
            else:
                print("Cannot divide by zero. ")
        elif choice == "6":
            if second_number != 0:
                result = (first_number % second_number)
                print(f"The result: {result} ")
            else:
                print("Cannot mod by zero. ")
        elif choice == "7":
            if first_number != 0 and second_number != (-1):
                result = (first_number ** second_number)
                print(f"The result: {result} ")
            else:
                print("Invalid operation. Please try again. ")
    elif choice == "8":
        if lastRecord == 0:
            print("There was no last record")
        else:
            lastRecord = result
            print(f"The last record was: {lastRecord}")

    else:
        print("Invalid operation. Please try again.")