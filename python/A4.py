#!/usr/bin/env python

"""
Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
