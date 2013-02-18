#!/usr/bin/env python

"""
Problem 1
05 October 2001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import itertools

def gcd(*integers):
    """Compute the Greatest Common Divisor of a list of integers.

    >>> gcd(5, 0)
    5
    >>> gcd(19, 21)
    1
    >>> gcd(4, 6, 8)
    2
    >>> gcd(10, 15, 20)
    5
    """

    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b

        return a

    if any(i < 0 for i in integers):
        raise Exception('GCD input must be non-negative integers')

    return reduce(_gcd, integers)


def lcm(*integers):
    """Compute the Least Common Multiple of a list of integers.

    >>> lcm(5, 0)
    0
    >>> lcm(19, 21)
    399
    >>> lcm(4, 6, 8)
    24
    """

    def _lcm(a, b):
        return a * (b / gcd(a, b))

    if any(i < 0 for i in integers):
        raise Exception('LCM input must be non-negative integers')

    return reduce(_lcm, integers)


def naive(n, factors):
    """Compute the sum of numbers less than n which are multiples of factors.
    This runs in linear time.

    >>> naive(10, [3, 5])
    23
    >>> direct(10**5, [4, 6])
    1666583334
    >>> naive(10**5, [2, 3, 5])
    3666683332
    >>> naive(10**5, [2, 3, 5, 7])
    3857107139
    >>> naive(10**5, [7, 13, 17, 29, 31])
    1520917441
    >>> naive(10**5, range(14, 20))
    1507660080
    >>> naive(10**5, [3, 6, 9])
    1666683333
    >>> naive(1000, [3, 5])
    233168
    """

    return sum(x for x in range(n) if any(x % f == 0 for f in factors))


def direct(n, factors):
    """Compute the sum of numbers less than n which are multiples of factors.
    This runs in constant time.

    The multiples of 3 below 1000 are 3, 6, 9, ... 996, 999.
    The multiples of 5 below 1000 are 5, 10, 15, ... 990, 995.
    The multiples of n below 1000 are n, 2*n, 3*n, ... (n-1)*(999/n), n*(999/n)

    The sum of multiples of n below N is n*p*(p+1)/2 where p=(N-1)/n

    >>> direct(10, [3, 5])
    23
    >>> direct(10**5, [4, 6])
    1666583334
    >>> direct(10**5, [2, 3, 5])
    3666683332
    >>> direct(10**5, [2, 3, 5, 7])
    3857107139
    >>> direct(10**5, [7, 13, 17, 29, 31])
    1520917441
    >>> direct(10**5, range(14, 20))
    1507660080
    >>> direct(10**5, [3, 6, 9])
    1666683333
    >>> direct(1000, [3, 5])
    233168
    """

    def sum_of_multiples(N, n):
        p = (N-1) // n
        return n * p * (p+1) / 2

    # Remove factors which are evenly divisible by another factor; this is an optimization and not required
    f = [x for x in factors if not any(x != y and x % y == 0 for y in factors)]

    # The inclusion-exclusion principle:  sum the multiples of each factor,
    # then substract the sum of multiples of the LCM of each pair of factors,
    # then add the sum of multiples of the LCM of each triplet of factors, ...
    return sum((1 if k % 2 else -1) * sum(sum_of_multiples(n, lcm(*c)) for c in itertools.combinations(f, k)) for k in range(1, len(f) + 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
