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
    https://projecteuler.net/problem=4
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def naive(low, high):
    """Compute all products of 3-digit numbers to find the largest palindrome.

    >>> naive(10, 99)
    9009
    >>> naive(100, 999)
    906609
    """

    largest = 0

    for x in range(low, high+1):
        for y in range(x, high+1):
            prod = x * y
            prod_str = str(prod)

            if prod_str == prod_str[::-1]:
                largest = max(largest, prod)

    return largest


def short_circuit(low, high):
    """Compute products of 3-digit numbers to find the largest palindrome,
    skipping over ranges that are too small.

    >>> short_circuit(10, 99)
    9009
    >>> short_circuit(100, 999)
    906609
    >>> short_circuit(1000, 9999)
    99000099
    >>> short_circuit(10000, 99999)
    9966006699
    """

    largest = 0

    for x in range(high, low-1, -1):
        if x * high < largest:
            break

        for y in range(high, x-1, -1):
            prod = x * y
            if prod < largest:
                break

            prod_str = str(x * y)
            if prod_str == prod_str[::-1]:
                largest = max(largest, prod)

    return largest


if __name__ == "__main__":
    import doctest
    doctest.testmod()
