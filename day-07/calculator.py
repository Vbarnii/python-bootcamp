

print("================================")
print("      PYTHON CALCULATOR v2")
print("================================")


last_record = 0
calculation_count = 0
has_last_result = False


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
    result = 0
    use_last_result = ""
    operation_successful = False

    
    

    if choice == "0":
        if calculation_count == 0:
            print("There was no  successful operation!")
        else:
            print(f"The number of successful operations: {calculation_count}")
        break
    elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":
        if has_last_result:
            use_last_result = input("Do you want to use the last result as the first number? (yes/no) ").strip().lower()
            if use_last_result == "yes":
                first_number = last_record
            elif use_last_result == "no":
                first_number = float(input("First number: "))
            else:
                print("Invalid answer. Please enter yes or no: ")
                continue
        else:
            first_number = float(input("First number: "))

        second_number = float(input("Second number: "))
        
        
        if choice == "1":
            result = first_number + second_number
            operation_successful = True
            
        elif choice == "2":
            result = first_number - second_number
            operation_successful = True
    
        elif choice == "3":       
            result = first_number * second_number
            operation_successful = True

        elif choice == "4":
            if second_number != 0:
                result = first_number / second_number
                operation_successful = True
            else:
                print("Cannot divide by zero. ")

        elif choice == "5":
            if second_number != 0:
                result = first_number // second_number
                operation_successful = True
            else:
                print("Cannot divide by zero. ")

        elif choice == "6":
            if second_number != 0:
                result = first_number % second_number
                operation_successful = True
            else:
                print("Cannot mod by zero. ")

        elif choice == "7":
            if first_number == 0 and second_number < 0:
                print("Cannot raise zero to a negative power.")
            else:   
                result = first_number ** second_number
                operation_successful = True

        if operation_successful:
            last_record = result
            has_last_result = True
            calculation_count += 1
            print(f"The result: {result}")

    elif choice == "8":
        
        if has_last_result == False:
            print("There was no last record")
        else:
            print(f"The last record was: {last_record}")

    else:
        print("Invalid operation. Please try again.")