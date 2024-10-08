from sympy import symbols, limit as sympy_limit
from .base_node import Node

class LimitNode(Node):
    """
    A node representing a limit operation.
    """
    
    def __init__(self, expression: Node, variable: str, point: float):
        """
        Initialize the node with the expression to limit, the variable, and the point to approach.

        :param expression: The expression for which the limit is being calculated.
        :param variable: The variable to which the limit is applied.
        :param point: The point to which the variable approaches.
        """
        self.expression = expression
        self.variable = variable
        self.point = point

    def evaluate(self, params: dict) -> float:
        """
        Evaluate the limit using symbolic computation.

        :param params: A dictionary mapping variable names to values.
        :return: The result of the limit operation.
        """
        # Use sympy to symbolically calculate the limit
        var = symbols(self.variable)  # Define the variable symbolically
        expr = self.expression.evaluate(params)  # Evaluate the expression without 'x'
        return float(sympy_limit(expr, var, self.point))
