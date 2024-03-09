"""Test cases for power expression."""

# Standard library

# 3rd Party library
import pytest

# Project library
from calculator.data_type import FactExpr, Number
from calculator.data_type import PowerExpr


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "left, right, expected",
    [
        (Number(1), Number(0), 1),
        (Number(5), Number(0), 1),
        (Number(0), Number(7), 0),
        (Number(2), Number(6), 64),
        (Number(2), FactExpr(Number(3)), 64),
        (FactExpr(Number(3)), Number(2), 36),
    ]
)
def test_power_expr(left, right, expected):
    """Calculate the value of the power expression."""
    # Arrange
    expr = PowerExpr(left, right)

    # Act
    result = expr.eval()

    # Assert
    assert result == expected
