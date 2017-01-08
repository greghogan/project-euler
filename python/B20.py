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
    https://projecteuler.net/problem=20
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 20
21 June 2002

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math


def sum_of_digits(n):
    """Compute the sum of the digits in the given number.

    >>> sum_of_digits(math.factorial(10))
    27
    >>> sum_of_digits(math.factorial(100))
    648
    """

    return sum(int(d) for d in str(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
