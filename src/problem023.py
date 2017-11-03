""" Non-abundant sums
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.
Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

from math import sqrt, ceil

def is_abundant(num):
    divisors_sum = 1 # 1 divides every num
    for i in xrange(2, int(sqrt(num))):
        if num % i == 0: divisors_sum += i + num / i
        if divisors_sum > num: return True
    if sqrt(num) ** 2 == num: divisors_sum += sqrt(num)
    return True if divisors_sum > num else False

def is_abundant_sum(num, abundants):
    for i in abundants:
        if i > num: return False
        if num - i in abundants: return True
    return False

def main():
    N = 28123
    abundants = set([num for num in xrange(2, N+1) if is_abundant(num)])
    print sum(n for n in xrange(1, N+1) if not is_abundant_sum(n, abundants))
    for i in xrange(62): print list(abundants)[i]

if __name__ == '__main__':
    main()