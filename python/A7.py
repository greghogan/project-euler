#!/usr/bin/env python

# Copyright Greg Hogan, 2012. Last modified 2015.
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
    https://projecteuler.net/problem=7
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

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
