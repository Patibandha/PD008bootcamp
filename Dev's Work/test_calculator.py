from calculator import Operation

def test_add():
    result = Operation.add(3,2)
    assert result == 5

def test_subtract():
    result = Operation.subtract(3,2)
    assert result == 1

def test_multiply():
    result = Operation.multiply(3,2)
    assert result == 6

def test_divide():
    result = Operation.divide(4,2)
    assert result == 2