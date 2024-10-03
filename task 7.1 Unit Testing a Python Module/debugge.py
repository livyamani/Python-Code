
def add(a, b):
    print(f"Debugging add: a={a}, b={b}")  # Debugging output
    result = a + b  # Perform addition
    print(f"Result of add: {result}")  # Output result for debugging
    return result


def subtract(a, b):
    print(f"Debugging subtract: a={a}, b={b}")  # Debugging output
    result = a - b  # Perform subtraction
    print(f"Result of subtract: {result}")  # Output result for debugging
    return result


def multiply(a, b):
    print(f"Debugging multiply: a={a} (type={type(a)}), b={b} (type={type(b)})")  # Debugging output
    result = a * b  # Perform multiplication
    print(f"Result of multiply: {result}")  # Output result for debugging
    return result


def divide(a, b):
    print(f"Debugging divide: a={a}, b={b}")  # Debugging output
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")  # Raise error for division by zero
    result = a / b  # Perform division
    print(f"Result of divide: {result}")  # Output result for debugging
    return result

# Function to get input for a specific operation
def get_input_for_operation(operation):
    while True:  # Loop until valid input is received
        try:
            a = float(input(f"Enter the first number for {operation}: "))
            b = float(input(f"Enter the second number for {operation}: "))
            return a, b
        except ValueError:
            print("Invalid input! Please enter numeric values.")

# Get input and perform operations
if __name__ == '__main__':
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
    try:
        division_result = divide(a, b)
        print("Result:", division_result)
    except ZeroDivisionError as e:
        print(e)  # Handle division by zero gracefully
