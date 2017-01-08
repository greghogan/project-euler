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
    https://projecteuler.net/problem=21
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 21
5 July 2002

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from A9 import divisor_list


def amicable_numbers(limit):
    """Find all amicable numbers from 2 to limit, inclusive.

    >>> sum(amicable_numbers(10000))
    31626
    """

    amicable = set()

    for number in range(2, limit):
        if number in amicable:
            continue

        # sum all divisors except the number itself
        sum_of_divisors = sum(divisor_list(number)) - number

        if number != sum_of_divisors > 1:
            sum_of_sum_of_divisors_divisors = sum(divisor_list(sum_of_divisors)) - sum_of_divisors

            # amicable if and only if a = d(d(a))
            if number == sum_of_sum_of_divisors_divisors:
                amicable.add(number)
                amicable.add(sum_of_divisors)

    return amicable


if __name__ == "__main__":
    import doctest
    doctest.testmod()
