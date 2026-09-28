from bank import value
def test_hello():
    assert value("hello") == 0
    assert value("hello, Newman") == 0
    assert value("HELLO") == 0
def test_h_start():
    assert value("hey") == 20
    assert value("Howdy") == 20
def test_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
