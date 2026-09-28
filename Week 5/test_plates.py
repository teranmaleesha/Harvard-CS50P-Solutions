from plates import is_valid
def test_min_and_max_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
def test_start_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False
def test_numbers_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("hello,") == False
    assert is_valid("CS 50") == False
