def calculator():
    #Get user input for two numbers
    firstNumber = int(input("Enter First Number:"))
    secondNumber = int(input("Enter Second Number:"))
    
    #Get user input for operator
    operator = input("Enter Operator (+, -, *, /):")
    
    #Perform calculations based on the operator
    if operator == '+':
        result = firstNumber + secondNumber
    elif operator == '-':
        result = firstNumber - secondNumber
    elif operator == '*':
        result = firstNumber * secondNumber
    elif operator == '/':
        # Check for division by zero
        if secondNumber == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = firstNumber / secondNumber
    else:
        print("Error: Invalid operator. Please enter a valid operator (+, -, *, /).")
        return
    # Display the result
    print(f"{firstNumber} {operator} {secondNumber} = {result}")
    
#Calling the function
calculator()    