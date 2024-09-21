from .base_node import Node
from abyssal.exceptions import ParseException

class OperationNode(Node):
    """
    A node representing a binary operation (e.g., addition, subtraction).
    """
    
    def __init__(self, operator: str, left: Node, right: Node):
        """
        Initialize the node with an operator and two operand nodes.

        :param operator: The operator (e.g., '+', '-', '*', '/').
        :param left: The left operand node.
        :param right: The right operand node.
        """
        self.operator = operator
        self.left = left
        self.right = right

    def evaluate(self, params: dict) -> float:
        """
        Evaluate the binary operation by evaluating the left and right operands.

        :param params: A dictionary mapping variable names to values.
        :return: The result of the binary operation.
        :raises ParseException: If an unsupported operator is used.
        """
        left_value = self.left.evaluate(params)
        right_value = self.right.evaluate(params)
        if self.operator in ('^', '**'):  # Handle both ^ and ** for exponentiation
            return left_value ** right_value
        if self.operator == '*':
            return left_value * right_value
        if self.operator == '/':
            return left_value / right_value
        if self.operator == '+':
            return left_value + right_value
        if self.operator == '-':
            return left_value - right_value
        
        raise ParseException(f"Unsupported operator: {self.operator}")
