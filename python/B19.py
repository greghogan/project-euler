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
    https://projecteuler.net/problem=19
licenced under a Creative Commons Licence:
    Attribution-NonCommercial-ShareAlike 2.0 UK: England & Wales

Problem 19
14 June 2002

You are given the following information, but you may prefer to do some research
for yourself.

  1 Jan 1900 was a Monday.

  Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.

  A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""


def count_1st_mondays(start_year, start_month, start_day_of_week, end_year, end_month):
    """Count the number of months where a Monday is the first day of the month.
    Months are represented as integers from January = 0 to December = 12. Days
    of the week are likewise represented from Sunday = 0 to Saturday = 6.

    >>> count_1st_mondays(1901, 0, 1, 2000, 11)
    171
    """

    year = start_year
    month = start_month
    day_of_week = start_day_of_week

    count = 0

    while year < end_year or (year == end_year and month <= end_month):
        if day_of_week == 1:
            count += 1

        if month % 12 in (0, 2, 4, 6, 7, 9, 11):
            # "all the rest"
            days_in_month = 31
        elif month % 12 in (3, 5, 8, 10):
            # September, April, June, and November
            days_in_month = 30
        else:
            # February
            days_in_month = 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28

        day_of_week = (day_of_week + days_in_month) % 7

        month += 1

        if month == 12:
            month = 0
            year += 1

    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
