#!/usr/bin/env python

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
    https://projecteuler.net/problem=18
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 18
31 May 2002

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
"""

import os


def shortest_triangle_path(triangle, x, y):
    """Compute the shortest triangle subpath starting at (x, y) by recursion.

    >>> shortest_triangle_path([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], 0, 0)
    23
    """

    if x == len(triangle) - 1:
        # bottom row of the triangle
        return triangle[x][y]
    else:
        left = shortest_triangle_path(triangle, x + 1, y)
        right = shortest_triangle_path(triangle, x + 1, y + 1)

        return triangle[x][y] + max(left, right)


def shortest_triangle_route(filename):
    """Compute the first ten digits of the sum of numbers from the given filename.

    >>> shortest_triangle_route("B18_triangle.txt")
    1074
    """

    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        triangle = [[int(number) for number in line.split()] for line in file.readlines()]
        return shortest_triangle_path(triangle, 0, 0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
