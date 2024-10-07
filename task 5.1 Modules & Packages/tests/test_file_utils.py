import unittest
import os
from my_package.file_utils import read_file, write_file

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file = 'test_file.txt'

    def tearDown(self):
        """Remove the temporary file after each test."""
        try:
            os.remove(self.test_file)
        except OSError:
            pass

    def test_write_and_read_file(self):
        """Test writing to and reading from a file."""
        content = "Hello, world!"
        write_file(self.test_file, content)
        self.assertTrue(os.path.exists(self.test_file))
        self.assertEqual(read_file(self.test_file), content)

    def test_read_non_existent_file(self):
        """Test reading a non-existent file raises FileNotFoundError."""
        with self.assertRaises(FileNotFoundError):
            read_file('non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()
