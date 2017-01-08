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
    https://projecteuler.net/problem=17
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 17
17 May 2002

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""


def count_letters(words):
    """Count the letters in the given words.

    >>> count_letters(["one", "two", "three", "four", "five"])
    19
    """

    return sum(len(word.replace(" ", "").replace("-", "")) for word in words)


def number_to_british(n):
    """Count the letters in the given words.

    Only numbers up to one thousand are supported as the grammar above this
    range is not defined.

    >>> number_to_british(4)
    'four'
    >>> number_to_british(30)
    'thirty'
    >>> number_to_british(33)
    'thirty-three'
    >>> number_to_british(200)
    'two hundred'
    >>> number_to_british(222)
    'two hundred and twenty-two'
    >>> number_to_british(1000)
    'one thousand'
    """

    names_by_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                       "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    names_by_tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return names_by_digits[n]

    if n < 100:
        tens = names_by_tens[n//10 - 2]
        return tens if n % 10 == 0 else tens + "-" + number_to_british(n % 10)

    if n < 1000:
        hundreds = names_by_digits[n//100] + " hundred"
        return hundreds if n % 100 == 0 else hundreds + " and " + number_to_british(n % 100)

    return "one thousand"


def count_letters_for_range(n):
    """Count the letters when writing out the numbers in the range 1 to n.

    Only numbers up to one thousand are supported as the grammar above this
    range is not defined.

    >>> count_letters_for_range(5)
    19
    >>> count_letters_for_range(1000)
    21124
    """

    return count_letters(number_to_british(num) for num in range(1, n+1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
