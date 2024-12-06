def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Division by zero"
        else:
            return a / b
    else:
        return "Invalid operation"

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the operation (+, -, *, /): ")

result = calculator(a, b, operation)
print(f"Result: {result}")
