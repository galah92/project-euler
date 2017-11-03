""" Counting Sundays
You are given the following information, but you may prefer to do some
esearch for yourself.
- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date

def main():
    """ Iterating over the desired dates where day of month is the 1st,
    we'll check, using Python's 'datetime' module, if we get Sundays and
    increment accordingly.
    """
    num_of_sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if date(year, month, 1).weekday() == 6: num_of_sundays += 1
    print num_of_sundays

if __name__ == '__main__':
    main()