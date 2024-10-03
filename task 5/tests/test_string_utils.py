# tests/test_string_utils.py

import unittest
from my_package.string_utils import capitalize_string, reverse_string

class StringUtilsTestCase(unittest.TestCase):

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string('hello'), 'Hello')
        self.assertEqual(capitalize_string('python'), 'Python')

    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('python'), 'nohtyp')

if __name__ == '__main__':
    unittest.main()
