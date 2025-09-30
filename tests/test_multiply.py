from calculator import multiply

def test_multiply_basic():
    assert multiply(4, 5) == 20

def test_multiply_by_zero():
    assert multiply(9, 0) == 0
