import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase)

    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Test Methods for Addition ---
    def test_add_positive_numbers(self):
        """Test addition with two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_add_negative_numbers(self):
        """Test addition with two negative numbers."""
        self.assertEqual(self.calc.add(-1, -5), -6)
        self.assertEqual(self.calc.add(-100, -20), -120)

    def test_add_positive_and_negative(self):
        """Test addition with a positive and a negative number."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -3), 2)
        self.assertEqual(self.calc.add(-8, 2), -6)

    def test_add_zero(self):
        """Test addition involving zero."""
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_float_numbers(self):
        """Test addition with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(1.1, 2.2), 3.3)

    # --- Test Methods for Subtraction ---
    def test_subtract_positive_numbers(self):
        """Test subtraction with two positive numbers."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_subtract_negative_numbers(self):
        """Test subtraction with two negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(-2, -5), 3)

    def test_subtract_positive_and_negative(self):
        """Test subtraction with mixed positive and negative numbers."""
        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(-5, 2), -7)

    def test_subtract_zero(self):
        """Test subtraction involving zero."""
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_float_numbers(self):
       
        self.assertEqual(self.calc.subtract(5.5, 2.0), 3.5)
        self.assertEqual(self.calc.subtract(10.0, 3.3), 6.7)

    # --- Test Methods for Multiplication ---
    def test_multiply_positive_numbers(self):
        """Test multiplication with two positive numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)

    def test_multiply_negative_numbers(self):
        """Test multiplication with two negative numbers."""
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-10, -5), 50)

    def test_multiply_positive_and_negative(self):
        """Test multiplication with mixed positive and negative numbers."""
        self.assertEqual(self.calc.multiply(5, -2), -10)
        self.assertEqual(self.calc.multiply(-5, 2), -10)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_float_numbers(self):
        """Test multiplication with floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)

    # --- Test Methods for Division ---
    def test_divide_positive_numbers(self):
        """Test division with two positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_negative_numbers(self):
        """Test division with two negative numbers."""
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(-7, -2), 3.5)

    def test_divide_positive_by_negative(self):
        """Test division of a positive by a negative number."""
        self.assertEqual(self.calc.divide(10, -2), -5.0)

    def test_divide_negative_by_positive(self):
        """Test division of a negative by a positive number."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)

    def test_divide_by_one(self):
        """Test division by one."""
        self.assertEqual(self.calc.divide(100, 1), 100.0)

    def test_divide_zero_by_number(self):
        """Test division of zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_by_zero(self):
        """Test division by zero, which should return None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Even 0/0 should return None as per method spec

    def test_divide_float_numbers(self):
        """Test division with floating-point numbers."""
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(10.0, 4.0), 2.5)

# This block allows the tests to be run when the script is executed directly
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # exit=False prevents sys.exit() if run in IDE



