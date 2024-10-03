# my_package/string_utils.py

class StringUtils:
    @staticmethod
    def capitalize_string(s):
        return s.capitalize()

    @staticmethod
    def reverse_string(s):
        return s[::-1]

    @staticmethod
    def count_vowels(s):
        return sum(1 for char in s.lower() if char in 'aeiou')
