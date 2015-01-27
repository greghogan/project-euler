#!/usr/bin/env python

"""
Problem 7
28 December 2001

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10,001st prime number?
"""

import A3

def find_nth_prime(n):
    """Compute the nth prime number using an unbounded prime generator.

    >>> find_nth_prime(6)
    13
    >>> find_nth_prime(101)
    547
    >>> find_nth_prime(10001)
    104743
    """

    primes = A3.prime_generator()

    for x in range(n):
        prime = primes.next()

    return prime


if __name__ == "__main__":
    import doctest
    doctest.testmod()
