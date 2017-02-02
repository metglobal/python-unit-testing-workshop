import pytest
from prime import is_prime


def test_negative():
    assert is_prime(-2) == False

def test_zero():
    assert is_prime(0) == False

def test_less_than_two():
    assert is_prime(1) == False

def test_min_prime():
    assert is_prime(2) == True

def test_positive():
    assert is_prime(47) == True

def test_string():
    with pytest.raises(TypeError):
        is_prime('47')

def test_float():
    with pytest.raises(TypeError):
        is_prime(49.9)

