"""Test cases for factorial operation."""

# Standard library

# 3rd Party library
import pytest

# Project library
from calculator.factorial import factorial
from calculator.data_type import FactExpr, Number


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "num, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
    ]
)
def test_factorial(num, expected):
    """Calculate the factorial of num."""
    # Arrange
    # Act
    result = factorial(num)

    # Assert
    assert result == expected


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "fact_term, expected_result",
    [
        (Number(5), 5),
        (FactExpr(Number(0)), 1),
        (FactExpr(Number(1)), 1),
        (FactExpr(Number(2)), 2),
        (FactExpr(Number(3)), 6),
        (FactExpr(Number(4)), 24),
        (FactExpr(Number(5)), 120),
        (FactExpr(Number(6)), 720),

        # FactExpr of FactExpr
        (FactExpr(FactExpr(Number(3))), 720),

    ]
)
def test_factorial_term(fact_term, expected_result):
    """Calculate the value of the factorial term."""
    # Arrange
    # Act
    result = fact_term.eval()

    # Assert
    assert result == expected_result
