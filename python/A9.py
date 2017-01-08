#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    https://projecteuler.net/problem=9
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 9
25 January 2002

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import functools
import heapq
import itertools
import math
import operator

from A1 import gcd
from A5 import factor_map


def naive(p):
    """Exhaustively test all triangles with perimeter p, returning the product
    a * b * c for the first triangle satisfying the Pythagorean theorem.

    >>> naive(12)
    60
    >>> naive(1000)
    31875000
    """

    for c in range(p//3, (p-1)//2 + 1):
        for b in range((p-c)//2, c):
            a = p - c - b

            if a * a + b * b == c * c:
                return a * b * c


def euclid_to_triplet(m, n, scale=1):
    """Generate the Pythagorean triplet using Euclid's formula:
        a = m² - n²
        b = 2 * m * n
        c = m² + n²
    given m > n > 0.

    >>> euclid_to_triplet(2, 1)
    (3, 4, 5)
    >>> euclid_to_triplet(4, 1)
    (15, 8, 17)
    """

    if m > n > 0 and type(m) == int and type(n) == int:
        m2 = m * m
        n2 = n * n

        a = scale * (m2 - n2)
        b = scale * (2 * m * n)
        c = scale * (m2 + n2)

        return a, b, c
    else:
        raise Exception("Constraints violated for m = {m}, n = {n}".format(m=m, n=n))


def pythagorean_triplet_generator(c_max=None):
    """Generates primitive Pythagorean triplets, (a, b, c), where a < b < c,
    ordered by increasing value of c then by increasing value of a. The optional
    parameter causes termination after all triplets for which c <= c_max have
    been generated.

    >>> list(pythagorean_triplet_generator(5))
    [(3, 4, 5)]
    >>> list(pythagorean_triplet_generator(20))
    [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
    >>> list(pythagorean_triplet_generator(70))
    [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),\
 (11, 60, 61), (16, 63, 65), (33, 56, 65)]
    """

    def _push(_h, _m, _n):
        _a, _b, _c = euclid_to_triplet(_m, _n)

        if not c_max or _c <= c_max:
            heapq.heappush(_h, (_c, min(_a, _b), max(_a, _b), _m, _n))

    h = []
    _push(h, 2, 1)

    while len(h):
        c, a, b, m, n = heapq.heappop(h)

        # m and n must be relatively prime for a, b, c to be a primitive Pythagorean triplet
        if gcd(m, n) == 1:
            yield a, b, c

        # By Euclid's formula m > n and m + n must be odd
        _push(h, m + 2, n)

        # For a given m + n, c is minimized when m - n = 1, so generate the extra
        # parameter pair in this case
        if m - n == 1:
            _push(h, m + 1, n + 1)


def using_generator(p):
    """Compute the side length product and side lengths of right triangles with
    perimeter p using the generator.

    >>> using_generator(1000)
    [(31875000, 200, 375, 425)]
    >>> using_generator(123456)
    [(65334732472320, 30864, 41152, 51440)]
    >>> using_generator(1234000)
    [(58324604157144000, 234000, 472622, 527378), (59895703815000000, 246800, 462750, 524450)]
    """

    triplets = []

    c_max = p // (2 + math.sqrt(2))
    for a, b, c in pythagorean_triplet_generator(c_max + 1):
        # Check for scaled triangles of the primitive Pythagorean triplets
        div, mod = divmod(p, a + b + c)
        if mod == 0:
            triplets.append((a * b * c * (div ** 3), a * div, b * div, c * div))

    return sorted(triplets)


def divisor_list(n):
    """Return the list of divisors of the given integer.

    >>> divisor_list(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    >>> divisor_list(30850)
    [1, 2, 5, 10, 25, 50, 617, 1234, 3085, 6170, 15425, 30850]
    >>> divisor_list(math.factorial(5))
    [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
    """

    factors = factor_map(n)

    factor_powers = (tuple(factor ** exp for exp in range(multiple + 1)) for factor, multiple in factors.items())

    return sorted(functools.reduce(operator.mul, data) for data in itertools.product(*factor_powers))


def euclids_formula(p):
    """Compute the side length product and side lengths of right triangles with
    perimeter p using Euclid's formula:
        p = a + b + c = 2 * m * (m+n)

    >>> euclids_formula(1000)
    [(31875000, 200, 375, 425)]
    >>> euclids_formula(123456)
    [(65334732472320, 30864, 41152, 51440)]
    >>> euclids_formula(1234000)
    [(58324604157144000, 234000, 472622, 527378), (59895703815000000, 246800, 462750, 524450)]
    """

    triplets = set()

    # m(m+n) == p/2
    half_p = p // 2

    # Check each divisor to account for scaled triangles
    for div in divisor_list(half_p):
        mul = half_p // div

        # n = (mul - m*2) / m
        start = 1 + int(math.sqrt(mul//2))
        stop = int(math.sqrt(mul))

        for m in range(start, stop):
            n, mod = divmod(mul - m*m, m)

            if mod == 0:
                a, b, c = euclid_to_triplet(m, n, scale=div)

                triplets.add((a * b * c, min(a, b), max(a, b), c))

    return sorted(triplets)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
