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
    https://projecteuler.net/problem=1
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 1
05 October 2001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import functools
import itertools


def gcd(*integers):
    """Compute the Greatest Common Divisor of a list of integers.

    >>> gcd(5, 0)
    5
    >>> gcd(19, 21)
    1
    >>> gcd(4, 6, 8)
    2
    >>> gcd(10, 15, 20)
    5
    """

    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b

        return a

    if any(i < 0 for i in integers):
        raise Exception('GCD input must be non-negative integers')

    return functools.reduce(_gcd, integers)


def lcm(*integers):
    """Compute the Least Common Multiple of a list of integers.

    >>> lcm(5, 0)
    0
    >>> lcm(19, 21)
    399
    >>> lcm(4, 6, 8)
    24
    """

    def _lcm(a, b):
        return a * (b // gcd(a, b))

    if any(i < 0 for i in integers):
        raise Exception('LCM input must be non-negative integers')

    return functools.reduce(_lcm, integers)


def naive(n, factors):
    """Compute the sum of numbers less than n which are multiples of one or
    more factors. This runs in linear time.

    >>> naive(10, [3, 5])
    23
    >>> naive(10**5, [4, 6])
    1666583334
    >>> naive(10**5, [2, 3, 5])
    3666683332
    >>> naive(10**5, [2, 3, 5, 7])
    3857107139
    >>> naive(10**5, [7, 13, 17, 29, 31])
    1520917441
    >>> naive(10**5, range(14, 20))
    1507660080
    >>> naive(10**5, [3, 6, 9])
    1666683333
    >>> naive(10**5, [3, 3, 6, 6, 9, 9])
    1666683333
    >>> naive(1000, [3, 5])
    233168
    """

    return sum(x for x in range(n) if any(x % f == 0 for f in factors))


def inclusion_exclusion(limit, factors):
    """Compute the sum of numbers less than limit which are multiples of one or
    more factors. This runs in constant time.

    The multiples of 3 below 1000 are 3, 6, 9, ... 996, 999.
    The multiples of 5 below 1000 are 5, 10, 15, ... 990, 995.
    The multiples of n below 1000 are n, 2*n, 3*n, ... (n-1)*(999/n), n*(999/n)

    The sum of multiples of n below N is n*p*(p+1)/2 where p=(N-1)/n

    >>> inclusion_exclusion(10, [3, 5])
    23
    >>> inclusion_exclusion(10**5, [4, 6])
    1666583334
    >>> inclusion_exclusion(10**5, [2, 3, 5])
    3666683332
    >>> inclusion_exclusion(10**5, [2, 3, 5, 7])
    3857107139
    >>> inclusion_exclusion(10**5, [7, 13, 17, 29, 31])
    1520917441
    >>> inclusion_exclusion(10**5, range(14, 20))
    1507660080
    >>> inclusion_exclusion(10**5, [3, 6, 9])
    1666683333
    >>> inclusion_exclusion(10**5, [3, 3, 6, 6, 9, 9])
    1666683333
    >>> inclusion_exclusion(1000, [3, 5])
    233168
    """

    def sum_of_multiples(_limit, n):
        p = (_limit - 1) // n
        return n * p * (p + 1) // 2

    # Remove factors which are evenly divisible by another factor; this is an optimization and not required
    distinct_factors = set(factors)
    f = [x for x in distinct_factors if not any(x != y and x % y == 0 for y in distinct_factors)]

    # The inclusion-exclusion principle:  sum the multiples of each factor,
    # then subtract the sum of multiples of the LCM of each pair of factors,
    # then add the sum of multiples of the LCM of each triplet of factors, ...
    return sum((1 if k % 2 else -1) * sum(sum_of_multiples(limit, lcm(*c))
                                          for c in itertools.combinations(f, k)) for k in range(1, len(f) + 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
