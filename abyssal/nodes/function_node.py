from .base_node import Node
from abyssal.exceptions import ParseException
from math import sin, cos, log, sqrt

class FunctionNode(Node):
    """
    A node representing a mathematical function (e.g., sin, cos, ln).
    """
    
    def __init__(self, function_name: str, argument: Node):
        """
        Initialize the node with a function name and its argument.

        :param function_name: The name of the mathematical function (e.g., 'sin', 'cos', 'ln').
        :param argument: The node representing the argument of the function.
        """
        self.function_name = function_name
        self.argument = argument

    def evaluate(self, params: dict) -> float:
        """
        Evaluate the function node by evaluating the argument and applying the function.

        :param params: A dictionary mapping variable names to values.
        :return: The result of the function evaluation.
        :raises ParseException: If an unsupported function is used.
        """
        arg_value = self.argument.evaluate(params)
        if self.function_name == 'sin':
            return sin(arg_value)
        elif self.function_name == 'cos':
            return cos(arg_value)
        elif self.function_name == 'ln':
            return log(arg_value)
        elif self.function_name == 'sqrt':
            return sqrt(arg_value)
        else:
            raise ParseException(f"Unsupported function: {self.function_name}")
