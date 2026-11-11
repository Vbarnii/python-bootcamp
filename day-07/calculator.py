

print("================================")
print("      PYTHON CALCULATOR v2")
print("================================")

result = 0
lastRecord = 0
calculation_count = 0
lastResult = ""

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
    
    
    

    if choice == "0":
        if calculation_count == 0:
            print("There was no  successful operation!")
        else:
            print(f"The number of successful operations: {calculation_count}")
        break
    elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":
        lastResult = input("Do you want to use the last result as the first number? (Yes/No) ")
        if lastResult == "Yes" and lastRecord != 0:
            first_number = lastRecord
            print(f"The previous result as the first number: {lastRecord}")
            second_number = float(input("Second number: "))
        elif lastResult == "No" and lastRecord != 0:
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))
        else:
            print("There was no previous operation! Please continue with the following: ")
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))
        
        
        if choice == "1":
            if lastResult == "Yes" and lastRecord != 0:
                result = (lastRecord + second_number)
                print(f"The result: {result} ")
            else:
                result = (first_number + second_number)
                print(f"The result: {result} ")
            calculation_count += 1
            
        elif choice == "2":
            if lastResult == "Yes" and lastRecord != 0:
                result = (lastRecord - second_number)
                print(f"The result: {result} ")
            else:
                result = (first_number - second_number)
                print(f"The result: {result} ")
            calculation_count += 1
    
        elif choice == "3":
            if lastResult == "Yes" and lastRecord != 0:
                result = (lastRecord * second_number)
                print(f"The result: {result} ")
            else:        
                result = (first_number * second_number)
                print(f"The result: {result} ")
            calculation_count += 1

        elif choice == "4":
            if lastResult == "Yes" and lastRecord != 0:
                if second_number != 0:
                    result = (lastRecord / second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Cannot divide by zero. ")
            else:
                if second_number != 0:
                    result = (first_number / second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Cannot divide by zero. ")

        elif choice == "5":
            if lastResult == "Yes" and lastRecord != 0:
                if second_number != 0:
                    result = (lastRecord // second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Cannot divide by zero. ")
            else:
                if second_number != 0:
                    result = (first_number // second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Cannot divide by zero. ")

        elif choice == "6":
            if lastResult == "Yes" and lastRecord != 0:
                if second_number != 0:
                    result = (lastRecord % second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Cannot mod by zero. ")
            else:
                if second_number != 0:
                    result = (first_number % second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Cannot mod by zero. ")

        elif choice == "7":
            if lastResult == "Yes" and lastRecord != 0:
                if first_number != 0 and second_number != (-1):
                    result = (lastRecord ** second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Invalid operation. Please try again. ")
            else:
                if first_number != 0 and second_number != (-1):
                    result = (first_number ** second_number)
                    print(f"The result: {result} ")
                    calculation_count += 1
                else:
                    print("Invalid operation. Please try again. ")

        lastRecord = result
    elif choice == "8":
        
        if lastRecord == 0:
            print("There was no last record")
        else:
            print(f"The last record was: {lastRecord}")

    else:
        print("Invalid operation. Please try again.")