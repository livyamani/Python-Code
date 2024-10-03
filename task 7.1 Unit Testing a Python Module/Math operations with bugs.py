def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Division by zero is not valid")
        return None
    return a / b

# Function to get input for a specific operation
def get_input_for_operation(operation):
    try:
        a = float(input(f"Enter the first number for {operation}: "))
        b = str(input(f"Enter the second number for {operation}: "))
        return a, b
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None

# Get input and perform operations
print("Addition")
a, b = get_input_for_operation("addition")
print("Result:", add(a, b))

print("\nSubtraction")
a, b = get_input_for_operation("subtraction")
print("Result:", subtract(a, b))

print("\nMultiplication")
a, b = get_input_for_operation("multiplication")
print("Result:", multiply(a, b))

print("\nDivision")
a, b = get_input_for_operation("division")
print("Result:", divide(a, b))
