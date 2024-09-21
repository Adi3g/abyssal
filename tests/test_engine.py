import unittest

from abyssal.engine import MathEngine

class TestMathEngine(unittest.TestCase):
    """Unit tests for the MathEngine class."""
    
    def setUp(self):
        """Set up the engine instance for testing."""
        self.engine = MathEngine()

    def test_evaluate_addition(self):
        """Test evaluating a simple addition expression."""
        result = self.engine.evaluate("3 + 4", {})
        self.assertEqual(result, 7)

    def test_evaluate_with_parameters(self):
        """Test evaluating an expression with parameters."""
        result = self.engine.evaluate("x + 4", {'x': 2})
        self.assertEqual(result, 6)

    def test_evaluate_logarithmic(self):
        """Test evaluating a logarithmic expression."""
        result = self.engine.evaluate("\\ln{10}", {})
        self.assertAlmostEqual(result, 2.302585092994046, places=6)

    def test_evaluate_logarithmic(self):
        """Test evaluating a logarithmic expression."""
        result = self.engine.evaluate("\\ln{10}", {})
        self.assertAlmostEqual(result, 2.302585092994046, places=6)

    def test_evaluate_square_root(self):
        """Test evaluating a square root expression."""
        result = self.engine.evaluate("\\sqrt{16}", {})
        self.assertEqual(result, 4)

    def test_evaluate_sine(self):
        """Test evaluating a sine function."""
        result = self.engine.evaluate("\\sin{\\frac{\\pi}{2}}", {})
        self.assertAlmostEqual(result, 1.0, places=6)

    def test_evaluate_exponential(self):
        """Test evaluating an exponential function."""
        result = self.engine.evaluate("e^{2}", {})
        self.assertAlmostEqual(result, 7.38905609893065, places=6)

    def test_division_by_zero(self):
        """Test division by zero raises an appropriate exception."""
        with self.assertRaises(ZeroDivisionError):
            self.engine.evaluate("\\frac{1}{0}", {})

    def test_division_by_(self):
        """Test division exception."""
        result = self.engine.evaluate("\\frac{x}{y}", {'x': 9, 'y': 3})
        self.assertEqual(result, 3,)