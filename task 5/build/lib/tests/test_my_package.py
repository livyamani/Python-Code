from my_package.math_utils import MathUtils
from my_package.string_utils import StringUtils
from my_package.file_utils import write_file, read_file

# Math utilities
math = MathUtils()
print(math.add(5, 3))  # Output: 8
print(math.divide(10, 2))  # Output: 5.0

# String utilities
string_utils = StringUtils()
print(string_utils.capitalize_string('hello'))  # Output: Hello
print(string_utils.reverse_string('world'))  # Output: dlrow

# File utilities
write_file('example.txt', 'Hello, World!')
print(read_file('example.txt'))  # Output: Hello, World!
