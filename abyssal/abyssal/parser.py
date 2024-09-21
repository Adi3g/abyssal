from lib2to3.pytree import Node
import re
from typing import List
from abyssal.exceptions import ParseException
from abyssal.nodes.number_node import NumberNode
from abyssal.nodes.variable_node import VariableNode
from abyssal.nodes.limit_node import LimitNode
from abyssal.nodes.operation_node import OperationNode
from abyssal.nodes.function_node import FunctionNode

class LatexParser:
    """
    Parser for converting LaTeX expressions into an AST (abstract syntax tree).
    """

    def parse(self, expression: str) -> Node:
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

    def parse_expression(self, tokens: List[str]) -> Node:
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
            elif token.isalpha():
                return VariableNode(token)
            else:
                raise ParseException(f"Invalid token: {token}")

        if tokens[0] == '\\lim':
            # Handle limits like \lim_{x \to 0} (expression)
            limit_info = self._extract_between_braces(tokens, 1)
            expression = self._extract_between_braces(tokens, limit_info['end'] + 1)

            limit_tokens = limit_info['tokens']
            var_token = limit_tokens[0]
            point_token = limit_tokens[-1]

            expression_node = self.parse_expression(expression['tokens'])
            return LimitNode(expression_node, var_token, float(point_token))

        # Handle binary operations (e.g., x + 2)
        for operator in ('^', '*', '/', '+', '-'):
            if operator in tokens:
                operator_index = tokens.index(operator)
                left = self.parse_expression(tokens[:operator_index])
                right = self.parse_expression(tokens[operator_index + 1:])
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
