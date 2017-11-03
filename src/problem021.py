""" Amicable numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.
For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt

def sum_of_proper_divisors(num):
    """ Return the sum of the proper divisors of num.
        Iterating from 2 to the square root of n, for every divisor under
        this root has a corresponding divisor above it. Add another divisor
        in case the root is a natural number.
    """
    divisors_sum = 1 # 1 divides every num
    for i in xrange(2, int(sqrt(num)) + 1):
        if num % i == 0: divisors_sum += i + num / i
    if isinstance(sqrt(num), int): divisors_sum += sqrt(num)
    return divisors_sum

def main():
    """ Iterating over all natural numbers until N, we'll find for each number
    (a) it's sum of proper divisors (b), then add to our 'amicables' list
    a and b if they are smaller than N and not the same number.
    We'll then sum up our 'amicables' list.
    """
    N, amicables = 10000, []
    for a in xrange(N):
        if a not in amicables:
            b = sum_of_proper_divisors(a)
            if sum_of_proper_divisors(b) == a and a != b:
                if a <= N: amicables.append(a)
                if b <= N: amicables.append(b)
    print sum(amicables)

if __name__ == '__main__':
    main()