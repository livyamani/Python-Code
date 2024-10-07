import unittest
from my_package.string_utils import capitalize_string, reverse_string, count_vowels

class TestStringUtils(unittest.TestCase):

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string(""), "")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels(""), 0)

if __name__ == '__main__':
    unittest.main()
