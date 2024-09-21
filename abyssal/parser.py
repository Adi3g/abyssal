import re
from typing import List
from abyssal.exceptions import ParseException
from abyssal.nodes.number_node import NumberNode
from abyssal.nodes.variable_node import VariableNode
from abyssal.nodes.limit_node import LimitNode
from abyssal.nodes.operation_node import OperationNode
from abyssal.nodes.function_node import FunctionNode
from abyssal.nodes.base_node import Node
import math

class LatexParser:
    """
    Parser for converting LaTeX expressions into an AST (abstract syntax tree).
    """

    def parse(self, expression: str) -> NumberNode:
        """
        Parse a LaTeX expression and return the root of the AST.

        :param expression: A LaTeX formatted mathematical expression.
        :return: The root node of the AST representing the expression.
        :raises ParseException: If the expression cannot be parsed.
        """
        tokens = self.tokenize(expression)
        return self.parse_expression(tokens)

    def tokenize(self, expression: str) -> List[str]:
        """
        Tokenize a LaTeX expression into symbols, numbers, and variables.

        :param expression: A LaTeX formatted mathematical expression.
        :return: A list of tokens.
        :raises ParseException: If the expression is invalid.
        """
        expression = expression.replace(' ', '')
        tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)|\\[a-zA-Z]+|\{|\}|\w+|\^', expression)
        if not tokens:
            raise ParseException("Invalid LaTeX expression.")
        return tokens

    def parse_expression(self, tokens: List[str]) -> NumberNode:
        """
        Parse a list of tokens into an AST node.

        :param tokens: A list of tokens representing a LaTeX expression.
        :return: The root node of the AST representing the expression.
        :raises ParseException: If the expression cannot be parsed.
        """
        if len(tokens) == 1:
            token = tokens[0]
            if token.isdigit():
                return NumberNode(float(token))
            elif token == '\\pi':
                # Handle the special constant \pi
                return NumberNode(math.pi)
            elif token.isalpha():
                return VariableNode(token)
            else:
                raise ParseException(f"Invalid token: {token}")


        if tokens[0] == '\\frac':
            # Handle fractions like \frac{numerator}{denominator}
            if len(tokens) < 6 or tokens[1] != '{' or tokens[3] != '}' or tokens[4] != '{' or tokens[6] != '}':
                raise ParseException("Expected '{' for \\frac.")

            # Extract numerator and denominator
            numerator_expr = tokens[2]
            denominator_expr = tokens[5]

            numerator_node = self.parse_expression([numerator_expr])
            denominator_node = self.parse_expression([denominator_expr])

            return OperationNode('/', numerator_node, denominator_node)

        if tokens[0] in ('\\sin', '\\cos', '\\tan', '\\ln', '\\sqrt'):
            # Handle functions like \sin{x}, \cos{x}, etc.
            function_name = tokens[0][1:]  # Remove the leading backslash
            argument_expr = self._extract_between_braces(tokens, 1)
            argument_node = self.parse_expression(argument_expr['tokens'])
            return FunctionNode(function_name, argument_node)

        if tokens[0] == 'e' and len(tokens) > 1 and tokens[1] == '^':
            # Handle exponentials like e^x
            exponent_expr = self._extract_between_braces(tokens, 2)
            exponent_node = self.parse_expression(exponent_expr['tokens'])
            return OperationNode('**', NumberNode(math.e), exponent_node)

        if tokens[0] == '\\lim':
            # Handle limits like \lim_{x \to 0} (expression)
            if tokens[1] == '_':
                limit_info = self._extract_between_braces(tokens, 2)
                expression_info = self._extract_between_braces(tokens, limit_info['end'] + 1)

                limit_tokens = limit_info['tokens']
                if len(limit_tokens) < 3 or limit_tokens[1] != '\\to':
                    raise ParseException("Expected a limit definition like 'x \\to 0'.")

                variable = limit_tokens[0]  # Variable (e.g., 'x')
                limit_point = float(limit_tokens[2])  # Point (e.g., '0')

                expression_node = self.parse_expression(expression_info['tokens'])
                return LimitNode(expression_node, variable, limit_point)

        if tokens[0] == '\\int':
            # Parse the definite integral \int_{a}^{b} expression dx
            bounds_info = self._extract_between_braces(tokens, 1)  # Extract bounds
            expression_info = self._extract_between_braces(tokens, bounds_info['end'] + 1)

            lower_bound = float(bounds_info['tokens'][0])
            upper_bound = float(bounds_info['tokens'][1])
            expr_node = self.parse_expression(expression_info['tokens'])

            return IntegralNode(expr_node, lower_bound, upper_bound)

        # Handle binary operations (e.g., x ^ 2)
        for operator in ('^', '*', '/', '+', '-'):
            if operator in tokens:
                operator_index = tokens.index(operator)
                left = self.parse_expression(tokens[:operator_index])
                right = self.parse_expression(tokens[operator_index + 1:])
                if operator == '^':
                    return OperationNode('**', left, right)  # Convert ^ to **
                return OperationNode(operator, left, right)

        raise ParseException("Unsupported or complex expression format.")

    def _extract_between_braces(self, tokens: List[str], start_index: int) -> dict:
        """
        Extract tokens between braces.

        :param tokens: The list of tokens to extract from.
        :param start_index: The index to start looking for braces.
        :return: A dictionary with extracted tokens and the end index.
        :raises ParseException: If the braces are not properly matched.
        """
        if tokens[start_index] != '{':
            raise ParseException("Expected '{'")

        end_index = start_index + 1
        brace_count = 1
        sub_tokens = []

        while end_index < len(tokens) and brace_count > 0:
            token = tokens[end_index]
            if token == '{':
                brace_count += 1
            elif token == '}':
                brace_count -= 1
            if brace_count > 0:
                sub_tokens.append(token)
            end_index += 1

        if brace_count != 0:
            raise ParseException("Unmatched braces in expression.")

        return {'tokens': sub_tokens, 'end': end_index}
