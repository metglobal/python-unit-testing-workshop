def is_prime(number):
    """
    Checks a number is a prime or not.
    Returns bool.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
