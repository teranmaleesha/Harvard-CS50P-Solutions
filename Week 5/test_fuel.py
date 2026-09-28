import pytest
from fuel import convert, gauge
def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99
def test_convert_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
