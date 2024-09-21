class Node:
    """
    Base class for nodes in the abstract syntax tree (AST).
    """
    
    def evaluate(self, params: dict) -> float:
        """
        Evaluate the node using given parameters.

        :param params: A dictionary mapping variable names to values.
        :return: The evaluated result of the node.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
