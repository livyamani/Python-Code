import unittest
import math
from my_package.calculator import Calculator, OverflowErrorCustom

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 2), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_by_zero(self):
        self.assertEqual(self.calc.divide(5, 0), "Error: Division by zero is not allowed.")

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(16), 4)
        self.assertEqual(self.calc.sqrt(-16), "Error: Square root of negative number is not defined.")

    
    def test_exponentiate(self):
        self.assertEqual(self.calc.exponentiate(2, 3), 8)
        with self.assertRaises(OverflowErrorCustom):
            self.calc.exponentiate(1e308, 2)  # Exponentiation that overflows
    
    def test_logarithm(self):
        self.assertEqual(self.calc.logarithm(10), math.log(10))  # Test base e
        self.assertEqual(self.calc.logarithm(100, 10), 2)  # Log base 10
        self.assertEqual(self.calc.logarithm(1), 0)  # log(1) = 0
        self.assertEqual(self.calc.logarithm(0), "Error: Logarithm of a non-positive number is not defined.")
        self.assertEqual(self.calc.logarithm(-1), "Error: Logarithm of a non-positive number is not defined.")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            self.calc.add("a", 5)

    def test_addition_overflow(self):
        large_num = '1e10000'  # A very large number for overflow
        with self.assertRaises(OverflowErrorCustom):
            self.calc.add(large_num, large_num)

    # Additional tests for other operations can follow...

if __name__ == '__main__':
    unittest.main()
