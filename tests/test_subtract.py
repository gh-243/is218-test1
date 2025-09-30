from calculator import subtract

def test_subtract_basic():
    assert subtract(10, 3) == 7

def test_subtract_negatives():
    assert subtract(-2, -3) == 1
