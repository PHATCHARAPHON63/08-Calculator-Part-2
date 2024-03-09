"""Test cases for number."""

# Standard library

# 3rd Party library

# Project library
from calculator.data_type import Number


# -----------------------------------------------------------------------------
def test_number():
    """Calculate a number."""
    # Arrange
    value = 5
    calc = Number(value)

    # Act
    result = calc.eval()

    # Assert
    assert result == value
