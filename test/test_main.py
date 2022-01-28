import main

def test_potega():
    assert main.potega(0) == 0

def test_potega1():
    assert main.potega(3) == 9

def test_potega2():
    assert main.potega(-6) == 36