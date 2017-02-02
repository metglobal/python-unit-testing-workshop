from prime import is_prime

def test_less_than_two():
	assert is_prime(1) is False

def test_greater_than_two_or_equal_two():
	assert is_prime(2) is True
	assert is_prime('prime') is False
	assert is_prime(12) is False
	assert is_prime(23) is True
