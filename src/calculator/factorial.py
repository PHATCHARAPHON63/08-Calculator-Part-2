"""Calculate the factorial of a number."""

# Standard library

# 3rd Party library

# Project library


# -----------------------------------------------------------------------------
def factorial(num):
    """Calculate the factorial of num."""
    result = 1
    for value in range(1, num+1):
        result = result * value

    return result
