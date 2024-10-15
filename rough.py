# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Input the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculation
if operation == '+':
    result = num1 + num2
    print("The result is:", result)
elif operation == '-':
    result = num1 - num2
    print("The result is:", result)
elif operation == '*':
    result = num1 * num2
    print("The result is:", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
