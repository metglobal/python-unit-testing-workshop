from prime import is_prime
import pytest


# some code testing is_prime...
def test_negative():
    assert is_prime(-4) is False


def test_prime():
    assert is_prime(67) is True


def test_not_prime():
    assert is_prime(1000) is False


def test_big_number():
    assert is_prime(1000000) is False


# This should fail
def test_invalid_input():
    with pytest.raises(TypeError):
        assert is_prime("13") is True
