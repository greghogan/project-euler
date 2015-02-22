#!/usr/bin/env python

# Copyright Greg Hogan, 2012. Last modified 2013.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but without any warranty; without even the implied warranty of
# merchantability or fitness for a particular purpose.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
The following problem is taken from Project Euler,
    https://projecteuler.net/problem=3
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 3
02 November 2001

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

def prime_generator(n=None):
    """Compute prime numbers.  If the optional integer is given, only numbers
    less than or equal to the given integer are returned.

    >>> list(prime_generator(1))
    []
    >>> list(prime_generator(2))
    [2]
    >>> list(prime_generator(100))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """

    if n and n < 2:
        return

    # Yield'ing '2' as a special case allows skipping
    # all even numbers below
    yield(2)

    odd_primes = []
    next_integer = 3

    while not n or next_integer <= n:
        is_prime = True
        square_root = int(math.sqrt(next_integer))

        for prime in odd_primes:
            # Factors must be less than or equal to the square root
            if square_root < prime:
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


def factor_list(n):
    """Compute prime factors of an integer.

    >>> factor_list(29)
    [29]
    >>> factor_list(72)
    [2, 2, 2, 3, 3]
    >>> factor_list(13195)
    [5, 7, 13, 29]
    >>> factor_list(600851475143)
    [71, 839, 1471, 6857]
    """

    factors = []

    # Use a generator to provide all potential prime divisors
    primes = prime_generator(int(math.sqrt(n)))

    try:
        while n > 1:
            p = primes.next()
            while n % p == 0:
                factors.append(p)
                n /= p
    except StopIteration:
        # The leftover quotient is prime
        factors.append(n)

    return factors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
