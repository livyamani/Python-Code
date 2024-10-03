from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    description='A package for mathematical, string, and file utilities',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),  # Automatically find all packages
    install_requires=[],  # List external dependencies here, e.g., numpy, pandas
)
