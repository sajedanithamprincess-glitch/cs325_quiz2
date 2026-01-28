def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b