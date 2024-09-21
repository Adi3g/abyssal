import unittest
from abyssal.exceptions import ParseException
from abyssal.parser import LatexParser

class TestLatexParser(unittest.TestCase):
    """Unit tests for the LatexParser class."""
    
    def setUp(self):
        """Set up the parser instance for testing."""
        self.parser = LatexParser()

    def test_simple_addition(self):
        """Test simple addition parsing."""
        node = self.parser.parse("3 + 4")
        self.assertEqual(node.evaluate({}), 7)

    def test_variable_substitution(self):
        """Test parsing with variable substitution."""
        node = self.parser.parse("x + 4")
        self.assertEqual(node.evaluate({'x': 3}), 7)

    def test_parse_exception(self):
        """Test that a parse exception is raised for invalid expressions."""
        with self.assertRaises(ParseException):
            self.parser.parse("invalid_expression")
