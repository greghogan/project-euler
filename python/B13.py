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
    https://projecteuler.net/problem=13
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 13
22 March 2002

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

def first_10_digits_of_sum(filename):
    """ Compute the first ten digits of the sum of numbers from the given filename.

    >>> first_10_digits_of_sum("B13_numbers.txt")
    5537376230
    """

    with open(filename, 'r') as file:
        total = sum(int(line) for line in file)
        return int(str(total)[:10])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
