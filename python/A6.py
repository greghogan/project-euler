#!/usr/bin/env python

"""
Problem 6
14 December 2001

The sum of the squares of the first ten natural numbers is,
  1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
  (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def naive(n):
    """Compute the difference of the square of sums and sum of squares by
    simple summation.

    >>> naive(10)
    2640
    >>> naive(100)
    25164150
    >>> naive(1000)
    250166416500
    """

    square_of_sums = sum(range(1, n+1)) ** 2
    sum_of_squares = sum(x*x for x in range(1, n+1))

    return square_of_sums - sum_of_squares


def formula(n):
    """Compute the difference of the square of sums and sum of squares directly
    by formula.

    >>> formula(10)
    2640
    >>> formula(100)
    25164150
    >>> formula(1000)
    250166416500
    >>> formula(10000)
    2500166641665000
    """

    square_of_sums = (n * (n+1) / 2) ** 2
    sum_of_squares = (2*n + 1) * (n + 1) * n / 6

    return square_of_sums - sum_of_squares


if __name__ == "__main__":
    import doctest
    doctest.testmod()
