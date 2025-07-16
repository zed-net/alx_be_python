num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Use a match-case statement to perform the selected operation.
# This is a structured way to handle different cases based on the 'operation' variable.
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        # Handle division by zero gracefully.
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _: # This is the default case, matching any other input for 'operation'.
        print("Invalid operation. Please choose from +, -, *, or /.")