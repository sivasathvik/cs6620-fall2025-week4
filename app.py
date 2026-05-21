"""Simple calculator module with basic arithmetic operations."""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation, num1, num2):
    """Perform calculation based on operation."""
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        raise ValueError(f"Unknown operation: {operation}")

    return result


if __name__ == "__main__":
    print("Simple Calculator")
    print("-" * 20)

    RESULT1 = calculate('add', 10, 5)
    print(f"10 + 5 = {RESULT1}")

    RESULT2 = calculate('multiply', 7, 3)
    print(f"7 * 3 = {RESULT2}")

    print("Calculator completed successfully!")
