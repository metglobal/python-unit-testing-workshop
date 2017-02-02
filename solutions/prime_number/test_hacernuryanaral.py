import pytest

from prime import is_prime


def test_is_prime_negative():
	assert is_prime(-3) == False

def test_is_prime_equal_2():
	assert is_prime(2) == True

def test_is_prime_even():
	assert is_prime(8) == False

def test_is_prime():
	assert is_prime(7) == True

def test_is_prime_str():
	with pytest.raises(TypeError):
		is_prime('83') == True