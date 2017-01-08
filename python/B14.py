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
    https://projecteuler.net/problem=14
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 14
05 April 2002

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

memory = {1: 1}


def collatz_chain_length(number):
    """The length of the collatz chain initialized with the given number.

    >>> collatz_chain_length(2)
    2
    >>> collatz_chain_length(13)
    10
    >>> max((collatz_chain_length(x), x) for x in range(2, 10**6))[1]
    837799
    """

    if number in memory:
        return memory[number]

    if number & 1:
        next_number = 3 * number + 1
    else:
        next_number = number // 2

    memory[number] = collatz_chain_length(next_number) + 1

    return memory[number]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
