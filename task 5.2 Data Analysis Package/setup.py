from setuptools import setup, find_packages

setup(
    name='data_analysis',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package for data cleaning, visualization, and statistical analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/data_analysis_package',  # Add your repository URL
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'scipy'
    ]
)
