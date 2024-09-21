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

    def test_evaluate_limit(self):
        """Test evaluating a limit expression."""
        result = self.engine.evaluate("\\lim_{x \\to 0} \\frac{\\sin{x}}{x}", {})
        self.assertEqual(result, 1.0)
