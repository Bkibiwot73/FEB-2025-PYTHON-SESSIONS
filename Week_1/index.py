# Basic calculator

# Ask the user to input the first number
num1 = float(input("Enter first number: "))

# Ask the user to input the second number
num2 = float(input("Enter second number: "))
operator = input("Enter operator: (+, -, *, /): ")

# Check the operator and perform the operation

if operator == "+":
    print("The sum of the two numbers is: ", num1 + num2)
elif operator == "-":
    print("The difference of the two numbers is: ", num1 - num2)
elif operator == "*":
    print("The product of the two numbers is: ", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("The division of the two numbers is: ", num1 / num2)
    else: print("Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter a valid operator.")

