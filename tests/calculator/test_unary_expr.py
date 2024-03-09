"""Test cases for Unary Expression."""

# Standard library

# 3rd Party library
import pytest

# Project library
from calculator.data_type import FactExpr, Number
from calculator.data_type import PowerExpr
from calculator.data_type import UnaryExpr


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        ("-", Number(3), -3),
        ("+", Number(7), 7),
        ("-", FactExpr(Number(3)), -6),
        ("+", FactExpr(Number(4)), 24),
        ("-", PowerExpr(Number(3), Number(2)), -9),
    ]
)
def test_unary_expr(operator, operand, expected):
    """Calculate the value of the unary expression."""
    # Arrange
    expr = UnaryExpr(operator, operand)

    # Act
    result = expr.eval()

    # Assert
    assert result == expected
