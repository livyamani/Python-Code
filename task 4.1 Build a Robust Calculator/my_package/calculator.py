from decimal import Decimal, Overflow, DivisionByZero, InvalidOperation, getcontext
import math

# Set up a custom precision context for decimal
getcontext().prec = 28  # Default precision
getcontext().Emax = 9999  # Upper limit for exponent to simulate overflow
getcontext().Emin = -9999  # Lower limit for exponent

# Custom exception for overflow
class OverflowErrorCustom(Exception):
    def __init__(self, message="Overflow occurred during calculation."):
        self.message = message
        super().__init__(self.message)

# Custom calculator class with Decimal handling
class Calculator:
    def add(self, num1, num2):
        try:
            result = Decimal(num1) + Decimal(num2)
            return result
        except InvalidOperation:
            raise ValueError("Invalid input for addition")
        except Overflow:
            raise OverflowErrorCustom("Overflow in addition.")

    def subtract(self, num1, num2):
        try:
            result = Decimal(num1) - Decimal(num2)
            return result
        except Overflow:
            raise OverflowErrorCustom("Overflow in subtraction.")

    def multiply(self, num1, num2):
        try:
            result = Decimal(num1) * Decimal(num2)
            return result
        except Overflow:
            raise OverflowErrorCustom("Overflow in multiplication.")

    def divide(self, num1, num2):
        try:
            result = Decimal(num1) / Decimal(num2)
            return result
        except DivisionByZero:
            return "Error: Division by zero is not allowed."
        except Overflow:
            raise OverflowErrorCustom("Overflow in division.")
        except InvalidOperation:
            return "Error: Invalid operation."

    def sqrt(self, num):
        try:
            result = math.sqrt(num)
            return result
        except ValueError:
            return "Error: Square root of negative number is not defined."

    def exponentiate(self, base, exp):
        try:
            result = math.pow(base, exp)
            return result
        except OverflowError:
            raise OverflowErrorCustom("Overflow in exponentiation.")

    def logarithm(self, num, base=math.e):
        try:
            result = math.log(num, base)
            return result
        except ValueError:
            return "Error: Logarithm of a non-positive number is not defined."

# Function to display operations and take input from the user
def calculate():
    calc = Calculator()
    
    print("Please select operation -\n" \
        "+ for Addition\n" \
        "- for Subtraction\n" \
        "* for Multiplication\n" \
        "/ for Division\n" \
        "sqrt for Square Root\n" \
        "^ for Exponentiation\n" \
        "log for Logarithm (base e or specify base)\n")

    # Error handling for operation selection
    try:
        select = input("Select operation (+, -, *, /, sqrt, ^, log): ").strip()
        if select not in ['+', '-', '*', '/', 'sqrt', '^', 'log']:
            raise ValueError("Invalid operation selected.")
    except ValueError as e:
        return f"Error: {e}"

    # Error handling for numeric input
    try:
        if select == 'sqrt':
            number_1 = float(input("Enter the number for square root: "))
            result = calc.sqrt(number_1)
            return f"sqrt({number_1}) = {result}"

        elif select == '^':
            number_1 = float(input("Enter the base: "))
            number_2 = float(input("Enter the exponent: "))
            result = calc.exponentiate(number_1, number_2)
            return f"{number_1} ^ {number_2} = {result}"

        elif select == 'log':
            number_1 = float(input("Enter the number: "))
            base_input = input("Enter the base (press Enter to use default base e): ")
            if base_input == "":
                result = calc.logarithm(number_1)
                return f"log({number_1}) = {result}"
            else:
                base = float(base_input)
                result = calc.logarithm(number_1, base)
                return f"log base {base} ({number_1}) = {result}"

        else:
            # For basic arithmetic operations
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if select == '+':
                result = calc.add(number_1, number_2)
            elif select == '-':
                result = calc.subtract(number_1, number_2)
            elif select == '*':
                result = calc.multiply(number_1, number_2)
            elif select == '/':
                result = calc.divide(number_1, number_2)

            return f"{number_1} {select} {number_2} = {result}"
    
    except OverflowErrorCustom as e:
        return f"Error: {e}"
    except ValueError:
        return "Error: Invalid input, please enter valid numbers."


print(calculate())
