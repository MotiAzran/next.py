import itertools


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    primes_gen = (x for x in itertools.count(start=n, step=1) if is_prime(x))
    return next(primes_gen)
