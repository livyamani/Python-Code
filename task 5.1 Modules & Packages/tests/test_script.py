# test_script.py
import sys
import os

# Add the parent directory to the system path so Python can find my_package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import functions from my_package
from my_package import (
    add, subtract, multiply, divide,  # From math_utils.py
    capitalize_string, reverse_string, count_vowels,  # From string_utils.py
    read_file, write_file  # From file_utils.py
)

# Test math_utils functions
print(f"5 + 3 = {add(5, 3)}")
print(f"5 - 3 = {subtract(5, 3)}")
print(f"5 * 3 = {multiply(5, 3)}")
try:
    print(f"5 / 0 = {divide(5, 0)}")
except ValueError as e:
    print(e)

# Test string_utils functions
print(f"Capitalized: {capitalize_string('hello world')}")
print(f"Reversed: {reverse_string('hello')}")
print(f"Number of vowels: {count_vowels('Hello world')}")

# Test file_utils functions
file_path = 'test_file.txt'
content = "Hello, this is a test file."
write_file(file_path, content)
print(f"File content:\n{read_file(file_path)}")
