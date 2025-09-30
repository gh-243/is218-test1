from calculator import add

def test_add_positive_integers():
    assert add(2, 3) == 5

def test_add_floats():
    assert add(2.5, 0.5) == 3.0

def test_add_negatives():
    assert add(-2, -3) == -5
