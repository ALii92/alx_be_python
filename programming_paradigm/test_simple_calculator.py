from simple_calculator import SimpleCalculator 
import unittest


class TestSimpleCalculator(unittest.TestCase):
    def test_addition(self):
        result = SimpleCalculator.add(5, 3)
        self.assertEqual(self.calc.add)
    def test_subtraction(self):
        result = SimpleCalculator.subtract(5, 3)
        self.assertEqual(self.calc.subtract) 
    def test_multiplication(self):
        result = SimpleCalculator.multiply(5, 3)
        self.assertEqual(self.calc.multiply)
    def test_division(self, a, b):
        assert b != 0, "Error: Division by zero!"
    def test_division(self):
        self.assertEqual(self.calc.divide)

    SimpleCalculator()
