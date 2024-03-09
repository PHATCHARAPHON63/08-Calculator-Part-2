"""The data types for the calculator."""

# Standard library

# 3rd Party library

# Project library
from calculator.factorial import factorial


# -----------------------------------------------------------------------------
class Number:
    """The number representation."""

    def __init__(self, value):
        """Construct a Number expression."""
        self.value = value

    def eval(self):
        """Calculate the value of the number expression."""
        return self.value


# -----------------------------------------------------------------------------
class FactExpr:
    """The representation of Factorial expression"""

    def __init__(self, operand):
        """Construct a Factorial expression."""
        self.operand = operand

    def eval(self):
        """Calculate the value of the Factorial expression."""
        return factorial(self.operand.eval())


# -----------------------------------------------------------------------------
class PowerExpr:
    """The representation of Power expression"""

    def __init__(self, left, right):
        """Construct a Power expression."""
        self.left = left
        self.right = right

    def eval(self):
        """Calculate the value of the Factorial expression."""
        return self.left.eval() ** self.right.eval()


# -----------------------------------------------------------------------------
class UnaryExpr:
    """The representation of Unary expression"""

    def __init__(self, operator, operand):
        """Construct a Unary expression."""
        self.operator = operator
        self.operand = operand

    def eval(self):
        """Calculate the value of the Unary expression."""
        if self.operator == "-":
            return - self.operand.eval()
        else:
            return self.operand.eval()


