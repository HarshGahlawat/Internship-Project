def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y
def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        return "Error: Invalid input! Please enter numeric values."
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    if choice == '1':
        result = add(num1, num2)
        operation = "addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "division"
    else:
        return "Error: Invalid choice! Please select a valid operation."
    return f"The result of the {operation} is: {result}"
if __name__ == "__main__":
    print(calculator())
