# my_package/file_utils.py

def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as f:
        f.write(content)

def read_file(filename):
    """Read content from a file."""
    with open(filename, 'r') as f:
        return f.read()
