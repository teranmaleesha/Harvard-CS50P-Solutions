import pytest
from um import count
def test_single_um():
    assert count("hello, um, world") == 1
    assert count("um") == 1
def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1
    assert count("UM, um, Um") == 3
def test_word_with_um():
    assert count("yummy") == 0
    assert count("instrumentation") == 0
def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("Hello, um... world!") == 1
