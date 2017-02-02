from prime import is_prime
import pytest

def test_prime():
	assert is_prime(7) == True
	
def test_big_number():
    assert is_prime(1559) == True

def test_not_prime():
    assert is_prime(20) == False
