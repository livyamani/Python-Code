import unittest
import os
from my_package.file_utils import read_file, write_file

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file = 'test_file.txt'

    def tearDown(self):
        # Remove the temporary file after each test
        try:
            os.remove(self.test_file)
        except OSError:
            pass

    def test_write_file(self):
        content = "Hello, world!"
        write_file(self.test_file, content)

        # Verify that the file has been created and contains the correct content
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            file_content = f.read()
            self.assertEqual(file_content, content)

    def test_read_file(self):
        content = "Testing read functionality."
        write_file(self.test_file, content)

        # Verify that read_file returns the correct content
        result = read_file(self.test_file)
        self.assertEqual(result, content)

    def test_read_non_existent_file(self):
        # Test reading a non-existent file should raise an IOError
        with self.assertRaises(FileNotFoundError):
            read_file('non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()
