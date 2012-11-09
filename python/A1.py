#!/usr/bin/env python

"""
Problem 1
05 October 2001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def naive():
    """Compute sum of multiples.  This runs in linear time.

    >>> naive()
    233168
    """

    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)


def quick():
    """Compute the sum of multiples in constant time.

    The multiples of 3 below 1000 are 3, 6, 9, ... 996, 999.
    The multiples of 5 below 1000 are 5, 10, 15, ... 990, 995.
    The multiples of n below 1000 are n, 2*n, 3*n, ... (n-1)*(999/n), n*(999/n)

    The sum of multiples of n below N is n*p*(p+1)/2 where p=(N-1)/n

    >>> quick()
    233168
    """

    def sum_of_multiples(N, n):
        p = (N-1) // n
        return n * p * (p+1) / 2

    return sum_of_multiples(1000, 3) + sum_of_multiples(1000, 5) - sum_of_multiples(1000, 15)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
