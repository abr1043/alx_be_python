import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # Addition tests
    def test_add_positive_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_add_with_negatives(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertAlmostEqual(self.calc.add(-1.2, 1.2), 0.0)

    # Subtraction tests
    def test_subtract_positive_integers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtract_with_negatives(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    # Multiplication tests
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiply_with_negatives(self):
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(-3, -5), 15)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, -2), -3.0)

    # Division tests
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
 self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_with_negatives(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75)
        self.assertAlmostEqual(self.calc.divide(9, 2.5), 3.6)

    # Edge / error behavior (type errors)
    def test_non_numeric_inputs_raise(self):
        with self.assertRaises(TypeError):
            _ = self.calc.add("a", 1)
        with self.assertRaises(TypeError):
            _ = self.calc.subtract("x", 2)
        with self.assertRaises(TypeError):
            _ = self.calc.multiply(3, "y")
        with self.assertRaises(TypeError):
            _ = self.calc.divide("foo", "bar")


if __name__ == "__main__":
    unittest.main()
