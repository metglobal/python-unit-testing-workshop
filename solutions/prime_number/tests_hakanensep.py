# -*- coding: utf-8 -*-
from prime import is_prime

def test_good():
	assert is_prime(3) is True
def test_one():
	assert is_prime(1) is False
def test_string():
	assert is_prime('1') is False
def test_some():
	assert is_prime('') is False
def test_negative():
	assert is_prime(-1) is False
def test_string():
	assert is_prime("test") is False
