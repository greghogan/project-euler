#!/usr/bin/env python

"""
Problem 3
02 November 2001

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

def prime_generator(n):
    """Compute prime numbers less than or equal to the given integer.

    >>> list(prime_generator(1))
    []
    >>> list(prime_generator(2))
    [2]
    >>> list(prime_generator(100))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """

    if n < 2:
        return

    # Yield'ing '2' as a special case allows skipping
    # all even numbers below
    yield(2)

    odd_primes = []
    next_integer = 3

    while next_integer <= n:
        is_prime = True

        for prime in odd_primes:
            # Factors must be less than the square root
            if next_integer < prime * prime:
                break

            # Composite if evenly divisible
            if next_integer % prime == 0:
                is_prime = False
                break

        if is_prime:
            # Yield and store the prime number
            yield(next_integer)
            odd_primes.append(next_integer)

        # Skip even numbers
        next_integer += 2


def factor(n):
    """Compute prime factors of an integer.

    >>> factor(29)
    [29]
    >>> factor(13195)
    [5, 7, 13, 29]
    >>> factor(600851475143)
    [71, 839, 1471, 6857]
    """

    factors = []

    # Use a generator to provide all potential prime divisors
    primes = prime_generator(int(math.sqrt(n)))

    try:
        while n > 1:
            p = primes.next()
            if n % p == 0:
                factors.append(p)
                n /= p
    except StopIteration:
        # The leftover quotient is prime
        factors.append(n)

    return factors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
