import pytest
from calculator import divide

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
