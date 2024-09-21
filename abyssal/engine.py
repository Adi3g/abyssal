from .parser import LatexParser

class MathEngine:
    """
    Mathematical engine for evaluating LaTeX expressions.
    """
    
    def __init__(self):
        """Initialize the engine with a LaTeX parser."""
        self.parser = LatexParser()

    def evaluate(self, expression: str, params: dict) -> float:
        """
        Evaluate a LaTeX expression using provided parameters.

        :param expression: A LaTeX formatted mathematical expression.
        :param params: A dictionary of variable names and their corresponding values.
        :return: The evaluated numerical result.
        :raises ParseException: If the expression cannot be parsed or evaluated.
        """
        ast = self.parser.parse(expression)
        return ast.evaluate(params)
