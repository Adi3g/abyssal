from .base_node import Node

class NumberNode(Node):
    """
    A node representing a numeric value.
    """
    
    def __init__(self, value: float):
        """
        Initialize the node with a numeric value.

        :param value: The numeric value to store.
        """
        self.value = value

    def evaluate(self, params: dict) -> float:
        """
        Evaluate the number node, which simply returns the value.

        :param params: Unused for this node type.
        :return: The numeric value stored in the node.
        """
        return self.value
