from .base_node import Node
from abyssal.exceptions import ParseException

class VariableNode(Node):
    """
    A node representing a variable.
    """
    
    def __init__(self, name: str):
        """
        Initialize the node with a variable name.

        :param name: The name of the variable.
        """
        self.name = name

    def evaluate(self, params: dict) -> float:
        """
        Evaluate the variable node by looking up its value in the given parameters.

        :param params: A dictionary mapping variable names to their values.
        :return: The value of the variable.
        :raises ParseException: If the variable is not found in the parameters.
        """
        if self.name in params:
            return params[self.name]
        raise ParseException(f"Variable '{self.name}' not found in parameters.")
