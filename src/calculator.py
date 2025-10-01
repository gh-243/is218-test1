"""Basic calculator operations used in tests and linting."""

def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return x minus y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return x / y, raising ZeroDivisionError when y == 0."""
    if y == 0:
        raise ZeroDivisionError
    return x / y
