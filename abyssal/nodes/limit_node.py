import math

from abyssal.exceptions import ParseException

from .base_node import Node

class LimitNode(Node):
    """
    A node representing a limit operation.
    """

    def __init__(self, expression: Node, variable: str, point: float):
        """
        Initialize the limit node.

        :param expression: The expression to compute the limit for.
        :param variable: The variable approaching the limit.
        :param point: The point the variable is approaching (e.g., 0, ∞, etc.).
        """
        self.expression = expression
        self.variable = variable
        self.point = point

    def evaluate(self, params: dict) -> float:
        """
        Evaluate the limit by approaching the point using a small delta for higher precision.

        :param params: A dictionary mapping variable names to values.
        :return: The result of the limit operation.
        """
        delta = 1e-8  # Small step size for precision

        # Special handling for infinity limits
        if self.point == float('inf') or self.point == float('-inf'):
            return self._evaluate_infinity_limit(params)

        local_params = params.copy()

        # Approach the limit point from both sides
        local_params[self.variable] = self.point - delta
        left_limit = self.expression.evaluate(local_params)

        local_params[self.variable] = self.point + delta
        right_limit = self.expression.evaluate(local_params)

        # Check if the limits from both sides are sufficiently close
        if abs(left_limit - right_limit) < 1e-6:
            return (left_limit + right_limit) / 2
        else:
            raise ParseException(f"Limit at {self.point} does not exist or is undefined.")

    def _evaluate_infinity_limit(self, params: dict) -> float:
        """
        Evaluate the limit as the variable approaches infinity or negative infinity.
        """
        large_value = 1e8  # Large value to approximate infinity
        local_params = params.copy()

        if self.point == float('inf'):
            # Approach positive infinity
            local_params[self.variable] = large_value
        else:
            # Approach negative infinity
            local_params[self.variable] = -large_value

        return self.expression.evaluate(local_params)
