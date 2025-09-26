def perform_operation(num1, num2, operation):

    #parameters to use and works as an input the get user input :

    # num1 = float(input("What is the first  number used "))
    # num2 = float(input("What is the second number used "))
    # operation_value = input("What is the value? 'add', 'subtract', 'multiply', 'divide' ").lower()

    result = None

    if operation == "add":
        result = num1 + num2
    elif operation== "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            result = "You cannot divide by zero (0)"
        else:
            result = num1 / num2
    else:
        result = "Invalid operation used"



    return result
