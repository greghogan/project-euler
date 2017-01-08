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
    https://projecteuler.net/problem=5
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 5
30 November 2001

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import collections
import math

from A3 import factor_list, prime_generator


def direct():
    """Compute product of prime factors. For each consecutive number, factors
    already listed are not considered. For example, when examining 4 = 2*2,
    the first 2 is already listed so only one additional 2 is included.

    >>> direct()
    232792560
    """

    return 2*3*2*5*7*2*3*11*13*2*17*19


def factor_map(n):
    """Compute prime factors of an integer.

    >>> factor_map(29)
    {29: 1}
    >>> factor_map(72)
    {2: 3, 3: 2}
    >>> factor_map(30850)
    {617: 1, 2: 1, 5: 2}
    """

    factors = {}
    for factor in factor_list(n):
        factors[factor] = factors.get(factor, 0) + 1

    return factors


def computed_with_factorizations(n):
    """Compute the number as the product of the union of prime factorizations.
    For each prime factor store the maximum number of occurrences in any single
    prime factorization.

    >>> computed_with_factorizations(20)
    232792560
    >>> computed_with_factorizations(40)
    5342931457063200
    >>> computed_with_factorizations(80)
    32433859254793982911622772305630400
    >>> computed_with_factorizations(160)
    117671955487901874837890815641362681946988303003141220897970719568000
    """

    prime_count = collections.defaultdict(int)

    for i in range(2, n+1):
        for factor, count in factor_map(i).items():
            if count > prime_count[factor]:
                prime_count[factor] = count

    product = 1
    for factor, count in prime_count.items():
        product *= factor ** count

    return product


def computed_with_prime_powers(n):
    """A faster method observes that for any prime number, a simple power of
    that prime number will be the smallest number with the that factorization
    count. For example, 16 is the largest power of 2 less than or equal to 20.

    >>> computed_with_prime_powers(20)
    232792560
    >>> computed_with_prime_powers(40)
    5342931457063200
    >>> computed_with_prime_powers(80)
    32433859254793982911622772305630400
    >>> computed_with_prime_powers(160)
    117671955487901874837890815641362681946988303003141220897970719568000
    """

    product = 1
    for prime in prime_generator(n):
        count = int(math.log(n, prime))
        product *= prime ** count

    return product


if __name__ == "__main__":
    import doctest
    doctest.testmod()
