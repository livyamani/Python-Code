# my_package/string_utils.py

def capitalize_string(s):
    """Capitalize the first character of a string."""
    return s.capitalize()

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in 'aeiou')
