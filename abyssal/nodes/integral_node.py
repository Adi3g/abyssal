from abyssal.nodes.base_node import Node

class IntegralNode:
    """
    A node representing a definite integral of a function over a given range.
    """

    def __init__(self, expression: Node, lower_bound: float, upper_bound: float, variable: str):
        """
        Initialize the integral node.

        :param expression: The expression to integrate.
        :param lower_bound: The lower bound of the integral.
        :param upper_bound: The upper bound of the integral.
        :param variable: The variable with respect to which the integration is done.
        """
        self.expression = expression  # The function/expression to integrate
        self.lower_bound = lower_bound  # The lower limit of integration
        self.upper_bound = upper_bound  # The upper limit of integration
        self.variable = variable  # The variable of integration

    def evaluate(self, params: dict) -> float:
        """
        Numerically evaluate the definite integral using the trapezoidal rule.

        :param params: A dictionary mapping variable names to their values.
        :return: The numerical result of the integral.
        :raises ParseException: If the variable is not found in the parameters.
        """
        num_steps = 1000  # Number of steps for numerical integration
        dx = (self.upper_bound - self.lower_bound) / num_steps
        total_area = 0.0

        # Create a copy of params to modify the integration variable value
        local_params = params.copy()

        for i in range(num_steps + 1):
            x = self.lower_bound + i * dx
            local_params[self.variable] = x
            fx = self.expression.evaluate(local_params)

            if i == 0 or i == num_steps:
                total_area += fx / 2.0  # Weight edges by half
            else:
                total_area += fx

        return total_area * dx
