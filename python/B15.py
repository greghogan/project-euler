#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright Greg Hogan, 2012. Last modified 2016.
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
    https://projecteuler.net/problem=15
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 15
19 April 2002

Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import functools

memory = {}


def recursive(m, n):
    """Compute the number of routes across a grid by recursion. Results are
    memoized in a dictionary.

    >>> iterative(2, 2)
    6
    >>> iterative(1, 20)
    21
    >>> iterative(20, 1)
    21
    >>> iterative(20, 20)
    137846528820
    """

    # when the grid has zero width then only one path exists
    if m == 0 or n == 0:
        return 1

    pair = (m, n)
    if pair in memory:
        return memory[pair]

    # sum the number of incoming paths in each direction (down and right)
    routes = recursive(m - 1, n) + recursive(m, n - 1)
    memory[pair] = routes

    return routes


def iterative(m, n):
    """Compute the number of routes across a grid by dynamic programming.

    >>> iterative(2, 2)
    6
    >>> iterative(1, 20)
    21
    >>> iterative(20, 1)
    21
    >>> iterative(20, 20)
    137846528820
    """

    # initialize only the initial state to non-zero values;
    # when the grid has zero width then only one path exists
    routes = [[1 if x == 0 or y == 0 else 0 for y in range(n + 1)] for x in range(m + 1)]

    for x in range(1, m + 1):
        for y in range(1, n + 1):
            routes[x][y] = routes[x - 1][y] + routes[x][y - 1]

    return routes[m][n]


def binomial(n, k):
    """Compute the binomial (n choose k).
    """

    return functools.reduce(lambda a, b: a*(n-b)//(b+1), range(k), 1)


def combinatorial(m, n):
    """Compute the number of routes across a grid by combinatorics.

    >>> iterative(2, 2)
    6
    >>> iterative(1, 20)
    21
    >>> iterative(20, 1)
    21
    >>> iterative(20, 20)
    137846528820
    """

    # traversal of the grid requires m + n total moves; compute the binomial
    # counting the number of permutations over m or n choices of movement in
    # each direction
    return binomial(m + n, min(m, n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
